# Pinsky & Schickentanz, "Inversions in Random Permutations Under the Ewens Sampling Distribution…" (arXiv:2510.20654) — superseded duplicate

This file holds the raw arXiv abstract-page HTML for arXiv:2510.20654. It is
**superseded**: the full curated summary is `pinsky_schickentanz_ewens_html.md`
(pointing at `L0/pinsky_schickentanz_ewens_html.full.md` and the earlier
`pinsky_schickentanz_ewens_inversions.full.md` for the complete text), and every
substantive claim lives there. The abstract page adds only:

- Authors: Ross G. Pinsky, Dominic T. Schickentanz. math.PR / math.CO, 60C05 / 05A05.
- v1 23 Oct 2025, v2 17 Nov 2025; DOI 10.48550/arXiv.2510.20654.
- Abstract: exact E[inversions] under Ewens P_θ^(n); exact per-pair inversion
  probability (decreasing in θ iff |j−i|≥2); expected-inversion and per-pair formulas
  conditioned on #fixed points; asymptotics n→∞, θ→∞, θ→0. v2 added the
  fixed-point-conditioned part (title changed accordingly).

## What the source establishes (repeated here so this file is self-sufficient)

Thm 1a (eq 1.1) — unconditioned pair-inversion probability:
  P_θ^(n)((i,j) inverted) = n(n−2(j−i)+1)/[2(θ+n−1)] − (n−1)(n−2(j−i))/[2(θ+n−2)]
  — depends only on the gap j−i and is **affine in the gap**. θ=1 (uniform) → 1/2;
  θ=0 (single cycle) → 1/2 + (j−i−1)/[(n−1)(n−2)].
Prop 10a (eq 3.2) — fixed-point-conditioned version, five-term combination of ratios
  of #fixed-point probabilities, each term affine in the gap.
Prop 4 — exact #fixed-points distribution
  P_θ^(n)(#fixed=m) = [n!θ^m/(m!θ^{(n)})]Σ_{k=0}^{n−m}(−θ)^k θ^{(n−m−k)}/(k!(n−m−k)!).
This is a second, independent proof of the same gap-affine/fixed-point-driven mechanism
behind f_n(k)=A_n+(k−1)B_n (uniform case θ=1 is what Q(n) sums over). **Not** a sum
over the cyclic subgroup {π^i}.

See `pinsky_schickentanz_ewens_html.md` for full implications and caveats.
