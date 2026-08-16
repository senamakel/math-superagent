# Thread: hexagon lower bound (Reimbayev 2024) as a 99-structural lead

```thread
id: thread-hexagon-bound
question: Does the Reimbayev lower bound on the number of hexagons in a
  lambda=1,mu=2 SRG give a route to (99,14,1,2)? Specifically: the number of
  hexagons is conjectured to equal exactly (1/12)*n*k*(k-2)*(2k^2-21k+53), and
  equality is tied (per the paper) to nonexistence; both Paley(9) and BvLS(243)
  attain the bound.
status: redirected
rests-on: research/sources/reimbayev-hexagon-bound-srg-lambda1-mu2.full.md,
  research/sources/reimbayev-hexagon-bound-body.full.md
**Makhnev 1988 RESOLVED** (the thread's original blocker): the conditional
"n_3=0 => no srg(99,14,1,2)" is Makhnev 1988 Thm 2, primary Russian full text
now in library (research/sources/makhnev-1988-lambda1-russian-fulltext.full.md).
Thm 2's 99-proof builds an srg(33,12,1,6) subobject from a triangle's closure +
its 60 exterior points and invokes Thm 1 (mu<=3 or (27,10,1,5)).
blocked-by: first the oracle's count path must be proven on a negative
  (task land-oracle-controls: C9(1,2) at 9 and one 14-regular at 99, rejection
  naming a lambda/mu mismatch, capture in code/out/oracle-controls.captured.txt);
  then an exact hexagon-count oracle on the two control graphs (count C6 exactly
  over the integer adjacency matrix) to confirm both attain the bound; then check
  what the bound predicts for n=99,k=14 and whether attaining/not-attaining is
  consistent with the 243 control surviving.
  If the bound forces the 99 case into the 'attained ⇒ nonexist' branch, it is
  a genuine structural lead; if 243 also sits in that branch, it is another
  eigenvalue/counting route that (like integrality) survives on the controls
  and is refuted on arrival.
granted: the full text is now in the library
  (research/sources/reimbayev-hexagon-bound-body.full.md), not merely the
  abstract. It pins the whole order-6 structure on the single parameter n_3
  (pairs of triangles sharing an edge / two triangles joined by two edges):
  all order<=5 subgraph counts are determined by (n,k); all 62 order-6 counts
  by (n,k) + n_3. The paper asserts n_3=0 would (via Makhnev 1988) rule out 99.
  See the Reimbayev order-six summary for the complete formulas and the
  shpectorov-zhao 85 summary for the successful local-enumeration analogue.
  Note one concrete defensible partial result now derivable: for the two
  existing graphs the run's oracle can independently verify the closed forms
  and pin n_3 = (observed count of edge-sharing triangle pairs).
next: build the exact C6 counter for the rook's graph and BvLS, compute the
  bound's value at n=99,k=14, and check the paper's claimed implications.
```

**COMPUTED** (tool_builder): the exact induced-C6 count for the BvLS control is
measured and confirmed. lib/hexagons.count_induced_C6 (P4-anchored, O(n^4))
on lib.srg.bvls_graph() gives 4,980,690 in 116.5s, EXACTLY the closed form
(1/12)*243*22*20*559. An independent directed-edge-anchored counter
(code/out/verify_hexagons_edge_anchor.py, O(n^5)) gives directed 59,768,280
= 12*4,980,690, confirming by a second route. Both are validated against brute
force on rook(3)=6, a bare C6=1, and two triangles=0.

Bearing: (a) the 243 control ATTAINS the Reimbayev hexagon bound, consistent
with the thread's expectation and with c4/c5 controls surviving. (b) Any
candidate 99-structural argument that counts induced hexagons now has a hard
measured target: formula(99,14) = 209,286, and the method (lib/hexagons) will
verify or refute any candidate graph against it, just as it did for 243.
(c) Because 243 attains the bound, the bound's equality branch does NOT by
itself predicate nonexistence — a fact the 99 argument must confront, exactly
the "does 243 also sit in that branch" test the thread names. The n_3=0
route (Makhnev 1988 Thm 2 ⇒ no 99) remains the live structural question the
hexagon count feeds; the next step is to pin n_3 for both controls from the
measured counts.

The trap to remember (from the Bagchi episode): any hexagon-counting argument
that would rule out 99 must first be run against 9 and 243 — if it also "rules
out" the existing BvLS (243,22,1,2), it proves a false statement and is wrong.
The Reimbayev paper claims both controls attain the bound, so the interesting
question is whether the bound's *equality branch* genuinely excludes 99 while
only "excluding" 243 in a way the 243 graph actually attains (i.e. the branch
is consistent, equality is possible and attained — then it predicates nothing
contradictory). This is exactly the kind of claim the oracle must test.

**Parked as a standalone nonexistence route (directive 5); REDIRECTED, not dead.**
The hexagon identity is confirmed and its role clarified:
```
n_12 = (1/12) n k (k-2)(2k^2-21k+53) + n_3   is an IDENTITY (checked on both controls)
```
Both existing members have n_3 = 0 (checked, exact: rook(3) n_3=0, bvls n_3=0), so
**n_3=0 is family-realizable** and the pure C6 count cannot distinguish 99 from the
controls: at k=14 the base count is 209286 + n_3, and n_3 is a free shift. The
hexagon bound alone cannot conclude anything about 99. The count *combined with the
Makhnev (*) conditional* is the live content: Makhnev 1988 Thm 2 (primary Russian
full text in library) = "no srg(99,14,1,2) satisfies (*) = n_3=0". So the real
question is whether n_3 >= 1 is forced at 99, not the C6 count itself. The two
controls are the n_3=0 witnesses any forcing argument must fail on. See the open
task row `n3-forced-question`.
