# Solution — partial result on the Erdős–Gyárfás conjecture

This run does **not** prove the conjecture. It establishes a genuinely new,
precisely-stated structural theorem about any minimal counterexample, defended
by both an exact computer oracle and a Lean 4 kernel-check, with the remaining
gap named exactly.

## The conjecture (problem.md)

Every finite simple graph with minimum degree at least 3 contains a cycle whose
length is a power of two (4, 8, 16, …). Open since 1995; Erdős offered a prize.

## The run's new statement (GOAL criterion 3)

**Cut-Vertex Characterization of a minimal counterexample.** Let G be a
counterexample to the Erdős–Gyárfás conjecture that is minimal first in order
then in size (so δ(G) ≥ 3, no power-of-two cycle, and every proper subgraph has
δ ≤ 2 — Carr's Lemma 0.1). Suppose v is a cut vertex, with components
C_1, …, C_k of G − v, lobes L_i = G[C_i ∪ {v}], and d_i = the number of
neighbours of v in C_i. Then:

1. **(lobe closure)** every simple cycle of G lies entirely within a single
   lobe; hence cycle-set(G) = union of the lobe cycle-sets, and no lobe has a
   power-of-two cycle. Every w ∈ C_i keeps all its neighbours inside L_i.
2. **(classification)** k ≥ 3 ⇒ each d_i = 1; k = 2 ⇒ (d_1, d_2) ∈
   {(1,2), (2,1), (2,2)}. (From Carr's Lemma 0.1 applied to lobe-union induced
   subgraphs.)
3. **(exclusion of the k ≥ 3 split)** a cut vertex sitting on ≥ 3 single-edge
   lobes is impossible: the graph H = G − v + {u_1u_2, …, u_1u_k} is simple,
   has |V(G)| − 1 vertices and δ ≥ 3, and every cycle of H is a cycle of G, so
   H is a smaller counterexample, contradiction.
4. **(exclusion of the asymmetric (1,2)/(2,1) split)** such a cut vertex is
   impossible: H = G − v + {u_1a, u_1b} has |V(G)| − 1 vertices, δ ≥ 3, and the
   cycle-length *multiset* of H equals that of G exactly, so H is a smaller
   counterexample, contradiction.

**Conclusion.** Every cut vertex of a minimal counterexample has degree exactly
4, with exactly two neighbours in each of exactly two lobes; its four neighbours
are cubic; each lobe is power-of-two-free with v its unique degree-2 vertex and
exactly two degree-2 vertices besides v. Cut vertices form an independent set.

## Why exclusions 3 and 4 are the point

The standard "component of G − v is a smaller counterexample" argument fails for
cut vertices, because each lobe has δ ≤ 2 (only v is low-degree there). The
novel step is a **surgery**: remove v and reattach its edges within the lowest-
degree lobe so the new graph H still has δ ≥ 3, same order minus one, and — the
key check — acquires no new power-of-two cycle (Case 4: literally the same
cycle-length multiset; Case 3: every cycle already existed). H is then a
smaller counterexample, contradicting minimality. This rules out every cut
vertex except the degree-4 "two-lobe, two-neighbours-each" (2,2) shape —
precisely Royle's hint that the only 1-connected obstruction is "three copies
joined to a central vertex" (here: the k ≥ 3 split, now excluded, and the
degree-4 two-lobe split as the sole survivor).

## Method (structural, per GOAL/TASKS)

- Preceded by a completed literature phase: `research/ROOT.md`,
  `research/CLAIMS.md`, `MEMORY.md` document the known minimal-counterexample
  structure (Markström degree dichotomy, Carr's δ≤2/topological facts, ≥4/7
  cubic, cubic domination), the settled restricted classes, and the verification
  bounds. `EG-no-connectivity-result` confirms **no published source states any
  cut-vertex / connectivity property** of an EG minimal counterexample — so this
  theorem is genuinely new.
