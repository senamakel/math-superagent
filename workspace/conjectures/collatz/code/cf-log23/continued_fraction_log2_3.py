"""Continued fraction of log_2(3) — exact, verified, with correct convergents.

The CF extraction is verified against Crandall 1978 (first 50 terms) and
stable under doubling precision.

Convergents use the standard recurrence:
  p_{-2}=0, p_{-1}=1,  p_n = a_n * p_{n-1} + p_{n-2}
  q_{-2}=1, q_{-1}=0,  q_n = a_n * q_{n-1} + q_{n-2}

The q_n (convergent denominators) are the odd-member counts K that appear
in cycle-exclusion bounds:
  - Eliahou 1993: K > q_21 = 6,586,818,670  (period > p_21 = 10,439,860,591)
  - Simons-de Weger 2005: K > q_23 = 137,528,045,312 (for m >= 76)
  - Hercher 2022: K > 1.375e11 ≈ q_23 (Corollary 29)

This program computes the terms, convergents, and checks the match against
these literature bounds.
"""
from __future__ import annotations

import sys
import math
import mpmath as mp

CRANDALL = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15,
            1, 9, 2, 5, 7, 1, 1, 4, 8, 1, 11, 1, 20, 2, 1, 10, 1, 4, 1, 1, 1,
            1, 1, 37, 4, 55, 1, 1, 49]


def extract(dps: int, n: int) -> list[int]:
    mp.mp.dps = dps
    x = mp.log(3) / mp.log(2)
    terms: list[int] = []
    for _ in range(n):
        a = int(mp.floor(x))
        terms.append(a)
        x = 1 / (x - a)
    return terms


def convergents(terms: list[int]) -> tuple[list[int], list[int]]:
    """Return (p_n, q_n) for n = 0..len(terms)-1."""
    p = [0, 1]  # p_{-2}, p_{-1}
    q = [1, 0]  # q_{-2}, q_{-1}
    for a in terms:
        p.append(a * p[-1] + p[-2])
        q.append(a * q[-1] + q[-2])
    return p[2:], q[2:]  # p_0.., q_0..


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    dps = max(40, 8 * n)
    terms = extract(dps, n)
    terms_2x = extract(2 * dps, n)

    print(f"terms a_0..a_{n-1}:")
    print(terms)

    # Crandall check
    match_crandall = terms[:50] == CRANDALL
    print(f"\nfirst 50 match Crandall 1978: {match_crandall}")
    if not match_crandall:
        for i, (a, b) in enumerate(zip(terms, CRANDALL)):
            if a != b:
                print(f"  first mismatch at index {i}: ours {a}, Crandall {b}")
                break

    # Precision stability
    stable_upto = n
    for i, (a, b) in enumerate(zip(terms, terms_2x)):
        if a != b:
            stable_upto = i
            break
    print(f"stable under 2x precision: a_0..a_{stable_upto - 1}")

    pn, qn = convergents(terms)
    print(f"\nconvergent denominators q_0..q_{len(qn)-1}:")
    print(qn)
    print(f"\nconvergent numerators p_0..p_{len(pn)-1}:")
    print(pn)

    # Check the literature bounds
    print("\n=== Literature bound checks ===")
    # Eliahou 1993: q_21 = 6,586,818,670, p_21 = 10,439,860,591
    print(f"q_21 = {qn[21]:,}")
    print(f"p_21 = {pn[21]:,}")
    print(f"  Eliahou odd-member bound K > q_21 = {qn[21]:,}  ({qn[21] == 6586818670})")
    print(f"  Eliahou period bound  > p_21 = {pn[21]:,}  ({pn[21] == 10439860591})")

    # Simons-de Weger / Hercher: q_23
    print(f"q_23 = {qn[23]:,}")
    print(f"  Hercher bound K > 1.375e11 ≈ {qn[23]:.4e}")

    # Find the convergent that gives 1.375e11 more precisely
    print(f"\nConvergent ratios (K+L)/K = p_n/q_n and differences from log2(3):")
    log23 = math.log(3) / math.log(2)
    for i in range(min(30, len(qn))):
        ratio = pn[i] / qn[i]
        diff = abs(ratio - log23)
        print(f"  n={i:2d}: p/q = {pn[i]:>15,}/{qn[i]:>15,} = {ratio:.15f}  diff={diff:.2e}")

    # Growth of q_n
    print("\nlog10(q_n)/n (growth rate estimate):")
    for k in range(1, min(101, len(qn))):
        if k % 10 == 0:
            print(f"  n={k}: {math.log10(qn[k]) / k:.6f}")

    # OEIS: the sequence of a_n is A028507 (log_2 3 continued fraction, offset 0)
    # OEIS: q_n is A076729 (denominators of convergents to log_2 3)
    # Let's see if q_n satisfies a recurrence independent of a_n
    from fractions import Fraction
    # Check: q_n / q_{n-1} ≈ phi for large n? Not really because large terms
    # cause jumps. But the growth rate is controlled by the geometric mean of terms.
    print(f"\nGeometric mean of first {len(terms)} a_n: {math.exp(sum(math.log(max(a,1)) for a in terms)/len(terms)):.4f}")


if __name__ == "__main__":
    main()