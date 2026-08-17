# Ladder: Fibonacci subword squares (PE1006)

The difficulties named below are the *specific* obstructions, not the topics.
Legend for the short names used in `off`:

- `huge-k` — k = 10^18. There are k+1 factors, so any per-factor or per-position
  scan costs ~10^18 operations. Evaluation must be O(log k) via a recurrence or
  closed form, never a scan over the factor set.
- `unbounded-n` — a factor is "a substring of *some* S_n", i.e. the definition
  quantifies over all n. One must show the factor set of S_n stabilizes to the
  factor set of the infinite Fibonacci word f = lim S_n, with a computable
  threshold n0(k). Without that, "smallest n by scanning" is a guess.
- `factor-classification` — the k+1 distinct length-k factors are not given
  explicitly. Identifying each of them exactly once (no repeats, no omissions)
  requires the Sturmian/Christoffel classification (balanced binary words,
  mechanical/standard words) for slope 1/φ². The count k+1 is stated, the
  enumeration is not.
- `sum-of-squares` — Ψ(k) is the sum of (integer value)² over the factor set, a
  quadratic function of the bits, not a linear statistic. Even with the factors
  classified, one needs the 2-point statistics (how many factors have 1s at a
  given pair of positions) to avoid per-factor squaring.
- `modulus` — the answer is required mod 101001001, not exactly. Ψ(10^18) has
  about 6·10^17 decimal digits, so exact integer arithmetic at full k is
  infeasible, and every division in a closed form must be valid mod 101001001
  (or routed through CRT after factoring the modulus).

```ladder
goal: Find Ψ(10^18) mod 101001001, where Ψ(k) is the sum of squares of the integer values of the k+1 distinct length-k Fibonacci subwords (contiguous substrings of some S_n, S_0="0", S_1="01", S_n=S_{n-1}S_{n-2}).
difficulties: huge-k, unbounded-n, factor-classification, sum-of-squares, modulus
status: open
```

```rung
id: R0-brute-oracle
statement: For each fixed k <= 30, compute Ψ(k) exactly by scanning S_n for the smallest n whose set of length-k subwords has cardinality k+1 (i.e. has stabilized), then summing the squares of the integer values of those distinct subwords. Deliverable: exact Ψ(k) for k = 1..30, reproducing the given Ψ(3)=20302 and Ψ(10) ≡ 10699667 (mod 101001001).
off: huge-k, unbounded-n, factor-classification, sum-of-squares, modulus
stance: open
merge: Turn `unbounded-n` back on — replace "smallest n found by scanning" with a theorem that the factor set of S_n stabilizes to the factor set of the infinite Fibonacci word f = lim S_n, and give a computable n0(k). First move: confirm the standard Sturmian fact that f is uniformly recurrent with exactly k+1 length-k factors, and pin down the stabilization threshold.
```

```rung
id: R1-stabilization
statement: The set of distinct length-k subwords of S_n is constant for all n >= n0(k), equals the set of length-k factors of the infinite Fibonacci word f = lim_{n->∞} S_n, and has cardinality exactly k+1 for every k >= 1; give a computable n0(k) and a proof or sourced citation of the count.
off: huge-k, factor-classification, sum-of-squares, modulus
stance: open
merge: Turn `factor-classification` back on — lift the bare count k+1 to an explicit bijection {0,...,k} -> factors via the standard description (balanced binary words with ⌊k/φ²⌋ or ⌈k/φ²⌉ ones, equivalently Christoffel/standard words for slope 1/φ²). First move: fetch a sourced statement of the Sturmian factor classification and specialize it to the Fibonacci word.
```

```rung
id: R2-factor-parameterization
statement: For every k >= 1 there is an explicit, indexable description of each of the k+1 length-k factors of the Fibonacci word: a bijection j -> w_j (0 <= j <= k) such that w_j is a balanced binary word whose number of 1s is one of the two consecutive values determined by k/φ², each w_j is computable bit-by-bit in O(k) from j, and {w_j} is exactly the factor set with no repeats.
off: huge-k, sum-of-squares, modulus
stance: open
merge: Turn `sum-of-squares` back on — write Ψ(k) = Σ_j (Σ_i w_j[i]·2^{k-i})² as a double sum over bit positions, reducing to the count of factors with a 1 at each position and at each pair of positions. First move: compute the per-position and 2-point statistics of the w_j family from the R2 parameterization.
```

```rung
id: R3-closed-form-sum
statement: Using the R2 parameterization, express Ψ(k) exactly as a closed form or a fixed-order linear recurrence / transfer-matrix expression in k, with no per-factor or per-position iteration at the 10^18 scale; validate against R0's exact values for k <= 30.
off: huge-k, modulus
stance: open
merge: Turn `huge-k` back on — exhibit Ψ(k) as a linear recurrence of k-independent order and build an exact O(log k) matrix-power evaluator, validated by direct O(k) recurrence iteration up to k = 10^6. First move: identify the minimal-order recurrence satisfied by the R0 sequence (k = 1..30).
```

```rung
id: R4-log-k-engine
statement: Evaluate Ψ(k) in O(log k) arithmetic operations via the R3 recurrence or closed form, with exact integer arithmetic, and validate the engine: reproduce R0 for k <= 30 and agree with direct O(k) recurrence iteration for k up to 10^6. (Exact Ψ(10^18) has ~6·10^17 digits, so this rung delivers the fast engine, not a printed integer.)
off: modulus
stance: open
merge: Turn `modulus` back on — run every arithmetic step mod 101001001; factor the modulus and, if the closed form divides by any d, verify gcd(d, 101001001) = 1 or route through CRT. First move: factor 101001001 and check invertibility of every denominator in the R3 formula.
```

```rung
id: R5-full-problem
statement: Find Ψ(10^18) mod 101001001 — the full Project Euler 1006 answer.
off: none
stance: open
merge: Ladder exhausted once settled: this rung is the goal with all five difficulties switched back on.
```
