# Pattern-finder findings — PE 761 K(n) sequence

## What was extracted
The integer sequence that matters in the PE 761 critical-speed computation is
the auxiliary index `K(n)`:

    K(n) = floor of the unique root r in [1, n/2) of  tan(r·π/n) = (r+n)·tan(π/n)

(from stewbasic / Abel et al. — this is the K used in α = ½(Kθ + acos(...)) and
V(n) = 1/cos(α)).

## Result 1 — TRUE asymptotic slope (derived, confirmed numerically)
As n → ∞, K(n)/n → c where `c` is the unique root of

    tan(c·π) = π·(c + 1)      in (0, 1/2)

c ≈ **0.4302966531242027578**. Derivation: let g ~ c·n be the root of
tan(g·π/n) = (g+n)·tan(π/n); LHS → tan(cπ), RHS → (c+1)n·(π/n) = π(c+1).

## Result 2 — floor(3n/7) is asymptotically WRONG
`K(n) = floor(3n/7)` (OEIS A057357) holds only for n ≲ 85.
The deviation grows **linearly**: K(n) − floor(3n/7) ~ (c − 3/7)·n,
with c − 3/7 ≈ 0.0017252. Confirmed exactly:
- n=1000:  K=430,  floor=428, diff=2  (≈1.73)
- n=10000: K=4302, floor=4285, diff=17 (≈17.25)
- n=50000: K=21514, floor=21428, diff=86 (≈86.26)
- n=100000: K=43029, floor=42857, diff=172 (≈172.52)

## Result 3 — K(n) = floor(c·n) is robust but NOT exact
`K(n) = floor(c·n)` holds for essentially all n, but fails at boundary cases
where c·n lands within ~1e-3 below an integer:
- n=165:   root r = 71.00036, so K=71, but floor(c·n)=70
- n=3809:  root r = 1639.00001, K=1639, floor(c·n)=1638
Dense scan of n ∈ [3, 19999]: only those 2 fails. Sparse checks to n=10^6
(K=430296 = floor(c·n)) all hold. There is no constant-coefficient linear
recurrence of order ≤ 12 fitting K(n) (asymptotically linear, not periodic).

## OEIS
Matches (A057357 floor(3n/7), A308358 Beatty sqrt3/4, etc.) are small-term
coincidences only; the true slope c ≠ 3/7 makes them asymptotically wrong.

## Relation to the answer
K is an AUXILIARY index; V(n) = 1/cos(α) is smooth in n/K, so none of these
K-deviations affect the 8-dp hexagon answer. Verified: `python code/solution.py`
reproduces V_hexagon = 5.05505046, plus anchors n=3 (7.4049183473), n=4
(5.78859314459), and the circle limit (4.60333885).

## Reproduction
    python code/pattern_k_structure.py         # K at large n, slope
    python code/pattern_k_deviation_linear.py  # linear deviation growth
    python code/pattern_k_closedform.py        # floor(c·n) structure
    python code/pattern_k_find_mismatch.py     # locate the boundary fails
    python code/pattern_k_fail_details.py      # root values at the 2 fails
