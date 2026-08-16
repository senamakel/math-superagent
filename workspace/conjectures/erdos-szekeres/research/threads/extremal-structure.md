# Structural constraints on a hypothetical extremal set

The run's core structural question: what must a set X of 2^{n-2} points in general position
with NO convex n-gon look like? This thread collects the constraints the library already
establishes, so a structural lemma does not re-derive what is on disk.

```thread
question: What local/global structure is a 2^{n-2}-point set with no convex n-gon forced into, and how close must it be to the ES construction?
status: open
rests-on: es61-lower-bound, es35-cups-caps-bound, ms-cups-caps-tight, baek-balko-split, baek-balko-decomposable, damasdi-saturation, ps-es6, ms-toth-valtr-bound, smqh-no-realizable-4fold-32-no7gon
blocked-by: a structural (stability/uniqueness) theorem does not yet exist; counting methods are proved insufficient (ms-cups-caps-tight shows the loss is in the cups/caps dimension, not the lemma)
next: (1) FIRST (steer 11): task `gsplit-enumeration-recheck` — one command,
not another design pass. Phase 1 is done: the rotating-line enumerator
(`gsplit_enum_definitive.py`) matches the 2^N disjoint-hulls oracle exactly at
N=8,10,12,14,16 (zero missing, zero extra, count N(N-1)). Re-capture Phase 2
with provenance by running exactly
`cd /workspace && { echo "$ python code/out/gsplit_enum_definitive.py"; timeout 550 python code/out/gsplit_enum_definitive.py; echo "EXIT: \0"; } > code/out/gsplit_phase2.captured.txt 2>&1`
(no pipe, no tee, no arrays), then read the capture back. If it reproduces
4 splits at n=5, 2 at n=6, 0 at n=7: promote
`gsplit-enum-completeness-and-n7-zero` to checked for the split counts too,
retire `gsplit-exhaustive-esconstruct` pointing at
`code/out/gsplit_phase2.captured.txt`, and write the scoped finding into
CONTEXT.md Established (template only: the splitting-line induction
f(n)<=2f(n-1) holds on the verified es_construct template through n=6 and fails
on it at n=7). If it does not reproduce, say so plainly and give the new
numbers. Do not start another enumerator. (2) only after the
rotating-line enumerator passes: scored program search over code/search/es-nogon
(steer 6) — tool_builder writes the scorer against the VERIFIED es_geom
orientation predicate (searcher must not write the scorer), k=6 rung must cap at
exactly 16 before k=7, k=7 record is 32 and 33+ refutes ES(7)=33, report the
score distribution and which constraint binds; (3) state and attack a precise
structural lemma from the convex-layer profiles of the verified construction —
captured [3,1] (n=4), [4,4] (n=5), [5,5,3,3] (n=6), [6,6,6,5,6,3] (n=7): e.g.
the outer layer of X_n has size n−1 (it does: 3,4,5,6), each layer is an
(n−1)-avoiding set in its own right, and the layer sizes sum to 2^{n-2}; the
natural conjecture is that for the ES construction every convex layer is
extremal — attack it with the oracle at n=6,7 before generalizing. The
block-tightness identity `es-construct-block-tightness` (every interior block
achieves cup+cap=n at n=3..11) is the sharpest per-block regularity and a
candidate lemma.
```

## What the library already pins down

- **The extremal object exists**: the ES 1961 construction is a 2^{n-2}-set with no convex
  n-gon (`es61-lower-bound`), saturated (`damasdi-saturation`). But Damásdi et al. also build
  saturated sets of only (7/8)·2^{n-2} for n≥7 — so saturation alone does NOT force size 2^{n-2}
  or near-decomposability.
- **Counting is provably lossy**: f(k,l)=C(k+l-4,k-2)+1 is tight (`ms-cups-caps-tight`), so the
  4^n bound loses entirely in the reduction to cups/caps. An exact 2^{n-2} bound needs a
  stability/uniqueness argument, not more counting.
- **Relaxed exact threshold is right**: split-k-gon threshold is exactly 2^{k-2}+1 and ES holds
  for decomposable sets (`baek-balko-split`, `baek-balko-decomposable`) — the strongest current
  evidence the 2^{k-2}+1 constant is the correct one, and a concrete route: force convex
  position from a split k-gon plus structure, or show extremal sets are near-decomposable.
- **The 4-set convexity criterion** (`es35-four-criterion`) reduces "no convex n-gon" to a
  finite local (4-set) condition — the handle the SAT encodings and any finite-constraint
  structural lemma use.
- **n=6 verified**: ES(6)=17 (`ps-es6`); the Peters–Szekeres encoding + cost is the oracle and
  n=7 budget model.
- **n=7 frontier**: Dumitru's SAT encoding settles only anchored subfamilies, heavy-tailed
  runtime (`dumitru-es7`, status asserted).
- **No 4-fold-symmetric 32-point no-7-gon set** (`smqh-no-realizable-4fold-32-no7gon`): full SAT
  enumeration (310,187,713 solutions, ~1 CPU-yr) shows every 4-fold-symmetric 32-point 7-gon-free
  orientation has one of 6 non-realizable inner-12 configurations; hence a hypothetical extremal
  32-point set (if it exists) has no 4-fold rotational symmetry. A concrete impossibility result
  on the ES(7) frontier.
- **200,000 abstract 32-point no-7-gon candidates, none realizable** (`kph-32-no7gon-no-realizable-found`):
  PointSAT's unconstrained search generated 200,000 abstract order-type solutions (2191 core-hrs),
  none realizable. Not a disproof of ES(7)=33 (abstract space not exhausted; realizable fraction
  shrinks with n); but it, SMQH, and Dumitru's anchored-subfamily UNSAT together mean: on the
  ES(7) frontier every computational route reaches 32-point no-7-gon candidates and none has
  realized one. The search space is almost entirely abstract/unrealizable.

## Contradiction / hazard to keep in view

- The ordered-3-uniform-hypergraph analogue of ES FAILS (`baek-balko-split`), so an abstract
  generalization is not free; do not claim the planar result from an abstract-hypergraph
  analogue.
- Realizability is ETR-complete; a structural claim proved over all abstract order types may
  hold on unrealizable ones and be false geometrically (`aichholzer-order-db` caveat).
