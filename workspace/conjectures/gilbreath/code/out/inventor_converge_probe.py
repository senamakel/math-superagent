#!/usr/bin/env python3
"""Resolve the exact relationship between the true {0,2}-suffix count nu2 and
the two candidate 'fold' statistics, on Thue-Morse and the real primes.

Conventions, all made explicit:
  q = 2-then-odds, q_1=2, q_2=3, gaps g_j = q_{j+1}-q_j (j>=2) even.
  halved-gap bit  h[j] = (g_j // 2) mod 2  for j>=2  (h[2],h[3],...).
  right diagonal through q_n : delta_k = A_k[n-k], k=0..n.
  body = delta_2..delta_{n-1};  maximal {0,2} suffix of body = the suffix
  whose cells are all 0 or 2, maximal from the right.  nu2 = # of 2s in it.

Three statistics compared at each n:
  A) true nu2  (cycle_and_nu2, maximal {0,2} suffix of the diagonal body)
  B) fold weight of the halved-gap bits over the fixed ancestor window
     [2, n-1]  (rule90fold.fold_weight, Pascal-row-(k-1) mod 2 XOR),
     which is the mod-4 parity count (fires on halved values odd, i.e.
     actual diagonal values 2,6,10,...).
  C) number of cells of the whole diagonal body (not suffix-restricted)
     that are exactly 2.
"""
from lib.gilbreath import primes_up_to, rows_generator
from lib.rightdiag import cycle_and_nu2, delta_diagonal
from lib.rule90fold import halved_gap_bits, fold_weight_h


def thue_morse(nbits):
    return [(j.bit_count() % 2) for j in range(nbits)]


def q_from_gaps(hbits, n):
    """Build q_1..q_{n+1} with q_1=2, q_2=3, and g_j = 2 + 2*hbits[j-2] for j>=2.
    hbits[0] corresponds to g_2 (gap from 3 to q_3)."""
    q = [2, 3]
    for j in range(2, n + 1):
        g = 2 + 2 * hbits[j - 2]
        q.append(q[-1] + g)
    return q[:n + 1]


def diag_from_seq(q):
    """right diagonal delta(q_n) via the in-place recurrence."""
    D = [q[0]]
    for n in range(1, len(q)):
        newD = [0] * (n + 1)
        newD[0] = q[n]
        for k in range(1, n + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
    return D


def stats_for_seq(q, hbits, nmax):
    print(f"{'n':>4} {'true_nu2':>9} {'fold_w':>8} {'exact2_whole':>12} "
          f"{'foldminustrue':>14}")
    for n in range(1, nmax + 1):
        D = diag_from_seq(q[:n + 1])
        tau, nu2 = cycle_and_nu2(D)
        body = D[1:-1]  # delta_1 .. delta_{n-1} (skip terminal and D[0]=q)
        exact2 = sum(1 for x in body if x == 2)
        # fold weight over the window [2, n-1] of columns: m = n-2 bits
        m = n - 2
        if m <= 0:
            fw = 0
        else:
            fw = fold_weight_h(hbits[:m], m)
        print(f"{n:>4} {nu2:>9} {fw:>8} {exact2:>12} {fw-nu2:>14}")


def main():
    # ---- Thue-Morse 2-then-odds ----
    nmax = 40
    print("== Thue-Morse halved-gap bits, n=1..%d ==" % nmax)
    hbits = thue_morse(nmax + 5)
    q = q_from_gaps(hbits, nmax)
    stats_for_seq(q, hbits, nmax)

    # ---- real primes ----
    print("\n== real primes, n=1..40 ==")
    P = primes_up_to(400)
    # halved gap bits for the prime sequence: h[c] for c>=1 (gap ending at index c)
    hc = halved_gap_bits(P)
    qp = P[:nmax + 1]
    stats_for_seq(qp, hc, nmax)


if __name__ == "__main__":
    main()
