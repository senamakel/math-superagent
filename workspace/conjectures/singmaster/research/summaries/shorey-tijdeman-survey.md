# Tijdeman — Highlights in the research work of T.N. Shorey (2007)

Source: R. Tijdeman, "Highlights in the Research Work of T.N. Shorey", in
Diophantine Equations (ed. N. Saradha), TIFR / Narosa, 2007.
Downloaded PDF: https://pub.math.leidenuniv.nl/~tijdemanr/shoreyt.pdf
Primary author's survey (Tijdeman is himself a coauthor of the key result).
[[shorey-tijdeman-survey]]

## What this source establishes that the library lacked

**The Beukers–Shorey–Tijdeman (BST) binomial finiteness theorem, in its own terms (Section 10).**

Erdős conjectured (generically eq. (10.1)) that for positive A,B there are only
finitely many x>0, y>0, k>=3, l>=0 with x>=y+k+l and

    A·x(x+1)...(x+k-1)  =  B·y(y+1)...(y+k+l-1).

**Beukers, Shorey & Tijdeman [6]** applied Siegel's theorem on integral points to
curves: **if k and l are fixed, the equation has finitely many solutions.**
The survey states the essential ineffectivity in his own words:
"*The work involves establishing irreducibility and computing genus of the curve
under consideration so that the assumptions of the theorem of Siegel are
satisfied. Because of the ineffective nature of Siegel's result, we do not know
any explicit estimate for the magnitude of the solutions.*"

This is exactly the reference MRSTT (arXiv:2106.03335, Remark 1.5) point to as
the only handle on the boundary regime `2<=m<=exp((log n)^{2/3+eps})` — and it is
**completely ineffective**, confirming the run's central "finiteness is not a
bound" obstruction with a primary-author citation.

## Corroborations / context in the same survey (Section 10)

- Saradha–Shorey [31]: the same Erdős conjecture holds effectively (via several
  applications of linear forms in logarithms) when x and y are composed of fixed
  primes; further (10.1) then implies `x - y >= C18·x^{2/3}` with C18>0 depending
  only on A and B.
- For `A=B=1, k+l` an integral multiple of k (eq. 10.2, `m>=2`):
  Saradha–Shorey [33], extending Runge's method to exponential Diophantine
  equations, proved `max(x,y,k)` is bounded by a number depending only on `m` —
  **an effective, uniform-in-k result for that restricted shape**. This is the
  closest analogue of an "effective, uniform-in-k" binomial-family bound in the
  literature, and it holds only because the two products are constrained to be in
  the ratio k:mk (m fixed). For Singmaster's own `C(x,k1)=C(y,k2)` there is no
  such fixed-m constraint, which is precisely why it stays ineffective.
- [32],[27]: (10.2) with 2<=m<=6 forces x=8,y=1,k=3,m=2; Shorey conjectures no
  solution for m>6.

## Bearing for this run

- Provides the primary statement + named ineffectivity of BST, the tool named in
  MRSTT Remark 1.5. Confirms that the boundary of the interior theorem is
  currently hopeless for an effective/uniform bound.
- De Weger's Conjecture-A route (all collisions known -> N<=8) remains the only
  clean path to Singmaster; this survey records the effective fixed-m analogue as
  the one place uniform-in-k effective results are known (but the fixed-m
  constraint is foreign to the binomial problem).
- The GOAL.md deliverable of "an effective bound for a specific (k1,k2) family
  with Baker's method and a computed constant" is the achievable target; the
  Bugeaud–Mignotte–Siksek–Stoll–Tengely hyperelliptic method (already held) is
  the worked example of that recipe.

```claim
id: bst-fixed-kl-ineffective
statement: Beukers-Shorey-Tijdeman (Tijdeman survey §10, primary-author): for fixed
  k,l the equation A·x(x+1)...(x+k-1)=B·y(y+1)...(y+k+l-1) has finitely many
  solutions, proved via Siegel's theorem on integral points after establishing
  irreducibility and positive genus; and because Siegel is ineffective there is no
  explicit estimate for the size of the solutions. As a special case, C(n,k)=C(m,l)
  with fixed k,l has finitely many solutions, ineffectively.
hypotheses: k,l fixed; A,B fixed positive; the underlying binom/product curve has
  positive genus and is irreducible (established in [6]).
holds-here: yes — this is exactly the per-pair finiteness (via Siegel) that MRSTT
  Remark 1.5 relies on for the boundary, and its ineffectivity in the pair (k,l)
  is the reason no uniform-in-k effective bound comes from it.
status: asserted-by-source (coauthor's own survey; the theorem is cited [6]
  Beukers-Shorey-Tijdeman, Number Theory in Progress 1 (1999) 11-26, not re-derived)
bearing: names the primary source of the "finiteness is not a bound" obstruction;
  the only uniform-in-k effective analogue in the survey is the fixed-m constrained
  equation (10.2), whose hypothesis does not hold for the binomial problem.
anchor: research/summaries/shorey-tijdeman-survey.md
```

```claim
id: saradha-shorey-fixedm-effective
statement: For A=B=1 and k+l an integral multiple of k (i.e. products in ratio
  1:mk, m fixed >=2), Saradha-Shorey (via a Runge-method extension to exponential
  Diophantine equations) proved max(x,y,k) is bounded by a number depending only on
  m — an effective bound uniform in k for that restricted product equation.
hypotheses: A=B=1; k+l = mk with m fixed; x>0,y>0,k>=2.
holds-here: no (as a uniform bound for Singmaster). The hypothesis k+l=mk with m
  fixed is foreign to C(n,k1)=C(y,k2), where k1,k2 are the independent small
  parameters of two different binomial coefficients. The failure of this hypothesis
  is the reason the clean effective-uniform result does not transfer.
status: asserted-by-source (survey §10; [33] Saradha-Shorey, Indag. Math. N.S. 3
  (1992) 79-90)
bearing: documents the one known effective uniform-in-k result for a product/binomial
  family and explains precisely why its hypothesis fails for Singmaster — closing
  the gap with an exact name rather than a vague hope.
anchor: research/summaries/shorey-tijdeman-survey.md
```
