# Tóth & Valtr, "The Erdős–Szekeres theorem: upper bounds and related results"

<!-- source: http://www.cs.bme.hu/~geza/es-1.pdf | full text at research/sources/toth-valtr-ES-theorem-upper-bounds-and-related-results.full.md -->

**Publication.** G. Tóth and P. Valtr, survey chapter in *Combinatorial and Computational Geometry* (Goodman, Pach, Welzl eds.), MSRI Publications 52 (2005) 605–623. Author copy (cs.bme.hu/~geza/es-1.pdf) is open access in the library.

**What it is.** The authors' own consolidated account of the upper-bound line, with **full proofs** of Erdős–Szekeres (cups–caps), Chung–Graham, Kleitman–Pachter, and Tóth–Valtr, plus a new combined improvement (Theorem 1) shaving one more. This is the primary treatment of the binomial-form upper bound, before Suk.

## The upper-bound theorems, exact statements and proofs (asserted-by-source, proofs given in the text)

- **ES cups–caps**: f(n,m) = C(n+m-4, n-2) + 1 is the least N such that any N general-position points contain an n-cap or an m-cup. Hence ES(n) ≤ f(n,n) = C(2n-4,n-2)+1. (Theorem 2, with the double-induction proof and Observation 1 — the cap/cup extension lemma.)
- **Chung–Graham** (Thm 3): ES(n) ≤ C(2n-4, n-2) for n ≥ 4. (Proof: A = right endpoints of (n-1)-caps, |A| ≥ C(2n-5,n-3); case analysis with an extremal-slope segment.)
- **Kleitman–Pachter** (Thm 4): ES(n) ≤ C(2n-4,n-2) + 7 - 2n for n ≥ 4. Introduces *vertical* point sets and f_v(n,m) ≤ C(n+m-4,n-2) + 7 - n - m.
- **Tóth–Valtr** (Thm 5): ES(n) ≤ C(2n-5, n-2) + 2 for n ≥ 3. Projective-transformation argument: pull a hull vertex to infinity so every (n-1)-cap extends to a convex n-gon, then apply f(n-1,n).
- **Tóth–Valtr combined** (Theorem 1): ES(n) ≤ C(2n-5, n-2) + 1 for n ≥ 5. Combines Chung–Graham's set-splitting with the projective transform: with N = C(2n-5,n-2)+1, A = right endpoints of (n-2)-caps with |A| = C(2n-6,n-3) and B with |B| = C(2n-6,n-2), then the largest-slope argument forces a convex n-gon.

## Related results collected (asserted-by-source)

- **Empty polygons**: g(3)=3, g(4)=5, g(5)=10 (Harborth), no finite g(7) (Horton); the empty-hexagon g(6) was open here with Overmars's 29-point example (later settled g(6)=30 by Heule–Scheucher, in library). `X_k(P)` empty-k-gon identities of Ahrens–Gordon–McMahon and Pinchasi–Radoičić–Sharir.
- **Convex bodies**: P3(n) bounds — 2^{n-2} ≤ P3(n) ≤ C(2n-4,n-2)^2 (Pach–Tóth); property P_k families.
- **Partitioned ES theorem**: any finite X in general position partitions into ≤ c_n convex clusterings plus ≤ c'_n leftover points (Pór–Valtr 2002, PV02). A *convex n-clustering*: X partitions into n equal-size sets X_1,..,X_n with x_1..x_n a convex n-gon for every transversal.
- **Positive fraction ES theorem** (BV98): any sufficiently large X contains a convex n-clustering of size ≥ ε_n·|X|, ε_n > 0 independent of X. (Full source in library: barany-valtr-A-positive-fraction-ES-theorem.full.md.)
- **k-convex variants and higher-dimensional** analogues surveyed.

## claim block (for CLAIMS.md)
```claim
id: toth-valtr-2005-combined
statement: ES(n) ≤ C(2n-5,n-2) + 1 for n ≥ 5, obtained by combining the Chung–Graham set-splitting and the Tóth–Valtr projective transform (Theorem 1). Also ES(n) ≤ C(2n-4,n-2)+1 (ES 1935), ≤ C(2n-4,n-2) (Chung–Graham), ≤ C(2n-4,n-2)+7-2n (Kleitman–Pachter), ≤ C(2n-5,n-2)+2 (Tóth–Valtr), all with proofs in the text.
hypotheses: general position; the cup/cap definitions; f(n,m)=C(n+m-4,n-2)+1 tight.
holds-here: true; these are the exact binomial-form upper bounds for the exact ES function. NOT bearing on the conjectured exact value 2^{n-2}+1 — they sit far above it (≈ 4^n/√n base) and were superseded for large n by Suk.
status: proved (peer-reviewed survey, full proofs in the text; not independently re-deriven here but the proofs are quoted directly).
bearing: complete primary record of the binomial-form upper-bound line and its proofs; the projective-transform "pull a hull vertex to infinity so every cap extends" trick is a reusable structural technique for the run's own candidate arguments.
anchor: research/sources/toth-valtr-ES-theorem-upper-bounds-and-related-results.full.md
```
