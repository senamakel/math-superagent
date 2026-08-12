# Variations on Euclid's Formula for Perfect Numbers (Firoozbakht & Hasler, JIS 13, 2010)

<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL13/Hasler/hasler2.html | full text: research/sources/hasler_firoozbakht_euclid_formula_perfect.full.md -->

## What it establishes

Firoozbakht & Hasler study families of integer solutions to linear equations
of the form

    sigma(n) = A·n + B(n),

where B may depend on properties of n. This covers perfect (B=0), multiperfect
(sigma(n)=kn), quasiperfect (sigma(n)=2n+1), near-perfect, and other
sigma-linear characterizations. The paper derives several parametric families
generalizing Euclid's even-perfect-number formula and links them to many OEIS
sequences (e.g. A007691 multiperfect, A001599 harmonic divisor numbers).

## Relevance to PE 241

- Hemiperfect condition is 2·sigma(n) = (2k+1)·n, i.e. sigma(n) = A·n with
  A = (2k+1)/2 — a half-integer multiple. This is the special case B=0,
  A half-integer, lying within the sigma(n)=A·n family.
- The paper's parametric constructions (Euclid-style for mersenne-type primes)
  give *infinite-family* intuition for multiply perfect numbers, but the
  half-integer case (hemiperfect) is NOT among the parametric families
  constructed; the known rarity of hemiperfects (22 below 10^18, only k≤5
  reachable below A088912's a(6)≈1.7e44) is consistent with no such family
  existing for half-integer abundancy.
- Provides no enumeration algorithm; the catalogued OEIS links reinforce the
  multiplicative sigma structure that the DFS solver already uses.

Adjacent/background source confirming the multiplicativity and the
sigma(n)=A·n framing; not the source of the enumeration method.
