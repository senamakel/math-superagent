# f(1)..f(5) — the falsification oracle, exhaustive and ILP

Backing programs: `code/fmax_oracle/fmax_driver.py` (exhaustive + scipy/HiGHS
ILP) and `code/fmax_oracle/f5_independent.py` (ortools CP-SAT + pure-python
exact recheck). Captured output: `code/out/fmax_driver.captured.txt` and
`code/out/f5_independent.captured.txt`.

```claim
id: f-exact-1..5
statement: f(1)=1, f(2)=2, f(3)=2, f(4)=2, f(5)=3, where
  f(n) = min { D(S) : S ⊆ {0,1}^n, |S| = 2^{n-1}+1 }.
hypotheses: n=1..4 exhaustive over all C(2^n,2^{n-1}+1) subsets
  (≤ C(16,9)=11440); n=5 posed as the ILP/CP-SAT decision "is there S of size
  17 with D(S)<=d?" — d=1,2 infeasible, d=3 feasible — independently with
  scipy.optimize.milp (HiGHS) and ortools CP-SAT, agreement checked.
holds-here: yes
status: checked
bearing: exact values. f(1..4) were already computed here (brute.py /
f_exact_spectral_check.py); f(5)=3 is new. The sequence 1,2,2,2,3 equals
ceil(sqrt(n)) for n=1..5. This is consistent with Huang's max-degree theorem
(max internal degree >= sqrt(n) for any induced subgraph on more than 2^{n-1}
vertices) together with the sqrt(n) upper construction — so it is a second
independent route agreeing with the recalled bound's prediction at small n,
but does NOT prove the theorem.
falsifies: any claimed lower bound exceeding ceil(sqrt(n)) (i.e. f(n) >= 4 for
n=4, or f(5) >= 4) is false against these values. A Construction claiming
D(S) <= 2 for n=5 is refuted (d=2 infeasible).
anchor: code/out/fmax_driver.captured.txt, code/out/f5_independent.captured.txt
```

## Mechanism of the n=5 decision

The decision ILP uses binary `x_v` (v in `{0,1}^5`, 32 of them):

```
sum_v x_v = 17
for each v:  sum_{u in N(v)} x_u + 5*x_v <= d + 5
```

`5*x_v` is the standard big-M device: when `x_v=1` the constraint reads
`(internal degree of v) <= d`; when `x_v=0` it reads `sum over neighbours <= 5`,
which is always true since Q_5 is 5-regular. `d + 5` follows from M = n = 5.
This is a polynomial-size ILP (32 binaries, 33 constraints); exhaustive
C(32,17) ≈ 5.66e8 is not enumerated.

## Validation

- decision_ilp agrees with the exhaustive decision_oracle on **all** (n,d)
  for n=1..4 (13 (n,d) pairs):  `ALL AGREE: True` (fmax_driver).
- The n=5 result is confirmed by a **second, independent solver** (ortools
  CP-SAT): reproduces d=1,2 infeasible / d=3 feasible, and returns an explicit
  17-vertex witness verified by a third exact route (pure-python degree
  recomputation).

## Witnesses (D(S) = f(n))

- n=2, S=[0,1,2]: profile {1:2, 2:1}
- n=3, S=[0,1,2,5,6]: profile {1:2, 2:3}
- n=4, S=[0,1,2,5,6,11,12,13,14]: profile {0:1, 2:8}
- n=5, S=[2,3,4,5,6,8,9,11,13,14,15,16,17,18,19,20,30]: profile {1:2, 2:3, 3:12}

The extremal sets are "flat": most vertices share the max degree (e.g. n=5 has
12 of 17 vertices at degree 3), which is precisely the structure that defeats
edge-counting/averaging arguments — an average-internal-degree bound could not
predict a max this high on so few internal edges.

## Runtimes

- n=1..4 exhaustive: < 0.1 s total (n=4 is 11440 subsets).
- n=5 decision d=1,2,3 (scipy/HiGHS): 0.07, 0.43, 0.01 s; whole driver 0.7 s.
- n=5 CP-SAT independent: 0.07, 0.12, 0.01 s; whole script 0.3 s.

## Note re: sqrt(4)=2

The task's parenthetical asked whether f(4) is achieved at 2 (the sqrt
construction) or forced higher by the spectral bound. f(4)=2: the sqrt(4)=2
upper construction IS achieved (equivalently, Huang's lower bound floor
sqrt(4)=2 is tight here). At n=5 the value 3 likewise reaches ceil(sqrt(5)),
so sqrt(n) remains consistent at every n computable so far.
