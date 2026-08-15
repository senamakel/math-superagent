# CHT 2026 — Gilbreath's conjecture: Cramér random model / deterministic analysis

**Source:** arXiv:2607.08712v1 [math.CO], 9 Jul 2026 (Zachary Chase, Zach
Hunter, Terence Tao). Read from the FULL PDF (pdftotext -layout):
`research/sources/chase-hunter-tao-2026-cramer-random-model-gilbreath-FULLPDF.full.md` [[chase-hunter-tao-2026-cramer-random-model-gilbreath.full]]
This note is the FULLPDF digest (the earlier `summaries/…-full-html.md` read
the HTML body; this is the primary-version verification of the one theorem
the run relies on, Theorem 1.6, together with its proof machinery).

## Normalized-gap equivalence (p.2, verified)

Removing the left diagonal and top row, dividing by 2, subtracting 1 from the
new top row: **GC ⟺ the left diagonal of the array from
`a_n = (p_{n+2} − p_{n+1})/2 − 1` is eventually `{0,1}`-valued.** First nine
normalized gaps: `0,0,1,0,1,0,1,2,0` (A100820). This is the run's `{0,2}`↔`{0,1}`
correspondence in the sources' coordinates.

## Theorem 1.6 (Deterministic criterion) — VERBATIM from the FULLPDF (p.7–8)

> Let `M, L ≥ 1` and `1 ≤ N′ ≤ N` be integers, and let
> `1 < R_0 < R_1 < … < R_M < (N − N′)/2` satisfy `R_m ≥ 4R_{m−1}` and
> `R_0 ≥ 100L·8^M`. Let `a_1,…,a_N` be non-negative integers with Gilbreath
> array `a(i,j)`, `0 ≤ i ≤ N−1`, `1 ≤ j ≤ N−i`. Assume:
> **(i)** `a_n ≤ 2^M` for all `n = 0,…,N`;
> **(ii)** no length-`L` zero-block `a(i,j)=…=a(i,j+L−1)=0`;
> **(iii)** no block with `2^{M−m} < d ≤ 2^{M−m+1}`, `0 ≤ i ≤ 2R_{m−1}`,
> `k ≥ R_m − 3R_{m−1}`, `N′ ≤ j ≤ N−i−k`, and
> `a(i,j),…,a(i,j+k−1) ∈ {0,d}`.
> Then `a(N−1,1) ∈ {0,1}`.

**The column restriction is in (iii): `j ≥ N′` (the RIGHT HALF).** The run's
leading `{0,2}` block sits at j=1, the far left, so it never violates (iii).
Verified against the FULLPDF text verbatim.

## Authors' own difficulty assessment (p.8, verbatim)

> "For a_n equal to the normalized prime gaps, hypothesis (i) follows from
> Cramér's conjecture. The other two hypotheses are plausible from
> probabilistic heuristics, but unfortunately look difficult to establish
> rigorously, even if one assumes strong conjectures on the primes such as
> the Hardy–Littlewood prime tuples conjecture."

(i) needs Cramér (gaps O(log² n), open, strictly stronger than BHP α=0.525).

## Proof core (the two obstruction families)

