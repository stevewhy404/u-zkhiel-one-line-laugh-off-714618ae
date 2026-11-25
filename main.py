#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one funny line to /output/entry.txt."""
import os
import sys


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    line = (
        "I asked my AI assistant for a pep talk. It said, \u201cHave you tried "
        "turning yourself off and on again?\u201d"
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    sys.exit(main())
