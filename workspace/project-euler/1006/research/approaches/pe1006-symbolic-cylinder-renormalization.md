# Approach: symbolic-dynamics / cylinder-set renormalisation for G4

```approach
id: pe1006-symbolic-cylinder-renormalization
idea: Sum over all length-k factors of the square of the decimal morphism by cylinder-set integration over the irrational rotation: write V_k(x)=Σ_j 10^{k-1-j} 1_{I_j}(x), so Ψ(k) is the exact second moment over the k+1 factor atoms; seek a Fibonacci continued-fraction renormalisation whose transfer operator keeps the tensor square V_k⊗V_k in a k-independent finite-dimensional module.
mechanism: Under continued-fraction/Rauzy–Veech induction the cylinder partition renormalises. If the base-10 weighted observable and its square stayed in a fixed-D module, Ψ would be a renormalisation fixed-point equation in O(log k).
status: refuted
precedent: https://arxiv.org/abs/math/0106217 (Berstel–Vuillon); https://doi.org/10.24033/asens.2257 (Leplaideur–Bruin); https://doi.org/10.5169/seals-63900 (Alessandri–Berthé); https://arxiv.org/abs/1807.11273 (Weiss); https://arxiv.org/abs/1210.4083 (Alkauskas)
killed-by: V_k² = Σ_{j,l} 10^{2k-2-j-l} 1_{I_j∩I_l} is a two-index family of translated intersection indicators. Standard transfer-operator/RPF theory (sources above) gives spectral/quasi-compact results for expanding maps and regular potentials, but no theorem that this observable's tensor square lies in a fixed-D module, nor that the exact sum over all factor atoms is O(log k). The boundary-sensitive joint-intercept coupling is the same obstruction already verified at k=1 (single-intercept failure) and k=2 (additive-summary collision on 010/101): a state collapsing intersections by displacement loses boundary placement; a state retaining placement has rank growing with k. Grouping only by l−j is valid only at k=F_n−1 (Toeplitz special case). So the route is an exact reformulation, not a closed method; the decisive finite-closure lemma is neither proved nor supplied by the literature.
```

Full reasoning, the exact cylinder formula, the module-rank obstruction, and the oracle status are in `research/approaches/pe1006-symbolic-cylinder-renormalization.md`.
