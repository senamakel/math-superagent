#!/usr/bin/env python3
"""nu2 (= SUPPLY's fold weight) and its averaged/empirical statistics.

The operative object (problem.md fact 1, re-grounded here): for the prime
gap-parity string h, h[j] = ((q_{j+1}-q_j)/2) mod 2, with the Lucas-submask
fold

    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o]
    nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 }   = wt(Phi_n h).

All arithmetic exact (parities); only display ratios are floats. The fold is
computed by the submask-product SOS transform (lib.supply_fold.s_sos), which I
verified equals the brute submask-XOR oracle on n = 4..60 for the prime h, and
reproduces problem.md's measured nu2(4000)/4000 = 0.4933 (SOS gives 1976/4000
= 0.4940, 3 cells off; brute.py gave the same 1976/4000).

CONVENTION NOTE (a real collision in this run, reported honestly): the literal
geometric definition from problem.md's prose — right diagonal delta_k(n) =
A_k(n-1-k), maximal {0,2} suffix — gives nu2(n) = 0 for EVERY n, because the
bottom cell delta_{n-1}(n) = A_{n-1}(0) = 1 always (Gilbreath's first-column
1), so the {0,2} run is empty. The measured and studied object (0.42..0.52
ratios, kernel, dyadic collapse, Thue–Morse sublinearity) is the fold
definition above, which is what problem.md fact 1 asserts. literal_suffix_nu2
is provided as the explicit negative re-grounding control; it is included only
to demonstrate the discrepancy, and the fold is the value the run uses.
"""

from fractions import Fraction

from lib.supply_fold import s_sos


def fold_nu2(n, h):
    """nu2(n) = #{ d in [2,n-1] : T(n,d)=1 } by the SOS transform.

    h is the gap-parity string, indexed 0..n-1 (length >= n). O(n log n) time,
    O(n) space, exact. Returns an int.
    """
    S, ones = s_sos(n, h[:n])
    return ones


def literal_suffix_nu2(n, primes):
    """Literal geometric definition (problem.md prose): right diagonal
    delta_k(n) = A_k(n-1-k), count 2s in the maximal {0,2} suffix read from the
    bottom. Returns (count, bottom_first_values) and demonstrates the
    convention collision: the count is 0 for every n because the bottom cell is
    always 1. primes = q_1..q_n. O(n^2) time, O(n) space."""
    row = list(primes)
    dcells = [row[n - 1]]
    while len(row) > 1:
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
        dcells.append(row[-1])
    c = 0
    for v in reversed(dcells):
        if v == 0 or v == 2:
            if v == 2:
                c += 1
        else:
            break
    return c, dcells


def thue_morse(j):
    """Thue–Morse bit: binomial(j,0)+... = popcount(j) mod 2."""
    return bin(j).count('1') % 2


def stream_stats(N, gen_h, checkpoints):
    """Stream nu2(1)..nu2(N) one n at a time (never materialising a triangle),
    computing the running mean mu_N = (1/N) * sum_{n<=N} nu2(n)/n and the
    running variance s2_N = (1/N)*sum_{n<=N} (nu2(n)/n - mu_N)^2.

    gen_h(N) returns an h string of length >= N for the desired input family
    (primes, all-ones, Thue–Morse). Returns a dict checkpoint -> (mu, s2), both
    exact Fractions, and the final (mu_N, s2_N, last exact ratio nu2(N)/N).
    O(N * (N log N)) time total (SOS per n), O(N) space, exact arithmetic.
    """
    h = gen_h(N + 1)
    # Welford-style running mean / population variance in exact Fractions.
    # mu and M2 are over the values nu2(n)/n for n = 2..N (count = N-1 values).
    mu, M2 = Fraction(0), Fraction(0)
    count = 0
    out = {}
    last = None
    for n in range(2, N + 1):
        v = fold_nu2(n, h)
        last = (v, n)
        r = Fraction(v, n)
        count += 1
        delta = r - mu
        mu = mu + delta / count
        delta2 = r - mu
        M2 = M2 + delta * delta2
        s2 = (M2 / count) if count else Fraction(0)
        if n in checkpoints:
            out[n] = (mu, s2)
    return out, (mu, s2), last
