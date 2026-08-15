#!/usr/bin/env python3
"""Independent hand-check reproduction of the G-supply-transfer refutation
on the consecutive-odds family, using ONLY the run's own definitions and the
runtime's documented oracle numbers in problem.md.

Consecutive odds is a SETTLED successful class (R2-consecutive-odds-class:
A_k(0)=1 for all k).  The goal is to test the claim

    G-supply-transfer:
      for every SUCCESSFUL 2-then-odds prefix q_1..q_n,
      nu2(q_n) >= (2/3) * w(n)
    where
      w(n)  = #{ j in [2,n-1] : q_{j+1} - q_j ≡ 2 mod 4 }
      nu2   = # of 2s in the maximal {0,2} suffix of the right diagonal.

Right diagonal (Granville's delta, as the run codes it in
code/gap_analysis/nu2_vs_gap_parity.py):
    delta(q_n) = [ A_k(n-k) for k in 0..n-1 ]
and the {0,2} suffix is taken over delta[2:-1]  (the run's tail convention).

For consecutive odds A_0 = (2,3,5,7,9,...,2n-1,...) we have, by the block
lemma / the R2 settlement, A_1 = (1,2,2,2,...), A_2 = (1,0,0,0,...),
A_3 = (1,0,0,...), ...  So for the prefix q_1..q_n (n>=4):
    delta_k = A_k(n-k):
      k=0: A_0(n)   = the (n+1)-th value, i.e. 2n-1 (odd, >= 9)
      k=1: A_1(n-1) = 2
      k=2: A_2(n-2) = 0
      k=3..: A_k(n-k) = 0
    tail = delta[2:-1] = (0,0,...,0)   ->   nu2 = 0
    w = #{j in [2,n-1]} = (n-2)  (every gap is 2 ≡ 2 mod 4)
    (2/3)w = (2/3)(n-2) > 0 for n >= 4, so nu2 >= (2/3)w FAILS.

We reproduce these exact numbers by a tiny exact computation, not a search.
"""
from lib.gilbreath import rows_generator


def delta_and_counts(seq):
    """seq = A_0, entries positions 0..n.  Right diagonal through q_n and the
    two counts, using the run's nu2_vs_gap_parity convention."""
    n = len(seq) - 1
    rows = list(rows_generator(seq, n))
    d = [rows[k][n - k] for k in range(n)]       # the run's diag(n)
    tail = d[2:-1]                                # run's {0,2}-tail window
    i = len(tail)
    while i > 0 and tail[i - 1] in (0, 2):
        i -= 1
    cyc = tail[i:]
    nu2 = cyc.count(2)
    w = sum(1 for j in range(2, n) if (seq[j + 1] - seq[j]) % 4 == 2)
    return rows, d, nu2, w


def bottom_entry(seq):
    rows = list(rows_generator(seq, len(seq) - 1))
    return rows[len(seq) - 1][0]


def main():
    print("Success marker of each prefix is the bottom-entry A_{n-1}(0) == 1.")
    lows = []
    for n in range(4, 12):
        seq = [2] + [3 + 2 * i for i in range(n)]      # 2,3,5,...,(2n-1) ... length n+1
        seq = seq[:n + 1]
        bottom = bottom_entry(seq)
        rows, d, nu2, w = delta_and_counts(seq)
        required = (2 / 3) * w
        viol = not (nu2 >= (2 / 3) * w)
        print(f"n={n:2d} bottom={bottom} (success={bottom==1}) | "
              f"delta={d} tail nu2={nu2} w={w} (2/3)w={required:.3f} | "
              f"nu2 >= (2/3)w? {not viol}")
        if viol and bottom == 1:
            lows.append(n)
    print()
    print("Successful prefixes n where G-supply-transfer is violated:",
          lows if lows else "NONE")

    # Explicit smallest one
    n = 4
    seq = [2, 3, 5, 7, 9]
    rows, d, nu2, w = delta_and_counts(seq)
    print("\nExplicit n=4, q=(2,3,5,7,9):")
    for k, r in enumerate(rows):
        print(f"  A_{k} = {list(r)}")
    print("  delta(q_4) =", d, " nu2 =", nu2, " w =", w,
          " nu2 >= (2/3)w ?", nu2 >= (2/3) * w)


if __name__ == "__main__":
    main()
