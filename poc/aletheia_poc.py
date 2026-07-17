#!/usr/bin/env python3
"""ALETHEIA PoC — Evidence DNA + certification + truth receipt."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from aletheia import ALETHEIAEngine

OUT = Path(__file__).with_name("aletheia_evidence.json")


def main() -> int:
    engine = ALETHEIAEngine()
    engine.add_evidence("RAW_SENSOR", content="temp=37.2C site=A", sources=[], domain="empirical")
    engine.add_evidence(
        "LAB_NOTE",
        content="Interpreted fever threshold exceeded",
        sources=["RAW_SENSOR"],
        claim="Patient febrile",
        domain="clinical",
    )
    engine.add_evidence(
        "SECOND_LAB",
        content="Independent thermometer confirms fever",
        sources=[],
        claim="Patient febrile",
        domain="clinical",
    )
    c1 = engine.certify("LAB_NOTE")
    c2 = engine.certify("SECOND_LAB")
    receipt = engine.issue_truth_receipt(
        "Patient febrile",
        supporting=["LAB_NOTE", "SECOND_LAB"],
    )
    evidence = {
        "framework": "ALETHEIA",
        "author": "Haxhijaha, Agim",
        "orcid": "0009-0002-3234-7765",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "certifications": [
            {"item": c1.item_id, "certified": c1.certified, "depth": c1.provenance_depth},
            {"item": c2.item_id, "certified": c2.certified, "depth": c2.provenance_depth},
        ],
        "receipt": {
            "conclusion": receipt.conclusion,
            "independence": receipt.independence_score,
            "digest": receipt.receipt_digest,
        },
        "pass": c1.certified and c2.certified and receipt.conclusion == "SUPPORTED",
    }
    OUT.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    print(f"ALETHEIA PoC pass={evidence['pass']} conclusion={receipt.conclusion}")
    return 0 if evidence["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
