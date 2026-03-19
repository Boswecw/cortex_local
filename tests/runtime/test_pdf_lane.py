from __future__ import annotations

import copy
import unittest
from pathlib import Path
from unittest.mock import patch

from cortex_runtime.extraction_emission import (
    emit_extraction_result_from_intake_payload,
    emit_extraction_result_from_source_file,
    pdf_lane_runtime_available,
)
from cortex_runtime.retrieval_package_emission import emit_retrieval_package_from_source_file
from tests.runtime.runtime_test_support import (
    ROOT,
    assert_schema_valid,
    build_file_intake_payload,
)

PDF_TEXT_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note.pdf"
PDF_ENCRYPTED_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note-encrypted.pdf"
PDF_SCANNED_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note-scanned.pdf"
PDF_PARTIAL_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note-partial.pdf"
PDF_CORRUPT_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note-corrupt.pdf"


def build_pdf_intake_payload(path: Path) -> dict[str, object]:
    return copy.deepcopy(build_file_intake_payload(path, "application/pdf"))


@unittest.skipUnless(pdf_lane_runtime_available(), "bounded local PDF tooling is not available")
class PdfLaneRuntimeTests(unittest.TestCase):
    def test_text_pdf_intake_emits_ready_extraction_result(self) -> None:
        result = emit_extraction_result_from_intake_payload(build_pdf_intake_payload(PDF_TEXT_FIXTURE))

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "ready")
        self.assertEqual(result["completeness"]["status"], "complete")
        self.assertEqual(result["structures"]["metadata_fields"]["source_lane"], "pdf_text")
        self.assertEqual(result["structures"]["metadata_fields"]["pdf_page_count"], "1")
        self.assertEqual(len(result["structures"]["content_blocks"]), 2)
        self.assertNotIn("sections", result["structures"])

    def test_pdf_extraction_is_deterministic(self) -> None:
        first = emit_extraction_result_from_source_file(
            PDF_TEXT_FIXTURE,
            request_id="pdf-det-001",
            source_ref="pdf-det",
            media_type="application/pdf",
        )
        second = emit_extraction_result_from_source_file(
            PDF_TEXT_FIXTURE,
            request_id="pdf-det-001",
            source_ref="pdf-det",
            media_type="application/pdf",
        )

        assert_schema_valid(self, first, schema_name="extraction-result.schema.json")
        assert_schema_valid(self, second, schema_name="extraction-result.schema.json")
        self.assertEqual(first["structures"], second["structures"])

    def test_partial_pdf_emits_partial_success(self) -> None:
        result = emit_extraction_result_from_source_file(
            PDF_PARTIAL_FIXTURE,
            request_id="pdf-partial-001",
            source_ref="pdf-partial",
            media_type="application/pdf",
        )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "partial_success")
        self.assertEqual(result["completeness"]["status"], "incomplete")
        self.assertEqual(result["structures"]["metadata_fields"]["pdf_page_count"], "2")
        self.assertEqual(result["structures"]["metadata_fields"]["extractable_text_pages"], "1")

    def test_encrypted_pdf_is_denied(self) -> None:
        result = emit_extraction_result_from_source_file(
            PDF_ENCRYPTED_FIXTURE,
            request_id="pdf-enc-001",
            source_ref="pdf-encrypted",
            media_type="application/pdf",
        )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "denied")
        self.assertEqual(result["refusal"]["reason_class"], "unsupported_source_type")

    def test_scanned_pdf_is_denied(self) -> None:
        result = emit_extraction_result_from_source_file(
            PDF_SCANNED_FIXTURE,
            request_id="pdf-scan-001",
            source_ref="pdf-scanned",
            media_type="application/pdf",
        )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "denied")
        self.assertEqual(result["refusal"]["reason_class"], "unsupported_source_type")

    def test_corrupt_pdf_is_unavailable(self) -> None:
        result = emit_extraction_result_from_source_file(
            PDF_CORRUPT_FIXTURE,
            request_id="pdf-bad-001",
            source_ref="pdf-corrupt",
            media_type="application/pdf",
        )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "unavailable")
        self.assertEqual(result["refusal"]["reason_class"], "dependency_unavailable")

    def test_pdfinfo_page_count_anomaly_is_unavailable(self) -> None:
        with patch("cortex_runtime.source_lanes.source_lane_slice_available", return_value=True), patch(
            "cortex_runtime.extraction_emission.pdf_lane_runtime_available",
            return_value=True,
        ), patch(
            "cortex_runtime.extraction_emission.subprocess.run",
            return_value=type(
                "CompletedProcess",
                (),
                {
                    "returncode": 0,
                    "stdout": "Pages: not-a-number\nEncrypted: no\n",
                    "stderr": "",
                },
            )(),
        ):
            result = emit_extraction_result_from_source_file(
                PDF_TEXT_FIXTURE,
                request_id="pdf-anomaly-001",
                source_ref="pdf-anomaly",
                media_type="application/pdf",
            )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "unavailable")
        self.assertEqual(result["refusal"]["reason_class"], "dependency_unavailable")

    def test_pdftotext_anomaly_is_unavailable(self) -> None:
        def run_side_effect(command: list[str], **_kwargs: object) -> object:
            if command[0] == "pdfinfo":
                return type(
                    "CompletedProcess",
                    (),
                    {
                        "returncode": 0,
                        "stdout": "Pages: 1\nEncrypted: no\n",
                        "stderr": "",
                    },
                )()
            return type(
                "CompletedProcess",
                (),
                {
                    "returncode": 1,
                    "stdout": "",
                    "stderr": "syntax error in xref table",
                },
            )()

        with patch("cortex_runtime.source_lanes.source_lane_slice_available", return_value=True), patch(
            "cortex_runtime.extraction_emission.pdf_lane_runtime_available",
            return_value=True,
        ), patch("cortex_runtime.extraction_emission.subprocess.run", side_effect=run_side_effect):
            result = emit_extraction_result_from_source_file(
                PDF_TEXT_FIXTURE,
                request_id="pdf-anomaly-002",
                source_ref="pdf-anomaly-2",
                media_type="application/pdf",
            )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "unavailable")
        self.assertEqual(result["refusal"]["reason_class"], "dependency_unavailable")

    def test_ready_pdf_extraction_is_retrieval_compatible(self) -> None:
        result = emit_retrieval_package_from_source_file(
            PDF_TEXT_FIXTURE,
            request_id="pdf-ret-001",
            source_ref="pdf-ret",
            media_type="application/pdf",
        )

        assert_schema_valid(self, result, schema_name="retrieval-package.schema.json")
        self.assertEqual(result["state"], "ready")
        self.assertEqual(result["retrieval_profile"]["chunking_mode"], "paragraph")
        self.assertEqual([chunk["ordinal"] for chunk in result["chunks"]], [0, 1])
        self.assertEqual({chunk["structure_kind"] for chunk in result["chunks"]}, {"paragraph"})


if __name__ == "__main__":
    unittest.main()
