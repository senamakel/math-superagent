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

Open core: no closed form for A_n,B_n; summing Lehmer ranks over the cyclic subgroup {π^i} is
covered by no source located — all above are routes, not the Q(10^6) computation.
