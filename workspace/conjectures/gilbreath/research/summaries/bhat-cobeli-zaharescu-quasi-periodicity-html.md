# Bhat, Cobeli, Zaharescu 2023 — On quasi-periodicity in Proth–Gilbreath triangles

**Full text:** `research/sources/bhat-cobeli-zaharescu-quasi-periodicity-html.full.md` [[bhat-cobeli-zaharescu-quasi-periodicity-html.full]]
**Source:** arXiv:2307.11776v1 [math.NT], 19 Jul 2023; Bull. Math. Soc. Sci. Math. Roumanie 67(115) (2024) 3–21.

## What it establishes

Operates PG: sequence → absolute differences of neighbours. Studies rows over F_2 (binary), which is the mod-2 (halved-even) part of the triangle this run studies.

- **Theorem 2 (main: fixed points of the halved operator).** A binary row α=(a_0,a_1,…) is *ultimately replicated identically* in the next PG row (α≍Ψ(α) in the ultimately-equal quotient) iff its generating function ϕ(α)=Σ a_k X^k ∈ F_2[[X]] is a rational function of either form
  `P(X)/(1+X+X^r)` or `P(X)/(X^r(1+X)+1)` for some r≥0, P∈F_2[X].
- **Eq. (6) (action of the operator).** On binary rows, ϕ(Ψ(α)) = ((1+X)ϕ(α) − α_0)/X. (In F_2, |a−b|=a+b mod 2 — the absolute value disappears and PG acts as the Pascal/rule-90 addition.)
- **Theorem 5.** α ultimately identical with Ψ(α) iff ϕ(α)=G(X)/(1−X^{2^d−1}) — i.e. exactly the **periodic** binary sequences.
- **Theorem 6 (leap fixed points).** α is ultimately replicated in the l-th following row iff ϕ(α)=P_l(X)/((1+X)^l+X^r) or P_l(X)/(X^r(1+X)^l+1).
- **Theorems 3–4.** Consequences for representing F_2 power series as rational functions (several ways), gcd combination.
- **Proposition 1.** Fibonacci sequences (mod 2) give left edge `1,1,0,1,1,0,…`; powers of two (1,2,4,8,…) give **all-ones** left edge.
- Empirical (Table 1): on the prime triangle, along rays parallel to the left edge, #0s ≈ #2s (mod 4), each within √50000, differing by <1% — consistent with the run's `{0,2}`/mod-4 concentration.

## Hypotheses held here

The theorems are about **binary** rows under the mod-2 operator. The prime Gilbreath triangle's even entries divided by 2 form a {0,1} (halved) triangle whose parity is governed by this same Pascal/rule-90 structure — that is the natural correspondence. The theorems characterize *when rows repeat* (periodic self-similarity), which is the run's rule-90-identification territory, NOT the regeneration of {0,2} blocks in the integer triangle. So: relevant as structure theory of the binary/halved regime; does not settle GC.

## Bearing on this run

- Confirms the {0,1}-halved triangle is a linear rule-90 (Pascal mod 2) system whose fixed points are exactly periodic F_2-rational rows — reinforcing `rule90-identification-real-absorption-refuted` that the {0,2} interior evolves as XOR, but that this alone does not absorb the boundary/intruder.
- Theorem 2's rational-function form is a clean characterization a future invariant of the halved triangle could target: periodic rows are exactly those with rational generating functions of the given shape.
- The 0≈2 ray statistic corroborates (motivationally) the run's mod-4 concentration but is empirical, not a theorem about the conjecture.

## Claims

```claim
id: pg-fixed-points-rational-form
statement: A binary row is ultimately replicated identically under the Proth–Gilbreath (mod-2) operator iff its F_2 generating function is P(X)/(1+X+X^r) or P(X)/(X^r(1+X)+1); periodic rows are exactly ϕ(α)=G(X)/(1−X^{2^d−1}).
hypotheses: α∈{0,1}^∞; PG action via |a−b|=a+b mod 2.
holds-here: yes for the binary/halved part of the triangle; not a GC statement.
status: proved in source (finite+periodic analysis)
bearing: characterizes row-repetition/periodicity in the halved {0,1} triangle; structure theory for a future invariant.
anchor: research/sources/bhat-cobeli-zaharescu-quasi-periodicity-html.full.md
answers: what-are-the-fixed-points-of-the-halved-gilbreath-operator
```

```claim
id: pg-fibonacci-powers-of-two
statement: Fibonacci rows (mod 2) give a left edge 1,1,0,1,1,0,…; the powers-of-two row (1,2,4,8,…) gives an all-ones left edge under PG.
hypotheses: rows in ℤ; PG operator.
holds-here: yes (elementary).
status: proved in source
bearing: irrelevant to the prime case directly; shows fixed/self-similar rows exist.
anchor: research/sources/bhat-cobeli-zaharescu-quasi-periodicity-html.full.md
```
