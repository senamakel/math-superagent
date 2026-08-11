# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

Sources are stored in `L0/` (full source text, `<name>.full.md`) and `L1/` (short summaries, `<name>.md`). Read the summary first; open the `.full.md` companion only when the summary does not answer the question.

| File | Purpose |
| --- | --- |
| `L1/competing_exponential_clocks_uchicago.md` | UChicago STAT253/317 Lecture 9 (Yibi Huang) summary: min of independent exponentials is Exp with pooled rate, P(X_j=min)=λ_j/Σλ, memoryless property, and the product-of-rate-ratios form for the probability of a given sequence of heteregeneous exponential clocks. Candidate machinery for exact (non-MC) chronology sums over the bump/finish events. Full text: `L0/competing_exponential_clocks_uchicago.full.md`. |
| `L1/exponential_order_statistics_memoryless_kth.md` | KTH course notes (Timo Koski) proving that spacings of i.i.d. Exp(1) order statistics are independent exponentials with rates n,n-1,...,1 — the memoryless-order-statistics structure that governs exact integration over the iid Exp(1) boat speeds in PE 597. Full text is embedded in this same file. |
| `L1/inverse_exponential_finish_times_wikipedia.md` | Wikipedia "Inverse distribution" — reciprocal-transform density/CDF formula and the inverse-exponential distribution (density λ/x^2 e^{−λ/x}, CDF e^{−λ/x}, no moments ≥1). Establishes that each boat's finish time (L−p_j)/v_j with v_j~Exp(1) is inverse-exponential, hence has NON-constant hazard, so finish events are not competing exponential clocks — a correction to the earlier exponential-clocks brief in context.md. Full text: `L0/inverse_exponential_finish_times_wikipedia.full.md`. |
