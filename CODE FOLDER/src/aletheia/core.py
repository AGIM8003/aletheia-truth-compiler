"""ALETHEIA core Evidence DNA primitives. Author: Haxhijaha, Agim ORCID 0009-0002-3234-7765"""
from __future__ import annotations

import hashlib
from typing import Any


def content_digest(content: str, source_ids: list[str] | None = None) -> str:
    """Content-addressed Evidence DNA digest (sha256 of content + sorted sources)."""
    sources = sorted(source_ids or [])
    payload = content + "|" + ",".join(sources)
    return hashlib.sha256(payload.encode()).hexdigest()


def independence_score(item_sources: dict[str, list[str]]) -> float:
    """1.0 = fully independent source sets; 0.0 = all share roots pairwise."""
    ids = list(item_sources.keys())
    n = len(ids)
    if n < 2:
        return 1.0
    total = n * (n - 1) / 2
    shared = 0
    sets = {i: set(item_sources[i]) for i in ids}
    for i in range(n):
        for j in range(i + 1, n):
            if sets[ids[i]] & sets[ids[j]]:
                shared += 1
    return round(1.0 - shared / total, 4)


def detect_shared_origins(item_sources: dict[str, list[str]]) -> list[dict[str, Any]]:
    usage: dict[str, list[str]] = {}
    for item_id, sources in item_sources.items():
        for s in sources:
            usage.setdefault(s, []).append(item_id)
    return [
        {"origin_id": oid, "used_by": items}
        for oid, items in usage.items()
        if len(items) > 1
    ]


def provenance_depth(
    item_id: str,
    registry: dict[str, list[str]],
    seen: set[str] | None = None,
) -> int:
    """Longest provenance path toward roots (iterative; safe for 2000+ deep chains).

    ``seen`` is accepted for API compatibility with earlier recursive callers;
    cycles are guarded via an explicit visiting set on the stack.
    """
    _ = seen  # API compatibility; unused in iterative implementation
    memo: dict[str, int] = {}
    visiting: set[str] = set()
    # (eid, expanded) — expand children first, then compute depth
    stack: list[tuple[str, bool]] = [(item_id, False)]
    while stack:
        eid, expanded = stack.pop()
        if expanded:
            visiting.discard(eid)
            sources = registry.get(eid, [])
            if not sources:
                memo[eid] = 0
            else:
                memo[eid] = 1 + max(memo.get(s, 0) for s in sources)
            continue
        if eid in memo:
            continue
        if eid in visiting:
            memo[eid] = 0  # cycle guard
            continue
        visiting.add(eid)
        stack.append((eid, True))
        for s in registry.get(eid, []):
            if s not in memo:
                stack.append((s, False))
    return memo.get(item_id, 0)
