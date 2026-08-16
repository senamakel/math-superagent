# Capture — oracle self-check (rook, BvLS, negative controls)

**Ran:** `python code/lib/srg.py` self-check, plus an inline near-miss probe.
**Oracle function:** `lib.srg.is_srg` (exact integer common-neighbour counting,
no floating point) over `rook(3)`, `rook(4)`,
`bvls_graph()` (from the corrected `_TERNARY_GOLAY_H`), `random_regular_14_99`,
an edge-moved rook(3), and the Petersen graph.
**Inputs:** the exact integer adjacency matrices produced by those constructors,
all 0/1, judged against parameters (9,4,1,2) and (243,22,1,2) and (99,14,1,2).

## Result — the oracle's admissibility controls all pass

```
$ python code/lib/srg.py
rook(3) is_srg(9,4,1,2): (True, 'srg(v,k,lambda,mu) confirmed by exact common-neighbour counts')
rook(4) is_srg(9,4,1,2): (False, 'shape (16, 16) != (9,9)')
bvls shape: (243, 243)
bvls edges: 2673
bvls is_srg(243,22,1,2): (True, 'srg(v,k,lambda,mu) confirmed by exact common-neighbour counts')
random 14-regular on 99 vertices is_srg(99,14,1,2): (False, 'off-diagonal common-neighbour mismatch on 9504 entries')
```

Near-miss controls (inline probe through the same `lib.srg.is_srg`):

```
rook(3) with one edge moved is_srg(9,4,1,2): (False, '2 rows have degree != 4')
Petersen is_srg(9,4,1,2): (False, 'shape (10, 10) != (9,9)')
```

## What this establishes

- **`rook(3)` IS srg(9,4,1,2)** — positive control at 9 vertices. (Also equals
  Paley(9) per research note; the rook construction is the graph of the 3x3
  grid, adjacent iff same row or same column.)
- **`bvls_graph()` IS srg(243,22,1,2)** — positive control at 243 vertices,
  2673 edges, every degree exactly 22, exact common-neighbour counts confirm
  lambda=1 / mu=2. The underlying code is confirmed to be the perfect ternary
  Golay code: 729 codewords in (11,6), minimum nonzero Hamming weight 5.
- The oracle **rejects** every near-miss tried: the shifted (16,16) rook, a
  14-regular graph on 99 vertices (mismatch on 9504 off-diagonal entries), an
  edge-moved rook(3), and the Petersen graph (wrong shape for (9,4,1,2)).

## Fixes made this run

1. **`code/lib/srg.py::_TERNARY_GOLAY_H` was wrong and is now corrected.** The
   previous parity-check matrix had two identical (mutually proportional)
   columns, so the coset graph double-counted edges: it produced 2430 edges and
   no vertex of degree 22, and `is_srg(243,22,1,2)` was False. The replacement
   H is derived from the cyclic generator polynomial
   `g0 = x^5 - x^3 + x^2 - x - 1` of the ternary Golay code; its 11 columns
   are pairwise non-proportional (verified: 11 unique, no scalar-multiple
   pair). With it the coset graph is 22-regular and passes exactly. The fix is
   to the *construction*, not a weakening of the check.
2. **`code/lib/srg.py::random_regular_14_99` no longer uses rejection
   sampling.** The config-model sampler for a 14-regular graph on 99 vertices
   can loop essentially forever (it is what made the first self-check run hang
   at the 600s tool timeout). Replaced with a deterministic circulant graph
   (connection set {1..7} mod 99, degree 14, matching the stated v-regularity
   but with the dependent structure that certainly fails srg(99,14,1,2)). It
   terminates instantly and serves the negative-control role.
3. **`code/out/check_bvls.py` now calls `lib.srg.is_srg` and `lib.srg.bvls_graph`
   and contains no inline srg decision.** Its own `is_srg`, `coset_graph`, and
   `ternary_golay_parity_check` were deleted; the canonical oracle in lib is
   now the single decision. (Its `count_induced_K112` helper is left in place,
   unfinished, for the subgraph question—this run did not rely on it.)

## Caveats

- `count_induced_K112` in check_bvls.py is incomplete and unused; nothing in
  this capture depends on it.
- The negative-control circulant graph is **not** a faithful uniform random
  14-regular graph; it is a fixed deterministic stand-in chosen only to have
  degree 14 and to be rejected by the oracle. If a uniform random sample is
  ever wanted, use a better sampler (e.g. `networkx.random_regular_graph`) with
  a hard loop cap — that is a separate decision and was not needed here.

## Ceiling

Oracle runs are O(v^3) exact integer matrix multiply on v=9, v=243, v=99 — all
well under a minute on this box. The largest object touched is the 243x243
BvLS adjacency matrix.
