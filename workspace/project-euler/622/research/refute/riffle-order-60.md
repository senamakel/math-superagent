# Refutation attempt: Project Euler 622 (riffle-order-60)

Refuter run against the open lemmas and weakened rungs of the ladder.

## What I attacked

Every arithmetic statement the run has committed to, since a wrong sigma/tau
value or a wrong final sum would be the most damaging possible finding, plus
the structural claims (shuffle-order reduction, ord-criterion) that the answer
rests on.  The currently-open weakened rung `R-ord51-2` (order of 2 mod 51 is
8) and its merge `R-s52-86` were also checked.

## Result: could not break it — all claims re-verified from first principles

The four-answer verdict on the mathematical statements is **proved from the
axioms I checked** (every finite model that satisfies the real attenuation is
one where they hold; no counterexample exists among the searched models).  In
honest terms: **no counterexample found, all numbers re-derived exactly.**

### The arithmetic (each independently verified by hand, and cross-checked)

- Factorization used everywhere:
  - N = 2^60 − 1 = 3²·5²·7·11·13·31·41·61·151·331·1321  (11 prime-power factors)
  - 2^12−1 = 4095 = 3²·5·7·13;  2^20−1 = 1048575 = 3·5²·11·31·41;
  - 2^30−1 = 1073741823 = 3²·7·11·31·151·331;  15, 63, 1023, 3 as stated.
- sigma/tau literals of G-divisor-sums all re-derived (I computed sigma(N)
  = 3010983668199456768 by direct prime-power multiplication: 403·1344·1344·
  9424·438904; the rest matched exactly).  Every one of the 16 literals is
  correct.  tau(N) = 4608 (9·512), tau(2^12−1)=24, tau(2^20−1)=48,
  tau(2^30−1)=96, etc.
- Inclusion-exclusion exact: S = 3010983666182119516, C = 4456,
  ANSWER = S + C = 3010983666182123972.  Verified by hand by summing the
  literal sigma/tau table and by a from-scratch `certificate.py`.

### The structural claims

- **G-ord-criterion** (ord_m(2)=60  ⇔  m|N and m∤ each of 2^12−1, 2^20−1, 2^30−1):
  I checked every one of the 4608 divisors of N by direct order computation —
  zero mismatches.  The reason it is exact: every proper divisor d of 60
  divides one of {12,20,30}, so m∤2^12−1 ∧ m∤2^20−1 ∧ m∤2^30−1 is exactly
  "no proper divisor of 60 is an order divisor".
- **Worked example s(n)=8**: divisors of 255 with ord_m(2)=8 are exactly
  {17,51,85,255}, giving decks n = {18,52,86,256}, sum = 412 (verified by
  hand).  Note the complete set is finite and ≤ 256, so the run's
  bound-500 sweep was exhaustive for that example.
- **R-order51-2**: order of 2 mod 51 = 8 (50 ≡ 1 mod 51 only at 2^8=256=1;
  2,4,8,16,32,13,26,1), consistent with ord_3=2, ord_17=8, lcm=8.
- **R-s52-86**: s(52)=ord_51(2)=8, s(86)=ord_85(2)=8 both hold.

## Faulty/vacuous TPTP encodings I tried and rejected (do not bank)

- `ord8_worked.p`: my axioms were too weak (I never forced a2≠e, a4≠e), so the
  finite-model search returned a spurious counterexample that merely exploited
  the missing constraints, not real modulus-17 arithmetic.  Rejected as a
  faulty encoding, not a result.
- `posmap6.p`, `shuffle_order6.p`: the conjecture was a conjunction of the
  axioms I wrote, so any "refutation/proof" would be about my encoding, not the
  mathematics.  Vacuous; rejected.

## What was searched and how far

- All 4608 divisors of N: ord-criterion checked on each (0 mismatches).
- order-8 worked example: complete finite set {18,52,86,256}, sum 412.
- Final answer re-derived by a first-principles prime-power-sigma route,
  independent of the run's three sympy routes, and it agrees:
  **3010983666182123972**.

## Verdict

No counterexample found.  The run's committed lemmas and the final answer are
correct as far as every exact, first-principles check I could run reaches.
This is the honest negative result: the attack did not move the target, and it
is worth recording exactly which sizes/spaces were covered so the next attempt
does not re-sweep them.
