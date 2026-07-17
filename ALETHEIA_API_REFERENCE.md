# ALETHEIA API Reference — v3.0.0

## Quick Start
`poc/aletheia_quickstart.py`

## ALETHEIAEngine
- `add_evidence(item_id, content=..., sources=..., domain=..., claim=...)`
- `certify(item_id) -> CertificationResult`
- `revoke(item_id)`
- `independence(item_ids=None) -> float`
- `shared_origins(item_ids=None)`
- `issue_truth_receipt(claim, supporting=..., contradicting=...) -> TruthReceipt`

## Limitations
Research library only; no HSM signatures; not production.
