# Skeleton: Fibonacci subword squares (PE1006)

Goal: `Psi(10^18) mod 101001001`, where `Psi(k)` is the sum of the squares of
the integer values of the `k+1` distinct length-`k` Fibonacci subwords, read as
decimals ignoring leading zeros.

The goal is not one quantity; it is a pipeline. Each lemma below removes one of
the five obstructions named in `research/weakened/fibonacci-subword-squares.md`
(`unbounded-n`, `factor-classification`, `sum-of-squares`, `huge-k`, `modulus`),
and the `implies` field is the chain that recombines them.

```skeleton
goal: Psi(10^18) mod 101001001, where Psi(k) = sum over the k+1 distinct length-k Fibonacci subwords of (integer value of the subword)^2.
implies: Fix k. By G-stabilization, the set of distinct length-k subwords of some S_n equals the set of length-k factors of the infinite Fibonacci word f = lim S_n once n >= n0(k), so Psi(k) is a sum over the k+1 factors of f, independent of n. By G-factor-parameterization there is an explicit bijection j -> w_j (0 <= j <= k) enumerating those k+1 factors, so Psi(k) = sum_{j=0}^k val(w_j)^2 with no repeats or omissions. By G-closed-form-sum, this double sum (squaring is a quadratic function of the bits) collapses to a closed form or fixed-order linear recurrence in k, with no per-factor or per-position iteration, each coefficient an exact integer with denominators D. By G-log-k-engine, that recurrence is evaluated at k = 10^18 in O(log k) arithmetic, working modulo 101001001 with every denominator d in D verified invertible (gcd(d, 101001001) = 1, else routed through CRT after factoring the modulus). Substituting k = 10^18 gives the answer.
status: live
rests-on: none (the stated fact "exactly k+1 distinct length-k subwords" from problem.md is subsumed and sharpened by G-stabilization; the Sturmian identification of f is sourced in research/summaries/morse-hedlund-theorem-sturmian-characterization.md)
killed-by: none
```

```gap
id: G-stabilization
lemma: For every k >= 1 there is a computable n0(k) such that the set of distinct length-k subwords of S_n is constant for all n >= n0(k), equals the set of length-k factors of the infinite Fibonacci word f = lim_{n->inf} S_n, and has cardinality exactly k+1. (This closes the `unbounded-n` difficulty: the definition quantifies over "some S_n", and this lemma pins that quantifier to the infinite word with an explicit threshold.)
status: open
discharged-by: none
thread: research/threads/fibonacci-subword-squares.md
next: Have brute.py scan S_n for each k <= 30 and record the smallest n whose length-k subword set has size k+1; compare that empirical threshold against the Fibonacci-index candidate n0(k) = smallest n with |S_{n-1}| >= k (or the sourced Sturmian recurrence threshold) and confirm the sets coincide with the factors of f. This is checkable today and falsifies the threshold guess if the empirical stabilizer jumps differently.
```

```gap
id: G-factor-parameterization
lemma: For every k >= 1 there is an explicit, indexable bijection j -> w_j (0 <= j <= k) between {0,...,k} and the length-k factors of the Fibonacci word, such that each w_j is a balanced binary word whose number of 1s is one of the two consecutive values determined by k/phi^2, each w_j is computable bit-by-bit in O(k) from j, and {w_j : 0 <= j <= k} is exactly the factor set with no repeats. (This closes the `factor-classification` difficulty and turns the bare count k+1 into an enumeration.)
status: open
discharged-by: none
thread: research/threads/fibonacci-subword-squares.md
next: Fetch the sourced Sturmian/Christoffel factor classification (the request `precise-sourced-statement-c1ec` in research/REQUESTS.md is exactly this), specialize it to slope 1/phi^2, and write down the bijection j -> w_j explicitly; validate it against brute.py's factor list for k <= 30.
```

```gap
id: G-closed-form-sum
lemma: With the G-factor-parameterization in hand, Psi(k) = sum_{j=0}^k val(w_j)^2 admits a closed form or a fixed-order linear recurrence in k (order independent of k). Writing val(w_j) = sum_i w_j[i] 2^{k-1-i} and expanding the square, this reduces to the per-position counts C_1(k,i) = #{j : w_j[i]=1} and the two-point counts C_2(k,i,i') = #{j : w_j[i]=w_j[i']=1}, each of which is a closed form in (k,i,i') from the parameterization. (This closes the `sum-of-squares` difficulty: no per-factor squaring.)
status: open
discharged-by: none
thread: research/threads/fibonacci-subword-squares.md
next: From the j -> w_j bijection, compute C_1 and C_2 explicitly for k <= 30, form Psi(k) = sum_{i,i'} 2^{(k-1-i)+(k-1-i')} C_2(k,i,i'), and run pattern-finding on the resulting integer sequence (Psi(1)..Psi(30)) to identify the minimal-order recurrence; cross-check the closed form against the brute values Psi(3)=20302 and Psi(10)=10699667.
```

```gap
id: G-log-k-engine
lemma: Psi(k) can be evaluated at k = 10^18 in O(log k) arithmetic operations via the G-closed-form-sum recurrence (matrix exponentiation or fast closed-form evaluation), with exact integer arithmetic, and every arithmetic step can be carried out modulo M = 101001001: factor M, and for every denominator d appearing in the closed form verify gcd(d, M) = 1, else route through CRT on the coprime prime-power factors of M. (This closes the `huge-k` and `modulus` difficulties.)
status: open
discharged-by: none
thread: research/threads/fibonacci-subword-squares.md
next: Factor 101001001, check invertibility of every denominator in the G-closed-form-sum formula, build the matrix-power (or fast evaluation) engine, and validate it by reproducing the brute Psi(k) for k <= 30 and a direct O(k) recurrence iteration for k up to 10^6 before running at k = 10^18.
```

## Notes

- The gap ids G-stabilization, G-factor-parameterization, G-closed-form-sum,
  G-log-k-engine mirror the rungs R1–R4 of the ladder in
  `research/weakened/fibonacci-subword-squares.md`, but here they are stated as
  propositions the run must prove, with the inference that recombines them
  written in `implies`.
- `rests-on` is empty because no claim has been discharged yet
  (`research/CLAIMS.md` records none); the stated `k+1` fact from the problem is
  a given, and G-stabilization is the lemma that proves it rather than assumes
  it.
