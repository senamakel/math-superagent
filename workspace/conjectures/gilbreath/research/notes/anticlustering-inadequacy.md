# Generic Markov anti-clustering is insufficient for G-supply (Directive 52)

`status: refuted (as a PROOF STRATEGY — not a statement about the primes)`
`thread: regeneration` (Route B, G-supply)

## The negative claim

The proof strategy "derive the supply bound `ν₂ ≥ c·w` (equivalently `ν₂ ≥ c·n`)
from the mixing / anti-clustering of the mod-4 switch bit" is REFUTED as a
strategy.  A generic Markov chain with prime-like or anti-clustered transition
probabilities does NOT force the required positive lower bound on the
worst-min `ν₂/w` statistic, so mixing alone cannot deliver G-supply.

## The evidence (exact, captured)

`code/out/anticlustering_hypothesis.captured.txt`.  For each candidate family,
`ν₂/w` is the worst (minimum) ratio over the window of a single Markov sample;
a trial "violates" if an all-2 stretch pushes `ν₂/w` below threshold.  The
threshold needed near G-supply's `n^{0.525}` target is far above the observed
worst minima:

| family | worst-min ν₂/w | trials violating |
| --- | --- | --- |
| prime-like (0.55, 0.60) | 0.0714 | 11/30 |
| anti-cluster (0.50, 0.60) | 0.3793 | 3/30 |
| anti-cluster (0.45, 0.60) | 0.2941 | 4/30 |
| anti-cluster (0.40, 0.60) | 0.3333 | 4/30 |
| Bernoulli control (0.59, 0.59) | 0.2500 | 12/30 |
| cluster (0.60, 0.50) | 0.2500 | 12/30 |
| strong cluster (0.75, 0.25) | 0.1111 | 13/30 |
| stationary density ~0.59 family | 0.13–0.30 | 11–17/30 |
| prime empirical transitions (a=0.5565, b=0.6584) | 0.2857 | 8/20 |

Even the prime's *own empirical* transition matrix fails 8/20 trials on the
worst-min statistic.  So a generic Markov model — whether anti-clustered,
clustered, or exactly matched to the primes' transition probabilities — cannot
certify `ν₂ ≥ c·w` for the worst-min bound that the dense supply target needs.

## What this refutes, and what it does not

**Refuted: the MIXING PROOF STRATEGY.**  "G-supply from anti-clustering of the
switch sequence" is a dead route.  A positive-linear lower bound cannot come
from generic Markov mixing alone.

**NOT refuted: G-supply for the primes.**  Two explicit caveats, both stated in
`research/threads/regeneration.md` Directive 52:

1. Real prime gaps are NOT a Markov chain — the empirical (a,b) transition fit
   is a two-parameter approximation, so a Markov null is a model, not the data.
2. 30 trials of a worst-min statistic is noisy (as few as 3/30 "violations"
   already for a healthy anti-clustered family).

So the correct reading is asymmetric: the Markov experiment busts the strategy,
and it leaves G-supply a named open hypothesis.  The remaining candidates are
arithmetic, not mixing — Hardy–Littlewood two-point mod-4 correlations, or the
Lemke Oliver–Soundararajan two-point bias and its oscillating second-order term.
The recorded bet is that neither is unconditional; G-supply stays a named open
hypothesis and the deliverable is the CONDITIONAL theorem with the HL/LOS
two-point switch-correlation lower bound as its named hypothesis
(`research/threads/regeneration.md`, Directive 52 "What it leaves").

## The durable finding

```claim
id: anticlustering-markov-insufficient-for-gsupply
statement: Generic Markov anti-clustering of the mod-4 switch bit does NOT deliver the supply bound ν₂ ≥ c·w (hence not ν₂ ≥ c·n). On the worst-min ν₂/w statistic, prime-like (0.55,0.60) gives 0.0714 with 11/30 trials violating; the prime's own empirical transition matrix gives 0.2857 with 8/20 violating; anti-clustered, clustered, Bernoulli and stationary-density-~0.59 families all violate 3–17/30 trials. This refutes the PROOF STRATEGY of deriving G-supply from mixing/anti-clustering, NOT the G-supply statement for the primes (real gaps are not a Markov chain; 30 trials of a worst-min statistic is noisy).
hypotheses: Markov chains on the two mod-4 switch states; ν₂/w = worst-min ratio over a single sample window; threshold near the n^{0.525} supply target.
holds-here: yes (as a statement about the strategy's failure)
status: checked (exact, captured; the failure is the finding)
bearing: closes the mixing route to G-supply; the supply side remains the single named-open hypothesis of Route B, and the honest deliverable is the conditional theorem at HL/LOS two-point level.
anchor: code/out/anticlustering_hypothesis.captured.txt, research/notes/prefix-determinism-proof.md (context of Route B)
contradicts: (none — this refutes a strategy, and it explicitly does NOT contradict the supply statement for the primes; see text)
answers: g-supply-from-mixing-closed
```
