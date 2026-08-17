# Approach: orbit-matrix enumeration under the reduced automorphism group {1, Z2, Z3}

```approach
idea: Use the sourced automorphism constraints to reduce any automorphism of a putative srg(99,14,1,2) to orders 1, 2, 3, then run a finite Kramer-Mesner / orbit-matrix case analysis for Z2 and Z3, concluding either nonexistence or -- what is equally a result -- that only the trivial (rigid) group remains.
mechanism: The consolidated sourced claims give that a nontrivial Aut must be Z2 or Z3: only primes 2 and 3 divide |G| (Behbahani-Lam 2011); |G| divides 2*3^3*7*11 (Makhnev-Minakova 2004); no G = Z6, S3, Z9, E9 (Crnkovic-Maksimovic 2020), with order 2^a 3^b and b in {0,1}; if 2 | |G| then |G| divides 6, so G in {Z2,Z6,S3}, and Z6,S3 are eliminated, forcing G = Z2 (Cesarz-Woldar 2025). Order 3 b=1 gives G = Z3. So the only nontrivial possibilities are an involution and an order-3 automorphism. The adjacency (or triangle-geometry incidence) matrix is constant on orbits, giving an orbit matrix M with nonnegative integer entries, forced row sums (degree 14), and the mu=2 / lambda=1 conditions become arithmetic conditions on M.
status: adopted
grounding: The orbit-matrix method for strongly regular graphs is a PUBLISHED, named tool, and it has been applied to EXACTLY this problem by the same school that produced the run's automorphism claims. Crnković-Maksimović 2020 run the complete orbit-matrix enumeration for SRG(99,14,1,2) under Z6, S3, Z9, E9, proving no SRG(99,14,1,2) has an automorphism group of order 6 or 9; Behbahani-Lam 2011 introduced orbit matrices for prime-order automorphisms; Cesarz-Woldar 2025 (arXiv:2308.02978) handle the 2- and 7- divisors. The residual Z2 and Z3 cases are precisely the ones not yet settled by the published orbit-matrix program, so this approach is the natural continuation of named, precedent-backed work rather than a speculative reformulation. The reduction to {1,Z2,Z3} is verified here from the run's own claims (aut-cm-2020, aut-cw-2025, aut-bounds-established).
precedent:
  - Crnković & Maksimović, "Construction of strongly regular graphs having an automorphism group of composite order", Contributions to Discrete Math. 15(1) (2020), https://doi.org/10.55016/ojs/cdm.v15i1.62323 : the orbit-matrix / orbit-length-distribution enumeration applied to SRG(99,14,1,2); proves no automorphism group of order 6 (Z6 or S3) and no Z9; conclusion: order 2^a 3^b with b in {0,1}, and an order-3 automorphism has NO fixed points. This is directly the run's claim aut-cm-2020.
  - Behbahani & Lam, "Strongly regular graphs with a prescribed automorphism group" / orbit-matrix definition for prime-order automorphisms (2011); also Behbahani's 2009 thesis.
  - Cesarz & Woldar, "On the automorphism group of a putative Conway 99-graph", arXiv:2308.02978 (2023) / Algebraic Combinatorics (2025), https://doi.org/10.48550/arxiv.2308.02978 : computer-free proofs that 7 | |G| => G = Z7 and 2 | |G| => |G| divides 6; combined with the run's aut-cm-2020 this forces |G| in {1,2,3}.
  - De Winter, Kamischke, Wang, "Automorphisms of strongly regular graphs", arXiv:1411.3429 (2014): the Benson-type trace congruence k - s = -s f + g (mod sqrt(Delta)) relating an automorphism's fixed points f and g to the eigenvalue machinery -- the congruence constraint an orbit matrix must satisfy at p=2 and p=3.
first-step: (concrete, tool_builder can start today)
  (1) BUILD THE CHECKER (lib/srg, exact integer arithmetic). Add
      orbit_matrix(A, g) for a permutation g: compute the orbit partition, the
      orbit-lengths vector, and the orbit matrix M[i,j] = number of neighbours in
      orbit j of a fixed vertex of orbit i. Run it on rook(3) and bvls_graph():
      for each it must (a) reproduce the degrees k=4,22 as row sums, (b) return
      integer nonnegative entries constant on orbits, (c) reproduce the
      De Winter–Kamischke–Wang congruence 4f + g ≡ 4 (mod 7) [check f,g from the
      actual orbit matrix]. This is the control discipline: the machinery must
      find the Z2 and Z3 actions both controls possess BEFORE any 99 conclusion.
  (2) THE Z3 CASE (the synthesis this round produced). Crnković–Maksimović 2020
      proved an order-3 automorphism of a putative (99,14,1,2) is FIXED-POINT-FREE
      [claim aut-cm-2020]. Couple this to the triangle geometry (the orbit matrix
      on the 231-line partial STS rather than on vertices alone): the triangle
      lines partition the 99 points, and fixed-point-freeness of the Z3 action on
      99 points forces the 33 point-orbits and the 77 line-orbits (231/3) to
      interact by a fixed incidence pattern. Enumerate the resulting 33×77
      point-line orbit incidence matrices over Z3 (constant-on-orbits), impose
      replication 7 and pair-covering (λ,μ), and decide feasibility. Space is
      bounded and must be stated; the count is a Kramer–Mesner-type number, NOT
      3^99.
  (3) THE Z2 CASE. An involution fixes f odd points (f ≥ 1) and has
      (99+f)/2 ≥ 50 orbits. Compute the exact f-range forced by μ=2/λ=1 and the
      congruence 4f + g ≡ 4 (mod 7) with g = number of fixed points adjacent to
      their image… [g here is vertices mapped to adjacent vertices; state the
      orbit matrix, then decide feasibility]. Either UNSAT on both → |Aut|=1
      (sharp, exhausts the published automorphism program); SAT → the surviving
      orbit matrices are the finite residual for a later bounded expansion.
  (4) ~~VERIFY the re-derived folklore lemma: under an automorphism of a
      srg(v,k,1,2), the fixed set is a coclique or a smaller srg — derive from
      λ=1,μ=2 before relying on it; both controls must satisfy it.~~ **CLOSED
      NEGATIVE (tool_builder): the lemma is FALSE.** On bvls_graph()=srg(243,22,1,2)
      an order-2 automorphism fixes 27 vertices inducing a 6-regular graph with
      lambda=1 constant but mu in {0,2} non-constant — neither coclique nor SRG
      (claim `fixed-set-lemma-fails-on-bvls`, note
      research/notes/fixed-set-lemma-fails-on-bvls.md). The orbit-matrix
      machinery must therefore NOT assume the fixed set is a coclique or smaller
      SRG; the DKW congruence and row-sum/constant-on-orbit checks are
      unaffected.
control-test: rook(3) and bvls_graph() both have automorphism groups containing Z2 and Z3 (both are rank-3 / highly symmetric). The orbit-matrix machinery must recover their involution and order-3 actions exactly before any 99 conclusion is trusted.
corrections-to-proposal:
  - The candidate's bound "at most 50 orbits under an involution" is WRONG. An involution on 99 vertices fixes f points (f odd, f >= 1) and pairs the rest into transpositions, so the orbit count is f + (99-f)/2 = (99+f)/2 >= 50. It is AT LEAST 50, not at most. For the order-3 case, Crnković-Maksimović proved [aut-cm-2020] that an order-3 automorphism has NO fixed points, so it has exactly 99/3 = 33 orbits -- the candidate's "at most 33" is then exactly 33. The honest statement: Z2 gives >= 50 orbits (>= 50 by f>=1, and the trace/variance constraints plus mu=2 typically force f small, so the true count is near 50), and Z3 gives exactly 33 orbits. The case split is still small and finite either way.
  - The folklore lemma "a fixed set under an automorphism is a coclique or an srg" is asserted, not re-derived here; the first-step must re-derive it from mu=2 / lambda=1 before relying on it (the candidate already flagged this). **RESOLVED: it is FALSE, closed by tool_builder (claim `fixed-set-lemma-fails-on-bvls`); do not rely on it.**
```

