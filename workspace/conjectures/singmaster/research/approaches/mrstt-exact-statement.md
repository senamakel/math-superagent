# MRSTT — the exact statement (the deliverable for this attempt)

Source read line-by-line: K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen,
"Singmaster's conjecture in the interior of Pascal's triangle", arXiv:2106.03335,
Quart. J. Math. 73 (2022) 1137–1177. Full text: research/sources/mrstt-fulltext.full.md.

Convention: below, `N(a)` counts **all** integer pairs `(n,m)`, `1<=m<n`, with
`C(n,m)=a`, both mirrors and the trivial pair counted (the MRSTT convention).
This is the convention of witnesses.json.

---

## The literal statement of Theorem 1.3

Let `0 < ε < 1`, and assume `t` is **sufficiently large depending on ε**. Then there
are **at most two** integer solutions `(n,m)` to `C(n,m)=t` in the region

```
exp( (log n)^{2/3+ε} )  ≤  m  ≤  n/2        (left half)
```

By symmetry `C(n,m)=C(n,n-m)`, there are therefore **at most four** solutions in the
symmetric interior

```
exp( (log n)^{2/3+ε} )  ≤  m  ≤  n − exp( (log n)^{2/3+ε} ).
```

Furthermore, in the smaller region `exp((log n)^{2/3+ε}) ≤ m ≤ n/exp((log n)^{1−ε′})`
there is **at most one** solution, whenever `0 < ε′ < ε/(2/3+ε)`, with `t` large
depending on both ε and ε′.

- effective: **yes** — Remark 1.7 states explicitly that the implied constants in
  "t sufficiently large depending on ε" are effective, but deliberately NOT optimized
  and likely too large for numerical use.
- uniform-in-k: the bound itself (at most 2 in a half, at most 4 in the interior) is
  **uniform over all column indices m in the interior region and over all t** (t large);
  the constant does not depend on m. But — see the gap below — it does **not** cover
  the small-m boundary, where only an ineffective bound exists.

## What is left open (Remark 1.5, verbatim content)

To prove Singmaster's conjecture it now suffices to handle

```
2 ≤ m ≤ exp( (log n)^{2/3+ε} n )      equivalently      2 ≤ m ≤ (log t) / (log_2 t)^{3/2−ε}
```

for any fixed ε>0 (the first equivalence is via `n/m ≍ exp(log t / m)`).

This small-m / outer-rows regime, where `m / log t → 0`, is **the entire remaining
gap**. There, the only known handle is Beukers–Shorey–Tijdeman / Siegel finiteness,
which is **completely ineffective** (no `w(n)` computable). So:

- effective: **no** in the boundary.
- uniform-in-k: **no** in the boundary — no bound at all (not even an ineffective
  finite one that is uniform) is known there.

## Sharpness (Remark 1.4)

The bound of two (per half) / four (interior) is attained by the infinite family
`C(n+1,m+1)=C(n,m+2)` with `n=F_{2j+2}F_{2j+3}−1`, `m=F_{2j}F_{2j+3}−1`
(Fibonacci). First member (j=1): 3003 with its eight occurrences.

## No-interior-3 (Remark 1.11)

There cannot be exactly three solutions in the interior: multiplicities there are
0, 1, 2, or 4 — never 3. (Three would force an `n=2m` solution, then
`|m′−m| ≫ m^{1/2}` by de Moivre–Laplace / Stirling, contradicting the distance
estimate (1.10).)

## Method and its hard limit (Section 1.3)

The new content is a **non-Archimedean** equidistribution argument: evaluate
`v_p(C(n,m))` (Legendre), draw `p` from primes in `[P, P+P/log^100 P]` with
`P ≈ exp((log(n+n′))^{2/3+ε/2})`, and compare covariance distributions (Prop 3.2).
The equidistribution estimate Prop 1.12 carries the hard restriction
`N, M = O(exp(log^{3/2−ε} P))`, which even under the Riemann Hypothesis cannot be
relaxed below `exp(log^{3/2−ε} P)`. Only a randomness heuristic would push to
`exp(P^c)`, which would lower the interior boundary from `exp((log n)^{2/3+ε})` to
`(log n)^C`. So the exponent **2/3 is a genuine, named barrier**, not an artifact.

## Bearing for the run

- Interior is done and effective: at most 4, never 3, uniform over the interior.
- **The whole remaining problem is the boundary** `2 ≤ m ≤ (log t)/(log_2 t)^{3/2−ε}`,
  and every known tool there is ineffective (Siegel/Beukers–Shorey–Tijdeman) or
  non-uniform in m.
- Therefore any uniform upper bound on `N(a)` must be built on the boundary, on a
  method different from the interior equidistribution argument. This is the precise
  statement of the frontier this run faces.
