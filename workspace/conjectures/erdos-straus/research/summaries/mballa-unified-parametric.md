# Mballa, "A unified parametric approach to the Erdős–Straus conjecture with explicit solutions for a set of integers of natural density one"

Source: arXiv:2602.20036 (23 Feb 2026, v2 22 Mar 2026), HTML: https://arxiv.org/html/2602.20036v2
Full text: `research/sources/mballa-unified-parametric.full.md`

## What it establishes (sourced, primary)

Symmetric (y = z) solutions. Defines `F(k)_{x,t}(n) = t²(kx − n)² − 2nxt`;
zeros of F produce symmetric solutions with `y = z`. Proves a Zero Lemma: a
zero of F on the admissible domain `D(k)_{x,t}` forces n to be the domain's
upper bound. For k = 4 (Erdős–Straus):

- Explicit symmetric solutions for `n ≡ 0, 2, 3 (mod 4)` — 75% of integers —
  (these are of course covered by the classical identities; the point is the
  unified F-based framework).
- For `n ≡ 1 (mod 4)`: symmetric solutions exist when n has a divisor
  `b ≡ 3 (mod 4)`; proved for **almost all** such n, so the exceptional set
  has natural density zero. The conjecture is thus verified (by explicit
  symmetric families) for a proportion approaching 1 within the `n ≡ 1 (mod 4)`
  class — including infinitely many new explicit families not covered by
  Mordell.

## Consequence

The `n ≡ 1 (mod 4)` divisor-condition (existence of `b ≡ 3 (mod 4)`) is
exactly the same structure Ventas uses (`d ≡ 3 (mod 4)` divisor of shifted
integers) — two independent families converging on the same mechanism for the
hard class. Since the six open classes are contained in `n ≡ 1 (mod 4)`, a
run targeting `n ≡ 1 (mod 840)` should check whether the divisor `b ≡ 3
(mod 4)` condition can be made to hold **identically** for a polynomial
sub-family (e.g. `b = 4k+3` dividing a quadratic in k), which would be a new
positive-density family inside the open class.

```claim
id: mballa-symmetric-density
statement: For k=4, explicit symmetric solutions (y=z) exist for all n ≡ 0,2,3 (mod 4), and for n ≡ 1 (mod 4) when n has a divisor b ≡ 3 (mod 4); the latter holds for almost all n ≡ 1 (mod 4), so the conjecture is verified by explicit families for a proportion tending to 1 in that class.
hypotheses: k=4 Erdős–Straus; divisor b ≡ 3 (mod 4) condition.
holds-here: true — the six open classes are inside n ≡ 1 (mod 4).
status: sourced (arXiv:2602.20036; density-zero exceptional set proved).
bearing: the b ≡ 3 (mod 4) divisor mechanism is a concrete target for a polynomial sub-family inside the open classes; check if it can be made to hold identically on n = 840k+1.
anchor: research/sources/mballa-unified-parametric.full.md
```