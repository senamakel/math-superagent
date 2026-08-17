# The folklore fixed-set lemma FAILS on the BvLS control

## Claim being tested

Folklore lemma (stated in `orbit-matrix-residual-group.md` first-step (4)):
*under an automorphism of an srg(v,k,1,2), the fixed-point set is a coclique or
a smaller strongly regular graph.*

This is asserted there, never re-derived, and was flagged as needing
re-derivation before being relied on. This note settles it: **the lemma as
stated is FALSE** — it fails on the BvLS control `srg(243,22,1,2)`, which
actually exists and is in the run's library.

## What was checked

Tool-builder constructed real automorphisms of both controls and classified
every fixed set exactly (exact integer arithmetic, `lib.srg.is_srg` oracle):

- **rook(3) = srg(9,4,1,2)**: all 72 automorphisms by construction
  (S3 rows × S3 cols × C2 transpose). Every fixed set is a coclique (size 1 or
  a 3-vertex independent set) or the complete K3 (a degenerate SRG). The lemma
  HOLDS on this control.

- **bvls_graph() = srg(243,22,1,2)**: coordinate-permutation/sign
  automorphisms fixing vertex 0, `v -> (signs_j * x_{perm_j})`, found by
  construction and **each validated as a true automorphism by direct 243×243
  matrix conjugation `P A P^T == A`**. Among the 40 such automorphisms fixing 0
  (39 non-identity), the fixed sets range over sizes 1, 3, 9, 27. Several of
  size 9 are cocliques; several induce exactly `srg(9,4,1,2)` (a smaller
  same-family member); several of size 3 are K3.

  **The counterexample:** an order-2 automorphism
  `perm=(0,2,1,4,3), signs=(1,1,1,2,2)` fixes exactly **27 vertices**. The
  induced subgraph is **6-regular** (81 edges) with **lambda = 1 constant**
  (all 162 adjacent pairs have exactly 1 common neighbour) but **mu
  non-constant in {0:216, 2:324}**. The exact oracle rejects it as
  `srg(27,6,1,2)` with "MU mismatch: 216 non-adjacent pairs have common-
  neighbour count != 2". So the fixed set is **neither a coclique nor an SRG**.

## Independent verification (second route)

`code/out/fixed_set_lemma_independent_verify.py` re-derives this from scratch:
re-builds BvLS, directly checks `P A P^T == A` for the candidate permutations
(243×243 boolean equality), and for the specific `(0,2,1,4,3),(1,1,1,2,2)`
automorphism confirms order 2, fixed size 27, 6-regular, lambda{1:162},
mu{0:216,2:324}, and `is_srg(S,27,6,1,2) = False`. Confirms the main script.

## The lambda=1 / mu=2 reasoning (verified against the actual matrices)

For a fixed vertex x and fixed a,b both adjacent to x:

- If a,b are **ADJACENT**: they share exactly lambda=1 common neighbour, so x
  is their **unique** common neighbour; {a,b,x} is a triangle and no other
  vertex is adjacent to both a and b.
- If a,b are **NON-adjacent**: they share exactly mu=2 common neighbours, so x
  is **one of two** (there is a second such vertex, fixed or not).

**lambda=1 does NOT force a,b non-adjacent.** The fixed set of an
automorphism is a union of "pieces" whose pairwise adjacency is governed only
by these local constraints — nothing forces it to be globally coclique or
globally strongly regular. The 27-vertex example is the proof.

## Consequence for the run

Approach `orbit-matrix-residual-group.md` first-step (4) listed this lemma as
needed and unanswered. It is now **answered negatively**: an orbit-matrix /
fixed-set argument for (99,14,1,2) must NOT assume the fixed set is a coclique
or a smaller SRG. The De Winter–Kamischke–Wang congruence and the orbit-matrix
machinery remain valid and are unaffected; only this extra structural claim
about the fixed set is removed.

## Files

- `code/out/fixed_set_lemma.py` — main construction + classification.
- `code/out/fixed_set_lemma_controls.captured.txt` — its capture.
- `code/out/fixed_set_lemma_bvls_detail.captured.txt` — BvLS orders/fixed sizes + the 27-vertex counterexample detail.
- `code/out/fixed_set_lemma_independent_verify.py` + `.captured.txt` — independent matrix-conjugation route.

```claim
id: fixed-set-lemma-fails-on-bvls
statement: The folklore lemma "under an automorphism of an srg(v,k,1,2), the
  fixed-point set is a coclique or a smaller strongly regular graph" is FALSE.
  It fails on the existing control bvls_graph() = srg(243,22,1,2): an order-2
  automorphism fixes exactly 27 vertices whose induced subgraph is 6-regular
  with constant lambda=1 (162 adjacent pairs) but non-constant mu in
  {0:216, 2:324}; the exact oracle rejects srg(27,6,1,2) with "MU mismatch".
  It HOLDS on rook(3) = srg(9,4,1,2) (all fixed sets are cocliques or complete
  K3, a degenerate SRG).
hypotheses: automorphism is taken in the graph-theoretic sense (permutation
  with A[g(i),g(j)]=A[i,j]); fixed set = vertices fixed pointwise; the controls
  are the two existing members of the srg(v,k,1,2) family.
holds-here: yes — it refutes a structural claim the orbit-matrix approach had
  listed as a lemma to rely on for the open (99,14,1,2) case.
status: checked (exact integer arithmetic; both the construction and an
  independent matrix-conjugation P A P^T == A route; oracle lib.srg.is_srg
  used for the induced-subgraph verdict).
base: code/out/fixed_set_lemma_controls.captured.txt,
  code/out/fixed_set_lemma_bvls_detail.captured.txt,
  code/out/fixed_set_lemma_independent_verify.captured.txt
bearing: an orbit-matrix / fixed-set argument for srg(99,14,1,2) must NOT
  assume the fixed set is a coclique or a smaller SRG. The De Winter–Kamischke–
  Wang congruence and the orbit-matrix machinery are unaffected; only this
  extra structural claim about the fixed set is removed. Closure of first-step
  (4) of approach orbit-matrix-residual-group.md.
```

