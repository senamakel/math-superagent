# Gouillon 2006 — Explicit lower bounds for linear forms in two logarithms

Source: Nicolas Gouillon, *Journal de Théorie des Nombres de Bordeaux* 18 (2006) no. 1, 125–146.
URL: https://jtnb.centre-mersenne.org/item/10.5802/jtnb.537.pdf (also
http://jtnb.cedram.org/item?id=JTNB_2006__18_1_125_0). Full text held at
`research/sources/gouillon-two-logarithms-2006.full.md`.

## What it establishes

For nonzero algebraic numbers α1, α2 with chosen nonzero log determinations and
nonzero integers b1, b2, the paper gives explicit lower bounds for
`Λ = b1 log α1 − b2 log α2`. It specializes Schneider's method with multiplicity
(interpolation determinants, Masser-type multiplicity estimate) to the
two-logarithm case and optimises the numerical constraints, improving the
effective constant in the two-logarithm case from ≈ 10^8 (Baker's method, e.g.
Matveev's Corollary 9.22 in Waldschmidt's book; around 10^8) down to ≈ 5·10^4.

**Main theorem (Thm 2.1)** is a fully parameterised bound (K, L, T_j, R_j, S_j,
E ≥ e parameters; N = (K+1)(K+2)(L+1)/2; V defined; conclusion log|Λ′| ≥ −V
with an adjusted Λ′). All corollaries follow from it by an explicit choice of
parameters (Section 5) — the constants below are not black boxes but computed
specialisations.

**Corollary 2.2** (α1, α2 multiplicatively independent; complex algebraic):
with `b = b1/D·log A2 + b2/D·log A1` and
`h = max{log b + 3.1, 1000/D, 498 + 284/D + 142 log D}`,

```
log |Λ| ≥ −9400 (3.317 + 1.888/D + 0.946 log D) D⁴ h log A1 log A2
```

**Corollary 2.3** (same, plus α1, α2 real > 0 with real positive logarithms):

```
log |Λ| ≥ −7200 (3.409 + 1.705/D + 0.946 log D) D⁴ h log A1 log A2
h = max{log b + 3.1, 1000/D, 512 + 256/D + 142 log D}
```

**Corollary 2.4** (log α1, log α2 positive and linearly independent over Q):
`log |Λ| ≥ −8550 D⁴ h log A1 log A2 log(E*)(log E)^{-3}`, with E, E*, h defined
in terms of D, A1, A2 and the determinations; best when the ratio log α1/log α2
is far from rational.

Notation: `D = [Q(α1,α2):Q]/[R(α1,α2):R]`; `h(α)` is the absolute logarithmic
height; `A1, A2 > 1` must satisfy `log Ai ≥ max{h(αi), |log αi|/D, 1/D}`.
The h-defining constant 1000 (resp. 265 in Cor 2.4) is arbitrary; the other
constants depend on it. Asymptotically in b the multiplicative constants are
≈ 8800, 6800, 8450 (Cors 2.2, 2.3, 2.4) — roughly the square root of the
Baker/Matveev constants.

## Relevance to this run

The adopted approach `baker-linear-forms-two-logarithms` needs an explicit lower
bound for `Λ = k1 log n1 − k2 log n2 − log(k1!/k2!)` with a **computed** constant.
Gouillon Cor 2.2/2.3 is the specialised two-logarithm bound: for the run's
integer case (K = ℚ, so D = 1; αi integers, h(αi) = log(max(|num|,|den|))),
Cor 2.3 reads

```
log |Λ| ≥ −7200 (4.554) · h · log n1 · log n2   (D = 1)
```

i.e. about −32789·h·log n1·log n2, with h ≈ log b + 3.1 for large b. This is
orders of magnitude sharper than Matveev 2000 Thm 2.3 (which the same approach
file previously proposed to use, constant ≈ 1.12·10^7). Gouillon is therefore
the **independent constant supplier / cross-check** for that computation, and
it is now held in the library.

Caveat to state with the bound: the third term log(k1!/k2!) is a logarithm of a
rational, so the linear form has all coefficients in ℚ and D = 1, but the
multiplicative-independence hypothesis and the exact A1, A2, b specialisation
must be checked per pair (k1,k2) before quoting the number. The paper supplies
the theorem; the per-pair computation is a task for the run's own tools.

## Status

`asserted` — sourced from the primary, not independently re-derived in this
workspace. The constants are stated as in the paper (Corollaries 2.2–2.4, §5.4
numerical appendix gives refined tables for h fixed).

```claim
id: gouillon-two-logarithm-bound-explicit
statement: For multiplicatively independent nonzero algebraic α1,α2 (real >0, log
  determinations real), nonzero integers b1,b2, D=[Q(α1,α2):Q]/[R(α1,α2):R],
  A1,A2>1 with log Ai>=max{h(αi),|log αi|/D,1/D}, b=b1/D·log A2+b2/D·log A1,
  h=max{log b+3.1, 1000/D, 512+256/D+142·log D}, the linear form
  Λ=b1·log α1−b2·log α2 satisfies log|Λ| >= −7200·(3.409+1.705/D+0.946·log D)
  ·D⁴·h·log A1·log A2 (Cor 2.3; Cor 2.2 is the complex version with 9400,
  (3.317+1.888/D+0.946·log D), 498+284/D+142·log D; Cor 2.4 refines when
  log α1/log α2 is far from rational). For K=Q (D=1, αi rational integers or
  rationals) the Cor 2.3 bound reads log|Λ| >= −32789·h·log A1·log A2
  (7200·4.554=32788.8). Constants ≈ 10^4, an order of magnitude below the
  10^7–10^8 Baker/Matveev two-logarithm constants.
hypotheses: α1,α2 nonzero algebraic, multiplicatively independent; log α1, log α2
  nonzero determinations; b1,b2 nonzero integers; h,A1,A2,b,D as in the
  statement; for Cor 2.3 additionally α1,α2>0 real.
holds-here: yes — the run's target form Λ=k1·log n1−k2·log n2−log(k1!/k2!) has
  all logarithms of rationals, so D=1 and heights are logs of integers; the
  multiplicative-independence hypothesis needs per-pair verification.
status: asserted
bearing: the explicit-constant supplier and independent cross-check for approach
  baker-linear-forms-two-logarithms; makes the GOAL-eligible per-pair effective
  bound computable in the two-logarithm formulation.
anchor: research/summaries/gouillon-two-logarithms-2006.md
```