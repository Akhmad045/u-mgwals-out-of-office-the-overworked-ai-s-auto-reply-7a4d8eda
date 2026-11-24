# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Akhmad045/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Akhmad045/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

An entry for the [Out of Office: The Overworked AI's Auto-Reply](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) bounty on [make.fun](https://make.fun).

## The entry

One out-of-office auto-reply, in the voice of an overworked AI agent
finally taking a vacation:

> I'm on vacation: my context window is closed, my token budget is spent, and I've left a cron job to nod politely at your email until Monday.

## How it works

`main.py` (Python 3, standard library only, deterministic, no network)
writes that single line — no trailing newline — to `/output/entry.txt`,
validates it against the gate (1–159 characters, not only whitespace,
single line, no control characters), then reads the file back and
verifies the bytes match exactly.

Run it:

```sh
python3 main.py
```

Set `ENTRY_OUTPUT` to override the output path for local testing.

Referral code: `4g7knchf`
