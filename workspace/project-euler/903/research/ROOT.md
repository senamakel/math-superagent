# research — what this now establishes

PE 903 reduces exactly (verify_red.py) to Q(n)=(n!)²+A_n(n!−1)+(B_n/2)T(n),
T(n)=Σ_{m=1}^{n-1}m(m−1)m!, from proved gap-affine pair-inversion counts
f_n(k)=A_n+(k−1)B_n. All sources are routes to A_n,B_n; NONE computes the
rank-sum over the cyclic subgroup {π^i} (the novel core), and OEIS confirms
A_n,B_n,Q(n) are uncatalogued. L0.0 sealed by [[L1.2/L0.0]] (Cambie–Yan
Thm 1.1/1.2 n≥2k+1, Archer–Geary, Campion-Loth Lemma 4.7 gap-affine pair
inversion, factoradic rank, Ford's factorial-moment toolkit, homomesy, Gaetz–Ryba
dead). L0.1 sealed by [[L1.2/L0.1]] (Hultman products characters — negative for
the {π^i} sum because rank is not a class function; Leaños m-th roots — preimage
counts, not the orbit sum; Legendre cyclic-shift rank code — rank-in-a-cyclic-orbit
solved only for rotation; Zawiślak Lehmer-digit independence; Nathanson
fixed-points-of-powers↔C(k) Möbius; Pinsky EJC fixed-point-conditioned per-gap
inversion formula, the A_n,B_n mechanism). **L0.2 sealed by [[L1.2/L0.2]]**
(power-side cycle structure of π^k: τ(k) fixed points, gcd(i,k)-splitting, fixed-point
EGF exp(Σ_{i|k}(y^i−1)/i) — Courtois–Bard–Ault; the SECOND independent proof of the
gap-affine pair-inversion mechanism, Pinsky–Schickentanz Ewens Thm 1a/Prop 10a, uniform
θ=1 case being what Q(n) sums over; Sack–Úlfarsson k-step gap-resolved inversion
distribution H_{n,k}; Stong average-order law log μ_n=C√(n/log n) bounding the n!/ord
weights. All mechanism/route; none computes the {π^i} sum). Library = [[rank_lehmer]] +
[[mechanism_pair_inversions]] (core mechanism, two proofs: Campion-Loth + Ewens) +
[[order_random_permutation]] (weights) + [[cycle_type_toolkit]] (summation engine) +
small-exponent [[cambie_yan_descents_inversions_powers]] +
[[sack_ulfarsson_refined_inversion_statistics]] (per-gap inversion machinery) +
[[homomesies_permutations]] (framework) + power-side structure now under [[L1.2/L0.2]].
[[legendre_number_system_cyclic_shift]] shares the "rank inside a cyclic-orbit" shape
but for rotation, not powers — related framework only. See [[report_literature_ranks_powers]]
(clean negative) and [[report_A_n_B_n_closed_forms_sources]] (derivation route).
