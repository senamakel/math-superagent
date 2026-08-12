# STATUS — `lean/erdos_gyarfas.lean`

Inspected and compiled this session. Findings below.

## (a) The formal statement as written

```lean
theorem erdos_gyarfas {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hmin : 3 ≤ G.minDegree) :
    ∃ (k : ℕ) (v : V) (p : G.Walk v v),
      p.IsCycle ∧ p.length = 2 ^ k ∧ 2 ≤ k := by
  sorry
```

In words: for every finite simple graph `G` (Mathlib `SimpleGraph V`) whose
`minDegree` is at least 3, there exist a natural `k`, a vertex `v`, and a
closed walk `p : G.Walk v v` such that `p` is a cycle (`p.IsCycle`), its
length (in edges) is exactly `2 ^ k`, and `2 ≤ k`.

## (b) Lemmas/proofs present vs `sorry`

There are **no lemmas and no proofs anywhere in the file.** The single theorem
`erdos_gyarfas` has an empty body containing one intentional `sorry`. This is
correct behaviour, not a gap: the conjecture is open, so the body is a
deliberate placeholder. The formal value of the file is the *statement*, which
elaborates. Nothing else (no auxiliary lemmas, no `#print axioms` directive)
is present.

## (c) `#print axioms`

The file itself does **not** contain a `#print axioms` directive; it ends
after the `by sorry`. I ran `#print axioms erdos_gyarfas` on a copy and got:

```
'erdos_gyarfas' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
```

- `propext`, `Classical.choice`, `Quot.sound` — the standard, kernel-checked
  axioms that every Mathlib proof (in fact every Lean proof) uses.
- `sorryAx` — present **because the body is `sorry`**. It stands in for the
  unproved conjecture.

**Suggestion:** add `#print axioms erdos_gyarfas` as the last line of the
file, so a future run can confirm with one command that the only
non-standard axiom is `sorryAx`. Once any part of the conjecture is proved,
`sorryAx` will drop out and the check becomes meaningful (a theorem depending
only on `propext`, `Classical.choice`, `Quot.sound` is kernel-proved).

## (d) Conventions — explicitly stated?

Yes. The theorem's conclusion is exactly `p.length = 2 ^ k ∧ 2 ≤ k`, so the
`2 ≤ k` clause (lengths 4, 8, 16, …) is part of the statement itself, not just
a prose comment. The header comment additionally spells out each convention
checked:
- `G.minDegree` is `0` on the empty vertex type, so `3 ≤ minDegree` rules the
  empty graph out and `∃ v` is inhabited (not vacuously true).
- `p.IsCycle` is Mathlib's predicate, which rules out length-0/1 walks, so any
  witness is a genuine cycle of length ≥ 3.
- `p.length` counts **edges**, matching the convention that a 4-cycle has
  length 4.
- `2 ^ k` is ℕ-valued exponentiation; `2 ≤ k` forces the exponent ≥ 2.

The comment also flags the intended divergence from the loose informal claim:
asking `2 ≤ k` makes the statement *stronger* than "a power of two" (which
would permit `2^0 = 1`), matching the run's formulation of the problem.

## (e) `#print axioms erdos_gyarfas` — appended and recompiled

`#print axioms erdos_gyarfas` is now the last line of the file. Recompiled:

```
$ cd /workspace && lean lean/erdos_gyarfas.lean
lean/erdos_gyarfas.lean:40:8: warning: declaration uses `sorry`
'erdos_gyarfas' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
```

Exit status 0. Exact axiom list: `[propext, sorryAx, Classical.choice, Quot.sound]`
— exactly the four reported before, the only non-standard one being
`sorryAx`, which correctly marks the open conjecture.

## (f) `lean/c4_lemma.lean` — a sorry-free proved lemma

New file `lean/c4_lemma.lean` carries and **proves** the contentful lemma:

```lean
theorem c4_gives_eg_conclusion {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (h : ∃ (v : V) (p : G.Walk v v), p.IsCycle ∧ p.length = 4) :
    ∃ (k : ℕ) (v : V) (p : G.Walk v v),
      p.IsCycle ∧ p.length = 2 ^ k ∧ 2 ≤ k := by
  rcases h with ⟨v, p, hpcycle, hplen⟩
  refine ⟨2, v, p, hpcycle, ?_, ?_⟩
  · rw [hplen]
    norm_num
  · norm_num

#print axioms c4_gives_eg_conclusion
```

This is the **"a counterexample must be C4-free"** direction: since `4 = 2²`
is itself a power of two, any graph containing a 4-cycle already satisfies the
EG conclusion, so a search for a counterexample may restrict to C4-free graphs
(the run's `nauty-geng -f` reduction). Proof shape: witness `k = 2`, then the
two arithmetic facts (`4 = 2^2` and `2 ≤ 2`) close with `norm_num`.

Imports: the four SimpleGraph modules plus `Mathlib.Tactic.NormNum` for the
arithmetic (`norm_num` is not pulled in automatically by the graph modules).
The proof uses only `rcases`, `refine`, `rw`, and `norm_num`.

### Compile + axioms

```
$ cd /workspace && lean lean/c4_lemma.lean
'c4_gives_eg_conclusion' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Exit status 0, **no `sorry` warning**. `#print axioms` shows exactly
`[propext, Classical.choice, Quot.sound]` — **no `sorryAx`** — so the lemma is
kernel-checked: the success test passes. Grep confirms the only occurrence of
`sorry` in the file is in a prose comment; no `sorry`/`admit`/`native_decide`/
`@[implemented_by]` is used as a tactic.

## Compile result (original file, before edits)

```
$ cd /workspace && lean lean/erdos_gyarfas.lean
lean/erdos_gyarfas.lean:40:8: warning: declaration uses `sorry`
```

Exit status 0. The file **elaborates**. The only diagnostic is the expected
`sorry` warning on line 40. All names resolve (`SimpleGraph`, `minDegree`,
`Walk`, `IsCycle`, `length`, `2 ^ k`), so the statement is well-typed against
Mathlib's API.

## Bottom line

- Statement elaborates: **yes**.
- Conventions (`k ≥ 2`, edge-length count) stated: **yes**, both in the
  statement and in prose.
- Proofs present: `erdos_gyarfas` is an intentional `sorry` (open conjecture);
  `c4_gives_eg_conclusion` (in `lean/c4_lemma.lean`) is **proved, sorry-free**.
- `#print axioms erdos_gyarfas`: `[propext, sorryAx, Classical.choice, Quot.sound]`
  — `sorryAx` the only non-standard axiom, correctly marking the open conjecture.
- `#print axioms c4_gives_eg_conclusion`: `[propext, Classical.choice, Quot.sound]`
  — **no `sorryAx`**; the lemma is kernel-checked.
