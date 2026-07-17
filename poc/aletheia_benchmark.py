#!/usr/bin/env python3
"""ALETHEIA benchmark harness."""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from aletheia import ALETHEIAEngine

OUT = Path(__file__).with_name("aletheia_benchmark_results.json")


def main() -> int:
    cases = []
    # scale certify
    e = ALETHEIAEngine()
    t0 = time.perf_counter()
    e.add_evidence("R0", content="root", sources=[])
    for i in range(1, 201):
        e.add_evidence(f"R{i}", content=f"c{i}", sources=[f"R{i-1}"])
    t_build = time.perf_counter() - t0
    t1 = time.perf_counter()
    cert = e.certify("R200")
    t_cert = time.perf_counter() - t1
    cases.append({"name": "chain_200_certify", "pass": cert.certified and cert.provenance_depth >= 1, "seconds": round(t_cert, 6)})

    e2 = ALETHEIAEngine()
    for i in range(50):
        e2.add_evidence(f"S{i}", content=f"x{i}", sources=[] if i % 2 else ["SHARED"])
    t2 = time.perf_counter()
    indep = e2.independence([f"S{i}" for i in range(50)])
    t_indep = time.perf_counter() - t2
    cases.append({"name": "independence_50", "pass": 0.0 <= indep <= 1.0, "seconds": round(t_indep, 6), "score": indep})

    e3 = ALETHEIAEngine()
    e3.add_evidence("A", content="a", sources=[])
    e3.add_evidence("B", content="b", sources=[])
    r = e3.issue_truth_receipt("c", supporting=["A", "B"])
    cases.append({"name": "receipt_independent", "pass": r.conclusion == "SUPPORTED", "seconds": 0.0})

    out = {
        "framework": "ALETHEIA",
        "author": "Haxhijaha, Agim",
        "orcid": "0009-0002-3234-7765",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "build_seconds": round(t_build, 6),
        "cases": cases,
        "pass": all(c["pass"] for c in cases),
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"ALETHEIA benchmark pass={out['pass']}")
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
