# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `competing_exponential_clocks_uchicago.md` | UChicago STAT253/317 Lecture 9 (Yibi Huang) summary: min of independent exponentials is Exp with pooled rate, P(X_j=min)=λ_j/Σλ, memoryless property, and the product-of-rate-ratios form for the probability of a given sequence of heterogeneous exponential clocks. Candidate machinery for exact (non-MC) chronology sums over the bump/finish events. |
| `exponential_order_statistics_memoryless_kth.md` | KTH course notes (Timo Koski) proving that spacings of i.i.d. Exp(1) order statistics are independent exponentials with rates n,n-1,...,1 — the memoryless-order-statistics structure that governs exact integration over the iid Exp(1) boat speeds in PE 597. Full text is embedded in this same file. |
| `inverse_exponential_finish_times_wikipedia.md` | Wikipedia "Inverse distribution" — reciprocal-transform density/CDF formula and the inverse-exponential distribution (density λ/x^2 e^{−λ/x}, CDF e^{−λ/x}, no moments ≥1). Establishes that each boat's finish time (L−p_j)/v_j with v_j~Exp(1) is inverse-exponential, hence has NON-constant hazard, so finish events are not competing exponential clocks — a correction to the earlier exponential-clocks brief. |
| `laplace_difference_of_exponentials_libretexts.md` | Siegrist LibreTexts 5.28 "The Laplace Distribution": the difference of two iid Exp(1) variables is standard Laplace (density (1/2)e^{−|u|}, MGF 1/(1−t²), even moments (2k)!, |Z|~Exp(1)). This is the distribution of the RELATIVE speed v_j−v_i driving each bump event in the race — new input for the exact bump-rate + finish-hazard chronology. |

## Folds

| Note | Covers |
| --- | --- |
| `L1/exponential_order_statistics_memoryless_kth.md` | One fold over the i.i.d. Exp(1) order-statistics/memoryless structure (single source). |
| `L1/competing_exponential_clocks_uchicago.md` | One fold over heterogeneous independent exponential clocks / rate-ratio product form (single source). |
| `L1/inverse_exponential_finish_times_wikipedia.md` | One fold over the inverse-exponential finish-time distribution and its non-constant hazard (single source). |
| `L1/laplace_difference_of_exponentials_libretexts.md` | One fold over the Laplace distribution of relative boat speeds (single source). |

Full text for each source is in `L0/`; see `L0/INDEX.md`.
