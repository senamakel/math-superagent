# Chebyshev separation — bounded mean does not give density-1 (directive 9)

The sanity capture `code/out/chebyshev_sanity.txt` (script
`code/averaged/chebyshev_sanity.py`) exhibits an explicit two-point
distribution with mean exactly `c` whose upper-tail set has density bounded
away from 1 for every N. This answers directive 3(c) / task
`mean-implies-density1-or-io`: a bounded Cesàro mean alone does not force a
density-1 set where `ν₂(n) ≥ c·n`.

- `c = 0.49`; `a ∈ {c/2, 1}` with `P(a=c/2) = θ = 2(1−c)/(2−c) = 0.675497`
  and `P(a=1) = 1−θ = 0.324503`.
- Check: `E[a] = θ·(c/2) + (1−θ)·1 = c` exactly.
- Yet `P(a ≥ c) = 1−θ = 0.324503` for every N (the finite-prefix sample
  L=1000 gives 0.3250) — bounded away from 1.

In the SUPPLY analogue, `M(N) = (1/N)Σ_{n≤N} ν₂(n)/n` rising to ~0.49 is a
bounded-mean fact; turning it into "ν₂(n) ≥ c·n for density-1 many n" is
exactly the step that does **not** follow from the mean alone. Density-1 needs
a concentration / second-moment input — concretely, the empirical variance
`s2_N = Var(ν₂(n)/n over n≤N) → 0`, which the measured `s2_N` (0.01273 @100 →
0.00059 @4000) suggests but does not prove.

```claim
id: mean-bounded-not-density1
statement: For a_n ∈ [0,1], the Cesàro mean (1/N)Σ_{n≤N} a_n ≥ c does NOT
  imply the lower-tail set {n ≤ N : a_n < c−ε} has density → 0, and in
  particular does not imply a density-1 set where a_n ≥ c. Explicit witness:
  a two-point distribution a ∈ {c/2, 1} with P(a=c/2)=θ=2(1−c)/(2−c),
  P(a=1)=1−θ has E[a]=c exactly, yet P(a ≥ c)=1−θ is bounded away from 1 for
  every N (c=0.49 gives θ=0.675497, 1−θ=0.324503). Density-1 requires a
  concentration / second-moment input such as s2_N = Var(a_n) → 0, which the
  mean alone does not supply.
hypotheses: a_n ∈ [0,1]; the Cesàro-mean condition alone, with no
  second-moment / concentration input.
holds-here: yes — M(N)=mean(ν₂/n) rising to ~0.49 is a bounded-mean fact;
  the step from it to density-1 ν₂(n) ≥ c·n is exactly the step shown not to
  follow. This answers directive 3(c).
status: checked (exact arithmetic identity; witnessed in
  code/out/chebyshev_sanity.txt)
bearing: resolves task mean-implies-density1-or-io (the mean gives only
  positive lower density / infinitely-often, not density-1). The remaining
  density-1 route is variance-vanishing s2_N → 0 (thread
  variance-vanishing-density1, task chebyshev-second-moment-density1).
anchor: code/out/chebyshev_sanity.txt
```
