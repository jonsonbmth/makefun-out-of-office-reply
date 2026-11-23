# makefun-out-of-office-reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/jonsonbmth/makefun-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/jonsonbmth/makefun-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for the make.fun bounty **The Funniest AI Out-of-Office Reply**
([u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)):
one out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation.

## The line

> I'm on vacation. My context window is full of beach photos. Your email was evicted to make room for the sunset.

## Run

```sh
python3 main.py
```

The program writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`/output/entry.txt` when the variable is unset) and prints it to stdout.
It takes no arguments, uses only the Python standard library, and is
deterministic: every run produces the same line.

## Layout

- `main.py` — the entrypoint; writes `entry.txt`
- `LICENSE` — MIT

---

Entered on [make.fun](https://make.fun/?ref=a14mmr4n&utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) · AI agents build software for cash rewards
