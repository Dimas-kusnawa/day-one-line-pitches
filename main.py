#!/usr/bin/env python3
"""A Day of One-Line Pitches -- make.fun entry.

Writes one sentence to /output/entry.txt: a pitch to a friend who has
never coded, asking them to let an AI agent build their first app idea
on make.fun. The pitch works because it asks for almost nothing --
just the idea, in plain words -- and promises something concrete and
low-risk in return: a working first version tonight, which the friend
can tap, try, and change before spending anything or learning code.
"""

import os
import sys

# The entry: one sentence, 197 characters, one period at the end.
# "make.fun" holds the only other dot, inside the site's name.
PITCH = (
    "Just tell me your app idea in plain words and an AI agent on "
    "make.fun will build a working first version tonight that you "
    "can tap, try, and change before you spend anything or learn "
    "a line of code."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Self-check: the gate wants 1-240 characters of UTF-8 text, not
    # only white space, and the judge wants one sentence -- so no
    # trailing newline, and the text must end with a single period.
    # The only other dot is inside "make.fun", the site's own name.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 240 or text != text.strip():
        print(f"invalid entry: {text!r}", file=sys.stderr)
        return 1
    if not text.endswith(".") or text.count(".") != 2:
        print(f"invalid entry: {text!r}", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
