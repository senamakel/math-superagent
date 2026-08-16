# Approach: Higman's combinatorial algebra module / structure constants as an exact SNF obstruction

```approach
idea: Use the Bose-Mesner (Higman) algebra of the association scheme on the distance partition of a fixed vertex, and the Smith normal form of its structure-constant matrices, as an exact integrality obstruction that survives where eigenvalue integrality does not.
mechanism: For any srg(v,k,1,2) the adjacency matrix A generates a 3-dim Bose-Mesner algebra with idempotents E0,E1,E2 (spectrum 3,-4). The combinatorial structure constants (Krein parameters, intersection numbers in the distance partition) satisfy q^1_11 = 4, and the Krein matrix B = (p^1_{ij}) must be an integer matrix whose SNF/rank over Z is fixed. The new move: the *intersection* matrices L_i (adjacency of the association scheme) commute, so the Smith normal form of the integral matrix A+kI (=J-A at mu=2, i.e. the complement) is forced. Rank over F_p of A+kI for primes p not dividing the determinant is an exact invariant that 9,243,99 all satisfy spectrally — but the SNF (not just the rank) may carry a char-p distinction the Krein/absolute bounds never see.
precedent:
  - Ducey, Duncan, Engelbrecht, Madan, Piato, Shatford, Vichitbandha, "Critical group structure from the parameters of a strongly regular graph", J. Combin. Theory Ser. A (2021), DOI 10.1016/j.jcta.2021.105424: the critical (cokernel-of-Laplacian) group of an SRG is, by and large, determined by the parameters.
  - Lorenzini 1991 (Discrete Math. 91, "A finite group attached to the laplacian of a graph", Prop 2.6): for a diagonalizable integer matrix with distinct non-zero eigenvalues theta_i, every torsion element of the cokernel is killed by all the theta_i. This is why SNF carries essentially no information beyond the spectrum when the distinct eigenvalues are few (an SRG has two).
  - Peeters 2002, "On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs": which p-ranks are spectrum-determined and which are "relevant" (can distinguish cospectral graphs). Relevant p-ranks exist only to split cospectral families.
  - Chandler, Sin, Xiang, "The Smith and critical groups of Paley graphs" (2014): the SNF/critical-group machinery applied to an SRG family; shows the object is a well-understood, parameter-driven invariant.
status: refuted
killed-by: (1) The proposal's mechanism contains a factual error: "A+kI = J-A at mu=2" is FALSE. A+14I has diagonal 14; J-A (the complement of A) has diagonal 0. The two cannot be equal. The claimed "complement forced at mu=2" step does not hold. (2) Independently of that slip, the intended SNF lever cannot bite: by Lorenzini's killing theorem and the Ducey et al. 2021 parameter-driven computation, the Smith normal form / critical group of an SRG is determined by the (v,k,lambda,mu) parameters (the distinct eigenvalues are just k and the two SRG eigenvalues). Since 9 and 243 share the srg(v,k,1,2) parameter shape and pass the same spectrum obstruction, an SNF argument built on the parameters alone survives on both controls and so proves nothing about 99. (3) Unlike the p-rank route's legitimate use (distinguishing a cospectral pair), here there is no cospectral pair to separate, so the SNF carries no existence information. No source applies it to (99,14,1,2).
first-step: (For the record, not the argument.) Compute the Smith normal form of A and of the Laplacian kI-A for rook(3) and bvls_graph() in sympy, confirm both are parameter-determined (equal to the values the Ducey/Lorenzini theory gives), and record that a hypothetical 99 has the same forced SNF. This closes the route on computation, not just on the parameter argument.
```

Refuted on evidence. Two independent grounds: the "A+kI = J-A at mu=2" step is
mathematically false, and the SNF/critical group of an SRG is parameter-determined
(Ducey et al. 2021; Lorenzini killing theorem), so it carries no invariant beyond
the shared spectrum and survives unchanged on the 9 and 243 controls — the exact
admissibility failure the GOAL rule forbids. The p-rank refinement (Peeters 2002)
cannot rescue it, because relevant p-ranks exist only to tell apart a cospectral
pair, and none is at issue here.
