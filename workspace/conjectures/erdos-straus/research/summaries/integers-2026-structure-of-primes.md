# Chamberland, "The Erdős–Straus Conjecture and the Structure of Primes" (Integers 2026)

Source: https://zenodo.org/records/19403738 (Integers: Electronic J. Combin.
Number Theory 26 (2026), #A42; author Marc Chamberland, Grinnell College).
DOI: 10.5281/zenodo.19403738.
Full text: `research/sources/integers-2026-structure-of-primes.full.md`

## What it establishes (sourced, primary journal article)

**Theorem 1 (Type-II iff prime-representation).** Let p be prime. Then 4/p
has a Type-II solution (a ≤ b ≤ c, p ∤ a, p | b and p | c) **iff**

```
p = qr − 4s₁s₂           (2)
```

for some q, r, s₁, s₂ ∈ Z⁺ with `q ≡ 3 (mod 4)` and `s₁, s₂ | (q+1)/4`.

- **Forward direction** builds q = 4b/p − 1, r = 4a − p,
  s₁ = gcd(ab/gcd(a,b), (a+b)/gcd(a,b)), s₂ = gcd(a,b); uses
  Bradford's identity for Type II: `c = ab/gcd(ab, a+b)`.
- **Reverse direction** gives the explicit unit-fraction representation

```
4/(qr − 4s₁s₂) = 1/(r·(q+1)/4 − s₁s₂)
               + 1/((q+1)/4·(qr − 4s₁s₂))
               + s₁s₂/((q+1)/4·(r(q+1)/4 − s₁s₂)·(qr − 4s₁s₂))
```

which is a sum of three unit fractions since s₁, s₂ | (q+1)/4; the last two
denominators contain p = qr − 4s₁s₂, so it is Type II.

**Conjecture 2 (Prime Representation Conjecture).** Every prime p is of the
form (2), i.e. ESC would follow from the PRC.

**Structure results.**
- With s₁,s₂ restricted to {1, (q+1)/4}, the three one-parameter families
  `qr − 4`, `qr − 1`, `qr − (q+1)/4` cover many classes; Table 2 lists the
  classes mod q for q ≤ 23 (e.g. q=11: 11r−1, 11r−3, 11r−4 — these are the
  OEIS A139665 `11n−3`, `11n−4` identities; q=7: 7r−1, 7r−2, 7r−4).
- p = 211 needs q = 43: 211 = 43·5 − 4·1·1. p = 1009 is the smallest prime
  needing s₁ ≥ 3 and s₂ ≥ 3: 1009 = 23·47 − 4·3·6. (Both 211 and 1009 are
  in the open classes mod 840: 211 ≡ 211 (not one of the six); 1009 ≡ 169
  mod 840 — so 1009 is in the open class 169!)
- p ≡ 3 mod 4 handled by two explicit Type-II solutions.
- Six examples of 4/41 Type-II representations in Table 1.

**Hand-verification of the reverse-direction identity (exact algebra, done
in this run).** Let T = (q+1)/4, P = qr − 4s₁s₂, A = rT − s₁s₂. The claim is
4/P = 1/A + 1/(TP) + s₁s₂/(TAP). Common denominator TAP: RHS numerator
= TP + A + s₁s₂ = T(qr−4s₁s₂) + rT − s₁s₂ + s₁s₂ = rT(q+1) − 4Ts₁s₂
= 4rT² − 4Ts₁s₂ = 4T(rT − s₁s₂) = 4TA. So RHS = 4TA/TAP = 4/P. ∎
(Should be confirmed mechanically by `is_identity` before any claim relies
on it; the algebra is exact as written.)

## Relation to the library

- This is a **necessary-and-sufficient Type-II characterisation** matching
  Schuh 2025 Theorem 2B (four-parameter family) and the classical
  Elsholtz–Tao Type-II parametrisation. It confirms from a journal source the
  boundary: Type-II solutions of primes are exactly an open-arith-progression /
  divisor-condition family, and the open classes mod 840 are precisely where
  the "first branch" (q ≤ 23 with small s₁,s₂) is exhausted.
- p = 1009 in open class 169 shows Type-II solutions DO reach the open
  classes — the obstruction is not "no Type-II family reaches them", it is
  that no *single* polynomial identity covers them (Schinzel).

## Consequence for this run

A family for n ≡ 1 (mod 840) can be sought as `840k + 1 = q·r(k) − 4s₁s₂` with
q ≡ 3 mod 4 fixed, r(k) a polynomial, and s₁,s₂ chosen as divisors of (q+1)/4
— this is exactly the ansatz space where Type-II solutions live, and the
obstruction to watch is Schinzel's: any such identity with s₁,s₂ constant
fails when 840k+1 is a quadratic residue class (which it is for the six). The
1009 = 23·47 − 4·3·6 example shows r must vary with k to escape Schinzel, or
the family must use non-constant s₁,s₂/k.

```claim
id: chamberland-type2-iff-primes
statement: For prime p, 4/p has a Type-II solution iff p = qr − 4s₁s₂ with q ≡ 3 (mod 4), s₁, s₂ | (q+1)/4; the reverse direction gives an explicit 3-term Type-II representation.
hypotheses: p prime; Type-II = exactly two denominators divisible by p.
holds-here: true — the six open classes are prime classes; the iff is a complete parametrisation of Type-II solvability.
status: sourced (Integers 26 (2026) #A42, published journal article; proof in full text; consistent with Schuh Thm 2B and Elsholtz–Tao Type-II description).
bearing: the exact ansatz family for Type-II coverage of n ≡ 1 (mod 840); combined with Schinzel's polynomial obstruction it bounds what a polynomial family can do.
anchor: research/sources/integers-2026-structure-of-primes.full.md
```

```claim
id: chamberland-1009-open-class-169
statement: p = 1009 = 23·47 − 4·3·6 is the smallest prime requiring s₁ ≥ 3 and s₂ ≥ 3 in the Type-II representation; 1009 ≡ 169 (mod 840), i.e. 1009 lies in one of the six open classes and has an explicit Type-II solution.
hypotheses: none.
holds-here: true — witness that the open classes do contain primes with Type-II solutions.
status: sourced (Chamberland 2026, §3; computation of residue class verified here: 1009 mod 840 = 169).
bearing: falsifies any claim that the open classes have no Type-II solutions at all; the obstruction is about uniform covering families, not individual solvability.
anchor: research/sources/integers-2026-structure-of-primes.full.md
```