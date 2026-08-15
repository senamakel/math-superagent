# Lebesgue Case A — v_2 parity reduction, machine-verified

Program: `code/lebesgueA/verify_v2_reduction.py`
Output: `code/out/lebesgueA_v2.captured.txt`
All arithmetic exact (Python ints), no floats except wall-clock timing.
Total wall time: **2.860 s** (EXIT_CODE=0).

## What is verified

Case A of Catalan's equation: `x^2 - y^q = 1`, q an odd prime, x,y >= 1.
The claimed RETURNED solution of this case is the known solution
`(x,y,q) = (3,2,3)` (`3^2 - 2^3 = 1`), which is **returned, never excluded**.

### Step 1 — x even impossible  [PASS]
`x^2 - 1 = (x-1)(x+1) = y^q`. For x even, x-1, x+1 are odd and coprime, so each
is a q-th power `a^q, b^q` with `b^q - a^q = 2`.  Verified by two independent
faithful exact enumerations over `x <= 10^6` (i.e. `y^q <= 10^12`), for q odd
prime <= 97:
- (y-side) all solutions of `x^2 - y^q = 1` with x <= 10^6 are exactly
  **[(3,2,3)]** — the singleton set of odd-x solutions; zero odd-y (x even)
  solutions.
- (x-side) direct scan of even x <= 10^6 with `x^2 - 1` in the perfect-q-th-
  power set D (|D| = 10320, 500000 even x scanned): zero hits.
The enumeration still returns the known (3,2,3), so x even being impossible is
a genuine "no extra solution" statement, not over-elimination.

### Step 2 — x odd structure  [PASS]
`x-1 = 2u, x+1 = 2v` gives `gcd(u,v)=1`, `v-u=1`, `y^q = 4uv`.  Writing
`y = 2^k z` (z odd) gives `uv = 2^{kq-2} z^q` with **exactly one of u,v even**.
Verified for every odd x in [3,2001] and on the known solution
(x=3: u=1, v=2, k=1, z=1; all structural checks pass, v even -> Branch B).

### Step 3 — branch enumeration  [PASS]
Exactly one of u,v even splits into:
- Branch A (u even): `b^q - 2^{kq-2} a^q = 1` — **no solutions** in
  q odd prime <= 97, k in [1,8], a,b in [1,300], gcd(a,b)=1
  (10,520,640 coprime pairs checked).
- Branch B (v even): `2^{kq-2} b^q - a^q = 1` — **only (q,k,a,b)=(3,1,1,1)**
  in the same range (10,520,640 coprime pairs checked).

### Step 4 — round-trip  [PASS]
Branch-B solution maps to `x = 2a^q + 1`, `y = 2^k a b`.  `(3,1,1,1)` maps to
`(x,y) = (3,2)` and `3^2 - 2^3 = 1`.  The enumerated Branch-B solution
reproduces `x^2 - y^q = 1`, and 3^2 - 2^3 = 1 is the known solution (RETURNED,
not excluded).

## Falsifier / over-elimination

The single known solution of Case A is `(3,2,3)`, which the enumeration
RETURNS (step 1 reports the full solution set [(3,2,3)]; step 3 returns the
only Branch-B solution (3,1,1,1); step 4 maps it back to (3,2)).  Step 1's
"x even impossible" excludes only even-x candidates, never the odd-x known
solution; a lemma implying no solution at all would be refuted and none is
used here.

## Ranges / bounds reached

- Step 1 enumeration: x <= 10^6 (y^q <= 10^12), q odd prime <= 97.
- Step 2 structural: odd x in [3,2001] + known solution.
- Step 3 branch enumeration: q odd prime <= 97, k in [1,8], a,b in [1,300],
  gcd(a,b)=1 — Branch A empty, Branch B = {(3,1,1,1)}.
- Step 4: round-trip exact.

## Claim

```claim
id: lebesgue-caseA-v2-reduction-verified
statement: For Lebesgue Case A x^2 - y^q = 1 (q odd prime, x,y >= 1), the
  v_2 parity reduction is machine-verified over the stated finite ranges:
  (1) x even impossible (verified x <= 10^6, q odd prime <= 97, by two
  independent exact enumerations); (2) x odd gives x-1=2u, x+1=2v with
  gcd(u,v)=1, v-u=1, y^q=4uv, uv = 2^{kq-2} z^q, exactly one of u,v even
  (verified for odd x in [3,2001] and at the known solution); (3) Branch A
  b^q - 2^{kq-2}a^q = 1 has NO solution and Branch B 2^{kq-2}b^q - a^q = 1
  has only (q,k,a,b) = (3,1,1,1), both over q odd prime <= 97, k in [1,8],
  a,b in [1,300], gcd(a,b)=1; (4) round-trip (3,1,1,1) -> (x,y)=(3,2) with
  x^2 - y^q = 1.  The known solution (3,2,3) is the claimed RETURNED solution
  of this case, not excluded.
hypotheses: q odd prime, x,y >= 1, exact integer arithmetic throughout.
holds-here: yes -- the known solution (x,y,q)=(3,2,3) / (q,k,a,b)=(3,1,1,1)
  is returned by the verification (Step 1 full solution set = [(3,2,3)],
  Step 3 Branch B = [(3,1,1,1)], Step 4 maps it to (3,2)), never excluded.
  Step 1's "x even impossible" excludes only even-x candidates; a lemma
  implying no solution at all would be refuted (none used).
status: verified-numerically over the stated ranges (exact integer arithmetic;
  all four steps PASS, total wall 2.860 s).  This is a finite-range numerical
  verification, not a proof for all q / all magnitudes.
bearing: banks the exact branch structure of the Lebesgue Case A descent that
  the in-workspace descent sub-claim (exp2-descent-subclaim-no-extra) and the
  q=3 Thue proof (exp2-fixed23-proved-thue) rest on; the return of (3,1,1,1)
  in Branch B is the known solution, consistent with the oracle claim
  oracle-single-solution.
anchor: code/out/lebesgueA_v2.captured.txt
```
