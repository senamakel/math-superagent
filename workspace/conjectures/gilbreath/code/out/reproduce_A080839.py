"""Reproduce OEIS A080839 first terms by brute force (oracle), NOT reading the catalogue.

A080839(n) = number of positive increasing integer sequences of length n
whose Gilbreath transform (the diagonal of leading successive absolute
differences, i.e. the leading entry of each row of the successive-abs-difference
triangle) is (1,1,1,...).

The catalogue statement gives the sequence bound: the fastest-growing such
sequence of length n is 1,2,4,8,...,2^(n-1) (last element 2^(n-1)); the
slowest is 1,2,4,6,...,2(n-1). So every count is achieved inside last <= 2^(n-1),
which bounds the brute force.

Definition check against the worked example: {1,2,4,6,10} (length 5) has
  1
  2 1
  4 2 1
  6 2 0 1
 10 4 2 2 1   -> diagonal 1,1,1,1,1, so it is counted.
"""
from itertools import combinations

def gilbreath_transform_all_ones(seq):
    """True iff the leading entry of every successive-abs-difference row is 1
    (including the first row's leading entry = seq[0], so we need seq[0]==1)."""
    row = list(seq)
    while row:
        if row[0] != 1:
            return False
        row = [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
    return True

def count(n):
    # a_0 = 1 (leading entry of row 0), strictly increasing, last <= 2^(n-1).
    if n == 1:
        # sequences of length 1 with leading entry 1 and all-1 transform: [1]
        return 1
    last_max = 2**(n-1)
    # a_0 = 1; choose remaining n-1 distinct values in {2..last_max}
    cnt = 0
    for rest in combinations(range(2, last_max+1), n-1):
        seq = (1,) + tuple(rest)
        if gilbreath_transform_all_ones(seq):
            cnt += 1
    return cnt

if __name__ == "__main__":
    expected = {1:1, 2:1, 3:1, 4:2, 5:6, 6:27, 7:180, 8:1786}
    got = {}
    for n in range(1, 9):
        got[n] = count(n)
        mark = "OK" if got[n] == expected.get(n) else f"MISMATCH (expected {expected.get(n)})"
        print(f"n={n}: count={got[n]}  {mark}")
    print("reproduced:", [got[n] for n in range(1,9)])
    print("catalogue :", [1,1,1,2,6,27,180,1786])
