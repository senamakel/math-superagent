# Stromquist 1989 — Cambridge abstract page (what it confirms; what is still missing)

**Source:** Walter Stromquist, "Inscribed squares and square-like quadrilaterals
in closed curves," Mathematika 36(2), 1989, 187–197. DOI
10.1112/S0025579300013061. Captured page: Cambridge Core abstract +
citation graph ([[research/sources/stromquist-1989-cambridge-abstract.full.md]]).
Primary full text remains paywalled.

**What this page establishes (version-of-record abstract, quoted verbatim in
the summary):**

1. **Main theorem (Rⁿ):** for every smooth curve in Rⁿ ("smooth" = continuously
   turning tangent), there is a quadrilateral with equal sides and equal
   diagonals whose vertices lie on the curve — a "square-like quadrilateral".
2. **Plane case:** implies an inscribed square, strengthening Schnirelmann's and
   Guggenheimer's theorems.
3. **The weaker condition:** "We give a weaker condition which is still
   sufficient for the existence of an inscribed square in a plane curve, and
   which is satisfied if the curve is convex, if it is a polygon, or (with
   certain restrictions) if it is piecewise of class C¹." — this is the
   primary-source-level confirmation that the run's claim
   `matschke2014-stromquist-locally-monotone` carries at second hand. The
   exact wording of the weaker condition ("Condition A") is NOT on the page.

**What it implies here:**

- The Lean `Cited` axiom `stromquist_square_peg` in
  `code/lean/Lib/Stromquist.lean` is consistent with the version-of-record
  abstract. Its `LocallyMonotone` definition now has two verbatim primary-
  adjacent wordings to choose from: Barber 2026 Def 1.9 and Asano–Ike 2024
  Def 5.10 (both cite [Str89, §6]) — identical in content (per-point unit
  vector v(p) with strictly monotone inner product). The formal statement is
  faithful.
- **Still missing:** the paywalled proof pages; the exact Condition A wording;
  Stromquist's own treatment of degenerate boundary configurations. The Rius
  Casado thesis PDF (not on disk) was the planned substitute exposition.
- Citation graph confirms the influence chain (cited by Matschke 2014/2009,
  Nielsen–Wright 1995, Tao 2017, Vrećica–Živaljević 2011, CDM 2022, GL 2023).
  No contradiction with any in-library claim.

```claim
id: stromquist1989-abstract-weaker-condition
statement: Stromquist 1989's own abstract states a weaker condition than smoothness that is still sufficient for an inscribed square in a plane curve, satisfied by convex curves, polygons, and (with restrictions) piecewise-C¹ curves. The exact wording of the condition is on the paywalled pages.
status: sourced (version-of-record abstract page)
evidence: Cambridge Core record, DOI 10.1112/S0025579300013061
holds-here: yes — corroborates matschke2014-stromquist-locally-monotone at primary-source level; the verbatim locally-monotone definition is carried by Barber 2026 Def 1.9 / AI 2024 Def 5.10
falsifies: a discrepancy between the survey's "locally monotone" and Stromquist's actual Condition A (only checkable against the paywalled primary)
anchor: research/sources/stromquist-1989-cambridge-abstract.full.md
```
