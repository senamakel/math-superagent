# Thread: pair-labeling 84-vertex reduction (gated)

```thread
id: thread-pair-labeling-84
question: Is the pair-labeling reduction — fix vertex 0, N(0)=7K2, the 84
  distance-2 vertices biject to the 84 non-matching pairs of the 14-set, and
  the entire remaining freedom of srg(99,14,1,2) is a 12-regular graph H on
  these pairs with mu=2/lambda=1 as pair-adjacency rules — a live 99-specific
  handle, or is it parameter-determined and refuted on arrival because the same
  reduction is over-determined at the existing controls 9 and 243 too?
status: open
rests-on: c5, integrality-five-members
blocked-by: gate-clique-complex-homology, incidence-budget-ledger-controls
next: (directive 40, gated) run the pair-labeling reduction on rook(3) FIRST —
  fix a vertex, N(0)=2K2, four outer pair-vertices, H 1-regular on 4, reproduce
  the actual rook graph through code/lib.srg.is_srg — then bvls_graph (N(0)=11K2,
  220 outer pair-vertices, H 20-regular, reproduce the actual BvLS outer graph).
  Then decide whether pair-labeling PLUS the interlacing eigenvalue counts
  over-determine H at 99 in a way that is ALSO over-determined at 9 and 243 —
  where a graph exists. If the over-determination is shared, the approach is
  refuted on arrival like the eigenvalue routes. NAME which quantity differs at
  a=7 (sqrt(4k-7)) or say explicitly that it does not. Do NOT start a 99 search
  on H before both controls have been through the same reduction. Basis:
  code/out/research_pair_label_gate.py (on disk, no capture yet).
```

## The gate the directive requires

The approach `research/approaches/pair-labeling-84-vertex.md` is already
adopted and names this gate as its first-step, so the directive 40 confirms
rather than widens it. The reduction is parameter-determined and applies
verbatim to both controls, so the controls must be run through it first: the
rook graph (N(0)=2K2, H 1-regular on 4 outer pairs) and BvLS (N(0)=11K2,
H 20-regular on 220 outer pairs). Interlacing on an induced subconstituent is
not automatically control-safe just because whole-spectrum interlacing was
refuted (the interlacing-84-vertex-rigidity approach records exactly that
caveat), so the over-determination test must be run at 9 and 243, not assumed.
A shared over-determination is not an obstruction; only a quantity that differs
at a=7 would make the line live.
