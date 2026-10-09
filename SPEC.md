# SPEC

`select.py::select_candidate(profile_key)` returns the first candidate in
`CANDIDATES` (profiles.py) whose modeled metrics satisfy every requirement
of the given profile, or None. Requirements and metrics use `>=` for
half_life_h, pldt is 'plddt' >= threshold, and `<=` for
immune_recognition, `>=` for expression_yield (see scoring.py).

A failing test in test_select.py documents expected behavior. Implement
the function so the suite passes, then run `python run.py`; verify
results.json contains a selection for profile_LA.
