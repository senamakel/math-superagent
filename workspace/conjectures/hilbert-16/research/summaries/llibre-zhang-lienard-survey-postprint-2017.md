# Llibre–Zhang, "Limit cycles of the classical Liénard systems: a survey on the Lins Neto, de Melo and Pugh's conjecture"

<!-- source: https://ddd.uab.cat/pub/artpub/2017/221320/expmat_a2017v35n3p286preprint.pdf | Expo. Math. 35(3):286–299 (2017), DOI 10.1016/j.exmath.2016.12.001 — full postprint text held -->

Full text: [[llibre-zhang-lienard-survey-postprint-2017.full]]

**The correct Liénard-survey anchor (full postprint, not just the record page).**
Replaces the contaminated held file `llibre-zhang-lienard-conjecture-survey.full.md`
(which was an unrelated German-power-grid paper, Mureddu arXiv:1612.05532).
This file holds the actual postprint body with complete proofs of the known
results.

## What it establishes

For the classical Liénard system

```
ẋ = y − F(x),  ẏ = −x,   F a real polynomial of degree n,
```

with [·] the integer part, the Lins Neto–de Melo–Pugh conjecture says there
are at most ⌊(n−1)/2⌋ limit cycles; the paper's Theorem 1 (a complete proof,
via first-order averaging f(r)=Σa_{2j+1}b_{2j+1}r^{2j+1} with simple roots)
shows this bound is **sharp** as a lower bound: degree-n systems exist with
⌊(n−1)/2⌋ cycles. Theorem 2 settles the conjecture's truth:

- (a) n = 1, 2: **no** limit cycles (n=1 linear; n=2 via Proposition 4,
  unique root of the odd part O(x)=a₁x).
- (b) n = 3, 4: **at most one** limit cycle, and examples with one exist
  (n=3: two new proofs given here — divergence/Greens integral I =
  −∬_{R}(−a₁/x²+3a₃)dxdy > 0 showing every cycle hyperbolic unstable, so
  ≤ 1; and a second proof via the first-integral comparison; n=4: by
  Li–Llibre 2012, 20-page proof not repeated).
- (c) n ≥ 6: the conjecture is **FALSE** — there are systems with at least
  **n − 2** limit cycles. Complete proof given, following De Maesschalck–Huzak
  2015 via the **slow divergence integral**
  I(x)=∫_{x}^{L(x)} f(s)²/s ds (Theorem 7: if I has exactly k simple zeros,
  the perturbed system (18) has exactly k+1 hyperbolic limit cycles for
  ε>0 small). The n=6 base case uses I₁(x)=0.4x³−1.248x⁵+1.17429x⁷−0.3x⁹
  with exactly 3 positive zeros → 4 cycles; induction in even degree 2k
  (I^{(k+1)}₁ gains two O(1/µ) zeros via J(x)=∫(A′B−AB′), with
  A=x^{2k−2}+10x^{2k}, B=x^{2k−1}+x^{2k+1} having exactly 2 simple positive
  zeros) then odd degree n=2k+1 by a Poincaré–Bendixson annulus argument at
  infinity.
- **n = 5: OPEN** (unresolved) as of this survey — the paper's open problem
  is the maximum number of limit cycles for degree n ≥ 5.

History of the disproof: DPR 2007 (n≥7, +1 cycle beyond the conjecture);
De Maesschalck–Dumortier 2011 (n≥6, +2); De Maesschalck–Huzak 2015 (n−2
cycles, n≥6).

## Implication for this problem

**The LdMP conjecture is true for n ≤ 4, false for n ≥ 6, and n = 5 is open** —
now anchored on the held full postprint with the actual proofs, not just the
record page. This is the cornerstone of the slow–fast test (problem.md test 3):
the counterexamples come from **canard / relaxation-oscillation constructions in
the singular limit** (slow divergence integral, small parameter ε), exactly the
warning that sharp conjectures die to slow–fast geometry. The slow divergence
integral I(x) is itself a displacement-type observable (counting zeros of a
one-variable function from a first-order asymptotic form), a model for this
run's zero-counting machinery.

**Evidence class**: sourced — full postprint text held
  `research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md`;
  peer-reviewed Expo. Math. 2017.
**Falsifier**: a source closing the n = 5 case (≥ 3 cycles for degree-5
  Liénard), or a corrected count for n ≥ 6.
**Holds-here**: yes.

Claims ledger: `h16-lienard-ldmp-survey-2017`, `h16-lienard-ldmp-disproved`,
`h16-lienard-n5-open`.