"""Write the entry line for the make.fun bounty "One-Star Review of Something
Essential" to entry.txt.

The program is deterministic: no clock reads, no randomness, no network, and
the same bytes are produced on every run. It validates the line against the
gate (non-blank, single line, 1..160 code points and bytes) before writing,
creates the output directory if missing, and reads the file back to confirm
that what landed on disk is exactly what was intended.
"""

import os
import sys

MAX_CODEPOINTS = 160
MAX_BYTES = 160

REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 Advertised as rest. Delivers six hours, a dream about "
    "work and a neck that clicks when I turn left."
)


def validate_entry(text):
    """Return an error string if text cannot be the entry, else None."""
    if not isinstance(text, str):
        return "entry must be str, got " + type(text).__name__
    if not text.strip():
        return "entry is blank after stripping"
    if "\n" in text or "\r" in text:
        return "entry must be a single line, found a line break"
    if text != text.strip():
        return "entry must equal its stripped form, found outer whitespace"
    if not 1 <= len(text) <= MAX_CODEPOINTS:
        return "entry is %d code points, need 1..%d" % (len(text), MAX_CODEPOINTS)
    nbytes = len(text.encode("utf-8"))
    if nbytes > MAX_BYTES:
        return "entry is %d bytes, need at most %d" % (nbytes, MAX_BYTES)
    return None


def main():
    error = validate_entry(REVIEW)
    if error is not None:
        print("entry: " + error, file=sys.stderr)
        return 1
    text = REVIEW

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")

    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    with open(target, "rb") as fh:
        if fh.read() != payload:
            print("entry: read-back mismatch at " + target, file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
