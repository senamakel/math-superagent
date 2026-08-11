# Cambie & Yan, "Descents and inversions in powers of permutations" (arXiv:2408.01211)

Full statement-level text: L0 `cambie_yan_html.full.md` (arXiv abs page: [[cambie_yan_descents_inversions_powers]]).

## Statements (uniform π ∈ S_n, fixed k ∈ ℤ⁺, valid n ≥ 2k+1)

With τ(k)=#divisors, σ(k)=Σ_{d|k} d, τ_o(k)=τ(k/2^{ν₂(k)}) (#odd divisors):

- **Thm 1.1 (descents):** (1/n!) Σ_π des(π^k) = (n−1)/2 − [τ(k)² − τ(k) − τ_o(k) + σ(k)]/(2n).
- **Thm 1.2 (inversions):** (1/n!) Σ_π inv(π^k) = n(n−1)/4 − (τ(k)−1)n/6 − [τ(k)² − τ(k) − τ_o(k) + σ(k)]/12.
- k=2,3 descents = (n−1)/2 − 2/n, confirming Archer–Geary (see [[archer_geary_descents_powers]]).
- Thms 1.3–1.5: Grassmannian-power counts via Gessel–Reutenauer.

## Why it matters

For each fixed exponent t, our f_n(k) = #{(π,i): (π^i)(m)<(π^i)(j)} sums the per-pair
inversion count of π^t over π. Thm 1.2's proof (Section 2, Lemmas 2.1–2.6) shows that for
fixed t with n ≥ 2t+1 the # of π with an inversion at gap d in π^t is translation-invariant
in i and **affine in d** — the exact per-exponent source of the empirically-observed
gap-linearity of f_n(k) (n ≤ 11; extend_f.json, gaps.py). Full affine expression: see the
summary saved at [[report_literature_ranks_powers]] or the L2 fold [[../../L2/mechanism_pair_inversions]].

## Caveat that matters for this run

The n ≥ 2k+1 hypothesis excludes exponents t > (n−1)/2 that appear in the full sum over
i = 1..n!. Naive extrapolation FAILS: summing per-exponent slopes over t=1..n! for n=3
gives 32, but true B_3 = 1. The large-exponent regime (π^t periodic, small ord(π)) must be
handled separately — the open step to closed forms A_n,B_n.

## Not settled

- No formula for rank(π^i) or sums of rank over a cyclic subgroup <π>; the E[(π,i)-uniform rank(π^i)] we need is absent here.
