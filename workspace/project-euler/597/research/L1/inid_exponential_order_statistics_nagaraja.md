# INID exponential order statistics — Nagaraja (Order Statistics from Indep. Exponential RVs)

<!-- source: http://homepages.math.uic.edu/~wangjing/stat416/orderstat-exp1.pdf | H. N. Nagaraja, Assoc. & Applications ch. 11, Handbook of Statistics (universit course copy at UIC STAT416) -->
Full text: `research/L0/inid_exponential_order_statistics_uic.full.full.md`

## What the source establishes

For **independent non-identically distributed (inid)** exponentials X_j ~ Exp(λ_j),
j=1..n, with possibly distinct rates λ_j:

- **iid case recap (Rényi 1953):** the order-statistic spacings of iid Exp(1) are
  independent exponentials with rates n, n−1, …, 1 — the representation already in
  the library [[exponential_order_statistics_memoryless_kth]]. Nagaraja cites
  Rényi and David & Nagaraja for this.

- **inid sequential antirank representation (Nevzorov 1984 / Tikhov 1991):** order
  the sample as X_(1) < … < X_(n) and let D(k) be the *antirank* (which original
  index is the k-th smallest). Then the antirank vector is generated **sequentially**,
  and after D(1),…,D(k) are fixed, D(k+1) is chosen from the remaining set Ω_k with

  ```
  P(D(k+1) = i) = λ_i / Σ_{j∈Ω_k} λ_j ,   i ∈ Ω_k .
  ```

  That is, each successive order statistic is picked among the *surviving* exponentials
  with probability proportional to its own rate λ_i — exactly the product-of-rate-ratios
  ordering of competing heterogeneous clocks, now stated as a theorem for inid *order
  statistics* with a proof via the joint density over n! permutations.

- **Distributional identity (Tikhov):** with iid standard exponentials Z_k independent
  of the antiranks,
  ```
  X_(k) = A_k Z_k + …  with A_k = ( λ_{D(k)} + … + λ_{D(n)} )^{-1}
  ```
  i.e. each order statistic is a fixed combination of the pooled-survivor rate reciprocals
  times the Z_k. The spacings X_(k) − X_(k−1) = A_k Z_k likewise carry the pooled-survivor
  rates.

- **Inid spacings are NOT independent** (unlike the iid case): Cov of consecutive spacings
  equals Cov(A_k, A_{k+1}), which vanishes **iff** the λ_j are all identical. This is the
  key caveat: the nice iid independence does not survive heterogeneity.

- **Sum of top order statistics (Lemma 11.3.1):** closed-form survival function for sums
  of the top k order statistics, built by integrating the product of (1 − e^{−λt}) factors
  against a pooled-rate exponential kernel — the same structure a bump/finish chronology
  sum would need.

## Implication for PE 597

The recursion for p(n,L) conditions on which boat is "slowest relative to a target t":
boat i's relative speed W_i = V_i/(t−i) with V_i~Exp(1) is Exp(t−i) with *rate t−i*
(a distance). The boat with the *minimum* W_i sets the target for the recursion. Nagaraja's
inid representation is the formal justification that, conditional on survivors, the next
slowest is chosen with probability proportional to its rate (distance), and each survivor's
next "relative speed" is again exponential at its remaining rate (memoryless). This tells
**what the clocks are** (relative speeds W_i = V_i/(t−i), Exp with rate = distance) and why
the recursion's probabilities are products of rate ratios even though the raw speeds V_i are
iid — the rates become heterogeneous *distances* after the change of variable.

Caveat carried forward: because V_i are independent but the *relative* rates t−i are distinct,
the resulting spacing independence of the iid case does NOT apply automatically; the library's
[[competing_exponential_clocks_uchicago]] product form covers the sequential choice, and
Nagaraja supplies the inid order-statistic theorem that choice is valid.

## Practical note

This source is the missing theorem for the recursion: it names (Nevzorov) and proves the
sequential survivor-proportional selection among heterogeneous exponentials, and it gives the
exact kernel for sums of top order statistics. Together with the existing competing-clocks
and iid-spacing notes it closes the question "what are the clocks and why are the odds
products of rate ratios". [[laplace_difference_of_exponentials_libretexts]] still governs the
*bump event's* relative-speed magnitude; [[inverse_exponential_finish_times_wikipedia]] still
governs finish events.
