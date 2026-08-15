# Granville Lemma 5.4 — composition leg (Link A + budget → success) formalised

This note records the kernel-checked formalisation of the two remaining legs of
Granville Lemma 5.4 that the run asked to close: **Link A** (the `v ≤ g*_n`
bound via the `|a−b| ≤ max(a,b)` induction) and **the composition**
(`g*_n ≤ 2ν₂+2` & `v ≤ g*_n` ⟹ `δ_L ∈ {0,2}`).

## Status

`id: lemma54-composition-lean-formalised`
`status: formalised`
`holds-here: yes`
`bearing:` closes the two legs between the already-formalised abstract descent
core (`descent-lemma-halved-formalised`) and the full even-domain Lemma 5.4
success statement (`lemma54-re-derived-proof`). Together with
`code/lean/lemma54_even_domain.lean` (the even-domain theorem via the halving
identity, already `formalised`-grade sorry-free) the full nondimensional chain
is now kernel-checked; the reduction passage and the supply side remain outside
Lean, as documented.

## Files

- `code/lean/link_a.lean` — Link A combinatorial core, sorry-free, already
  present and passing. `orbit_le_max` : `runAbs v el ≤ max v (maxAll el)`;
  engine `dist_le_max` (`|a−b| ≤ max(a,b)`), plus `maxAll_ge`, `run_le`.
  `lean_check` (this run): compiled=true, verified=true, no `sorry`; axioms all
  within `propext`/`Classical.choice`/`Quot.sound`.
- `code/lean/lemma54_even_domain.lean` — even-domain descent via halving,
  sorry-free, already present and passing (`lemma54_even_forward`,
  `lemma54_even_high`, `lemma54_even`, `lemma54_even_iff`).
- `code/lean/lemma54_composition.lean` — **the composition leg, this run.** A
  single self-contained sorry-free file (the container builds no olean files,
  so a theorem cannot import the others; the two legs are re-derived inline and
  named). It proves:
  - `orbit_le_max` (Link A): `runAbs v el ≤ max v (maxAll el)`.
  - `descent_backward` (descent core, even-unit): `Even v & v ≤ 2·ν₂+2 ⟹
    runAbs v el ∈ {0,2}`.
  - `lemma54_composition`: `Even v & v ≤ g & g ≤ 2·ν₂+2 ⟹
    runAbs v el ∈ {0,2}` (the transitivity composition, `g = g*_n` a free
    parameter).
  - `lemma54_composition_via_max`: `max v (maxAll el) ≤ 2·ν₂+2 ⟹
    runAbs v el ∈ {0,2}` (the record-gap form with `g*_n = max v (maxAll el)`).
  - `lemma54_full`: the maximal reading bundling Link A and the budget.
  `lean_check`: compiled=true, verified=true, zero `sorryAx`; every theorem's
  `#print axioms` is within `propext`/`Classical.choice`/`Quot.sound`.
  Capture: `code/out/lemma54_composition.captured.txt`.

## Non-vacuity / faithfulness check (independent route)

`code/lemma54_composition_oracle.py` (exact integers, independent Python route
against the Lean proof) over all `{0,2}^L` patterns L=0..8 and all even
`v ∈ [0, 2L+8)`:

- `composition_via_max`: checked 2815 (pattern,v) pairs with the budget premise
  in force, 0 violations;
- transitivity composition: checked 2815, 0 violations;
- `orbit_le_max` (Link A orbit bound): checked 5630, 0 violations.

So each Lean statement is non-vacuously true and faithfully captures the
informal `(pattern, v)` claim it names. This is verification, not the proof —
the proof is the kernel check.

## Axiom footprint (kernel-checked, this run)

Representative:

```
lemma54_composition       [propext, Classical.choice, Quot.sound]
lemma54_composition_via_max [propext, Classical.choice, Quot.sound]
lemma54_full              [propext, Classical.choice, Quot.sound]
orbit_le_max              [propext, Classical.choice, Quot.sound]
descent_backward          [propext, Classical.choice, Quot.sound]
```

No `sorryAx`, no `Lean.ofReduceBool`/`native_decide` anywhere. Every theorem in
the file carries an in-file `#print axioms` (a condition of the `lean_check`
verdict passing).

```claim
id: lemma54-composition-lean-formalised
statement: The composition leg of Granville Lemma 5.4 is kernel-checked in Lean 4, sorry-free. With el : List Nat a {0,2}-pattern (∀ e ∈ el, e = 0 ∨ e = 2), ν₂ = countTwo el, and the descent orbit runAbs v el (x_0 = v, x_{s+1} = |x_s - e_s|), Link A (orbit_le_max: runAbs v el ≤ max v (maxAll el), from the |a-b| ≤ max(a,b) induction) and the composition are proved: Even v & v ≤ g & g ≤ 2ν₂+2 ⟹ runAbs v el ∈ {0,2} (lemma54_composition), and max v (maxAll el) ≤ 2ν₂+2 ⟹ runAbs v el ∈ {0,2} (lemma54_composition_via_max). Every theorem's #print axioms is within propext/Classical.choice/Quot.sound; zero sorryAx; no native_decide. Statements NOT weakened.
hypotheses: el : List Nat with ∀ e ∈ el, e = 0 ∨ e = 2; v even (hypothesis of the descent core). The record-gap identification g*_n = max v (maxAll el) and the reduction-passage identity Delta_k(q_n) = |Delta_{k-1}(q_n) - eps_k| are OUTSIDE this file (they need the triangular array); here g is a free parameter and the nondimensional algebra from Link A + budget to success is what is proved.
holds-here: yes (real prime right-diagonals are even-valued; the {0,2} cycle is the pattern)
status: formalised
formalisation: code/lean/lemma54_composition.lean
anchor: code/lean/link_a.lean, code/lean/lemma54_even_domain.lean, code/lean/lemma54_composition.lean (lean_check), code/out/lemma54_composition.captured.txt, code/lemma54_composition_oracle.py
bearing: With descent-lemma-halved-formalised (abstract core) and lemma54_even_domain.lean (even-domain theorem via halving), this closes the two legs between the abstract core and the full even-domain Lemma 5.4 success statement, as the run's formalisation plan (TASKS.do-next: formalise-link-a / formalise-the-composition) required. It does NOT upgrade lemma54-re-derived-proof to proved beyond what the kernel gives: the reduction passage (reduction-passage-exact, currently status: checked) and the supply side ν₂(q_{n-1}) > n^β remain outside Lean, and the record-gap construction from the triangle is left to the reduction.
```
