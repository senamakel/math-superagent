# Link A of Granville Lemma 5.4 — Lean 4 formalisation of the combinatorial core

Status: **formalised** (kernel-checked, sorry-free) — `code/lean/link_a.lean`.

## What Link A is

In the right-diagonal reduction of Granville Lemma 5.4 the orbit is

    x_0 = v,   x_{s+1} = |x_s - e_s|

(the `runAbs` trajectory, same convention as `code/lean/descent_lemma.lean`),
and `g*_n` is the record gap — a common upper bound for the starting value `v`
and every `eps_k`. Link A is the claim that the whole orbit never exceeds the
record:  `runAbs v el ≤ g*_n`.

The engine is the pointwise inequality `|a − b| ≤ max(a, b)`: each descent step
keeps the value at most the running max, so the orbit stays inside
`[0, max(v, max_s e_s)]`. The lower bound 0 is automatic for naturals, so Link A
reduces to the upper bound.

## What is proved here (sorry-free, kernel-checked)

`code/lean/link_a.lean`, `lean_check` verdict **compiled=true, verified=true,
sorry warnings: none**. Declarations:

- `dist_le_max (a b : Nat) : Nat.dist a b ≤ max a b` — the core induction
  step, for all naturals.
- `maxAll` / `maxAll_ge` — list maximum; every element ≤ its max.
- `run_le : ∀ el w M, w ≤ M → (∀ e ∈ el, e ≤ M) → runAbs w el ≤ M` — the
  generic orbit invariant: if the start and every pattern entry are ≤ M then
  the whole orbit is ≤ M. This is exactly Link A modulo the identification of
  `g*_n` as a common upper bound.
- `orbit_le_max : runAbs v el ≤ max v (maxAll el)` — the boundedness invariant
  with the maximal bound made explicit.

Axiom footprint (`#print axioms`):

- `dist_le_max`, `run_le`, `orbit_le_max`: `[propext, Classical.choice, Quot.sound]`
- `maxAll_ge`: `[propext]`

No `sorry`, no `sorryAx`, no `native_decide`. The geometric `g*_n` is **not**
constructed here: that step needs `Delta_k(q_n) = |Delta_{k-1}(q_n) − eps_k|`
with `eps_k = Delta_{k-1}(q_{n-1})` (claim `reduction-passage-exact`, verified
on 49,873,204 positions), and the definition of the record gap itself.

## What this joins, and what it does not

This file is self-contained (imports only `Mathlib.Data.Nat.Dist` +
`Mathlib.Tactic`), so it is kernel-checked in isolation. Cross-file import does
**not** work in this container (read-only root, no writable Lean project —
verified: `import descent_lemma` fails with "unknown module prefix"), so
`link_a.lean` deliberately redefines `runAbs` rather than importing
`descent_lemma.lean`. The two files agree on the `runAbs` convention.

Together `descent_lemma.lean` (the absorption/descent core — {0,2} absorbing,
`x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2` for even v) and `link_a.lean` (the `v ≤ g*_n` bound)
cover the two structural legs of Lemma 5.4's combinatorial heart. The
composition `g*_n ≤ 2ν₂+2 ⟹ v ≤ g*_n ⟹ success` would then close the loop; it is
not yet a single Lean theorem because the record gap `g*_n` and the
reduction-passage geometry entering it are not yet defined in Lean. That is the
precise piece still missing toward a full Lean Lemma 5.4, and it is a
definitional/geometric step, not a gap in `dist_le_max` or `run_le`, which are
themselves complete and kernel-checked.
