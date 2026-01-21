#!/usr/bin/env python3
"""Export Mermaid diagrams from a markdown file to SVG (PowerPoint compatible)."""

import subprocess
import sys
from pathlib import Path


def get_config_file() -> Path:
    """Get the mermaid config file path (same directory as this script)."""
    return Path(__file__).parent / "mermaid-config.json"


def export_mermaid(input_file: Path) -> bool:
    """
    Export mermaid diagrams from a markdown file to SVG.

    Uses htmlLabels:false config for native SVG text (no foreignObject).

    Args:
        input_file: Path to the markdown file containing mermaid diagrams

    Returns:
        True if export succeeded, False otherwise
    """
    directory = input_file.parent
    base_name = input_file.stem
    svg_output = directory / f"{base_name}.svg"
    config_file = get_config_file()

    args = ["mmdc", "-i", str(input_file), "-o", str(svg_output)]
    if config_file.exists():
        args.extend(["-c", str(config_file)])

    result = subprocess.run(args, capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout, end="")
        print(f"Exported to: {svg_output}")
        return True
    else:
        print("Mermaid export failed", file=sys.stderr)
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
