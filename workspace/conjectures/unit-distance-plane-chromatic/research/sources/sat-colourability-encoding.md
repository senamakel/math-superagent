# Complete k-colourability oracle via SAT: encoding and method

**Subject:** The second half of the oracle pair required by GOAL.md — a
**complete** `(k-1)`-colourability test returning a witness, so an UNSAT can be
contrasted with a real SAT on graphs known to be colourable. This source
records the standard encoding the run should implement, from the literature on
SAT graph-colouring encodings.

## Source
- D. Faber, A. Jabrayilov, P. Mutzel, *SAT Encoding of Partial Ordering Models
  for Graph Coloring Problems*, LIPIcs SAT 2024, DOI 10.4230/lipics.sat.2024.12
  (assignment-model encoding, equations (8a),(8b); sequential at-most-one
  encoding, equations (9a)-(9c)).
- A. Ignatiev, A. Morgado, J. Marques-Silva, *Cardinality Encodings for Graph
  Optimization Problems*, IJCAI 2017, DOI 10.24963/ijcai.2017/91 (MinCol
  encoding with x_{u,k} variables).
- E. Hébrard, G. Katsirelos, *Constraint and Satisfiability Reasoning for Graph
  Coloring*, JAIR (2020) / arXiv (add/contract Zykov recurrence, DSATUR
  branching, symmetry-free tree).
Recorded as syntheses of search passages (direct publisher download blocked).

## What it establishes — the standard k-colourability SAT encoding

Let `G = (V, E)` and let the target number of colours be `C`.

**Variables:** `x_{v,i}` for each vertex `v in V`, colour `i in {1..C}`;
`x_{v,i} = True` iff vertex `v` gets colour `i`.

**Clauses:**
- Every vertex gets at least one colour:
  `(x_{v,1} OR x_{v,2} OR ... OR x_{v,C})` for each `v`.  [at-least-one]
- Adjacent vertices may not share a colour: for each edge `{u,v} in E` and each
  colour `i`,
  `(not x_{u,i} OR not x_{v,i})`.  [properness]
- (Optional, sound but complete as a *decision* without it) every vertex gets at
  most one colour — needed only if a variable assignment mapping to a colouring
  is required as a witness; implemented via a sequential encoding of
  3C-4 clauses and C-1 auxiliary variables per vertex: `not x_{v,i} OR s_{v,i}`,
  `not s_{v,i-1} OR s_{v,i}`, `not x_{v,i} OR not s_{v,i-1}`.

The CNF is satisfiable iff `G` is `C`-colourable; a satisfying assignment gives
a witness colouring directly. To find the chromatic number one tests
`C = 1, 2, 3, ...` with the SAT solver (SAT at C, UNSAT at C-1 pins it).

**Symmetry breaking** (cuts colour-permutation symmetries, optional): use the
known DSATUR/Zykov ordering ideas — e.g. the Hébrard–Katsirelos add/contract
recurrence gives a symmetry-free tree.

## Why this source matters
- It is the *technique* tier, not the answer tier: it does not state `chi` of
  the plane, it states how to build the complete colouring test the run must
  write and calibrate on the 7-vertex graph (SAT for 4 colours, UNSAT for 3).
- It is the independent-verification leg: the construction code and the
  verification colouring test must not share arithmetic; a SAT encoding is a
  genuinely independent route.

## Claim block
```claim
id: sat-k-colourability-encoding
statement: G = (V,E) is C-colourable iff the CNF consisting of
  (i) at-least-one  OR_i x_{v,i} for every v, and
  (ii) properness  (not x_{u,i} OR not x_{v,i}) for every edge {u,v} and every i,
  is satisfiable; a satisfying assignment is a C-colouring of G, and the
  chromatic number is the least C for which the CNF is satisfiable.
hypotheses: G finite simple graph; C a positive integer; booleans x_{v,i}.
holds-here: YES — the target graphs are finite unit-distance graphs; this gives
  the complete colouring oracle required by GOAL.md.
status: asserted-by-source (standard, textbook SAT encoding; references above).
bearing: the oracle for "is this graph k-colourable", to be calibrated on the
  7-vertex graph (4-colourable / not 3-colourable) before trusting any bound.
anchor: research/sources/sat-colourability-encoding.md
falsifies: a graph that is C-colourable but whose at-least-one+properness CNF is
  UNSAT — impossible; the clauses are a direct transcription of the definition.
```
