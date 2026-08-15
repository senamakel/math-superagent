# Lemma 5.4 composition leg — already kernel-checked; the literal "clean composition lemma" is refuted

## Headline

The task's two ledger rows (`formalise-link-a-v-g-n` and
`formalise-the-composition`) were **already closed on disk by a prior
session**, and both files pass `lean_check` here (re-verified this run).  The
composition leg is a **kernel-checked `status: formalised`** artefact, not an
open target.

What is genuinely NOT a theorem is the *literal* generalisation the task
proposed as the minimal fallback:

```
runAbs w el ∈ {0,2}   given   w ≤ 2·ν₁ + 2     (el a halved {0,1} pattern, ν₁ = countOnes el)
```

That statement is **false**.  This run refuted it by brute force and then
formalised the refutation in Lean.  The deliverable below is therefore: (1) the
confirmation that the real composition already exists and is kernel-checked,
(2) the located-error note naming precisely why the minimal proposal fails and
what the correct statement is.

## 1. The composition leg is already formalised and kernel-checked

Three self-contained files (cross-file import is impossible in this container,
so each redefines `runAbs`/`countTwo`; parity is machine-guarded by
`code/lean/link_a_drift_guard.py`):

- **`code/lean/link_a.lean`** — verdict: `compiled=true, verified=true, sorry
  warnings none`.
  - `dist_le_max (a b) : Nat.dist a b ≤ max a b` — the `|a-b| ≤ max(a,b)`
    induction kernel.
  - `orbit_le_max : runAbs v el ≤ max v (maxAll el)` — the **Link A** bound:
    the whole orbit is ≤ the record gap `g*_n = max v (maxAll el)`.
  - `link_a_composition` / `_via_max` / `_full` — the transitivity
    `v ≤ g*_n ≤ 2·ν₂+2` then `descent_backward` ⟹ `runAbs v el ∈ {0,2}`.
    (g*_n free in `link_a_composition`, concrete `max v (maxAll el)` form in
    `_via_max`.)
- **`code/lean/lemma54_composition.lean`** — same content under the
  `lemma54_composition` / `_via_max` / `_full` names; verdict
  `compiled=true, verified=true, sorry warnings none`.
