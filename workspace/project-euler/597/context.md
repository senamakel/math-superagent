# Shared context

Standing brief: what the `research/` library establishes for PE 597 (Torpids),
so any role can act without opening sources. Detail lives in the fold notes
behind wikilinks; `research/INDEX.md` lists every source with its URL.

## Model

Speeds v_j are iid Exp(1) (v_j = −ln X_j, X_j~U(0,1)). Boat j rows at constant
v_j until it finishes (at L) or bumps the nearest rowing boat ahead (then OUT,
passed freely; bumped boat continues). Parity of the new order = the inversion
count (# pairs i<j with a bump chain i→…→j) mod 2. Goal: p(13,1800).

## Established (sources)

- **Exponential spacings.** The order-statistic spacings of n iid Exp(1) are
  independent exponentials with rates n, n−1, …, 1; survivors of an exponential
  remain exponential at original rates (memoryless). This is the structure that
  decomposes an Exp-speed integration into products over independent rates
  rather than high-dimensional integrals. [[exponential_order_statistics_memoryless_kth]]
- **Competing heterogeneous clocks.** For independent Exps with rates λ_i:
  min is Exp(Σλ_i), P(j fires first) = λ_j/Σλ_i, and a specific firing order
  has probability = product of rate ratios (one factor per event, survivor
  rates). [[competing_exponential_clocks_uchicago]]

Together: an event chronology whose event times are exponential has an exact
probability as a product of rate ratios — no sample enumeration. (What the
clocks are is now resolved below.)
- **Relative (bump) speed is Laplace.** The relative speed v_j−v_i of two iid
  Exp(1) boats is standard Laplace (density (1/2)e^{−|u|}, even moments, |Z|~Exp).
  So each catch-up's timing is built from a Laplace relative speed, not an
  exponential clock. [[laplace_difference_of_exponentials_libretexts]]
- **The clocks are relative speeds, and their ordering is survivor-proportional
  rate ratios — now a named theorem (NEW).** Relative speed of boat i to a target
  at coordinate t is W_i = v_i/(t−i) ~ Exp(t−i), rate = the *distance* t−i. The
  slowest relative to t is chosen among the survivors with probability proportional
  to its rate (Nevzorov/Tikhov inid order-statistic representation, Nagaraja):
  P(antirank = i) = (t−i)/Σ_survivors(t−s). This is exactly what the exact recursion
  sums: probabilities are products of distance-ratio factors, conditioning on the
  slowest boat and recursing on the two subranges. Caveat: inid spacings are NOT
  independent, and finish times are still inverse-exponential (not clocks).
  [[inid_exponential_order_statistics_nagaraja]]

## Caveat

- **Finish times are NOT exponential clocks.** T_j = (L−p_j)/v_j with
  v_j~Exp(1) is inverse-exponential (density (c/t²)e^{−c/t}, CDF e^{−c/t},
  non-constant hazard). Product-of-rate-ratios applies only where event times
  are genuinely exponential; finish events contribute an inverse-exponential
  competing hazard. [[inverse_exponential_finish_times_wikipedia]]

## Contradictions / gaps

None between sources and the model. The run now has the structural fact it
lacks before this cycle: conditional on a target t, the slowest boat relative to
it is chosen with probability proportional to rate (=distance), and recursing on
subranges turns p(n,L) into products of distance ratios (Nevzorov/Tikhov, Nagaraja).
memory.md: parity depends on speed magnitudes, not just the rank of
w_j = v_j/(L−p_j) (w-order hypothesis refuted) — exact integration over the Exp
speeds is required, and the recursion above is the route that integration takes.
