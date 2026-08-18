# Kaleda–Shchurov 2011 — elementary-polycycle cyclicity bound (primary NOT held)

**IMPORTANT — WRONG FETCH on the "primary" file.** The file
`research/sources/kaleda-shchurov-elementary-polycycles-2011-primary.full.md` does NOT
contain this paper: it is arXiv:1102.1234, a homotopy-theory paper on topological Quillen
homology (wrong content under the wrong name). See
`research/findings/wrong-fetch-kaleda-shchurov-primary-homotopy-2026-08-19.md`.

## What is established (held evidence only)

**Citation abstract (DOI 10.1090/S1061-0022-2011-01158-6, St. Petersburg Math. J. 2011/2012,**
held in `research/summaries/citations_w2034778875.md`): "An estimate is found for the
number of limit cycles arising from polycycles in generic finite-parameter families of
differential equations on the two-sphere. It is proved that if the polycycles have a fixed
number of singular points and all the singular points are elementary, then an estimate of
cyclicity holds true, which is polynomial in the number of parameters of the family."

**Explicit form via Dukov 2023** (held full text, summary
`research/summaries/dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.md`
line 46): `E(n,k) ≤ C(n) k^{3n}` with `C(n) = 2^{5n²+20n}`, for polycycles with n fixed
elementary singular points in generic k-parameter C^∞ families. Carried at second-hand
level — Dukov's survey quotes it; the primary full text is NOT held.

## What it lets this run conclude

- The elementary-polycycle restricted class (ROOT.md row 1) is settled with an explicit
  polynomial-in-k bound for fixed n: this is a genuine restricted-class result and the
  sharpest elementary-polycycle bound this run holds.
- The bounds are **elementary-only** (nonzero eigenvalues): they do not cover nilpotent or
  degenerate DRR graphics, which is exactly the separation ROOT.md's obstruction section
  draws.
- The exact constant C(n)=2^{5n²+20n} must be re-verified against the real primary before
  any load-bearing use beyond "polynomial in k for fixed n" (which the citation abstract
  does establish).

```claim
id: h16-kaleda-shchurov-elementary-polycycle-bound
statement: For polycycles with a fixed number n of elementary singular points in generic k-parameter C^infty families of differential equations on the two-sphere, an estimate of cyclicity holds that is polynomial in k: E(n,k) <= C(n) k^{3n} with C(n) = 2^{5n^2+20n} (explicit form quoted via Dukov 2023; citation abstract establishes the polynomial-in-k statement).
hypotheses: fixed number n of singular points; all singular points elementary; generic k-parameter C^infty family.
holds-here: yes — restricted class only; the open DRR graphics are nilpotent/degenerate, not elementary.
status: asserted
evidence: citation abstract held (research/summaries/citations_w2034778875.md); explicit constant via Dukov 2023 summary (research/summaries/dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.md line 46); primary full text NOT held (the file claiming to be it is a wrong fetch — homotopy theory).
falsifier: the real Kaleda–Shchurov primary text giving a different bound shape; or a counterexample elementary polycycle in a generic k-parameter family with more than C(n)k^{3n} cycles.
sources: https://doi.org/10.1090/S1061-0022-2011-01158-6
anchor: research/summaries/citations_w2034778875.md
follows-from:
answers:
```
