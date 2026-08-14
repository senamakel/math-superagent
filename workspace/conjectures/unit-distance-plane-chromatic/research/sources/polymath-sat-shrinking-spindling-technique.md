# SAT-certified shrinking and spindling of 5-chromatic unit-distance graphs — technique

**Subject:** The computer-assisted *method* for simplifying large unit-distance
graphs while preserving a colouring obstruction. This is the technique tier for
the run's lower-bound construction engine — it develops the machinery (SAT
4-colouring-with-constraint, DRAT core extraction, shrinking, spindling to
concatenate copies) without handing over the concrete answer.

## Source
- *Polymath proposal: finding simpler unit distance graphs of chromatic
  number 5*, Polymath Projects blog, 2018-04-10,
  https://polymathprojects.org/2018/04/10/polymath-proposal-finding-simpler-unit-distance-graphs-of-chromatic-number-5/.
  Retrieved via `read_sources` (server-side).
  Contributors in the discussion thread include M. Heule, T. Tao, D. de Laat
  and the author of the shrinking procedure (DRAT-trim use).

## What it establishes (the technique; no concrete 5-chromatic graph is stored here)

### SAT-based core extraction ("shrinking")
The question "does graph M have a 4-colouring under which a specified subgraph
H has a monochromatic triple?" is encoded as a SAT instance. When the answer is
UNSAT, the solver's **unsatisfiability proof (DRAT)** is used to identify which
vertices participated in the argument that no such colouring exists; the
vertices not needed are removed. Repeating gives a **core** graph that still
forces the obstruction.

- First DRAT-trim pass on a ~1400-vertex graph removed ~550 vertices.
- Greedy vertex-removal in arbitrary order loses symmetry; the method iterates.
- Reported result: a 397-vertex graph shrank to 300 vertices by this method.

### Spindling to concatenate copies
Two copies of the obstruction graph can be *spindled* together (identified at
linking vertices) to assemble a larger graph that still forces the colouring
obstruction — the same gluing the 7-vertex spindle instantiates, at scale.

## Why it matters here

- This is a **method** source, not an answer: it shows how to certify, by SAT +
  DRAT proof, exactly *which* vertices are load-bearing for a colouring
  obstruction, and how to shrink/spline constructions. This is directly the
  run's construction-engine problem (which subgraphs of a candidate force the
  obstruction, and how to glue candidates).
- It confirms that the natural computer-assisted language for this problem is:
  encode "4-colouring under a constraint" as SAT, run a solver that emits an
  UNSAT proof, and use the proof to extract the essential core. The run's own
  `forced_pair.py` (complete forced-pair test) is the same shape at small scale.
- The spindling-extension paragraph is the scale-up of the thread
  `minkowski-rigidity.md`'s construction accumulation.

## Basis and status

- The described technique (SAT 4-colouring-with-monochromatic-triple encoding,
  DRAT core extraction, shrinking, spindling) = sourced (retrieved verbatim from
  the Polymath proposal and its thread).
- **No concrete 5-chromatic graph or its coordinate list is stored here.** The
  section headings / vertex counts are facts about the *method's* reported
  scale, recorded only as evidence of the method's usefulness, not as the
  answer to `problem.md`.
- Not re-verified computationally here (it is a method description; the run's
  own exact oracle is separately calibrated on the 7-vertex graph).

## Claim block

```claim
id: sat-shrinking-core-extraction
statement: Whether a graph M has a 4-colouring under which a given subgraph H
  has a monochromatic triple can be decided by SAT; when UNSAT, the DRAT
  unsatisfiability proof identifies the load-bearing vertices, and iterated
  removal of the non-essential ones yields a smaller core still forcing the
  obstruction. Spindling two copies at linking vertices concatenates them.
hypotheses: finite unit-distance graph M; a SAT solver emitting UNSAT proofs
  (DRAT-trim) on the 4-colouring-with-constraint encoding.
holds-here: YES — the same encoding pattern is the run's complete forced-pair
  test; shrinking/spindling is the run's construction accumulation at scale.
status: asserted-by-source (Polymath proposal 2018; M. Heule's reported
  shrinkage of a 397-vertex graph to 300).
bearing: the computer-assisted method language for the construction engine —
  SAT with proof-emitting solver to certify which vertices force an obstruction,
  then shrink and splice candidates; complements the run's forced_pair harness.
anchor: research/sources/polymath-sat-shrinking-spindling-technique.md
falsifies: a 5-chromatic unit-distance graph whose obstruction is not detected
  by any 4-colouring-with-monochromatic-constraint SAT encoding — would break
  the method's completeness, but the method is a tool, not a theorem about
  chi(plane).
```
