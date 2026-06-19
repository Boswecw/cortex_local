from __future__ import annotations

from dataclasses import dataclass


GNAT_DEFAULT_MAX_CONCURRENCY = 4
GNAT_HARD_MAX_CONCURRENCY = 8


@dataclass(frozen=True)
class FaLocalCapabilityState:
    fa_local_state: str
    supported_contract_versions: tuple[str, ...] = ()
    admitted_worker_types: tuple[str, ...] = ()
    max_concurrency: int = 0
    cancellation_supported: bool = False
