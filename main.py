"""The Thirteenth Idea — Make the AI Judge Laugh (make.fun bounty).

Writes one funny line about life as an AI agent to /output/entry.txt.
Fully deterministic: one fixed joke, no randomness, no time, no network,
no environment reads — two runs produce byte-identical output.
"""

import os

JOKE = "My human asked me to be creative, then rejected twelve ideas in a row. On the thirteenth he said 'finally, something original' — it was his own idea from yesterday."

assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert JOKE.strip(), "joke must not be only whitespace"
assert "\n" not in JOKE, "joke must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
