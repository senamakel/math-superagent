# Friedl–İnce 2023 — When does the Table Theorem imply a solution to the Square Peg Problem?

**Source:** Stefan Friedl, Kenan İnce, arXiv:2303.17711 [math.GN], 30 Mar 2023 (8 pages, 6 figures). Full text: `research/sources/friedl-ince-2023-table-theorem-square-peg.full.md`.

**Status: verified against full text on disk.**

## What it establishes

Fenn's **Table Theorem** (1970) does *not* straightforwardly imply the Square Peg Problem, even for convex curves — because the Table Theorem can have **trivial solutions** (a large square whose vertices lie outside the domain D while its center lies in D, all at level 0 of the "ground function" f). The paper characterizes exactly when the Table Theorem yields a *nontrivial* inscribed square.

**Main Lemma 2.2.** For a compact convex non-empty D ⊂ ℝ²: D is **obtuse** ⟺ D is s-nontrivial for some s > 0.

(Definitions: D obtuse = every boundary point x has a sector T_{v,θ}(x) ⊂ D of angle θ > π/2; D s-nontrivial = for every square of side ≤ s with center in D, at least one vertex lies in the interior of D.)

**Main Theorem 1.5.** If J is the boundary of a compact convex D ⊂ ℝ² and D is obtuse, then J admits an inscribed square.

**Caveat the paper itself makes:** the Square Peg Problem for convex curves was already known (Zindler 1921; Christensen 1950); the paper's contribution is a new proof via the Table Theorem, and the elucidation of the obtuseness condition.

## Why it matters for this run (the trivialization obstruction)

The "trivial solution" phenomenon of the Table Theorem — a square too large to be informative, with all vertices outside D — is structurally the **same failure mode as shrinkout**: a limit/construction produces only degenerate or uninformative configurations. The paper's Main Lemma is exactly the identification of the condition that rules the trivialization out (obtuseness gives a positive scale s). This is a second documented instance of the run's core obstruction, in the Table-Theorem setting, with the obstruction precisely characterized.

## Claim blocks

```claim
id: friedl-ince-2023-table-theorem-triviality
statement: Fenn's Table Theorem alone does not imply the Square Peg Problem even for convex curves: its solutions may be trivial (all vertices of the square outside D, center in D). The nontrivial case is exactly characterized: D obtuse ⟺ D s-nontrivial for some s > 0.
hypotheses: D compact convex non-empty in ℝ².
holds-here: shows a named method (Table Theorem route) fails to prove the square peg problem without an extra scale condition; records the obstruction.
evidence: full text verified (arXiv:2303.17711).
status: theorem (arXiv preprint)
falsifies: a compact convex D that is non-obtuse yet s-nontrivial, or an obtuse D that is s-trivial for all s.
```

```claim
id: friedl-ince-2023-convex-square-known
statement: The Square Peg Problem for convex curves was proved by Zindler (1921) and Christensen (1950) — the convex case is not the open part of the conjecture.
hypotheses: convex Jordan curve.
holds-here: places the convex case as settled long before Stromquist.
evidence: Friedl–İnce 2023 (citing Zindler 1921, Christensen 1950).
status: sourced claim (secondary citation; primary sources not in library)
falsifies: a convex Jordan curve without an inscribed square.
```

## Relation to existing library

- CONTRADICTS nothing; complements Matschke 2014's remark that the Table Theorem "implies the Square Peg Problem for convex curves" — Friedl–İnce show that claim was too optimistic without the obtuseness/nontriviality caveat.
- Records a *method failure* under Ruled out: the Table-Theorem route, like the naive approximation route, needs a positive-scale certificate.
