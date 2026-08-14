# Khovanova & Marton, "Archive Labeling Sequences" — arXiv v2 (proof of the bound)

**Source:** https://arxiv.org/html/2305.10357 (arXiv:2305.10357v2 [math.HO], 16 Feb 2024). Full text: `research/sources/archive-labeling-arxiv-latest.full.md`. (v1, 25 Apr 2023, is `research/sources/archive-labeling-arxiv-v1.full.md` — it lacks Section 9; use v2.) Published version: `research/sources/archive-labeling-amm-published.full.md`.

This is the version the run's G2 bound rests on. It contains the **proof** of Proposition 9.1 that the AMM version only states.

## What this version establishes that the run needs

### Prop 9.1 — the finite search bound (Section 9, "All Your Base")
For any digit d > 0 in base b > d, the maximum possible value of a=(d,b) is b^b, and every x with f_d(x,b) = x satisfies **x ≤ d·b^b**.

Proof (on disk, complete): f_b(b^b) = b^b (so a solution exists at b^b); f_d(d·b^b) = d·b^b + 1 and every x in [d·b^b, (d+1)·b^b] has leading digit d so no solution lies there; then f_d((d+1)b^b) = (d+2)b^b, and a base-b version of Lemma 5.1 pushes the count permanently ahead of the index, so no later solution exists.

**Base 10 instance:** every n with f(n,d) = n for d ∈ {1,...,9} satisfies n ≤ d·10^10. Hypothesis matching for PE156: the paper's f_d(x,b) counts 1..x; the problem's f(n,d) counts 0..n; they agree for d > 0 because 0 contributes no nonzero digit. **The bound transfers verbatim** (recorded in `claim km-prop91-bound`, gap G2 discharged in `research/backward/fixed-point-enumeration.md`).

### Section 7 — digit-count closed form (same as AMM eq. (1))
f_d(x) = Σ_k c_d(x_k), per-position closed form; O(log x) exact evaluation.

### Lemma 7.1 — skip lemma
If a≥(d) > x and f_d(y) < x for some y > x, then a≥(d) > y. This is what lets the fixed-point search jump over intervals.

### Section 9 — related facts (context, not required by PE156)
- A092175(b) = a>(1,b); A165617(b) = number of solutions of f_1(x,b)=x (base 10: 83, i.e. 84 with n=0).
- A226238: largest x with f_1(x,b)=x; base 10 largest is 1 111 111 110 (the concatenation of nine 1s and a 0), which is also Table 3's max for d=1.
- Theorem 9.2: a=(d,b) well-defined for b > 2 and d > 0 (except b=2, d a power of 2).
- Prop 9.3: a=(0,b) < b^(b+3) when defined; Theorem 8.1 (Section 5): a=(0) is not well-defined in base 10.

## Implication for PE156

The bound n ≤ d·10^10 is **proven**, not conjectured, in a citable primary source now on disk. This is the lemma that makes the efficient solver's completeness claim sound: search [0, d·10^10] with the closed-form f and the skip lemma, and every fixed point is found without enumerating the interval.