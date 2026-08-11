# Shared context

PE 903: Q(n)=Σ_π Σ_{i=1}^{n!} rank(π^i) mod (10^9+7), rank=lex position. Reduced exactly
(verify_red.py) → Q(n)=(n!)²+A_n(n!−1)+(B_n/2)T(n), T(n)=Σ_{m=1}^{n-1}m(m−1)m!, from the
proved gap-affine pair-inversion counts f_n(k)=A_n+(k−1)B_n. Missing: closed forms A_n,B_n.

Established (all mechanism/route; none solves rank-sum over {π^i}):
- [[conjugacy_class_statistics_body]] + [[pinsky_schickentanz_ewens_html]]: pair-inversion
  probability affine in the gap, depending only on #fixed,#2-cycles (two proofs); Ewens
  Thm 1a + fixed-point-conditioned Prop 10a = concrete summation route to A_n,B_n.
- [[pinsky_inversion_fixed_points]]: exact finite-n fixed-point-conditioned pair-inversion
  formulas.
- [[ford_cycle_type_toolkit]]: factorial moments E∏(C_k)_{r_k}=∏k^{−r_k}; the engine for the
  cycle-type sums behind A_n,B_n; bibliography maps the order literature.
- [[cambie_yan_html]]: descents/inversions of π^k closed forms, small-exponent regime (n≥2k+1).
- [[nathanson_fixed_points_powers]]: powers' fixed points ↔ cycle counts (Möbius inversion).
- [[hultman_products_random_permutations]]: characters for products of class-distributed perms,
  not the cyclic subgroup {π^i}.
- [[stong_average_order_permutation]]: average-order law governing the n!/ord(π) weights.
- [[factorial_number_system_wiki]]: Lehmer code = lex rank. [[oeis_Aseq]]/[[oeis_Bdiv]]/[[oeis_Qseq]]: A_n,B_n,Q(n) uncatalogued.
- [[sack_ulfarsson_refined_inversion_statistics]]: gap-resolved inversion statistics — closed per-gap k-step inversion distribution H_{n,k} via Eulerian polynomials (Thm 4.4), dot-product identity 1·π=n(n+1)(2n+1)/6−invsum (Thm 2.5), zone-crossing recurrence. New machinery for the per-gap counts f_n(k); single-permutation only, not {π^i}.
- [[homomesies_permutations]] (Elder et al, 2206.13409): NEW — the homomesy framework. A statistic is homomesic under a map when its average is constant on every orbit, so an orbit-average equals the global average. Lehmer-code rotation: every orbit has size lcm(1..n) (Thm 4.8) and 45 inversion-linked stats are homomesic there (Thm 4.7). This is the natural phrasing of the open 'average rank over the cyclic subgroup {π^i}' question, but the map is rotation (not permutation-power/{π^i}) and rank itself is not homomesic there. So it sharpens but does not close the core.

- [[legendre_number_system_cyclic_shift]] (Legendre, arXiv:1007.2870): NEW — a number system
  ranking/unranking permutations inside a cyclic-shift orbit (size n), the closest located
  treatment of "rank within one map-orbit," the shape of the open core. Limitation: the map is
  one-line word rotation (n-cycle on positions), not the permutation-power subgroup {π^i}
  (order d=lcm of cycle lengths); supplies no closed form for A_n,B_n. Related framework only.

Open core: no closed form for A_n,B_n; summing Lehmer ranks over the cyclic subgroup {π^i} is
covered by no source located — all above are routes, not the Q(10^6) computation. The library
now additionally establishes that "ranking permutations inside a cyclic-orbit" is a studied,
solved-for-rotation framework (Legendre), but that the power-subgroup variant central to PE 903
remains uncovered.
