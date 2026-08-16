# Lean 4 formalisation — verification report

Date of check: this run. Command used for every file: `lean_check`.

## Status summary

| File | Compiles | `sorry` | Axioms | Status |
| --- | --- | --- | --- | --- |
| `ErdosGyarfas_Statement.lean` | yes | 1 (conjecture itself) | propext, sorryAx, Classical.choice, Quot.sound | stated, **not** proved (open conjecture) |
| `LemmaA_chord_deletion.lean` | yes | 1 (whole lemma) | propext, sorryAx, Classical.choice, Quot.sound | **stated, proof `sorry`** |
| `LemmaB_cycle_lengths_transfer.lean` | yes | 1 (whole lemma) | propext, sorryAx, Classical.choice, Quot.sound | **stated, proof `sorry`** |
| `LemmaB_path_plus_chord_is_cycle.lean` | yes | 0 | propext, Classical.choice, Quot.sound | **proved** (easy direction of Lemma B) |
| `LemmaB_cycle_splits_to_path.lean` | yes | 2 (both hard-direction lemmas) | propext, sorryAx, Classical.choice, Quot.sound | **stated, proofs `sorry`** |
| `Lemma_b_single.lean` | **no** | 1 (IsCycle part of `cycle_from_neighbor`) | (does not compile) | broken draft |
| `Lemma_b_single_fixed.lean` | **no** | 0 (but does not compile) | (does not compile) | newer draft, not yet compiling |
| `Lemma_b_single_neighbor.lean` | **no** | 2 (in `subpathPos_not_mem_start`) | (does not compile) | broken draft |
| `LongestPathLemma_b1.lean` | yes | 0 | propext, Classical.choice, Quot.sound | **proved** |
| `LongestPathLemma_b2.lean` | **no** | 1 (IsCycle part) | (does not compile) | broken draft |
| `LongestPathLemma_b2_fixed.lean` | **no** | 0 (but does not compile) | (does not compile) | newer draft, `where`-scoped `subpathPos_getVert` invisible; not finished |
| `Subpath.lean` | **no** | 0 (but does not compile) | (does not compile) | broken draft |
| `Subpath_positional.lean` | **no** | 0 (but does not compile) | (does not compile) | broken draft |
| `Test_subpath.lean` | yes | 0 | (no `#print axioms` line) | compiles, unverifiable |
| `Test_subpath2.lean` | yes | 0 | (no `#print axioms` line) | compiles, unverifiable |

`native_decide` and `admit` are used nowhere. Every remaining gap is a `sorry`.

## The two load-bearing lemmas of the adopted approach (edge-deletion-2adic-transfer)

The approach file (`research/approaches/edge-deletion-2adic-transfer.md`) rests on:

- **Lemma A** — every 2-connected finite simple graph with min-degree ≥ 3 has an
  edge `e = ab` such that `G − e` is 2-connected and `minDegree(G − e) ≥ 2`.
- **Lemma B** — `C(G) = C(G − e) ∪ {|P| + 1 : P a simple a–b path in G − e}`,
  where `e = ab`.

### Lemma A — formalised statement, proof NOT done

`LemmaA_chord_deletion.lean` states it with a `sorry`. The statement is:

```lean
theorem chord_deletion_lemma (G : SimpleGraph V) [Fintype V] [DecidableEq V]
    [DecidableRel G.Adj] (h₂ : IsTwoConnected G) (hδ : 3 ≤ G.minDegree) :
    ∃ a b : V, G.Adj a b ∧
      IsTwoConnected (G.deleteEdges {s(a, b)}) ∧
      2 ≤ (G.deleteEdges {s(a, b)}).minDegree
```

with `IsTwoConnected G := G.Connected ∧ ∀ v, (G.induce {v}ᶜ).Connected`.
The proof rests on Dirac's theorem (every minimally 2-connected graph has a vertex
of degree 2), which is not in Mathlib; **the proof is `sorry`**. This lemma is not
formally proved.

### Lemma B — one direction PROVED, the other stated with `sorry`

The full equality is stated (with `sorry`) in `LemmaB_cycle_lengths_transfer.lean`:

