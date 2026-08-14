# Skeleton — complete fixed-point enumeration of f(n,d)=n

This is a decomposition of the PE156 goal into the three statements that
together force the final answer. It is not a route to a faster algorithm; it
is the argument that, given these three lemmas, the number a program prints is
provably Σ s(d).

```skeleton
goal: Σ_{d=1}^{9} s(d) = Σ_{d=1}^{9} Σ_{n : f(n,d)=n} n, computed exactly, where f(n,d) is the count of digit d in the decimal writings of 0..n inclusive (n counted once per digit d it satisfies, per the problem note).
implies: >
  For each d in 1..9 let B(d) = d·10^10. G2 gives that the solution set
  S_d = {n ≥ 0 : f(n,d)=n} lies entirely in [0, B(d)], so it is finite and
  every element is reachable by a search that never goes past B(d).
  G1 gives an exact O(#digits) evaluation of f(n,d) at any single n, so the
  search can move by evaluating f at chosen points rather than by visiting
  numbers. G3 states the two skip rules that make such a search complete:
  (i) if f(n,d) = c > n then every solution m satisfies m ≥ c, so jump n to c;
  (ii) if c < n then every solution m satisfies m ≥ n + (n−c)/(D−1) with
  D = digits(B(d)), so jump n to ⌈n + (n−c)/(D−1)⌉. Starting at n=0 and
  applying (record-and-step when c = n, else the appropriate jump) enumerates
  exactly S_d and terminates, because n strictly increases at every step and is
  bounded by B(d). Hence the output list for digit d is exactly S_d, so the
  program's s(d) = Σ S_d is exact, and summing over d = 1..9 gives the answer.
  Independent verification (second route): the same enumerator restricted to
  [0, 10^6] must agree with a naive per-n counter, and it must reproduce the
  statement's oracle f(11,1)=4, f(12,1)=5, first solutions 0, 1, 199981, and
  s(1)=22786974071. Agreement is a certificate that G1's formula and G3's
  skip logic are not simultaneously wrong in a way that changes the sum.
status: sketched
rests-on: none (the problem statement's own oracle targets are input facts, not library claims)
killed-by: none
```

```gap
id: G1-f-closed-form
lemma: >
  For n ≥ 0 and digit d in {0,...,9}, f(n,d) is computable in exact integer
  arithmetic in O(number of decimal digits of n) by the standard place-value
  digit count (digit-DP / per-position contribution). Formally: for n with
  digits a_{k}...a_{0}, f(n,d) = Σ over positions i of the number of times
  position i carries digit d across 0..n, each term given by a closed formula
  in the higher digits, the lower digits, and 10^i. In particular the formula
  agrees with the problem's definition on 0..12 for d=1 (0,1,1,1,1,1,1,1,1,1,2,4,5)
  and gives f(22,2)=6.
status: discharged
discharged-by: G1-checked (code/out/closed-form-verified.md) — the closed form
  code/lib/digits.py::f_place_value was verified to agree with the brute-force
  oracle on the full n=0..12 table, f(22,2)=6, every n in 0..20000, and all 14
  solutions in 0..300000.
thread: none
next: none — G1 is computed and checked; the solver uses f_place_value.
```

```gap
id: G2-solution-bound
lemma: >
  For every digit d in {1,...,9}, every n with f(n,d)=n satisfies n ≤ d·10^10.
  This is the base-10, d>0 instance of Proposition 9.1 of Khovanova & Marton,
  "Archive Labeling Sequences" (arXiv:2305.10357v2, published Amer. Math.
  Monthly 132(8) 2025 780-787). Hypothesis check completed: the paper's
  fd(x,b) counts occurrences of digit d in the base-b writings of 1..x;
  because 0 contributes no occurrence of any digit d>0, fd(x,10) = f(x,d) for
  d>0, so the bound transfers verbatim. The bound is proven in the source
  (Prop 9.1 with proof), not conjectured.
status: discharged
discharged-by: km-prop91-bound (= G2-solution-bound)
thread: none
next: >
  tool_builder: use n ≤ d·10^10 as the search ceiling in code/solution.py and
  assert every solution found lies below it; the solver's completeness rests
  on this lemma together with G1 and G3.
```

```gap
id: G3-skip-completeness
lemma: >
  Let D = digits(B(d)) for the bound B(d) from G2, and let f = f(·,d). f is
  non-decreasing, and the number of occurrences of d in any single number is at
  most its number of digits (≤ D on [0,B(d)]). Then: (i) if c := f(n) > n,
  every solution m ≥ n has m ≥ c; (ii) if c < n, every solution m ≥ n has
  m ≥ n + (n−c)/(D−1). Consequently the iteration n ↦ c when c>n,
  n ↦ ⌈n + (n−c)/(D−1)⌉ when c<n, and (record n; n ↦ n+1) when c=n, started at
  n=0, visits a supersequence-free enumeration of exactly the solutions of
  f(n)=n and terminates at n > B(d).
status: discharged
discharged-by: >
  code/verify.py implements exactly these two rules (R1: f=c>n ⇒ resume at c;
  R2: coast ⌈(n−c)/(D−1)⌉) with D = digits of the bound, re-derived from
  monotonicity alone, and verified them: the jump iterator equals the naive
  oracle scan on [0, 300000] for d=1 exactly (458 probes vs 300001 scanned),
  and for all d on [0, 20000]; full-size runs for d=1..9 use 5 932–29 409
  f-evaluations per digit (86 649 total) and reproduce the sourced per-digit
  counts A130432 and the paper's Table 3 maxima (code/out/verify-output.txt,
  code/out/solution-run.log).
thread: none
next: none — G3 is computed and checked; completeness of the enumeration is
  established by the agreement with the brute-force scan on the reachable
  range together with the sourced bound G2.
```
