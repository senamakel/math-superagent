# Ladder: maximum internal degree at one vertex past half

```ladder
goal: Determine the growth rate of f(n) = min { D(S) : S ⊆ {0,1}^n, |S| = 2^(n-1)+1 }, where D(S) is the maximum internal degree of the induced subgraph Q_n[S]. Known: c·log n ≤ f(n) ≤ sqrt(n), gap open thirty years.
difficulties: unbounded-n, universal-S, exact-half-plus-one, maximum-not-average, sqrt-mechanism
status: open
```

Climb direction, bottom to top: R-instance → R-small-n → R-parity-plus-one → R-goal.
R-average, R-density, R-sqrt-construction are the "one difficulty switched off"
diagnostics, to be settled in parallel; each one isolates where a known method dies.

```rung
id: R-instance
statement: For n=3 and the explicit S = {000, 011, 101, 110} ∪ {001} (size 5 = 2^2+1), verify the checker: degree_profile(S) = (0:1, 1:3, 3:1) and D(S) = 3.
off: unbounded-n, universal-S, exact-half-plus-one, maximum-not-average, sqrt-mechanism
stance: open
merge: Turning universal-S, maximum-not-average and exact-half-plus-one back on jointly gives R-small-n — the three cannot be separated without the rung collapsing to a triviality, because they jointly define f(n). First move: one degree_profile call on this S settles R-instance; then hand the (n,d) decision encoding to sat_solver.
```

```rung
id: R-small-n
statement: Determine f(n) exactly for n = 1,2,3,4 (exhaustive), and extend to n = 5,6 by the SAT/ILP decision "∃S ⊆ {0,1}^n, |S| = 2^(n-1)+1, D(S) ≤ d?"; the minimum is the least d for which it is satisfiable.
off: unbounded-n, sqrt-mechanism
stance: open
merge: Turning unbounded-n back on while keeping universal-S off — via the restricted parity family — gives R-parity-plus-one. First move: encode as ILP with variables x_v ∈ {0,1}, Σ_v x_v = 2^(n-1)+1, and Σ_{u~v} x_u ≤ d + n(1−x_v) for every v; binary-search d, starting at n=4. Check the complement-domination characterization: D(S) ≤ d iff every vertex has ≥ n−d neighbours in T = {0,1}^n ∖ S. Hand values to confirm, not assume: f(1)=1, f(2)=2, f(3)=2 — f(3)≥2 by counting (a 5-set S with D≤1 would need 2·5=10 edges into its 3-vertex complement, which has only 9 incident edges), and f(3)≤2 by T={000,111,001} giving the 5-set {010,011,100,101,110} with D=2. f(4) is left to the solver.
```

```rung
id: R-parity-plus-one
statement: For every n ≥ 1 and the family F = { S = {x : |x| even} ∪ {v} : v has odd weight }, show D(S) = n exactly: the even-weight set is independent, and an odd-weight vertex has all n of its neighbours even, so the added vertex attains degree n.
off: universal-S, sqrt-mechanism
stance: open
merge: Turning universal-S back on is the step that gets hard — it is the goal. The finding R-parity-plus-one banks is that the naive one-extra-vertex set is as bad as possible (D = n), so any approach to the sqrt bound must leave parity halves entirely and engage arbitrary S. First move: the two-line parity argument (neighbours of an odd vertex flip one bit, hence have even weight); nothing further is blocked here, but this rung is deliberately a dead end as an upper-bound construction.
```

```rung
id: R-goal
statement: Determine the growth rate of f(n) = min { D(S) : S ⊆ {0,1}^n, |S| = 2^(n-1)+1 }; close or narrow the gap c·log n ≤ f(n) ≤ sqrt(n).
off: (none)
stance: open
merge: Top of the ladder, reached by turning universal-S back on at unbounded n; no further merge. Closing it needs a quantity that is a maximum by construction, because R-average shows averages collapse to ~0 at this size while R-density shows edge-counting degenerates exactly at density 1/2.
```

```rung
id: R-average
statement: Let g(n) = min over |S| = 2^(n-1)+1 of the average internal degree 2|E(S)|/|S|. Show 2/(2^(n-1)+1) ≤ g(n) ≤ 2n/(2^(n-1)+1), hence g(n) → 0, while f(n) ≥ c·log n: the average version collapses while the maximum version does not.
off: maximum-not-average, sqrt-mechanism
stance: open
merge: Turning maximum-not-average back on is the goal. The growth statement settles from the sandwich: the lower bound holds because the independence number of Q_n is 2^(n-1) (Kőnig on the perfect matching), so any (2^(n-1)+1)-set has an edge; the upper bound is the parity class plus one vertex, contributing 2n to the degree sum. Pinning the exact minimum needs the classification of maximum independent sets of Q_n, which is an open gap here — request it only if the forward loop wants the constant, not the growth.
```

```rung
id: R-density
statement: For fixed α ∈ (1/2, 1], let F_α(n) = min over |S| = α·2^n of D(S). Show (2α−1)/α · n ≤ F_α(n) ≤ n, hence F_α(n) = Θ(n); the lower bound is the plain edge-counting argument, and it degenerates to 0 exactly as α → 1/2.
off: exact-half-plus-one, sqrt-mechanism
stance: open
merge: Turning exact-half-plus-one back on (α ↓ 1/2 + 2^(−(n−1))) collapses the bound (2α−1)/α · n to 0 — this is the precise point where the averaging method dies, and it is the finding R-density banks. First move: verify the lower bound by the computation D(S) = n − min_{v∈S}|N(v)∩T| with T = complement, min ≤ |T|n/|S| = (1−α)n/α; check tightness at α=3/4 against the majority-set construction.
```

```rung
id: R-sqrt-construction
statement: Rebuild the known upper-bound construction: for n a perfect square, exhibit an explicit S, |S| = 2^(n-1)+1, with D(S) ≤ sqrt(n); verify it by degree_profile for the smallest perfect-square case n=4 (expect D ≤ 2).
off: sqrt-mechanism
stance: open
merge: Turning sqrt-mechanism back on is the goal: matching the sqrt construction by a lower bound is exactly what no known quantity does, and the construction is where the sqrt arises (a recursive/product, i.e. quadratic, relation — counting alone produces only linear and logarithmic scales). First move: re-derive the recursive block construction and measure its degree_profile at n=4 before trusting its asymptotics.
```
