"""Sum of the 22 sourced hemiperfect numbers <= 10^18 from A159907.

Pure arithmetic over values already established in the library
(research/summaries/hemiperfect_below_1e18_oracle.md). This is an
independent recomputation so the run does not have to trust a recalled sum.
"""
from collections import defaultdict

# (abundancy, [values]) - exact integers from the oracle note's classification.
BY_ABUNDANCY = [
    ("3/2", [2]),
    ("5/2", [24, 91963648, 10200236032]),
    ("7/2", [4320, 4680, 26208, 20427264, 197064960, 21857648640,
             57575890944, 88898072401645056, 301183421949935616]),
    ("9/2", [8910720, 17428320, 8583644160, 57629644800, 206166804480,
             1416963251404800, 15338300494970880]),
    ("11/2", [17116004505600, 75462255348480000]),
]

def main():
    allvals = []
    total = 0
    per_r = defaultdict(int)
    for r, vals in BY_ABUNDANCY:
        for v in vals:
            assert 0 < v <= 10**18, (r, v)
            allvals.append(v)
            total += v
            per_r[r] += v
    n = len(allvals)
    assert n == 22, f"expected 22 values, got {n}"
    assert len(set(allvals)) == n, "values must be distinct"
    print("count =", n)
    for r in sorted(per_r):
        print(f"{r}: {len([v for a,vv in BY_ABUNDANCY for v in vv if a==r])} values, "
              f"sum={per_r[r]}")
    print("TOTAL SUM =", total)
    print("sorted:", sorted(allvals))
    return total

if __name__ == "__main__":
    main()
