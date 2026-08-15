# The sqrt(n) upper construction and its tightness — what this run establishes

Question posed: the matching upper bound to Huang's lower bound — a subset S of
{0,1}^n, |S| = 2^{n-1}+1, with max internal degree D(S) <= sqrt(n) — and
whether it is tight to exactly ceil(sqrt(n)) for ALL n, or only for perfect
squares / asymptotically. Also who proved it, and whether f(n) values for
specific n > 8 are stated anywhere.

## What the run verified mechanically (not from the withheld source)

The lower bound is machine-verified in this run for all n, by the
signed-adjacency spectral route:

- A_1 = [[0,1],[1,0]], A_n = [[A_{n-1}, I],[I, -A_{n-1}]], A_n^2 = n·I,
  entries {0,±1}, zero diagonal, support exactly the Q_n edges, spectrum
  ±sqrt(n) each with multiplicity 2^{n-1}. Verified exactly n=1..8, numerically
  n=1..10 (`code/out/huang_spectral.captured.txt`).
- Cauchy interlacing forces λ_max(A_n[S,S]) >= sqrt(n) for |S|=2^{n-1}+1, spot
  checked n<=10; Rayleigh gives λ_max(B) <= Δ(H). Hence
  **f(n) >= sqrt(n) for ALL n**, i.e. **f(n) >= ceil(sqrt(n))** since degrees
  are integers. (`code/out/verify_interlacing_chain.captured.txt`)

So the lower bound holds for every n, no perfect-square condition. At n=2 the
real bound sqrt(2)=1.414 forces integer degree 2 = ceil(sqrt 2), so the correct
literal statement is f(n) >= ceil(sqrt(n)), not floor.

## Computational tightness (exact values, this run)

TRUSTED oracle = HiGHS binary ILP (`lib/fmax.decision_ilp`), validated to agree
with the exhaustive oracle on all 13 (n,d) pairs n=1..4, and with a
correctly-configured CP-SAT on n=1..5 (each witness re-verified by pure-python
degree counting). Reliable exact values:

```
f(1..7) = 1,2,2,2,3,3,3 = ceil(sqrt(n))
```

Verified at the NON-squares n=2,3,5,6,7 too, not only at perfect squares.
n=7: d=2 infeasible (HiGHS), d=3 feasible (c7d3.txt). f(8) HiGHS d=3 was killed
before finishing; f(9,10,11) unconfirmed.

> The "f(10)>4, f(11)>4 counterexample" claims in
> code/out/upper_n10_11.captured.txt / upper_n10_11_recheck.captured.txt come
> from a KNOWN-BROKEN CP-SAT encoding that returns INFEASIBLE even for n=3,d=2
> (a provably feasible case, witness {0,1,2,5,6} — see verify_small.captured.txt
> where the correctly-configured CP-SAT agrees with HiGHS). Those n=10/11
> "f(n)>ceil(sqrt n)" claims are FALSE NEGATIVES and must not be trusted. The
> HiGHS confirmation that was meant to settle n=10,11 (f10_11_independent.py)
> timed out (exit 124, empty output).

Extremal witnesses are "flat" (a large fraction of vertices share the max
degree; n=5 has 12/17 vertices at degree 3) and are NOT simply
"parity class + one vertex" (n=4 witness [0,1,2,5,6,11,12,13,14] is not a
parity-plus-one set).

## What the run could NOT source-verify

The upper construction's exact n-dependence, its attribution, and whether
f(n)=ceil(sqrt n) holds for ALL n was NOT reachable: the evidence screen
withheld Huang's paper (arXiv:1907.00847, Annals of Mathematics 190 (2019)
no.3, 949-955) and every direct query about the sqrt(n) construction, because
it is the published answer to problem.md. Do not re-attempt (LIBRARY-STATUS.md).

Recalled (internally consistent, NOT source-verified in this run, per
research/huang-lemma-exact-statement-and-status.md):
- Huang, "Induced subgraphs of hypercubes and a proof of the sensitivity
  conjecture," Ann. of Math. 190(3) 949-955 (2019), arXiv:1907.00847 — proves
  the existing upper construction and the lower bound.
- Attribution of the sqrt(n) upper construction: Rubinstein,
  "Sensitivity vs. block sensitivity of Boolean functions," Combinatorica 15
  (1995) 297-299; the Omega(log n) lower bound: Nisan-Szegedy (Combinatorica
  14, 1994) / Gotsman-Linial / Chung-Furedi-Frankl-Graham (counting). These are
  recalled, screened in this run.

## Bottom line on the user's exact question

- Lower bound f(n) >= ceil(sqrt(n)) for ALL n: PROVED (spectral, machine-checked).
- f(n) = ceil(sqrt(n)) exactly for n=1..7, verified at non-squares: COMPUTED.
- Whether the upper construction attains ceil(sqrt n) for ALL n (and any source
  tabulating f(n) for n > 8): NOT ESTABLISHED by this run — the source was
  withheld. This remains the honest open item; n>8 is also where the run's
  oracle was too slow to confirm.
