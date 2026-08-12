# The sum-of-divisors function and the Riemann hypothesis (Nicolas survey)

Source: http://math.univ-lyon1.fr/~nicolas/colHRrev1mod.pdf — `[[nicolas_divisor_function_RH.full]]`
(J.-L. Nicolas, "The sum of divisors function and the Riemann hypothesis", survey/handout,
Institut Camille Jordan, Université Lyon 1.)

## What it is

An authoritative survey of the large-value behaviour of sigma(n)/n and its exact
relation to the Riemann hypothesis, centered on Robin's 1984 theorem. Primary,
peer-reviewed-level treatment (from the author's own university page).

## Robin's theorem (the exact statement, this is the load-bearing content)

**Robin (1984).** Let gamma = 0.57721... be the Euler constant and
σ(n) = sum of divisors of n. Then the Riemann hypothesis is true iff

    σ(n)/n < e^gamma · log log n   for every n > 5040.

Equivalently (the form A088912's bound is built on): assuming RH, σ(n)/n <
e^gamma log log n for all n > 5040, and this inequality is *equivalent* to RH.

So for a number n with half-integer abundancy k+1/2 (this problem) one gets the
conditional upper bound (k+1/2) < e^gamma log log n, i.e. n bounded in terms
of k. For k = 6 (abundancy 13/2) this says on the hypothesis that any such n
satisfies e^gamma log log n > 13/2, forcing log log n > (13/2)/e^gamma ≈
13/(2·1.78107) ≈ 3.65, log n > e^3.65 ≈ 38.4, n > e^38.4 ≈ 4.7e16. This is the
**hypothesis-conditional** lower bound quoted in the A088912 note
(a(6) > 5e16, a(7) > 1.9e29). It is not needed decisively here because the
unconditional explicit value a(6) ≈ 1.71e44 >> 10^18 already settles that k=6
contributes nothing below 10^18 — but it is the *reason* a(6) is that large, and
it is the origin of the reachability cutoff that restricts the DFS to k=1..5.

Also records Gronwall's 1913 classical result σ(n)/n ⩽ (1+o(1)) e^gamma log log n
(limsup), and Ramanujan's suppressed-manuscript refined asymptotic under RH.

## Also in the survey

- Colossally abundant (CA) and superabundant numbers: the extremal numbers at
  which σ(n)/n approaches its maximal size; Robin's proof in the original paper
  reduces the inequality to checking CA numbers. Nicolas generalizes.
- Effective form improving on Robin's inequality under RH (Cor 1.2): for
  n > 16, σ(n)/n ⩽ e^gamma( log log n − 0.582/√log n ) under RH.

## Relevance / bearing for this problem

Gives the *primary* statement and proof-theoretic origin of the Robin inequality
that A088912's lower-bound comments cite (so the library now holds the primary
source for the claim `a088912-abundancy-threshold`, which previously leaned on a
secondary OEIS retelling). Confirms that the reachability cutoff for k≥6 is
genuinely grounded: both the hypothesis-conditional bound (a(6)>5e16) and the
unconditional explicit value (a(6)≈1.71e44) exceed 10^18.

## Does not settle

Robin's inequality is conditional on RH for its equivalence; the specific numeric
a(6) value comes from explicit hemiperfect tables (A088912/A160678), not from
Robin's theorem alone. The sum under 10^18 remains the computation.

```claim
id: robin-inequality-RH
statement: (Robin 1984) RH is true iff sigma(n)/n < e^gamma log log n for all n > 5040; therefore a half-integer-abundancy n with sigma(n)/n = k+1/2 satisfies e^gamma log log n > k+1/2, a hypothesis-conditional lower bound on the least such n (gives a(6) > 5e16, a(7) > 1.9e29).
hypotheses: n > 5040; the inequality's equivalence is conditional on RH
holds-here: yes (we only need the conditional bound, and the unconditional explicit a(6) ~ 1.7e44 supersedes it numerically)
status: sourced (Nicolas survey; Robin's theorem stated with proof-theoretic origin)
bearing: explains/grounds why k>=6 is unreachable below 1e18; primary source behind A088912's bound
anchor: research/sources/nicolas_divisor_function_RH.full.md
```
