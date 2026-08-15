#!/usr/bin/env python3
"""Cross-check the brute-force worst case: extend a suspected death sequence
out to large width and confirm the first failure is NOT a width artifact."""
import sys
sys.path.insert(0, "/workspace/code")
from refute.leftmost_decides import build_from_gaps, first_failure_row

def main():
    # Try any deaths found at wider width
    for gaps in ([2,2,4,6], [2,2,4,6,6], [2,2,2,4,6], [2,4,2,6], [2,4,2,6,6]):
        for W in (80, 200):
            fr = first_failure_row(gaps, W)
            print(f"gaps={gaps} W={W} -> {fr}")

if __name__ == "__main__":
    main()
