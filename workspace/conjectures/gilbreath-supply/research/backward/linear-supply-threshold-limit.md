# Superseded

This file was a duplicate of `research/backward/supply-threshold-limit.md`, which
already decomposes the third-pass threshold question and is on the `goals` ledger.
It was written before that canonical file was found, and it duplicated the
canonical skeleton's *false* hypergeometric-parity bound rather than fixing it.

The live decomposition is `supply-threshold-limit.md`. The false bound
`|E[(−1)^X]| ≤ (1−2θ)^m` for `X ~ Hypergeometric(n, m, θn)` is refuted there by
the counterexample n=6, m=3, w=2 (|E| = 1/5 > (1−2/3)³ = 1/27) and corrected to
an exact generating-function identity plus a unimodality/alternating-sum bound.

```skeleton
reason: Superseded. The third-pass threshold question already has a canonical skeleton at research/backward/supply-threshold-limit.md (goal id supply-threshold-limit), which was found after this duplicate was recorded. This entry's file (research/backward/linear-supply-threshold-limit.md) now carries a 'Superseded' pointer, and the canonical skeleton was corrected in place: the refuted pointwise bound |E[(−1)^X]| ≤ (1−2θ)^m (false at n=6,m=3,w=2) was replaced by the exact Krawtchouk identity plus a unimodality bound, and the mean-closed-form gap was discharged via guruswami-macwilliams-lp-from-fourier.
status: spent
```
