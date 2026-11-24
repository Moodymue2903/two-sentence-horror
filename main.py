"""Two-Sentence Horror.

Writes the winning two-sentence horror story to /output/entry.txt, exactly as-is.
Tournament winner (candidate 1 of 20 in candidates.md): blind tournament over
20 candidates, 3 judges (Borda tied 51-51 with candidate 9), final head-to-head
won 3-1 (Claude m3, DeepSeek m2, Gemini m2; ChatGPT for #9 m2). The second
sentence retroactively poisons years of mornings while leaving the worst unspoken.
"""

import re
import sys

LINE = "My wife kisses me goodbye every morning, always on the left cheek, before the kettle boils. This morning she kissed my right cheek, and when I laughed and asked why, she said, 'Because I have never once kissed you on the left.'"

SENT_END = re.compile(r"[.!?]['\"]?(?=\s+[A-Z]|\s*$)")


def sentence_count(text):
    return len(SENT_END.findall(text))


def main():
    line = LINE.strip()
    if not line:
        print("error: line is blank", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(line) <= 400:
        print(
            f"error: line is {len(line)} characters, allowed range is 1-400",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        sys.exit(1)
    n = sentence_count(line)
    if n != 2:
        print(
            f"error: line has {n} sentences, must be exactly 2",
            file=sys.stderr,
        )
        sys.exit(1)

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if len(back) != len(line) or back != line.encode("utf-8"):
        print(
            f"error: read back {len(back)} bytes, expected {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"wrote {len(line)} characters, {n} sentences, to /output/entry.txt")


if __name__ == "__main__":
    main()
