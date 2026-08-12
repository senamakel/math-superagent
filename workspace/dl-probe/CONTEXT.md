# Shared context

Problem: the Erdős–Gyárfás conjecture (1995) — every graph with minimum degree 3 contains a simple cycle whose length is a power of two. Erdős offered $100 for a proof / $50 for a counterexample. This run is gathering the three named sources; they were already downloaded (see below).

## Established

**Erdős–Gyárfás conjecture** (sourced — [[research/sources/wikipedia-eg.full.md]], digest [[research/summaries/wikipedia-eg.md]]). Open; every δ≥3 graph has a power-of-two cycle. $100/$50 prize.

**Counterexample bounds** (sourced): Royle & Markström computer searches — any counterexample needs ≥17 vertices; any cubic counterexample ≥30; bipartite ≥30 (Nowbandegani–Esfandiari 2011). Markström found four graphs on 24 vertices with the only power-of-two cycles of length 16; exactly one is planar — the **Markström graph** (cubic planar on 24 vertices, lacks C4 and C8, contains C16; a cyclic group graph; GraphData["MarkstroemGraph"]) — [[research/sources/mathworld-markstrom.md]]. So a 24-vertex cubic graph can have only a 16-cycle as its power-of-two cycle, yet the conjecture survives for them.

**Proved restricted classes** (sourced, recalled): 3-connected cubic planar graphs (Heckman–Krakovski, EJC 2013, discharging + computer); P13-free δ≥3 (Hegde–Sandeep–Shashank, arXiv:2410.22842v2, backtracking verify k=3..13); P12-free δ≥3 ⇒ has C4 or C8 (ibid, sharpens Hu–Shen P10 2024 and Gao–Shan P8 2022); planar claw-free (Daniel–Shauger 2001); K1,m-free with min-deg≥m+1 or max-deg≥2m-1 (Shauger 1998); several Cayley families (Ghaffari–Mostaghim 2018); very-sparse avg-deg in iterated log n (Sudakov–Verstraëte 2008). Liu–Montgomery: every graph with large avg degree has a power-of-two cycle — disproved Erdős's later belief the conjecture fails for every min-deg≥3.

**Claw-free case** (sourced — [[research/sources/bibnauki-30148697.full.md]], digest [[research/summaries/bibnauki-30148697.md]]; Salehi–Esfandiari–Shirdareh–Bibak): Hobbs asked whether EG holds in claw-free graphs. Thm 1: every claw-free δ≥3 has a cycle of length 2^k or 3·2^k. Thm 5: claw-free δ≥4 without C4 — every non-cut vertex lies on a power-of-two cycle. Thm 9: any cubic claw-free counterexample needs ≥114 vertices. Cor 7: the cubic↔cubic-claw-free-without-C4 correspondence G↔Ĝ turns a length-k cycle in Ĝ into cycles of all lengths 2k..3k in G.

**Minimal counterexample structure** (recalled, from earlier runs on this problem):
- Markström: G = independent set V1 of degree≥4 vertices + nonempty V2 of degree-3 vertices.
- Carr (arXiv:2605.22844v1): (a) every degree-3 vertex has a degree-3 neighbor; (Cor 0.1) cubic vertices form a dominating set; degree≥4 vertices independent; every regular minimal counterexample is cubic; ≥4/7 of vertices have degree exactly 3; every proper subgraph has δ≤2.
- NOT established: 2-connectedness (Royle's relaxation builds a 1-connected near-counterexample — three min-deg-3 lobes joined to a central vertex, so do NOT assume 2-connected), girth, any bound on distance-2 degree-≥4 pairs. Only independence (distance ≥2) of the degree-≥4 set is known.

## Ruled out

- P_k-free method (Hegde–Sandeep–Shashank) does NOT extend to H-free for cyclic H (infinite min-deg-3 tree is H-free with no power-of-2 cycle) or non-path trees (clique-substitution claw-free example) — so it does not touch the full conjecture.

## Numbers

- Counterexample vertex bounds: ≥17 (general), ≥30 (cubic), ≥30 (bipartite), ≥114 (cubic claw-free).
- Markström: four 24-vertex graphs with only 16-cycles as the power-of-two cycle; one planar; confirmed C16 present, C4/C8 absent.
- Carr: ≥4/7 of a minimal counterexample's vertices have degree exactly 3.

## Recalled

Durable memory from earlier runs on this conjecture (recalled, not this run's own finding): full statement of EG, the restricted-class proofs listed above, and the minimal-counterexample structure attributed to Markström §4 and Carr. The P_k-free details (explore algorithm, github.com/rbsandeep/Erdos-Gyarfas) are in durable memory, not this run's work.

## Contradictions

None recorded. (Note: Hegde–Sandeep–Shashank give bipartite ≥30 same as Nowbandegani–Esfandiari — consistent.)

## Gaps

- Whether any δ≥3 graph lacks all power-of-two cycles — unproved; the three sources here are the input gathering for this run's study, not a proof.
- The full conjecture remains open; the 114 bound is for cubic claw-free counterexamples only.
