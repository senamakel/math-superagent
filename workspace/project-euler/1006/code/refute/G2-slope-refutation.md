# Refutation record: G2-mechanical-word-representation — stated slope formula is wrong

## Statement attacked
`G2-mechanical-word-representation` (pe1006-psi).  The open lemma as committed:

> "For n with F(n) > k and **rational slope a = F(n-1)/F(n)**, the k+1 length-k
> factors of F are produced exactly by the rotation/mechanical construction:
> cut the unit circle at the k+1 points frac(-ma), m=0..k; for the midpoint
> x_m of each arc define digit_j(x_m) = floor(x_m+(j+1)a) - floor(x_m+ja),
> j=0..k-1."

## Finding: the stated slope F(n-1)/F(n) is FALSE
The Fibonacci word is the characteristic Sturmian word of slope **1/phi^2**
(density of 1s = 1/phi^2 ~ 0.38197).  Its continued-fraction convergents are
0/1, 1/2, 1/3, **2/5**, 3/8, 5/13, 8/21, ... i.e. **F(n-2)/F(n)** — the *previous*
convergent — NOT F(n-1)/F(n).  F(n-1)/F(n) converges to 1/phi ~ 0.618, the slope
of the *complement* of the Fibonacci word.

### Hand check, k = 3 (smallest case with F(n) > k; F(5)=5)
True length-3 factor set (given by the problem itself, used for
Psi(3) = 1^2 + 10^2 + 100^2 + 101^2 = 20302): **{001, 010, 100, 101}**.

- **Stated slope a = 3/5.**  Cut points {0, 1/5, 2/5, 4/5}; arc midpoints
  1/10, 3/10, 3/5, 9/10 read as digits give {011, 011, 101, 110} =>
  distinct {011, 101, 110}.  Contains 011 and 110 (which never occur as
  Fibonacci factors) and omits 001 and 100.  Only **3 distinct words**, not
  k+1 = 4.  FAILS.
- **Correct slope a = 2/5.**  Cut points {0, 1/5, 3/5, 4/5}; arc midpoints
  1/10, 2/5, 7/10, 9/10 give {001, 010, 100, 101} = true factor set.  PASSES.

## Where the run stands
The *implemented* construction `code/mech/mech_psi.py` uses the correct slope:
`slope_for` returns `p = f[-3]`, `q = f[-1]`, i.e. **F(n-2)/F(n)**, and it is
verified against several oracles (brute string factors k<=50, recorded exact
k<=25, recorded residues k<=400).  So the **computation is correct**; only the
**claim's formula text** has an off-by-one index.  Any downstream code or formal
proof that quotes G2's formula verbatim (slope F(n-1)/F(n)) will produce wrong
words — this refutes the claim *as stated*, not the mechanical method.

## Status
`refuted` (claim text as stated), checked by hand against k=3 and the
problem-given factor set.  The mathematical method survives with the corrected
slope F(n-2)/F(n) = fib(n)/fib(n+2) (convergents to 1/phi^2), which is what
every implementation (mech_psi.py, mechSlope in Problem1006.lean, check_slope.py)
already uses and verifies for k=1..100.  The G2 skeleton's formula text carried
the off-by-one index; it has been corrected.  Corroborating evidence already in
the workspace: code/out/check_slope.captured.txt,
research/notes/mechanical-slope-correction.md.
(Cognee was unhealthy at write time, so this record lives in the workspace.)
