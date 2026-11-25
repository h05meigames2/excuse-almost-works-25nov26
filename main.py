"""Entry generator for make.fun bounty
u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5
(The Excuse That Almost Works).

Writes one line of plain text -- the excuse a gamer texts the boss
to skip work during GTA 6 launch week -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The line: a boring, specific, verifiable-sounding domestic appointment
(the gas engineer and his all-day window) that a tired manager has
heard a hundred times and can neither check nor argue with. No wild
story, no dead relative, no flat tyre, no sudden fever -- just the
ten-hour window nobody can escape.
"""

import os

ENTRY = (
    "sorry boss gas engineer coming to my flat between 8 and 6 "
    "and someone has to be in"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
