"""One-star review of something essential: gravity.

The program writes one single-line deadpan one-star review, at most
160 characters, to /output/entry.txt. The essential is gravity: it has
no off switch, no customer service and no refund policy, yet it drops
everything we own. The complaint is filed in earnest against a thing
that cannot be fixed, and the sting lands in the last few words.
"""

import os

REVIEW = (
    "One star. Gravity has no off switch, no customer service, "
    "and no refund policy, yet it drops everything I own."
)

MAX_CHARS = 160


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # One line, 1-160 characters, no trailing newline: the gate allows
    # UTF-8 text of 1 to 160 characters, not only white space.
    text = REVIEW
    assert "\n" not in text and 1 <= len(text) <= MAX_CHARS
    assert text == text.strip(), "entry must not start or end with space"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
