# Lemma 5.4 even-domain theorem — kernel-checked via the halving identity

**Status: formalised** (lean_check: compiled=true, verified=true, zero `sorryAx`;
axioms all ⊆ `{propext, Classical.choice, Quot.sound}`).
Formalisation: `code/lean/lemma54_even_domain.lean`.

## What was proved

For a `{0,2}^L` pattern `el` (i.e. `∀ e ∈ el, e = 0 ∨ e = 2`) and an **even**
start `v : Nat`, with the trajectory `d_0 = v`, `d_{k+1} = |d_k - eps_k|`
(`runAbs`) and `countTwo el = ν₂ = #{s : eps_s = 2}`:

- `lemma54_even_forward` : `v ≤ 2·ν₂ + 2  ⟹  d_L ∈ {0,2}`
- `lemma54_even_high`    : `2·ν₂ + 2 < v  ⟹  d_L = v - 2·ν₂` (exact)
- `run_absorb02`         : `{0,2}` is absorbing under `|·-e|` for `e ∈ {0,2}`
- `lemma54_even`         : the two implications bundled
- `lemma54_even_iff`     : `(d_L ∈ {0,2}) ↔ v ≤ 2·ν₂ + 2`

The `Even v` hypothesis is **explicit and load-bearing** (needed to lift the
halved `{0,1}` conclusion back to `{0,2}`; parity-preservation makes the whole
orbit even).

## The halving route

The proof does **not** re-run the descent on the even domain. It *halves*:

- `dist_even_halves` (the halving identity): for even `a, b`,
  `|a - b|/2 = |a/2 - b/2|`.  In the `a = k+k` form this is
  `(x+x).dist (y+y) / 2 = x.dist y`.
- So a `{0,2}^L` pattern halved is a `{0,1}^L` pattern
  (`map_halve_zero_one`), with `ν₂ = ν₁(halved)` (`countTwo_eq_countOnes_half_of`),
  and `v/2` is the halved start.
- `runAbs_halve` : `runAbs v el / 2 = runAbs (v/2) (halved el)` — the halved
  orbit is the orbit of the halved data.
- `descent_claim1` / `descent_claim2` (the **unweakened** halved core, restated
  in full: `{0,1}` pattern, `countOnes = ν₁`, `w ≤ ν₁+1 ⟹ h_L ∈ {0,1}`,
  `ν₁+1 < w ⟹ h_L = w - ν₁`) applied to `w = v/2`.
- `even_of_halve` lifts an even value with halving in `{0,1}` back to `{0,2}`.

## Axioms

Every theorem depends on at most `propext`, `Classical.choice`, `Quot.sound`.
`descent_claim1`, `descent_claim2`, `lemma54_even_forward`, `_high`, `_even`,
`_iff` all report `[propext, Classical.choice, Quot.sound]`. No `sorryAx`; no
`Lean.ofReduceBool`.

## Scope (what this does NOT cover)

This is the **abstract even-domain descent core** only.  It does **not**
formalise: Link A (`v ≤ g*_n` from the `|a-b| ≤ max(a,b)` induction — that is
`code/lean/link_a.lean`, separate), the composition
`g*_n ≤ 2ν₂+2 ⟹ v ≤ g*_n ⟹ success`, the reduction from real column dynamics
to the `(pattern, v)` model, or the supply side (`ν₂ ≥ c·n`).  So the full
Granville Lemma 5.4 chain is *not* yet kernel-checked end to end; this closes
the abstract descent core on the even domain.
