"""Write one short line for a make.fun bounty.

Standard library only, no network.
"""

import os
import sys
from pathlib import Path

TEXT = "My agent scheduled the deploy for end of day, defined end of day as 11:40, and went to lunch."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"

    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    out_dir = Path(target)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
