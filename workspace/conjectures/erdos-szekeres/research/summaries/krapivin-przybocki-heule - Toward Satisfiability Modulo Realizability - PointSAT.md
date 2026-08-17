# Krapivin, Przybocki, Heule — "Toward Satisfiability Modulo Realizability" (2026)

> **Source:** arXiv:2607.02958 (cs.CC), PointSAT solver. Full text at `research/sources/krapivin-przybocki-heule - Toward Satisfiability Modulo Realizability - PointSAT HTML.full.md`; code `andrewkrapivin/PointSAT`.
> **Role in this run:** the newest computational attack on ES-type problems; live status of the computational frontier at ES(7)=33's critical size, plus the SMT-style method (diversity + partial-realization + flippability) the run's SAT arm can mirror.

## What it establishes

PointSAT = SAT solver (generates *abstract order types*) + Localizer realizability, three heuristics: (1) generate *diverse* abstract solutions, (2) pass *nearby* candidates back from Localizer, (3) omit *flippable orientations* — needed because almost all abstract order types are unrealizable.

- **Theorem 1.1: h(6,7) = 24** — the largest set in R² with no 6-hole or 7-gon has 23 points (witness with explicit coordinates). ADJACENT (6-hole variant), not ES(7).
- **The 32-point no-7-gon experiment (critical size for ES(7)=33):** 2191 core-hrs, 200,000 abstract order-type solutions generated, **ZERO realizable found**. By comparison, the 23-point problem found 423 realizations from 200,000 abstracts (1811 core-hrs); 26-point → 32 from 200,000 (1193); 29-point → 4 from 18,806 (3433). The 32-point case also has fewer flippable orientations (0.9% of triples vs ≥1.2%) and mean 121.6 partial-realization violations (vs ≤38) — added problem-specific difficulty.
- **Interpretation:** evidence but NOT a proof against a 32-point no-7-gon set — the abstract space was not exhausted. Consistent with SMQH 4-fold (inner-12 unrealizable) and Dumitru (UNSAT only for anchored subfamilies).
- **Cost note:** smallest unrealizable abstract order types have 9 points; forbidding them needs O(n⁹) clauses — realizability must be settled by a separate solver (Localizer), not by added clauses at n=32.

## Claims

```claim
id: kph-h67-24
statement: The largest point set in general position in the plane with no 6-hole and no 7-gon has exactly 23 points; equivalently h(6,7)=24 (every 24 points contain a 6-hole or a 7-gon, and 23 points suffice to avoid both).
hypotheses: planar, general position; 6-hole = convex 6-gon with empty interior.
holds-here: yes (adjacent to ES; exact value on a k-hole/k-gon simultaneous-avoidance variant, NOT ES(7)=33 itself)
status: asserted-by-source (PointSAT computational proof + 23-point witness with explicit coordinates; not independently re-verified here)
bearing: a new exact computational value on this run's frontier; a caution that h(6,7) is an adjacent problem and must not be mistaken for ES(7)=33.
formalisation: none
```

```claim
id: kph-32-no7gon-no-realizable-found
statement: A PointSAT search for 32 points with no 7-gon generated 200,000 abstract order-type solutions (2191 core-hrs) and found no realizable one.
hypotheses: 32 points, general position; abstract order types over the signotope axioms; Localizer used for realizability.
holds-here: true — the critical size for ES(7)=33; the direct computational status.
status: asserted-by-source (numerical/search result; does NOT prove no such set exists, only that the search found none)
bearing: the computational frontier for ES(7). Consistent with SMQH (no 4-fold-symmetric realizable 32-pt no-7-gon), Dumitru (UNSAT only for anchored subfamilies). An empty result here rules out nothing by itself — the abstract space was not exhausted.
formalisation: none
```

```claim
id: kph-flippability-method
statement: PointSAT's three heuristics — diverse abstract-solution generation, nearby-candidate feedback, and omitting flippable orientations — make realizations findable where a plain SAT+Localizer fails; identically a template for this run's required SAT reproduction.
hypotheses: order-type (signotope) SAT encoding + Localizer realizability.
holds-here: true — this run's SAT arm needs exactly this to reproduce ES(5)=9 / ES(6)=17 (cited as now solvable in seconds by SAT).
status: asserted-by-source (method, validated on h(6,7)=24 and reproductions)
bearing: the run's oracle/SAT arm should mirror the signotope encoding + Localizer-style realization search.
formalisation: none
```