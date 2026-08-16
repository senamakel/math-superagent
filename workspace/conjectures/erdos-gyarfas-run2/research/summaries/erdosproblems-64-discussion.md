# Erdős Problems #64 — discussion thread

Source: https://www.erdosproblems.com/forum/thread/64 (T. Bloom, ed.)
Full text: [[erdosproblems-64-discussion.full]] (`research/sources/erdosproblems-64-discussion.full.md`).

## What this page fixes

The canonical open-problem page; prize $1000 (site), not the $100/$50 of West's
older page. Conjectured by Erdős–Gyárfás, who **believed the answer negative** —
for every r a min-degree-r graph with no 2^k cycle. That stronger belief was
**disproved** by Liu–Montgomery (large average degree ⟹ 2^k cycle, in fact all
even lengths in [(log ℓ)^8, ℓ]). Infinite min-degree-3 tree shows failure for
infinite graphs. Formalised statement exists (DeepMind formal-conjectures /64.lean).

## Alfaiz's list of confirmed families (06 Dec 2025)

The most complete published list of settled restricted classes, each with its
exact hypothesis:

(i) K1,m-free with minimum degree ≥ m+1 OR maximum degree ≥ 2m−1 (Shauger
    Sh98, Congr. Numer. 134 (1998) 61–65).
(ii) Planar claw-free graphs (Daniel–Shauger DaSh01).
(iii) 3-connected cubic planar graphs (Heckman–Krakovski HeKr13).
(iv) Cayley graphs on generalized quaternion, dihedral, semidihedral, order-p^3
     groups (Ghaffari–Mostaghim GhMo18).
(v) Cayley graphs of order 2p^2 and 4p (Ghasemi–Varmazyar GhVa21) — NEW to this
     library's holdings.
(vi) P8-free graphs (Gao–Shan GaSh22). [held]
(vii) P10-free graphs (Hu–Shen HuSh24). [held]
(viii) Diameter-2 graphs (Carr Ca26). [held]

Lower bounds:
(I) any cubic counterexample ≥ 30 vertices (Markström Ma04). [held]
(ii) any bipartite counterexample ≥ 32 vertices (Nowbandegani–Esfandiari
     NoEs11). [partly held]
(iii) cubic claw-free counterexample ≥ 114 vertices; and every claw-free δ≥3
      graph has a 2^k or 3·2^k cycle (NEHB14, arXiv:1109.5398) — the 3·2^k
      weakening is NEW to holdings.
(iv) minimal counterexample: every vertex adjacent to a deg-3 vertex, ≥ 4/7 of
     vertices degree exactly 3 (Carr Ca26b). [held]

## New unverified claim (26 Jul 2026, user jul059 — NOT verified, marked as such)

A claimed improvement building on Carr: in a minimal counterexample,
|V3| ≥ 2|V≥4| + 1, hence |V3| > 2/3 |V(G)| (up from Carr's 4/7). The argument:
Carr gives V≥4 independent, every vertex adjacent to a deg-3 vertex ⟹ every edge
incident to V≥4 joins V≥4 to V3 and each V3 vertex has at most two V≥4 neighbours,
so 4|V≥4| ≤ e(V≥4,V3) ≤ 2|V3|, i.e. |V3| ≥ 2|V≥4|. To rule out equality: if
|V3| = 2|V≥4| all equalities hold, so each V≥4 has degree exactly 4 and each V3
has exactly two V≥4 neighbours. Form H on V≥4 replacing each V3 vertex u_x with
edge u_x v_x (simple: two V3 with same pair would give a 4-cycle). Every H-vertex
has degree 4, H is smaller than G, so H has a 2^k-cycle by minimality; replacing
each H-edge by its 2-edge V3-path gives a 2^{k+1}-cycle in G — contradiction.

```claim
id: ce-2-3-degree-fraction
statement: In a minimal counterexample |V3| ≥ 2|V≥4| + 1, hence strictly more than 2/3 of vertices have degree exactly 3 (improving Carr's 4/7).
hypotheses: G a vertex-minimal, then edge-minimal counterexample to Erdos-Gyarfas; V3 = deg-3 vertices, V≥4 = deg-≥4 vertices
holds-here: yes (improves the live near-cubic thread ce-principality-carr)
status: asserted (forum comment, explicitly "not verified", found by an AI tool)
bearing: if correct, tightens the minimal-counterexample degree spine the run's live thread attacks; BUT it is a forum post, not a checked source — MUST be attacked/verified before reliance.
anchor: research/sources/erdosproblems-64-discussion.full.md
```

## For this problem

The single most useful addition is (v) Ghasemi–Varmazyar (Cayley graphs of order
2p^2 and 4p) and (iii) the NEHB14 3·2^k weakening — both are confirmed-family
results not previously in the holdings, extending the "settled classes" list
ROOT.md must state. The 2/3 claim is a live, unverified lead for the structural
thread. The Alfaiz list is cross-checks the library's existing partial results.
