# PE1006 — Ψ(k) as a second moment of mechanical-word floor-sums

Skeleton decomposing the goal "compute Ψ(10^18) mod M, M = 101001001" into
propositions that can each be attacked alone. Built from the problem statement
(`problem.md`) and two steering directives (`config/directives.jsonl`). The run
currently establishes **no claim** — all four lemmas below are open gaps, and
none has a `rests-on` id.

**Problem, precisely.** S_0=0, S_1=01, S_n = S_{n-1}S_{n-2}. A *Fibonacci
subword* is a contiguous substring of some S_n. For each k ≥ 1 there are
exactly k+1 distinct length-k subwords. Read each as a decimal (the value
Σ_j d_j 10^{k-1-j} already ignores leading zeros), square, sum:
Ψ(k) = Σ_w (value(w))². Find Ψ(10^18) mod M.

```skeleton
goal: compute Psi(k) mod M for k = 10^18, M = 101001001, where
      Psi(k) is the sum of squares of the decimal values of the k+1 distinct
      Fibonacci subwords of length k.
implies: Let F be the infinite Fibonacci word (limit of the S_n). Lemma 1
      identifies the k+1 length-k Fibonacci subwords with the length-k factors
      of F and fixes their count as k+1. Lemma 2 gives the mechanical-word /
      rotation representation of those factors: for any n with F(n) > k and
      slope a = F(n-1)/F(n), cutting the unit circle at the k+1 points
      frac(-ma), m = 0..k, and taking arc midpoints x_m yields digit_j(x_m) =
      floor(x_m+(j+1)a) - floor(x_m+ja), and the k+1 factors are exactly the
      words v(x_m) = sum_j digit_j(x_m) 10^(k-1-j). Hence
      Psi(k) = sum_{m=0}^k v(x_m)^2. Lemma 3 telescopes each v(x_m) into
      floor(x_m+ka) - 10^(k-1) floor(x_m) + 9 sum_{j=1}^{k-1} 10^(k-1-j)
      floor(x_m+ja), so Psi(k) is a second moment of a geometrically weighted
      floor-sum over the m-range 0..k. Lemma 4 proves the universal Euclidean
      algorithm (monoid generalisation of floor_sum / Chtholly's algorithm)
      evaluates this second moment in O(log k) exact modular arithmetic using
      x = 10^(-1) mod M (legitimate because gcd(10,M)=1). Composing the four
      equalities at k = 10^18 with n = min index having F(n) > 10^18, and
      reducing mod M at the end, yields the answer. Quantifier note: the count
      k+1 from Lemma 1 is exactly the number of arc midpoints in Lemma 2, which
      is the point at which the two sides of the bijection match.
status: sketched
rests-on: (none yet — the library holds no claim for this problem)
killed-by: (none; a broken reduction would be recorded here)
```

```gap
id: G1-sturmian-factor-structure
lemma: Let F be the infinite Fibonacci word (limit of S_0=S_1... with S_n =
      S_{n-1}S_{n-2}). For every length k ≥ 1, the set of distinct Fibonacci
      subwords (substrings of some S_n) equals the set of length-k contiguous
      factors of F, and there are exactly k+1 of them. F is the characteristic
      Sturmian word of slope 1/phi^2, and a Sturmian word has factor complexity
      p(k) = k+1.
status: open
discharged-by: (none — no claim in the library)
thread: (none yet)
next: (a) compute, by direct generation of S_1..S_n and substring harvesting
      alongside a direct factor enumeration of the infinite word, that the two
      sets agree and have size k+1 for k = 1..60; (b) record the standard
      citation (Berstel/Morse–Hedlund: Sturmian words have factor complexity
      n+1; the Fibonacci word is Sturmian) as a claim block with source URL so
      it reaches research/CLAIMS.md and can discharge this gap on a source's
      word.
```

```gap
id: G2-mechanical-word-representation
lemma: For n with F(n) > k and rational slope a = F(n-1)/F(n), the k+1 length-k
      factors of F are produced exactly by the rotation/mechanical construction:
      cut the unit circle at the k+1 points frac(-ma), m=0..k; for the midpoint
      x_m of each arc define digit_j(x_m) = floor(x_m+(j+1)a) - floor(x_m+ja),
      j=0..k-1. The k+1 words so obtained are exactly the k+1 distinct length-k
      factors, digits in {0,1}. (This subsumes directive 1's case k = F_n - 1,
      where the factors are the F_n rotations of the truncated standard word.)
      Remark on exactness: every quantity is a rational with denominator F(n)^2
      or better, and floor is exact-integer, so the construction is
      checkable exactly, not in floating point.
status: open
discharged-by: (none)
thread: (none yet)
next: reproduce directive 2's check in-container: implement the construction for
      k = 3,5,8,10,13,17,21,26,34,40,55 (non-Fibonacci k included) with n the
      smallest index with F(n) > k, compare the produced digit words against the
      actual distinct length-k substrings of S_1..S_{n+2}, and assert exact set
      equality. This is the load-bearing representation; attack it first.
```

```gap
id: G3-telescoped-second-moment
lemma: With v(x) = sum_{j=0}^{k-1} digit_j(x) 10^(k-1-j) where digit_j(x) =
      floor(x+(j+1)a) - floor(x+ja), summation by parts (telescoping) gives
      v(x) = floor(x+ka) - 10^(k-1) floor(x) + 9 sum_{j=1}^{k-1} 10^(k-1-j)
      floor(x+ja). Consequently Psi(k) = sum_{m=0}^k v(x_m)^2 is a second moment
      of a geometrically weighted floor-sum over the contiguous range m = 0..k,
      and the positional weights already enforce "ignore leading zeros"
      (leading digits contribute value 0).
status: open
discharged-by: (none — algebraic identity, not yet checked in-container)
thread: (none yet)
next: verify the identity exactly in Python for random small (k, x_m) against the
      direct digit sum, and check that sum_{m} v(x_m)^2 with the Lemma 2 reps
      reproduces Psi(3) = 20302 and Psi(10) ≡ 10699667 mod M — the statement's
      own oracle values. Until these print correctly the reduction has not
      touched the goal.
```

```gap
id: G4-universal-euclidean-floor-sum
lemma: The quantity Psi(k) = sum_{m=0}^k v(x_m)^2 mod M, with v(x_m) the
      telescoped geometric floor-sum from Lemma 3, is evaluated in O(log k)
      exact rational-free modular steps by the universal Euclidean algorithm
      (monoid generalisation of the AtCoder floor_sum, Chtholly's algorithm),
      carrying the tuple (count, sum x^j, sum x^j floor, sum x^j floor^2) with
      x = 10^(-1) mod M. Correctness is by induction on the Euclidean step; it
      never enumerates the k+1 representatatives or the k-1 floor terms.
status: open
discharged-by: (none)
thread: (none yet)
next: implement Chtholly's tuple-recursion in sympy/gmpy2, check it against a
      brute-force enumeration of sum_{m=0}^k v(x_m)^2 for k = 1..150, and against
      Psi(10) ≡ 10699667 mod M; then run at k = 10^18 with F(n) > 10^18 and
      confirm the result is a fixed point of re-checking (deterministic exact
      integers). Record the running time and the exact congruence it prints.
```
