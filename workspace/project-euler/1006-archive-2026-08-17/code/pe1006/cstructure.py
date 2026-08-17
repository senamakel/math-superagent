"""Analyze the C(j,l;k) matrices in code/out/structure.json.

Reads the brute-force structural dump (k=1..60) and reports:
  (1) number of distinct values of C(j,l;k) over all pairs (j,l), vs k;
  (2) the set of distinct values, and the diagonal values N(j;k)=C(j,j;k);
  (3) whether C(j,l;k) depends only on (l-j) or also on absolute position.
Exact integers only.
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
STRUCT = os.path.join(HERE, "..", "out", "structure.json")


def load():
    with open(STRUCT) as fh:
        return json.load(fh)


def distinct_values_matrix(cmat, k):
    """Return Counter of all values C(j,l;k), j<=l<k."""
    cnt = Counter()
    for j in range(k):
        for l in range(j, k):
            cnt[int(cmat[f"{j},{l}"])] += 1
    return cnt


def diagonal(cmat, k):
    return [int(cmat[f"{j},{j}"]) for j in range(k)]


def main():
    data = load()
    print("k : ndistinct_values : distinct_values : diag_N")
    for k in range(1, 61):
        d = data[str(k)]
        cmat = d["C"]
        cnt = distinct_values_matrix(cmat, k)
        vals = sorted(cnt)
        diag = diagonal(cmat, k)
        print(f"{k:3d} : {len(vals):4d} : {vals} : {diag}")


if __name__ == "__main__":
    main()
