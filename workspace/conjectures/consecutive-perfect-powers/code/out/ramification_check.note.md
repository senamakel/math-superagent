# Note — cyclotomic ramification claim: exact verification (previously asserted)

Programs: `code/out/verify_ram_fast.py`, `code/out/verify_ramification.py`,
`code/scholar_oracle/verify_ramification.py` (all written by earlier roles,
none executed until this run).
Outputs: `code/out/verify_ram_fast.captured.txt` (EXIT 0),
`code/out/verify_ramification.captured.txt` (EXIT 0),
`code/out/scholar_ramification_check.captured.txt` (EXIT 0).

The library claim `zeta-p-ring-of-integers-and-ramification` was
`Evidence: asserted` (Conrad factorize.pdf). Its exact consequences are now
checked by three independent routes, all exact integer arithmetic.

## What was verified, and how

For K = Q(zeta_p), p an odd prime, P = (1 - zeta_p):

1. **N(1 - zeta_p) = p.** The conjugates of 1-zeta_p are 1-zeta_p^j
   (j = 1..p-1), so N(1-zeta_p) = prod_j (1-zeta^j) = Phi_p(1) = p.
   Verified for p in {3,5,7,11,13,17,19} via `sympy.cyclotomic_poly(p).eval(1)`.
2. **u = (1-zeta_p)^(p-1)/p is an integral unit in Z[zeta_p]** — i.e. the
   ideal equality (p) = (1-zeta_p)^(p-1). Two independent exact routes:
   - `verify_ram_fast.py`: reduce (1-x)^(p-1) modulo Phi_p(x) over Z[x];
     every remainder coefficient divisible by p, for all odd primes p <= 97.
     Since N((1-zeta)^(p-1)) = p^(p-1) = N(p), norm-multiplicativity forces
     N(u) = 1: u integral implies u a unit.
   - `verify_ramification.py`: exact resultant norm of the element
     u = (1-zeta)^(p-1)/p in Q(zeta_p) (via `lib.cyclo.Cyclo`, rational
     coefficients, reduced mod Phi_p); N(u) = ±1 and u has integer
     coefficients, for p in {3,5,7,11,13,17,19,23}. Also p/(1-zeta) integral
     (p in (1-zeta)).
3. **Phi_p(X) ≡ (X-1)^(p-1) (mod p)** coefficientwise — total ramification,
   residue degree 1 — for p in {3,5,7,11,13,17,19}.

## What this establishes, and what it does not

- The three exact identities are **verified-numerically for the listed primes**
  (the ideal equality (p) = P^(p-1) and N(P) = p, plus the mod-p congruence),
  by exact integer arithmetic. `verify_ram_fast.py` covers all odd primes
  p <= 97 for the integrality-of-u statement; the unit-norm statement is
  verified to p = 23.
- It does **not** prove the ring-of-integers equality Z[zeta_p] = O_K for all
  p (that needs the monogenicity/discriminant argument, still asserted by
  Conrad), and it does not prove the ramification claim for all p. The
  evidence tier of claim `zeta-p-ring-of-integers-and-ramification` is
  upgraded from `asserted` to `checked` for the stated ranges.

## Falsifier placement (the known solution)

The known solution 3^2 - 2^3 = 1 has p = 2 (even). Q(zeta_p) with p an odd
prime never arises for it. These ring-theoretic identities hold for every odd
prime p independently of any solution, so they neither include nor exclude the
known solution — the claim's hypothesis gate (p odd prime) excludes it.

```claim
id: ramification-check-exact
statement: >
  For p in {3,5,7,11,13,17,19}: N_{Q(zeta_p)/Q}(1-zeta_p) = Phi_p(1) = p;
  u = (1-zeta_p)^(p-1)/p is an integral cyclotomic integer with exact
  norm ±1 (hence a unit), so (p) = (1-zeta_p)^(p-1) as ideals; and
  Phi_p(X) ≡ (X-1)^(p-1) (mod p) coefficientwise. For every odd prime
  p <= 97 the remainder of (1-x)^(p-1) mod Phi_p(x) has all coefficients
  divisible by p (u integral in Z[zeta_p]).
hypotheses: p an odd prime; exact integer arithmetic (sympy Poly over Z,
  exact resultants over Q(zeta_p)); P = (1-zeta_p) the unique prime over p.
holds-here: yes — this is the ramification foundation of the both-odd
  cyclotomic factorisation; it holds for every odd prime p independently of
  any solution.
status: checked — verified-numerically by exact integer arithmetic; three
  independent programs agree. NOT a proof for all p (ring-of-integers
  equality and the general-p statement remain asserted by Conrad).
anchor: code/out/verify_ram_fast.captured.txt (all odd primes <= 97),
  code/out/verify_ramification.captured.txt, code/out/scholar_ramification_check.captured.txt
bearing: upgrades claim zeta-p-ring-of-integers-and-ramification from
  asserted to checked on its exact consequences (p <= 97 for integrality of u,
  p <= 23 for the unit norm), the foundation the both-odd cyclotomic
  approach stands on.
```
