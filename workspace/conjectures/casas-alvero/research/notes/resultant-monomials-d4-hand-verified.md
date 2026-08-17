# result-monomials structure at d=4 — partial independent hand-verification

Extends the d=3 check (research/notes/verify-monomial-structure-d3.md) to d=4.
This note records what is verified *by hand* and what remains queued to the
executor (code/scholar/verify_monomial_structure.py has no capture yet).

Load-bearing claim `resultant-monomials` (Schaub–Spivakovsky arXiv:2307.05997
Thm 6/9; de Frutos PhD Prop 2.2.1). With f = x^4 + a_1 x^3 + a_2 x^2 + a_3 x
(a_4 = 0), Hasse H_i, R_i = Res_x(f, H_i):

  (A) (-1)^{d-i}(C(d,i)-1)^{d-i} a_{d-i}^d appears in R_i, and a_{d-i}^d are
      the ONLY pure powers in any R_i;
  (B) for i>=2, (-1)^{(d-1)(d-i)} C(d,i)^{d-1} a_{d-1}^{d-i} a_{d-i} is the
      unique degree-(d-i+1) monomial in R_i, all others higher.

## The coefficient identity is literally binomial theorem (always true)

The paper's engine:
  sum_{k=0}^{d-i} (-1)^k C(d-i,k) C(d,i)^k  =  (1 - C(d,i))^{d-i}
                                            =  (-1)^{d-i}(C(d,i)-1)^{d-i}
This is the expansion of (1-x)^n with n=d-i, x=C(d,i). So the pure-power
coefficient of a_{d-i}^d is a closed binomial value for every d,i — no
computational content, exactly as the paper claims.

Spot checks: d=3,i=1: 1-2·3+9=4=(3-1)^2 ✓; d=3,i=2: 1-3=-2=-(3-1) ✓;
d=4,i=2: 1-2·6+36=25=(6-1)^2 ✓; d=4,i=3: 1-4=-3=-(4-1) ✓.

(B)'s coefficient (-1)^{(d-1)(d-i)} C(d,i)^{d-1}: d=3,i=2 gives 9; d=4,i=3
gives -64; both match the fully-computed R_i below.

## Full hand computation of R_3 at d=4

Hasse derivatives: H_1 = 4x^3+3a_1x^2+2a_2x+a_3; H_2 = 6x^2+3a_1x+a_2;
H_3 = 4x+a_1.

R_3 = Res(f, H_3): root of H_3 is x = -a_1/4.
f(-a_1/4) = a_1^4/256 - a_1^4/64 + a_2 a_1^2/16 - a_1 a_3/4
           = -3a_1^4/256 + a_1^2 a_2/16 - a_1 a_3/4.
Res(f,H_3) = 4^4 · f(-a_1/4) = 256 · f(-a_1/4)
           = **-3 a_1^4 + 16 a_1^2 a_2 - 64 a_1 a_3**.

Checks against the claim:
- (A) a_1^4 present, coeff -3 = (-1)^(4-3)(C(4,3)-1)^(4-3) = -3 ✓. Unique pure
  power: a_1^4 is the only single-variable-^4 monomial (a_1^2a_2 and a_1a_3
  each involve two variables) ✓.
- (B, i=3) degree d-i+1 = 2: a_{d-1}^{d-i}a_{d-i} = a_3^1 a_1 = a_1 a_3, coeff
  -64 = (-1)^(3·1) C(4,3)^3 = -64 ✓, and a_1a_3 is the unique degree-2
  monomial (a_1^2a_2 has degree 3, a_1^4 degree 4) ✓.

So the full claim (A)+(B) is verified exactly at d=4,i=3.

## What remains queued (not yet machine-expanded)

- The FULL expansion of R_1 = Res(f,f') and R_2 = Res(f,H_2) at d=4, to
  confirm the *uniqueness* ("a_3^4 only pure power in R_1", "a_2^4 only pure
  power in R_2", "a_3^2 a_2 unique degree-3 monomial in R_2"). The pure-power
  and low-degree coefficients are already fixed by the binomial identities
  (25 for a_2^4, 216 for a_3^2a_2, 27-magnitude for a_3^4); only the
  "no OTHER such monomial" assertion wants the expansion.
- script code/scholar/verify_monomial_structure.py is written and will do
  d=3,4 exhaustively once executed (it has no capture on disk).

## Claim block

```claim
id: resultant-monomials-d4-i3-hand-verified
statement: The Schmidt-Spivakovsky distinguished-monomial structure (claim
  resultant-monomials, Thm 6/9) holds exactly at d=4, i=3: R_3 =
  -3a_1^4 + 16a_1^2a_2 - 64a_1a_3, with a_1^4 the unique pure power (coeff
  -3 = (1 - C(4,3))^(4-3)) and a_1a_3 the unique degree-2 monomial (coeff
  -64 = C(4,3)^3). Coefficient of a_2^4 in R_2 is (1-C(4,2))^2 = 25 and of
  a_3^2a_2 in R_2 is C(4,2)^3 = 216 by binomial theorem (uniqueness at
  i=1,2 not yet machine-expanded).
hypotheses: d=4, Hasse derivatives, a_4=0, Z coefficients
holds-here: yes
status: checked (hand-computed R_3 exactly, independent of the source's
  computation; coefficient identities are closed binomial values; uniqueness
  at i=1,2 is partially open)
follows-from: resultant-monomials
answers: resultant-monomials-verified (at least at i=3)
anchor: research/sources/schaub_spivakovsky_bad-primes_2023.full.md (Thm 6, 9)
falsifies: any d=4 computation of R_3 disagreeing with
  -3a_1^4+16a_1^2a_2-64a_1a_3
```

## Bearing
Same as the d=3 check: this is the engine of the sufficient binomial bad-prime
criterion (bad-prime-criterion) the n=20 frontier rests on. The binomial hard
value is now confirmed at d=4,i=3 mechanically-by-hand; the residual (i=1,2
uniqueness expansions) is queued to the executor rather than claimed.
