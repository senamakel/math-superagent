# Keramatipour, "Approaching the Conway-99 problem using SAT solvers" (arXiv:2604.23037)

**Availability:** Only the arXiv abstract landing page is in the library (`research/sources/keramatipour-sat-conway99.full.md`); the paper body was not downloaded.

## What the abstract establishes

An experiment encoding the problem of finding strongly regular graphs (specifically toward (99,14,1,2)) as SAT instances and running them. The reported outcome is the **incapability of SAT solvers to handle this problem in reasonable time**, and the identification of underlying mathematical reasons for the limitation. The search space for the graph is finite but the computational power needed to traverse it is substantial.

## Implication here

This is negative evidence about a method, not about the problem: it confirms the run's standing caution (GOAL.md/AGENTS.md) that a blind/unbounded search is out of scope and defeats any solver. It is consistent with the conclusion that a useful search must be inside a small stated sub-space with an exhaustiveness argument. The abstract gives no search space size, symmetry reduction, or wall-clock numbers, so it adds no reportable boundary value.

## Does not settle

Whether (99,14,1,2) exists. Whether the SAT encoding has reached any stated reduction or isomorph-rejection. `status: asserted-by-source` (and from an arXiv preprint claiming solver limitation rather than a theorem). Does not help the run beyond confirming enumeration is the wrong method.

## Leads from a search-result summary of the body (UNVERIFIED — not in library)

A web-search summary of the full paper body reported additional claimed contributions:
- no Paley(9) subgraph can appear inside a putative (99,14,1,2), and the graph
  cannot contain eleven independent Paley(9) subgraphs; a conjecture of no
  Paley(9) subgraphs at all;
- a "triangular view": studying how the lambda=1 triangles interact, building a
  triangular graph whose vertices are the triangles of G, with claimed
  properties (6 vertices / 3-6-2-regular etc.).

These were NOT read in the source (only the abstract landing page is in the
library; the PDF body download is refused as already registered). They are
leads only, to be verified against the full text if the run ever needs them.
Note the "triangular view" here is a different object from Makhnev 1988's
triangle graph Gamma_Delta (triangles adjacent iff sharing a vertex): the two
must not be conflated.

[[keramatipour-sat-conway99.full]]
