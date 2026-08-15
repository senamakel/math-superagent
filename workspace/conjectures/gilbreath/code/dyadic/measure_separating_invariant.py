#!/usr/bin/env python3
"""
Measure the 2-adic separating invariant (Directive 66 item 2) on three
strings with the SAME code path.

Task: measure-2adic-separating-invariant-three-strings. The corrected open
question is: which finer invariant separates Thue-Morse (nu2 = O(log n)) from
the odd-factor families (nu2 ~ c*n, linear), and where do the real primes
sit on it. The operational ground-truth shadow of the named invariant
(2-adic spectral non-rigidity, i.e. mass of h in the non-nilpotent part of
sigma = I+S) is the TRUE supply density nu2(n)/n, computed by the actual
right-diagonal dynamics -- NOT the subset-zeta parity statistic, which was
already shown to mis-identify nu2 (thue-morse-subset-zeta-confirmed-identification-refuted).

The three strings, all converting a bit string h into a 2-then-odds sequence
q (q_1=2, q_2=3, gap q_{j+2}->q_{j+3} = 2 if h[j]==1 else 4):

  1. Thue-Morse    h[j] = wt(j) mod 2                    (aperiodic, 2-automatic)
  2. odd-factor    h   = periodic word [0,0,1] (P=3)     (dyadically non-rigid)
  3. real primes   h[j] = (gap//2) mod 2 for the prime gaps ending at index j

nu2(q_n) = # of 2s in the maximal {0,2} suffix of the right diagonal
           delta(q_n), using lib.rightdiag.cycle_and_nu2 (canonical).
Density is nu2(n)/n ; the exponent is log nu2 / log n (linear <=> ~1,
Thue-Morse sublinear <=> -> 0).

Regression (held value, dyadic_inf_measure): period-3 gives nu2 ~ 0.647*n
at n ~ 102, and stays ~0.5 at n=20000. We assert the density at n=200
for P=3 is in [0.4, 0.8].

Cost: for each 2-then-odds sequence of length N+1, incremental_diagonals is
O(N^2) diffs with O(N) memory (one row live). Nmax = 4096 -> ~8.4M diffs per
string, trivial.
"""
import math
import sys

from lib.rightdiag import incremental_diagonals, cycle_and_nu2
from lib.gilbreath import primes_up_to


def build_seq(h_pattern, n_terms):
    """2-then-odds q_1..q_{n_terms}.  bit h[j] governs gap q_{j+2}->q_{j+3};
    gap = 2 if bit else 4.  q_1=2, q_2=3, so A_1 = (1, even, even, ...)."""
    period = len(h_pattern)
    q = [2, 3]
    while len(q) < n_terms:
        m = len(q)          # appending q_{m+1}; gap is q_m->q_{m+1}
        j = m - 2           # bit index (h[0] = gap 3->5)
        q.append(q[-1] + (2 if h_pattern[j % period] else 4))
    return q[:n_terms]


def thue_morse_word(n):
    """Thue-Morse bits h[j] = wt(j) mod 2."""
    out = []
    for j in range(n):
        out.append(bin(j).count("1") & 1)
    return out


def nu2_curve(seq, ns):
    """For each n in ns, nu2 at q_n (requires len(seq) >= max(ns)+1).
    incremental_diagonals yields delta(q_n) for n=0..len-1."""
    diags = incremental_diagonals(seq)
    res = {}
    maxn = max(ns)
    for n, d in enumerate(diags):
        if n in ns:
            _, nu2 = cycle_and_nu2(d)
            res[n] = nu2
        if n >= maxn:
            break
    return res


def report(name, ns, curve):
    print(f"=== {name} ===")
    print(f"{'n':>8} {'nu2':>10} {'nu2/n':>10} {'log nu2/log n':>14}")
    for n in ns:
        v = curve.get(n, None)
        if v is None:
            continue
        dens = v / n
        expo = (math.log(v) / math.log(n)) if v > 0 else 0.0
        print(f"{n:>8} {v:>10} {dens:>10.4f} {expo:>14.3f}")
    print()


def main():
    ns = [100, 200, 500, 1000, 2000, 4000]
    Nmax = max(ns)

    # 1. Thue-Morse
    tm = thue_morse_word(Nmax + 1)
    q_tm = build_seq(tm, Nmax + 1)
    c_tm = nu2_curve(q_tm, ns)
    report("Thue-Morse (h[j] = wt(j) mod 2)", ns, c_tm)

    # 2. odd-factor P=3
    p3 = [0, 0, 1]
    q_p3 = build_seq(p3, Nmax + 1)
    c_p3 = nu2_curve(q_p3, ns)
    report("odd-factor periodic [0,0,1] (P=3)", ns, c_p3)

    # 3. real primes
    PRIME_SIEVE = 400000          # ~33860 primes (matches witnesses.json)
    primes = primes_up_to(PRIME_SIEVE)
    if len(primes) <= Nmax + 1:
        print("not enough primes; need", Nmax + 1, "have", len(primes))
        sys.exit(1)

    # 3a. GROUND TRUTH: the actual prime right diagonal (real gaps, incl. 6,10,...)
    q_true = primes[:Nmax + 1]
    c_true = nu2_curve(q_true, ns)
    report("REAL PRIMES, actual right diagonal (ground truth)", ns, c_true)

    # 3b. the mod-4 switch bit string h[j] = (gap//2)%2 of the real primes,
    #     fed through the SAME 2/4 reconstruction as TM and P=3 (bit string alone)
    # halved gap bit h[c] for c>=1: (gap ending at index c)//2 mod 2
    # need bits for j = 0..Nmax-1 -> gaps ending at prime indices 1..Nmax
    h_primes = [((primes[c + 1] - primes[c]) // 2) % 2
                for c in range(1, Nmax + 1)]
    q_primes = build_seq(h_primes, Nmax + 1)
    c_primes = nu2_curve(q_primes, ns)
    report("real prime halved-gap bits, 2/4 reconstruction", ns, c_primes)

    # Regression: period-3 density at n=200 in [0.4, 0.8]
    d200 = c_p3[200] / 200
    ok_p3 = 0.4 <= d200 <= 0.8
    print(f"REGRESSION P=3 nu2(200)/200 = {d200:.4f}  in [0.4,0.8]: {ok_p3}")

    # Separator verdict: Thue-Morse density must be a small fraction of P=3
    # and of the true primes at the same n (sublinear vs linear).
    for n in (1000, 4000):
        ratio_tm = c_tm[n] / max(1, c_p3[n])
        ratio_pr_true = c_true[n] / max(1, c_p3[n])
        print(f"SEPARATOR n={n}: nu2(TM)/nu2(P3)={ratio_tm:.4f}  "
              f"nu2(TRUE primes)/nu2(P3)={ratio_pr_true:.4f}")
    print("DONE")


if __name__ == "__main__":
    main()
