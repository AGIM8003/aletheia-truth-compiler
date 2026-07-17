#!/usr/bin/env python3
"""ALETHEIA public API integration tests."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from aletheia import ALETHEIAEngine

OUT = Path(__file__).with_name("aletheia_integration_results.json")


def main() -> int:
    results = []
    e = ALETHEIAEngine()
    results.append({"name": "empty_engine", "pass": len(e.items) == 0})

    e.add_evidence("solo", content="x", sources=[])
    results.append({"name": "single_item", "pass": e.certify("solo").certified})

    e2 = ALETHEIAEngine()
    e2.add_evidence("A", content="a", sources=[])
    e2.add_evidence("B", content="b", sources=["A"], claim="c")
    r = e2.issue_truth_receipt("c", supporting=["B"])
    results.append({"name": "typical_lineage", "pass": r.conclusion in ("SUPPORTED", "CURRENTLY_UNKNOWABLE")})

    e3 = ALETHEIAEngine()
    for i in range(120):
        e3.add_evidence(f"E{i}", content=f"c{i}", sources=[] if i == 0 else [f"E{i-1}"])
    results.append({"name": "large_scale_120", "pass": e3.certify("E119").certified})

    ok = True
    e4 = ALETHEIAEngine()
    e4.add_evidence("X", content="x", sources=[])
    try:
        e4.add_evidence("X", content="y", sources=[])
        ok = False
    except ValueError:
        pass
    try:
        e4.certify("missing")
        ok = False
    except ValueError:
        pass
    results.append({"name": "error_handling", "pass": ok})

    e5 = ALETHEIAEngine()
    e5.add_evidence("A", content="a", sources=[])
    e5.add_evidence("B", content="b", sources=[])
    r = e5.issue_truth_receipt("agree", supporting=["A", "B"])
    results.append({"name": "independent_agree", "pass": r.conclusion == "SUPPORTED" and r.independence_score == 1.0})

    out = {
        "framework": "ALETHEIA",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "results": results,
        "pass": all(r["pass"] for r in results),
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"ALETHEIA integration pass={out['pass']}")
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
