# Forced-Structure Reduction 2026 — claim block

Source: https://arxiv.org/html/2608.11211v1, "A Forced-Structure Reduction and
Verifiable Bounds for Conway's 99-Graph" (CAISc 2026 preprint by an autonomous
AI research agent; NOT peer-reviewed). Full text in library at
`research/sources/forced-structure-reduction-conway99.full.md`; summary at
`research/summaries/forced-structure-reduction-conway99.md`.

```claim
id: forced-structure-reduction-conway99
statement: An independent (preprint, AI-agent) treatment confirms and extends
  the forced-structure reduction to the outer graph. For any srg(v,k,1,2) fix a
  vertex 0 with N(0) a perfect matching (7K2); μ=2 forces every outer vertex to
  have exactly two neighbours in N(0) and outer vertices to be in bijection
  with the non-matched pairs of N(0), so inner-outer adjacency is fully forced
  and the only unknown is the outer-outer graph, (k-2)-regular on
  M = C(k,2) - k/2 vertices. For (99,14,1,2) this is a 12-regular graph on 84
  vertices. The paper exhaustively proves (Prop 1) no circulant on Z/99Z
  satisfies more than 33/49 difference-classes (score 3366/4950 = 68.0%); an
  orbit-existence CP-SAT encoding for a prescribed automorphism is validated by
  recovering srg(9,4,1,2) and Paley srg(13,6,2,3), then leaves the open
  single-fixed-point Z_7 case unresolved (unknown after 48h/14 cores); the best
  heuristic artifact is 3437/4950 = 69.43%. A perfect score 4950 is an
  srg(99,14,1,2), so a provable bound below 4950 would be a nonexistence proof;
  no such bound is claimed.
hypotheses: none beyond the srg(v,k,1,2) forced-structure derivation, the
  circulant-connection-set model, and the prescribed-automorphism orbit model.
holds-here: yes — the Section 4 reduction independently reproduces the run's
  own derived-design-at-a-vertex reduction (research/backward/
  derived-design-at-a-vertex.md), which this run has additionally COMPUTED to
  NOT recurse (the outer design's collinearity graph is not an srg(*,*,1,2);
  checked on bvls, g-reduce-c-refuted). The Z_7 sub-case the paper leaves open
  is exactly the rung this run's automorphism ledger lists as not excluded.
status: asserted-by-source (preprint, not peer-reviewed; all reported numbers
  are the paper's claims, none reproduced in this run's code/out/ yet). The
  forced-structure reduction is independently derivable and matches the run's
  own checked computation; the circulant bound and Z_7 unknown are leads.
bearing: provides the only independent corroboration in this library of the
  outer-graph reduction, documents (honestly) that general-purpose CP-SAT does
  not decide even the open Z_7 sub-case, and frames the 4950/68.0%/69.43% score
  terminology under which a provable bound < 4950 is a nonexistence proof.
anchor: research/sources/forced-structure-reduction-conway99.full.md
```

## Relationship to the run's own computed results

The run independently derived the same forced-structure reduction
(`research/backward/derived-design-at-a-vertex.md`) and — beyond the preprint —
computed that the reduction does NOT recurse: the outer (84-vertex) design's
collinearity graph has λ=1 but non-constant μ on the 243 control
(`g-reduce-c-refuted`, checked). So the preprint's Section 4 stops at the
12-regular/84-vertex model; the run's g-reduce thread goes further and shows
that model cannot be an srg(*,*,1,2) in kind. This preprint corroborates the
hard part (inner-outer adjacency fully forced) and the Z_7 open status.
