"""Customer requirement profiles."""

PROFILES = {
    "profile_LA": {   # long-acting topical biologic
        "half_life_h": 1500.0,
        "plddt": 80.0,
        "immune_recognition": 0.40,
        "expression_yield": 0.50,
    },
    "profile_FA": {   # fast-acting research reagent
        "half_life_h": 0.0,
        "plddt": 85.0,
        "immune_recognition": 1.00,
        "expression_yield": 0.50,
    },
}

CANDIDATES = [
    {"id": "HIT-001", "domains": {"D1": "ref", "D2": "ref", "D3": "ref"},     "template": "expr-A"},
    {"id": "HIT-002", "domains": {"D1": "ref", "D2": "ri",  "D3": "ref"},     "template": "expr-A"},
    {"id": "HIT-003", "domains": {"D1": "ri",  "D2": "ri",  "D3": "ri"},      "template": "expr-A"},
    {"id": "HIT-004", "domains": {"D1": "ri",  "D2": "ri",  "D3": "ri"},      "template": "expr-B"},
    {"id": "HIT-005", "domains": {"D1": "ri",  "D2": "ri",  "D3": "ref"},     "template": "expr-B"},
    {"id": "HIT-006", "domains": {"D1": "ref", "D2": "ref", "D3": "ri"},      "template": "expr-B"},
]
