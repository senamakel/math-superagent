# Matschke 2014 — A Survey on the Square Peg Problem

**Source:** Benjamin Matschke, "A Survey on the Square Peg Problem," Notices of the AMS 61(4), 2014, pp. 346–352. DOI: 10.1090/noti1100. Full text at [[research/sources/matschke2014-survey-square-peg.full.md]].

## What it establishes

The canonical entry point. States the Square Peg Problem (Toeplitz, 1911), reports it **open** in full generality, and catalogs the affirmative classes and the methods behind them.

**Conjecture 1 (Square Peg Problem).** Every continuous simple closed curve γ : S¹ → R² (a Jordan curve, equivalently a topological embedding) contains four points that are the vertices of a square.

Key facts:
- **All known positive results use the same mechanism:** smooth curves inscribe *generically an odd number of squares*, measurable several topological ways. No method yet extends to the general continuous case.
- **The approximation trap is explicit:** the survey states one might reduce the general case to smooth by approximation, but a limit of inscribed squares can degenerate (side length → 0), and no known method rules this out.
- **Theorem 2 (Stromquist):** any *locally monotone* embedding γ : S¹ ↪ R² inscribes a square. Definition: every point x ∈ S¹ has a neighborhood U and a linear functional ℓ : R² → R such that ℓ∘γ|_U is strictly monotone. The survey calls this "the second strongest" class.
- **Theorem 4 (open-dense criterion):** Let γ be a Jordan curve. If there is 0 < ε < 2π such that γ contains no (or generically an even number of) *special trapezoids of size ε*, then γ inscribes a square. This is the basis of Matschke's open-dense class.
- **Theorem 5 (annulus result):** if γ : S¹ → A (annulus {x : 1 ≤ ||x|| ≤ 1+√2}) is a continuous closed curve non-zero in π₁(A) = Z, then γ inscribes a square of side length ≥ √2. (A *quantitative*, nondegenerate-square result for a class of continuous curves.)
- **Theorem 7 (Vaughan):** any continuous embedding γ : S¹ ↪ R² inscribes a rectangle. (Rectangle is fully solved for continuous curves; the square is not.)
- The survey also lists: Hebbert (quadrilaterals), Zindler/Christensen (convex), Jerrard (analytic), Nielsen–Wright (curves symmetric across a line or about a point), Vrećica–Živaljević (Stromquist's class), Pak (piecewise linear), Sagols–Marín (discretizations), CDM (bounded total curvature without cusps, and C¹-curves), Makeev (star-shaped C² curves), Matschke (open-dense class, and continuous curves in bounded domains).

## Status and what would falsify it

- Survey is a secondary source: its claims are the authors' reports of the primary results. Each named theorem must be traced to its primary paper before this workspace relies on the *details*.
- The survey (2014) predates: Greene–Lobb's rectangular-peg proof (2020/21), Tao's integration approach (2017), Akopyan–Avvakumov cyclic quadrilaterals (2018), Matschke's open-classes paper (2022). Those are covered by their own sources here.

## Claims

```claim
id: matschke2014-conjecture1
statement: Toeplitz's Square Peg Problem: every Jordan curve γ: S^1 → R^2 contains four points that are the vertices of a square.
status: conjectured
evidence: stated by Matschke 2014 (survey), attributed to Toeplitz 1911; open in full generality as of 2014
holds-here: this is the problem under attack
falsifies: a published proof for all continuous Jordan curves, or a counterexample
```

```claim
id: matschke2014-stromquist-locally-monotone
statement: Any locally monotone embedding γ: S^1 → R^2 inscribes a square. (Stromquist's theorem, as reported in the survey.)
status: asserted-by-source
evidence: Matschke 2014 survey Theorem 2; primary source Stromquist 1989 (Mathematika 36, 187–197) not yet in library
holds-here: yes — this is the load-bearing theorem GOAL.md names as the base to formalize and extend
falsifies: a locally monotone Jordan curve without an inscribed square, or a discrepancy with the primary source
```

```claim
id: matschke2014-vaughan-rectangle
statement: Any continuous embedding γ: S^1 → R^2 inscribes a rectangle. (Vaughan's theorem.)
status: asserted-by-source
evidence: Matschke 2014 survey Theorem 7
holds-here: related result — rectangle solved, square open; must not be conflated with the square case
falsifies: a continuous Jordan curve with no inscribed rectangle
```

```claim
id: matschke2014-annulus-square
statement: If γ: S^1 → A is a continuous closed curve in the annulus {1 ≤ ||x|| ≤ 1+√2}, non-zero in π1(A)=Z, then γ inscribes a square of side length at least √2.
status: asserted-by-source
evidence: Matschke 2014 survey Theorem 5
holds-here: candidate quantitative test case; a verified instance would exercise the config-space map on a genuinely continuous curve
falsifies: a continuous curve in the annulus, homotopically nontrivial, with no square of side ≥ √2
```

```claim
id: matschke2014-open-dense-criterion
statement: If a Jordan curve γ contains no special trapezoid of size ε (0 < ε < 2π), or generically an even number of them, then γ inscribes a square.
status: asserted-by-source
evidence: Matschke 2014 survey Theorem 4; developed in Matschke 2009 arXiv:1001.0186
holds-here: the engine behind Matschke's open-dense class; structural route to "generic curves have squares"
falsifies: a curve with no special trapezoid of size ε and no inscribed square
```
