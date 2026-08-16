# Krapivin, Przybocki, Heule — "Toward Satisfiability Modulo Realizability" (2026)

> **Source:** arXiv:2607.02958 (cs.CC), PointSAT solver. Full text at `research/sources/krapivin-przybocki-heule - Toward Satisfiability Modulo Realizability - PointSAT HTML.full.md` and GitHub `andrewkrapivin/PointSAT`.
> **Relevance:** the newest computational attack on ES-type problems; the live status of the computational frontier near ES(7)=33, plus the SMT-style method (diversity + partial-realization + flippability) that this run's SAT arm can mirror.

## What it establishes

PointSAT is a SAT+Localizer ("satisfiability modulo realizability") solver for point-configuration problems in R². It interfaces a SAT solver (which generates *abstract order types*) with the Localizer realizability solver (from Subercaseaux et al.), using three heuristics: (1) generate *diverse* abstract solutions so the search does not get stuck in unrealizable regions, (2) pass *nearby* candidate solutions back from Localizer to SAT, and (3) omit *flippable orientations* (pass only partial orientation info). These heuristics are what make realizable order types findable, since almost all abstract order types are unrealizable.

### Main theorem
**Theorem 1.1: the largest point set in R² with no 6-hole or 7-gon has size 23.** I.e. h(6,7) = 24 (minimum N forcing a 6-hole or a 7-gon).
- Heule–Scheucher had proved h(6,7) ≤ 24; PointSAT proves the matching lower bound by exhibiting the 23-point witness (Figure 1, explicit coordinates) and establishing 24 is forced.
- This is a genuinely new exact computation on this run's frontier. (CAUTION against drift: h(6,7) is an **adjacent** problem — a 7-gon or 6-hole — not the exact ES(7)=33 question. Record it as adjacent-problem status, not as progress on ES(7).)

### Methods — exact status of the h-values (context)
- h(3)=3, h(4)=5, h(5)=10, h(6)=30, h(7)=∞. h(5,6)=h(5)=10, h(6,8)=h(6)=30, and now h(6,7)=24.
- ES(k)=2^{k-2}+1 verified for k≤6 (k=6 by Peters–Szekeres; SAT now proves it in seconds).

### The 32-point no-7-gon experiment — the direct ES(7) relevance
- Ran PointSAT on the problem "exists 32 points with no 7-gon" (the ES(7)=33 question's critical size).
- **2191 core hours, 200,000 abstract order-type solutions generated, ZERO realizable solutions found.**
- By contrast: 23-point problem → 423 solutions from 200,000 abstracts (1811 core-hrs); 26-point → 32 solutions from 200,000 (1193); 29-point → 4 solutions from 18,806 (3433).
- Interpretation: this is evidence but NOT a proof against a 32-point no-7-gon set. A smaller fraction of abstract solutions are realizable as n grows, and the 32-point problem has additional problem-specific difficulty (flippable-orientation ratio is smaller, and mean violations 121.6 vs ≤38 on the others, suggesting the realizable ones are even rarer and harder to reach). The search found none but did not exhaust the abstract space — so it neither proves nor refutes ES(7)=33.
- **Consistent with the SMQH 4-fold-symmetry result:** both computational attacks fail to realize any 32-point no-7-gon candidate, but for different structural reasons (SMQH: 4-fold symmetry's inner 12 are unrealizable; PointSAT: general search, only abstract solutions found).
- Also consistent with Dumitru's UNSAT certificates being only for anchored subfamilies.

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

## Further implications for the run

- The **200,000 abstract no-7-gon solutions at 32 points** — a large pool of abstract order types, almost all unrealizable — is the cleanest current quantification of how alien the abstract space is to the geometric question. It reinforces the REQUESTS/method caution: a SAT upper-bound argument must encode 4-tuple realizability or it proves something in the (largely unrealizable) abstract space.
- The "smallest unrealizable abstract order types have 9 points; forbidding them needs O(n⁹) clauses" remark is a concrete cost note: this run cannot simply add realizability clauses at n=32; realizability must be settled by a separate solver (Localizer) as PointSAT does.
- **Record carefully:** the 32-point no-7-gon search failure is NOT a disproof of ES(7)=33, and h(6,7)=24 is an adjacent (6-hole) result. Both must be marked as such so the run does not drift into claiming progress on ES(7) from them.
