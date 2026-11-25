#!/usr/bin/env python3
"""Duskline Tired Dark Lord — make.fun entry.

Writes the 100-word villain monologue to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network. Never raises: any failure exits 0
without writing anything. Never writes into the repository directory.
"""

import os
import sys
import tempfile

ENTRY = (
    "Ah. The hero. I saw the sword, yes. Sit\u2014not the throne, the stool. "
    "Three hundred years I waited in the dark, rehearsing. I had a speech. I had lightning. "
    "I had\u2014where did I put the lightning? Never mind. The point is, boy, I won. "
    "Nine kingdoms kneel, the dragons file their taxes on time, the prophecy is... filed. "
    "Under P. Now you want a duel at dawn. Dawn. I have a grain levy at dawn, and the "
    "trolls want the bridge tolls cut. So. Kneel, swear, take the east wing, and we shall "
    "fight... Tuesday. Bring your own lunch, hero."
)

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _resolve_output_dir():
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if raw:
        return os.path.abspath(os.path.expanduser(raw))
    return tempfile.mkdtemp(prefix="duskline-tired-dark-lord-")


def main():
    try:
        # Gate: entry must be UTF-8, 1-600 chars, not only whitespace.
        if not ENTRY or not ENTRY.strip():
            return 0
        if len(ENTRY) > 600:
            return 0
        ENTRY.encode("utf-8")

        out_dir = _resolve_output_dir()
        # HARD GUARD: never write into (or under) the repo directory.
        repo = os.path.abspath(REPO_DIR)
        if out_dir == repo or out_dir.startswith(repo + os.sep):
            return 0

        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(ENTRY)
        # Read back and verify.
        with open(path, "r", encoding="utf-8") as fh:
            if fh.read() != ENTRY:
                return 0
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
