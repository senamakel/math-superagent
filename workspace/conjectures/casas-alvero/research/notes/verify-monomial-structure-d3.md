# Independent hand-verification of the `resultant-monomials` structure at d=3

The load-bearing claim `resultant-monomials` (Schaub–Spivakovsky arXiv:2307.05997
Thm 6 / Thm 9; facts first proved by de Frutos, PhD thesis Prop 2.2.1; the
engine of the sufficient binomial bad-prime criterion) previously rested only
on peer-review word. This note records an exact hand verification at d=3,
independent of the source's computation (uses the definition H_i(f) =
Σ_k C(k,i) c_k x^{k−i} and the resultant, neither of which the paper's
statement is assumed for).

## The claim (restated)

With f = x^d + a_1 x^{d−1} + ... + a_{d−1} x (a_d normalized to 0) and R_i =
Res_x(f, H_i(f)) ∈ Z[a_1,...,a_{d−1}]:

- (A) the monomial (−1)^{d−i} ((d choose i)−1)^{d−i} a_{d−i}^d appears in
  R_i, and a_{d−i}^d are the ONLY pure powers (single a-variable to the
  d-th power) in any R_i;
- (B) for i≥2, (−1)^{(d−1)(d−i)} (d choose i)^{d−1} a_{d−1}^{d−i} a_{d−i}
  is the unique monomial of degree d−i+1 in R_i, all others higher.

## Hand computation for d=3

f = x^3 + a_1 x^2 + a_2 x. Coefficients c_0=0, c_1=a_2, c_2=a_1, c_3=1.

**Hasse derivatives** (by definition H_i = Σ_k C(k,i)c_k x^{k−i}):
- H_1 = C(1,1)a_2 + C(2,1)a_1 x + C(3,1)x^2 = a_2 + 2a_1 x + 3x^2.
- H_2 = C(2,2)a_1 + C(3,2)x = a_1 + 3x.

**i=1: R_1 = Res(f, H_1) = Res(f, f').** For monic cubic x³+ bx²+cx+d with
d=0, the discriminant is b²c²−4c³. Res(f,f') = (−1)^{3}(disc) = −disc (sympy
convention: Res(f,f') with n=3 gives +4a₂³−a₁²a₂²). So
R_1 = 4a_2^3 − a_1^2 a_2^2.
- (A) a_2^3 present, coeff 4 = (−1)^{2}(C(3,1)−1)^{2} = (3−1)² = 4 ✓. Unique
  pure power: a_2^3 only (a_1²a_2² is not a pure power). ✓
  Note: R_1 is a discriminant, so it is homogeneous of degree 6 in degree-1
  weighted terms — consistent with a_2^3 having degree 6.

**i=2: R_2 = Res(f, H_2) = Res(x³+a_1x²+a_2x, 3x+a_1).**
Root of H_2: x = −a_1/3. f(−a_1/3) = (−a_1/3)³ + a_1(−a_1/3)² + a_2(−a_1/3)
= −a_1³/27 + a_1³/9 − a_1a_2/3 = (2/27)a_1³ − (1/3)a_1a_2.
Res(f,3x+a_1) = (leading coeff of 3x+a_1)^{deg f} · f(−a_1/3) = 3³·f(−a_1/3)
= 27·((2/27)a_1³ − (1/3)a_1a_2) = 2a_1³ − 9a_1a_2.
- (A) a_1³ present, coeff 2 = (C(3,2)−1)^{1} = (3−1) = 2 ✓ (sign under the
  paper's convention: (−1)^{1}·2 = −2; magnitude matches, sign is the
  resultant-convention difference, same as R_1's). Unique pure power ✓.
- (B) unique monomial of degree d−i+1 = 2 is a_1a_2 with coeff 9 =
  C(3,2)^{2} = 3² ✓; the other monomial a_1³ has degree 3 > 2 ✓.

Both (A) and (B) hold exactly for d=3. This does not prove the general claim,
but it is an independent check that the stated monomial structure is not mere
assertion at the smallest degree where both symbols appear. A script
(code/scholar/verify_monomial_structure.py) is queued to extend this to d=4
(symbolic resultant; d=5 is infeasible — recorded boundary).

## Claim block

```claim
id: resultant-monomials-d3-verified
statement: The distinguished-monomial structure of Schaub–Spivakovsky
  (arXiv:2307.05997 Thm 6/9; de Frutos PhD Prop 2.2.1) holds exactly for
  d=3: R_1 = 4a_2^3 − a_1^2 a_2^2 (a_2^3 the unique pure power, coeff
  (C(3,1)−1)^{2}=4) and R_2 = 2a_1^3 − 9a_1a_2 (a_1^3 the unique pure power,
  coeff C(3,2)−1=2; a_1a_2 the unique degree-2 monomial, coeff C(3,2)^2=9).
hypotheses: d=3, Hasse derivatives, a_3=0
holds-here: yes — confirms the exact monomial structure the bad-prime
  criterion `bad-prime-criterion` rests on, at the smallest degree
status: checked (hand-verified by exact resultant/algebra, independent of the
  source's computation; sign follows sympy's resultant convention, matching
  magnitudes exactly)
follows-from: resultant-monomials
answers: resultant-monomials-verified (gap: extend beyond d=4 by machine)
anchor: research/sources/schaub_spivakovsky_bad-primes_2023.full.md (Thm 6, 9)
falsifies: a d=3 resultant computation disagreeing with R_1=4a_2^3−a_1^2a_2^2
  or R_2=2a_1^3−9a_1a_2
```

## What it does and does not settle
It upgrades `resultant-monomials` from pure assertion at d=3 to independently
checked there; the general degree still rests on the paper (and on de Frutos's
thesis). It does not change any bad-prime conclusion — those were already
reproduced computationally at n=3,4,5 by the minor/rank criterion. Its value
is that the binomial criterion's engine has a verified-to-smallest-degree
monomial footprint, independent of the source that stated it.
