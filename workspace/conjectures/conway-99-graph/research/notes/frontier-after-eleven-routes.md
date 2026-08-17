# Frontier after eleven closed routes — what is actually left

Status of `srg(99,14,1,2)` at close of attempt 2. This states plainly what
remains, so a next pass does not open a twelfth route against an obstruction
already named.

## The one live lever

**Global closure of the n3 >= 1 seed.** n3 > 0 is forced at 99 (Makhnev 1988
Thm 2, re-derived and controls-passed). Take the n3 configuration — two disjoint
triangles joined by exactly two edges — whose local closure is a radius-6
fixpoint with 19 survivors on 8–12 vertices and zero free interior bits. The
only place an obstruction can live is whether the outside 87–91 vertices can be
joined to satisfy μ=2 and degree-14 simultaneously for every boundary pair.

The **6-vertex condition over the n3 type** (approach `6vertex-condition-obstruction`,
adopted) is the cleanest home of this lever, and it is **control-immune by
construction**: both controls rook(3)=srg(9,4,1,2) and BvLS(243)=srg(243,22,1,2)
are rank-3 / vertex-transitive and satisfy every t-vertex condition trivially,
while 99 is provably not vertex-transitive. An obstruction there is 99-specific
and cannot be refuted by the 9/243 test. The n3-type 6-vc embedding count is 0
at both controls (they have n3=0) — so the stated limit of the existing control
is that it needs a positive n3>0 witness, which no in-family μ=2 SRG provides,
or the hypothetical 99 geometry itself.

## The a=7 specificity requirement

Any valid nonexistence argument must break at `a = √(4k−7) = 2u+1` with u=3
(a=7, k=14) but survive at u=1 (a=3, k=4) and u=4 (a=9, k=22). An argument that
works at all three values, or that is a pure function of (n,k,1,2), is
parameter-determined and refuted on arrival.

## What is closed, and by what (eleven routes, solution.md §2)

1. Eigenvalue-only routes (integrality, Krein, absolute bound, interlacing) —
   survive unchanged on 9 and 243.
2. Bagchi / Brouwer–Neumaier μ=2 dichotomy — "grid" branch needs k<6, false at
   k=14.
3. Order-6 / n3 count identities and hexagon counts — n3-agnostic, admit n3=0
   at every family member.
4. g-reduce recursion — the outer derived design is not itself an srg on BvLS.
5. Coclique-design contradiction at 99 — the forced super-simple 2-(22,4,2)
   design exists.
6. Local obstructions at all radii — n3 seed extends; radius-6 fixed point,
   no local kill.
7. Global incidence counting floor — arithmetically absorbable for all 19
   survivors; ruled out.
8. Incidence p-rank / SNF — circular / unmeasurable without the very graph.
9. Regular two-graph descendant — fails k=2μ arithmetic at 99 and 243.
10. (six-vertex / Pech import) — corrected: the 6-vc family Pech proves is
    PQ(q−1,q²,q²−q)=(81,20,1,6), NOT PQ(2,6,2); must be computed, not imported.
11. Orbit-matrix programme — closed by **computational infeasibility, NOT
    mathematics** (below).

## Route 11's exact boundary (measurement, not judgement)

From the live order-3 CP-SAT heartbeat (research/notes/orbit-order3-infeasibility-boundary.md),
independently re-verified exactly in `code/out/route11_boundary_final_verify.py`
/ `.captured.txt`:

- Model at m=33: **41,745 variables, 57,165 constraints**.
- 15 vars fixed at 694.32 s, 33 at 1889.85 s → 18 vars in 1195.53 s =
  **39851/600 s/var ≈ 66.42 s**.
- Presolve-only extrapolation to all 41,745 vars = 110905333/40 s ≈ **32.09
  days**.
- Order-3 fixed-point-free automorphism: 99/3 = **33** point-orbits.
- Order-2 (odd f fixed points): (99+f)/2 ∈ **[50,99]**, all > 33 → the order-2
  orbit matrix is strictly larger, strictly worse.

**What route 11 does NOT establish:** no order-3 or order-2 automorphism is
excluded. The published Aut reduction to {Z2, Z3} stands untouched; Aut(99)
remains open. The route is closed because the CP-SAT encoding at this presolve
rate cannot reach a verdict, not because of any graph-theoretic obstruction. A
*different* encoder, solver, or structural (non-41,745-variable-search) orbit
argument remains open.

## What a next pass should NOT repeat

- The orbit-matrix programme in CP-SAT (route 11).
- Local-radius growth (exhausted, fixed point).
- Radius-2 CP-SAT setups generally (burned two specialists for zero artifacts).
- Reproducing Makhnev's Thm-1 route (the shorter integrality re-derivation
  lands the same n3>=1).
- Any parameter-determined count as a lever (all closed, list above).
