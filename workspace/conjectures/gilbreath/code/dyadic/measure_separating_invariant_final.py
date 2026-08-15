#!/usr/bin/env python3
"""Clean, correctly-labelled measurement of the 2-adic separating invariant
on the three/four bit strings, using the canonical lib.rightdiag path.

Conventions tested explicitly (they differ by a constant shift of the bit
index, which is the only freedom in the 2-then-odds build):

  C1  h[j] governs gap q_{j+2}->q_{j+3}   <- on-disk script + claimed table
  C2  h[j] governs gap q_{j+3}->q_{j+4}   <- literal wording in the task brief

q1=2, q2=3.  A "2-then-odds" sequence: gap = 2 if bit==1 else 4.

nu2(n) = # of 2s in the maximal {0,2} suffix of the right diagonal
delta(q_n) (lib.rightdiag.cycle_and_nu2, canonical).  Density nu2(n)/n,
exponent log nu2 / log n.

Four families: (a) Thue-Morse, (b) odd-factor P=3 = [0,0,1] periodic,
(c) REAL primes' actual right diagonal (ground truth), (d) the primes' mod-4
switch bits re-fed through the same 2/4 reconstruction:
  switch h[j] = [gap_j mod 4 == 2], gap_j = p_{j+1} - p_j.
Primes from lib.gilbreath.primes_up_to(400000) (~33860 primes).

Exact integers throughout; floats only for /n and log.
"""
import math
from lib.rightdiag import incremental_diagonals, cycle_and_nu2
from lib.gilbreath import primes_up_to


def build2thodds(h_bits, n_terms, offset):
    """Return q = [q1,q2,...] of length n_terms, q1=2, q2=3.  bit h[j]
    governs gap q_{j+offset+1}->q_{j+offset+2}:
      offset 1 -> q_{j+2}->q_{j+3}  (C1, on-disk/claimed)
      offset 2 -> q_{j+3}->q_{j+4}  (C2, task-literal)."""
    q = [2, 3]
    while len(q) < n_terms:
        g = len(q) - 1                 # gap g = q_{g+1}->q_{g+2} being appended
        j = g - offset
        q.append(q[-1] + (2 if h_bits[j] else 4))
    return q[:n_terms]


def thue_morse_word(n):
    return [bin(j).count("1") & 1 for j in range(n)]


def nu2_curve(seq, ns):
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
    print(f"{'n':>8} {'nu2':>8} {'nu2/n':>9} {'log nu2/log n':>14}")
    for n in ns:
        v = curve.get(n)
        if v is None:
            continue
        e = (math.log(v) / math.log(n)) if v > 0 else 0.0
        print(f"{n:>8} {v:>8} {v/n:>9.4f} {e:>14.3f}")
    print()


CLAIMED = {
    "TM":   ([0.270,0.145,0.078,0.041,0.022,0.011], 0.459),
    "P3":   ([0.660,0.660,0.664,0.666,0.666,0.667], 0.951),
    "TRUE": ([0.430,0.490,0.498,0.496,0.497,0.493], 0.915),
    "RECON":([0.430,0.495,0.502,0.499,0.498,0.494], None),
}


def measure_all(offset, ns, Nmax, primes):
    tm = thue_morse_word(Nmax + 2 + offset)
    c_tm = nu2_curve(build2thodds(tm, Nmax + 1, offset), ns)

    p3 = [0, 0, 1] * ((Nmax + 2 + offset) // 3 + 1)
    c_p3 = nu2_curve(build2thodds(p3, Nmax + 1, offset), ns)

    c_true = nu2_curve(primes[:Nmax + 1], ns)

    h_recon = [1 if ((primes[j + 1] - primes[j]) % 4 == 2) else 0
               for j in range(1, Nmax + 2 + offset)]
    c_recon = nu2_curve(build2thodds(h_recon, Nmax + 1, offset), ns)

    return {"TM": c_tm, "P3": c_p3, "TRUE": c_true, "RECON": c_recon}


def main():
    ns = [100, 200, 500, 1000, 2000, 4000]
    Nmax = max(ns)
    primes = primes_up_to(400000)
    print("num primes <= 400000:", len(primes), "\n")

    for offset, cname, cdesc in (
            (1, "C1", "h[j] governs gap q_{j+2}->q_{j+3}  (on-disk / claimed)"),
            (2, "C2", "h[j] governs gap q_{j+3}->q_{j+4}  (task literal)")):
        print("=" * 70)
        print("CONVENTION %s : %s" % (cname, cdesc))
        print("=" * 70)
        curves = measure_all(offset, ns, Nmax, primes)
        report("Thue-Morse", ns, curves["TM"])
        report("odd-factor P=3 [0,0,1]", ns, curves["P3"])
        report("REAL PRIMES (ground truth)", ns, curves["TRUE"])
        report("primes mod-4 switch bits, 2/4 reconstruction", ns,
               curves["RECON"])

        for fam, curve in curves.items():
            dens = [curve[n] / n for n in ns]
            expo = math.log(curve[4000]) / math.log(4000) if curve[4000] > 0 \
                else 0.0
            cd, ce = CLAIMED[fam]
            # match: densities within 0.0006 (rounding) and exponent within 0.004
            md = all(abs(a - b) <= 0.0006 for a, b in zip(dens, cd))
            me = (ce is None) or abs(expo - ce) <= 0.004
            print(f"VERDICT {cname} {fam:5s}: densities "
                  f"{[' '.join('%.3f'%d for d in dens)]} match={md}, "
                  f"exp@4000={expo:.3f} match={me}")

    # raw nu2 of the reconstruction vs TRUE primes under C1 (the faithful-shadow
    # check from the claim): raw pairs (43,98,249,496,993,1973) vs
    # (43,99,251,499,995,1975).
    print("\n" + "=" * 70)
    print("Raw nu2 TRUE vs RECON under C1 (on-disk) convention")
    print("=" * 70)
    h_recon = [1 if ((primes[j + 1] - primes[j]) % 4 == 2) else 0
               for j in range(1, Nmax + 3)]
    c_true = nu2_curve(primes[:Nmax + 1], ns)
    c_recon = nu2_curve(build2thodds(h_recon, Nmax + 1, 1), ns)
    print("  TRUE :", [c_true[n] for n in ns])
    print("  RECON:", [c_recon[n] for n in ns])
    print("  claimed TRUE (43,98,249,496,993,1973)  RECON (43,99,251,499,995,1975)")
    print("  TRUE raw match :", [c_true[n] for n in ns] == [43,98,249,496,993,1973])
    print("  RECON raw match:", [c_recon[n] for n in ns] == [43,99,251,499,995,1975])
    print("DONE")


if __name__ == "__main__":
    main()
