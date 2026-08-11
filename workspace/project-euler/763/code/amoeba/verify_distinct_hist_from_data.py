#!/usr/bin/env python3
"""Definition-check: count DISTINCT level-histograms in data/level_N.txt.

A level histogram of a config is the tuple a_k = #cubes at level k=x+y+z
(the token list before the '|' on each data line).  This reads the existing
data dumps N=2..12 and counts distinct histogram tuples, to confirm we
understand the definition before trusting it against the stated expectation
1,1,2,3,5,8,13,22,36,60,100 for N=2..12.
"""

import sys

EXPECTED = {2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 8, 8: 13, 9: 22, 10: 36,
            11: 60, 12: 100}


def main():
    ok = True
    for n in range(2, 13):
        path = f"/workspace/data/level_{n}.txt"
        histos = set()
        with open(path) as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                toks = line.split("|")[0].split()
                histos.add(tuple(int(t) for t in toks))
        got = len(histos)
        exp = EXPECTED[n]
        status = "OK" if got == exp else "MISMATCH"
        if got != exp:
            ok = False
        print(f"N={n}: distinct_histograms={got} expected={exp} {status}")
    print("ALL MATCH" if ok else "MISMATCH FOUND")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
