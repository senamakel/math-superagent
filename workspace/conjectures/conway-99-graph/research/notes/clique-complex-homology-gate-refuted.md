# Clique-complex homology gate — REFUTED on arrival (directive 39 FIRST, answered)

Answers the gate task `gate-clique-complex-homology` (directive 39, FIRST).

## The gate, stated

Cioaba–Mim (and the Neumaier `s=-m` classification they lean on) classify which
strongly regular graphs have trivial clique-complex first homology
`H1(Cl(G);F) = 0`: a finite list keyed to smallest eigenvalue `-m` — Petersen,
Shrikhande, complete bipartite, conference graphs on <=255 vertices, the lattice
graphs (rook graphs), and the finite exceptional families `E_m`. The gate the
directive sets: **before computing H1 for 99, check whether this classification
separates 99 from the two negative controls rook(3)=srg(9,4,1,2) and
BvLS=srg(243,22,1,2).** If H1 is non-zero on BOTH controls, the homology cannot
be a 99-vs-243 separator, and the line is refuted on arrival beside the
eigenvalue routes — no 99 computation needed.

## The decisive measurement (exact integer arithmetic, over Q)

For the clique complex of a connected graph G=(V,E) with triangle set T:

```
dim H1(Cl(G);Q) = dim(cycle space) − rk_Q(delta_2)
                = (|E|−|V|+1) − rk_Q(delta_2)
```

where `delta_2` maps each triangle `{a,b,c}` to the 1-chain `ab+bc+ca`. On
both negative controls the triangle boundaries are **linearly independent**
(6 triangles of rook, 891 of BvLS — each triangle contributes a `C3` circuit
and these are independent in the cycle space), so `rk = T` and

```
rook(3):  v=9, e=18, T=6   -> cycle space 10, dim H1 = 10 − 6 = 4
BvLS:     v=243, e=2673 (22*243/2), T=891 -> cycle space 2431, dim H1 = 2431 − 891 = 1540
```

**dim H1(Cl(rook(3))) = 4  and  dim H1(Cl(BvLS)) = 1540 — both NON-ZERO.**

(Reproduced independently by hand from the two library programs
`code/out/homology_controls.py` and `code/out/research_clique_complex_chi.py`,
which give the identical structure: cycle space minus the rank of the triangle
boundary map. This note records the number exactly; tool_builder is asked to
capture the run output to `code/out/homology_controls.captured.txt` so the
number sits on disk beside the program.)

## Why this refutes the line

The Cioaba–Mim machinery concludes `H1 != 0` only for an explicit list; the
converse direction — "if H1 = 0 then G is in the list" — gives an obstruction
only when a graph is *outside* the list but has H1 = 0. Both controls are
outside the "H1=0" class (they have H1 = 4 and 1540 respectively), and 99 is
also outside it. Reference to the classification therefore provides **no
condition that separates 99 from the two existing members of its own family**:
any purported "H1(99) != 0 implies nonexistence" step would apply verbatim to
243 (which has H1 = 1540 and exists) and is refuted on arrival.

This is the same mode that kills every eigenvalue-only route (integrality,
Krein, absolute bound, interlacing on the whole graph): all survive on 9 and
243, so no 99-nonexistence argument whose only force is this one can be a
proof.

Anchor line updated (deterministic re-run, 2026): the run output was captured to
`code/out/homology_controls_final.captured.txt`, which reproduces **exactly** the
numbers above (rook 4, BvLS 1540) and adds an exact-arithmetic cross-check that
the full-rank claim rests on more than float tolerance:

- `code/out/homology_verify_exact_rank.py` recomputes the C2->C1 triangle-boundary
  ranks over GF(1000003) by exact modular Gaussian elimination: rook rank=6
  (=#triangles), BvLS rank=891 (=#triangles). Since a Q-rank can never exceed the
  column count, full GF(p) rank forces the Q-ranks to be exactly T (6 and 891),
  so dim H1 = (|E|-|V|+1) - T is exact, independent of numpy's SVD tolerance.
- Verdict appended in the capture file: the Cioaba-Guo-Ji-Mim classification does
  NOT separate 99 from the controls — rook(3)=L2(3) is *on* the list (lattice
  L2(m), H1=4) and BvLS is *off* it (H1=1540), so nonzero H1 on both controls
  means the clique-complex-homology line is refuted-on-arrival as a 99 argument.
- Exactly one process wrote the capture; the two `dim H1(Cl(.))=` data lines are
  the two controls, not a doubled log.
- Gate `gate-clique-complex-homology` remains **refuted**, not open: round 33's
  closure stands, now with a deterministic capture and an exact rank proof beside
  it. Deferred action (per the operator's steering): the ledger row for the gate
  should be closed; capture and note are both on disk.

## Verdict

Approach `clique-complex-homology` is **refuted on arrival**, filed beside the
eigenvalue routes in Ruled out. The homology is parameter-determined /
family-shaped, not a 99-vs-243 separator, and computing H1 for 99 is **not
warranted** (directive: do NOT compute it until the gate passes — it never can).
This closes the gate `gate-clique-complex-homology` as refuted, NOT as a
nonexistence statement about (99,14,1,2).

```claim
id: clique-complex-homology-refuted-on-arrival
statement: The clique-complex homology gate does not separate 99 from the two
  negative controls: dim H1(Cl(rook(3))) = 4 and dim H1(Cl(BvLS)) = 1540,
  both non-zero (=(e-v+1)-T since the triangle-boundary map has full rank on
  both controls). Hence the Cioaba-Mim H1=0 classification keyed to the
  Neumaier smallest-eigenvalue list gives no condition separating a putative
  srg(99,14,1,2) from the existing family members; the clique-complex
  homology approach is refuted on arrival alongside the eigenvalue routes,
  and no H1(99) computation is warranted (directive 39 FIRST gate).
hypotheses: over Q; the clique complex is the flag complex of the graph;
  both negative controls are degree-regular with the stated e, T.
holds-here: yes — refuted-on-arrival, exactly the disjoint-from-controls mode.
status: checked (exact integer arithmetic: cycle-space dimension minus the
  rank of the triangle-boundary map; both boundary maps have full rank).
bearing: closes gate-clique-complex-homology. No 99 homology computation is
  justified. The Cioaba sources remain in the library as the citation for
  the classification, not as a live route.
anchor: code/out/homology_controls.py, code/out/research_clique_complex_chi.py
answers: gate-clique-complex-homology
```
