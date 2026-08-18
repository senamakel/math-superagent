# Pedregal, "A variational approach to Hilbert's 16th problem" (arXiv:2103.07193, 2021) — UNREFEREED claimed resolution

<!-- source: https://arxiv.org/pdf/2103.07193 | converted from HTML (this is the arXiv PDF sibling of the ar5iv full text). Full text: [[pedregal-variational-h16-ar5iv.full]]. Claim `h16-pedregal-variational-claim-unrefereed` (in research/notes/claims.md, and duplicated in derived/CLAIMS.md). -->

## What it (claims to) establish — treat as suspect, NOT a result

Claims a **uniform upper bound on H(n) depending only on degree**:

- even n: `H(n) ≤ (5/2)n⁴ − (23/2)n³ + (43/2)n² − (37/2)n + 7`
- odd n: `H(n) ≤ (5/2)n⁴ − (23/2)n³ + (41/2)n² − (33/2)n + 6`

and in particular **H(2) = 4** — i.e. it claims to prove the open H16.2 and the
standing H(2)=4 conjecture. Method: **variational** — counts limit cycles as
global minimizers of `E₀(x,y) = (1/2)∫₀¹(Py'−Qx')² dt`, applies Morse
inequalities to a perturbation E_ε, bounding critical points via **Bezout** and
**Harnack** on the divergence curve div = P_x+Q_y = 0 and its contact points.

## Why the run treats it as refuted (not a resolution)

- **Test 1 (smooth test):** the argument never uses analyticity of the return
  map — it counts critical points of a functional via Bezout/Harnack, exactly
  the shape of Dulac's error. Prima facie refuted.
- **Unrefereed** preprint; no journal acceptance located; community (held Gasull
  2024 survey) still treats H16.2 as open.
- The prior variant Llibre–Pedregal (arXiv:1411.6814) **announced a mistake in
  its limit-cycle counting**; this 2021 paper is the unverified reworking.
- It yields a **quartic** upper bound, which does NOT collide with the n²log n
  lower bound (so Test 2 passes) — the suspicion rests on Test 1 and status.

## Hypotheses / holds here

None beyond degree n>1 polynomial P,Q (claimed). **Holds here: NO** — treated as
a claim to test, not a result. The run's premise (H16.2 open, H(2)=4 conjectured
not proved) is unchanged.

**Evidence class: asserted-by-source, unverified** (full ar5iv text held).

## Bearing / implication

Do not cite Pedregal's H(2)=4 as established. Its variational-obstruction shape
is a **negative example**: the contrast with the o-minimal route
(`h16-ominimality-route-roussarie`) shows where a valid uniform-finiteness proof
must use analyticity of the return map.
