"""ALETHEIA — Evidence DNA, certification, and bounded truth discovery (research library)."""
from .engine import ALETHEIAEngine
from .types import CertificationResult, EvidenceNode, TruthReceipt
from .core import content_digest, independence_score, detect_shared_origins

__all__ = [
    "ALETHEIAEngine",
    "EvidenceNode",
    "CertificationResult",
    "TruthReceipt",
    "content_digest",
    "independence_score",
    "detect_shared_origins",
]
__version__ = "3.0.0"
