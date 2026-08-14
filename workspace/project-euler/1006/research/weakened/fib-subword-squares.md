# Weakened ladder: Fibonacci subword sum of squares (PE 1006)

Goal: compute Psi(k) = sum over the k+1 distinct length-k factors of the
Fibonacci word of (decimal value of the factor)^2, at k = 10^18, mod 101001001.

Definition restated: S_0 = "0", S_1 = "01", S_n = S_{n-1}S_{n-2}; the infinite
Fibonacci word f is the limit. |S_n| = F_{n+2}. A "Fibonacci subword" is a
contiguous factor of f. There are exactly k+1 distinct factors of length k
(Sturmian complexity p(k) = k+1).

```ladder
goal: Psi(10^18) mod 101001001, where Psi(k) = sum over the k+1 distinct length-k factors of the infinite Fibonacci word of (decimal value)^2, leading zeros ignored
difficulties: big-k, factor-set, cross-terms, fib-index, mod-exp
status: open
```

**Difficulty definitions** (short name = the switch that is ON in the full
problem and OFF in a rung that weakens it away):

- `big-k` — k = 10^18: there are k+1 factors and k digit positions, so any
  method that enumerates factors or iterates once per position/bit is
  infeasible. The intended method must be polylog in k.
- `factor-set` — there is no trivial closed form for the k+1 distinct factors.
  Hand check (k=5): the filter "avoid `11` and avoid `000`" yields 7 words but
  only 6 are factors — `10101` is spurious, because the gap sequence between
  consecutive 1s (distances 2 or 3) is itself a Fibonacci word and forbids the
  gap pattern "2,2". So the factors are words with isolated 1s, 0-runs in
  {1,2} (endpoints {0,1,2}), *and* a 1-gap sequence that is itself a
  Fibonacci factor. The real description is the Sturmian/bispecial-word
  structure (substitution tree, singular words), and it is the unknown core.
- `cross-terms` — Psi squares the value: if beta has value sum_j beta_j 10^{k-j},
  then Psi(k) = sum_{j,l} N(j,l;k) 10^{2k-j-l} where N(j,l;k) = #{factors with
  1 at both positions j,l}. This needs pairwise position correlations, not just
  per-position 1-counts.
- `fib-index` — for arbitrary k the factor set (and the counts N(j,l;k)) is
  organised by k's Fibonacci/Zeckendorf representation, not by a single integer
  parameter; a formula valid in one interval [F_n, F_{n+1}) must be threaded
  across all n.
- `mod-exp` — powers 10^{2k-j-l} have exponents up to 2*10^18 and must be
  reduced mod 101001001 (order of 10 mod p, possible gcd(10,p) > 1) without
  losing the k-structure of the recurrence.

**Note that removes a would-be difficulty:** "ignoring leading zeros" is
automatic. A factor beta = b_1...b_k has value sum_j b_j 10^{k-j}; leading
zeros contribute 0 regardless of their exponent, so the decimal value equals
this weighted sum with no case-splitting. Sanity check on the statement's
oracle: Psi(3) = 1^2+10^2+100^2+101^2 = 1+100+10000+10201 = 20302. (matches)

```rung
id: R0-small-brute
statement: For k <= 40 compute Psi(k) exactly by reading a long enough finite Fibonacci word S_n (F_{n+2} >= k + margin), collecting its distinct length-k substrings, and summing squares of their decimal values; must reproduce Psi(3)=20302 and Psi(10) = 10699667 (mod 101001001). This is the oracle for every higher rung.
off: big-k, factor-set, cross-terms, fib-index, mod-exp
stance: open
merge: turn on factor-set: replace substring enumeration by an explicit, brute-verified description of the k+1 distinct factors. R1 does this at the linear level first, where only the factor set (not pairwise positions) is needed.
```

```rung
id: R1-factor-structure-linear
statement: Derive and verify against R0 (k <= 40) an explicit structural description of the k+1 distinct length-k factors of f (substitution tree / bispecial and singular words / 1-gap-word characterisation), and use it to compute Phi(k) = sum over factors of sum_j beta_j 10^{k-j} (sum of decimal values, unsquared) without enumerating substrings.
off: big-k, cross-terms, fib-index, mod-exp
stance: open
merge: turn on cross-terms: from the factor description extract the pairwise correlation N(j,l;k) = #{factors with 1 at both j and l}. First move: classify a factor by its 1-gap sequence and decide which position pairs (j,l) are compatible with a given gap pattern, since Psi = sum_{j,l} N(j,l;k) 10^{2k-j-l}.
```

```rung
id: R2-pairwise-correlations
statement: Using the R1 factor description, compute Psi(k) = sum_{j,l} N(j,l;k) 10^{2k-j-l} exactly (or mod p) for moderate k (k <= 10^6) without enumerating factors, and verify against R0 at k <= 40 and against direct substring enumeration wherever brute force reaches.
off: big-k, fib-index, mod-exp
stance: open
merge: turn on fib-index: express N(j,l;k) (or Psi(k) directly) as a function of k's Fibonacci/Zeckendorf representation so it evaluates at arbitrary k. First move: a uniform formula on one Fibonacci interval [F_n-2, F_{n+1}-2] plus a substitution-tree recurrence in n.
```

```rung
id: R3-arbitrary-k-recurrence
statement: Obtain a recurrence or closed form for Psi(k) valid for arbitrary k >= 1, via the Fibonacci/Zeckendorf representation of k (equivalently a transfer/matrix recurrence in the Fibonacci index n with the k-th entry extracted), and verify it against R2 over a range of k.
off: big-k, mod-exp
stance: open
merge: turn on mod-exp: evaluate the recurrence at k = 10^18 using fast matrix/doubling exponentiation with all arithmetic mod 101001001. First move: find the order of 10 mod p (and whether gcd(10,p)=1) so exponents 2k-j-l can be reduced, then check that the recurrence's matrices exponentiate in O(log k).
```

```rung
id: R4-full-problem
statement: Compute Psi(10^18) mod 101001001 by the R3 recurrence, all arithmetic mod 101001001, fast (log k) exponentiation of both the linear recurrence and the powers of 10; output the residue.
off: big-k
stance: open
merge: none - this is the full-strength target; if it is settled the ladder is exhausted.
```
