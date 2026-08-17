# G-n3-zero — Lean formalisation of the n₃ = 0 branch

Node `n3-dichotomy/G-n3-zero` from research/backward/n3-dichotomy.md.
Formalised at code/lean/n3_dichotomy_G_n3_zero.lean (lean_check `verified`,
no sorries, no `native_decide`).

## The statement, and a correction to the earlier formalisation

The node says "no pair of *disjoint* triangles is joined by exactly 2 edges".
The earlier `CondStar` in makhnev99_shorter_proof_integrality.lean quantified
over *all* distinct triangle pairs. Two triangles sharing a vertex are joined
by ≥ 4 cross edges, so `2 ≤ edgeCount` holds and the conclusion forced
`= 3`, making `CondStar` unsatisfiable (hence vacuously true) for any graph
with intersecting triangles — which every candidate graph has. That old
rendering was **vacuously true**, so it carried no content.

This file restates the condition honestly:

```lean
def n3_zero G :=
  ∀ T1 T2, T1.card = 3 → T2.card = 3 →
    G.IsClique T1 → G.IsClique T2 → Disjoint T1 T2 →
      edgeCountBetween G T1 T2 ≠ 2
```

For disjoint T1,T2 each undirected cross edge lies in `T1.product T2` exactly
once, so "joined by exactly 2 edges" is `edgeCountBetween = 2`; `n3_zero`
says no such pair exists — this is Makhnev's (∗) where it bites.

## What each binder carries

The dichotomy theorem:

```lean
theorem no_srg_99_14_1_2_n3_zero :
  ¬ ∃ V (iv : Fintype V) (G : SimpleGraph V) (da : DecidableRel G.Adj),
      G.IsSRGWith 99 14 1 2 ∧ n3_zero G
```

- `G.IsSRGWith 99 14 1 2` — the srg hypothesis (binder/type-level data).
- `n3_zero G` — Makhnev's condition (∗) = n₃ = 0 (a *hypothesis*, established
  nowhere — it is the branch assumption being discharged).
- The whole existence statement is negated, so the kernel shows: *if* such a
  graph with n₃=0 existed, *then* contradiction.

The proof rests on two `Cited` axioms, so the theorem is **conditional**, not
formalised:

1. `Cited.srg_multiplicity_integrality` — Bose–Mesner eigenvalue-multiplicity
   integrality of an SRG: an srg(33,12,1,6) forces 7 ∣ (2k+(v−1)(λ−μ)) = −136.
2. `Cited.makhnev_lemmas_6_9` — Makhnev 1988 Lemmas 6–9: a putative
   srg(99,14,1,2) with (∗) forces the subobject Λ₀ = srg(33,12,1,6).

The **arithmetic kernel** — discriminant 49 = 7², numerator −136, 7 ∤ 136 —
is proved outright: `not_seven_dvd_33_12_1_6_numerator` depends only on
`propext` and `Quot.sound` (lean_check reports no cited axioms, no sorries).
That is the `formalised` part.

## #print axioms (from lean_check)

- `N3Dichotomy.not_seven_dvd_33_12_1_6_numerator`: [propext, Quot.sound] → formalised
- `N3Dichotomy.srg33_12_1_6_infeasible`: [propext, Classical.choice, Quot.sound,
  Cited.srg_multiplicity_integrality] → conditional
- `N3Dichotomy.no_srg_99_14_1_2_n3_zero`: [propext, Classical.choice, Quot.sound,
  Cited.makhnev_lemmas_6_9, Cited.srg_multiplicity_integrality] → conditional

Note: lean_check prints `cited axioms: none` at the top of its block, but its
`#print axioms` output names the two Cited axioms on the two conditional
theorems. The conditional theorems are `conditional`; only the arithmetic
kernel is `formalised`.

## Relationship to the already-filed claim

`makhnev99-shorter-proof-integrality` already carried this node as
`conditional`. This file is a fresh, kernel-verified rendering with the
statement corrected to the disjoint-triangle reading, so the claim below only
re-verifies the node rather than loosening its status.

```claim
id: n3-dichotomy-G-n3-zero-lean
statement: No srg(99,14,1,2) has n3 = 0 (Makhnev's condition (*) restricted to
  disjoint triangle pairs). Kernel-verified at code/lean/n3_dichotomy_G_n3_zero.lean:
  theorem no_srg_99_14_1_2_n3_zero. The arithmetic kernel (7 does not divide
  -136 = 2k+(v-1)(lam-mu) for (33,12,1,6)) is formalised (propext/Quot.sound
  only). The theorem-level claim is conditional on Cited.srg_multiplicity_integrality
  (Bose-Mesner multiplicity integrality) and Cited.makhnev_lemmas_6_9 (Makhnev's
  forced-subobject chain). Corrects the earlier CondStar bug (quantified over all
  distinct triangles, vacuously true).
hypotheses: a putative srg(99,14,1,2); n3 = 0 (branch assumption); the two Cited
  axioms. The n3 = 0 hypothesis is NOT established by the run — it is the branch
  being discharged.
holds-here: yes (node G-n3-zero; kernel check passed lean_check, no sorries).
status: conditional (rests on the two Cited axioms), with the arithmetic kernel
  formalised.
formalisation: code/lean/n3_dichotomy_G_n3_zero.lean
bearing: kernel-verifies the n3 = 0 branch of the dichotomy; the node is
  discharged as conditional, and nothing above it is undermined (the conditional
  is strictly weaker than a formalised theorem but the arithmetic kernel is solid).
```

## Controls / no local claim of nonexistence

Nothing here asserts srg(99,14,1,2) does not exist. Both control graphs
rook(3) and BvLS(243) have n₃ = 0 (and μ = 2 ≤ 3), so they satisfy the same
condition — consistent with the conditional, which only fires at the 99
parameter set via the k=14-specific 60/20/33 count chain. The controls thus do
not refute it and are not refuted by it.
