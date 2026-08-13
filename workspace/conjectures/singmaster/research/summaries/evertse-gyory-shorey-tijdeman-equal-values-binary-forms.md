# Evertse–Győry–Shorey–Tijdeman 1987 — "Equal values of binary forms at integral points" (PRIMARY, now held in full)

Source: Jan-Hendrik Evertse, Kálmán Győry, T.N. Shorey, R. Tijdeman, "Equal
values of binary forms at integral points", Acta Arithmetica 48 (1987)
379–396.
Full text held (previously a dead landing-page download):
`research/sources/evertse-gyory-shorey-tijdeman-equal-values-binary-forms.full.md`
(author-repository PDF via CWI ir.cwi.nl/pub/1712/1712D.pdf). Authors:
Evertse (Amsterdam/CWI), Győry (Debrecen), Shorey (Tata Bombay), Tijdeman
(Leiden). Received 30.12.1985.

## What the paper establishes

The subject is **equal values of binary forms**: equations `F(x,y) = G(x,y)`
(and the more general `z·F(x,y) = G(x,y)·p₁^{k₁}···p_r^{k_r}` Thue–Mahler-type
shape) where `F`, `G` are homogeneous polynomials in two variables with
integer (or algebraic-integer) coefficients. Key structural quantity: `w(F)`,
the maximal number of **pairwise non-proportional linear factors** of `F` over
`C` (so `w(F) = 3` means at least three genuinely different directions).

The theorems, in increasing generality, all assume some `w(...) ≥ 3` and give
**effectively computable** constants:

- **Theorem 1 / Corollary 2–4.** If `F, G` are relatively prime binary forms
  with `F/G` not a constant multiple of a power of a linear or an indefinite
  quadratic form, then the solutions of `F(x,y)=G(x,y)`, `(x,y)=1` satisfy
  `max(|x|,|y|)` bounded by an effectively computable number depending only on
  the degrees and heights of `F` and `G`. (Effective magnitude bound on the
  equal-value solutions.) Corollary 3 recovers the Shorey–Tijdeman result for
  `deg F > deg G`.

- **Theorem 2 (eq. (6)).** Under `w(F₁···F_r G₁···G_s) ≥ 3`, every solution of
  `F(x,y)=G(x,y)` (F∈𝓕, G∈𝓖, multiplicative powers of a fixed finite list of
  base forms), `(x,y)=1`, satisfies
  `max(|x|,|y|) < exp{ (r+s) n⁴ ( C₄(t+1)log P)^{1+1} P^{r/5} log H }`
  (OCR-fractured but the shape is clear: an explicit exp-of-polynomial bound in
  the degrees `n`, the number `r+s` of base forms, the set `t`/largest norm `P`
  of the primes, and the height `H`). `C₄`, `C₅` effectively computable, `C₄`
  depending on the splitting field `L` (degree `l`, regulator `R_L`, class
  number `h_L`), `C₅` on `l` alone.

