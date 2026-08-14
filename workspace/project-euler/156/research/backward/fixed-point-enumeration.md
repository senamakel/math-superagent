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
status: open
discharged-by: none
thread: none
next: >
  tool_builder: implement the formula in code/lib/digitcount.py (or fold it
  into code/solution.py), then verify it equals the naive per-n count for all
  d in 0..9 and all n ≤ 10^4, and against the oracle points f(11,1)=4,
  f(12,1)=5, f(22,2)=6. Record the result as a `claim` block (id, statement,
  status: checked) in code/out/ so it reaches research/CLAIMS.md.
```

```gap
id: G2-solution-bound
lemma: >
  For every digit d in {1,...,9}, every n with f(n,d)=n satisfies n ≤ d·10^10.
  This is the base-10, d>0 instance of Proposition 9.1 of the "sticker
  numbers / exactly numbers" paper (recalled in memory, identity not yet on
  disk). Hypothesis check needed before use: the paper's fd(x,b) counts
  occurrences of digit d in the base-b writings of the numbers 1..x; because
  0 contributes no occurrence of any digit d>0, fd(x,10) = f(x,d) for d>0, so
  the bound transfers verbatim.
status: open
discharged-by: none
thread: none
next: >
  librarian/theorem_prover: fill request `identify-sticker-numbers-eeda`
  (already posted in research/REQUESTS.md) — download the identifiable paper,
  extract Lemma 5.1 and Proposition 9.1, and confirm (a) the 1-based vs
  0-based count agrees for d>0 and (b) the bound is proven, not conjectured.
  Record the bound as a `claim` block with hypotheses and anchor URL. If the
  source cannot be identified, the fallback is an independent proof of the
  bound, which is a separate theorem_prover task and should be filed rather
  than silently assumed.
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
status: open
discharged-by: none
thread: none
next: >
  theorem_prover: prove (i) from monotonicity of f (f(m) ≥ f(n) = c > m for
  n ≤ m < c) and (ii) from f(m) ≤ c + (m−n)·D. tool_builder: implement the
  jump iterator with these two rules as the only skip logic, run it for all
  d in 1..9, and confirm the output equals a naive per-n counter on
  [0, 10^5] (and reproduces first solutions 0, 1, 199981 for d=1). Report the
  iteration count up to B(d) — if it does not stay small, the bound D in the
  c<n jump is too coarse and the block formulation must replace it; that
  failure would kill G3, not the goal.
```
