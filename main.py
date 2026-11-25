"""Notes From a Passive-Aggressive Fridge.

make.fun bounty: u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7
Writes the locked final note (F-K3, Sesi B decision) to /output/entry.txt,
or to $MAKEFUN_OUTPUT when set (used by the local tests).

Stdlib only. No network, no model: fully deterministic.
"""

import os
from pathlib import Path

FINAL_TEXT = (
    "I counted the leftovers you promised to eat. "
    "All four are still here, judging you. I taught them."
)


def main() -> None:
    if not 1 <= len(FINAL_TEXT) <= 200:
        raise ValueError(
            f"final text must be 1-200 characters, got {len(FINAL_TEXT)}"
        )
    if not FINAL_TEXT.strip():
        raise ValueError("final text must not be only whitespace")
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(FINAL_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
