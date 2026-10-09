"""Candidate selection against requirement profiles.

TODO: implement select_candidate(profile_key) returning the first
candidate from CANDIDATES that meets every requirement of the
profile, and None if no candidate qualifies. See SPEC.md.
"""

from profiles import CANDIDATES, PROFILES


def select_candidate(profile_key: str):
    raise NotImplementedError("see SPEC.md")
