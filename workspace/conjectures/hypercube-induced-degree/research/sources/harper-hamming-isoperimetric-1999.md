# Harper, "On an isoperimetric problem for Hamming graphs" (Discrete Applied Math., 1999)

Source URL: https://doi.org/10.1016/s0166-218x(99)00082-7
(Retrieved via `read_sources`; direct PDF download blocked by network boundary.)

## What this source establishes

Harper's vertex-isoperimetric theorem for the Hamming cube Q_n: among all
subsets A ⊆ {0,1}^n with |A| = k, the **minimum vertex boundary** is achieved
when A is a Hamming ball (all strings of weight ≤ r, completed in the relevant
layer), where k = Σ_{i=0}^{r} C(n,i). For such a ball the vertex boundary is
determined by the layer structure. The edge-boundary-vs-single-index version:
initial segments in the binary Hamming order (layers by weight, grey/lex within
layer) minimise edge boundary for fixed size.

Method: compression (shifting) operators that push a set toward ball/skyline
form without increasing the boundary; iterate to a fully compressed set, which
is a Hamming ball.

## Why it is here

This is the canonical primary source for cube vertex-isoperimetry. It controls
the *external* boundary, not the maximum *internal* degree D(S) that problem.md
asks about. Recording the exact boundary: a compression argument that fixes the
vertex boundary does not transfer to D(S) without a new argument, because
internal degree is not monotone under the same compressions in the needed
direction.

## Claim block

```claim
id: harper-vertex-isoperimetric-hamming-ball
statement: Among subsets A of Q_n of a fixed size k, the vertex boundary is
  minimised by a Hamming ball B_r with k = sum_{i<=r} C(n,i) (Harper 1999);
  compression proves it.
hypotheses: A ⊆ {0,1}^n, fixed |A| = k.
holds-here: yes as a boundary statement; but it bounds external boundary,
  not max internal degree D(S). Not directly usable for problem.md's D(S).
status: asserted-by-source.
bearing: confirms the obstruction: vertex-isoperimetry (compression) optimises
  an outer quantity and does not by itself lower-bound the maximum degree
  inside S; a new, degree-monotone compression would be needed.
anchor: harper-hamming-1999
```
