# Michaud-Rodgers, "Magic Squares of Squares", Warwick talk (2019) — [[michaud-rodgers-warwick-talk-2019.full]]

Undergraduate project talk (Philippe Michaud-Rodgers, Warwick). Uses algebraic geometry on the **magic square variety** — the projective variety X ⊂ P⁸ cut out by the seven independent line-equal-sum equations (homogeneous quadrics) in the eight free entries.

## Structural facts presented (asserted, from the project, not independently verified here)
- The magic square variety X is a **surface** (Hilbert polynomial degree 2, via Gröbner basis).
- X has **256 singular points** (over C), each with exactly three zero entries; explicit matrices given (entries ±1, ±√2, ±√−1…).
- **X contains no lines.**
- The **magic-hourglass** variety also contains no lines.
- The **near-magic square of squares** variety (Sallows-area, lines/columns + one diagonal equal) contains **infinitely many lines** (a two-dimensional set).
- Eliminating variables on X yields a class of **degree-8 curves** on the variety, but none passes through any rational point — offered as "further evidence" of non-existence. One such curve given (parametrised with α=1/√−3, equations −(2a²−4ab−b²)/3 = f², etc.).

**Status:** these are undergraduate-project claims, consistent with Bremner II's "no lines/low-degree rational curves" flavour but with different configuration(s); `asserted`, not reproduced. The "X contains no lines" is a clean, checkable algebraic-geometry statement that would be a genuine structural fact if verified. Note the near-magic variety having lines matches Brenner's infinite parametrised families of squared squares.

```claim
id: magic-variety-surface-no-lines
statement: The magic square variety X⊂P⁸ (3×3 grids with all 8 line sums equal) is a
  surface with 256 singular points and contains no lines; the near-magic square-of-squares
  variety contains infinitely many lines.
hypotheses: over C; homogeneous quadrics
holds-here: unchecked (undergraduate claim, not verified here)
status: asserted
bearing: if confirmed, a structural fact (no line in the projective variety) that a
  non-existence/geometric argument could build on; the degree-8 curves-through-no-rational-
  point is a lead for a rational-points obstruction
anchor: research/sources/michaud-rodgers-warwick-talk-2019.full.md
```