```lean
theorem cycle_lengths_transfer {G : SimpleGraph V} {a b : V} (hab : G.Adj a b) :
    CycleLengths G =
      CycleLengths (G.deleteEdges {s(a, b)}) ∪
        { n | ∃ P : (G.deleteEdges {s(a, b)}).Walk a b, P.IsPath ∧ n = P.length + 1 }
```

**The easy inclusion (path in G−e + chord e is a cycle of G) is PROVED** in
`LemmaB_path_plus_chord_is_cycle.lean`:

```lean
theorem cycle_lengths_transfer_subset {G : SimpleGraph V} {a b : V}
    (hab : G.Adj a b)
    (P : (G.deleteEdges {s(a, b)}).Walk a b) (hP : P.IsPath) :
    CycleLengths G (P.length + 1)
```

`lean_check` verdict: **verified: true**; axioms `[propext, Classical.choice, Quot.sound]`
— no `sorryAx`. Proof: map `P` up to `G` via `Walk.mapLe`, prepend the closing edge
`hab.symm`, apply `Walk.cons_isCycle_iff`; the chord is absent from `P.edges` because
every edge of a walk of `G − e` avoids `s(a,b)` (`deleteEdges_adj`), and
`s(b,a) = s(a,b)` (`Sym2.eq_swap`).

**The hard inclusion (a cycle of G through e splits into a simple a–b path of G−e)
is NOT proved.** It is stated with `sorry` in `LemmaB_cycle_splits_to_path.lean`:

```lean
theorem cycle_using_edge_splits_to_path {G : SimpleGraph V} {a b v : V}
    (hab : G.Adj a b) (c : G.Walk v v) (hc : c.IsCycle)
    (huse : s(a, b) ∈ c.edges) :
    ∃ P : (G.deleteEdges {s(a, b)}).Walk a b,
      P.IsPath ∧ P.length = c.length - 1 := by sorry

theorem cycle_lengths_transfer_subset_cycle {G : SimpleGraph V} {a b : V}
    (hab : G.Adj a b) {n : ℕ} (hn : CycleLengths G n) :
    CycleLengths (G.deleteEdges {s(a, b)}) n ∨
      ∃ P : (G.deleteEdges {s(a, b)}).Walk a b, P.IsPath ∧ n = P.length + 1 := by sorry
```

The proof plan for the hard direction exists and the Mathlib API supports it
(`Walk.rotate`, `Walk.cons_isCycle_iff`, `Walk.IsPath.takeUntil`/`dropUntil`,
`Walk.transfer`, `Sym2.eq_iff`), but it has not been completed. This is the 
precise remaining gap in Lemma B.

### Bottom line for the adopted approach

- Lemma A: **not formalised** (statement only, `sorry`).
- Lemma B: **half formalised** — the easy inclusion is proved (kernel-checked,
  no `sorry`); the hard inclusion (cycle through the chord splits into an a–b
  path) is stated with `sorry`.

The load-bearing pair is therefore **not yet fully machine-checked**: both lemmas
need their `sorry`s replaced by proofs before the approach rests on formalised
content.

## Which statement of the conjecture is formalised

`ErdosGyarfas_Statement.lean` formalises the conjecture as:

```lean
def IsPowerOfTwoLen (n : ℕ) : Prop := ∃ k : ℕ, 2 ≤ k ∧ n = 2 ^ k

def HasPowerOfTwoCycle (G : SimpleGraph V) : Prop :=
  ∃ v : V, ∃ c : G.Walk v v, c.IsCycle ∧ IsPowerOfTwoLen c.length

theorem erdos_gyarfas_conjecture (G : SimpleGraph V) [Fintype V]
    [DecidableRel G.Adj] (hδ : 3 ≤ G.minDegree) : HasPowerOfTwoCycle G := by sorry
```

Notes on the statement:
- cycle = `SimpleGraph.Walk v v` with `Walk.IsCycle` (simple cycle, i.e. closed
  trail whose support.tail is nodup);
- "power of two" means `2^k` with `k ≥ 2` (lengths 4, 8, 16, …), excluding the
  vacuous lengths 1 and 2;
