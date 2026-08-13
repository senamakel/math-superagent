# Lagarias: Ternary expansions of powers of 2 (J. London Math. Soc., 2009)

**Source:** arXiv:math/0512006 (v4), published J. London Math. Soc. (2) 79 (2009) 562–588, doi:10.1112/jlms/jdn080. Full text at `research/sources/lagarias-ar5iv-full.full.md`.

## What it establishes

1. **Narkiewicz's bound, exactly.** N(1) = #{n ≤ X : (2^n)_3 omits digit 2}. Narkiewicz (1980): `N_1(X) ≤ 1.62 X^{α_0}` with `α_0 = log_3 2 ≈ 0.63092`. The proof: 2 is a primitive root mod 3^k for every k ≥ 1 (order 2·3^(k-1)); among the 2·3^(k-1) power residues mod 3^k, exactly 2^(k-1) have a 3-adic expansion omitting digit 2 in the first k digits. Choosing k with 2·3^(k-2) < X ≤ 2·3^(k-1) gives N ≤ 2^k ≤ 2X^{α_0}; the 1.62 constant in the published version comes from the same count with the sharper constant.
2. **Generalization to 3-adic dynamics (Theorem 1.4):** for every nonzero λ ∈ ℤ_3, # {n ≤ X : (λ·2^n)_3 omits digit 2} ≤ 2·X^{α_0}, uniformly in λ, X ≥ 2. This is precisely the sieve-set statement: A_k ⊆ Z/(2·3^(k-1))Z has at most 2^k elements, and this is what makes |A_k| ≤ 2^(k-1) roughly; it grows like 2^k, NOT tending to 0.
3. **Hausdorff dimension of exceptional sets:** dim_H E^(1)(ℤ_3) = log_3 2; (1/2)log_3 2 ≤ dim_H E^(2)(ℤ_3) ≤ 1/2; (1/6)log_3 2 ≤ dim_H E^(3)(ℤ_3). Conjectures A, B: real and 3-adic exceptional sets have Hausdorff dimension 0. Erdős's conjecture is equivalent to 1 ∉ E(ℝ+) and to 1 ∉ E(ℤ_3).
4. **Truncated real dynamics (Theorem 1.1):** for every λ>0, #{n≤X : (⌊λ2^n⌋)_3 omits digit 2} ≤ 25 X^(36/37) ≈ 25 X^0.9725, using logarithmic-density of rotations by α_0 and Baker/Rhin lower bounds for |α_0 - p/q|.
5. **Why both methods stall:** the real method uses the ~log_3 X most significant digits; the 3-adic method uses the ~log_3 X least significant digits. Neither touches the middle of the expansion, which has α_0·n digits. Closing the gap to β < log_3 2 remains open and is posed explicitly as a challenge.

## Critical implication for this run

The naive count in GOAL.md (`|A_k| ≈ 2·3^(k-1)·(2/3)^k ≈ 2^k/3` grows) is exactly the Narkiewicz/Lagarias bound: sieve-set sizes grow like 2^k, so a transfer-operator/spectral-radius approach must show the *counting measure* on A_k concentrates or that the splitting rule has a contraction Narkiewicz's uniform bound misses. Lagarias's Theorem 1.4 is uniform in λ, and the three-witness structure (n=0,2,8 ↔ multipliers 1,4,256) used in his Theorem 1.5 lower bounds mirrors the run's witness check.

## Claims
```claim
id: LAG-1
statement: N_1(X) = #{n ≤ X : ternary of 2^n omits digit 2} satisfies N_1(X) ≤ 1.62 X^{α_0}, α_0 = log_3 2 ≈ 0.63092 (Narkiewicz 1980).
hypotheses: X ≥ 1 real/integer; digit 2 omitted from full ternary expansion (equivalently low ⌈log_3 X⌉ digits after sieve).
holds-here: yes — it is THE partial result this run would need to re-derive with an explicit constant.
status: asserted-by-source (theorem in Lagarias's paper; original in 1980 Narkiewicz note)
bearing: any claimed improvement must beat 1.62 X^{0.63092}.
anchor: research/sources/lagarias-ar5iv-full.full.md
```
```claim
id: LAG-2
statement: For every nonzero λ ∈ ℤ_3, #{n ≤ X : (λ2^n)_3 omits digit 2} ≤ 2 X^{α_0} for X ≥ 2.
hypotheses: λ ≠ 0 in 3-adic integers.
holds-here: yes; λ=1 is the Erdős case.
status: proved in paper (Theorem 1.4, self-contained)
bearing: bounds the sieve set A_k uniformly; |A_k| ≤ 2^(k-1), so no size-based argument can reach zero without new structure.
anchor: research/sources/lagarias-ar5iv-full.full.md
```
```claim
id: LAG-3
statement: dim_H E^(1)(ℤ_3) = log_3 2; (1/2)log_3 2 ≤ dim_H E^(2)(ℤ_3) ≤ 1/2; (1/6)log_3 2 ≤ dim_H E^(3)(ℤ_3). Conjecture B: dim_H E(ℤ_3) = 0.
hypotheses: ℤ_3 with its 3-adic metric; E^(k) = {λ : at least k of the λ2^n omit digit 2}.
holds-here: witnesses 1, 4, 256 = 2^0, 2^2, 2^8 are exactly what gives the E^(1..3) lower bounds — an explicit reminder the witnesses are structural, not accidental.
status: proved for E^(1),(2),(3) bounds in paper; Conjecture B open.
bearing: ties witness structure to Hausdorff dimension of exceptional λ-sets.
anchor: research/sources/lagarias-ar5iv-full.full.md
```
```claim
id: LAG-4
statement: The real truncated method uses only the top ~log_3 X digits and the 3-adic method only the bottom ~log_3 X digits of (2^n)_3; neither exploits the middle digits, and combining them is open.
hypotheses: none.
holds-here: yes — it is the reason Narkiewicz's bound has not been improved in 40+ years.
status: asserted in the paper's summary (Section 1.6), open challenge.
bearing: a genuine partial result could come from controlling a *block* of middle digits.
anchor: research/sources/lagarias-ar5iv-full.full.md
```