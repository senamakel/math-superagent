# PE1006 structural ground: Tasks A, B, C (tool-builder)

Established by exact computation on the verified oracle (`psi_brute`, `psi_data_1_150.txt`,
`factors_k40.json`). All numbers exact.

## Task A — modular structure of M = 101001001

**M is prime.** `sympy.isprime(M)=True`, `sympy.factorint(M)={M:1}`, and independent trial
division to `sqrt(M)=10049` finds no divisor. So M is a single prime power M^1; there is no
CRT decomposition to do.

**ord_10(M) = 50500500.** `10^50500500 mod M = 1`, and 50500500 = 2^2·3·5^3·131·257.
So the period of `10^k mod M` is 50500500. Its even-power period (used for 10^(2e)) is
50500500/gcd(2,50500500) = 25250250.

**Pisano period pi(M) = 101001000 = M − 1.** Verified F_101001000≡0, F_101001001≡1 mod M,
and no smaller T returns to the pair (0,1). Since M is prime and M≡1 (mod 5), pi(M)=M−1 is
the expected special value. This is the period of the Fibonacci-recurrence structure mod M.

## Task B — eventual periodicity of r(k) = Psi(k) mod M

Built r(k) for k=1..150 (exact). `r(10)=10699667` reproduces the given value.

A genuine eventual period (pre, T) requires a non-vacuous batch of aligned comparisons; a
search requiring at least 40 aligned equalities found **no (pre,T) with T<150**. The naive
report of (pre=0, period=150) is vacuous (it compares nothing). Conclusion: **r(k) is not
small-periodic**; there is no shortcut `r(10^18)=r(10^18 mod T)` of the simple kind. The
natural period scale is ord_10(M)=50500500 (weight positions) and Pisano(M)=101001000, but
r(k) rescales its coefficient positions with k, so it is not simply periodic. r(10^18)
cannot be read off a reduced index without the full coefficient structure.

## Task C — structure of factor values

### C1: factor values (decimals) for k=1..12
See `code/out/PE1006_report_tasks_ABC.txt` for the full table. Consecutive decimal values
differ by 1, 9, 90, 900, … (single `1`→`10`→`100` flips at a position), reflecting the
separating `ab`/`ba` pattern of the Sturmian factor order.

### C2: closure/recurrence of N(i;k)
`N(i;k)` = #distinct length-k factors with a `1` at position i (0=left).
- **Verified for all k≤40: N(i;k) ∈ { ⌊(k+1)a⌋, ⌊(k+1)a⌋+1 }, a=(3−√5)/2=1/φ².**
- The task-suggested ramp `N(i;k)=floor((k−i)a+const)` does **NOT** fit: N is nearly
  *constant* in i (two values, ±1), not a ramp; a const-grid scan never got below ~700
  mismatches. This is a firm negative result — the per-position one-count is not a
  decreasing ramp in position.
- Empirically `N(i;k) = ⌊(k+1)a⌋ + e(i;k)` with `e∈{0,1}`; the ceil columns
  `{i : e(i;k)=1}` are recorded per k in the report (Fibonacci/mechanical structure).

### C3: the real structure — columns are circular intervals on the (k+1)-circle
Treat the k+1 factors as the k+1 rows, and each of the k columns as the list of bits down
the factors. **Each column is a contiguous (circular) interval of 1s on the (k+1)-circle.**
Verified for all k≤40. When N(i;k) is constant in i, the interval starts s(i) are a pure
arithmetic rotation s(i) ≡ c + m·i (mod k+1); otherwise a two-increment mechanical walk.

### C4: pair correlations and the sum-of-squares
`Psi(k) = Σ_j val(w_j)² = Σ_{i,l} A(i,l) 10^{2k−2−i−l}` where `A(i,l)`=# factors with 1 at
both i and l. `A(i,i)=N(i)`; for i≠l, `A(i,l)` = size of the intersection of column
intervals i and l on the circle.
- **The full circular-interval representation reconstructs Psi(k) exactly** for
  k=3,4,5,6,8,10,12,15 against the oracle (validated).
