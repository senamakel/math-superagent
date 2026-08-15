# Thue unit descent in Q(∛2): does (1−ω)ⁿ⁻²-coefficient vanish again?

Program: `code/thue_unit_descent.py`
Output: `code/out/thue_unit_descent.captured.txt`

## Question

`c^3 − 2 d^3 = ±1` (Thue T2).  In `Q(ω)`, `ω³ = 2`, the field has class
number 1 and unit rank 1 and `1 − ω` is the fundamental unit, so every unit is
`±(1−ω)ⁿ`.  Writing `(1−ω)ⁿ = aₙ + bₙω + cₙω²`, the solutions `(c,d)` are
exactly the `n` with `cₙ = 0` (then `c = aₙ, d = −bₙ`, plus the negative-unit
partner `(−aₙ, bₙ)`).  The open completeness question is whether `cₙ` vanishes
only for `n ∈ {0,1}`.

## Recurrence (exact integers)

- forward (× (1−ω)): `aₙ₊₁ = aₙ − 2cₙ`, `bₙ₊₁ = bₙ − aₙ`, `cₙ₊₁ = cₙ − bₙ`,
  base `(a₀,b₀,c₀)=(1,0,0)`.
- backward (× (1−ω)⁻¹ = −(1+ω+ω²)): `a' = −a−2b−2c`, `b' = −a−b−2c`,
  `c' = −a−b−c`.

Sanity: forward gives `(1,0,0)→(1,−1,0)→(1,−2,1)→(−1,−3,3)→(−7,−2,6)…`,
so `(1−ω)¹ = 1−ω` (c₁=0) ✓ and `(1−ω)² = 1−2ω+ω²` (c₂=1≠0) ✓; inverse maps
`(1,−1,0)→(1,0,0)` ✓ and `(1,0,0)→(−1,−1,−1)` ✓.

## Result (numerical evidence over |n| ≤ 2000, exact arithmetic)

- `cₙ = 0` **exactly** for `n ∈ {0,1}` within `|n| ≤ 2000`.  No vanishing
  again inside this window.
- Full solution set with negative partners:
  `(c,d) = (1,0)` → `1³−2·0³ = 1`; `(1,1)` → `1−2 = −1`;
  `(−1,0)` → `−1`; `(−1,−1)` → `−1+2 = 1`.
  This is exactly PARI's proven `thue()` output
  (`thue c^3-2d^3=1 : [[-1,-1],[1,0]]`, `-1 : [[-1,0],[1,1]]`,
  from `code/out/thue_gp.captured.txt`).
- Growth: `cₙ` **oscillates** — 2373 sign changes among nonzero `cₙ` over
  `|n| ≤ 2000` — and grows irregularly, `|c₂₀₀₀| ≈ 5.6×10⁸⁶⁴` (exponentially
  in |n|, as expected from the embedded real embedding, |1−∛2| < 1 so negative
  powers grow).

## Interpretation — does the unit-descent prove the Thue equations complete?

**No, the scanned window is numerical evidence, not a proof.**  The `ω²`
coefficient is neither monotone nor sign-stable (2373 sign changes), so the
absence of a zero inside `|n| ≤ 2000` does not rule out a zero at some larger
`|n|`.  A recorded window can never be "complete for all n" on its own.

The genuine completeness of the Thue step rests on **PARI's proven `thue()`
algorithm** (already in the run: `code/out/thue_descend_fixed23.note.md`),
which proves the two Thue equations have exactly the four solutions above.
The unit-descent scan here **corroborates** that complete answer (agreeing on
all four solutions) and quantifies the growth/oscillation, but the scan alone
leaves completeness open in principle.  The elementary unit-window route would
need a separate proof that `cₙ ≠ 0` for all `n ∉ {0,1}` — e.g. that no power of
the fundamental unit lies in the rank-1 sublattice `Z + Zω` of the rank-2
`Z`-lattice `Z[ω]` — which is a unit-equation/subspace result, not something a
finite scan establishes.

## Where this sits

This is exploration, as intended: it shows the unit-descent does *not* on its
own give the elementary proof (no new structural fact is found that would make
most of the `n`-range unvisitable; the coefficient genuinely oscillates), and
it reconfirms the complete Thue answer by an independent exact route that
agrees with PARI.  The desk already proved `x² − y³ = 1` fully via the descent
+ PARI `thue()`.

```claim
id: thue-unit-descent-window-2000
statement: In Q(cuberoot 2), omega^3=2, writing (1-omega)^n = a_n + b_n omega
  + c_n omega^2, the omega^2-coefficient c_n vanishes exactly for n in {0,1}
  within |n| <= 2000.  Equivalently the only Thue solutions (c,d) of
  c^3 - 2 d^3 = +-1 recovered from zero-c_n units, both ± sign partners, are
  (1,0),(1,1),(-1,0),(-1,-1).
hypotheses: |n| <= 2000, exact integer recurrence; field has class number 1,
  unit rank 1, fundamental unit 1 - omega (verified by PARI bnfinit, see
  thue_gp.captured.txt).
holds-here: true for the exponent-2 case (this is the Thue equation behind
  x^2 - y^3 = 1); agrees with PARI's proven thue() complete answer.
status: checked (numerical, within |n| <= 2000; not a proof for all n;
  completeness of the Thue step is proved by PARI's thue() not by this scan).
bearing: corroborates the complete Thue resolution behind the exp2 proof;
  quantifies that the window route is not a finite-scan proof because c_n
  oscillates (2373 sign changes) and grows exponentially.
anchor: code/thue_unit_descent.py, code/out/thue_unit_descent.captured.txt
```
