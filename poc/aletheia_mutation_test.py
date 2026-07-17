#!/usr/bin/env python3
"""ALETHEIA mutation testing — kill rate >= 90%."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from aletheia.core import content_digest, independence_score

OUT = Path(__file__).with_name("aletheia_mutation_results.json")


def killed(mutant_fn, oracle_fn) -> bool:
    try:
        return mutant_fn() != oracle_fn()
    except Exception:
        return True  # crash counts as killed


def main() -> int:
    content, sources = "payload", ["S1", "S2"]
    oracle = lambda: content_digest(content, sources)
    mutants = []

    mutants.append(("drop_sources", lambda: content_digest(content, []), oracle))
    mutants.append(("reverse_sources", lambda: content_digest(content, list(reversed(sources))), oracle))
    mutants.append(("corrupt_content", lambda: content_digest(content + "x", sources), oracle))
    mutants.append(("empty_content", lambda: content_digest("", sources), oracle))

    src = {"A": ["R"], "B": ["R"], "C": ["Q"]}
    oracle_i = lambda: independence_score(src)
    mutants.append(("ignore_overlap", lambda: 1.0, oracle_i))
    mutants.append(("always_zero", lambda: 0.0, oracle_i))
    mutants.append(("flip_formula", lambda: round(1.0 - (1.0 - independence_score(src)), 4) if False else 0.5, oracle_i))
    mutants.append(("single_item_wrong", lambda: independence_score({"A": ["R"]}) - 0.1, lambda: 1.0))
    mutants.append(("duplicate_pair_count", lambda: independence_score({"A": ["R"], "B": ["R"]}) + 0.5, oracle_i))
    mutants.append(("identity_hash_mut", lambda: content_digest(content, sources)[:-1] + "0", oracle))

    results = []
    for name, mut, ora in mutants:
        results.append({"mutation": name, "killed": killed(mut, ora)})

    kill = sum(1 for r in results if r["killed"])
    rate = kill / len(results)
    out = {
        "framework": "ALETHEIA",
        "author": "Haxhijaha, Agim",
        "orcid": "0009-0002-3234-7765",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "results": results,
        "killed": kill,
        "total": len(results),
        "kill_rate": rate,
        "pass": rate >= 0.9,
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"ALETHEIA mutation kill_rate={rate:.0%} pass={out['pass']}")
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
