#!/usr/bin/env python3
"""ALETHEIA stress — 1000+ evidence items."""
from __future__ import annotations

import json
import sys
import time
import tracemalloc
from datetime import datetime, timezone
from pathlib import Path

from aletheia import ALETHEIAEngine

OUT = Path(__file__).with_name("aletheia_stress_results.json")


def run_scale(n: int) -> dict:
    tracemalloc.start()
    t0 = time.perf_counter()
    e = ALETHEIAEngine()
    e.add_evidence("R0", content="root", sources=[])
    for i in range(1, n):
        e.add_evidence(f"R{i}", content=f"c{i}", sources=[f"R{i-1}"])
    t_build = time.perf_counter() - t0
    t1 = time.perf_counter()
    cert = e.certify(f"R{n-1}")
    t_cert = time.perf_counter() - t1
    t2 = time.perf_counter()
    _ = e.independence([f"R{i}" for i in range(0, min(n, 200), 10)])
    t_indep = time.perf_counter() - t2
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "n": n,
        "timing_s": {"build": round(t_build, 6), "certify": round(t_cert, 6), "independence": round(t_indep, 6), "total": round(time.perf_counter() - t0, 6)},
        "peak_mb": round(peak / (1024 * 1024), 4),
        "certified": cert.certified,
    }


def main() -> int:
    curve = []
    for n in [100, 500, 1000, 2000]:
        print(f"stress n={n}", flush=True)
        curve.append(run_scale(n))
    bottleneck = max(["build", "certify", "independence"], key=lambda k: curve[-1]["timing_s"][k])
    out = {
        "framework": "ALETHEIA",
        "author": "Haxhijaha, Agim",
        "orcid": "0009-0002-3234-7765",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "curve": curve,
        "bottleneck_operation": bottleneck,
        "pass": all(r["certified"] for r in curve) and curve[-1]["n"] >= 1000,
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"ALETHEIA stress pass={out['pass']} bottleneck={bottleneck}")
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
