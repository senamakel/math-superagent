# Goal — state at end of attempt 2

Attack Conway's 99-graph problem (`problem.md`): the existence of `srg(99,14,1,2)`.
This remains an OPEN problem; the deliverable is exact partial results with a
named failing step on the controls, never a claim of the whole.

## What attempt 2 established (all checked unless marked)

1. **Oracle proven, count path exercised.** `code/lib/srg.py::is_srg` now classifies
   λ vs μ count failures separately. Count-path negatives land in
   `code/out/oracle-controls.captured.txt`: C9(1,2) (4-regular, 9 vtx, not rook)
   fails (9,4,1,2) citing "LAMBDA wrong on 18 adjacent pairs, MU wrong on 18
   non-adjacent pairs"; circulant(99,{1..7}) fails (99,14,1,2) citing counts.
   rook(3) PASS, bvls(243) PASS with 2673 edges. `sys.path.insert` removed.
   Claims c4/c5 are `checked`.

2. **G-reduce part (c) REFUTED on BvLS (checked negative).** The outer partial
   STS's collinearity graph has λ=1 but μ ∈ {0:330, 1:11880, 2:9900} — not an
   srg(*,*,1,2). Parts (a),(b) hold on both controls. The reduction does NOT
   recurse. `code/out/g_reduce_control.captured.txt`.

3. **Hexagon/n3 line redirected, not dead.** n12 = (1/12)nk(k-2)(2k²-21k+53) + n3
   is an identity (checked on both controls); both controls have n3=0 (checked).
   At k=14 base count = 209286 + n3; n3 is a free shift, so the C6 count alone
   cannot distinguish 99. Makhnev-type-2 conditional makes n3 the crux.

4. **Makhnev 1988 Thm 2 gate PASSED (checked).** Primary Russian full text in
   library; condition (*) = n3=0; Thm2 = no (99,14,1,2) with (*). Both controls
   satisfy (*) with n3=0 (μ=2≤3, absorbed by Thm1 branch), so the conditional
   is consistent with the existing members. `code/out/makhnev-1988-condition-captured.txt`.

5. **Order-6 counting does NOT force n3≥1 at 99 (checked).** All 62 Reimbayev
   order-6 counts admit n3=0 at every family member (n3≡0 mod 3, interval
   [0,4158] at k=14). So n3=0 is arithmetically consistent and family-realizable;
   a forcing argument needs k=14-specific geometry.

## The open lever for phase 4

**Is n3 ≥ 1 forced for a putative (99,14,1,2)?** n3 = number of disjoint triangle
pairs joined by exactly two edges. Makhnev Thm2 gives: n3=0 ⇒ nonexistence
(sourced, controls pass). Both controls have n3=0 and EXIST, so any argument
forcing n3≥1 (or n3=0) at 99 must fail on 9 and 243; any forcing must be
k=14-specific, since the order-6 identities are n3-agnostic in the family sense.
A construction with n3=0 would refute the Makhnev conditional's consequence only
if it built a real 99-graph (impossible if Thm2 is sound); a construction with
n3≥1 is consistent with existence. The next attack should be a k=14 local
geometric constraint on the triangle geometry (partial STS, 99 pts / 231 lines /
7 per point) that no order-6 identity captures.

## Completion test (unchanged from original GOAL)

No nonexistence argument is admissible until it is run against rook(3) and
bvls_graph() through `code/lib.srg.is_srg` and the step that breaks on them is
named. The oracle now satisfies that gate for its own correctness.
