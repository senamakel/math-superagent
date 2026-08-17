# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `ellis_gilmer_conjecture_refuted.lean` | Formalises Ellis's counterexample (arXiv:2211.12401) to Gilmer's Conjecture 1 as a decomposition. Kernel-proven core: the n=2 distribution p(∅)=p({1,2})=x, p({1})=p({2})=1/2−x has marginal p({i})+p({1,2})=1/2 for both elements (marginal_1_half, marginal_2_half, boundary_distribution), and the Ellis rewrite quantity LHS(3/10) = (2/25)·ln(2/3) < 0 (lhs_eq_closed, closed_at_3_10, closed_neg, ellis_lhs_negative) — all verified with only propext/Classical.choice/Quot.sound. **DIRECTIVE 21:** two of the four sorry-blocked goals (gap_perturbed_strict, gilmer_refuted_boundary) are FALSE as stated — both ask for the entropy of p to be negative — and must be restated around the (1)-difference (LHS/closed), not around hsum. See task restate-false-lean-goals-ellis-gilmer and research/approaches/ellis-gilmer-decomposition.md. gap_union_weights and gap_entropy_rewrite are correctly stated and mechanical.
| `gnm_envelope.lean` | _(undescribed)_ |
| `yu_gamma_half_is_phi_over_2.lean` | Formalises the collapsed alpha=0 extremal value of Yu's Gamma_hat(1/2) as the clean constant phi/2 = (1+sqrt5)/4 = cos(pi/5): defines binary entropy h, the collapsed atom a=(3-sqrt5)/2, its weight w1=1-a/2, and proves the collapse identities 2a-a^2=1-a (turning h(1-a) into h(a)), w1=(1+sqrt5)/4=goldenRatio/2=cos(pi/5), and that the ratio numerator w1^2 h(2a-a^2) = w1 * denominator (w1 h(a)). Kernel-verified with only propext/Classical.choice/Quot.sound. |
