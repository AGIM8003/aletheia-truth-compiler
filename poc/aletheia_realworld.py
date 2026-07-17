#!/usr/bin/env python3
"""ALETHEIA real-world scenario — scientific claim with hidden shared preprint origin."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from aletheia import ALETHEIAEngine

OUT = Path(__file__).with_name("aletheia_realworld_evidence.json")


def main() -> int:
    e = ALETHEIAEngine()
    # Shared origin looks like three independent papers
    e.add_evidence("PREPRINT_X", content="novel biomarker Z elevates in disease D", sources=[], domain="preprint")
    e.add_evidence("PAPER_A", content="Journal A reproduces biomarker Z", sources=["PREPRINT_X"], claim="Z predicts D", domain="journal")
    e.add_evidence("PAPER_B", content="Journal B meta confirms Z", sources=["PREPRINT_X"], claim="Z predicts D", domain="journal")
    e.add_evidence("NEWSWIRE", content="Press summary of Z breakthrough", sources=["PAPER_A", "PAPER_B"], claim="Z predicts D", domain="media")
    e.add_evidence("INDEPENDENT_RCT", content="RCT n=1200 finds null effect for Z", sources=[], claim="Z does not predict D", domain="trial")

    shared = e.shared_origins(["PAPER_A", "PAPER_B", "NEWSWIRE"])
    receipt_false_plurality = e.issue_truth_receipt(
        "Z predicts D",
        supporting=["PAPER_A", "PAPER_B", "NEWSWIRE"],
    )
    receipt_with_rct = e.issue_truth_receipt(
        "Z predicts D",
        supporting=["PAPER_A", "PAPER_B"],
        contradicting=["INDEPENDENT_RCT"],
    )
    out = {
        "framework": "ALETHEIA",
        "author": "Haxhijaha, Agim",
        "orcid": "0009-0002-3234-7765",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "scenario": "scientific_claim_hidden_shared_preprint",
        "shared_origins": shared,
        "false_plurality_receipt": {
            "conclusion": receipt_false_plurality.conclusion,
            "independence": receipt_false_plurality.independence_score,
        },
        "with_rct_receipt": {
            "conclusion": receipt_with_rct.conclusion,
            "independence": receipt_with_rct.independence_score,
        },
        "what_existing_approaches_miss": (
            "Citation counts and journal prestige treat PAPER_A/B/NEWSWIRE as three "
            "independent confirmations; Evidence DNA shows they share PREPRINT_X."
        ),
        "pass": (
            any(s["origin_id"] == "PREPRINT_X" for s in shared)
            and receipt_false_plurality.conclusion == "CURRENTLY_UNKNOWABLE"
            and receipt_with_rct.conclusion == "CONTRADICTED"
        ),
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"ALETHEIA realworld pass={out['pass']}")
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
