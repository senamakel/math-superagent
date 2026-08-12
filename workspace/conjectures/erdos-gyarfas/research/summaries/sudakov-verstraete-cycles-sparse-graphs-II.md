# Sudakov–Verstraëte — Cycles in sparse graphs II

Source: https://arxiv.org/pdf/1010.5309 (arXiv:1010.5309)
Full text: `research/sources/sudakov-verstraete-cycles-sparse-graphs-II.full.md`

## What it is

Companion to "Cycle lengths in sparse graphs" (Combinatorica 28 (2008) 357–372).
Studies which cycle lengths must appear in graphs with **large independence ratio**
ι(G) = sup_X |X|/α(X) — a relaxation of chromatic number. Consequence for the EG
direction: cycle lengths from prescribed sparse sequences (primes, powers) are forced
by high independence ratio, a different regime than minimum-degree-3.

## Key theorems (as stated in the paper)

- **Theorem 1**: every triangle-free graph with independence ratio ≥ k ≥ 3 has cycles
  of Ω(k² log k) consecutive lengths.
- **Theorem 2** (hereditary properties): if P is hereditary with speed at most f and
  G ∈ P has ι(G) > 18k + 4, then G has cycles of at least (1/2)f⁻¹(k) consecutive lengths.
- **Theorem 4** (application): if σ is an infinite increasing sequence with σ₁≥3 and
  log σ_r ≤ σ_{r−1}, then an n-vertex graph with ι(G) ≥ 3 exp(8 log* n) contains a cycle
  of length in σ. In particular (taking σ = primes): **a graph of independence ratio
  ≥ 3 exp(8 log* n) contains a cycle of prime length**. Also applies to powers of three,
  and to 2+1, 2²+1, 2^{2²}+1, ... — but NOT to powers of two, whose gaps 2^k do not
  satisfy log σ_r ≤ σ_{r−1}.
- **Theorem 6**: triangle-free G with ι(G) > 3k+1 (k ≥ e¹⁵) has a cycle of length ≥ 3k² log k.

## Why it matters (and does not matter) here

- It is the **dense/independence-ratio regime**, not the δ≥3 regime. The run's
  conjectures (Verstraëte 2005, Sudakov–Verstraëte 2008, Liu–Montgomery) are about
  average degree / independence ratio; this paper is the same family.
- It gives cycle lengths in prescribed *sets* but under exponentially strong hypotheses,
  and the sequence condition explicitly excludes powers of two by their growth. So it is
  a boundary marker: any theorem forcing a power-of-two cycle from an interval of lengths
  must handle the factor-2 growth gap, which is precisely the run's central obstruction.

## Status

Peer-reviewed companion (Combinatorica); arXiv open text read here. Theorems as
abstracted. No claim block is warranted beyond the boundary-marker observation, which
is already embodied in `EG-dense-regime-constraint`.