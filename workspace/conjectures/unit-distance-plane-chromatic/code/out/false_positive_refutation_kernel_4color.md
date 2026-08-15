# False-positive refutation — the TPTP kernel_4color.p "refuted" verdict is an artifact

## What the tool returned

`code/refute/kernel_4color.p` (an existing problem in this workspace, encoding
the sharp-kernel-4color claim "every graph with min-deg>=4, K4-free, K2,3-free,
nbhd-maxdeg<=2 is 4-colourable") was run through `find_counterexample`. SZS
verdict: **CounterSatisfiable** — an 8-vertex model satisfying all four kernel
axioms and, the engine claims, falsifying the conjecture (no proper 4-colouring).

This directly contradicts the run's verified census: n=8 has EXACTLY one kernel
member, and it is 4-colourable (page `code/out/census_kernel_n11_run.captured.txt`
and the 249-member cross-check). A genuine non-4-colourable C_8 member would be
a headline result. It had to be checked by hand against the original statement.

## Decoding the model

Decoded edge relation (1-indexed -> 0-indexed adjacency, all 8 vertices degree 4):

```
0(v1):{3,4,5,7}  1(v2):{2,5,6,7}  2(v3):{1,3,6,7}  3(v4):{0,2,4,7}
4(v5):{0,3,5,6}  5(v6):{0,1,4,6}  6(v7):{1,2,4,5}  7(v8):{0,1,2,3}
```

Edges (16): 0-3,0-4,0-5,0-7, 1-2,1-5,1-6,1-7, 2-3,2-6,2-7, 3-4,3-7, 4-5,4-6, 5-6.

## Verification against the four kernel conditions — all PASS

- (a) min degree = 4 (every vertex 4-regular). PASS.
- (b) K4-free: for every vertex, its neighbourhood contains NO triangle, so no
  K4. Checked all 8. PASS.
- (c) K2,3-free: every pair of vertices has at most 2 common neighbours
  (max common = 2). PASS.
- (d) nbhd-maxdeg<=2: every vertex-neighbourhood induces max degree <= 2.
  PASS.

So the model graph IS a member of C_8 — consistent with the census's single
n=8 member.

## The graph is 4-colourable — the verdict is an artifact

Explicit proper 4-colouring (A,B,C,D distinct):

```
0:C  1:D  2:A  3:D  4:A  5:B  6:C  7:B
```

Verified edge-by-edge (all 16 edges have distinct endpoint colours — full
listing in the analysis below). **The graph has a proper 4-colouring**, so it is
NOT a counterexample to `sharp-kernel-4color`. The engine's "refuted" is a
false positive.

## Why the encoding is unsound for refutation

The TPTP problem declares `has_colour(X, C)` as a completely unconstrained
free predicate (the axioms never mention it) and states as the conjecture "a
proper 4-colouring exists" (at-least-one colour per vertex + no edge shares a
colour). The model-finder satisfies the axioms and then makes the conjecture
false in a **vacuous** way: it leaves vertex 1 (fmb_$i_1) UNCOLOURED
(has_colour(1, c) = false for all four colours). That falsifies the
conjecture's "every vertex has a colour" conjunct regardless of the graph's true
chromatic number.

But "G is 4-colourable" is an **existential** claim. An exhibit of one
assignment that is not a proper colouring says nothing about whether a proper
colouring exists. The model-finder exploits the free `has_colour` to "refute"
a true statement. The SZS `CounterSatisfiable` verdict therefore does not mean
`sharp-kernel-4color` is false — it means the FOL encoding is the wrong vehicle
for this claim. "Not 4-colourable" is a universal negative over colour
assignments and cannot be soundly captured in a single model-finding pass via a
free predicate; the sound method is exhaustive graph enumeration + a complete
chromatic oracle, which is exactly what the run's census does (and it finds this
member 4-colourable).

## The n=8 census member is the same story — consistent

The run's census (`census_kernel_n11_run.captured.txt`) lists exactly **one**
n=8 kernel member, with witness `[0,0,1,1,2,2,3,3]`, and reports it
4-colourable. My hand-checked model graph (decoded from the TPTP model) is also
a C_8 member with an explicit proper 4-colouring
`[0=C,1=D,2=A,3=D,4=A,5=B,6=C,7=B]`. Both are 4-chromatic, both 4-colourable —
fully consistent with the verified census.

## What this means for the run

- The existing `code/refute/kernel_4color.p` must NOT be read as a refutation
  of `sharp-kernel-4color`. Its "refuted" verdict is a coding artifact, not a
  counterexample.
- **The FOL-encoding route cannot soundly refute this claim.** "G is
  4-colourable" is an existential assertion over colour assignments; its
  negation (non-4-colourability) is universal and cannot be witnessed by one
  model. A model-finder will always "refute" it vacuously by leaving some
  vertex uncoloured through the free `has_colour` predicate. The sound method
  is exhaustive graph enumeration + a complete chromatic oracle — exactly what
  the run's census does.
- It is **consistent** with the size-bound census: the unique n=8 kernel member
  is 4-colourable.
- The run's strongest verified result ("every unit-distance graph on <=11
  vertices is 4-colourable", `census-kernel-n11-result.md`) is **not**
  contradicted.

```claim
id: kernel-4color-tptp-refutation-is-false-positive
statement: >
  find_counterexample on code/refute/kernel_4color.p reports "refuted"
  (CounterSatisfiable) with an 8-vertex model, but the decoded graph is a
  genuine member of C_8 (min-deg=4, K4-free, K2,3-free, every neighbourhood
  max-deg<=2 — all verified by hand) AND has an explicit proper 4-colouring
  [0=C,1=D,2=A,3=D,4=A,5=B,6=C,7=B], checked edge-by-edge over all 16 edges.
  So it is NOT a counterexample to sharp-kernel-4color. The engine's "refuted"
  is an artifact: the FOL conjecture expresses 4-colourability existentially
  via a free has_colour predicate, and the model-finder falsifies it vacuously
  by leaving vertex 1 uncoloured, independent of the graph's true chromatic
  number. "Not 4-colourable" is a universal negative over colourings and cannot
  be soundly captured in one model-finding pass; the sound method is exhaustive
  enumeration + complete chromatic oracle, which is what the run's census does.
hypotheses: code/refute/kernel_4color.p encoded as written (four kernel axioms
  + a proper-4-colouring conjecture with a free has_colour predicate).
holds-here: yes — this is the workspace's own refute file; the finding is about
  the encoding, not the mathematics.
status: checked (hand-verified: all four kernel conditions AND an explicit
  proper 4-colouring of the 8-vertex model; consistent with the unique 4-
  colourable n=8 census member)
bearing: retracts the engine's "refuted" verdict on sharp-kernel-4color; the
  size-bound census (N=11) and the size-bound-udg-4color-n11 result stand; the
  FOL/TPTP route is the wrong vehicle for this existential-colourability claim.
falsifies: any genuine member of C_8 that is not 4-colourable — none exists
  (the single n=8 census member is 4-colourable, and so is this model).
```
