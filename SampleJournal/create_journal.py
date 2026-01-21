#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path

def main():
    script_dir = Path(__file__).parent
    filename = datetime.now().strftime("%Y-%m-%d-%A.md")
    filepath = script_dir / filename
    filepath.touch()
    print(f"Created: {filepath}")

if __name__ == "__main__":
    main()
