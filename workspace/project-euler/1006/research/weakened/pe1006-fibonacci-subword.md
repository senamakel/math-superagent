# PE1006 — Ψ(k): sum of squares of the decimal values of the Fibonacci subwords of length k

Notation (from `problem.md`): S_0=0, S_1=01, S_n = S_{n-1} S_{n-2}; a *Fibonacci
subword* is a contiguous substring of some S_n. For each length k there are
exactly k+1 Fibonacci subwords; interpreting each as a decimal number (leading
zeros ignored) and squaring gives values V_1..V_{k+1}, and
Ψ(k) = Σ V_i^2. Oracle: Ψ(3)=20302 (subwords 001,010,100,101 → values
1,10,100,101 → 1+100+10000+10201); Ψ(10) ≡ 10699667 (mod 101001001). Target:
Ψ(10^18) mod 101001001. All rungs below are open — `search_claims` returns
nothing on Fibonacci subwords, and the survey confirms no brute oracle has been
run in-container yet.

```ladder
goal: compute Psi(10^18) mod 101001001, where Psi(k) is the sum of squares of the decimal values (leading zeros ignored) of the k+1 distinct Fibonacci subwords of length k
difficulties: k=10^18, self-similar factor set, leading zeros dropped, square second moment, power-10 weights mod M
status: open
```

```rung
id: R1-brute-oracle
statement: compute Psi(k) exactly for 1 <= k <= 10 by exhaustive substring enumeration over finite prefixes S_n large enough to contain every length-k subword, keeping the full problem shape (decimal reading, leading zeros dropped, squares, no modulus needed at this size). Must reproduce Psi(3)=20302 and Psi(10) % 101001001 = 10699667.
off: k=10^18
stance: open
merge: replace brute substring enumeration with the structural fact that the length-k factors of the infinite Fibonacci word are exactly k+1, characterized self-similarly instead of by scanning S_n; climb to the count-only rung.
```

```rung
id: R2-factor-count
statement: prove and verify (for small k) that the infinite Fibonacci word has exactly k+1 distinct factors of length k, and give the self-similar recursion for the factor set — the objects Psi sums over. No values, no squares, no weighting are involved.
off: k=10^18, square second moment, power-10 weights mod M
stance: open
merge: attach to each of the k+1 factors its decimal value, reintroducing the place-weighting; climb to the first-moment rung.
```

```rung
id: R3-first-moment
statement: compute the first moment Psi_1(k) = sum of the k+1 factor values (leading zeros still dropped, decimal reading), instead of the sum of squares. Drops the cross-term structure that makes the second moment hard, while keeping the factor set and the place weights.
off: k=10^18, square second moment
stance: open
merge: reintroduce squaring — the single hardest step is the coupling of two position weights inside V_i^2 — to get from a first-moment sum to the second-moment form Psi(k).
```

```rung
id: R4-moderate-second-moment
statement: compute the full second moment Psi(k) with the real shape (self-similar factor set, leading zeros dropped, decimal reading, squares) at moderate k (up to ~10^3-10^6), by any O(k) or enumerable method, and check it against R1's brute oracle where the ranges overlap. This is the whole problem except for the astronomical scale: everything structural is present, only the size is tamed.
off: k=10^18
stance: open
merge: scale k up to 10^18, which forces the O(k)-per-factor and O(k)-sums machinery to collapse into an O(log k) evaluation — the power-10 geometric weights x^j (x = 10^-1 mod M) become a floor-sum / Euclidean recursion carried mod 101001001. This is the rung that becomes the goal.
```

```rung
id: R5-full
statement: the goal itself — evaluate Psi(10^18) mod 101001001 via the geometric-weight sum sum over the factor set of V_i^2 modulo M, using an O(log k) Euclidean/floor-sum recursion (integer part of j*a with a = F(n-1)/F(n), weights 10^(k-1-j), carried as (count, sum, sum-of-squares) mod M). Reached only by climbing R1-R4.
off: (none)
stance: open
merge: none — this is the full-strength target. The ladder is exhausted exactly when this rung is settled.
```
