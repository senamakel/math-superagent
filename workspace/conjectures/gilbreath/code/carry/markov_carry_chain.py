#!/usr/bin/env python3
"""Part 3: carry-decorrelation Markov chain.

Claim tested (carry-decorrelation-nu2-supply, step 1c): a 2-state Markov carry
chain with Bernoulli(1/2) stationary density gives stationary count density 1/2,
matching nu2/n ~ 0.5.

The Diaconis-Fulman carry of the two-operand addition a+b is
    c' = majority(a_i, b_i, c)
with a_i, b_i the i.i.d. bit streams. For uniform bits this is the chain
    P(c'=1 | c=0) = 1/4,  P(c'=1 | c=1) = 3/4,
i.e. transition matrix [[3/4,1/4],[1/4,3/4]], whose unique stationary measure
is Bernoulli(1/2), so the long-run density of carry=1 is exactly 1/2.

We verify BOTH exactly (stationary vector as the nullspace of the generator)
and empirically (a long Markov simulation) and report against the measured
nu2/n. Then we feed the ACTUAL prime halved-gap bits through the same carry/
borrow chain and report its count density vs nu2/n, so the claim "tracks, not
equals" is stated with the measured gap.
"""
import numpy as np
from lib.gilbreath import primes_up_to

BOUND = 1_000_000
MAX_N = 5000
KEEP = MAX_N + 3


def majority(a, b, c):
    return (a + b + c >= 2)


def main():
    # --- Exact stationary measure of the Markov chain ---------------------
    # P = [[3/4, 1/4],[1/4, 3/4]] with rows "c out", columns "c in"? Use
    # transition T[i][j] = P(c' = j | c = i). Solve pi T = pi.
    T = np.array([[0.75, 0.25], [0.25, 0.75]])
    d = T - np.eye(2)
    d[-1] = [1, 1]
    rhs = np.array([0.0, 1.0])
    pi = np.linalg.solve(d, rhs)
    print("=== Part 3a: two-operand addition carry chain c'=majority(a,b,c) ===")
    print("transition P(c'=1|c=0)=1/4, P(c'=1|c=1)=3/4:")
    print("  T = %s" % T.tolist())
    print("  exact stationary vector pi = %s (Bernoulli(1/2) density %.6f)"
          % (pi.round(6).tolist(), pi[1]))

    # --- Empirical: long Markov simulation with i.i.d. uniform bits --------
    rng = np.random.default_rng(1)
    L = 4_000_000
    a = rng.integers(0, 2, L)
    b = rng.integers(0, 2, L)
    c = 0
    counts = 0
    ncarry = 0
    # run as a single chain (carry carries over bit to bit)
    for i in range(L):
        c = majority(a[i], b[i], c)
        counts += 1
        ncarry += c
    print("  empirical (single chain, L=%d iid Bern(1/2) operand bits): "
          "carry density = %.6f" % (L, ncarry / counts))

    # --- Now the two's-complement subtraction borrow chain fed by the REAL
    #     prime halved-gap bits ---------------------------------------------
    P = primes_up_to(BOUND)[:KEEP]
    hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
    # The borrow chain of the subtraction of consecutive halved gaps
    # g_{j+1}=h_j-bit as operand: run c' from (a + ~b + 1) with the LSB-first
    # bit planes of consecutive halved gaps.
    # Consecutive halved gaps as integers
    half = [(P[i + 1] - P[i]) // 2 for i in range(len(P) - 1)]
    m = 8
    total_pos = 0
    carry_total = 0
    for i in range(len(half) - 1):
        a = half[i]
        b = half[i + 1]
        # borrow chain of two's-complement subtraction a - b = a + ~b + 1
        c = 1
        for bit in range(m):
            x = (a >> bit) & 1
            y = 1 - ((b >> bit) & 1)
            s = x + y + c
            c = 1 if s >= 2 else 0
            carry_total += c
            total_pos += 1
    print("\n=== Part 3b: two's-complement borrow chain on CONSECUTIVE halved")
    print("    prime gaps (a=G[i], b=G[i+1], m=%d fixed width) ===" % m)
    print("  borrow density (count of carry-out=1 over all bit positions) = %.6f"
          % (carry_total / total_pos))
    print("  (vs stationary 1/2 for an iid-fed infinite-width chain)")

    # compare with the measured nu2/n at n=3999 and n=1600 etc.
    print("\n=== Part 3c: comparison of stationary 1/2 vs measured nu2/n ===")
    print("  stationary carry density (exact): 0.500000")
    print("  measured nu2/n (n=3999):           0.5121")
    print("  measured nu2/n range (n>=17):     [0.2941, 0.6842] (fluctuates)")
    print("  borrow density on real gaps:      %.6f" % (carry_total / total_pos))


if __name__ == "__main__":
    main()
