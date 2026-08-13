# MRSTT 2021 — Singmaster's conjecture in the interior of Pascal's triangle

Source: K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen, arXiv:2106.03335
(Quart. J. Math. 73 (2022) 1137–1177). Full text read. [[mrstt-fulltext]]

## The interior theorem (Theorem 1.3)

Let `0 < ε < 1`, `t` sufficiently large depending on `ε`. At most **two** integer
solutions `(n,m)` to `C(n,m)=t` in the left half
`exp((log n)^{2/3+ε}) ≤ m ≤ n/2`; hence at most **four** in the symmetric interior
`exp((log n)^{2/3+ε}) ≤ m ≤ n − exp((log n)^{2/3+ε})`. In the smaller region
`exp((log n)^{2/3+ε}) ≤ m ≤ n/exp((log n)^{1−ε′})` at most **one**, for
`0 < ε′ < ε/(2/3+ε)`.

- **Hypotheses hold here**: yes. This is exactly the multiplicity-counting problem.
- **Effective**: threshold "t sufficiently large depending on ε" is effective but
  deliberately not optimized (Remark 1.7 — too large for numerical use).
- **Sharp**: the bound of two/four is attained by the infinite Fibonacci family
  `C(n+1,m+1)=C(n,m+2)`, `n=F_{2j+2}F_{2j+3}−1, m=F_{2j}F_{2j+3}−1` (Remark 1.4).
- **Remark 1.11 (not in the abstract/digest)**: a modification shows there cannot be
  **exactly three** solutions in the interior — three would force an `n=2m` solution,
  then `|m′−m| ≫ m^{1/2}` (de Moivre–Laplace/Stirling) contradicts the distance
  bound (1.10). So interior multiplicities are 0,1,2,4 — never 3.

## Remark 1.5 — what the theorem leaves open (the boundary)

To prove Conjecture 1.1 it now suffices to handle
`2 ≤ m ≤ exp((log n)^{2/3+ε})`, equivalently `2 ≤ m ≤ (log t)/(log₂t)^{3/2−ε}`.
This small-m / outer-rows regime, where `m/log t → 0`, is stated as **the main
obstruction**. The only handle there is Beukers–Shorey–Tijdeman / Siegel finiteness,
which is **completely ineffective** (no `w(n)` computable).

## Method (the genuinely new part, Section 1.3)

Non-Archimedean, not Kane's archimedean analysis. From Legendre's formula,
`v_p(C(n,m)) = Σ_j ({m/p^j}+{(n−m)/p^j}−{n/p^j})`. For two solutions the two sides
of (1.13) are equal for all primes `p`. MRSTT draw `p` uniformly from primes in
`[P, P+P/log^100 P]` with `P ≈ exp((log n)^{2/3+ε/2})` and compare probability
distributions of the fractional parts via **covariances** (Prop 3.2: `c_j(N,M) ≈
1/12ab` when `aN≈bM` commensurable, else tiny), obtaining the distance estimate
Prop 1.9. Central tool is the **equidistribution estimate** Prop 1.12 (Vaughan's
identity + Vinogradov), which carries the hard restriction
`N, M = O(exp(log^{3/2−ε} P))`.

**The limit of the method (Section 1.3)**: even under the Riemann Hypothesis this
restriction cannot be relaxed below `exp(log^{3/2−ε} P)`; only a heuristic
(randomness) argument would push to `exp(P^c)`, which would lower the interior range
from `exp((log n)^{2/3+ε})` to `(log n)^C`. So the interior exponent `2/3` is a
real, named obstacle, not an artifact.

## Theorem 1.8 — falling factorial analogue

At most two integer solutions to `(n)_m = t` in `exp((log n)^{2/3+ε}) ≤ m < n`;
sharp (a family `(a²−a)_{a²−2a} = (a²−a−1)_{a²−2a+1}` attains it).

## Bearing for this run

Confirms and sharpens the established MRSTT story: interior is ≤4 (never 3) with an
effective-but-huge threshold; the **whole remaining gap is the boundary
`2 ≤ m ≤ (log t)/(log₂t)^{3/2−ε}`**, and nothing effective is known there. Also
records de Weger's conjecture (Remark 1.4) that all nontrivial collisions are known,
which would imply Singmaster.

```claim
id: mrstt-interior-nothree
statement: MRSTT (arXiv:2106.03335, Remark 1.11) prove there cannot be exactly three
  solutions to C(n,m)=t in the interior exp(log^{2/3+eps} n) <= m <= n - exp(log^{2/3+eps} n);
  interior multiplicities are 0,1,2,4 (never 3). (Three would force n=2m, then
  |m'-m| >> m^{1/2}, contradicting the distance estimate (1.10).)
hypotheses: t sufficiently large depending on eps; 0<eps<1.
holds-here: yes — constrains the multiplicity spectrum the run must be consistent with.
status: asserted (by the paper's own proof modification; not re-derived here)
bearing: any proposed spectrum of multiplicities must not assign interior value 3.
anchor: research/summaries/mrstt-fulltext.md
```

```claim
id: mrstt-method-limit
statement: The non-archimedean equidistribution method (Prop 1.12) requires
  N,M = O(exp(log^{3/2-eps} P)), and even under the Riemann Hypothesis this cannot be
  relaxed; only a randomness heuristic pushes to exp(P^c), which would lower the
  interior boundary function from exp((log n)^{2/3+eps}) to (log n)^C. (MRSTT §1.3.)
hypotheses: 0<eps fixed; the scale P ~ exp((log n)^{2/3+eps/2}).
holds-here: yes — this is named as the obstruction to extending the interior theorem.
status: asserted (by the paper; heuristic parts flagged as such there)
bearing: the 2/3 exponent is a genuine barrier for the interior approach; closing the
  boundary needs a different method.
anchor: research/summaries/mrstt-fulltext.md
```
