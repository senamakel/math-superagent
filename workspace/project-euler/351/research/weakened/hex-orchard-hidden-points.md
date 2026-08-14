# Ladder: hexagonal orchard hidden points (Project Euler 351)

Weakener's ladder. Each rung is the full goal with the named difficulties in
`off` switched off; climbing turns them back on one at a time, so the top rung
is the goal itself. Nothing here is settled yet: `research/CLAIMS.md` is empty
and no `code/brute.py` exists on disk, so every rung is `open` until the
forward loop attacks it.

```ladder
goal: Compute H(100 000 000) for Project Euler 351, where H(n) is the number of
      points hidden from the center in a hexagonal orchard of order n (the
      triangular-lattice points inside a regular hexagon of side n); the
      statement's oracle values are H(5)=30, H(10)=138, H(1000)=1177848.
difficulties: hex-geometry, compute-Phi-linear, n-bound-1e8, sublinear-Phi-recursion, answer-verification
status: open
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
stance: open
merge: turning hex-geometry back on. On this brute oracle, confirm hidden <=>
       gcd(a,b)>1, that the visible (gcd=1) points number 6*Phi(n)+1 counting
       the center, and that the total is 3n^2+3n+1, which yields
       H(n) = 3n^2+3n-6*Phi(n) = 6*A063985(n) with Phi(n)=sum_{k<=n} phi(k)
       and A063985(n)=sum_{k<=n}(k-phi(k)). This is the whole of R1.
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
stance: open
merge: turning compute-Phi-linear back on. Replace the hand-listed phi values
       with an exact O(n log log n) sieve of phi(k) and its prefix sum Phi(k),
       and re-derive Phi(1000)=304192 mechanically; that is R2.
```

```rung
id: R-linear-Phi-sieve-crosscheck
statement: Implement an exact O(n log log n) sieve producing phi(k) and the
            prefix sum Phi(k) for k up to n, confirm Phi(1000)=304192, and
            cross-check H(n) against the R0 brute-force enumeration on every n
            the brute force still reaches, reporting the largest n where the
            two agree.
off: n-bound-1e8, sublinear-Phi-recursion, answer-verification
stance: open
merge: turning n-bound-1e8 back on. Run the sieve at n=10^8 and observe whether
       its memory (~10^8 phi values, ~400 MB as uint32) and time are actually
       prohibitive in this environment. If it completes, the bound does not
       bite and H(10^8) is banked straight from this rung; if it dies, the
       failure is the first move into R4's recursion.
```

```rung
id: R-Phi-1e8-linear-probe
statement: Compute Phi(10^8) by the linear sieve (or a segmented variant) and
            hence H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8) exactly. This rung
            exists to test whether the 10^8 bound genuinely forces sublinearity
            or is merely at the edge of what a linear sieve can reach.
off: sublinear-Phi-recursion, answer-verification
stance: open
merge: turning sublinear-Phi-recursion back on. Derive
       Phi(n) = n(n+1)/2 - sum_{k>=2} Phi(floor(n/k)) from
       sum_{d=1..n} phi(d)*floor(n/d) = n(n+1)/2, memoize the O(sqrt n)-many
       distinct values Phi(floor(n/k)), and match the sieve's Phi(n) at every
       n where the sieve was trusted. That is R4.
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
stance: open
merge: turning answer-verification back on. Produce a second, independent route
       to Phi(10^8) -- the same recursion with a different floor-grouping/
       partition, or a segmented sieve of phi up to 10^8, or the
       Dirichlet-hyperbola double sum -- and confirm the two agree on H(10^8).
       That is the full goal.
```

```rung
id: R-goal-H-1e8-verified
statement: H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8), computed exactly and
            confirmed by a second independent route; this is the full Project
            Euler 351 answer with no difficulty switched off.
off: (none)
stance: open
merge: ladder exhausted once this settles -- every difficulty has been turned
       back on and the goal is reached.
```
