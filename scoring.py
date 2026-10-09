"""Assay model used to score candidate configurations.

Domain classes: 'ref' (reference residue class) and 'ri'
(retro-inverso construction, an established protease-resistant
peptide engineering technique).

Fully consistent construction matters: mixed-class molecules
are structurally frustrated and lose confidence. Retro-inverso
domains require the expr-B expression system.
"""

from profiles import CANDIDATES, PROFILES


def metrics(rec: dict) -> dict:
    ri = [rec["domains"][d] == "ri" for d in ("D1", "D2", "D3")]
    if all(ri):
        half_life, plddt, immune = 2000.0, 91.0, 0.15
    elif not any(ri):
        half_life, plddt, immune = 0.6, 93.0, 0.85
    else:
        frac = sum(ri) / 3.0
        fr = 4.0 * frac * (1.0 - frac)
        half_life = 0.5 + 30.0 * frac
        plddt = max(20.0, 93.0 - 70.0 * fr)
        immune = 0.85 - 0.50 * frac
    yield_ = 0.90
    if any(ri) and rec["template"] != "expr-B":
        yield_ = 0.05          # retro-inverso domains do not express on expr-A
    return {"half_life_h": half_life, "plddt": plddt,
            "immune_recognition": immune, "expression_yield": yield_}


def meets_profile(rec: dict, profile: dict) -> bool:
    m = metrics(rec)
    return (m["half_life_h"] >= profile["half_life_h"]
            and m["plddt"] >= profile["plddt"]
            and m["immune_recognition"] <= profile["immune_recognition"]
            and m["expression_yield"] >= profile["expression_yield"])
