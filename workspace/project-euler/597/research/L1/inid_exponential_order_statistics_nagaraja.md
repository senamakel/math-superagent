# INID exponential order statistics — Nagaraja (Nevzorov/Tikhov antirank theorem)

<!-- source: http://homepages.math.uic.edu/~wangjing/stat416/orderstat-exp1.pdf | H. N. Nagaraja, ch. 11 Handbook of Statistics (UIC STAT416 copy) -->
Full text: `research/L0/inid_exponential_order_statistics_uic.full.full.md`

For **inid** exponentials X_j~Exp(λ_j) (distinct rates allowed), D(k) = antirank (index of k-th smallest):

- **Nevzorov 1984 / Tikhov 1991:** the antirank vector is generated sequentially and
  ```
  P(D(k+1)=i) = λ_i / Σ_{j∈survivors} λ_j
  ```
  each next order statistic picked with probability proportional to its own rate — the
  product-of-rate-ratios ordering, stated and proven (joint density over n! perms) for inid
  *order statistics*. Same content as [[competing_exponential_clocks_uchicago]] but as a theorem.
- **Inid spacings are NOT independent** (Cov of consecutive spacings ∝ Cov(A_k,A_{k+1}), zero iff all λ equal) — the iid independence of [[exponential_order_statistics_memoryless_kth]] does NOT survive heterogeneity.
- Sum of top order statistics has a closed-form survival kernel (Lemma 11.3.1): integrate ∏(1−e^{−λt}) against a pooled-rate exponential.

## Why this closes the PE 597 gap

Relative speed W_i = V_i/(t−i) with V_i~Exp(1) is Exp(t−i) — rate = *distance* t−i. So which boat is "slowest relative to a target t" is chosen with probability proportional to its rate (=distance), and recursing on the two subranges makes p(n,L) a sum of products of distance ratios. This is the exact-integration route that memory.md demands (parity depends on speed magnitudes, not just w-order). Also: distances are distinct ⇒ inid condition → Nagaraja's theorem is the valid justification.

[[laplace_difference_of_exponentials_libretexts]] governs a bump's relative-speed magnitude; [[inverse_exponential_finish_times_wikipedia]] governs finish events (inverse-exponential, not clocks).