- `minDegree ≥ 3` is Mathlib's `3 ≤ G.minDegree`.
- The theorem is **stated with `sorry`** and is NOT claimed proved — the conjecture
  is open. The statement elaborates and is the formal target.

## What is genuinely proved (kernel-checked, no sorry)

1. `LongestPathLemma_b1.lean` — `neighbor_of_longest_path_vertices_is_on_path`:
   every neighbour of the start vertex of a longest path lies on the path.
   Axioms: `[propext, Classical.choice, Quot.sound]`.
2. `LemmaB_path_plus_chord_is_cycle.lean` — `cycle_lengths_transfer_subset`:
   a simple a–b path in G − e closes with the chord e to a cycle of G of length
   |P| + 1. Axioms: `[propext, Classical.choice, Quot.sound]`.

## What is stated but not proved (sorry)

- `ErdosGyarfas_Statement.lean`: the conjecture itself (open).
- `LemmaA_chord_deletion.lean`: Lemma A (needs Dirac's theorem).
- `LemmaB_cycle_lengths_transfer.lean`: the full Lemma B equality.
- `LemmaB_cycle_splits_to_path.lean`: the hard inclusion of Lemma B (2 sorries).

## Files that do not compile

These are drafts that were superseded or never finished. Each is listed with the
first error from `lean_check`:

- `Lemma_b_single.lean` — `rw` failure on `subpathPos_getVert` inside
  `subpathPos_mem_is_getVert`, and a type mismatch in `cycle_from_neighbor`
  (`subpathPos p 0 i` has type `G.Walk (p.getVert 0) (p.getVert i)`, not
  `G.Walk u w`). Contains 1 sorry (the IsCycle part). **Note:** the informal claim with `1 ≤ i`
  is mathematically false (i = 1 gives the degenerate walk u–w–u); the correct
  hypothesis is `2 ≤ i`.
- `Lemma_b_single_fixed.lean` — a newer attempt with hypothesis `2 ≤ i`, does
  not compile: the `rw [← p.getVert_zero]` coercion does not reduce `sub` to
  `subpathPos`, so the subpath lemmas do not apply to `sub`. The `IsCycle` proof
  also has an error (`simp [hw.symm.toWalk]` on a walk type). Contains 0 sorries
  but no complete proof.
- `Lemma_b_single_neighbor.lean` — `dsimp` made no progress in
  `subpathPos_not_mem_start`; contains 2 sorries.
- `LongestPathLemma_b2.lean` — `rw` failure in `cycle_from_two_neighbors`
  (`Walk.append` pattern not found); the `IsCycle` goal is unsolved; 1 sorry.
- `LongestPathLemma_b2_fixed.lean` — newer attempt with hypothesis `1 ≤ ia`;
  does not compile: `subpathPos_getVert` (scoped with `where`) is unknown at its
  use site, `rw [Walk.append_assoc]` does not match the `cons`-form goal, and the
  length goal is left unsolved. Contains a detailed analysis comment showing the
  intended `isCycle_append` route; 0 sorries but no complete proof.
- `Subpath.lean` — `subpathPos_getVert` application error, `List.mem_tail` and
  `isPath_def` unknown, and the final goal unsolved in `subpathPos_not_mem_start`.
- `Subpath_positional.lean` — unknown identifier `subpathPos_getVert` (it was
  scoped with `where`, so the later use cannot see it); 0 sorries but does not
  compile.

The two `Test_subpath*.lean` files compile but have no `#print axioms` line, so
`lean_check` cannot verify what they rest on; they are scratch tests.

## Recommendation

To complete the formalisation of the two load-bearing lemmas:

1. **Lemma B hard direction** (`LemmaB_cycle_splits_to_path.lean`): prove that a
   cycle through `s(a,b)` splits into a path. The API exists; the remaining work
   is a careful `rotate`/`takeUntil`/`transfer` argument.
2. **Lemma A**: needs Dirac's theorem (minimally 2-connected ⇒ degree-2 vertex).
   This is a genuine theorem not in Mathlib; either add it as its own formalised
   lemma or keep Lemma A as a stated conditional.
