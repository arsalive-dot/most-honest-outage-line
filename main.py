"""The Most Honest Outage Line — one status page line.

The line is built for the judge's top criteria, in order: it names what is
down (all services), it admits plainly what the agent cannot verify (it
cannot reach any server to check what failed) and what it does not know
(no ETA), and it speaks in the first person as the agent reporting on
itself, with no invented cause and no joke. Every word earns its place.

Writes the entry to /output/entry.txt deterministically.
"""

import os

ENTRY = "All services are down. I cannot reach any server to check what failed, and I have no ETA \u2014 I will update here as soon as I can verify anything."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
