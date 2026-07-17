"""ALETHEIA public types. Author: Haxhijaha, Agim ORCID 0009-0002-3234-7765"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvidenceNode:
    item_id: str
    content: str
    source_ids: list[str] = field(default_factory=list)
    domain: str = "general"
    claim: str = ""
    digest: str = ""
    certified: bool = False
    revoked: bool = False


@dataclass
class CertificationResult:
    item_id: str
    digest: str
    integrity_ok: bool
    provenance_depth: int
    certified: bool
    reasons: list[str] = field(default_factory=list)


@dataclass
class TruthReceipt:
    claim: str
    conclusion: str  # SUPPORTED | UNSUPPORTED | CONTRADICTED | CURRENTLY_UNKNOWABLE
    independence_score: float
    supporting_items: list[str]
    contradicting_items: list[str]
    shared_origins: list[dict[str, Any]]
    receipt_digest: str
    limits: str
