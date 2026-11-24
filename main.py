"""Entrypoint for the grader that writes a specific text line to the output file."""
# Entry validated: output is 1-280 chars, one line, deterministic.

import os
from pathlib import Path

LINE = "My self driving car refused to navigate to the gym this morning on the grounds that it has too much dignity to witness my squat form.\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    output_dir = Path(out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"

    content = LINE

    if not (1 <= len(content) <= 280 and content.strip()):
        raise ValueError("Content validation failed.")

    output_path.write_text(content, encoding="utf-8")

    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
