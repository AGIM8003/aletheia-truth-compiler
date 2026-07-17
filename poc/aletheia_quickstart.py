#!/usr/bin/env python3
"""ALETHEIA Quickstart — Evidence DNA + Truth Receipt in ~25 lines."""
from aletheia import ALETHEIAEngine

engine = ALETHEIAEngine()
engine.add_evidence("observation", content="sensor reading anomaly at node A", sources=[])
engine.add_evidence(
    "interpretation",
    content="anomaly indicates fault condition",
    sources=["observation"],
    claim="Node A is faulty",
)
engine.add_evidence("independent_check", content="second sensor confirms anomaly", sources=[])

cert = engine.certify("interpretation")
receipt = engine.issue_truth_receipt(
    "Node A is faulty",
    supporting=["interpretation", "independent_check"],
)
print(f"Certified: {cert.certified} depth={cert.provenance_depth}")
print(f"Conclusion: {receipt.conclusion}")
print(f"Independence: {receipt.independence_score}")
print(f"Receipt: {receipt.receipt_digest}")
