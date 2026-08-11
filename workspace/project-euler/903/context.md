# Shared context

Run solves PE 903: Q(n) = Σ_pi Σ_{i=1}^{n!} rank(pi^i) mod (10^9+7). memory.md and
verify_red.py reduce it to Q(n) = (n!)^2 + A_n·(n!−1) + (B_n/2)·T(n), where
f_n(k)=A_n+(k−1)B_n is the exact arithmetic gap function of pair-inversion counts
and T(n)=Σ_{m=1}^{n-1} m(m−1)m!. Only inputs still missing: closed forms for
A_n, B_n. Everything below feeds that hunt.

## Established

- **Gap-affine pair-inversion probabilities are proved, two independent ways** —
  the mechanism behind f_n(k)=A_n+(k−1)B_n.
  - [[conjugacy_class_statistics_body]] (Campion-Loth et al.): per-cycle-type
    inversion probability Pr_λ[I_{i,j}=1] is translation-invariant and affine in
    the gap j−i, depending only on n, a_1=#fixed, a_2=#2-cycles (Lemma 4.7);
    weighted-inversion first moments depend only on n,a_1,a_2 (Thm 4.8).
  - [[pinsky_schickentanz_ewens_html]] (Pinsky & Schickentanz): exact pair-
    inversion probabilities under Ewens sampling (uniform=θ=1), unconditioned
    (Thm 1a, affine in gap) and conditioned on m fixed points (Prop 10a, exact
    per-gap per-m; fixing probs Prop 4). θ=0 cyclic case:
    1/2+(j−i−1)/[(n−1)(n−2)]. Concrete summation route to A_n, B_n.
- **Expected descents & inversions in pi^k have closed forms** (fixed k, n≥2k+1)
  via divisor functions — [[cambie_yan_html]] (Cambie-Yan; confirms Archer-Geary).
  Small-exponent regime only.
- **Character-theoretic machine for expected stats on products of class-distributed
  random perms** — [[hultman_products_random_permutations]]. Covers independent
  products, NOT the cyclic subgroup {pi^i} nor lexicographic rank.
- **Fixed points of powers determine the conjugacy class** — [[nathanson_fixed_points_powers]]:
  F(σ^ℓ)=Σ_{k|ℓ}k·C(k), Möbius inversion recovers cycle counts. Character-free
  cross-check for the (a_1,a_2) sums behind A_n, B_n.
- **Lehmer/factorial code gives lexicographic rank** — [[factorial_number_system_wiki]].
- **NEW: exact fixed-point-conditioned per-pair inversion probability at finite n**
  — [[pinsky_inversion_fixed_points]] (Pinsky, EJC 33(2) P2.36, DOI 10.37236/14250):
  exact formula for P_n^(k)(σ_i^{-1}<σ_j^{-1}) and the expected inversion count
  under uniform measure conditioned on exactly k fixed points, plus derangement
  (k=0: n(n−1)/4+n/6+1/12+o(1)) and k≥1 asymptotics. Together with
  [[pinsky_schickentanz_ewens_html]] Prop 10a this is a concrete summation route
  to A_n, B_n: average the per-gap inversion probability over the fixed-point
  count distribution of a uniform permutation. Closes the gap between the two
  already-proved mechanisms at exact finite n (not just asymptotically).
- **Negative OEIS**: A_n, B_n/(n−1)!, Q(n), probes uncatalogued — [[oeis_Aseq]],
  [[oeis_Qseq]], [[oeis_Bdiv]].
- **NEW: canonical cycle-type summation machinery** — [[ford_cycle_type_toolkit]]
  (Ford, Discrete Analysis 2022:9): exact factorial moments E[∏(C_k)_{r_k}] = ∏ k^{−r_k}
  for Σ k r_k ≤ n, fixed-point count ~ Poisson(1) with explicit error, sieve/CLT for
  cycle counts. This is the engine for evaluating the cycle-type sums (A_n, B_n)
  behind both already-proved gap-affine mechanisms, and its bibliography maps the
  order-of-permutation literature that governs the n!/ord(π) weights in brute2.

## Open core (no source addresses it)

No closed form for A_n, B_n; summing Lehmer/factoradic ranks over the cyclic
subgroup {pi^i} of a single π — the genuinely novel statistic — is covered by no
source located. All above are mechanism/route, not the Q(10^6) computation.
