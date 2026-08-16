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
statement: Decide existence of srg(9,4,1,2) and exhibit the witness. Settled: it exists — the 3×3 rook's graph K₃□K₃, equivalently Paley(9). Its 6 triangles are the 3 rows and 3 columns, a partial STS(9) with 6 lines of size 3, replication 2, and μ=2 exactly.
off: enumeration-ceiling, sporadic-sandwich, spectral-route-dead, no-symmetry, sts-unclassified, nonlocal-mu, local-too-weak
stance: settled
established-by: c4
merge: Turn `sporadic-sandwich` back on: move to v=33, where the two 9/243 controls no longer settle the question and the argument must first fail on them. First move: certify rook(3) through lib.srg.is_srg from the adjacency matrix; the next member's mechanism is already settled, see R-precedent-33.
```

```rung
id: R-aut-99
statement: Given the sourced exclusion list (claim `automorphism-orders-consolidated`: |G| divides 2·3³·7·11; only primes 2,3; no Z6/S3/Z9/E9; 2||G| ⇒ |G|≤6; 7||G| ⇒ G=Z7, hence |G| ∈ {1,2,3}), settle the next residual case: prove srg(99,14,1,2) has no involution (no Z2), narrowing |G| ∈ {1,2,3} to {1,3}, by exact orbit-matrix enumeration over the fixed-vertex structure of an involution, with the orbit matrices stated and the exhaustiveness argued.
off: enumeration-ceiling, spectral-route-dead, sts-unclassified, nonlocal-mu, local-too-weak
stance: open
merge: Turn `local-too-weak` back on: exhausting the residual {1,3} would prove G trivial, after which the local 7K₂ geometry must carry the argument unaided — that is R-local-config-99. First move: write the orbit-matrix constraints for the involution case and run the CP-SAT encoding, but only after the same encoder is made to FIND the involutions of rook(3) and BvLS — both controls have them, so this is exactly the `sporadic-sandwich` discipline that stays switched on.
```

```rung
id: R-precedent-33
statement: Decide existence of srg(33,8,1,2) and name the mechanism. Settled: it does NOT exist, by eigenvalue-multiplicity integrality — eigenvalues r=2, s=−3, and the multiplicity gap f−g = k(4−k)/(2√(4k−7)) = 8·(−4)/10 = −16/5 is non-integral. The same formula excludes k=32 (v=513) and k=44 (v=969).
off: enumeration-ceiling, spectral-route-dead, no-symmetry, local-too-weak
stance: settled
established-by: srg33-does-not-exist-integrality
merge: Turn `spectral-route-dead` back on: the 33 mechanism is spectral, so it provably cannot transfer to v=99 (f=54, g=44 are integral). Bank it as a dead end for reaching 99, not as a template. First move: recompute the multiplicity gap at k=8,14,22,32,44 with the oracle and confirm the mechanism; no further work on 33 is needed.
```

```rung
id: R-local-config-99
statement: Choose a finite forced sub-configuration C of the triangle geometry (e.g. the n3 seed — two disjoint triangles joined by exactly two edges) and prove by bounded exhaustive extension — stated search space, symmetry reduction, isomorph rejection — that no srg(99,14,1,2) contains C, or that every one forces a specified extension. The exhaustiveness argument is the result, not the runtime.
off: enumeration-ceiling, spectral-route-dead, sts-unclassified, nonlocal-mu
stance: open
merge: Turn `nonlocal-mu` back on: extend the finite configuration until the μ=2 condition on non-collinear pairs enters and constrains the line set globally. First move: take C = the n3 seed, and use what is already known — it is locally consistent to every radius (radius-6 is a stable fixpoint, claim `n3-seed-locally-consistent-radius1`), so an empty-result argument must reach radius ≥7 or invoke global μ=2; before trusting any UNSAT, make the same encoder find srg(9,4,1,2) and srg(243,22,1,2).
```

```rung
id: R-sts-restricted-99
statement: Classify the partial STS(99) with 231 lines of size 3 and replication 7 satisfying μ=2, under an added hypothesis that makes the class finite — e.g. the line set is resolvable (a parallelism into 7 classes of 33 lines), or invariant under a stated small group, or a subdesign of an STS(99). Show the class is empty, or list it, by design theory plus bounded search.
off: enumeration-ceiling, spectral-route-dead, sts-unclassified
stance: open
merge: Turn `sts-unclassified` back on: drop the added hypothesis. If the restricted class is empty, the added hypothesis is itself the obstruction and the open problem is the unclassified remainder; if non-empty, the survivors are the search frontier. First move: settle the resolvability hypothesis (parallel classes of the 231 lines), since a parallelism is a strong, checkable structure. Known negative to respect: the vertex-derived outer design does NOT recurse (claim `g-reduce-c-refuted-on-bvls`), so "the outer design must be its own srg" is already refuted.
```

```rung
id: R-spectral-99-failed
statement: Prove nonexistence of srg(99,14,1,2) by a spectral or feasibility argument — eigenvalue integrality, Krein conditions, absolute bound, or interlacing on the whole graph.
off: spectral-route-dead
stance: failed
because: every eigenvalue / Krein / absolute-bound / whole-graph-interlacing test passes verbatim for srg(9,4,1,2) and srg(243,22,1,2), so the failing step cannot be located on the controls and the argument would prove a false statement. At v=99 the multiplicities are integral (f=54, g=44), so even the 33 precedent's mechanism is unavailable here.
merge: What went wrong — every eigenvalue / Krein / absolute-bound / whole-graph-interlacing test passes verbatim for srg(9,4,1,2) and srg(243,22,1,2), so the failing step cannot be located on the controls and the argument would prove a false statement. At v=99 the multiplicities are integral (f=54, g=44), so even the 33 precedent's mechanism is unavailable here. This rung stays on the ladder as a permanent dead end; the climb resumes at orbit matrices. Do not re-propose a spectral-only nonexistence route.
```

---

The two difficulties still standing between the top rung and the full goal are
`enumeration-ceiling` and `sts-unclassified`; `spectral-route-dead` and
`no-symmetry` are not obstacles to *overcome* so much as facts a real proof
must route around. The climb is not yet complete, so the ladder is `open`.
