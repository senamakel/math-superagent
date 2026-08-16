"""Feasibility boundary of the Casas-Alvero minor criterion (Schaub-
Spivakovsky, arXiv:2411.13967 Thm 3.1) as a function of degree n in {3..8}.

Parameters of the criterion at degree n (see lib.badprimes docstring):

    d = (n^2 - 3n + 4) / 2                       degree of the monomials
    C = binomial((n^2 - n)/2, n - 2)             number of monomials of
                                                 degree d in n-1 variables
                                                 = #columns of M_T = size
                                                 of the square minors
    D = sum_{i=1}^{n-1} binomial(d - i + n - 2, n - 2)
                                                 = #rows of M_T
    tuples = n^(n-1)                             #tuples T in {1..n}^{n-1}

M_T is a D x C integer matrix; p is bad for degree n iff rank_{F_p}(M_T) < C
for some T.  Three exact routes to the bad primes, in increasing cost:

  SNF route   : J_T = gcd of all C x C minors of M_T via Smith normal form;
                cost per tuple roughly polynomial in D*C with large exact-
                integer blowup.  Measured: n=4 19x15 SNF in 0.002 s
                (code/out/commands.log line ~1193), n=5 one 195x120 SNF
                exceeded a 90 s cap (commands.log ~line 2725).
  rank-mod-p  : rank_{F_p}(M_T) via modular Gaussian elimination,
                O(D * C^2) mod-p arithmetic ops per (tuple, prime) pair.
                Measured: n=5 all 625 tuples x 170 primes = 106250 ranks
                in 384.1 s over 28 workers (internal wall,
                verify_badprimes_n5.py, capture badprimes_n5.captured.txt).
  enumeration : p^n monic polynomials over F_p through the canonical oracle;
                feasible only to p = 13 at n = 5 (semantic_n5_smallprimes.py).

This program is NOT a new verification: it computes the integer parameters
exactly for n = 3..8 and quotes the two measured feasibility points (n=4 SNF
milliseconds, n=5 SNF > 90 s per matrix, n=5 rank 384.1 s for the full
sweep).  Everything else is magnitude extrapolation, labelled as such, to
state where each route stops being feasible.  Exit 0 always (a feasibility
statement, not a pass/fail check).

Deliverable: the boundary statement
    minors criterion fully feasible (SNF) : n <= 4
    rank-only                          : n = 5
    rank route also infeasible         : n >= 6  (see C, D, D*C^2 below)
"""

from __future__ import annotations

import math
import os

from lib.badprimes import lex_monomials  # exact monomial count cross-check

# measured anchors (code/out/commands.log; code/out/badprimes_n5.captured.txt)
SNF_N4_SECONDS = 0.002          # one 19x15 SNF (commands.log line ~1193)
SNF_N5_CAP = 90                 # one 195x120 SNF exceeded 90 s cap (line ~2725)
RANK_N5_SECONDS = 384.1         # 106250 ranks, 28 workers (internal wall)
RANK_N5_RANKS = 106250
N5_D, N5_C = 195, 120           # matrix shape at n=5


