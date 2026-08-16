# Pattern-finder report — round 6: the n3 admissibility closed form and the n3≥3 sharpening

## What changed since round 5

Rounds 1–5 catalogued every *parameter-determined* family count (triangles,
pentagons, hexagons, outer blocks, distance-2, coclique bounds, eigenvalue
multiplicities) as a quartic-in-`u` closed form with no low-order linear
recurrence and no OEIS entry. Round 6 attacks the one quantity that is **not**
parameter-determined — the count `n3` of disjoint triangle pairs joined by
exactly 2 edges — which is the pivot of the Makhnev-1988 line (n3=0 would rule
out the 99 graph; the two controls have n3=0). Prior rounds established only
that *integrality alone does not force n3≥1*. This round computes the exact
admissible set of n3 and derives its closed form.

## Finding 1 — the n3 admissible set is exactly multiples of 3 in [0, cap], cap = v·k(k−2)/4 (CHECKED)

The 62 Reimbayev order-6 count formulas give, for each feasible member, the
tightest nonnegativity upper bound `cap` on n3 and the residue class of n3.

**Exact values (computed here, `code/out/n3_upper_bounds_exact.py`, exact
Fraction arithmetic):**

| (v,k) | cap (brute) | v·k(k−2)/4 | match |
|---|---|---|---|
| (9,4)   | 0          | 18         | (k=4 degenerate: n5, with factor (k−4), binds at 0) |
| (99,14) | 4158       | 4158       | ✓ |
| (243,22)| 26730      | 26730      | ✓ |
| (6273,112) | 19320840 | 19320840  | ✓ |
| (494019,994) | 121781611728 | 121781611728 | ✓ |

For all k≥6 members the closed form
**`cap = v·k·(k−2)/4 = k(k−2)(k²+2)/8`** holds exactly
(`code/out/n3_cap_closed_form.py`, sympy: exponential degree 8 in u, i.e.
`v·k(k−2)/4`; verified brute-vs-analytic match on all four k≥6 members). The
k=4 case is the rook graph, which has no free n3 and is degenerate because the
binding formula there is n5 (contains (k−4)); reported honestly rather than
forced into the same form.

**Residue class (exact):** every member has period P=3 with the only good
residue **n3 ≡ 0 (mod 3)** (`code/out/n3_residue_check.py`). At (99,14) the
complete admissible set is the 1387 multiples of 3 in [0,4158]: 0,3,6,…,
4158 (`code/out/n3_admissible_check.py`, brute over the full 62-formula set).

Run through the sequence tools: `{0,4158,26730,19320840,121781611728}` has
no order-≤4 constant-coefficient linear recurrence, no low-degree polynomial
(octic in u), every term divisible by 18, and **no OEIS entry** — a miss
recorded so nobody searches again.

## Finding 2 — sharpening: if srg(99,14,1,2) exists then n3 ≥ 3 (reasoned, exact arithmetic on a sourced conditional)

Combine two exact/established ingredients:

1. **Order-6 integrality (computed this round):** admissible n3 at (99,14) is
   the multiples of 3 in [0,4158]. So n3 ∈ {0,3,6,…}. Integrality alone leaves
   n3=0 admissible.
2. **Makhnev 1988 Thm 2, re-derived and controls-checked (sourced; established
   in the library):** any putative srg(99,14,1,2) has n3 ≥ 1 (n3=0 would force
   the parameter-infeasible srg(33,12,1,6) subobject and hence nonexistence).

Intersecting the two: n3 is a positive multiple of 3, so
**`n3 ≥ 3`** — the previously recorded bound n3≥1 is sharpened to n3≥3
(`code/out/n3_sharpen3.py`).

## Status labels

- Finding 1 (admissible set = multiples of 3 in [0, cap], cap = v·k(k−2)/4):
  **computed in exact integer/Fraction arithmetic** over the 62 sourced
  Reimbayev formulas; the closed form is a derivation (sympy), verified
  brute-vs-analytic on every k≥6 feasible member. A conjecture only in the
  sense that it is a computation over a finite catalogue of sourced formulas,
  not a proof from first principles.
- Finding 2 (n3≥3): the arithmetic step (residue) is **computed**; the n3≥1
  premise is **sourced + re-derived** (Makhnev 1988, controlled against both
  existing graphs). The conjunction is a reasoned consequence, hence the n3≥3
  claim rests on the Makhnev conditional being correctly stated — the same
  caveat the library already attaches to that conditional.

## Bearing

The n3 axis is the one counting quantity that separates 99 (forced n3≥1 by
Makhnev) from both controls (n3=0). This round's contribution is (a) the exact
admissible set and its closed form cap = v·k(k−2)/4, and (b) the sharpening
n3≥3. It is a *constraint*, not a nonexistence proof — the n3≥3 case is still
open. First falsifying term: n3=3 would be the minimum genuine test; the bound
would be broken only by an n3 ∈ {1,2,4,…} actually occurring in a real
99-graph, which the residue class excludes exactly — so within the family the
bound cannot be falsified (it is an integer-arithmetic consequence of the
sourced formulas), and the honest statement is that n3≥3 is exact given the
Makhnev conditional.

## Independent cross-check of the cap at (99,14) — three routes agree

`code/out/n3_cap_crosscheck.py` computes cap three independent ways at
(99,14): (1) `n3_upper_cap` = min over all 62 negative-coefficient formulas of
`base/(-c)`; (2) the upper endpoint `U` of the `linear_bounds` interval from
the same nonnegativity constraints; (3) the closed form `v·k(k−2)/4`. All
three give **4158**. The bound is **sharp**: n3=4158 is admissible (all 62
formulas nonneg integer), n3=4159 is not. The smallest positive admissible n3
is **3**, verifying the n3≥3 sharpening.

## First falsifying term

- The residue n3≡0 (mod 3) is a *robust integer-arithmetic consequence* (all
  fractional n3-coefficients have denominator exactly 3, independent of which
  formula binds), so within the family it cannot be falsified by n3 ∈ {1,2,4,5,…}.
- The cap closed form v·k(k−2)/4 is exact on all four k≥6 feasible members and
  is a derivation (the binding formula is n1 = (1/12)nk(k−2) − n3/3 for k≥6).
  It would be broken only by a transcription error in the n1 formula — a
  hypothesis not under test here — so the honest statement is that it holds
  exactly over the sourced 62-formula catalogue.
- The n3≥3 claim is conditional: it need the Makhnev n3≥1 premise, so its
  falsifier is a 99-graph with n3 ∈ {0,1,2} (excluded by n3≥1 + residue) or an
  error in the Makhnev conditional. Within the family, n3≥3 is exact given that
  conditional.

## Files

- `code/out/n3_upper_bounds_exact.py` — exact caps and ratio-to-T table.
- `code/out/n3_cap_closed_form.py` — sympy closed form of the cap.
- `code/out/n3_residue_check.py` — period-3 residue class, all members.
- `code/out/n3_admissible_check.py` — full admissible set at (99,14).
- `code/out/n3_sharpen3.py` — the n3≥3 consequence.
