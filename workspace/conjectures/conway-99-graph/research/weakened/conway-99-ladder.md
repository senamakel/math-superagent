# Conway's 99-graph problem — ladder of weakened targets

Weakest-first climb from the trivial member of the family toward the open
target. Every `off` entry names a difficulty declared in the ladder header.
Nothing here implies the goal, and nothing here is reported as the goal.

```ladder
goal: decide whether srg(99, 14, 1, 2) exists, equivalently whether there is a partial linear space on 99 points with 231 lines of size 3 and 7 lines through each point whose collinearity graph has λ=1 and μ=2
difficulties: enumeration-ceiling, sporadic-sandwich, spectral-route-dead, no-symmetry, sts-unclassified, nonlocal-mu, local-too-weak
status: open
```

Meaning of the difficulties, one obstruction each:

- `enumeration-ceiling` — the v=99 search space (14-regular graphs on 99
  vertices, or partial Steiner triple systems with 231 blocks) defeats any
  complete enumeration, and the symmetry assumptions that made earlier searches
  feasible are themselves largely excluded.
- `sporadic-sandwich` — srg(9,4,1,2) and srg(243,22,1,2) *exist*, so any
  deciding argument must fail on both controls and bite exactly at v=99; no
  family-uniform mechanism can reach it.
- `spectral-route-dead` — every eigenvalue / Krein / absolute-bound /
  interlacing feasibility test passes at v=99, witnessed by the fact that the
  9 and 243 controls pass them too.
- `no-symmetry` — the automorphism group is believed small, possibly trivial,
  which kills symmetry-based search and group-theoretic constructions.
- `sts-unclassified` — the partial STS(99) (231 lines, replication 7) has no
  known classification to reduce the problem to.
- `nonlocal-mu` — μ=2 constrains *non-collinear* pairs through their common
  transversals, a two-point condition that resists local design arguments.
- `local-too-weak` — locally 7K₂ plus the finite triangle-extension rules do
  not force a global contradiction.

---

```rung
id: R-control-9
statement: Decide existence of srg(9,4,1,2) and exhibit the witness. Answer (classical): it exists — the 3×3 rook's graph K₃□K₃, equivalently Paley(9). Its 6 triangles are the 3 rows and 3 columns, giving a partial STS(9) with 6 lines of size 3, replication 2, and μ=2 exactly.
off: enumeration-ceiling, sporadic-sandwich, spectral-route-dead, no-symmetry, sts-unclassified, nonlocal-mu, local-too-weak
stance: settled
merge: Turn `sporadic-sandwich` back on: move to the next member v=33, where existence is genuinely open and the obstruction must already fail on the 9 and 243 controls. First move is the oracle in phase 2 building K₃□K₃ and certifying srg(9,4,1,2) from the adjacency matrix, then sourcing the claimed nonexistence of srg(33,8,1,2).
```

```rung
id: R-precedent-33
statement: Decide existence of srg(33,8,1,2) and name the mechanism. Strong indication (hand arithmetic, to be re-derived by the oracle phase): it is infeasible by eigenvalue-multiplicity integrality — eigenvalues r=2, s=−3, and the multiplicity gap f−g = k(4−k)/(2√(4k−7)) = 8·(−4)/10 = −16/5 is non-integral, so no such graph exists; the same formula also excludes k=32 (v=513) and k=44 (v=969).
off: enumeration-ceiling, spectral-route-dead, no-symmetry, local-too-weak
stance: open
merge: Turn `spectral-route-dead` back on: the 33 mechanism, if it is multiplicity integrality, is *spectral*, so it provably cannot transfer to v=99 (where f=54, g=44 are integers) — that is exactly why the 99 case survives. Confirm the 33 mechanism from its source and bank it, then the precedent is closed as a dead end for reaching 99, not as a template. First move: have the oracle recompute the multiplicity gap at k=8,14,22,32,44 and confirm the source's mechanism for 33.
```

```rung
id: R-spectral-99-failed
statement: Prove nonexistence of srg(99,14,1,2) by a spectral or feasibility argument — eigenvalue integrality, Krein conditions, absolute bound, or interlacing on the whole graph.
off: spectral-route-dead
stance: failed
merge: Refuted on arrival: every such test passes verbatim for srg(9,4,1,2) and srg(243,22,1,2), so the failing step cannot be located on the controls and the argument would prove a false statement. At v=99 the multiplicities are integral (f=54, g=44), so even the 33 precedent's mechanism is unavailable here. This rung stays on the ladder as a permanent dead end; the climb resumes at orbit matrices.
```

```rung
id: R-aut-99
statement: Establish exactly which prime orders p are excluded as automorphisms of srg(99,14,1,2) (source: Behbahani–Lam, Makhnev et al.), then exclude one further prime order by exact orbit-matrix enumeration over the prime-order orbits, encoded for CP-SAT, with the orbit matrices stated and the exhaustiveness argued.
off: enumeration-ceiling, spectral-route-dead, sts-unclassified, nonlocal-mu, local-too-weak
stance: open
merge: Turn `local-too-weak` back on: exhausting all prime orders would prove the automorphism group is trivial, after which the no-symmetry reality must be faced head-on. First move: source the exact list of excluded orders, then write the orbit-matrix constraints for one not-yet-excluded prime p and run the CP-SAT encoding — the orbit space is finite, so this does not touch `enumeration-ceiling`.
```

```rung
id: R-local-config-99
statement: Choose a finite forced sub-configuration C of the triangle geometry (e.g. a pair of intersecting triangles with a fixed partial extension) and prove by bounded exhaustive extension — stated search space, symmetry reduction, isomorph rejection — that no srg(99,14,1,2) contains C, or that every one forces a specified extension. The exhaustiveness argument is the result, not the runtime.
off: enumeration-ceiling, spectral-route-dead, sts-unclassified, nonlocal-mu
stance: open
merge: Turn `nonlocal-mu` back on: extend the finite configuration until the μ=2 condition on non-collinear pairs enters and constrains the line set globally. First move: SAT/CP-SAT encode a fixed pair-of-intersecting-triangles extension and, before trusting any UNSAT, make the same encoder *find* srg(9,4,1,2) and srg(243,22,1,2).
```

```rung
id: R-sts-restricted-99
statement: Classify the partial STS(99) with 231 lines of size 3 and replication 7 satisfying μ=2, under an added hypothesis that makes the class finite — e.g. the line set is resolvable (a parallelism into 7 classes of 33 lines), or invariant under a stated small group, or a subdesign of an STS(99). Show the class is empty, or list it, by design theory plus bounded search.
off: enumeration-ceiling, spectral-route-dead, sts-unclassified
stance: open
merge: Turn `sts-unclassified` back on: drop the added hypothesis. If the restricted class is empty, the added hypothesis is itself the obstruction and the open problem is the unclassified remainder; if non-empty, the survivors are the search frontier. First move: settle the resolvability hypothesis (parallel classes of the 231 lines), since a parallelism is a strong, checkable structure.
```

---

The two difficulties still standing between the top rung and the full goal are
`enumeration-ceiling` and `sts-unclassified`; `spectral-route-dead` and
`no-symmetry` are not obstacles to *overcome* so much as facts a real proof
must route around. The climb is not yet complete, so the ladder is `open`.
