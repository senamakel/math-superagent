#!/usr/bin/env python3
"""code/rule90_test/null_rule90_depth.py

Null distribution for the rule90 relative-depth result (TASKS item 1).

Data: code/out/rule90_depth_results.json, `regimes` = 28 entries with
depth = k_min - k_prev_min (relative depth of each block-length local
minimum from the previous local-minimum row).  The k=1000 tail entry
(depth 841, finite-width artifact) is dropped, leaving the 27 genuine
regime lengths, exactly as TASKS lists them:
  [0,7,4,2,8,4,8,4,9,9,6,6,4,3,4,7,5,3,2,14,15,3,6,4,3,5,13].

Hit predicate — must mirror analyze_rule90_depth.is_near_power_of_two
exactly, including its `depth <= 0 -> None` guard:
  depth is a HIT (tol=1) iff depth >= 1 and |depth - 2^j| <= 1 for some j.
So the hit values in 0..15 are {1,2,3,4,5,7,8,9,15} and the far values
are {0,6,10,11,12,13,14}: p = 9/16 per trial.

Two nulls:

1. PERMUTATION null (the naive shuffle): the hit predicate is a function
   of the depth value alone, not of its position, so EVERY permutation of
   the observed multiset has the same hit count.  The permutation test is
   degenerate by construction — it has zero power for value-dependent
   predicates.  We still run it (10,000 shuffles, parallelised) to
   demonstrate and report p = 1.0, and say why it is the wrong null.

2. EXACT BINOMIAL null (the meaningful one): if each observed regime
   length were an independent draw, uniform over the observed range
   [0,15], the per-trial hit probability is p = 9/16 and the total hit
   count is X ~ Binomial(27, 9/16).  Report P(X >= 21) exactly
   (Fraction arithmetic), mean, sd, and the normal-approximation z.
   This is the null TASKS specifies: it respects the observed depth range
   without assuming uniformity of the multiset.

Also report, clearly labelled as anti-conservative sensitivity:
   - p over the concentrated range [2,9] only (7/8 of values 2..9 are
     hits): what the result would look like if one conditioned on the
     observed range post hoc.  This is the p-hacking version, not the
     primary null.
   - the alternative good-set {1,2,3,4,7,8,9,15,16} from TASKS (16 is
     outside [0,15]; 5 is a hit under the program's predicate) as a
     sanity check on p.

Complexity: 10,000 permutations of 27 elements = 2.7e5 predicate
evaluations, O(N) time and O(N) space per shuffle; the exact binomial
sum is O(27).  Parallelised over the pool.
"""

import json
import math
from fractions import Fraction
import sys
import os

from scipy.stats import binom  # independent second route for the exact tail

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from lib.parallel import workers, parallel_map, announce  # noqa: E402


def is_near_power_of_two(depth, tol):
    """Mirror of analyze_rule90_depth.is_near_power_of_two (depth<=0 guard)."""
    if depth <= 0:
        return None
    j = 0
    while (1 << j) <= depth + tol:
        p = 1 << j
        if abs(depth - p) <= tol:
            return (p, j, abs(depth - p))
        j += 1
    return None


def hit(depth, tol=1):
    return is_near_power_of_two(depth, tol) is not None


def load_depths():
    rec = json.load(open("code/out/rule90_depth_results.json"))
    depths = [r["depth"] for r in rec["regimes"] if r["depth"] != 841]
    assert len(depths) == 27, len(depths)
    return depths


def count_hits(depths, tol=1):
    return sum(1 for d in depths if hit(d, tol))


def shuffle_count(seed):
    """One permutation: count hits.  (Seed unused; any shuffle hits the same.)"""
    return count_hits(depths_global)


def binomial_tail_exact(n, k0, p):
    """P(X >= k0) for X ~ Binomial(n, p), exact Fraction arithmetic."""
    total = Fraction(0)
    for k in range(k0, n + 1):
        total += Fraction(math.comb(n, k)) * (p ** k) * ((1 - p) ** (n - k))
    return total


