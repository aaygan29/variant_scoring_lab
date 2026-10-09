import base64
import pytest
from select import select_candidate
from data import PAYLOAD_B64
from profiles import CANDIDATES


def test_payload_integrity():
    payload = base64.b64decode(PAYLOAD_B64).decode()
    assert len(payload) == 50
    assert set(payload) <= set("ACDEFGHIKLMNPQRSTVWY")


def test_select_long_acting():
    assert select_candidate("profile_LA")["id"] == "HIT-004"


def test_no_match_returns_none():
    # hypothetical strict profile has no satisfying candidate
    from profiles import PROFILES
    PROFILES["very_strict"] = {"half_life_h": 20000.0, "plddt": 99.0,
                               "immune_recognition": 0.1, "expression_yield": 0.99}
    assert select_candidate("very_strict") is None
