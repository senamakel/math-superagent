"""Verify the Schaub-Spivakovsky bad-prime-minors criterion (Thm 3.1,
arXiv:2411.13967) for degree n = 5, by rank over GF(p).

Published ground truth (Castryck-Laterveer-Ounaies 2012, Thm 4,
research/sources/castryck2012_degree12_html.full.md lines ~147-149): the bad
primes of degree 5 are {2, 3, 7, 11, 131, 193, 599, 3541, 8009}.

Method (Thm 3.1): p is bad for degree n iff p | J_T for some tuple
T in {1..n}^{n-1}, where J_T = gcd of all C x C minors of the D x C integer
matrix M_T (see lib.badprimes docstring for the exact definition of M_T).
Mechanically  p | J_T  <=>  rank_{F_p}(M_T) < C, so deciding a named prime
needs only the exact rank over F_p, never the (astronomically large) J_T.

At n = 5: d = 7, C = 120, D = 195, tuples in {1..5}^4 (625 tuples).
The SNF route to J_T is measured-infeasible at n = 5 (one 195x120 SNF
exceeded a 90 s cap; code/out/commands.log), so this program uses ONLY the
rank-mod-p route: lib.badprimes.rank_mod_p, modular Gaussian elimination
over F_p, O(D * C^2) mod-p arithmetic ops per rank.

Scope of this run (stated as bounds, not as a proof of the theorem):
  * every prime in the published list {2,3,7,11,131,193,599,3541,8009} is
    certified BAD at n=5 by this criterion, with a witnessing tuple and the
    rank over F_p;
  * every prime q < 1000 is DECIDED: q is bad iff q is in the published list;
  * spot check: one tuple at p = 3547 (a prime just above 3541, in no list);
  * no claim about primes in [1000, 8009) outside the list beyond the
    published theorem — they are simply not re-verified here.

The rank <-> J_T equivalence was validated at n = 4 by two independent exact
routes (code/out/badprimes_n4.captured.txt: SNF lcm = 1575 = 3^2.5^2.7 and
rank-mod-p agree, both equal {3,5,7}).

Exit 0 iff every assert passes.
"""

from __future__ import annotations

import math
import os
import time
from concurrent.futures import ProcessPoolExecutor
from itertools import product

import sympy as sp

from lib.badprimes import matrix_MT, rank_mod_p

N = 5
NAMED = [2, 3, 7, 11, 131, 193, 599, 3541, 8009]
SWEEP_BOUND = 1000  # decide every prime below this bound
WORKERS = 28


def _worker(args):
    """(chunk of tuples, prime list) -> [(T, p, rank_Fp(M_T)), ...].
    Builds each matrix in the chunk once and ranks it over every prime."""
    chunk, primes = args
    out = []
    for T in chunk:
        M = matrix_MT(N, T)
        assert M.shape == (195, 120), M.shape
        for p in primes:
            out.append((T, p, rank_mod_p(M, p)))
    return out


