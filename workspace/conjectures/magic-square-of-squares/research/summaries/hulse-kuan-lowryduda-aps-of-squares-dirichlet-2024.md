# Hulse–Kuan–Lowryduda–Walker, "Arithmetic Progressions of Squares and Multiple Dirichlet Series" (arXiv:2007.14324)

[[hulse-kuan-lowryduda-aps-of-squares-dirichlet-2024]]
Full text: `research/sources/hulse-kuan-lowryduda-aps-of-squares-dirichlet-2024.full.md` (arXiv:2007.14324v4, 11 Oct 2023; authors Hulse, Kuan, Lowry-Duda, Walker).

## What it establishes

An analytic number theory paper counting **primitive three-term arithmetic progressions of integer squares** {h, m, 2m−h} (i.e. h, m, 2m−h all squares, with (m,h)=1; there is no primitive AP of squares with more than 3 terms — Fermat, proved by Euler, restated in §1).

**Method.** The multiple Dirichlet series D(s,w) = Σ_{(m,h)=1} r₁(h)r₁(m)r₁(2m−h)/(m^s h^w) (r₁ = square-indicator), shown to have **meromorphic continuation to C²** (Theorem 5.1) via spectral expansion against dihedral Maass forms on Γ₀(8) with character χ = (2/·). Tauberian techniques then give exact asymptotic counts for constrained families of APs of squares:

- **Theorem 7.1**: # primitive APs with m ≤ X and (a/b)² ≤ δ is (2/π²)·arcsin(√δ/2)·X^{1/2} + O_ε(X^{3/8+ε}).
- **Theorem 8.1**: # primitive APs with largest term ≤ X is (√2/π²)·log(1+√2)·X^{1/2} + O_ε(X^{3/8+ε}).
- **Theorem 8.3**: # with first term ≤ Y and centre ≤ X (Y ≤ X) is (1/(√2π²))Y^{1/2}log(X/Y) + cY^{1/2} + O_ε(X^ε Y^{3/8+ε}).
- **Theorem 8.4**: # with hm ≤ X is (2√2/π²)·₂F₁(¼,½,⁵⁄₄,½)·X^{1/2} + O_ε(X^{3/8+ε}).

**Correspondences (§2).** (i) Each primitive AP of squares {a,b,c} ↔ rational point (a/b, c/b) on the circle x²+y²=2, so the counts equidistribute rational points on that circle. (ii) Each AP of squares with common difference t ↔ a right triangle with area t (standard congruent-number link): {a,b,c}, b²−a²=c²−b²=t, ↔ triangle with legs c−a, c+a and hypotenuse 2b, area t.

## Bearing on the 3×3 MSS

**Corroborates the abundance picture, does not advance the proof.** It confirms (a) APs of squares exist only up to length 3, so each of the four centre APs (differences u, v, u+v, u−v) is individually a length-3 AP and no longer; and (b) such APs are **numerous** — Θ(X^{1/2}) with largest term ≤ X. This independently agrees with the run's computed structural finding that |S(e)| grows and millions of centres admit four AP-differences: **scarcity of APs of squares is not the obstruction**; the additive dependence among u, v, u+v, u−v is. No statement here bears on forcing four such APs to share the middle square with pairwise additive relations, so it gives no leverage toward non-existence (or existence).

**What it does not settle:** anything about a *fourth* linked AP, the additive relation, or rationalness/integrality separation on the magic square — all open as before.

```claim
id: aps-of-squares-count-asymptotics
statement: The number of primitive three-term arithmetic progressions of integer
  squares with largest term <= X is asymptotic to (sqrt(2)/pi^2) log(1+sqrt(2)) X^{1/2}
  + O_eps(X^{3/8+eps}); a primitive AP of squares has at most 3 terms; each primitive
  AP {a,b,c} corresponds to a rational point (a/b,c/b) on x^2+y^2=2 and to a right
  triangle with area equal to the common difference.
hypotheses: primitive 3-term APs of squares (m,h coprime); X the size bound
holds-here: yes (each of the four MSS centre APs is such a primitive/3-term object;
  the count bound applies to candidate APs)
status: proved (Theorems 5.1, 7.1, 8.1, 8.3, 8.4; length-3 cap is Fermat/Euler, sourced)
bearing: corroborates the run's S(e)/Phi structural finding that APs of squares are
  abundant (Theta(X^{1/2}) of them), so scarcity of APs is not the MSS obstruction;
  the additive relation among the four centre differences is. No direct bearing on
  non-existence/existence of the 3x3 MSS.
anchor: research/sources/hulse-kuan-lowryduda-aps-of-squares-dirichlet-2024.full.md
```

## Does this source help?

**Marginally.** It is a neighbouring analytic result, not a 3×3 input. Its value is confirming the abundance-of-APs picture and the length-3 cap already central to the run's parametrisation, and its circle/rational-point link is a restatement of structures the run has from Bremner and its own Φ work. No theorem here constrains the four-linked-AP additive condition.

## Source

Hulse, Kuan, Lowry-Duda, Walker. "Arithmetic Progressions of Squares and Multiple Dirichlet Series." arXiv:2007.14324v4 [math.NT]. https://arxiv.org/abs/2007.14324
