#!/usr/bin/env python3
"""One Star for Monday: write a one-star review of Monday as a restaurant.

Writes the review to /output/entry.txt by default, or to the path given
as the first argument, or to $OUTPUT_PATH. Deterministic: stdlib only,
no network, no clock, no randomness. Prints the line too.

The review (24 words, inside the 25-word limit): a diner complains the
waiter brought the weekend back cold, charged for the coffee, and Monday
smiled like it was doing him a favour. Table, server, dish and bill all
in it, and the joke is Monday itself.
"""

import os
import sys

ENTRY = (
    "One star. The waiter brought my weekend back cold, charged me "
    "for the coffee, and Monday smiled like it was doing me a favour."
)

MAX_CHARS = 180


def validate(text):
    """Check the entry passes the kit gate: 1 to 180 chars, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 180 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if chr(8212) in text:
        raise ValueError("entry must not contain an em dash")


def resolve_output_path(argv):
    """Pick the output path: argv[1], else $OUTPUT_PATH, else default."""
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def write_entry(text, target):
    """Write the validated entry text to the target path."""
    directory = os.path.dirname(target)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)


def main(argv):
    """Validate the entry and write it to the output target."""
    validate(ENTRY)
    target = resolve_output_path(argv)
    write_entry(ENTRY, target)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
