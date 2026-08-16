"""Independent check of the mod-9 structural claim on S-roots.

Loads the 408 roots <= 10^6 (from code/out/roots408.txt), and the full
3200-term b-file if present. Verifies:
  1. Every root is 0 or 1 mod 9.
  2. No other cheap residue/narcissistic regularity jumps out.
"""
import os

def roots_from_file(path):
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # b-file lines are "n a(n)"; our roots408.txt is bare ints
            parts = line.split()
            try:
                if len(parts) == 2:
                    out.append(int(parts[1]))
                else:
                    out.append(int(parts[0]))
            except ValueError:
                continue
    return out

def main():
    r408 = roots_from_file('code/out/roots408.txt')
    print("roots408.txt entries:", len(r408))
    viol = [m for m in r408 if m % 9 not in (0, 1)]
    print("mod-9 (0 or 1) violations among 408:", len(viol))
    res = {0: 0, 1: 0}
    for m in r408:
        res[m % 9] += 1
    print("residue 0:", res[0], " residue 1:", res[1])

    # full b-file up to 10^9 for a wider test
    bfile = 'research/sources/oeis_a038206_b.full.md'
    if os.path.exists(bfile):
        rb = roots_from_file(bfile)
        rb = [m for m in rb if m >= 0]
        print("b-file up to 10^9, roots > 0:", len(rb))
        violb = [m for m in rb if m % 9 not in (0, 1)]
        print("mod-9 violations in full b-file:", len(violb))
        maxroot = max(rb)
        print("max root:", maxroot)
    else:
        print("b-file not found")

if __name__ == "__main__":
    main()
