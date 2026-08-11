# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L1/competing_exponential_clocks_uchicago.md` | Summary of UChicago STAT253/317 Lecture 9 (Yibi Huang): min-of-exponentials pooled rate, P(fires first)=λ_j/Σλ, memoryless property, and product-of-rate-ratios form for any specific firing order. Candidate machinery for exact chronology sums. |
| `L1/dirichlet_distribution_wikipedia.md` | Summary of Wikipedia "Dirichlet distribution": normalized iid Exp(1) are uniform on the simplex (Dirichlet(1,…,1)); race outcome is invariant under common scaling of speeds, so p(n,L) = uniform-simplex measure of the parity region — the exact integration target. |
| `L1/exponential_order_statistics_memoryless_kth.md` | Summary of KTH order-statistics note (Timo Koski): order-statistic spacings of iid Exp(1) are independent exponentials with rates n,n-1,...,1; the memoryless structure for exact integration over the Exp speeds. |
| `L1/inid_exponential_order_statistics_nagaraja.md` | Summary of Nagaraja INID exponential order statistics chapter (via UIC STAT416): sequential survivor-proportional selection among heterogeneous exponentials (Nevzorov/Tikhov antirank theorem), P(D(k+1)=i)=λ_i/Σ_survivors λ_j; spacings NOT independent when rates differ; closed-form kernel for sums of top order statistics. Closes the 'what are the clocks / why product of rate ratios' gap: relative speeds W_i=v_i/(t−i)~Exp(t−i) with rate=distance, so the exact recursion sums products of distance ratios. |
| `L1/inverse_exponential_finish_times_wikipedia.md` | Summary of Wikipedia "Inverse distribution": finish time (L−p_j)/v_j with v_j~Exp(1) is inverse-exponential (density (c/t²)e^{−c/t}, non-constant hazard) — finish events are NOT competing exponential clocks. |
| `L1/laplace_difference_of_exponentials_libretexts.md` | Summary of Siegrist LibreTexts 5.28 "The Laplace Distribution": difference of two iid Exp(1) is standard Laplace — the distribution of the RELATIVE speed v_j−v_i driving each bump event. |
