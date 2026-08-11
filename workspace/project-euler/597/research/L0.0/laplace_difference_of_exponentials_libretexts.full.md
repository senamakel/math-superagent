# Laplace distribution — difference of two iid exponentials (Siegrist, LibreTexts)

<!-- source: https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/05%3A_Special_Distributions/5.28%3A_The_Laplace_Distribution | full text at research/L0/laplace_difference_of_exponentials_libretexts.full.full.md -->

For independent X, Y ~ Exp(1), the difference Z = X − Y is **standard Laplace**
(double exponential): density g(u) = (1/2)e^{−|u|} on ℝ; MGF 1/(1−t²); odd
moments 0, even E[Z^{2k}]=(2k)! (Var=2, excess kurtosis 6); |Z| ~ Exp(1).

## Why it bears on PE 597

A bump is a catch-up of boat j on boat i ahead; its timing depends on the
**relative speed** v_j − v_i. With speeds iid Exp(1), the relative speed is
Laplace — the input distribution of every bump event. This complements the
library: [[exponential_order_statistics_memoryless_kth]] (order-statistic
spacings) and [[competing_exponential_clocks_uchicago]] (rate-ratio product
form) cover single-boat Exp structure; this note supplies the *Laplace law of
the relative speed* driving catch-ups, needed for the exact bump-rate +
finish-hazard chronology sum (the run's own open derivation).
