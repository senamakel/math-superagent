# Laplace distribution — difference of two iid exponentials (Siegrist, LibreTexts)

<!-- source: https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/05:_Special_Distributions/5.28:_The_Laplace_Distribution | downloaded from LibreTexts -->

## What the source establishes

For independent X, Y ~ Exp(1) (same rate), the difference Z = X − Y has the
**standard Laplace** (double-exponential) distribution:

- density  g(u) = (1/2) e^{−|u|} on ℝ
- MGF  m(t) = 1/(1 − t²), t∈(−1,1)  (so with scale b: M(t) = e^{μt}/(1−b²t²))
- moments: odd moments = 0 (symmetry); even moments E[Z^{2k}] = (2k)!  (so
  Var = 2, excess kurtosis = 6)
- |Z| ~ Exp(1) (the absolute value of a standard Laplace is standard
  exponential); Z = ±V with equal probability for V~Exp(1).

## Implication for PE 597

A bump happens when boat j catches boat i ahead: contact time solves the linear
kinematics with relative gap g and relative speed v_j − v_i. Since v_j, v_i are
iid Exp(1), the relative speed v_j − v_i is Laplace. This is the *input*
distribution for the bump event's timing, and it is what the open derivation
(what exactly the "clocks" are) must integrate over. It complements the
existing library:
- [[exponential_order_statistics_memoryless_kth]] gives the spacings/order-
  statistic structure of a single boat's Exp speeds;
- [[competing_exponential_clocks_uchicago]] gives the rate-ratio product form
  where event times are exponential;
- this note gives the distribution of the *relative* speed that drives each
  catch-up — the Laplace law (non-exponential, symmetric, |Z| exponential).
So the bump clock's arrival time is built from a Laplace relative speed: its
density/moments here are the machinery an exact bump-rate + finish-hazard
chronology sum needs. The full reduction remains the run's own derivation.
