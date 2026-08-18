# Gasull–Santana, "On a variant of Hilbert's 16th problem" (arXiv:2405.04281)

- **src**: https://arxiv.org/abs/2405.04281  (final v3, 26 Sep 2024)
  Full HTML: https://arxiv.org/html/2405.04281v3
  Related DOI: 10.1088/1361-6544/ad8c1b (published in Nonlinearity)
- **Full texts held**:
  - `research/sources/gasull-santana-monomial-hilbert-variant-arxiv.full.md` (abstract page)
  - `research/sources/gasull-santana-monomial-hilbert-variant-arxiv-html.full.md` (full HTML, 452 lines)
- **Authors**: Armengol Gasull (UAB), Paulo Santana.

## What the paper does

Counts limit cycles by **number of monomials** rather than degree. Define

```
M_m = { planar polynomial vector fields with exactly m monomials }
H^M(m) = sup { pi(X) : X in M_m },   pi(X) = number of limit cycles of X
```

Very little was known: from Buzzi et al [9], H^M(m)=0 for m in {1,2,3},
H^M(m) >= m-3 for m>=4, and H^M(m_k) >= N(m_k) of order O(m ln m) on a sequence
(a bound that follows from the O(n^2 ln n) lower bound on H(n) via Liénard-type
fields).

**Theorem 1.** For m >= 9,  H^M(m) >= (1/2)m^2 - 3m - 8.  (quadratic growth, O(m^2))

This is a corollary of the sharper Proposition 1: for any non-negative integers
n,r there are planar polynomial vector fields with n+r+4 monomials and at least
2n(r+1) + n(1 + (-1)^r) limit cycles.

**Theorem 2.** Small m:
- H^M(4) >= 12, H^M(5) >= 12, H^M(6) >= 12
- H^M(7) >= 16, H^M(8) >= 20, H^M(9) >= 24, H^M(10) >= 32

Previously only H^M(9) >= 24 was known (computed-assisted, Bréhard et al, a
quartic with 24 limit cycles and 9 monomials; the present paper reproduces it
with a direct proof).

## Methods

- **Abelian integrals** (Poincaré–Pontryagin / Melnikov criterion), Theorem 3 /
  Corollary 1 and a Liénard-type family (the second illustrative family (2),
  used for H^M(9) >= 24).
- **Reversible-center constructions** and **weak-focus cyclicity** (used for the
  first family (1), the planar-S system, for H^M(4) >= 12).
- The (1/2)m^2 - 3m - 8 quadratic bound uses an Abelian-integral argument and is
  self-contained.

## Why it matters to this run

1. **The n²log n lower bound on H(n) is reproduced and sharpened in the
   monomial-count setting.** This corroborates `h16-canard-asymptotic-lower-
   bound-2020` / `h16-bd-abelian-linear-in-m` from an independent 2024 source.
2. The monomial-count variant H^M(m) is a genuinely **adjacent problem** the
   library previously had no source on; it is a natural test-bed for the
   adopted approach `abelian-picard-fuchs-argument-principle-sharp-count`
   (sharp zero-counts of Abelian integrals are the paper's engine).
3. It records that a quartic field with 24 limit cycles and only 9 monomials
   exists (computed-assisted, Bréhard et al) — a data point used in the
   H(n)>=28 lower bound picture (degree 4 already exceeds H(4)>=28's count via
   few monomials).

## Status

- Paper is **published** (Nonlinearity, doi:10.1088/1361-6544/ad8c1b), so its
  claims are not mere preprints.
- All claims below are **asserted-by-source** (I have read the statements, not
  re-derived them).
- No claim here concerns the DRR graphics / finite cyclicity directly.
