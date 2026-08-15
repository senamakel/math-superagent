# Lemma 5.4 core — descent/absorption lemma, EVEN-UNIT form, Lean-formalised

```claim
id: lemma54-descent-lean-formalised-even
statement: Let el : List Nat have every entry in {0,2} (hall), countTwo el = nu2, and orbit runAbs with x_0 = v, x_{s+1} = |x_s - e_s|. For Even v: (a) runAbs v el in {0,2} iff v <= 2*nu2+2; (b) v > 2*nu2+2 -> runAbs v el = v-2*nu2 and 4 <= v-2*nu2. Formalised sorry-free in Lean 4.
hypotheses: el entries in {0,2}; v even (load-bearing — for odd v the biconditional is false: machine oracle found 192 odd-v counterexamples to (a)).
holds-here: yes
status: formalised
formalisation: code/lean/descent_lemma.lean
bearing: the combinatorial core of Granville Lemma 5.4 in original even units (v, nu2, c in {0,2}), the demand-to-success leg of Route B.
answers: lemma54-descent-proof-repaired (halved-only formal record); this is the even-unit biconditional the task and oracle require.
anchor: research/notes/lemma54-descent-lean-formalised-even.md
lean_check: compiled true, verified true, sorry warnings none; axioms only {propext, Classical.choice, Quot.sound} — no sorryAx, no Lean.ofReduceBool.
```

## The theorem (even units — this run's file)

Pattern `el : List Nat` with every entry in {0,2} (hypothesis `∀ e ∈ el,
`e = 0 ∨ e = 2`), starting value `v : Nat`.  Orbit

```
x_0 = v,   x_{s+1} = |x_s - e_s|
```

`countTwo el` = ν₂ = #{s : e_s = 2}.  The trajectory is parity-preserving
when `v` is even (lemma `dist_even_even`: difference of two evens is even).
The three machine-checked claims, all for `Even v`:

```
(a)  x_L ∈ {0,2}  ⟺  v ≤ 2·ν₂ + 2
(b)  v > 2·ν₂ + 2  ⟹  x_L = v - 2·ν₂   and   x_L ≥ 4
(3)  {0,2} is absorbing under |·-e| for e ∈ {0,2}
```

Statement-lean correspondence (theorem names in code/lean/descent_lemma.lean):

- `absorbing`, `run_absorb`            — claim (3), absorption along the whole pattern.
- `run_inv_even`                       — engine invariant: the value is either exactly
  `v - 2·(ν₂ so far)` or inside {0,2}.  Needs `Even v` (uses dist_even_even).
- `run_high_even`                      — high branch claim (b): if v > 2ν₂+2 no value
  ever drops below 2, so each c=2 step subtracts exactly 2 and each c=0 fixes,
  giving `x_L = v - 2ν₂`.  (First-class, not the false 'v-2ν₂ always' algebra,
  which is false on bounce trajectories where δ=0,ε=2 gives δ=2, a +2.)
- `descent_backward`                   — claim (a) backward leg: v ≤ 2ν₂+2 ∧ Even v
  ⟹ x_L ∈ {0,2}   (via run_inv_even + even_le_two).
- `descent_high_value`                 — claim (b): the value equation AND the lower
  bound x_L ≥ 4, both.
- `descent_biconditional`              — claim (a) in full: Even v ⟹
  (x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2).  Backward via descent_backward; forward is the
  contrapositive of the high branch (if v > 2ν₂+2 then x_L = v−2ν₂ ≥ 4 ∉ {0,2}).

## Proof shape (the corrected case split)

`{0,2}` is absorbing: |0−0|=0, |0−2|=2, |2−0|=2, |2−2|=0 (claim (3)).

**Engine invariant**, `run_inv_even`: at each scan position the value is
either the exact line `v − 2·(ν₂ so far)` or it has already dropped into
{0,2}.  Induct on the pattern; at a c=0 step nothing changes (value fixed,
ν₂ fixed); at a c=2 step |v−2| is even and the invariant recurses.  If the
old value is already in {0,2}, absorption keeps it there.  Note a c=2 step
acts as |0−2|=2 or |2−2|=0 — a *bounce* when the old value is small, which
is exactly why the naive "subtract 2" fails and why the invariant instead
branches into the absorbed {0,2} state.

**Backward leg** (descent_backward): if v ≤ 2ν₂+2 then on the exact-line
alternative `v − 2ν₂ ≤ 2`, and it is even, so by `even_le_two` it is 0 or 2;
the other alternative is already {0,2}.

**High branch** (run_high_even): if v > 2ν₂+2 then v ≥ 2ν₂+3, and on the
exact line the value is `v − 2·(ν₂ so far) ≥ v − 2ν₂ ≥ 3 ≥ 2` throughout, so
no bounce ever occurs and each c=2 step is |x−2| = x−2, each c=0 step fixes.
This gives the exact value `v − 2ν₂`; with v even it is ≥ 4
(descent_high_value).  This non-vacuous branch is the tightness of the budget
`2ν₂+2`.

**Biconditional** forward: contrapositive of the high branch — if
v > 2ν₂+2 then x_L = v−2ν₂ ≥ 4, impossible for x_L ∈ {0,2}.

## Exchange with the halved form

The halved {0,1}-form (w, ν₁, claim1/claim2) is the same lemma under
v=2w, ν₂=ν₁, x=2d.  The even-unit file proves the theorem directly with the
even-parity hypothesis made explicit, which is the shape the task and the
oracle require.  Both are Lean-checked sorry-free; see the even-unit oracle
(Section below) noting that odd v genuinely breaks (a) — the `Even v`
hypothesis is not decoration.

## Oracle check (this run)

Exhaustive oracle over patterns c ∈ {0,2}^L, L ≤ 10, all even v in a range:
**0 failures** of claim (a) [even v], **0 failures** of claim (b).  For odd v,
claim (a) fails 192 times (e.g. the empty pattern with v=1 gives x_L=1 ∉ {0,2}
but v=1 ≤ 2·0+2=2) — confirming `Even v` is load-bearing, not cosmetic.  This
matches the prior halved verify (12,582,900 pairs, 0 violations).

## Axiom footprint (verbatim from lean_check)

- `absorbing` — no axioms
- `run_absorb`, `run_inv_even`, `run_high_even`, `descent_backward`,
  `descent_high_value`, `descent_biconditional` — `[propext,
  Classical.choice, Quot.sound]`
- `even_le_two` — `[propext, Quot.sound]`

No `sorry`, no `sorryAx`, no `Lean.ofReduceBool`.  `decide` is used only on
closed finite goals (the absorbing case table), which the kernel checks.
