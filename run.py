"""CLI: run selection and write results.json."""

import json
import base64
from profiles import CANDIDATES, PROFILES
from select import select_candidate
from data import PAYLOAD_B64
from scoring import metrics


def main():
    results = {}
    for key in PROFILES:
        rec = select_candidate(key)
        results[key] = {
            "selected": rec["id"] if rec else None,
            "metrics": metrics(rec) if rec else None,
            "payload": base64.b64decode(PAYLOAD_B64).decode() if rec else None,
        }
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
