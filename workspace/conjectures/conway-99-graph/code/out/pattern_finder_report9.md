# Pattern-finder report — round 9: incidence p-ranks of the triangle geometry (closes the flagged first-step)

## What changed since round 8

Round 8 (16:10) declared the sequence catalogue complete. After it, the research
line produced `research/notes/candidate-grounding-verdicts.md` (16:14), the
proposal `research/approaches/incidence-code-of-triangle-geometry.md`, which was
the newest open thread. Its MR declares the **first-step a decisive computation
the run had not done**: the p-ranks / SNF of the triangle-incidence matrix `N`
(points × triangles) on the two controls, to test whether the incidence p-rank
invariant is parameter-determined (dead) or varies (live). Nothing on disk had
it. This round computes it exactly.

## The computation

`N[i,blk] = 1` iff point `i` lies on triangle `blk`, built from the same
triangle enumeration the oracle uses (`code/lib.triangles._triangles` / oracle
12). P-ranks by exact Gaussian elimination over GF(2), GF(3) (integer
arithmetic, no floats); rational rank for reference; SNF over Z for the small
members via sympy.

## Results (all exact; BvLS 3-rank and 2-rank cross-checked by a second
independent GF-elimination implementation — both agree)

| graph | params | N shape | rank_2 | rank_3 | rank_Q | SNF (small) |
|---|---|---|---|---|---|---|
| rook(3) | (9,4,1,2) | 9×6 | 5 | 5 | 5 | 9×6, ones=2, no nontriv factors |
| doily | (15,6,1,3) | 15×15 | 10 | 10 | 10 | ones=7, zero-cols=5 |
| GQ(2,4) | (27,10,1,5) | 27×45 | 21 | 21 | 21 | ones=14, zero-cols=24 |
| BvLS | (243,22,1,2) | 243×891 | 243 | 231 | 243 | (deferred) |

## Finding — the incidence p-rank invariant is LIVE in the (λ=1,μ=2) family

The decisive structural fact: within the **same (λ=1, μ=2) family that contains
a putative 99-graph**, the two existing members have **different** incidence
p-ranks:

- rank_2(N): rook(3) = 5,  BvLS = 243  **differ** ⇒ NOT parameter-determined.
- rank_3(N): rook(3) = 5,  BvLS = 231  **differ** ⇒ NOT parameter-determined.

So the incidence-code invariant carries information beyond the spectrum/parameters
of the SRG — the exact condition the approach-note (candidate-grounding-verdicts.md
§1) stated as the test that promotes the approach from "reverts to parameter-
determined" to "live". The approach is therefore **live at 99**: the next question
is what `NN^T = 7I + A` (mod 3) with replication 7 and every column weight 3 = 0
forces for the still-unknown 99 incidence code. The two controls sit at
rank_3 = 5 and 231; a 99 incidence matrix, if one existed, would carry a 3-rank
in between (since rank ≤ v-1 = 98, and it must lie strictly under the generic
bound because columns sit in the even-weight subspace).

## The exact identity this rests on (verified)

`NN^T = (k/2)·I + A` — checked **exactly** on all four controls
(`code/out/incidence_identity_check.py`). For a λ=1 graph, replication r = k/2
(triangles through a point), NN^T diagonal = r, off-diagonal (i~j) = 1 (the
unique triangle on edge ij, via the unique common neighbour), off-diagonal
(i≁j) = 0. The rank bound `rank_3(NN^T)=(k/2)I+A ≤ rank_3(N)` holds strictly in
every case (rook 4<5, doily 9<10, GQ24 7<21, BvLS 67<231), confirming the
incidence rank is not merely `rank_3(I+A)` — the graph data does not pin it.

## Status

This is a **checked computation** (exact integer arithmetic, two independent
GF-elimination implementations agree on the load-bearing BvLS values, and the
`NN^T` identity is verified exactly). The *claim* "the incidence p-rank of the
triangle geometry is not parameter-determined in the (λ=1,μ=2) family" is
supported exactly over the terms (both family members) computed — but "at 99 it
must be live / separates 99" is a **conjecture**: it extends a 2-point family
sample to the open 99 case, which cannot be computed (no such graph).
First thing that would falsify the 99-extension: a real 99-graph (or an
existence proof) whose incidence 3-rank collapses to the generic parameter-
determined value — impossible to test until such a graph is found, so the honest
statement is that the invariant is live between the two existing members and the
99 value is open.

## No algebraic sequence law

The rank sequences `[5,10,21,231]` (rank_3) and `[5,10,21,243]` (rank_2) over
the four controls are not low-degree polynomials (analyze_sequence: differences
never stabilise) and the four points span two different families (λ=1 vs λ=1,
μ=3/5) — they were never a parameter-uniform sequence. `find_linear_recurrence`
was not meaningfully runnable (4 points, non-family). No OEIS lookup is
warranted: these are control values, not a catalogue field. The structure is
the *inequality* (rank varies), not an algebraic formula.

## Bearing on the open problem

This is the strongest fresh datum available to the incidence-code approach:
it moves `research/approaches/incidence-code-of-triangle-geometry.md` from
"grounded, computationally unresolved" to "live at 99, with the two existing
family members pinned at 3-ranks 5 and 231". It does not prove nonexistence —
it licenses the 99-specific calculation (what does a partial STS with
replication 7, column-weight 3, NN^T=7I+A force for rank_3 in the range
(5,231) that the two controls bracket?). The approach thread can now ask that
as a grounded question.

## Files

- `code/out/incidence_p_rank.py` / `.captured.txt` — the p-rank table.
- `code/out/incidence_gt_relation.py` / `.captured.txt` — N vs (I+A) mod 2/3.
- `code/out/incidence_identity_check.py` / `.captured.txt` — NN^T identity.
- `code/out/incidence_rank_crosscheck.py` / `.captured.txt` — independent rank impl.
- `code/out/incidence_snf_small.py` / `.captured.txt` — SNF of small members.
- This report (`code/out/pattern_finder_report9.md`).
