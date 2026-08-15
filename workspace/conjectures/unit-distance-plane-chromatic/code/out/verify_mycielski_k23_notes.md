# M^k(C5) is not unit-distance realizable for k >= 2 — via the K2,3-freeness lemma

## Task

Check whether any higher Mycielski iterate of C5 can be realized as a
unit-distance graph (UDG). Claimed answer: **no**, for k >= 2, and the
disqualification is a *direct consequence of the K2,3-freeness lemma* — it
does **not** depend on any colouring oracle or chromatic computation.

## The two facts that make the claim

**Fact 1 (certified lemma, `code/out/sharp_nbhd_cert.captured.txt`).** Every
unit-distance graph is K2,3-free. Proof sketch recorded there: if u ≠ w are
vertices at squared distance d² > 0, the set `{x : |x−u| = |x−w| = 1}` is the
intersection of two unit circles centred d apart, which is empty or exactly two
points. Hence any two vertices share at most two common neighbours, so no two
vertices can share three, so no K2,3 occurs. This is a pure geometry/exact-algebra
fact — no colouring oracle, no SAT, no chromatic number. Status: PASS
(ALL CERTIFICATES PASS in that artifact).

Therefore **K2,3-free is a NECESSARY condition for unit-distance realizability.**

**Fact 2 (computed here).** M^k(C5) contains a K2,3 for every k >= 2.

## Construction used (the correct textbook one)

Mycielskian `mu(G)`: keep the original vertices/edges, add a twin `u_i` per
vertex, a root `w`; add cross edges `u_i v_j, u_j v_i` for each edge `v_i v_j`,
and the star `w u_i` to every twin. Total `3|E| + n` (the *mirror* variant with
twin-to-twin edges `u_i u_j` is a different, non-canonical flavour; the run's
kernel and the verdict use the no-mirror canonical form — see below).

This is confirmed by the catalogue value Mycielski(C5) = Groetzsch = **11 v, 20 e**
and the run's recorded verdict **Mycielski²(C5) = 23 v, 71 e, chi 5**,
both reproduced exactly. (A misleading comment in `diag_mycielski.py` claims a
4|E|+n total, but its code — like the verdict — computes the 3|E|+n canonical
form; the counts 20 and 71 only match the canonical form.)

## Machine-verified results

Built M^0..M^4 by iterating the accepted Mycielskian, cross-checked counts two
ways (direct build vs edge recurrence `E_{k+1}=3E_k+V_k`, `V_{k+1}=2V_k+1`;

| level | |V| | |E| | K2,3-free? | explicit K2,3 |
| --- | --- | --- | --- | --- |
| M^0 = C5 | 5 | 5 | yes | — |
| M^1 = Groetzsch | 11 | 20 | yes | — |
| **M^2** | **23** | **71** | **NO** | vertices 0,2 share {1,6,12,17} |
| **M^3** | **47** | **236** | **NO** | vertices 0,2 share {1,6,12,17} |
| **M^4** | **95** | **755** | **NO** | vertices 0,2 share {1,6,12,17} |

**Explicit K2,3 in M^2(C5):** vertices **0 and 2** are joined to each of the
three common neighbours **1, 6, 12**; the six cross-edges
{0,1},{0,6},{0,12},{2,1},{2,6},{2,12} were each asserted present in the exact
edge set. (In fact these two vertices share **four** common neighbours
{1,6,12,17}, an even stronger violation.) The same K2,3 on vertices (0,2) is
present in M^3 and M^4 by containment of the M^2 original-vertex subset — the
construction keeps every original edge, so a K2,3 already present inside M^2
persists.

Robustness: the identical K2,3 is found by an **independent adjacency-list
builder** (`verify_mycielski_k23_indep.py`) and by the **mirror variant**
(`verify_mycielski_both_variants.py`), so the conclusion does not depend on the
choice of "textbook" construction.

## Conclusion

- The kernel disqualification **is** a consequence of the K2,3-freeness lemma:
  since every UDG is K2,3-free (Fact 1) and M^k(C5) contains a K2,3 (Fact 2),
  M^k(C5) is not realizable as a unit-distance graph for every k >= 2. **No
  colouring assumption, solver, or chromatic computation is involved.**
- Consequence: the Mycielski family **cannot** supply the run's needed
  "rigid 4-chromatic UDG with a forced monochromatic pair". The route dies to a
  NECESSARY geometric condition (K2,3-free) at the very second iterate.

## Artifacts

- `code/verify_mycielski_k23_udg.py` (primary, cross-checked counts + asserted K2,3 cross-edges)
- `code/verify_mycielski_k23_indep.py` (independent adjacency build)
- `code/verify_mycielski_both_variants.py` (robustness to mirror-variant)
- Outputs in `code/out/verify_mycielski_k23_udg.captured.txt` and siblings.

## Status

Verified (machine-checked, exact/graph-theoretic). Both premises are
independently established: the lemma is a certified artifact; the K2,3 is
constructed and its six cross-edges asserted present. Two independent builders
agree. Not a proof in the colouring sense — it is a correct, complete
non-realizability argument resting on a certified geometric fact.
