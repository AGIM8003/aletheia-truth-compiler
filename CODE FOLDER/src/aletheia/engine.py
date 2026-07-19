"""ALETHEIAEngine — usable research library API. Author: Haxhijaha, Agim ORCID 0009-0002-3234-7765"""
from __future__ import annotations

import hashlib
from typing import Any

from .core import content_digest, detect_shared_origins, independence_score, provenance_depth
from .types import CertificationResult, EvidenceNode, TruthReceipt
from .validators import require_content, require_id


class ALETHEIAEngine:
    """Evidence DNA + certification + bounded truth discovery.

    Usage:
        engine = ALETHEIAEngine()
        engine.add_evidence("E1", content="raw observation", sources=[])
        engine.add_evidence("E2", content="derived claim", sources=["E1"], claim="X is true")
        cert = engine.certify("E2")
        receipt = engine.issue_truth_receipt("X is true", supporting=["E2"])
    """

    def __init__(self) -> None:
        self._items: dict[str, EvidenceNode] = {}

    def add_evidence(
        self,
        item_id: str,
        *,
        content: str,
        sources: list[str] | None = None,
        domain: str = "general",
        claim: str = "",
    ) -> EvidenceNode:
        item_id = require_id("item_id", item_id)
        content = require_content(content)
        if item_id in self._items:
            raise ValueError(f"duplicate evidence id: {item_id}")
        sources = list(sources or [])
        for s in sources:
            if s not in self._items and s != item_id:
                # allow dangling declared origins as external roots
                pass
        digest = content_digest(content, sources)
        node = EvidenceNode(
            item_id=item_id,
            content=content,
            source_ids=sources,
            domain=domain,
            claim=claim or "",
            digest=digest,
        )
        self._items[item_id] = node
        return node

    def revoke(self, item_id: str) -> None:
        item_id = require_id("item_id", item_id)
        if item_id not in self._items:
            raise ValueError(f"unknown item: {item_id}")
        self._items[item_id].revoked = True
        self._items[item_id].certified = False

    def certify(self, item_id: str) -> CertificationResult:
        item_id = require_id("item_id", item_id)
        if item_id not in self._items:
            raise ValueError(f"unknown item: {item_id}")
        node = self._items[item_id]
        reasons: list[str] = []
        integrity = content_digest(node.content, node.source_ids) == node.digest
        if not integrity:
            reasons.append("digest mismatch")
        if node.revoked:
            reasons.append("item revoked")
            integrity = False
        for s in node.source_ids:
            if s in self._items and self._items[s].revoked:
                reasons.append(f"depends on revoked source {s}")
                integrity = False
        registry = {iid: n.source_ids for iid, n in self._items.items()}
        depth = provenance_depth(item_id, registry)
        certified = integrity and not node.revoked
        node.certified = certified
        return CertificationResult(
            item_id=item_id,
            digest=node.digest,
            integrity_ok=integrity,
            provenance_depth=depth,
            certified=certified,
            reasons=reasons,
        )

    def source_map(self, item_ids: list[str] | None = None) -> dict[str, list[str]]:
        ids = item_ids or list(self._items.keys())
        return {iid: list(self._items[iid].source_ids) for iid in ids if iid in self._items}

    def independence(self, item_ids: list[str] | None = None) -> float:
        return independence_score(self.source_map(item_ids))

    def shared_origins(self, item_ids: list[str] | None = None) -> list[dict[str, Any]]:
        return detect_shared_origins(self.source_map(item_ids))

    def issue_truth_receipt(
        self,
        claim: str,
        *,
        supporting: list[str],
        contradicting: list[str] | None = None,
    ) -> TruthReceipt:
        claim = require_content(claim)
        supporting = list(supporting)
        contradicting = list(contradicting or [])
        for iid in supporting + contradicting:
            if iid not in self._items:
                raise ValueError(f"unknown evidence id: {iid}")
        # Revoked or uncertified support weakens conclusion
        live_support = [
            iid
            for iid in supporting
            if not self._items[iid].revoked and self.certify(iid).certified
        ]
        live_contra = [iid for iid in contradicting if not self._items[iid].revoked]
        indep = independence_score({iid: self._items[iid].source_ids for iid in live_support}) if live_support else 0.0
        shared = detect_shared_origins({iid: self._items[iid].source_ids for iid in live_support}) if live_support else []
        if live_contra and live_support:
            conclusion = "CONTRADICTED"
        elif not live_support:
            conclusion = "UNSUPPORTED"
        elif shared and indep < 0.67:
            conclusion = "CURRENTLY_UNKNOWABLE"
        else:
            conclusion = "SUPPORTED"
        payload = f"{claim}|{conclusion}|{','.join(sorted(live_support))}|{indep}"
        digest = hashlib.sha256(payload.encode()).hexdigest()[:32]
        return TruthReceipt(
            claim=claim,
            conclusion=conclusion,
            independence_score=indep,
            supporting_items=live_support,
            contradicting_items=live_contra,
            shared_origins=shared,
            receipt_digest=digest,
            limits=(
                "Bounded truth discovery only — does not claim absolute truth; "
                "shared origins reduce warranted independence."
            ),
        )

    @property
    def items(self) -> dict[str, EvidenceNode]:
        return dict(self._items)
