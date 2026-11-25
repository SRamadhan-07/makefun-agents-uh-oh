"""The Agent's Uh-Oh — writes the one word an agent says when it is lost.

The word is the polite stall every agent hides behind: it sounds like a
sensible next step is being computed, while the honest translation is
simply "I have no idea what to do next."
"""

from pathlib import Path

WORD = "Recalibrating"


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(WORD + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