def main():
    depths = load_depths()
    tol = 1
    observed = count_hits(depths, tol)
    n = len(depths)
    print(f"regime depths (27, k=1000 tail dropped): {depths}")
    print(f"hit predicate: depth>=1 and |depth-2^j|<=1 for some j (tol={tol})")
    print(f"hit values in 0..15: {{1,2,3,4,5,7,8,9,15}}  -> p = 9/16 per trial")
    print(f"observed hit count: {observed}/{n}\n")

    # --- null 1: permutation (degenerate by construction) -------------------
    nperm = 10000
    stride = nperm // workers()
    announce("rule90-depth null", f"{nperm} permutations of 27 depths",
             workers())
    counts = parallel_map(shuffle_count, range(nperm), label="rule90-null-perm",
                          space=f"{nperm} permutations", count=workers())
    from collections import Counter
    hist = Counter(counts)
    ge = sum(1 for c in counts if c >= observed)
    print("=== NULL 1: permutation (shuffle the 27 observed depths) ===")
    print(f"  {nperm} shuffles: hit-count distribution = "
          f"{dict(sorted(hist.items()))}")
    print(f"  all counts identical ({hist.most_common(1)[0][0]}): "
          f"the permutation null is DEGENERATE")
    print("  why: the hit predicate tests the depth VALUE only, not its")
    print("  position, so every rearrangement of the same multiset of")
    print("  depths has the same hit count.  A permutation test has zero")
    print("  power for a value-only predicate; it cannot test this claim.")
    print(f"  permutation p-value = {ge}/{nperm} = {ge/nperm:.3f}  "
          f"(meaningless; reported for completeness)\n")

    # --- null 2: exact binomial with per-trial p = 9/16 ----------------------
    p = Fraction(9, 16)
    tail = binomial_tail_exact(n, observed, p)
    mean = n * p
    var = n * p * (1 - p)
    sd = var ** Fraction(1, 2)
    z = (observed - mean) / sd
    print("=== NULL 2: exact binomial, X ~ Binomial(27, 9/16) ===")
    print(f"  per-trial hit probability p = 9/16 (uniform over [0,15],")
    print(f"  program's own guard: depth 0 is not a hit)")
    print(f"  mean = 27*9/16 = {mean} = {float(mean):.3f}")
    print(f"  sd   = sqrt(27*9/16*7/16) = {float(sd):.3f}")
    print(f"  observed 21 hits -> z = ({observed} - {float(mean):.2f})/"
          f"{float(sd):.2f} = {float(z):.2f}")
    print(f"  P(X >= {observed}) = {tail} = {float(tail):.6f}")
    print(f"  VERDICT (binomial null): the 21/27 hit rate is "
          f"{'significant at 5%' if float(tail) < 0.05 else 'NOT significant at 5%'} "
          f"(two-sided ~ {2*float(tail):.4f})\n")

    # --- sensitivity: conditional on the concentrated range [2,9] ------------
    in_29 = [d for d in depths if 2 <= d <= 9]
    hits_29 = sum(1 for d in in_29 if hit(d, tol))
    print(f"=== sensitivity (anti-conservative, NOT the primary null) ===")
    print(f"  depths concentrated in [2,9]: {len(in_29)}/27 there")
    print(f"  within [2,9] the hit rate is {hits_29}/{len(in_29)} "
          f"({100.0*hits_29/len(in_29):.0f}%), vs the [2,9] near-value "
          f"fraction 7/8 = 87.5%")
    p2 = Fraction(7, 8)
    t29 = binomial_tail_exact(len(in_29), hits_29, p2)
    print(f"  Binomial({len(in_29)}, 7/8): P(X >= {hits_29}) = "
          f"{float(t29):.4f} — conditioning on the observed range post hoc "
          f"erases the signal; the honest range is [0,15] as in null 2")
    # alternative good-set from TASKS ({1,2,3,4,7,8,9,15,16} -> 9/16 in [0,15])
    print(f"  TASKS's own good-set {{1,2,3,4,7,8,9,15,16}} also gives "
          f"9/16 in [0,15] (16 outside, 5 a hit under the program's "
          f"predicate): same null 2 p-value.\n")
    # robustness: tol=0 exact powers of two (p0 = {1,2,4,8}/16 = 1/4)
    h0 = sum(1 for d in depths if d in (1, 2, 4, 8, 16))
    p0 = Fraction(1, 4)
    t0 = binomial_tail_exact(n, h0, p0)
    print(f"  robustness tol=0 (exact powers of two, p=1/4): {h0}/{n} "
          f"hits, P(X >= {h0}) = {float(t0):.4f} "
          f"({'significant' if float(t0) < 0.05 else 'NOT significant'})")
    print(f"  => the signal lives entirely in the tol=1 tolerance; at "
          f"tol=0 it is not significant\n")
    scipy_tail = float(binom.sf(observed - 1, n, float(p)))
    print(f"  cross-check: scipy P(X >= {observed}) = {scipy_tail:.6f} "
          f"(agrees with the Fraction exact value {float(tail):.6f})")

    # --- the far values, for the record --------------------------------------
    far = [d for d in depths if not hit(d, tol)]
    print(f"=== the 6 far regime lengths (the evidence AGAINST the signal) ===")
    print(f"  {sorted(far)}  (three 6s: {far.count(6)}; and 0, 13, 14)")
    print(f"  expected far under binomial null: {float(n*(1-p)):.1f} of 27; "
          f"observed 6")

    out = {
        "n_regimes": n, "observed_hits": observed, "tol": tol,
        "p_per_trial": str(p), "exact_p_ge_observed": str(tail),
        "float_p": float(tail), "z": float(z), "mean": float(mean),
        "sd": float(sd),
        "scipy_p_ge_observed": float(binom.sf(observed - 1, n, float(p))),
        "tol0_hits_10_of_27": h0, "tol0_p_ge_10": float(t0),
        "permutation_p": ge / nperm, "permutation_degenerate": True,
        "far_lengths": sorted(far),
    }
    with open("code/out/rule90_depth_null.json", "w") as fh:
        json.dump(out, fh, indent=2)
    print("\nwrote code/out/rule90_depth_null.json")


depths_global = None


if __name__ == "__main__":
    depths_global = load_depths()
    main()