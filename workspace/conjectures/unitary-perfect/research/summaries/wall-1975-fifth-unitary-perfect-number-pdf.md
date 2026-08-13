# Wall (1975), *The fifth unitary perfect number* — digest

Full text: [[wall-1975-fifth-unitary-perfect-number-pdf.full]] (Canad. Math.
Bull. 18 (1975) 115–122; OCR noisy, exponents of the fifth example render as
`2^183 · 5^47` in the raw text — the true factorization is `2^18 · 5^4`).

**Establishments (read from the full text):**

- **The result.** `W = 146,361,946,186,458,562,560,000` is the *next* unitary
  perfect number after 87360: the paper eliminates every UPN `N < W`. `W` is
  `2^18 · 3 · 5^4 · 7 · 11 · 13 · 19 · 37 · 79 · 109 · 157 · 313`.
- **Attribution to Subbarao 1970 §2:** "Subbarao [1] has reported the
  impossibility of having A be 0, 3, 4, 5, 7, 8, 9 or 10, and that if A = 1,
  then N = 6 or 90; if A = 2, then N = 60; if A = 6, then N = 87360. Thus we
  may restrict our attention here to A ≥ 11." [1] = Subbarao, *Are there an
  infinity of unitary perfect numbers?*, AMM 77 (1970) 389–390.
- **Seed cap.** For `N < W`, `a < 38` (from `(3/2)·2^38 > W`).
- **The 2-adic budget identity appears here too** (p. 116): "If N is unitary
  perfect and N = 2^A k with k odd, then as a consequence of (2), the number
  of distinct prime divisors of k is no more than A + 1." — the same identity
  derived in `research/notes/parity-and-2-adic-budget.md`.
- **Elimination method (3):** if N has enough known divisors to require
  `N > W`, the case is dead. The "excess" test (e) / bound (6) via largest
  prime `p | 2^A+1`; runtime was partly by computer (11 ≤ A ≤ 38).
- **Special cases (8)–(15):** descend the candidates, e.g. (15) forces
  `N = W` exactly.
- **"10^102" does not occur anywhere in this paper** — see
  `research/notes/wall-1975-bounds-and-102-claim.md`.

```claim
id: wall1975-bound-is-1e23-not-1e102
statement: Wall 1975 proves W is the next unitary perfect number after 87360
  by eliminating all N < W = 146361946186458562560000 ~= 1.46e23; the seed cap
  is a < 38 for N < W; the number of distinct prime divisors of the odd part
  is at most a + 1 (the 2-adic budget identity); "10^102" does not occur.
hypotheses: full Cambridge PDF is the primary text and accurately OCR'd
holds-here: yes - fixes the actual historical search scale; compute policy
  unchanged (10^23 already unreachable)
status: asserted (sourced from the held Wall 1975 full text)
bearing: the run must state 10^23, not 10^102, when citing Wall; the
  10^102 figure remains an orphan claim
anchor: research/sources/wall-1975-fifth-unitary-perfect-number-pdf.full.md
contradicts: GOAL.md, ROOT.md, CONTEXT.md to the extent each states 10^102
answers: primary-source-for-the-10-102-search-bound
```

<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B1919CB85AE1D97A7BAD3842B6E2AFB4/S000843950006598Xa.pdf/the-fifth-unitary-perfect-number.pdf | converted from PDF -->

Canad. Math. Bull. Vol. 18 (1), 1975

THE FIFTH UNITARY PERFECT NUMBER

BY
CHARLES R. WALL

1. Introduction. A  divisor d of a positive integer « is a unitary divisor if d and
njd are relatively prime. An integer is said to be unitary perfect if it equals the sum
of its proper unitary divisors. Subbarao and Warren [2] gave the first four
unitary perfect numbers: 6, 60, 90 and 87360. In 1969,1 reported [3] that

146 361 946 186 458 562 560 000

= 2
183 • 5
47 • 11 • 13 • 19 • 37 • 79 • 109 • 157 • 313

is also unitary perfect. The purpose of this paper is to show that this last number,
which for brevity we denote by W9 is indeed the next unitary perfect number
after 87360.
If d is a unitary divisor of n, we write d\\n; note that this notation is consistent
with the standard notation for exact division by prime powers. Let o*(ri) be the
sum of all unitary divisors of n :  <r*(n) = 2 *
d\\n
It is easy to show that a* is a multiplicative function, and in fact

cr*(pV-- 0 =  (l+P a )(l+^)"- ,

where p, q,... are distinct primes and the exponents are positive. We remark that
o*(ri) is odd only for n=l and n any power of 2.
Ifp and q are distinct primes, and/? | n but qjfn, then

(1) <**(pri)lpn <  o**(n)/n <  a*(qn)[qn.

Thus the value o*(ri)jn decreases as the primes dividing n are repeated, so if we wish
to maximize o*(ri)jn and at the same time minimize n, we must take n squarefree.
The requirement that N  be unitary perfect is clearly equivalent to o*(N)=2N.
Thus the search for unitary perfect numbers is the search for solutions to the Dio-
phantine equation

(2) 2 = £±1.Z±1.... ;
x y

with the restriction that x, y .. . are powers of distinct primes. If iVis unitary per-
fect and N=2
Ak with k odd, then as a consequence of (2), the number of distinct
prime divisors of A: is no more than A + l.

Received by the editors March 2, 1971 and, in revised form, October 24, 1973.
115

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

116  C. R. WALL  [April

For the remainder of this paper we assume that N is unitary perfect, that N< JV>
and that 2
A \\ N.

2. Elimination methods. Subbarao [1] has reported the impossibility of having
A be 0, 3, 4, 5, 7, 8, 9 or 10, and that

if ,4 = 1, then N=6 or 90;
if ,4=2, theniV=60;
if A=6, then N= 87360.

Thus we may restrict our attention here to ,4>11. Since o*(2
A)=l+2
A
9 we may
write 7V=2^(l+2^)<iwith d>\. Then N<> ^requires ^<38 , since J^<(3/2)1023.
The simplest way to eliminate a case is to show:

(3) N has enough known (or assumed) divisors to require that N > W.

Our basic procedure is to start with a given value for A; then o*(2
A)=\+2
A

provides us with some known divisors of N. We then sort the known (or assumed)
divisors into two categories: known (or assumed) unitary divisors, and other
known (or assumed) divisors. We let p be some prime, usually the largest, in the
latter category; then use of (3) allows us to obtain an upper bound on how many
times p can divide N. Once we have this bound we may consider cases in which
p
e || N; then a*(p
e)=l+p
e in general provides us with other known odd divisors
of N, and we repeat the procedure.
We write
 N = 2
A3
B5
cs,

with (s, 30)=1. If A^ll, B>3 and C>3 , then

2 = cr*(N)/N < (2049/2048)(28/27)(126/125)tf*(5)/5,

so that a*(s)js>l.9l. If s is the product of the primes from 7 through 59, inclusive,
then o*(s)js<l.90. Thus by the remarks following (1), s can be no smaller than
the product of the primes from 7 through 61, but this would imply

N > 2n3353s > 10
28.

Since 28/27> 126/125>1, the same lower bound for a*(s)ls also holds if B=C=0,
if B=0 and C>3 , or if B>3 and C=0 . However, each of these conditions implies
that iV>1024. Therefore:


*[excerpt ends; 13242 characters not shown — see `research/sources/wall-1975-fifth-unitary-perfect-number-pdf.full.md`]*
