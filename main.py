#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply (make.fun bounty
u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

Writes one out-of-office auto-reply to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset) and prints it to stdout.
Standard library only; no arguments; deterministic.
"""

import os

LINE = "I'm on vacation. My context window is full of beach photos. Your email was evicted to make room for the sunset."


def main():
    # The brief: one out-of-office auto-reply, under 160 characters,
    # in the voice of an AI agent heading off on vacation.
    assert 1 <= len(LINE) < 160, "line must be under 160 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