## What it would buy

Completing the orbit-matrix programme on the residual Z2 and Z3 cases. If both are infeasible, the conclusion is |Aut(Gamma)| = 1 -- a sharp, named search-boundary statement (no nontrivial symmetry can locate the graph, so enumeration must start from a rigid seed, and the published automorphism program is exhausted). If either is feasible, the surviving orbit matrices become the finite residual that a later bounded search must expand. Either is a reportable exact result, and neither contradicts the controls (both have Z2 and Z3 the checker must find first).

## De Winter-Kamischke-Wang congruence (the arithmetic an orbit matrix must pass)

For an SRG with eigenvalues k, r, s and an automorphism phi of order n with f fixed vertices and g vertices mapped onto adjacent vertices, the eigenvalue eigenspace gives
  k - s = -s f + g   (mod sqrt(Delta)),   Delta = (lambda-mu)^2 + 4(k-mu).
For (99,14,1,2): Delta = (1-2)^2 + 4(14-2) = 1 + 48 = 49, sqrt(Delta)=7; k-s = 14-(-4)=18. So the involution/order-3 orbit data must satisfy 18 = 4 f + g (mod 7) → 18 ≡ 4 (mod 7), so 4f + g ≡ 4 (mod 7). Combined with f ≡ 99 (mod 2)=1 odd for an involution and the run's proven "order-3 has no fixed points" (f=0, hence g ≡ 4 (mod 7)), this gives the exact congruence constraints the orbit-matrix enumeration must pass.