- The pair correlation `C(i,i+d)` is **not** constant in i in general (e.g. k=6,d=3), so
  the sum-of-squares cannot collapse to a single-count closed form by diagonality alone; it
  needs the interval-intersection (position-pair) sums.

## Deliverables saved
- `code/out/PE1006_report_tasks_ABC.txt` — the printed consolidated report (all three tasks).
- Programs in `code/pe1006/`: `task_a_modular.py`, `task_b_period.py`,
  `task_b_rigorous.py`, `task_c_structure.py`, `task_c_rigorous.py`, `task_c_fit.py`,
  `task_c_fit2.py`, `task_c_ceilset.py`, `task_c_intervals.py`, `task_c_starts.py`,
  `task_c_validate_intervals.py`, `report_tasks.py`.

## Status / hand-off
Tasks A, B, C are each answered as exact numbers / verified structural statements. The
actual numerical evaluation at k=10^18 mod M is not a small-period lookup (Task B negative)
and is left to the hammer-and-chisel school's divide-and-conquer on the Fibonacci/Zeckendorf
structure of k; the interval-ground established here is what that recurrence must close over.

```claim
id: PE1006-M-is-prime
statement: 101001001 is prime (its only prime-power factorization is itself).
hypotheses: none.
holds-here: true (the object is M itself).
status: checked — sympy.isprime, sympy.factorint={M:1}, and independent trial division to sqrt(M)=10049 finds no divisor.
bearing: the modulus is a single prime, so ord_10(M) and Pisano(M) are directly the prime values (no CRT needed).
anchor: code/out/PE1006_report_tasks_ABC.txt (run code/pe1006/task_a_modular.py).
```

```claim
id: PE1006-ord10-and-pisano
statement: ord_10(101001001)=50500500 and the Pisano period of the Fibonacci recurrence mod 101001001 is 101001000 (M-1).
hypotheses: M=101001001 prime.
holds-here: true — verified 10^50500500=1 mod M with no smaller period, and F_101001000=0, F_101001001=1 with no smaller T.
status: checked (verified by direct modular scan; two routes: order via sympy.n_order and state-scan for Pi).
bearing: period of 10^k mod M is 50500500; Fibonacci structure period is 101001000.
anchor: code/out/PE1006_report_tasks_ABC.txt.
```

```claim
id: PE1006-no-small-eventual-period
statement: r(k)=Psi(k) mod 101001001 for k=1..150 has no genuine eventual period T<150 (a search requiring >=40 aligned equalities finds none).
hypotheses: exact Psi(1..150).
holds-here: true (negative result over available data).
status: checked.
bearing: rules out the simple periodic shortcut r(10^18)=r(10^18 mod T).
anchor: code/out/PE1006_report_tasks_ABC.txt (run code/pe1006/task_b_rigorous.py).
```

```claim
id: PE1006-columns-circular-intervals
statement: In the (k+1)xk factor matrix of the Fibonacci word (rows=k+1 length-k factors in lex order, columns=positions), every column is a contiguous circular interval of 1s on the (k+1)-circle; its length N(i;k) is in {floor((k+1)a), floor((k+1)a)+1}, a=(3-sqrt5)/2, for all k<=40, and this interval representation reconstructs Psi(k) exactly (validated on k=3,4,5,6,8,10,12,15 vs oracle).
hypotheses: k<=40 computed set.
holds-here: true (verified over the computed range).
status: checked (reconstruction reproduces oracle values exactly).
bearing: the sum-of-squares reduces to sums of pairwise circular-interval intersections; N(i;k) is NOT a ramp in i.
anchor: code/out/PE1006_report_tasks_ABC.txt (run code/pe1006/task_c_*.py).
```