- **`code/lean/lemma54_even_domain.lean`** — `lemma54_even_forward` : the clean
  even-domain composition from the halved core.  With `el` a **{0,2}** pattern,
  `countTwo el = ν₂`, `v` even, and `v ≤ 2·ν₂ + 2`:
  `runAbs v el ∈ {0,2}`.  This is the *correct* "generalise descent_claim1 to
  {0,2}" statement.  Verdict `compiled=true, verified=true, sorry warnings
  none`.

Axiom footprint (all three): every theorem's axioms are within
`propext / Classical.choice / Quot.sound` — nothing beyond.  No `sorry`, no
`sorryAx`, no `native_decide` anywhere.

So the phrase in the task brief ("link_a.lean proved only the trivial kernel… the load-bearing geometric leg is NOT yet a Lean theorem") is **stale**: the
`g*_n`-parameterised composition *is* now a Lean theorem whose geometric
identification (`g*_n` = the right-diagonal record gap, an object of the
triangular array) is the only part that lives outside the nondimensional
algebra, exactly as the prior note `research/notes/lemma54-link-A-lean.md`
records.

## 2. The literal "clean composition lemma" is FALSE — located error

Proposed (this run's task text): *"runAbs w el in {0,2} given w ≤ 2·ν₁+2 with
the halved {0,1} pattern el (generalise descent_claim1)."*

This is a **domain confusion**.  `descent_claim1` (halved core, `{0,1}`
pattern) concludes `runAbs w el ∈ {0,1}`, not `{0,2}`.  Putting the budget
`2·ν₁+2` in front of it and demanding a `{0,2}` outcome is not a
generalisation; it asks something false.

**Counterexample** (brute force, L≤6, w≤12): `el = [0]`, `w = 1`.

- `el` is a valid `{0,1}` pattern: `0 = 0 ∨ 0 = 1`.
- `ν₁ = countOnes [0] = 0`, so the budget bound is `w = 1 ≤ 2·0 + 2 = 2`.  ✓
- `runAbs 1 [0] = |1−0| = 1`, and `1 ∉ {0,2}`.  ✗

The proposal is refuted even at the very first pattern of length 1.  The full
brute force found many more: `el=[1],w=0` (ν₁=1, budget 4, orbit 1∉{0,2});
`el=[1],w=2`; `el=[1],w=4`→3; `el=[0,0],w=1`; `el=[0,1],w=0`; `el=[0,1],w=2`;
`el=[0,0,0],w=1`.  The pattern is that any odd start, or any start large enough
to skip past 2, escapes `{0,2}`; the halved medium has no parity ceiling.

**Correct statement.**  A `{0,2}`-valued orbit requires the **even {0,2}
pattern** (so every intermediate value stays even), which is exactly
`lemma54_even_forward`.  The halved core's correct composition is
`descent_claim1` itself: `w ≤ ν₁+1 ⟹ runAbs w el ∈ {0,1}`.  There is no
`2·ν₁+2` budget for a `{0,2}` conclusion in the halved domain.

## 3. The formalised refutation (new Lean artefact)

`code/lean/lemma54_composition_halved_refut.lean` — self-contained, sorry-free,
verdict `compiled=true, verified=true`:

- `runAbs` / `countOnes` redefined.
- `budget_holds : 1 ≤ 2 * countOnes [0] + 2`
- `runAbs_value : runAbs 1 [0] = 1`
- `one_not_in : ¬ (1 = 0 ∨ 1 = 2)`
- `halved_composition_refuted : runAbs 1 [0] = 1 ∧ ¬ (runAbs 1 [0] = 0 ∨ runAbs 1 [0] = 2)`
- `halved_composition_not_a_theorem : ∃ el w, (valid {0,1} pattern) ∧ w ≤ 2·ν₁+2 ∧ ¬ (runAbs w el ∈ {0,2})`

Axioms: only `propext / Classical.choice / Quot.sound`.  This is a **refuted
statement recorded so a later attempt does not walk into it** — it is not and
must not be filed as a `formalised` positive claim.

## 4. What remains genuinely open (honest scope)

The composition leg of the *nondimensional algebra* is closed.  What is not yet
a single Lean theorem is the **geometric identification** that `g*_n` (the
`max v (maxAll el)` used here) equals the *right-diagonal record gap* of the
real triangular array — the "reduction passage" `δ_k(q_n) =
|δ_{k−1}(q_n) − δ_{k−1}(q_{n−1})|` of `research/notes/reduction-passage-exact.md`
(proved there, machine-checked, but not Lean).  That is a definitional step
into the array, not a gap in `orbit_le_max` or in `lemma54_composition`, both
of which are complete.  The supply side (ν₂ ≥ c·n) remains the open
mathematical content, per GOAL.md.

```claim
id: lemma54-composition-halved-literal-refuted
statement: The literal halved-domain composition "runAbs w el ∈ {0,2} given w ≤ 2·ν₁+2 with el : List Nat a {0,1} pattern and ν₁ = countOnes el" is FALSE. Counterexample el=[0], w=1: ν₁=0, 1 ≤ 2·0+2, yet runAbs 1 [0]=1 ∉ {0,2}. The {0,2}-valued orbit needs the EVEN {0,2} pattern with countTwo and an even start, i.e. lemma54_even_forward, not the halved core. This records a located error (domain confusion) so it is not re-proposed.
hypotheses: el a {0,1} pattern (∀e∈el, e=0∨e=1); w : Nat; ν₁ = #{e=1}; LiteralLemmaBudget := w ≤ 2·ν₁+2
holds-here: yes (brute force L≤6 w≤12; Lean witness)
status: formalised (as a REFUTATION — the artefact proves the statement false)
formalisation: code/lean/lemma54_composition_halved_refut.lean
anchor: code/lean/lemma54_composition_halved_refut.lean
bearing: prevents a later session from treating the proposed minimal formalisation as a real generalisation; steers {0,2}-composition to the even domain (lemma54_even_forward) which is already kernel-checked.
```

## 5. Summary against the task's asks

| Ask | Status |
| --- | --- |
| `formalise-link-a-v-g-n` (v ≤ g*_n, |a−b|≤max induction) | **already formalised** `link_a.lean` / `lemma54_composition.lean`: `dist_le_max`, `run_le`, `orbit_le_max`, all kernel-checked |
| `formalise-the-composition` (g*_n ≤ 2ν₂+2 & v ≤ g*_n ⟹ success) | **already formalised** `link_a_composition(_via_max/_full)` / `lemma54_composition(_via_max/_full)`, kernel-checked |
| even-domain composition from `descent_claim1` | **already formalised** `lemma54_even_forward` in `lemma54_even_domain.lean`, kernel-checked |
| literal halved "clean composition lemma" (proposed minimal) | **REFUTED** — `lemma54_composition_halved_refut.lean`, kernel-checked as a refutation |

Per-file `lean_check` verdicts and full `#print axioms` lists are reproduced in
this run's tool history and in `code/out/lean/*.lean.json`; every file reports
only `propext / Classical.choice / Quot.sound`.
