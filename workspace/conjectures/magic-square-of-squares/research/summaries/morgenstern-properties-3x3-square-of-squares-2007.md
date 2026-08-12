# Morgenstern, "3×3 Magic Square of Squares Properties" (2015) — [[morgenstern-properties-3x3-square-of-squares-2007.full]]

Elementary number-theory proofs of structural restrictions on a primitive MSS (all entries distinct squares, gcd of entries = 1). The parametrisation used is x,y,z (centre x, steps y,z):
```
x+y    x-y-z   x+z
x-y+z    x      x+y-z
x-z    x+y+z   x-y
```
(equivalent to problem.md's c,u,v). The eight APs are: four through centre (steps y, z, y+z, y−z) and four on the pandiagonals (steps y, y, z, z) — Lemma 9. Note: **all nine entries are covered by the four through-centre APs.**

## AP structure (audit of classical facts)
- AP of squares: A²+B²=2C². Primitive APs (gcd(A,B,C)=1) parametrised (Lemma 7): `A=2mn−m²+n², B=2mn+m²−n², C=m²+n²` with m,n coprime, one odd one even. Middle term C=m²+n².
- Theorem 1 (parity): in an AP, A²,B²,C² are all odd or all even.
- Theorem 2: middle term of a primitive AP consists only of 1 (mod 4) primes.
- Theorem 3: an outer term 2r²−s² (of a primitive AP) consists only of 1 and 7 (mod 8) primes.

## MSS restrictions (proved)
- **Theorem 4:** in a primitive MSS, all entries are odd.
- **Theorem 5:** the central entry consists only of 1 (mod 4) primes.
- **Theorem 6:** no entry can have a 3 (mod 8) prime factor.
- **Theorem 7:** no middle-side entry can have a 5 (mod 8) prime factor.
- Theorems 8–9: corner-entry 3 (mod 4) / 5 (mod 8) factors propagate to a couple of other entries (scaling argument).
- **Theorem 10:** in a primitive MSS all entries are 1 (mod 3).
- **Theorem 12:** in the x,y,z formulation, duplicated entries occur exactly when yz=0 (and the y=2z, y=z cases collapse because they'd force 5 or 7 squares in AP, impossible). For yz=0 the only non-trivial possibility is z=0 giving a grid built from one AP (e.g. {49,25,1} family).

## Step-value prime restrictions (Theorems 13–20, infinite-descent proofs)
Put z = p·y, p integer. Then **p ∉ {0,1,2,3,4, any 4k+3 prime, q−1, q+1 for q a 4k+3 prime}**. Proofs are elementary (parity, primitive Pythagorean-triangle descent). p=4 would give six squares in an AP (impossible), p=3 gives nine squares in an AP (impossible), p a 4k+3 prime gives an infinite descent on y.

**Bearing:** These are the strongest sieve/structural facts in the library. They constrain any candidate grid sharply: all entries odd, ≡1 mod 3, centre only-1-mod-4 primes, no 3-mod-8 prime factor anywhere, and the AP step ratio z/y avoids that forbidden set. Any impossibility proof built on the step-value arithmetic must respect (survive) the known 7-square witnesses — and the run's generator can test the forbidden-p set cheaply.

```claim
id: morgenstern-primitive-restrictions
statement: In a primitive 3×3 magic square of distinct squares: all entries are odd and
  ≡1 (mod 3); the central entry has only 1 (mod 4) prime factors; no entry has a 3 (mod 8)
  prime factor; no middle-side entry has a 5 (mod 8) prime factor; and with z=p·y the step
  ratio p avoids {0,1,2,3,4, 4k+3 primes, q±1 (q a 4k+3 prime)}.
hypotheses: primitive (gcd of entries = 1); all entries distinct positive squares
holds-here: yes (these are exactly the objects of the problem, after removing a common
  square factor)
status: proved (elementary number theory, in-source, with full proofs)
bearing: the sharpest sieve constraints available; any candidate grid and any descent must
  satisfy them; the forbidden-p set is trivially testable on the generator output
anchor: research/sources/morgenstern-properties-3x3-square-of-squares-2007.full.md
contradicts: (none; consistent with Bremner's 7-square witness which has all-odd, ≡1 mod 3
  entries)
```
