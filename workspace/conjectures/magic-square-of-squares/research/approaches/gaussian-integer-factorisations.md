# Approach: Gaussian-integer factorisations of the four centre APs

```approach
idea: Use the standard parametrisation of each AP of squares through the centre
c = e² = m²+n², d = 2mn, to express the problem as: find one integer c that
admits four representations c = m_i² + n_i² (i=1..4) linked by the additive
constraints m₁n₁ + m₂n₂ = m₃n₃ and m₁n₁ − m₂n₂ = m₄n₄. In Z[i], each
representation is a factorisation c = π_i π̄_i with N(π_i) = c, and the additive
constraints become linear conditions on Im(π_i²). The hope: the four-
representation requirement forces c to have ≥ 3 distinct prime factors ≡ 1 mod 4,
and the additive constraints impose multiplicative restrictions that no integer
can satisfy simultaneously — a combinatorial contradiction in the distribution of
Gaussian prime factors.
```

## What this reformulation is actually called

This is **the standard sum-of-two-squares / Gaussian-integer parametrisation** of
a three-term AP of squares, and the specific reduction is exactly **Onno Cain's
2019 reformulation**: the 3×3 magic square of squares is *equivalent to solving
quartic polynomials with certain factorisation constraints over an abelian
extension of Q*, and the case where that extension is the Gaussian integers gives
a "new search method".
(arXiv:1908.03236, "Gaussian Integers, Rings, Finite Fields, and the Magic Square
of Squares".)

## Precise statement of the theorem and how it applies

**Fermat's two-squares / Gaussian factorisation:** an integer c is a sum of two
squares c = m²+n² iff every prime ≡ 3 mod 4 divides c to even exponent; the
number of essentially different representations is governed by how many distinct
primes ≡ 1 mod 4 divide c. In Z[i], c = ππ̄ with N(π) = c. The candidate's claim
that four representations force at least 3 distinct primes ≡ 1 mod 4 in c is
correct and standard (r distinct such primes give 2^(r−1) representations up to
symmetry; needing 4 essentially different linked representations needs the prime
factor structure to support them).

**Does this hold here?** Yes — c = e² is a square, so all exponents are even, and
primes ≡ 3 mod 4 appear with even exponent (fine). The parametrisation of each
AP by `c = m²+n², d = 2mn` is exactly what the run's own
`near-miss-baseline-and-incidence` claim realises on Bremner's 7-square witness
(which has `c = 425² = 385²+180² = 408²+119²` giving the two realised AP
differences `v = 2·385·180` and `u+v = 2·408·119`).

## Has anyone applied it to this problem?

**Yes — and it is already in the library.** Cain (2019) pursues exactly this
Gaussian-integer route and obtains a *reformulation plus a search method*, not a
proof of non-existence. The hoped-for final step — a combinatorial contradiction
in the distribution of Gaussian prime factors that no integer can realise — is
**not achieved anywhere in the literature**. The candidate's point "extension
fields change which primes split and how representations behave" is precisely why
MSS exist over Q(√3) (Bremner's extension-field hinge, and Bremner II's Q(√3)
8-square family), which is why an elementary prime-distribution argument that also
forbids the Q(√3) examples would be false.

## What it would buy

A correct reformulation that isolates the `Q`-vs-extension difference in prime
splitting, and (in Cain's hands) a genuinely new search family. It directly
targets the "hinge". But it does **not** currently close: the additive constraints
are **satisfiable** in the sense that Bremner's 7-square witness realises two of
the four AP-difference representations as genuine `c = m²+n²` factorisations —
any contradiction must be delicate enough to allow that witness while forbidding
the fourth.

## Verdict

**status: grounded** — the reformulation is real, named (Cain's quartic/abelian-
extension + Gaussian search reduction), and the necessary-condition part (four
representations force ≥ 3 primes ≡ 1 mod 4) is standard and holds here. But the
proof goal (a global contradiction in the prime distribution) is **open**; the
only literature attempt (Cain) produced a search method, and it must survive
Bremner's witness. Grounded as a reformulation; not grounded as a proof.

## Precedent

- Onno Cain, "Gaussian Integers, Rings, Finite Fields, and the Magic Square of
  Squares", arXiv:1908.03236 (2019): the problem is equivalent to quartic
  factorisation constraints over an abelian extension of Q; Gaussian case = new
  search method; finite-field/ring enumeration conjectures.
  - https://arxiv.org/abs/1908.03236
  - library: `research/summaries/cain-gaussian-integers-magic-square-of-squares-2019.md`
- Bremner, "On squares of squares II", Acta Arith. 99 (2001): the `c = m²+n² =
  r²+s²`, `d = 2mn` parametrisation used throughout; the 7-square witness and its
  two realised `c = x²+y²` splittings; the Q(√3) 8-square families. (library:
  `research/summaries/bremner-on-squares-of-squares-II-2001.md`)
- Bremner, "On squares of squares", Acta Arith. 88 (1999): extension-field MSS
  exist; the hinge. (library: `research/summaries/bremner-on-squares-of-squares-1999.md`)

## First step (if pursued)

Follow Cain's quartic/abelian-extension formulation rather than re-deriving it;
treat the "≥ 3 primes ≡ 1 mod 4" necessary condition as a check, and test any
prospective contradiction against Bremner's witness (which realises two of the
four factorisations, so the constraint system is genuinely non-empty).
