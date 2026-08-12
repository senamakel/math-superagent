# Approach: Gaussian-integer factorisations of the four centre APs

```approach
idea: Use the standard parametrisation of each AP of squares through the centre
c = e² = m²+n², d = 2mn, to express the problem as: find one integer c that
admits four representations c = m_i² + n_i² (i=1..4) linked by the additive
constraints m₁n₁ + m₂n₂ = m₃n₃ and m₁n₁ − m₂n₂ = m₄n₄. In Z[i], each
representation is a factorisation c = π_i π̄_i with N(π_i) = c, and the additive
constraints become linear conditions on Im(π_i²).
status: refuted
killed-by: The approach does not differ from what Onno Cain (arXiv:1908.03236)
  already published as a search method, and no prime-distribution contradiction
  is in reach. The Chabauty–Coleman candidate attacks the explicit quartics that
  Bremner II already wrote down (eq. 12-13); this candidate reduces to a search
  family that Bremner and Cain both explored without closing. Moreover the
  representation-count necessary condition (centre ≥ 5 representations: Brown's
  Prop. 1) is a single number-theoretic filter rather than a structural argument,
  and Bremner's 7-square witness already realises two of the four factorisations,
  so any contradiction must survive that witness while forbidding a fourth —
  exactly the delicacy that has resisted decades of work. Adopted instead:
  Chabauty–Coleman on the explicit Bremner II quartics, which has a concrete
  computable first step (genus + rank of the eq. 13 curves at λ=13).
precedent: Onno Cain, "Gaussian Integers, Rings, Finite Fields, and the Magic
  Square of Squares", arXiv:1908.03236 (2019); Bremner II §2 eq. (12)-(13).
first-step: none — this candidate is a search reformulation that does not advance
  beyond what Cain and Bremner already attempted, and Chabauty–Coleman on the
  explicit quartics is the stronger line.
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

```claim
id: hilbert-symbol-of-two-squares-trivially-split
statement: If c±d are both squares (A^2,B^2), then the quaternion algebra
  (c+d,c-d) has Hilbert symbol (A^2,B^2)_p=1 at every prime, so it is the zero
  element of Br(Q); every AP-of-squares difference gives a trivially-split
  algebra, and no Hilbert-reciprocity/local-invariant contradiction can arise at
  the level of Q. Geometrically all AP points on X^2+Y^2=2c, which is locally
  soluble everywhere, so Hasse-Minkowski gives no obstruction.
hypotheses: c,d rationals with c±d rational squares
holds-here: yes (every realised AP difference in Bremner's witness satisfies this)
status: proved (bimultiplicativity of the Hilbert symbol; Hasse-Minkowski for
  ternary/conic forms)
bearing: rules out the Hilbert-reciprocity/four-conics line and any Q-level
  quaternion local-obstruction; forces higher-dimension (K3/Brauer-Manin) tools
anchor: research/approaches/hilbert-reciprocity-four-conics.md
```

```claim
id: gaussian-factorisation-is-cains-reformulation
statement: The Gaussian-integer factorisation of the four centre APs is exactly
  Onno Cain's arXiv:1908.03236 reformulation: the 3x3 MSS problem is equivalent
  to quartic factorisation constraints over an abelian extension of Q, and the
  Gaussian case yields a new search method, not a proof; no prime-distribution
  contradiction is established anywhere.
hypotheses: c=e^2 a square, four AP representations, additive constraints
holds-here: yes (the reformulation; Bremner's witness realises two factorisations,
  so the constraint system is non-empty)
status: asserted (per Cain's abstract/claim; verified reformulation standard)
bearing: grounds the candidate as a search reformulation; its proof goal remains open
anchor: research/approaches/gaussian-integer-factorisations.md
```
