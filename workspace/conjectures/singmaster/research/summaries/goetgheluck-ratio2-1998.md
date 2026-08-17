# Goetgheluck 1998 — infinite families of solutions of C(n,k) = 2·C(a,b)

Source: P. Goetgheluck, "Infinite families of solutions of the equation
$\binom{n}{k}=2\binom{a}{b}$", Math. Comp. 67 (1998) 1727–1733.
AMS PDF: https://www.ams.org/journals/mcom/1998-67-224/S0025-5718-98-01002-3/S0025-5718-98-01002-3.pdf
DOI: 10.1090/S0025-5718-98-01002-3
Full text: [[goetgheluck-ratio2-1998.full]]

## What it establishes

The ratio-2 binomial equation, along with the ratio-1 equation
`C(n,k)=C(a,b)` (Singmaster's repeated-binomial-coefficient problem), is the
family of near-collision Diophantine equations whose fixed-(k,b) finiteness is
a Siegel-theorem consequence.

- **Trivial infinite family (eq. (1) with k≤n/2, b≤a/2):**
  `(n,k,a,b) = (2r, r, 2r−1, r−1)` for every r ≥ 1, i.e.
  `C(2r,r) = 2·C(2r−1,r−1)` (central binomial = 2× the adjacent entry).
- **Siegel finiteness for near-collisions:** "for any fixed k ≥ 2 and b ≥ 2
  with k+b > 4, there are only finitely many solutions n, a to equation (1)"
  (Siegel's theorem [7, Th. 22, p. 278]). So per-pair finiteness holds for the
  ratio-2 equation too, with the same ineffectivity in (k,b) as the ratio-1
  case — a uniform-in-k bound would need a different mechanism.
- **Two new infinite families** obtained by solving Pell equations (the paper's
  main content; explicit formulas in §3–§4 of the full text).
- **Method** (same as Singmaster's FQ 1975): (1) computer search for small
  solutions, (2) identify which solutions belong to infinite families by
  solving Pell equations.

## Bearing for this run

- The k=2 column is where every known N(a)≥6 witness sits (120, 210, 1540,
  7140, 11628, 24310, 3003 all have a k=2 representation `C(x,2)` for some x),
  and the ratio-2 family is a structurally-adjacent infinite family in the
  same column. It confirms the column's infinite richness: even fixing
  `C(n,2) = 2·C(a,b)`-type equations, the k=2 column has infinitely many
  solutions.
- The paper's Kummer theorem (borrowing count = exponent of p in C(n,k)) is
  stated as background and is directly relevant to the run's adopted
  `binary-lucas-submask` approach — the parity structure of binomial
  coefficients is governed by exactly this class of theorem.
- Marginal to the central uniform-bound question: it gives finiteness per fixed
  (k,b) (ineffective), not uniformity. Recorded for completeness of the
  ratio-2 / k=2 column thread.

## Evidence class

sourced (full primary PDF held at `research/sources/goetgheluck-ratio2-1998.full.md`;
the trivial family `C(2r,r)=2·C(2r−1,r−1)` and the Siegel finiteness statement
are quoted above).

```claim
id: goetgheluck-ratio2-families
statement: Goetgheluck 1998 (Math. Comp. 67, 1727-1733): (i) the equation
  C(n,k)=2*C(a,b) (k<=n/2, b<=a/2) has the infinite family
  C(2r,r)=2*C(2r-1,r-1) for every r>=1, plus two further infinite families
  obtained by solving Pell equations; (ii) for any fixed k>=2, b>=2 with
  k+b>4, only finitely many solutions (n,a) exist (Siegel);
  (iii) states Kummer's theorem: v_p(C(n,k)) = number of borrows in n-k in base p.
hypotheses: k<=n/2, b<=a/2; k+b>4 for the Siegel part.
holds-here: true — ratio-2 is the near-collision analogue of the ratio-1
  equation; the k=2 column is where all known N(a)>=6 witnesses live.
status: sourced (AMS full text held)
bearing: the k=2 column is infinitely rich even at fixed ratio 2; the Siegel
  part is per-pair ineffective (same wall as the ratio-1 case); Kummer's
  theorem supports the binary-lucas-submask thread.
anchor: research/summaries/goetgheluck-ratio2-1998.md
```