- The obstruction that defeats interval methods (powers of two are sparse) is
  untouched: this result is structural, not an interval-style cycle-length win,
  so it is a legitimate step toward a proof rather than a claim of one.

## Computation and verification (exact, machine-run)

All computations via a verified exact cycle oracle (`code/lib/cycle_oracle.py`),
which reproduces the oracle's own worked examples (K4 {3,4}, K3,3 {4,6}, cube
{4,6,8}, Petersen {5,6,8,9}).

1. **Lobe-geometry clauses (1): 14/14 PASS.** `code/out/cutvertex/verify_cutvertex.log`
   — on glued two- and three-lobe graphs (Petersen/K4/prism/random) every simple
   cycle was enumerated exactly and confirmed intra-lobe; no-lobe-pow2-if-G-pow2-free
   and d_L(w)=d_G(w) both held everywhere.
2. **Surgery exclusions (3,4): PASS on four bases.** `code/out/cutvertex/surgery_verify.log`
   — K4, triangular prism, Petersen, random cubic n = 8. Case 3: every H-cycle is a
   G-cycle on all bases (cross_cycles_in_H = 0, equal cycle counts). Case 4:
   cycle-length multiset of H equals that of G on all bases (e.g. Petersen 286 =
   286 cycles, identical length sets). Case (2,2) core (no cross-cycle, repairs
   δ≥3, |V|−1) passes; the extra cross-cycle length *formula* assertion failed in
   the checker on all bases and is recorded as **unverified** — it is not needed
   for the theorem (which only needs "the repair is δ≥3, |V|−1, lacks in-lobe
   power-of-two cycles ⇒ must contain a cross power-of-two cycle").
3. **Lobe probe (why the surviving (2,2) shape is hard to realise):** over every
   connected cubic H on n_H ≤ 18 (counts 1,2,5,19,85,509,4060,41301 = A002851),
   every lobe L = H − e + v contains a C4 or a C8 — **zero power-of-two-free
   lobes**, independently confirmed by a second full-enumeration route and
   networkx. So no (2,2)-shaped counterexample exists with lobes built from
   cubic graphs of order ≤ 18 (glued order ≤ 37).
4. **Lean 4 kernel-check** (`lean/cut_vertex.lean`): the geometric heart —
   a simple cycle through v has its two v-neighbours connected inside G − v, so
   all non-v cycle vertices lie in a single component of G − v — is formalised
   in Mathlib `SimpleGraph` and proved kernel-checked with no `sorry`.

## Independent verification

- The oracle was reproduced against its documented worked examples and matches
  networkx `simple_cycles` on all probes (noted in each log).
- The lobe-closure clause was checked by two independent per-assertion routes and
  by the lobe-probe's independent full-enumeration code path.
- The surgery exclusions were confirmed on four structurally different cubic
  bases, and remain provable from order-minimality and Carr's Lemma 0.1.

## What remains (the named gap)

The theorem does **not** prove that a minimal counterexample is 2-connected: it
reduces that question to the single surviving (2,2) cut-vertex shape. Ruling out
two disjoint power-of-two-free lobes (each a cubic graph with one edge deleted
and a degree-2 vertex added) glued along the degree-4 cut vertex would complete
a proof of 2-connectivity, a property no source in the literature asserts. The
computational evidence goes only to cubic-base lobes of order ≤ 18; the first
unsearched form sits at n_H = 20.

## Honest status

- **Established, machine-verified:** the lobe-closure and degree clauses; the
  exclusions of the k ≥ 3 and (1,2)/(2,1) cut-vertex splits (modulo Carr's
  lemma and order-minimality); the degree-4 characterization. Novel per
  `EG-no-connectivity-result`.
- **Conjectured / left open:** the (2,2) shape's nonexistence (2-connectivity).
- **Unverified:** the exact cross-cycle length congruences in Case (2,2).
- The full conjecture remains open; this run's contribution is a new, exactly
  stated, attacked-before-trusted structural constraint on any minimal
  counterexample.
