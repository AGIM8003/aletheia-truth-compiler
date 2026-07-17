#!/usr/bin/env python3
"""ALETHEIA alt impl — Merkle-style rolling digest vs content_digest; replication check."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from aletheia.core import content_digest, independence_score

OUT = Path(__file__).with_name("aletheia_replication_evidence.json")


def merkle_digest(content: str, sources: list[str]) -> str:
    h = hashlib.sha256(content.encode()).digest()
    for s in sorted(sources):
        h = hashlib.sha256(h + s.encode()).digest()
    return h.hex()


def main() -> int:
    fixtures = [
        ("hello", []),
        ("derived", ["A", "B"]),
        ("leaf", ["ROOT"]),
    ]
    rows = []
    for content, sources in fixtures:
        a = content_digest(content, sources)
        b = merkle_digest(content, sources)
        # Not equal algorithms — compare independence agreement instead
        rows.append({"content": content, "primary": a[:16], "alt": b[:16], "primary_len": len(a)})

    # Independence replication: same formula must match
    src = {"X": ["R1"], "Y": ["R1"], "Z": ["R2"]}
    s1 = independence_score(src)
    # alt: pairwise Jaccard independence proxy inverted
    ids = list(src)
    n = len(ids)
    shared = sum(1 for i in range(n) for j in range(i + 1, n) if set(src[ids[i]]) & set(src[ids[j]]))
    s2 = round(1.0 - shared / (n * (n - 1) / 2), 4)
    match = s1 == s2
    out = {
        "framework": "ALETHEIA",
        "author": "Haxhijaha, Agim",
        "orcid": "0009-0002-3234-7765",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "approach": "primary=content_digest; alt=merkle_rolling; independence formula replicated",
        "digest_rows": rows,
        "independence_primary": s1,
        "independence_alt": s2,
        "replication_pass": match,
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"ALETHEIA replication_pass={match}")
    return 0 if match else 1


if __name__ == "__main__":
    sys.exit(main())
