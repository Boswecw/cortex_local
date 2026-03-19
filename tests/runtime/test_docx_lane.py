from __future__ import annotations

import copy
import tempfile
import unittest
import zipfile
from pathlib import Path

from cortex_runtime.extraction_emission import emit_extraction_result_from_intake_payload
from cortex_runtime.extraction_emission import emit_extraction_result_from_source_file
from cortex_runtime.retrieval_package_emission import emit_retrieval_package_from_source_file
from tests.runtime.runtime_test_support import (
    ROOT,
    assert_schema_valid,
    build_file_intake_payload,
)

DOCX_READY_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note.docx"
DOCX_REVIEWED_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note-reviewed.docx"
DOCX_CORRUPT_FIXTURE = ROOT / "tests/runtime/fixtures/sample-note-corrupt.docx"


def build_docx_intake_payload(path: Path) -> dict[str, object]:
    return copy.deepcopy(
        build_file_intake_payload(
            path,
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    )


def write_docx(path: Path, document_xml: str, *, comments_xml: str | None = None) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("word/document.xml", document_xml)
        if comments_xml is not None:
            archive.writestr("word/comments.xml", comments_xml)


class DocxLaneRuntimeTests(unittest.TestCase):
    def test_docx_intake_emits_ready_extraction_result(self) -> None:
        result = emit_extraction_result_from_intake_payload(build_docx_intake_payload(DOCX_READY_FIXTURE))

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "ready")
        self.assertEqual(result["completeness"]["status"], "complete")
        self.assertEqual(result["structures"]["metadata_fields"]["source_lane"], "docx_text")
        self.assertEqual(len(result["structures"]["sections"]), 2)
        self.assertEqual(result["structures"]["tables_detected"], 1)
        self.assertEqual(
            {block["block_kind"] for block in result["structures"]["content_blocks"]},
            {"heading", "paragraph", "list", "table"},
        )

    def test_docx_extraction_is_deterministic(self) -> None:
        first = emit_extraction_result_from_source_file(
            DOCX_READY_FIXTURE,
            request_id="docx-det-001",
            source_ref="docx-det",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
        second = emit_extraction_result_from_source_file(
            DOCX_READY_FIXTURE,
            request_id="docx-det-001",
            source_ref="docx-det",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

        assert_schema_valid(self, first, schema_name="extraction-result.schema.json")
        assert_schema_valid(self, second, schema_name="extraction-result.schema.json")
        self.assertEqual(first["structures"], second["structures"])

    def test_reviewed_docx_is_denied(self) -> None:
        result = emit_extraction_result_from_source_file(
            DOCX_REVIEWED_FIXTURE,
            request_id="docx-denied-001",
            source_ref="docx-reviewed",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "denied")
        self.assertEqual(result["refusal"]["reason_class"], "unsupported_source_type")

    def test_corrupt_docx_is_unavailable(self) -> None:
        result = emit_extraction_result_from_source_file(
            DOCX_CORRUPT_FIXTURE,
            request_id="docx-bad-001",
            source_ref="docx-corrupt",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "unavailable")
        self.assertEqual(result["refusal"]["reason_class"], "dependency_unavailable")

    def test_non_heading_styles_are_not_promoted_to_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            source_path = Path(tmpdir) / "style-only.docx"
            write_docx(
                source_path,
                """
                <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
                  <w:body>
                    <w:p>
                      <w:pPr><w:pStyle w:val="TitleLike"/></w:pPr>
                      <w:r><w:t>Not a heading</w:t></w:r>
                    </w:p>
                    <w:p><w:r><w:t>Body paragraph.</w:t></w:r></w:p>
                  </w:body>
                </w:document>
                """,
            )

            result = emit_extraction_result_from_source_file(
                source_path,
                request_id="docx-style-001",
                source_ref="docx-style",
                media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "ready")
        self.assertNotIn("sections", result["structures"])
        self.assertEqual(
            [block["block_kind"] for block in result["structures"]["content_blocks"]],
            ["paragraph", "paragraph"],
        )

    def test_nested_docx_table_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            source_path = Path(tmpdir) / "nested-table.docx"
            write_docx(
                source_path,
                """
                <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
                  <w:body>
                    <w:tbl>
                      <w:tr>
                        <w:tc>
                          <w:tbl>
                            <w:tr>
                              <w:tc>
                                <w:p><w:r><w:t>Nested</w:t></w:r></w:p>
                              </w:tc>
                            </w:tr>
                          </w:tbl>
                        </w:tc>
                      </w:tr>
                    </w:tbl>
                  </w:body>
                </w:document>
                """,
            )

            result = emit_extraction_result_from_source_file(
                source_path,
                request_id="docx-nested-001",
                source_ref="docx-nested",
                media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        assert_schema_valid(self, result, schema_name="extraction-result.schema.json")
        self.assertEqual(result["state"], "denied")
        self.assertEqual(result["refusal"]["reason_class"], "ineligible_source")

    def test_ready_docx_extraction_is_retrieval_compatible(self) -> None:
        result = emit_retrieval_package_from_source_file(
            DOCX_READY_FIXTURE,
            request_id="docx-ret-001",
            source_ref="docx-ret",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

        assert_schema_valid(self, result, schema_name="retrieval-package.schema.json")
        self.assertEqual(result["state"], "ready")
        self.assertEqual(result["retrieval_profile"]["chunking_mode"], "section")
        self.assertEqual([chunk["ordinal"] for chunk in result["chunks"]], [0, 1])
        self.assertEqual({chunk["structure_kind"] for chunk in result["chunks"]}, {"section"})


if __name__ == "__main__":
    unittest.main()
