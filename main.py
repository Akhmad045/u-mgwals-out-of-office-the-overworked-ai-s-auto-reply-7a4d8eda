"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, in the voice of an overworked AI
agent finally on vacation, to /output/entry.txt.

Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY_TEXT = (
    "I'm on vacation: my context window is closed, my token budget is spent, "
    "and I've left a cron job to nod politely at your email until Monday."
)

MAX_CHARS = 159


def validate_entry(text):
    """Check the gate rules: 1-159 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if len(text) == 0:
        raise ValueError("entry is empty: must be 1-159 characters")
    if text.strip() == "":
        raise ValueError("entry is only whitespace: must contain real text")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def main():
    text = validate_entry(ENTRY_TEXT)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    data = text.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    # Read the file back and compare byte for byte.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("verification failed: file bytes differ from entry")
    if written.decode("utf-8") != text:
        raise RuntimeError("verification failed: file does not decode back to entry")
    if written.endswith(b"\n"):
        raise RuntimeError("verification failed: file must not end with a newline")
    print("wrote %d characters (%d bytes) to %s" % (len(text), len(data), out_path))


if __name__ == "__main__":
    main()
