# Ladder: the max-degree-of-half-plus-one problem on the cube

```ladder
goal: Determine the growth rate of f(n) = min{ D(S) : S ⊆ {0,1}^n, |S| = 2^{n-1}+1 }, where D(S) is the maximum internal degree of the induced subgraph Q_n[S]. Known: c·log n ≤ f(n) ≤ sqrt(n); the gap has not moved in thirty years.
difficulties: unbounded-n, adversarial-S, minimal-excess, max-vs-average, internal-only, minimax
status: open
```

- `unbounded-n` — the answer is an asymptotic growth rate; no finite value of f(n) can separate log from sqrt.
- `adversarial-S` — a lower bound must hold for *every* S of size 2^{n-1}+1, a doubly-exponential family the adversary picks after seeing the argument.
- `minimal-excess` — |S| = 2^{n-1}+1 is exactly one vertex past the maximum independent set, the weakest hypothesis that forces any internal degree at all.
- `max-vs-average` — D(S) is a maximum over vertices of internal degree; edge-counting yields only the average 2e(S)/|S|, and the single extra vertex gives ~0 edges.
- `internal-only` — D(S) counts neighbours inside S only; edges to the complement and the edge boundary are invisible to it, so isoperimetric boundary bounds do not reach D(S).
- `minimax` — f(n) = min_S max_v d_S(v); no known extremal quantity produces this maximum directly, which is the thirty-year obstruction.

```rung
id: R1-small-n-exact
statement: Establish f(n) exactly for n = 1,2,3,4 by exhaustive search over all S ⊆ {0,1}^n with |S| = 2^{n-1}+1, checked by an independent direct degree_profile checker; then push to n = 5,6 via the SAT/ILP decision problem "is there S with |S| = 2^{n-1}+1 and D(S) ≤ d?". Record the method and the runtime at the last n completed.
off: unbounded-n
stance: open
merge: These exact values are the falsification oracle every other rung is checked against. Turning unbounded-n back on is automatic and necessary: f(1..5) cannot distinguish c·log n from sqrt(n), so the next rung keeps S fixed and probes where the maximum degree actually comes from.
```

```rung
id: R2-parity-plus-one
statement: With E_n = {x ∈ {0,1}^n : |x| even}, a maximum independent set of size 2^{n-1}, and v any odd-weight vertex, D(E_n ∪ {v}) = n. Equivalently: the natural "independent set plus one vertex" candidate has maximum internal degree n, not ~sqrt(n).
off: adversarial-S
stance: open
merge: One attempt settles this by hand: every neighbour of v flips one bit, hence is even and lies in E_n, so d(v) = n. The lesson to bank: the extremal S must sacrifice independence to keep the maximum small. minimal-excess is already on here (the size is exact); the real next step is adversarial-S — find the best D over a structured class of S rather than one fixed S.
```

```rung
id: R3-average-collapses
statement: Define f_avg(n) = min over |S| = 2^{n-1}+1 of 2·e(S)/|S|, the average internal degree (e(S) = number of internal edges). Establish f_avg(n) ≤ n/2^{n-2} via E_n ∪ {v}; hence f_avg(n) → 0 while f(n) ≥ c·log n. Conclusion to bank: any argument that bounds only the number of internal edges cannot prove any lower bound f(n) ≥ g(n) with g(n) → ∞.
off: max-vs-average
stance: open
merge: This is the problem.md obstruction made quantitative. Turning max-vs-average back on is the open problem itself: a lower bound must come from a quantity that bounds the maximum directly, without passing through 2e(S)/|S|.
```

```rung
id: R4-hamming-ball
statement: Define f_ball(n) = min D(S) over S = {x : |x| ≤ k} ∪ {one vertex} with |S| = 2^{n-1}+1 (a Hamming ball plus one vertex). Establish its value in closed form or by a tiny computation; expect D = n (interior vertices already have full degree n).
off: adversarial-S
stance: open
merge: Balls are the wrong shape: interior vertices have degree n regardless. The extremal S must be spread across the cube, not a threshold/initial segment. Turning adversarial-S back on asks whether any S beats every ball — and the sqrt(n) construction is exactly such an S.
```

```rung
id: R5-level-union
statement: Define f_sym(n) = min D(S) over S that are unions of full Hamming levels (permutation-invariant S), |S| = 2^{n-1}+1. This is an (n+1)-variable 0-1 optimisation over level indicators a_k with D(S) = max_k [a_{k-1}·k + a_{k+1}·(n-k)]. Settle it for small n by a tiny ILP.
off: adversarial-S
stance: open
merge: The sqrt(n) construction is not level-symmetric, so this rung measures how much the unrestricted adversary buys. Turning adversarial-S back on is the whole difficulty — but with f_ball and f_sym banked, the run can say exactly where symmetry fails.
```

```rung
id: R6-sqrt-construction
statement: Rebuild the known recursive/product construction: for n a perfect square, produce an explicit S ⊆ {0,1}^n with |S| = 2^{n-1}+1 and D(S) = sqrt(n) (or state the constant actually achieved), and verify D(S) directly with the construction checker for the smallest applicable n.
off: adversarial-S
stance: open
merge: An upper bound is a witness, not a universal statement, so only one S is needed. Turning adversarial-S back on converts "there exists S with D(S) = sqrt(n)" into "every S has D(S) ≥ sqrt(n)" — that is the full lower-bound conjecture, not a rung.
```

```rung
id: R7-log-lower-bound
statement: Re-derive the known lower bound f(n) ≥ c·log n over all S (the induction/counting argument), with the constant c made explicit, and check c·log n ≤ f(n) against the exact values from R1.
off: minimax
stance: open
merge: This rung keeps adversarial-S, max-vs-average, and internal-only fully on; it is weaker only in settling for the log rate. Turning minimax back on is the thirty-year step: improving c·log n to omega(log n) needs a quantity that bounds the maximum directly, which the known argument does not provide.
```

```rung
id: R8-constant-excess
statement: For fixed δ > 0, determine g_δ(n) = min over |S| = (1/2 + δ)·2^n of D(S). Target: prove D(S) ≥ c(δ)·n for an explicit c(δ) > 0. Falsified if an explicit S with constant excess has D(S) = o(n).
off: minimal-excess
stance: open
merge: This is the positive-excess regime where a single extra vertex is replaced by a constant fraction of vertices; isoperimetric or boundary arguments may reach it where they fail at excess one. Turning minimal-excess back on (δ → 2^{-n}, exactly one vertex) is precisely where the known techniques are stuck, so a c(δ) that survives δ → 0 would be the whole result.
```

```rung
id: R9-obstruction-theorem
statement: Prove an obstruction theorem: every argument of a named class — edge-counting/averaging, edge-isoperimetry, vertex-isoperimetry, coordinate induction — outputs at best O(log n), by exhibiting why each bounds an average or total quantity and cannot produce sqrt(n). Minimum form: prove the averaging class (R3) is stuck, then extend to the others.
off: minimax
stance: open
merge: This is a GOAL-listed result and is weaker than the conjecture (it proves techniques fail, not that f(n) is larger). Turning minimax back on means replacing the obstruction with an actual maximum-producing quantity — finding one is the open problem.
```
