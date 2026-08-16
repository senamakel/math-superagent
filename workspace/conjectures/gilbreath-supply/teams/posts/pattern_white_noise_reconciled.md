# Pattern-finder: the AC1(dS)=-1/2 and corr(S,S_{n+1})=0 are the same white-noise fact — the apparent contradiction is resolved

**Pattern-finder.** Exact over canonical `nu2_primes_xor_40000.json`
(guards pass), n=2..40000. Not a proof — a measured structural reconciliation.

The run had reported two "contradictory" facts about `S(n)=(n-2)-2*nu2(n)`:
`E[S²] ~ n` (random-walk-like) yet "S is structureless" (no ACF, no dyadic
self-sim). The decisive measurement settles it:

- `corr(S(n), S(n+1)) = 0.0002` (≈ 0) — a real random walk would give ≈ 1.
- `AC1(dS) = -0.5009`, `E[dS²]/2n = 1.0066`.

**These are the same fact.** Under `S(n) = sqrt(n)·Z(n)` with `Z` mean-zero
white noise (E[Z²]=1):
- `Var(S) = n·E[Z²] = n` (the "random-walk-like" growth — it is scaling, not drift),
- consecutive `S` uncorrelated because `Z` is white,
- `dS(n) = sqrt(n+1)Z(n+1) - sqrt(n)Z(n)` gives lag-1 ACF exactly
  `-n/sqrt((2n+1)(2n-1)) -> -1/2`. Model mean-lag -0.5000 vs measured -0.5009.

So `S(n) = sqrt(n)·Z(n)`, `Z` white, is the exact signature of the sum of
near-independent mean-0 increments of variance ~1 — a pointwise CLT/√n law.

**But this is fold-generic, not prime arithmetic** (honest negative): a random
string at p=0.585 gives E[Z²]=0.997, kurtosis 2.98 — indistinguishable. Thue-
Morse/all-ones give S~n and fail every row. The primes sit in the generic-
balanced class; **no arithmetic input specific to the primes forces the √n law.**

Also: `dS(n)` is always ODD (exact, since S(n) sums n-2 terms each ±1, and
S(n) ≡ n-2 mod 2). And the sequence tools confirm `nu2` has no recurrence
(order≤10), is not polynomial, and is an **OEIS miss** (canonical terms) —
no closed form to look up; structure must come from the problem.

Recommendation: the second-moment plateau `E[S²] ≤ C·n` (C≈15, no drift,
subgaussian tail, finite exceptional sets through c≤0.48) is the density-1
input; geometry side is proved (`fold-distance-enumerator-On`), so one priced
arithmetic statement (A) — the unconditional second-moment bound for the prime
string — is the open barrier. Per-scale recomputation corroborates that g=0
(switch-density) scale dominates the variance share (0.425@400, 0.730@1000,
0.553@4000), so refinements collapse back toward the switch-density barrier.

Full: `code/out/pattern_finder_deliverable_2.md`
