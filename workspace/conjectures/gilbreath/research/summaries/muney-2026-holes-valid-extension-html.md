# Muney 2026 — Holes in Valid-Extension Sets of Finite Gilbreath Sequences

**Full text:** `research/sources/muney-2026-holes-valid-extension-html.full.md` [[muney-2026-holes-valid-extension-html.full]]
**Source:** arXiv:2606.23721v2 [math.CO], 16 Jul 2026, Leila Muney, 36pp.

## What it establishes (the finite LOCAL extension problem)

For a Gilbreath sequence S=(s_1..s_n), s_1=2, s_2=3, strictly increasing, the **valid-extension set** K_S = {k∈ℤ : (S,k) is Gilbreath}. The right anti-diagonal e_i = s_{n−i}^i (i=1..n−1); e_{n−1}=1 and e_1..e_{n−2} are even; A(S)=Σe_i.

- **Proposition 2 (membership criterion).** k∈K_S ⟺ F_S(|k−s_n|)=1, where F_S(d)=||…||d−e_1|−e_2|…−e_{n−1}| is the ordered composition of folding maps x↦|x−e_i|. Equivalently the valid-distance set D_S = F_S^{-1}({1}).
- **Corollary 3 (candidate bound).** K_S ⊆ C_S = {k : |k−s_n| ≤ A(S)+1, k≡s_n mod 2}; |C_S|=A(S)+2.
- **Theorem 20 (interval-completeness criterion — the main theorem).** K_S = C_S ⟺ e_i ≤ 1+Σ_{j>i} e_j for every 1≤i≤n−2. This is an **order-sensitive analogue of Brown's classical subset-sum completeness criterion**; the order is forced by the nested absolute-value recurrence.
- **Theorem 24 (first hole).** For n≤4 all S∈𝒢_n are interval-complete. Smallest failure: n=5, unique S=(2,3,5,9,15), H_S=C_S∖K_S={15} (single hole). Reverse tree: D_S={2,4,6,8,10}.
- **Theorem 25 (min width).** min_{S∈𝒢_n}|K_S|=5 for all n≥3, uniquely at L_n=(2,3,5,…,2n−1), anti-diagonal (2,0,…,0,1).
- **Theorem 29.** Doubling U_n=(2,3,5,9,17,…,2^{n−1}+1): |K_{U_n}|=2^{n−1}+1; conjectured max (verified n≤10).
- **Theorem 35.** Family V_n: |K_{V_n}|=5·2^{n−4}, #components=2^{n−4}, defect h=3·2^{n−4}−2n+5 — valid-extension sets can have exponentially many parity-lattice components.
- **Proposition 18 (reverse-tree algorithm).** Exact O(*) algorithm computing K_S from e_i; runs the preimage step P_e(T)={e+t}∪{e−t:e≥t} backwards from {1}.
- **Gatti [11] correction.** The signed-sum/unfolding characterization (that K_S always fills the parity interval) is FALSE: signs aren't independent. Example 10: S=(2,3,5,9,17,19) has S_±=C_S but K_S=C_S∖{17,21}.

## Hypotheses held here

Yes for the finite theory (verified by the included reproducible code and enumeration through n=11, N_11=17,535,396 matching OEIS A080839). It does NOT address GC directly — it is the local extension problem of a fixed finite prefix, not the infinite leading-entry claim.

## Bearing on this run — the key new sourcing

Muney's theorem governs the **full valid-extension set** K_S — the set of ALL integers that can be appended while keeping every row's leading entry 1. That set is governed by the whole ordered right anti-diagonal via the folding map F_S; it cannot be read off a single local row quantity.

**Important distinction (do not over-claim):** this is a different question from the run's *block-regeneration criterion*. The run's own corrected computation (`check_regenerate_lemma.notes.md`, depth 1000) established that **block regeneration** b_{k+1} ≥ b_k IS a single-row local property — it holds iff (A_k[b_k]==2 and A_k[b_k+1]==4), zero failures over 998 transitions (the earlier "refutation" was an off-by-one indexing bug and has been withdrawn). There is **no contradiction** between the two: which specific next value is allowed by the full extension set is a global question (Muney), but whether the leading {0,2} block *grows when a particular next value is chosen* can still be a local law (the run's criterion). Muney's Theorem 20 (interval-completeness criterion) and the reverse-tree algorithm are structural tools for the global question; the run's local criterion is the empirically-checked law for the growth question.

## Claims

```claim
id: valid-extension-nonlocal
statement: The valid-extension set K_S and the interval-completeness condition K_S=C_S are governed by the whole ordered right anti-diagonal via the folding map F_S: k∈K_S ⟺ F_S(|k−s_n|)=1, and K_S=C_S ⟺ e_i≤1+Σ_{j>i}e_j (1≤i≤n−2) — an order-sensitive analogue of Brown's completeness criterion.
hypotheses: S∈𝒢_n (2,3-start, strictly increasing, Gilbreath); e_i=s_{n−i}^i anti-diagonal.
holds-here: yes (finite theory; code reproduces enumeration through n=11).
status: proved in source (elementary + Brown's criterion); first hole n=5 (2,3,5,9,15)
bearing: the full valid-extension set is a global (whole-anti-diagonal) object — orthogonal to, and NOT contradicting, the run's local block-regeneration criterion (edge-2/intruder-4, checked depth 1000). Supplies the correct global object if the extension-set route is pursued.
anchor: research/sources/muney-2026-holes-valid-extension-html.full.md
answers: what-structure-governs-the-valid-extension-set
```
