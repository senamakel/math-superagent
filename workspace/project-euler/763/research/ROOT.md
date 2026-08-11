# research — what this now establishes

Top of the tree. Batches of originals in `L0.<n>/`; seal a level up. What the
whole library lets this run treat as known, each claim wikilinked to its note.

## The 2D chessboard-pebbling problem is fully characterised (and is the 2D amoeba)

The 2D amoeba sequence IS OEIS A007902 (pebbling configurations), and the
literature now supplies its exact structure:
- [[amoeba2d_pebbling_a007902]] — 2D amoeba = pebbling = A007902, with the
  exact G(k,m) recurrence (CGMO eqs 2.1-2.3) and asymptotics d=2.3216, c=0.1227.
- [[pebbling_structure_3d_ladder]] — the *precise structural characterization*:
  reachable 2D positions = **polyominoids** (set between two lattice paths),
  bijectively = **voidance sets** (Eriksson Prop 20); 2D is hard because of
  **crossings** (cells played twice), giving the marked-crossing GF g(x) with
  growth 4.112. For the 3D PE763 process the result is decisive: in n≥3 no
  cell is ever played twice (Eriksson Prop 24), so positions ⇄ voidance sets ⇄
  **folded polyominoids** coincide (Eriksson Theorem 9); PE763 is exactly
  Eriksson/Vaderlind's n=3 pebbling game.
- [[pebbling_ejc_survey]] (Eriksson, EJC 2 (1995) #R7) — the primary structural
  source: polyominoids, crossings, folded polyominoids, Theorem 9, Fig.3 table,
  weight invariant n^{-(x_1+…+x_n)}.
- [[cgmo_opening_dijkstra]] — CGMO "Pebbling a chessboard" (AMM 102 (1995)),
  opening transcribed verbatim: weight invariant, unavoidable sets, Lemmas 1-3,
  Theorem 1 (level-trimming = "3-pebble-point" criterion).
- [[pebbling_knessl_pdf]] — Zhen & Knessl arXiv:1009.5731: exact 2D contour
  formula + the G(k,m) recurrence + asymptotics (z*=0.4307, a=2.3216).

Net for the goal: the 3D D(N) is a *folded-polyominoid* reachable-position
count (Eriksson n=3), not a random directed-animal count; the 2D genus has
no closed form (only recurrence + asymptotics) and all the 2D-specific crossing
machinery drops out in 3D. Literature does not hand over the numeric 3D
D(10000) — that must come from the run's own structure (folded-polyominoid /
level-histogram DP), but the correct counting object is now named and sourced.

## Negative results retained (do not re-search)

- 3D D(N) has no OEIS entry (direct queries: "No results") — no catalogued
  closed form. [[amoeba_seq_oeis]], [[oeis_lookup_2d_3d]].
- 3D D(N) is not Motzkin/Fibonacci-family (A001006, A005207, A086246, A168049).
- 2D reachable count ≠ directed-animal count (A005773) although heads agree;
  the true 2D object is A007902.

## Sources of evidence
Every theorem above is sourced with a URL in the named notes; none is invented.
The G(k,m) recurrence and the reverse-merge/folded-polyominoid picture on small
N are cross-checked against the run's own BFS (see code/amoeba2d/).
Deliberately NOT consulted: any Project Euler 763 solution/forum thread.
