# Report — PE1006 modular & factor structure (tool-builder)

All work exact integer arithmetic (a = 1/phi^2 = (3-sqrt5)/2 handled as
high-precision Decimal; all *counts and values* exact). Brute oracle verified:
Psi(3)=20302, Psi(10) mod M = 10699667; Psi(1..150) exact in
code/out/psi_data_1_150.txt.

## TASK A — modular structure of M = 101001001  (saved code/out/mod_A.txt)

- **M = 101001001 is PRIME.** Verified by trial division to sqrt(M)=10049
  (exhaustive, all d), confirmed by sympy.isprime. So M-1 is the only evident
  factorization: M-1 = 101001000 = 2^3 * 3 * 5^3 * 131 * 257.
  This collapses the "prime-power factors" question: M is its own single
  prime-power factor q = M^1.
- **ord_10(M) = 50500500** = (M-1)/2. (10^50500500 ≡ 1 mod M; minimality
  verified by reducing each prime divisor of 50500500 and confirming none of
  the reduced exponents gives 1. Independent check: pow(10,o,M)==1.)
- **Pisano period pi(M) = 101001000 = M-1.** Legendre(5,M)=1 (5 is a QR mod M)
  so pi(M) | M-1; F_{M-1}≡0 and F_M≡1 mod M; minimality verified by reducing
  each prime divisor of M-1. Independent fast-doubling recheck agrees.
- Both orders independently re-verified (divisor-reduction + fast-doubling).

## TASK B — eventual periodicity of r(k)=Psi(k) mod M  (saved code/out/mod_B.txt)

- r(k) listed for k=1..150. **No constant period <= 75 exists** (the only
  search hit is the trivial endpoint (preperiod 150, period 1)). So within the
  oracle range r(k) is not eventually periodic with a small period, and
  10^18 cannot be reduced into a periodic range this way.
- Structural reason (from Task A): value mod M depends on 10^(k-1-i) mod M
  for each 1-bit, and ord_10(M)=50500500 is far larger than the 150 points, so
  no two powers of 10 coincide in range. A small-period route is structurally
  ruled out; the period, if any, is at least ord_10(M)-scale.

## TASK C — structure of factor values  (saved code/out/mod_C.txt, _struct, _ones)

- Factor table k=1..12 (k, j, factor, V, V mod M) printed exactly. Note
  V mod M hits 0 for the factors spelling 101001001 (M's decimal), e.g.
  k=9 j=8, k=10 j=9, etc.
- **N(i;k) is BALANCED in i**: for every k<=40 it takes only two consecutive
  integer values (verified all k). 
- **Constant when k = F_m - 1**: N(i;k) = F_{m-2} constant across i, verified
  for k=4,7,12,20,33 (== F_3,F_4,F_5,F_6,F_7).
- **The candidate N(i;k)=floor((k-i)a+const) is FALSIFIED.** Best single const
  matches only 111/820 positions; consistency at k=8 needs const 0.94 at i=0
  but 0.33 at i=1, so no single const works even for one k. The correct
  description is the *balanced/two-value* one, not this position-Beatty form.
- Exact ones-total: T(k)=sum_i N(i;k) = (k+1)*floor(ka) + r_k where r_k = # of
  heavy factors (those with ceil(ka) ones); r_k table printed (values vary;
  r_{F_m}=F-sequence at Fibonacci k, e.g. r_k=13 at k=13, r_k=34 at k=34).

## On k=10^18

No small-period reduction is available (Task B negative). The value-mod-M
depends on 10^(k-1-i) mod M; with ord_10(M)=50500500 one can always reduce the
*bits' powers of 10* (each 10^(k-1-i) mod M needs only (k-1-i) mod ord_10(M))
— that is the structurally correct way to compute mod M without building 10^18
objects: it is the ord_10-reduction on exponents, not a Psi-period. The
remaining open step is turning the factor set into a sum of (sum_j 2^{s_j}·10^e)^2
with exponents reduced mod ord_10(M).
