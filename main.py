# SPDX-License-Identifier: MIT
"""The Dog Ate My Homework: Funniest Excuse.

A deterministic, offline, stdlib-only entry. It writes exactly one line —
the excuse a dog gives after being caught eating the homework — to
/output/entry.txt, byte-identical on every run.

The line: the dog was "helping". It smelled the pencil the owner chews
when stuck, so it finished the job the only way a dog knows how — and it
regrets nothing. Dog logic, dog's own voice, no embarrassment, and a
twist the judge has not heard a thousand times.
"""

import os

EXCUSE = (
    "I only ate it because it smelled like the pencil you chew when "
    "you're stuck \u2014 I was helping, and I regret nothing."
)


def main() -> None:
    # Self-check against the gate: 1-200 characters, not only whitespace.
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
