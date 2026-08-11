# Fold: cycle-type / fixed-point summation machinery

Tools for the conjugation-class (cycle-type) sums behind A_n, B_n, and the order-domain weights n!/ord(π). Supporting routes, not solutions.

- [[ford_cycle_type_toolkit]] (Ford, Discrete Analysis 2022:9 / 2104.12019): exact factorial moments E[∏(C_k)_{r_k}]=∏k^{−r_k} for Σkr_k≤n; Poisson(1) fixed points with rates; sieve/CLT — the summation engine and its order-literature map. L0 `ford_cycle_type_toolkit.full.md`.
- [[nathanson_fixed_points_powers]] (2206.04021): F(σ^ℓ)=Σ_{k|ℓ} k·C(k); Möbius inversion recovers cycle counts from fixed points of powers — cross-check for the a_1,a_2 sums. L0 `nathanson_fixed_points_powers.full.md`.
- [[leanos_mth_roots_of_permutations]] (1005.1531): exact m-th-root counts by cycle type; NOT directly usable (root counts don't feed the intra-subgroup rank sum). L0 `leanos_mth_roots_of_permutations.full.md`.
- [[hultman_products_random_permutations]] (1301.0430): irreducible-character method for expected stats on products of class-distributed perms; covers independent products, not {π^i}. L0 `hultman_products_random_permutations.full.md`.

<!-- brief -->
Established: exact factorial moments of cycle counts; fixed points of powers ↔ cycle counts via Möbius; m-th-root counts; character method for products. All are machinery for the cycle-type sums, none computes the rank-sum over {π^i}.
