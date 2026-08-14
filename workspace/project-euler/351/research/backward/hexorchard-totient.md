# Backward skeleton — PE 351 hexagonal orchard

The goal reduces to one structural fact (the visibility formula) and one
numerical evaluation (the summatory totient at the bound). Everything else is
arithmetic that the `implies` line carries.

```skeleton
goal: Determine H(100000000) exactly, via the closed form
      H(n) = 3n^2 + 3n - 6*Phi(n),  Phi(n) = sum_{k=1..n} phi(k),
      evaluated at n = 10^8.
implies: Lemma G1 fixes H(n) = 3n^2 + 3n - 6*Phi(n) for every n >= 1, so the
      only unknown at n = 10^8 is Phi(10^8). Lemma G2 supplies the exact integer
      Phi(10^8) = V by an established algorithm. Substituting gives the single
      exact-integer evaluation H(10^8) = 3*10^8*(10^8 + 1) - 6V. Lemma G3
      re-establishes V and the final value by a second, independent route, so
      the substitution's output is the answer and not an implementation error.
status: sketched
rests-on: none (research/CLAIMS.md is empty; no claim in the ledger covers this)
```

```gap
id: G-hexorchard-visibility
lemma: For every n >= 1, the hexagonal orchard of order n contains
       3n^2 + 3n + 1 lattice points, of which exactly 1 + 6*Phi(n),
       Phi(n) = sum_{k=1..n} phi(k), are visible from the centre; hence
       H(n) = 3n^2 + 3n - 6*Phi(n) = 6 * sum_{k=1..n} (k - phi(k)).
status: open
next: Write the axial-coordinate bijection: the six open 60-degree sectors have
      ring-k points {(a,b) : a,b >= 1, a+b = k}, and (a,b) is visible from the
      centre iff gcd(a,b) = 1, giving sum_{k=2..n} phi(k) visible points per
      sector; the six boundary axes contribute n visible points each and the
      centre contributes 1, so visible = 1 + 6*(n + sum_{k=2..n} phi(k))
      = 1 + 6*Phi(n). Total points = 1 + 6*sum_{k=1..n} k = 3n^2 + 3n + 1.
      tool_builder: confirm the resulting formula against code/brute.py for
      n <= 30 and against the statement's oracle H(5)=30, H(10)=138,
      H(1000)=1177848.
```

```gap
id: G-summatory-totient-value
lemma: Phi(10^8) = sum_{k=1}^{10^8} phi(k) has an exact integer value V,
       computable by an established algorithm: the Euler-totient sieve over
       k <= 10^8 (O(n log log n) time, O(n) 32-bit memory), or the sublinear
       recurrence Phi(n) = n(n+1)/2 - sum_{d=2..n} Phi(floor(n/d)) — a direct
       consequence of sum_{d|m} phi(d) = m — evaluated in O(n^{2/3}) time with
       memoisation at the floor(n/d) points.
status: open
next: tool_builder: implement one of these with exact integer arithmetic,
      output V, and assert it reproduces Phi(10) = 32 and Phi(1000) = 304192
      (equivalently H(10)=138 and H(1000)=1177848 via G1) before evaluating
      n = 10^8.
```

```gap
id: G-answer-verification
lemma: The value H(10^8) = 3*10^8*(10^8 + 1) - 6V produced from G1 and G2 is
       the true H(10^8): both the closed form and the computed V are
       independently confirmed, so no arithmetic, off-by-one, or
       implementation error survives.
status: open
next: tool_builder: run a second, independent computation of Phi(10^8) — a
      different algorithm from the one used for G2 (linear/interval sieve vs
      Dirichlet-hyperbola recursion) — and diff its V against the first; also
      diff code/solution.py against code/brute.py on every n the brute force
      can reach. Report which second route was used.
```
