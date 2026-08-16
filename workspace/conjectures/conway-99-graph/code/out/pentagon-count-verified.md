# Induced pentagon (C5) count closed form — verified on both controls

GOAL.md names "a counting identity in the number of induced C5" as a candidate
structural lever for a putative srg(99,14,1,2). The Reimbayev closed form is
`p5 = n·k·(k−2)·(k−4)/5`. This note records that it is now **verified on both
control graphs** (promoting it from asserted-by-source to checked), and states
what it does and does not do for the 99 problem.

## The verification (two independent exact routes)

1. **rook(3) = srg(9,4,1,2):** brute force over all C(9,5) = 126 five-subsets
   with an exact induced-degree-2 criterion (5 edges, all degrees 2): induced
   C5 count = **0** = 9·4·2·0/5. (`code/out/check_pentagon_formula.py`.)
2. **BvLS = srg(243,22,1,2):** anchored directed-edge enumeration — for each
   edge a–b the pentagon a-b-c-d-e-a is completed with c∈N(b), e∈N(a),
   d∈N(c)∩N(e), no chords, then the 5-set verified by the exact
   induced-degree-2 test; divide by 10 (each C5 anchored at its 10 directed
   edges): **384,912** = 243·22·20·18/5. (`code/out/count_C5_bvls_anchored.py`.)

Both entry guards passed (rook = 0). The first anchored attempt over-counted
(1,924,560 undirected, admitting "C4-with-pendant" shapes); the correction was
the exact induced-degree-2 verification of the 5-set. The closed form is now
checked, not merely asserted.

```claim
id: pentagon-count-closed-form-verified
statement: In any srg(v,k,1,2), the number of induced pentagons (C5) is
  p5 = n·k·(k−2)·(k−4)/5. This is parameter-determined (depends only on (n,k)),
  and is verified on both existing family members by exact enumeration:
  rook(3)=0 and BvLS=384,912, both matching the closed form. At the target
  (99,14,1,2) the formula gives p5 = 99·14·12·10/5 = 33,264, so any putative
  99-graph contains EXACTLY 33,264 induced pentagons.
hypotheses: an srg(v,k,1,2) (lambda=1 so induced C5 = cycle C5 with no chord);
  the Reimbayev derivation of the closed form (arXiv 2508.03377 body, in
  library).
holds-here: yes — both controls reproduce the form exactly; at 99 it forces a
  hard count target (33,264) but no contradiction.
status: checked (two independent exact routes, both entry-guarded, on the two
  existing graphs; the 99 value is the closed-form evaluation, an exact
  parameter-determined consequence).
bearing: closes the last GOAL.md-named counting lever (C5) as a fixed
  parameter-determined count with no separating power: the pentagon count
  forces nothing at 99 and does not distinguish 99 from 9 (0) or 243 (384,912).
  Its value is as a verified hard isomorph-rejection / candidate-checker target,
  not as a structural lever. Like the hexagon count and the K4−e degeneracy, it
  is a dead end as a nonexistence route (it survives unchanged on the controls).
anchor: code/out/check_pentagon_formula.py, code/out/count_C5_bvls_anchored.py
follows-from: reimbayev-order-six-subgraph-counts
```