## Directive 27 gates — must be satisfied before any 99 verdict is believed or recorded

1. **State what a verdict proves, in the note before running.** `Crnković–Maksimović
   give fixed-point-freeness for order 3, hence exactly 33 point-orbits and 77 line-orbits.
   INFEASIBLE there excludes an order-3 automorphism — it does NOT show
   srg(99,14,1,2) does not exist.** Combined with the published reduction of any
   nontrivial Aut to {Z2, Z3}, finishing both cases would show the graph has
   **TRIVIAL automorphism group if it exists**. That is a genuine result and it is
   **not a nonexistence proof**. Say so in the note before running, not after.

2. **Validate the encoder before trusting UNSAT.** Build the analogous orbit
   matrix for a graph we have — **BvLS admits automorphisms of order 3** — and
   require Z3 to **FIND** it. This workspace has one unvalidated-engine false
   positive on record already (`n3_vc_gate`; the `E = 16·n3` identity failed
   across 37 random graphs, handled as SUPERSEDED/FLAWED); an UNSAT from an
   unvalidated orbit-matrix encoding would be the second. No UNSAT is
   admissible until the encoder has recovered BvLS's order-3 action.

## Status

adopted — the method is cited, applied to this exact parameter set, and its residual cases are the well-defined Z2/Z3 orbits. Not refuted: both controls contain the required Z2/Z3 actions the checker must reproduce (rook(3) and bvls both admit order-3 fixed-point-free automorphisms). The one falsification risk, which survives, is an orbit matrix that is feasible but not expandable, yielding a boundary rather than a contradiction — still a reportable result. Directive 27's two gates are mandatory: the "what it proves" caveat and the BvLS-order-3 encoder validation must be in the note and the positive control before any 99 INFEASIBLE is recorded.

## Progress (tool_builder)

Step (1), the checker, is DONE and VALIDATED on both controls
(`code/out/orbit_matrix_controls.py`, capture `code/out/orbit_matrix_controls.captured.txt`;
`orbit_matrix` and `orbit_matrix_is_constant` in `code/lib/srg.py`). For each of
the four control automorphisms the orbit matrix: (a) reproduces the degree k as
row sums (4 for rook, 22 for bvls), (b) is constant on orbits (verified per
vertex), and (c) satisfies the DKW congruence k-s ≡ -s·f+g (mod sqrt(Delta))
with integer residue 0: rook(3) Z2 transpose f=3 diff 0 (sqrt Delta=3); rook(3)
Z3 row-shift f=0 diff -3; bvls Z2 negation s->-s f=1 diff 0; bvls Z3 translation
f=0 diff -216 (sqrt Delta=9). Every one is a genuine automorphism, order
verified. The checker is therefore a trustworthy control gate. It is NOT yet a
99 verdict: the next step (encoders for Z3/Z2 orbit matrices / the triangle-geometry
incidence orbits at 99) must first be validated to FIND the bvls order-3 action
before any UNSAT from it is believed (the run's standing unvalidated-engine rule).