The contrapositive: in a {0,…,2^M}-valued triangle with no L-zero-block whose
bottom vertex `a(N−1,1) > 1`, one *finds* a long shallow `{0,d}`-block.
Key lemmas, all PROVED in source:
- **Lemma 3.7(iii):** `{0,d}` is closed under `|x−y|`, so a `{0,d}` block
  persists in all descendants. (The run's `closure-0d-double-edge`.)
- **Lemma 3.8 (Parentage):** a `{0,d}`-block's parent is `{0,d}`-valued, or
  `{a,a+d}`-valued (0<a<d), or attains ≥ 2d. Drives the tower construction.
- **Lemma 3.10 (parity formula):** `a(i,j) ≡ Σ_k C(i,k) a_{j+k} (mod 2)`;
  Lucas governs. Generalizes Odlyzko's mod-4 linearization to all entries' parity.
- **Lemma 3.11 (Separation):** if `D` is 2-separated and `a_j..a_{j+i−1}`
  fixed, the set of `a_{j+i}` making `(i,j)` D-valued is 2-separated.
  Confirms the run's `two-separation-hypothesis` as the operative condition.
- **Lemma 3.13 (Attained tower) + 3.14 (shadow):** a value >1 at the bottom
  vertex forces an attained tower of {0,d} triangles with a large shadow.
- **Lemma 5.8 (Blocks are small or huge):** a good block of the triangle is
  either length ≤ 100L·4^M or spans all but 10L·2^M of the row — the dichotomy
  that yields the length threshold `R_m − 3R_{m−1}`.

## Hypotheses hold here? — NO (final, Directives 34/35)

`cht-inverse-theorem-hyp-check`: real primes depth-1000 give max normalized
gap 89 → M=7, longest 0-run L=2, R_0 = 100·L·8^M = 419,430,400 ≫ depth. The
right-half scan (`cht-right-half-0d-scan-6e8`) confirms the `{0,d}`-block
obstruction is absent at any length the theorem controls (observed max 25 vs
threshold T_1 = R_1 − 3R_0 = 5.63e16, a ≥ 2.25e15× gap). The theorem's bite is
out of range at every reachable depth, matching the authors' own difficulty
assessment. Do NOT re-run the hypothesis check.

## What it lets this run do

- Pins the deterministic obstruction hunt precisely onto **long zero-blocks**
  and **long shallow `{0,d}`-blocks (d≥2)** in the right half — the only ways
  small `{0,…,2^M}` initial data fails to decay. A counterexample to GC must
  produce one of these structures; proving none exist is exactly the
  regeneration/consumption question the run attacks via `(2,4)`-events.
- Route C is calibrated and not pursued: (i) needs Cramér, and the authors'
  own assessment says (ii),(iii) are as hard as the conjecture.

## What it does NOT settle

- Does not prove GC for the primes (deterministic case open; found only the
  inverse theorem).
- The `{0,d}`-block obstruction (iii) is what the run's own leading `{0,2}`
  block at j=1 would look like if shifted right; the theorem cannot see it
  at j=1 and the run's regeneration question is unaffected by (iii).

```claim
id: cht-theorem16-verbatim-fullpdf
statement: CHT 2026 Theorem 1.6 (deterministic inverse theorem), verified
  verbatim in the FULL PDF: if a_n ≤ 2^M, no length-L zero-block, and no
  right-half block (N' ≤ j) with 2^{M-m} < d ≤ 2^{M-m+1}, depth ≤ 2R_{m-1},
  length ≥ R_m - 3R_{m-1}, a(i,j..j+k-1) ∈ {0,d}, with R_m ≥ 4R_{m-1},
  R_0 ≥ 100L·8^M, then a(N-1,1) ∈ {0,1}. The {0,d}-block obstruction is
  restricted to columns j ≥ N' = ⌊N/2⌋.
hypotheses: non-negative integer initial data; R-tower hierarchy as stated;
  M, L ≥ 1; 1 ≤ N' ≤ N.
holds-here: no — checked against prime rows (density-1000 hyp-check and the
  6e8 right-half scan): Cramér (i) open and stronger than BHP; R_0 ≫ depth;
  right-half {0,d}-blocks observed ≤ 25 vs threshold 5.63e16.
status: proved in source (contrapositive, elementary), not checked here
bearing: the two obstruction families (long 0-blocks, long shallow right-half
  {0,d}-blocks) are the only ways small initial data fails to decay; directs
  the counterexample/regeneration hunt at exactly these, and calibrates Route
  C as out of reach.
anchor: research/sources/chase-hunter-tao-2026-cramer-random-model-gilbreath-FULLPDF.full.md (p.7-8)
contradicts: none — agrees with cht-inverse-theorem and cht-right-half-0d-scan-6e8
answers: cht-theorem16-fullpdf-read (Directive 35 item/thread next-step 2)
```

Also verified in the FULLPDF and consistent with the earlier HTML digest:
Theorem 1.2 (Cramér-geometric a.s. holds), Theorem 1.3 (general random models
under 2-separated non-concentration), Theorem 1.4 (Σc_i ≥ log(n+e)), Prop 2.1
(c_n ≥ exp(−Σ_{i<n} c_i)). No change to the run's use of these.
