# Pedregal — "A variational approach to Hilbert's 16th problem within the framework of global analysis" (arXiv:2103.07193, 2021, UNREFEREED preprint)

Full text: `research/sources/pedregal-variational-h16-ar5iv.full.md` (ar5iv HTML conversion, 301KB).
Also `research/sources/pedregal-variational-h16-full.full.md` (arXiv abstract; the PDF body did not extract).
Primary URL: https://arxiv.org/abs/2103.07193

## What it claims (statement of the claim, NOT established)

This is a **claimed resolution of exactly the run's open problem, H16.2** —
and therefore must be treated as a suspect claim to test, not an accepted
result. It asserts:

- An explicit **uniform upper bound on the Hilbert number depending only on
  the degree**: for degree `n > 1`,
  - `H(n) ≤ (5/2)n^4 − (23/2)n^3 + (43/2)n^2 − (37/2)n + 7` if `n` even,
  - `H(n) ≤ (5/2)n^4 − (23/2)n^3 + (41/2)n^2 − (33/2)n + 6` if `n` odd.
- Hence `H(2) = 4` (the standing conjecture: `H(2) = 4` is claimed **proved**;
  only `H(2) ≥ 4` is established in the literature — Shi, Chen–Wang).
- It claims to answer Hilbert's 16th problem and Smale's 13th problem with a
  universal exponent `q = 4` (`H(n) ≤ C n^4`).

## The method (why it is suspect under the run's three tests)

The proof is **entirely variational** and, per its own description, "no
particular expertise in dynamical systems is necessary." The mechanism:

1. Writing limit cycles as zeros of the functional
   `E0(x,y) = (1/2) ∫₀¹ (P y' − Q x')² dt`,
   identifying limit cycles with absolute (global) minimizers of `E0 ≥ 0`.
2. Counting global minimizers via **Morse inequalities** on a perturbation
   `Eε`, relating connected components of sublevel sets `{Eε ≤ a}` to critical
   points of `E0` with critical value away from zero.
3. Bounding critical points using Bezout and Harnack on the divergence curve
   `div = Px + Qy = 0` and the contact-point system.

**Test 1 (smooth test) violation risk.** The argument is built from Morse
theory, Bezout, Harnack, and the *divergence curve* — topolog/algebraic-geometry
of the vector-field data — and nowhere uses analyticity/quasianalyticity of the
**return map**, whose isolated fixed points are the limit cycles. This is
exactly the shape of error Test 1 flags: a `C^∞` field can have infinitely many
limit cycles, so any valid finiteness argument must have a step that fails for
`smooth` fields. A Morse/critical-point and curve-component count could, in
principle, bound critical points of `E0` — but whether the *isolated periodic
orbits* (a dynamical, non-algebraic object) are in bijection with those counted
components is the fragile step. The paper's own claim "limit cycles correspond
to global minimizers" plus illumination of connected components of sublevel sets
is where the isolatedness/analyticity of limit cycles must enter, and the paper
does not clearly exhibit such a step.

**Test 3 (slow–fast) relevance.** A uniform polynomial bound `n^4` does not
collide with the `n² log n` lower bound, so Test 2's lower-bound check is not
the failure. But the reliance on the divergence curve `div=0` and its contact
points is precisely the kind of geometric-algebraic count that canard /
relaxation-oscillation (slow–fast) constructions bypass in the singular limit.

## Provenance / status in the community

- **UNREFEREED preprint** (arXiv:2103.07193, March 2021). No journal
  publication or referee acceptance located; **not established** by this run.
- It is the successor in the **Llibre–Pedregal variational program**, whose
  earlier iteration **arXiv:1411.6814 "Hilbert's 16th problem. When variational
  principles meet differential systems"** explicitly states in its abstract:
  *"Thanks to the interest of many people, a mistake has been found in our way
  of counting limit cycles. We are working on a new version."* — i.e., the
  earlier variational counting method was **found to contain a mistake** in
  counting limit cycles. This 2021 paper is the reworking; whether the cited
  mistake is fully repaired is not independently established.
- The held **Gasull 2024 survey** ("From Abel's differential equations to
  Hilbert's 16th problem", São Paulo J. Math. Sci., held full text) states as
  of 2024 that no universal upper bound on H(n) is proven and the problem is
  open. So the community does **not** treat Pedregal's arXiv paper as having
  settled H16.2.

## Bottom line for the run

Record as claim `h16-pedregal-variational-claim-unrefereed`:
**asserted-by-source, NOT established.** If Pedregal were right, the run's whole
frame (H(2)<∞ equivalent to DRR finite cyclicity, "open") would change — but on
the balance of evidence (unrefereed preprint, prior variant retracted/announced-
mistaken, method apparently failing Test 1, community still treating H16.2 as
open in 2024) this is treated as a **suspect claim to test**, not as a result.
The concrete test applicable here: check whether the claimed bijection between
isolated periodic orbits and counted sublevel-set components of `E0` holds —
the step where analyticity must enter.