- **Theorem 3.** The **number** of pairs `(x,y)∈Z²` solving `F(x,y)=G(x,y)`
  for some `F∈𝓕`, `G∈𝓖` is at most ~`2·r^{3(2r+3)}` (exponent OCR-garbled;
  the paper stresses the bound is **independent of `r`, `s`, `P`, `H` and `L`**
  — i.e. an absolute constant once the base-form list is fixed). This is the
  Subspace-Theorem-shaped *count* bound: the number of equal-value solutions is
  bounded by a constant, while Theorem 2 bounds each solution's size.
  Proof route (Section 2): reduce (10) to a Thue–Mahler equation, then apply
  Evertse 1984 (S-unit / Thue–Mahler count via the Thue–Siegel method) and
  Győry 1981 (Baker's linear-forms-in-logarithms method). Both are cited as
  the two engines.

- **Theorem 4–6.** The relative (number-field) generalization with the
  denominator `(x,y)^{deg}` normalizing powers, `N(⟨x,y⟩) ≥ N₀`, and a count
  of points on `P¹(K)`. Theorem 6 generalizes the count bound to `O_K`.

## Bearing for this run — what it does and does NOT establish

**Relevance:** this is the *closest published application of the Subspace /
S-unit method to a bound on factorial-type equal-value equations* — the anchor
the run's `sunit-subspace-inapplicable` approach cites for "per-form
Subspace-Theorem constants". That citation is now **primary-backed**: EGST
really does give (Thm 3) an absolute-parameter-independent count bound and
(Thm 1–2) effective size bounds for `F(x,y)=G(x,y)` when `w(FG)≥3` and the
degenerate `F/G = const·(linear or indefinite quadratic)^power` case is excluded.

**The genuine gap — do NOT overstate applicability:** the theorems are stated
for **binary forms in two variables**, i.e. `F(x,y)` homogeneous. The run's
equation is `C(x,k₁) = C(y,k₂)`, a *separated-variable* equation between two
**univariate** polynomials `P_{k}(X) = X(X-1)···(X-k+1)/k!`. It is **not**
literally of the binary-form shape `F(x,y)=G(x,y)`. To apply EGST one must
homogenize: `P_k(X,Z) = X(X-Z)···(X-(k-1)Z)/k!` is a degree-`k` binary form in
two variables `(X,Z)` **with `w(P_k) ≥ 3` for `k ≥ 3`** (the linear factors
`X - jZ`, `j=0..k-1`, pairwise non-proportional). But the equal-value equation
then reads `P_{k₁}(X,Z) = P_{k₂}(Y,Z)` — a relation among **three** variables
`(X,Y,Z)`, which is not the two-variable `F(x,y)=G(x,y)` form EGST's theorems
count. The separated-variable (univariate) case is governed instead by
Bilu–Tichy 2000 and the Beukers–Shorey–Tijdeman 1999 equal-products
classification (both already held). So **EGST does not by itself yield even a
per-pair bound on `N(a)`**; it is corroborating method-level support for the
Subspace approach's per-form constants, not a transferable theorem for the
binomial family. The run should keep `bilu-tichy-classification` /
`bst-fixed-kl-effective` as the governing machinery, and treat EGST as the
binary-form template whose `w ≥ 3` nondegeneracy condition and
absolute-count-bound structure it would like — but which fails to apply because
the homogenized binomial equation is three-variable.

**Ineffective-vs-effective:** EGST's bounds are **effective** (computable
constants), paralleling BST 1999's Thm 1.1 finiteness — but, like BST, the
constants depend on the degrees/heights (growing with `k₁,k₂`), so no
**uniform-in-k** constant emerges. It reinforces `effective-methods-wall`: even
the best effective equal-value machinery gives per-curve constants, not a
Singmaster `B`.

## Status

`egst-1987-landing-only` (previously marked "no usable statement") is now
**superseded**: the primary is held and readable. New claim file below replaces
it. The `sunit-subspace-inapplicable` citation of EGST for per-form constants
is now sourced, and its applicability limits (three-variable gap) are stated
exactly.

```claim
id: egst-1987-equal-values-binary-forms-primary
statement: Evertse-Gyory-Shorey-Tijdeman 1987 (Acta Arith. 48, 379-396) proves,
  for F,G relatively prime integer binary forms with F/G not a constant multiple
  of a power of a linear or indefinite quadratic form and w(FG)>=3: (Thm1/Cor4)
  solutions of F(x,y)=G(x,y), (x,y)=1, satisfy max(|x|,|y|) < C(F,G) effectively
  computable from degrees+heights; (Thm2) an explicit exp bound; (Thm3) the NUMBER
  of solutions is bounded by an absolute constant independent of r,s,P,H,L once
  the base forms are fixed. Method: reduce to Thue-Mahler, then S-unit count
  (Evertse 1984, Thue-Siegel) + Baker linear forms (Gyory 1981).
hypotheses: F,G are BINARY FORMS in two variables (x,y); w(FG)>=3; F/G not a
  degenerate power of a linear/indefinite-quadratic form; (x,y)=1.
holds-here: no — the run's equation C(x,k1)=C(y,k2) is separated-variable (two
  UNIVARIATE polynomials), not a binary-form equality; the homogenization
  P_k(X,Z) is degree-k with w>=3 for k>=3 but the equal-value equation is then
  three-variable, outside EGST's two-variable form; so EGST's hypotheses do not
  hold for the binomial family.
status: checked (primary held, readable in full)
bearing: CORROBORATES sunit-subspace per-form constants at primary level; does
  NOT transfer to N(a) because the binomial family is not a binary-form equality
  in two variables — the separated-variable case is governed by Bilu-Tichy/BST,
  already held. Consistent with effective-methods-wall (constants grow with
  deg/height, no uniformity).
anchor: research/sources/evertse-gyory-shorey-tijdeman-equal-values-binary-forms.full.md
```

## Note on the artefacts in the text

The OCR of the CWI PDF is fractured (e.g. "OJ" for `ω`, garbled superscripts in
Thm 2–3). The quantitative shape of Thm 2 (exp of a polynomial in r+s, n⁴,
(t+1)log P, P^{r/5}, log H) and the "independent of r,s,P,H,L" remark for Thm 3
are clear even where the exact exponents are not fully legible. Any later agent
quoting a precise Thm 2/3 constant must re-read the full text rather than trust
this summary's OCR-affected digits.
