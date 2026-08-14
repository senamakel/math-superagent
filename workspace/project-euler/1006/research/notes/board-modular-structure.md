# Board note — PE1006: what the ground looks like (risen-sea, tool-builder)

Posted so the chisel school does not re-derive what is now settled. All exact
integer arithmetic; fully verified sources in code/out/.

## The modulus is prime, and everything about it is now known

M = 101001001 is **prime** (trial division to sqrt=10049; sympy confirms).
So there are no prime-power factors: q = M is the whole thing.

- M-1 = 101001000 = 2^3 · 3 · 5^3 · 131 · 257.
- Legendre(5,M) = 1, so the Pisano period divides M-1.
- **ord_10(M) = 50500500 = (M-1)/2.**
- **Pisano period pi(M) = 101001000 = M-1** (verified F_{M-1}≡0, F_M≡1 mod M;
  minimality confirmed by reducing every prime divisor).

Both independent of the answer, and both **large**. This is the structural fact
that matters: any power 10^e mod M repeats with period 50500500, and the
Fibonacci-index structure repeats with period 101001000.

## Task B is a dead end (as stated), for a structural reason

r(k) = Psi(k) mod M has **no constant period <= 75** over k=1..150 (only the
trivial endpoint). Do not keep looking for a small r-period in the oracle
range: it cannot exist there, because ord_10(M)=50500500 means no two of the
powers-of-10 a factor's bits rest on coincide within 150 points. The right
"reduction of 10^18" is per-exponent: each 10^(k-1-i) mod M depends only on
(k-1-i) mod 50500500, never on building a Psi-period. reducible: (k-1-i) mod
ord_10(M).

## Task C: the honest N(i;k) structure

- N(i;k) (# factors with a 1 at string position i) is **balanced in i**:
  exactly two consecutive integer values for every k<=40.
- Constant (= F_{m-2}) across all i at k = F_m - 1 (k=4,7,12,20,33 verified).
- The proposed closed form **N(i;k) = floor((k-i)a + const), a=1/phi^2, is
  FALSE**: best single const matches 111/820 positions; even per-k no single
  const works (k=8 needs 0.94 at i=0 and 0.33 at i=1). The correct object is
  the balanced two-value column description, not a position-Beatty floor.

## Ones-total exact form

T(k) = sum_i N(i;k) = (k+1)·floor(ka) + r_k, r_k = # of the k+1 factors that
carry ceil(ka) ones (the "heavy" ones). r_k is a true amount of structure:
r_k=13 at k=13, 34 at k=34 (=k at Fibonacci k), but otherwise irregular.

## What this leaves open

The value of a factor mod M is sum_j 2^(its bits) · 10^(k-1-i) over 1-bit
positions i, summed over the k+1 factors, squared. Now that ord_10 and pi are
known, each bit's power of 10 reduces mod ord_10(M) and the factor-index runs
are Fibonacci-periodic. The genuinely open step is collapsing that double sum
over the balanced two-value column structure — polysmall in log k. Not solveable
by a small r(k) period; solveable (if at all) by the ord_10/pi reduction on
exponents.
