# Abundance profile of union-closed families — exact scan (n = 1..4)

This note records a fresh, self-contained pass over the exact abundance profile
of union-closed families on small ground sets, using the canonical oracle
`code/lib/uc.py` (no second union-closure checker was written for the main
result; the only independent re-implementation is the separately-audited
`worst_independent.py`, deliverable 4). Every number below is from an executed
run whose capture is on disk (see Sources).

## Definitions

A family `F` of subsets of `[n]` is union-closed (UC) if `A ∪ B ∈ F` for all
`A,B ∈ F`. For element `x` let `c_x = |{A ∈ F : x ∈ A}|` and
`density_x = c_x / |F|`. The **abundance profile** is the vector
`(c_x)_{x ∈ [n]}` (all integer). An element is **abundant** if `2 c_x ≥ |F|`
(density ≥ 1/2). We restrict densities to elements that actually occur
(`c_x ≥ 1`), i.e. elements of the union.

`WORST(n) = min over UC F on [n] of min_{x occurs} c_x/|F|` is the smallest
density any element of any UC family can have.

## Deliverable 1 — WORST(n), verified against the expected values

```
n:       1     2     3     4
WORST:  1/2   1/3   1/5   1/9    =  1 / (2^{n-1} + 1)
```

Exhaustive enumeration over all UC families on `[n]` (excluding the trivial
`{∅}`), exact integer/rational arithmetic via `lib.uc`. Matches the expected
`1/(2^{n-1}+1)`. The family achieving it is, at each n, one of the `n`
permutations of the near-n-cube `F = 2^[n-1] ∪ {[n]}` with `|F| = 2^{n-1}+1`.

## Deliverable 2 — the profiles that occur

Distinct sorted-descending profiles over all UC families on `[n]`:

| n | UC families | distinct profiles |
|---|---|---|
| 1 | 2 | 1 |
| 2 | 12 | 4 |
| 3 | 120 | 18 |
| 4 | 4958 | 138 |

(The UC-family counts exclude `{∅}`; including it gives 3, 13, 121, 4959, the
catalogued A121921 — a consistency check with the oracle. Full profile lists
are in `profile_listing.captured.txt`.)

**Minimum rarest-element count as a function of `|F|` and `n`.** Define
`r(n,m) = min over UC F with |F|=m of (rarest occurring element's count)`.
Exhaustive result:

```
n=1:  m=1→1, 2→1
n=2:  m=1→1, 2→1, 3→1, 4→2
n=3:  m=1..5→1, 6→2, 7→3, 8→4
n=4:  m=1..9→1, 10→2, 11→3, 12→4, 13→5, 14→6, 15→7, 16→8
```

In every case `r(n,m) = max(1, m − 2^{n-1})`, and the inequality
`c_x ≥ m − 2^{n-1}` holds elementwise for **every** occurring element of **every**
UC family. See `minrarest_formula.captured.txt` (0 elementwise violations).

## Deliverable 3 — structural claim

The claim we test as the candidate constraint on a minimal counterexample:

> **Claim B'.** For every union-closed family `F` on `[n]` with `|F| = m` and
> every occurring element `x`, `c_x ≥ m − 2^{n-1}`; hence the rarest occurring
> element satisfies `c_x ≥ max(1, m − 2^{n-1})`, and this is **tight**.

**Status: holds (checked exhaustively n ≤ 4), and proved by a counting
argument.** The members of `F` that avoid `x` are subsets of `[n]\{x}`, of which
there are exactly `2^{n-1}`; there are `m − c_x` of them, so
`m − c_x ≤ 2^{n-1}`, i.e. `c_x ≥ m − 2^{n-1}`. This does not use the
entropy/Nagel machinery — it is a containment count. It is tight: for every
`m` a UC family achieves it (data above).

**Caveat on force.** This bound is real but does not by itself rule out a
counterexample: for a counterexample we need some `c_x ≤ m/2 − 1`, and the bound
`c_x ≥ m − 2^{n-1}` is weaker than `m/2` whenever `m > 2^{n-1} − 1`, which is
always true for `|F| > 2^{n-1}`. So B' is a correct structural statement but not
a proof ingredient by itself; it constrains the *shape* (the rarest element's
count is at least `m − 2^{n-1}`), which for squares the family very tightly.

We also tested three candidate claims:

- **Claim A (the weak k = n Nagel/Das–Wu bound).** Every UC family satisfies
  `min occurring c_x ≥ |F|/(2^{n-1}+1)`. **Held** (0 failures, n ≤ 4);
  equality iff `F` is isomorphic to the near-n-cube (the equality cases are
  exactly the `n` coordinate permutations — a relabeling artifact, confirmed in
  `equality_cases.captured.txt`).
