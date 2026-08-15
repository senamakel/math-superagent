# Case B (Lebesgue's theorem): x^p - y^2 = 1, p odd prime — machine-certified

Program: `code/caseB/certify_lebesgue_caseB.py`
Output: `code/out/caseB.captured.txt`
Library used: `code/lib/gaussint.py` (exact Gaussian integers), `sympy` exact
expansion. All arithmetic exact (Python ints + sympy); no floats.

## What is claimed, exactly

For positive integers x, y and an **odd prime p >= 3**, the equation

    x^p - y^2 = 1

has **no solution**.

The known Catalan solution `3^2 - 2^3 = 1` has x-exponent 2 and y-exponent 3
(q = 3), so it sits **outside** this case's hypothesis (y-exponent 2, p odd
prime). The claim therefore does not eliminate the known solution; it is the
"no second solution with y-exponent 2" statement, consistent with the oracle.

## The reduction (machine-certified, steps 1-5)

1. **Parity.** Mod 4: if y odd, `y^2+1 = x^p ≡ 2 (mod 4)`, but an odd p-th
   power of an odd x is ≡ x ≡ 1 or 3 (mod 4), never 2. So y is even; then
   `x^p = y^2+1 ≡ 1 (mod 4)` forces x odd.  **Checked** for all y in a range
   and all odd primes p < 60.

2. **Factorisation in Z[i].** `x^p = y^2+1 = (y+i)(y-i)` with
   `gcd(y+i, y-i)` a unit for even y: `1+i ∤ (y+i)` because re(y+i)=y is even
   and im=1 is odd, and in Z[i] `1+i | (a+bi) ⇔ a,b` same parity. Z[i] is a
   UFD and p is odd, so `y+i = u·(a+bi)^p` for a unit u.
   **Checked**: N(y+i)=y²+1 and gcd is a unit for all even y in [0,2000).

3. **Unit absorption.** The unit group of Z[i] has order 4 and p is odd, so
   every unit u has a p-th root w (a unit): `u·(a+bi)^p = (w(a+bi))^p`. Hence
   `y+i = (c+di)^p` for a Gaussian integer c+di.  **Checked** symbolically and
   on concrete integers for every unit and every p in {3,...,17,19,23,29,...};
   absorption maps printed (e.g. u=1→(a,b), u=-1→(-a,-b), u=i→(b,-a) or
   (-b,a) according to p mod 4, etc.).

4. **Imaginary part ⇒ d = ±1.** `1 = Im(y+i) = Im((c+di)^p) = d·Q(c,d)` with
   Q(c,d) an integer polynomial (every monomial of Im carries a factor d).
   Since d and Q are integers, d | 1, so **d = ±1**.  **Checked**: Im vanishes
   at d=0 as a polynomial in c,d for all tested p.

5. **Real part ⇒ c | y, norm ⇒ x = c²+1.** `Re((c+di)^p) = c·R(c,d)` (every
   real binomial term carries a power of c^{odd}); with d=±1 and y = Re, this
   gives **c | y**.  Norm: `N(y+i) = x^p = N((c+di)^p) = (c²+d²)^p`, so
   **x = c²+d² = c²+1**.  Writing y = c·m (m integer, c ≥ 1; c = 0 would give
   y = Re((di)^p) = 0, excluded because y > 0):
   `c²m² = y² = x^p - 1 = c²·sum_{i=0}^{p-1}(c²+1)^i`, hence

       m² = T(c,p) := sum_{i=0}^{p-1} (c²+1)^i = (x^p-1)/(x-1).

   **Checked**: Re((c±i)^p)/c integral, N-identity, geometric-sum identity,
   and m² = sum identity — all symbolic/exact for the tested primes.

**Conclusion of steps 1-5 (machine-certified):** every solution forces
`x = c²+1` and `m² = T(c,p)`.

## The key lemma (step 6) — NOT proved here, verified + classical-asserted

`T(c,p)` is never a perfect square for odd prime p ≥ 3, c ≥ 1.

- **(6a) Numerical:** exact integer check for c in [1,2000] and every odd
  prime p in [3,101] — **50,000 pairs, 0 squares** (0.28 s). Closest near
  misses (gap = T − isqrt(T)²): c=1,p=3 gap 3; c=1,p=5 gap 6; c=1,p=7 gap 6;
  c=2,p=3 gap 6; c=3,p=3 gap 11.  Largest c reached 2000.
- **(6b) Classical theorem (Ljunggren-type):**
  `(X^n-1)/(X-1) = Y²` has, for n > 2, exactly the solutions
  `(n,X,Y) = (4,7,20)` and `(5,3,11)`.  Our slice has n = p an odd prime and
  X = c²+1.  Of the two exceptions only `(5,3,11)` has odd n, and it requires
  X = 3, i.e. c²+1 = 3, c² = 2 — impossible for integer c.  Hence T(c,p) is a
  square only if it equals the (5,3,11) case, which is excluded.
  **This lemma is ASSERTED-CLASSICAL and VERIFIED-NUMERICALLY in-workspace; it
  is NOT re-proved here.**
- The two-square "elementary" bound of the prompt's original step 6 FAILS for
  large odd p (T/m² → x/(x-1) > (1+1/m)², so T can exceed m²+2m+1) and is
  **not** used.  The claims below are stated honestly: the reduction is proved,
  the final step is numeric + classical-asserted.

## Falsifier / over-elimination check

Claimed lemma "x^p − y² = 1 has no solution (p odd prime)" does **not** imply
no solution at all: the known solution has y-exponent 3, so it is excluded by
hypothesis (`in_case = False`). No over-elimination.

## Claims

```claim
id: exp2-case-B-reduction
statement: If x^p - y^2 = 1 with x,y positive and p an odd prime, then
  x = c^2+1 and y = c*m for positive integers c,m, with
  m^2 = T(c,p) = sum_{i=0}^{p-1}(c^2+1)^i = (x^p-1)/(x-1).  (Steps 1-5,
  machine-certified: parity, Gaussian factorisation, unit absorption,
  Im ⇒ d=±1, Re ⇒ c|y, norm ⇒ x=c^2+1.)
hypotheses: x,y > 0, p odd prime >= 3, exact arithmetic.
holds-here: yes -- the known solution (3,2,2,3) has y-exponent 3, so it is
  outside this case's hypothesis (y-exponent 2); no over-elimination.
status: reduction-proved (steps 1-5 machine-certified); key lemma T(c,p) not
  a square is verified-numerically (c<=2000, odd prime p<=101, 50000 pairs,
  0 squares) and asserted by the classical Ljunggren-type theorem
  ((X^n-1)/(X-1)=Y^2 only (4,7,20),(5,3,11); odd-n slice X=3 excluded).  NOT
  status: proved -- the final lemma is not re-proved in this workspace.
bearing: gives the honest Lebesgue-type reduction for Case B; the theorem
  x^p-y^2=1 (p odd prime) is proved conditional on Ljunggren's theorem.
anchor: code/out/caseB.captured.txt
```

## What verified / what failed

- **All of steps 1-5 PASS** (the reduction) — certified exactly.
- **Step 6(a) PASS** (numeric box, 50,000 pairs, 0 squares, c ≤ 2000, p ≤ 101).
- **Step 6(b) NOT proved in-workspace**: asserted by Ljunggren, verified
  numerically.  This is the honest limit; the earlier two-square bound is
  known to fail for large p and was **not** used.
- A note on the false-lemma trap: any claim implying the reduction solves Case B
  *without* the key lemma would be wrong; it does not, and nothing here claims it.
