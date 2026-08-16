# Chellali, "On the number of real polynomials of the Casas-Alvero type" (2015)

Source: https://doi.org/10.1016/j.jtusci.2015.02.008 — Journal of Taibah University for Science, 2015. Full text: `research/sources/chellali2015_real-casas-alvero-count.full.md`.

## What it establishes

Works entirely over **K = ℝ with P split over ℝ** (so every derivative P^(j) is also real-split). It does **not** exhibit real CA-polynomials — CA is true for real-rooted polynomials (held: `real-rooted-and-convex-hull`); rather it counts the *combinatorial zero-distribution data* a hypothetical real CA counterexample of the reduced normal form

```
P = X² (X − x₃) ⋯ (X − x_n),  0 < x₃ < ⋯ < x_n
```

would force, and bounds how many such structures there are.

**Main theorem (Thm 2.3):** the number uₙ of "Casas graphs" of size n satisfies

```
(n − 4)! ≤ uₙ ≤ c (n − 3)^{n−2},   c := 2e^{−1} (∏_{n=2}^{∞} e^{−1}(Σ_{k=0}^{n} 1/k!))² = 0.59373381…
```

- A **Casas–Rolle graph** (Def 2.1) is the interleaving of the roots of P and its derivatives required by **Rolle's theorem**: a shared-root assignment f : {2,4,…,n−1} → {3,…,n−1} (even floors j≥2 — the odd floor j=1 carries no constraint) picking which root of the j-th derivative coincides with a root x_{f(j)}^0 of P, subject to the interlacing x_i^j < x_i^{j+1} < x_{i+1}^j. Two graphs are equivalent iff same size and same map f; a Casas graph is the equivalence class.
- The count is finite and the map f is the only essential datum ("regardless of values of x_ij, the only significant function is f").
- **Lemma 2.6** — the structural heart: for each k, the number |f^{-1}(k)| of derivatives sharing the root x_k^0 satisfies |f^{-1}(k)| ≤ min(k−1, n−k). (A single root shared at floors j_1<…<j_t forces strictly nested semi-progeny positions 1≤i_t<…<i_1<m with m<i_1+j_1<…<i_t+j_t≤n, so t≤m−1 and t≤n−m.) This is the bound the upper estimate is built on.
- Rolle's theorem alone settles CA for **n ≤ 4** but not n ≥ 5; the size-5 graph in §1 cannot be realised by an actual polynomial (by Graf-von-Bothmer et al's degree bound such polynomials do not exist).
- §3 gives an explicit algorithm for computing uₙ; §4 shows how the Rolle-graph method reproves and mildly improves some prior results ([2]–[4], i.e. Draisma–de Jong, Yakubovich).

## Bearing on this problem

- It is a **counting/structural constraint on a real minimal counterexample's zero-distribution**, complementary to the analytic constraints (≥5 distinct roots, convex-hull/Gauss–Lucas) already held. The graph data is char-0 and Rolle-based, so it is *not* the char-p break — it is a geometric/combinatorial obstruction specific to real roots that cannot transfer to F_p.
- The normal form P = X²(X−x₃)⋯(X−x_n) is exactly the pinned form (shared root of f' = x²-style double root at 0) the run's scheme method normalises to; the count shows the real combinatorial search space has size between (n−4)! and c(n−3)^{n−2} — far smaller than the full scenario space, which is why real-rooted CA is provable while the general case is not.
- Status: **sourced/asserted** (I read Thm 2.3, Lemma 2.6 and the estimates; the numeric constant 0.5937… and the factorial-count algebra are taken on the paper's word, as is the algorithm of §3).