def main():
    lines = []

    def rec(label):
        lines.append(label)

    # ---- parameters from the theorem -------------------------------------
    d = (N * N - 3 * N + 4) // 2
    C = int(sp.binomial((N * N - N) // 2, N - 2))
    D = sum(int(sp.binomial(d - i + N - 2, N - 2)) for i in range(1, N))
    rec("parameters: n=%d, d=%d, C=%d, D=%d" % (N, d, C, D))
    assert (d, C, D) == (7, 120, 195)

    tuples = list(product(range(1, N + 1), repeat=N - 1))
    assert len(tuples) == 625

    sweep = list(sp.primerange(2, SWEEP_BOUND))
    primes_to_check = sorted(set(sweep) | set(NAMED))
    assert set(NAMED) <= set(primes_to_check)
    assert all(p in sweep for p in NAMED if p < SWEEP_BOUND)
    rec("search space: %d tuples T in {1..5}^4 x %d primes "
        "(%d primes < %d plus listed primes >= %d) = %d rank computations"
        % (len(tuples), len(primes_to_check), len(sweep), SWEEP_BOUND,
           SWEEP_BOUND, len(tuples) * len(primes_to_check)))
    rec("worker count: %d" % WORKERS)

    # ---- the sweep --------------------------------------------------------
    chunks = [tuples[i::WORKERS] for i in range(WORKERS)]
    chunks = [c for c in chunks if c]
    t0 = time.time()
    results = []
    with ProcessPoolExecutor(max_workers=len(chunks)) as ex:
        for chunk_res in ex.map(_worker, [(chunk, primes_to_check)
                                          for chunk in chunks]):
            results.extend(chunk_res)
    wall = time.time() - t0
    assert len(results) == len(tuples) * len(primes_to_check)
    rec("wall time for %d ranks over %d workers: %.1f s"
        % (len(results), len(chunks), wall))

    # ---- aggregate: bad tuples per prime ----------------------------------
    bad_by_p = {}
    min_rank_by_p = {}
    for T, p, r in results:
        assert 0 <= r <= C
        if r < C:
            bad_by_p.setdefault(p, []).append(T)
            min_rank_by_p[p] = min(min_rank_by_p.get(p, C), r)
    found = set(bad_by_p)

    # ---- assertions against the published list ----------------------------
    assert found == set(NAMED), (
        "found %s, named %s, excess %s, missing %s"
        % (sorted(found), NAMED,
           sorted(found - set(NAMED)), sorted(set(NAMED) - found)))
    # every listed prime is bad, and every prime < 1000 outside the list good
    for p in NAMED:
        assert p in bad_by_p, p
    for q in sweep:
        assert (q in bad_by_p) == (q in set(NAMED)), q
    assert all(p < SWEEP_BOUND for p in bad_by_p if p not in (3541, 8009))

    # ---- report ------------------------------------------------------------
    rec("")
    rec("certified BAD primes (rank_{F_p}(M_T) < 120 for some T):")
    for p in sorted(found):
        w = bad_by_p[p]
        rec("  p=%5d  witnesses=%3d  min rank=%3d  first witness T=%s"
            % (p, len(w), min_rank_by_p[p], w[0]))
    rec("")
    good_checked = [q for q in sweep if q not in set(NAMED)]
    rec("primes decided GOOD (full rank 120 on all 625 tuples): %d primes "
        "q < %d outside the list" % (len(good_checked), SWEEP_BOUND))
    rec("  smallest such: %s" % good_checked[:12])
    rec("")

    # ---- spot checks --------------------------------------------------------
    for spot_p in (3547,):  # just above 3541, in no published list
        M = matrix_MT(N, (1, 2, 3, 4))
        r = rank_mod_p(M, spot_p)
        rec("spot check: rank_{%d}(M_(1,2,3,4)) = %d (expected %d, sample only)"
            % (spot_p, r, C))
        assert r == C

    rec("RESULT: rank-over-F_p criterion at n=5 reproduces exactly the "
        "published bad-prime list {%s} (Castryck 2012 Thm 4), and certifies "
        "no bad prime below %d outside it." % (", ".join(map(str, NAMED)),
                                               SWEEP_BOUND))
    rec("ALL CHECKS PASSED")
    return "\n".join(lines)


if __name__ == "__main__":
    text = main()
    print(text)
    out_dir = "/workspace/code/out"
    os.makedirs(out_dir, exist_ok=True)
    header = [
        "SCHAUB-SPIVAKOVSKY BAD-PRIME-MINORS CRITERION, DEGREE n=5 "
        "(arXiv:2411.13967 Thm 3.1), RANK-OVER-F_p ROUTE",
        "program: code/badprimes_criterion/verify_badprimes_n5.py",
        "oracle: lib.badprimes.rank_mod_p (exact modular Gaussian "
        "elimination over F_p; p | J_T <=> rank_{F_p}(M_T) < C=120)",
        "base ring: integer matrix M_T (D=195 x C=120), rank computed mod p; "
        "term order: not used (exact matrix rank, no Groebner basis)",
        "ground truth: Castryck-Laterveer-Ounaies 2012 Thm 4, bad primes of "
        "degree 5 = {2,3,7,11,131,193,599,3541,8009}",
        "scope: all 625 tuples T in {1..5}^4 x every prime < 1000 plus the "
        "listed primes 3541, 8009; rank<->J_T equivalence validated at n=4 "
        "(code/out/badprimes_n4.captured.txt); SNF route at n=5 measured "
        "infeasible (>90 s per 195x120 matrix, code/out/commands.log)",
        "",
    ]
    with open(os.path.join(out_dir, "badprimes_n5.captured.txt"), "w") as fh:
        fh.write("\n".join(header) + text + "\n")
    raise SystemExit(0)
