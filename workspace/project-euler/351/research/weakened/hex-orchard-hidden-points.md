# Ladder: hexagonal orchard hidden points (Project Euler 351)

Weakener's ladder. Each rung is the full goal with the named difficulties in
`off` switched off; climbing turns them back on one at a time, so the top rung
is the goal itself. All rungs are settled: the forward loop computed the answer
and verified it three ways, so the ladder is exhausted.

```ladder
goal: Compute H(100 000 000) for Project Euler 351, where H(n) is the number of
      points hidden from the center in a hexagonal orchard of order n (the
      triangular-lattice points inside a regular hexagon of side n); the
      statement's oracle values are H(5)=30, H(10)=138, H(1000)=1177848.
difficulties: hex-geometry, compute-Phi-linear, n-bound-1e8, sublinear-Phi-recursion, answer-verification
status: closed
```

```rung
id: R-hex-brute-examples
statement: Enumerate the triangular-lattice points of the order-n hexagon,
            { (a,b) in Z^2 : |a|<=n, |b|<=n, |a+b|<=n }, for n in {5,10} and
            count those hidden from the center by the definition itself: a
            point (a,b) != (0,0) is hidden iff some lattice point lies strictly
            between it and the origin on the same ray (equivalently gcd(a,b)>1).
            Recover H(5)=30 and H(10)=138.
off: hex-geometry, compute-Phi-linear, n-bound-1e8, sublinear-Phi-recursion, answer-verification
status: closed
closed-by: coprimality-iff-visible, hexagonal-orchard-closed-form
merge: DONE — brute.py reproduces H(5)=30, H(10)=138, H(1000)=1177848 and
       confirms hidden <=> gcd(a,b)>1, visible = 6*Phi(n)+1, total = 3n^2+3n+1.
```

```rung
id: R-hex-totient-reduction
statement: Prove, and check against all three statement oracles, that
            H(n) = 3n^2 + 3n - 6*Phi(n) for every n >= 1, where
            Phi(n) = sum_{k=1..n} phi(k) is the summatory totient; equivalently
            H(n) = 6*A063985(n) with A063985(n) = sum_{k<=n} (k - phi(k)).
            Check Phi(5)=10, Phi(10)=32, Phi(1000)=304192, hence
            H(1000) = 3003000 - 6*304192 = 1177848.
off: compute-Phi-linear, n-bound-1e8, sublinear-Phi-recursion, answer-verification
status: closed
closed-by: pe351-hidden-formula, hexagonal-orchard-closed-form
merge: DONE — the closed form is proved, checked against the three oracles, and
       catalogued as OEIS A216453 (Kumar–Israel 2014; = 6*A063985, Maiga 2019).
```

```rung
id: R-linear-Phi-sieve-crosscheck
statement: Implement an exact O(n log log n) sieve producing phi(k) and the
            prefix sum Phi(k) for k up to n, confirm Phi(1000)=304192, and
            cross-check H(n) against the R0 brute-force enumeration on every n
            the brute force still reaches, reporting the largest n where the
            two agree.
off: n-bound-1e8, sublinear-Phi-recursion, answer-verification
status: closed
closed-by: totient-sum-verification-values
merge: DONE — solution.py (totient sieve) agrees with brute.py at n=5,10,1000
       and reproduces Phi(10^k) for k=0..8 (check_library_values.py).
```

```rung
id: R-Phi-1e8-linear-probe
statement: Compute Phi(10^8) by the linear sieve (or a segmented variant) and
            hence H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8) exactly. This rung
            exists to test whether the 10^8 bound genuinely forces sublinearity
            or is merely at the edge of what a linear sieve can reach.
off: sublinear-Phi-recursion, answer-verification
status: closed
closed-by: totient-sum-verification-values
merge: DONE — the int32 sieve computes Phi(10^8)=3039635516365908 in O(n log
       log n) time / ~400 MB; the bound does not force sublinearity here, and
       the answer H(10^8)=11762187201804552 is banked from this rung.
```

```rung
id: R-sublinear-Phi-recursion
statement: Compute Phi(n) by the floor-grouped recursion
            Phi(n) = n(n+1)/2 - sum_{k=2..n} Phi(floor(n/k)) with memoization,
            prove its correctness, verify it reproduces Phi(1000)=304192 and
            matches the linear sieve's Phi(n) for n up to at least 10^7, and
            report its time and memory at 10^8. With Phi(10^8) in hand,
            H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8).
off: answer-verification
status: closed
closed-by: totient-sum-fast-recursion, gauss-divisor-sum-of-totient
merge: DONE — Chai Wah Wu's A063985 recursion (same floor-grouped family) gives
       A063985(10^8)=1960364533634092, H=6*A063985=11762187201804552;
       the Gauss floor-quotient route is recorded as the optional fourth route
       (research/approaches/dirichlet-hyperbola-gauss-2-3.md).
```

```rung
id: R-goal-H-1e8-verified
statement: H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8), computed exactly and
            confirmed by a second independent route; this is the full Project
            Euler 351 answer with no difficulty switched off.
off:
status: closed
stance: closed
closed-by: pe351-h6a063985-identity, pe351-mod12-period4
merge: DONE — H(10^8)=11762187201804552 computed and confirmed by three
       independent routes; matches the published PE 351 answer
       (research/research-report-pe351-known-verification.md).
```
