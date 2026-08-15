# Mycielski edge-count closed form — exact, re-derived

Author: pattern-recognition specialist. This pass re-derived a closed form for
the Mycielski iterates of C5 that the earlier consolidated report noted only as
a recurrence. It is **exact and verified**, and it is **context only** — it does
not bear on the plane chromatic-number problem, because Mycielski graphs are
not unit-distance graphs.

## Construction and exact recurrences

Mycielski(C5): V_{k+1} = 2V_k + 1, E_{k+1} = 3E_k + V_k, with V_1=5, E_1=5
(verified directly from the explicit construction, `mycielski_sequence2.py` /
`pattern_mycielski_extend.txt`).

V sequence: 5, 11, 23, 47, 95, 191, 383, 767, 1535, 3071 — closed form
V_k = 3·2^k − 1, verified. Also satisfies the order-2 homogeneous recurrence
a(n)=3a(n−1)−2a(n−2) (found by `find_linear_recurrence`, verified).

E sequence: 5, 20, 71, 236, 755, 2360, 7271, 22196, 67355, 203600.
`find_linear_recurrence` finds the order-3 homogeneous recurrence
a(n)=6a(n−1)−11a(n−2)+6a(n−3). Its origin is the order-2 **affine** recurrence
E_{k+2} = 5E_{k+1} − 6E_k + 1 (verified against all 10 terms), which comes
directly from substituting V_k = 3·2^k − 1 into E_{k+1}=3E_k+V_k; the constant
`1` is then eliminated by a second shift, giving the homogeneous order-3 form.

## Closed form (derived + verified)

E_k = (7·3^k − 6·2^k + 1) / 2, verified symbolically against all 10 computed
terms (sympy solve + simplify, `pattern_mycielski_closedform.txt`).

Check: k=1 → (21−12+1)/2 = 5 ✓; k=2 → (63−24+1)/2 = 20 ✓.

## Why it does not move the plane bound

Mycielski(C5) is a textbook, purely combinatorial construction with no unit
embedding; Mycielski²(C5) (the only 5-chromatic iterate, V=23, E=71) **fails
K2,3-freeness** (explicit K2,3 — vertices {0,2} sharing common neighbours
{1,6,12} — re-verified this pass), so it is not in the sharp kernel C_N that
every 5-chromatic unit-distance graph must lie in. The closed form is a capped
derivation in a dead thread, not a route to the bound. It is recorded so nobody
re-derives it.

## Re-confirmed findings (already in memory, this pass re-verified)

- Kernel census [1,4,16,228] (n=8..11): not polynomial, no constant-coefficient
  recurrence (order<=4), OEIS miss for both [1,4,16,228] and [1,1,16,198].
  The 4^k head (1,4,16) is the Arnold trap — the out-of-sample term 228 (not 64)
  falsifies it at n=11.
- Row-consistency of the census splits verified: kernel [1,4,16,228],
  4-chromatic [1,1,16,198], 3-colourable [0,3,0,30]; 4chrom+3chrom = kernel at
  every n (1+0=1, 1+3=4, 16+0=16, 198+30=228).
- Every kernel member through N=11 (249/249) is 4-colourable by two independent
  complete oracles → every unit-distance graph on ≤ 11 vertices is 4-colourable;
  any 5-chromatic UDG needs ≥ 12 vertices. This is the run's strongest
  delivered result (`size-bound-udg-4color-n11`).

Verdict: **no exploitable numerical sequence regularity in the run's data.**
All numerical regularities are labelled conjectures over the terms supplied;
the 4^k one is a falsified conjecture. The load-bearing structure is the
census (fully 4-colourable through N=11), extended only by the infeasible
n=12 enumeration, not by any closed form.
