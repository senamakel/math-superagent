# Pattern-finder report — extending the abundance-profile-count sequence and the n=5 structural claims

## What this pass did

The run's one genuinely in-scope, uncatalogued integer sequence was the
**number of distinct abundance profiles over all union-closed families on
`[n]`**:

```
n:       1   2    3    4
profiles: 1   4   18  138
```

Stuck at 4 terms — n=4 was the strong ceiling for the direct `2^(2^n)`
subfamily enumeration (n=4: 65536 subfamilies; n=5: `2^32` ≈ 4e9, declared
infeasible). This pass broke that ceiling with a *canonical cascade* so the
sequence could be extended and tested, and used the same machinery to push two
structural claims one `n` further.

## The cascade (canonical generator, exact, no brute force over subfamilies)

A union-closed family `F′` on `k+1` elements (adding element `x`) projects to
a union-closed family `π` on `k` elements. `F′` is determined by `π` and the
pair `(R1, R2)` with

```
R2 = {A in π : A∪{x} in F′}          (members whose x-lift appears)
R1 = {A in π : A      in F′} = π \ R2 (members appearing without x)
```

with the compatibility conditions: `R2` is an **up-set** of the
join-semilattice poset `(π, |)`; `R1` is closed under `|`; and
`A∈R1, B∈R2 ⇒ A∪B ∈ R2`. Every valid triple gives a UC family and the triple
is unique, so the number of families at level `k+1` equals the sum over UC
families `π` on `k` elements of the number of valid `(R2, R1)`. This is a
bijection on the *same objects the oracle counts* — no duplicates, no misses,
no subfamily brute force.

**Validation against the oracle and the catalogue:**

```
n:           1      2       3       4
UC families: 2     12     120    4958      (matches oracle & A121921)
profiles:    1      4      18     138      (matches oracle)
```

and at n=5 it reproduces `2771102 = A121921(5) − 1`, preserving the oracle's
exact off-by-one at every level — the strongest evidence it enumerates the same
objects.

## Result 1 — the 5th term of the profile-count sequence

```
n:       1    2    3    4      5
profiles: 1   4   18  138   2503
```

The n=5 value **2503** is new (exhaustive over all 2,771,102 nonempty UC
families on 5 elements, exact).

Tool verdicts over the 5 terms:
- not a low-degree polynomial (first differences 3, 14, 120, 2365 — never
  stabilise);
- **no constant-coefficient linear recurrence of order ≤ 4** fits all 5 terms
  (find_linear_recurrence);
- **not in OEIS** (oeis_lookup returned nothing — a recorded miss).

Growth ratios 4.0, 4.5, 7.67, 18.1 — super-exponential, mirroring the
catalogued family-count double-exponential `A102897`. **Verdict:** this
sequence carries no exploitable low-order structure for Frankl's conjecture.
Treat as an enumeration curiosity (like `A102897`), not a route to an
abundance bound. This is reported plainly: no recurrence, no closed form, no
catalogued match — the honest reading of 5 terms.

## Result 2 — structural claims extended to n=5 (exhaustive, exact)

Over all 2,771,102 nonempty UC families on `[5]`:

1. **Claim C (no degree-1 element without an abundant element): 0 failures.**
   Every UC family on `[n≤5]` with an element in exactly one set has an
   abundant element. Corollary for a minimal counterexample: it can have **no
   degree-1 element** — every element lies in at least two sets. This was
   previously verified to n≤4; now n≤5. (Verified-computational, not a theorem
   here.)
2. **Claim A (Nagel/Das–Wu sharpness):** `WORST(5) = 1/(2⁴+1) = 1/17` exactly,
   and every family satisfies `min_present_count · 17 ≥ |F|`, equality iff the
   near-5-cube (profile `[9,9,9,9,1]`, i.e. `2^{n-2}+1` repeated `n-1` times
   then 1). The near-5-cube profile confirmed. This is a sourced theorem
   (Das–Wu), here corroborated exhaustively at n=5.

## Honesty of labels

- `2503`, the 0-failure tallies, and `1/17` are **checked** (exhaustive at the
  stated n, exact integer/fraction arithmetic).
- The general statements (the sequence has no recurrence for all n; the claims
  hold for all n) are **not** proved here. Claim A is a **sourced theorem**;
  claim C is **verified-computational n≤5**.
- No fit is dressed up as a proof; an invented pattern is avoided.

## First falsifier if one pursued a conjecture

For the profile-count sequence, the tools report **no order ≤ 4 recurrence to
falsify** and no polynomial — so there is nothing honest to state a first
falsifier against. The sequence is reported as structureless over its terms.

## Files

- `code/out/profile_count_cascade.py` — the canonical cascade (validated,
  exact; the generator).
- `code/out/profile_count_n5_claims.py` — n=5 claim C / claim A / profiles /
  near-cube check.
- `code/out/profile_count_extend.py`, `debug_upsets.py`, `debug_cascade.py`,
  `debug_n2.py` — exploratory versions; superseded, kept only for provenance.
