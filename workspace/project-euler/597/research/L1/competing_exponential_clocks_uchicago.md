# Competing exponential clocks — UChicago STAT253/317 Lecture 9 (Yibi Huang)

<!-- source: https://www.stat.uchicago.edu/~yibi/teaching/stat317/2021/Lectures/Lecture9.pdf | converted from PDF -->

## What the source establishes

For **independent** exponentials X_i ~ Exp(λ_i) (rates may differ):
- **Min as a single clock:** min(X_1,...,X_n) ~ Exp(λ_1 + ... + λ_n). Proof: P(min > t) = ∏ e^{−λ_i t} = e^{−(Σλ)t}.
- **Winner probability:** P(X_j = min) = λ_j / (λ_1 + ... + λ_n), by conditioning on X_j = t and integrating. This is the "competing clocks" property.
- **Memoryless property:** P(X > t+s | X > t) = P(X > s); used to argue the *post office* example (remaining service times stay Exp with original rates).
- **Ordering product form** (consequence, used throughout queueing/Mondrian): the probability that heterogeneous independent exponential clocks fire in a specific sequence i_1, i_2, ..., i_D is
  `(λ_{i1}/Σλ) · (λ_{i2}/(Σλ − λ_{i1})) · (λ_{i3}/(Σλ − λ_{i1} − λ_{i2})) · ...`,
  i.e. at each stage the next clock is chosen among the surviving clocks with probability proportional to its rate. This is the repeated application of the min/winner property + memorylessness.

## Implication for PE 597

The race has n boats with i.i.d. Exp(1) speeds v_j (constant speed until finish or bump).
For a *fixed* speed vector v, each boat j's time to finish is (L − p_j)/v_j, and the "bump" times are solutions of linear kinematics reflecting catch-ups and removals. The set of boats that are still rowing at any moment forms a set of **competing clocks**: conditional on the current configuration, the *next* event (a specific boat finishing or a specific pair bumping) happens first with probability proportional to its rate, and after that event the survivors remain independent exponentials (memoryless). So the entire bump/finish chronology can be summed as **products of rate ratios**, with no high-dimensional integral over the speeds.

The subtlety (flagged in memory.md) is that event *rates are not the raw speeds*: a catch-up time depends on the relative speed of two boats through a linear equation, so the "clock rate" of a bump is not simply v. The library's two exponential facts — i.i.d. spacings (already held) and this heterogeneous competing-clocks/ordering product form (new) — together give the machinery to attempt an exact sum over the exponentially distributed *gaps in geometry* rather than the raw speeds. The derivation of exactly what the clocks are for this race remains the run's own task.

## Practical note for the run

The product-of-ratios formula is exact and combinatorial over the set of orderings of heterogeneous exponentials; it is the standard way to get exact (non-MC) probabilities for exponential event chronologies and is the intended route to dodge enumeration over speed vectors.
