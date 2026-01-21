#!/usr/bin/env python3
"""Export Mermaid diagrams from a markdown file to PNG (PowerPoint compatible)."""

import subprocess
import sys
from pathlib import Path


def export_mermaid(input_file: Path, scale: int = 3) -> bool:
    """
    Export mermaid diagrams from a markdown file to PNG.

    Args:
        input_file: Path to the markdown file containing mermaid diagrams
        scale: Resolution scale factor (default 3x)

    Returns:
        True if export succeeded, False otherwise
    """
    output_file = input_file.with_suffix(".png")

    result = subprocess.run(
        ["mmdc", "-i", str(input_file), "-o", str(output_file), "-s", str(scale)],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print(result.stdout, end="")
        print(f"Exported to: {output_file}")
        return True
    else:
        print(f"Error: Export failed", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        return False


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    if not input_file.exists():
        print(f"Error: File '{input_file}' not found", file=sys.stderr)
        sys.exit(1)

    success = export_mermaid(input_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
