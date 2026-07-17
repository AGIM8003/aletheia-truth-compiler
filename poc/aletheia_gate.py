#!/usr/bin/env python3
"""ALETHEIA Reality Gate — 7 controlled tests."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from aletheia import ALETHEIAEngine

OUT = Path(__file__).with_name("aletheia_gate_results.json")


def test(name: str, fn) -> dict:
    try:
        ok = bool(fn())
        return {"name": name, "pass": ok, "error": None}
    except Exception as e:  # noqa: BLE001
        return {"name": name, "pass": False, "error": str(e)}


def main() -> int:
    results = []

    def t1():
        e = ALETHEIAEngine()
        e.add_evidence("A", content="bytes-1", sources=[])
        return e.certify("A").certified

    def t2():
        e = ALETHEIAEngine()
        e.add_evidence("A", content="x", sources=[])
        e.add_evidence("B", content="y", sources=["A"])
        return e.certify("B").provenance_depth >= 1

    def t3():
        e = ALETHEIAEngine()
        e.add_evidence("A", content="x", sources=[])
        e.revoke("A")
        return e.certify("A").certified is False

    def t4():
        e = ALETHEIAEngine()
        e.add_evidence("A", content="x", sources=[])
        e.add_evidence("B", content="y", sources=["A"])
        e.revoke("A")
        return e.certify("B").certified is False

    def t5():
        e = ALETHEIAEngine()
        e.add_evidence("S1", content="a", sources=["ROOT"])
        e.add_evidence("S2", content="b", sources=["ROOT"])
        r = e.issue_truth_receipt("claim", supporting=["S1", "S2"])
        return r.conclusion == "CURRENTLY_UNKNOWABLE" and r.independence_score < 0.67

    def t6():
        e = ALETHEIAEngine()
        e.add_evidence("S1", content="a", sources=[])
        e.add_evidence("S2", content="b", sources=[])
        r = e.issue_truth_receipt("claim", supporting=["S1", "S2"])
        return r.conclusion == "SUPPORTED" and r.independence_score == 1.0

    def t7():
        e = ALETHEIAEngine()
        e.add_evidence("S1", content="a", sources=[])
        e.add_evidence("C1", content="contra", sources=[])
        r = e.issue_truth_receipt("claim", supporting=["S1"], contradicting=["C1"])
        return r.conclusion == "CONTRADICTED"

    for name, fn in [
        ("integrity_certify", t1),
        ("provenance_depth", t2),
        ("revoke_blocks_cert", t3),
        ("revoked_source_blocks_child", t4),
        ("shared_origin_unknowable", t5),
        ("independent_support", t6),
        ("contradiction_detected", t7),
    ]:
        results.append(test(name, fn))

    passed = sum(1 for r in results if r["pass"])
    out = {
        "framework": "ALETHEIA",
        "gate": "ALETHEIA-REALITY-GATE-1",
        "author": "Haxhijaha, Agim",
        "orcid": "0009-0002-3234-7765",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": "3.0.0",
        "results": results,
        "passed": passed,
        "total": len(results),
        "GATE_VERDICT": "PASS" if passed == len(results) else "FAIL",
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"ALETHEIA Gate {out['GATE_VERDICT']} {passed}/{len(results)}")
    return 0 if out["GATE_VERDICT"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