- **Claim B (near-n-cube profile shape).** The near-n-cube has profile
  `[2^{n-2}+1 repeated n−1 times, 1]` for all `n` (n = 2..8 shown). **Held.**
- **Claim C (degree-1 forces abundance).** Every UC family with an element of
  degree exactly 1 has an abundant element. **Held** for every family on
  `n = 1..4` (never violated). Equivalently, a minimal counterexample can have
  **no** element of degree 1 — every element appears in at least two sets.
  This is recorded as a computational fact for n ≤ 4; I do not claim it as a
  general sourced theorem here (the standard singleton lemma is the allied but
  weaker statement), so it is marked *verified-computationally n ≤ 4*.
- **Claim D (min-count-1 forces near-cube shape).** Is every UC family whose
  rarest occurring element has count 1 necessarily near-cube-shaped?
  **FAILED** — e.g. the trivial families `{∅, {x}}` (profile `[1]`) and many
  others have a degree-1 element but are not near-cubes. So the near-cube is
  *not* the only family with a rarest count of 1; uniqueness holds only if one
  additionally demands `|F| = 2^{n-1}+1` and `|∪F| = n`.

## Deliverable 4 — independent brute force

`worst_independent.py` re-implements union-closure and abundance **from
scratch, not importing lib.uc**, and recomputes WORST(2), WORST(3):

```
INDEPENDENT n=2: UC count=12, WORST=1/3 == 1/3 ? True
INDEPENDENT n=3: UC count=120, WORST=1/5 == 1/5 ? True
```

Agreement with the oracle route confirms both.

## Ceilings and honesty

- All exhaustive enumeration is the sanctioned brute-force **oracle** at
  `n ≤ 4` (hard-capped; at n=4 it is 65536 subfamilies, at n=5 it would be
  `2^32 = 4.3e9`, declared infeasible by this route).
- `n = 5` (≈ 2.7M UC families = A102896(5)) is **not** reached; direct
  enumeration of every subfamily to find them is `2^32` steps, too heavy.
- Every abundance is an exact integer; densities are exact rationals
  (`fractions.Fraction`); nothing below is floating-point evidence dressed as a
  result.

## Sources (captures)

- `profile_scan.captured.txt` — WORST, profile counts, claim A, claim C, formula data.
- `profile_listing.captured.txt` — full distinct-profile lists per n.
- `minrarest_formula.captured.txt` — B' elementwise check and tightness.
- `nearcube_profile_claim.captured.txt` — claim B, claim D.
- `equality_cases.captured.txt` — claim A equality cases (the n permutations).
- `worst_independent.captured.txt` — deliverable 4.

```claim
id: rarest-count-floor
statement: For every family F (union-closed or not) of subsets of [n] with |F| = m, every occurring element x satisfies c_x >= m - 2^{n-1}, so the rarest occurring element has count >= max(1, m - 2^{n-1}); the bound is tight (attained for every m). Proof: the m - c_x members of F avoiding x are subsets of [n]\{x}, of which there are exactly 2^{n-1}.
hypotheses: F any family of subsets of [n], |F| = m, element x occurs in F
holds-here: yes
status: proved (counting argument); tightness verified exhaustively for n<=4 via lib.uc oracle
bearing: constrains the rarest element's count of any (hence any minimal-counterexample) family; but it is satisfied by arbitrary families, so it carries no union-closure content and is weaker than m/2 for |F| > 2^{n-1} -- a true but weak structural bound, stated honestly.
anchor: code/out/abundance_pass2_note.md, code/out/minrarest_formula.captured.txt
answers: <none>
```

```claim
id: no-degree-1-element-in-minimal-counterexample
statement: No union-closed family with an element of degree exactly 1 fails Frankl's conjecture: every UC family on ground set [n], n<=4 (exhaustive), containing an element in exactly one set has an abundant element. Equivalently a minimal counterexample can have no element of degree 1 -- every element appears in at least two sets. Verified computationally for all UC families on n=1..4 (never violated).
hypotheses: F union-closed on [n], n<=4, has an element x with c_x = 1
holds-here: yes
status: verified-computationally (n<=4, exact oracle; not promoted to a general sourced theorem)
bearing: a structural constraint on the abundance profile of a minimal counterexample: it can have no degree-1 element.
anchor: code/out/abundance_pass2_note.md (claim C), code/out/profile_scan.captured.txt
answers: <none>
```