def params(n):
    """Exact criterion parameters (d, C, D, tuples) for degree n.
    C and D cross-checked against direct monomial enumeration via
    lib.badprimes.lex_monomials (an independent exact implementation)."""
    d = (n * n - 3 * n + 4) // 2
    C = math.comb((n * n - n) // 2, n - 2)
    D = sum(math.comb(d - i + n - 2, n - 2) for i in range(1, n))
    n_tuples = n ** (n - 1)
    # independent cross-check: C = #lex_monomials(n-1, d), each row count
    # = #lex_monomials(n-1, d-i)
    C_check = len(lex_monomials(n - 1, d))
    D_check = sum(len(lex_monomials(n - 1, d - i)) for i in range(1, n))
    assert C == C_check and D == D_check, (n, C, C_check, D, D_check)
    return d, C, D, n_tuples


def classify(n):
    """Route feasible at degree n.  n <= 4: SNF (measured milliseconds);
    n == 5: rank-only (SNF measured > 90 s per matrix); n >= 6: neither
    (C and D below make even one rank cost ~ 185 core-seconds at n=6)."""
    if n <= 4:
        return "SNF"
    if n == 5:
        return "rank-only"
    return "neither"


def fmt(v):
    s = "%d" % v
    if len(s) > 8:
        s = "%.3e" % v
    return s


def main():
    lines = []
    rec = lines.append

    rec("CASAS-ALVERO MINOR-CRITERION FEASIBILITY BOUNDARY (n = 3..8)")
    rec("criterion: Schaub-Spivakovsky arXiv:2411.13967 Thm 3.1; p bad for "
        "degree n iff rank_{F_p}(M_T) < C for some T in {1..n}^{n-1},")
    rec("  M_T the D x C integer matrix of the Phi_j-transformed elementary "
        "symmetric polys (lib.badprimes); C = #monomials of degree d in n-1")
    rec("  variables, D = total #rows = sum_i #monomials of degree d - i.  "
        "Computed exactly; C, D cross-checked against lex_monomials.")
    rec("measured anchors: n=4 SNF 19x15 = 0.002 s/matrix (commands.log); "
        "n=5 SNF one 195x120 > 90 s cap (commands.log);")
    rec("  n=5 rank route: 106250 ranks (625 tuples x 170 primes), 28 "
        "workers, 384.1 s internal wall (badprimes_n5.captured.txt).")
    rec("rank cost model: O(D*C^2) mod-p ops per (tuple, prime) rank; "
        "per-rank core-time at n=5 measured "
        "%.4f s (= 384.1*28/106250)."
        % (RANK_N5_SECONDS * 28 / RANK_N5_RANKS))
    rec("")

    hdr = ("n   d      C                D                 tuples         "
           "D*C^2 (ops/rank)  est core-s/rank(n)  route")
    rec(hdr)
    rec("-" * len(hdr))

    P = {}
    for n in range(3, 9):
        P[n] = params(n)
        d, C, D, n_tuples = P[n]
        route = classify(n)
        ops = D * C * C
        # per-rank core-seconds: extrapolate from the n=5 measurement.
        # One rank at n=5 costs ops5 = 195*120^2 mod-p ops in
        # (384.1*28/106250) core-seconds, so core-s/rank(n) scales with
        # the op count.
        ops5 = N5_D * N5_C * N5_C
        core_s = (RANK_N5_SECONDS * 28 / RANK_N5_RANKS) * ops / ops5
        rec("%-3d %-6d %-16s %-18s %-15s %-18s %-21s %s"
            % (n, d, fmt(C), fmt(D), fmt(n_tuples), fmt(ops),
               ("%.4f" % core_s) if core_s < 100 else ("%.3e" % core_s),
               route))

    rec("")
    rec("route legend: SNF = full minors criterion feasible via exact Smith "
        "normal form (J_T for every T, or lcm);")
    rec("  rank-only = SNF infeasible, rank-mod-p over F_p feasible; "
        "neither = both infeasible.")

    # ---- the boundary argument, computed from the exact parameters -------
    d6, C6, D6, t6 = P[6]
    d7, C7, D7, _ = P[7]
    d8, C8, D8, _ = P[8]
    ops6 = D6 * C6 * C6
    ops7 = D7 * C7 * C7
    ops8 = D8 * C8 * C8
    ops5 = N5_D * N5_C * N5_C
    core_s6 = (RANK_N5_SECONDS * 28 / RANK_N5_RANKS) * ops6 / ops5
    NP6 = 550  # ~#primes up to 8009, the largest published n=5 bad prime
    core_hours6 = core_s6 * t6 * NP6 / 3600

    rec("")
    rec("BOUNDARY STATEMENT:")
    rec("  * n <= 4 : SNF route feasible.  n=4 measured: all 64 tuples, "
        "19x15 SNF 0.002 s each, lcm J_T = 1575 = 3^2.5^2.7 -> bad primes "
        "{3,5,7} (verify_badprimes_n4.py, ALL CHECKS PASSED).")
    rec("  * n = 5  : SNF infeasible (one 195x120 SNF > 90 s cap), rank "
        "route feasible: 106250 ranks over 28 workers in 384.1 s, "
        "reproduces exactly {2,3,7,11,131,193,599,3541,8009}.")
    rec("  * n = 6  : rank route infeasible.  C = %d (vs 120 at n=5), "
        "D = %d (vs 195), so one (tuple, prime) rank costs" % (C6, D6))
    rec("       (D*C^2)_6/(D*C^2)_5 = %d/%d = %.1f times the n=5 cost, "
        "i.e. %.1f core-seconds per rank;" % (ops6, ops5, ops6 / ops5,
                                              core_s6))
    rec("       the full n=6 sweep (%d tuples x ~%d primes up to 8009) "
        "would be ~ %.2e core-hours -- infeasible." % (t6, NP6,
                                                       core_hours6))
    rec("       (SNF at n=6 is far worse: C = %d, so the gcd-of-all-minors "
        "problem is out of reach; the n=5 90 s cap is already for "
        "C = 120.)" % C6)
    rec("  * n = 7, 8 : C = %d, %d and D*C^2 = %s, %s ops/rank -- the rank "
        "route is infeasible a fortiori (neither)."
        % (C7, C8, fmt(ops7), fmt(ops8)))
    rec("")
    rec("FEASIBILITY BOUNDARY: the minor criterion is fully feasible at "
        "n <= 4 (SNF), rank-only at n = 5, and at n >= 6 the rank route "
        "is also infeasible (C = %d, D = %d at n = 6 make a single rank "
        "~ %.0f core-seconds and the full sweep ~ %.2e core-hours)."
        % (C6, D6, core_s6, core_hours6))
    rec("Numbers above the measured anchors (n=4, n=5) are magnitude "
        "extrapolations of the measured O(D*C^2) per-rank cost, not new "
        "verifications.")
    return "\n".join(lines)


if __name__ == "__main__":
    text = main()
    print(text)
    out_dir = "/workspace/code/out"
    os.makedirs(out_dir, exist_ok=True)
    header = [
        "CASAS-ALVERO MINOR-CRITERION FEASIBILITY BOUNDARY, n = 3..8",
        "program: code/n5/feasibility_boundary.py",
        "computed exactly: d=(n^2-3n+4)/2, C=binom((n^2-n)/2, n-2), "
        "D=sum_{i=1}^{n-1} binom(d-i+n-2, n-2), tuples=n^(n-1); C, D "
        "cross-checked against lib.badprimes.lex_monomials",
        "measured anchors: n=4 SNF 19x15 = 0.002 s (commands.log); n=5 SNF "
        "195x120 > 90 s cap (commands.log); n=5 rank 106250 ranks/28 "
        "workers = 384.1 s (badprimes_n5.captured.txt)",
        "rank route nominal cost: O(D*C^2) mod-p ops per (tuple, prime) "
        "rank, times tuples n^(n-1) times #primes per sweep",
        "",
    ]
    with open(os.path.join(out_dir, "feasibility_boundary.captured.txt"),
              "w") as fh:
        fh.write("\n".join(header) + text + "\n")
    raise SystemExit(0)
