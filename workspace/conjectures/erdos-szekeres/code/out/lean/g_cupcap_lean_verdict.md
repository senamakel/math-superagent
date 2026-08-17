# lean_check verdict — code/lean/extremal_split_stability_G_cupcap.lean

Node: `extremal-split-stability/G-cupcap` (ES 1935 cup–cap characterization of
convex position). This node is **discharged** in the statement graph
(g-cupcap-verified: 624 sets / 1220 cases, 0 mismatch) and is classical
literature, so the artifact is a decomposition, not a fresh proof.

## lean_check output (final)

```
file: code/lean/extremal_split_stability_G_cupcap.lean
compiled: true
outcome: failed            <- only because 1 sorry remains (the (⇒) leaf)
sorry warnings:
  .../extremal_split_stability_G_cupcap.lean:189:8: declaration uses `sorry`
#print axioms:
  'union_card_shared_two' depends on axioms: [propext, Classical.choice, Quot.sound]
  'cupcap_gives_convex'    depends on axioms: [propext, Classical.choice, Quot.sound]
  'g_cupcap'               depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
```

## What is genuinely proved (kernel, no sorryAx)

- `union_card_shared_two`: `C.card = k` ∧ `D.card = n+2-k` ∧ `(C∩D).card = 2`
  ⟹ `(C∪D).card = n`. The arithmetic core of "C ∪ D is exactly n points".
- `cupcap_gives_convex` — the **(⇐) direction** of the node: a k-cup C and
  (n+2−k)-cap D with shared x-extremes and convex union give an n-point convex
  subset (namely C ∪ D). Proved over the abstract predicates
  `convexPos/isCup/isCap/sameExtremes` and the single interface law
  `hSharedTwo : sameExtremes C D → (C∩D).card = 2`.

## What is open (one sorry)

- `convex_gives_cupcap` — the **(⇒) direction**: a convex n-polygon decomposes
  into an upper cap and a lower cup sharing its two x-extreme vertices. This is
  the single genuine gap, a pure Lean-formalisation task (the mathematics is
  established: classical ES 1935, computationally verified).
- `g_cupcap` (the combining iff) is kernel-checked in shape — `constructor`
  over the (⇐) proof and the (⇒) leaf — and carries `sorryAx` only through its
  (⇒) arm.

## Fenced gap blocks carried in the file

- `id: G-cupcap/convex-gives-cupcap` — status gapped; next: formalise the
  upper/lower x-monotone boundary chains of a convex n-polygon (upper chain a
  cap, lower a cup, covering all n vertices, meeting exactly in the two x-extreme
  vertices).
- `id: G-cupcap/hshared-two` — status gapped; next: define `sameExtremes`
  concretely (leftmost/rightmost-by-x equal, C∩D exactly those two elements) and
  derive |C∩D|=2.

NOT formalised (correct — the (⇒) leaf is a declared sorry). The run may treat
the (⇐) direction as kernel-checked and the full iff as established-by-source +
computed, with the formal (⇒) chain-decomposition still to be written in Lean.
