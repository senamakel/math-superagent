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

The run had **empirically REFUTED** a candidate "regeneration is a single-row local property" lemma (check_regenerate_lemma). Muney now gives this a **proof-level foundation**: K_S is determined by the entire (length n−1) ordered anti-diagonal via the folding map — it cannot be read off a single local row quantity. This independently confirms the regeneration-thread conclusion that regeneration is genuinely non-local, and supplies the correct global object (the folding composition F_S and its fiber over 1) for a future regeneration argument. It also supplies an order-sensitive completeness criterion (Theorem 20) — a structural invariant the run's {0,2}-block-length track could potentially dualize.

## Claims

```claim
id: valid-extension-nonlocal
statement: The valid-extension set K_S and the interval-completeness condition K_S=C_S are governed by the whole ordered right anti-diagonal via the folding map F_S: k∈K_S ⟺ F_S(|k−s_n|)=1, and K_S=C_S ⟺ e_i≤1+Σ_{j>i}e_j (1≤i≤n−2) — an order-sensitive analogue of Brown's completeness criterion.
hypotheses: S∈𝒢_n (2,3-start, strictly increasing, Gilbreath); e_i=s_{n−i}^i anti-diagonal.
holds-here: yes (finite theory; code reproduces enumeration through n=11).
status: proved in source (elementary + Brown's criterion); first hole n=5 (2,3,5,9,15)
bearing: confirms and explains the run's empirical refutation that regeneration is single-row-local; gives the correct global object for a regeneration argument.
anchor: research/sources/muney-2026-holes-valid-extension-html.full.md
contradicts: nothing on disk; supports the thread's local-iff-refutation
answers: why-is-regeneration-nonlocal
```
