# Sequence-analysis route: CLOSED (directive 32)

The pattern-finder's analysis of the measured ν₂ / S sequence — white-noise law,
per-scale second-moment split, recurrence/OEIS checks — was a route to GOAL
priority 2 (an arithmetic input on the prime gap-parity string weaker than
positive mod-4 switch density). Directive 32 registers it closed.

```thread
id: sequence-analysis-route
question: Does the measured ν₂/S sequence yield an arithmetic input on the prime
  gap-parity string h strictly weaker than positive mod-4 switch density, i.e. a
  measurement route to GOAL priority 2?
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: per-scale-refinement-collapses-to-switch-density,
  g-normalized-fold-weight-white-noise, density-model-rising-mean-is-generic
blocked-by:
next: none — closed. The per-scale second-moment refinement collapses back to the
  g=0 switch-density scale (claim per-scale-refinement-collapses-to-switch-density:
  g=0 variance share 0.425@400, 0.730@1000, 0.553@4000), and the √n/white-noise
  plateau is fold-generic (uniform h reproduces it), so the sequence data provides
  no arithmetic handle specific to the primes. GOAL priority 2 is unanswered by
  any measurement; only an unconditional arithmetic theorem can reach it.
```

## Why it closed

- The per-scale second-moment share of the g=0 scale dominates at every computed
  n, so the natural refinement toward a weaker input collapses to the same
  switch-density scale the known reduction already collapses to.
- The √n/white-noise law and the rising mean are reproduced by uniform /
  density-matched Bernoulli input: the primes sit in the generic-balanced class,
  not in a class the fold reads distinctly.
- Therefore no sequence tool or measurement supplies a prime-specific arithmetic
  handle. The open step remains an unconditional second-moment bound for the
  prime string (condition (A) of the fold-second-moment-krawtchouk route).

Terminus assessment: `research/notes/terminus-assessment-directive32.md`.
