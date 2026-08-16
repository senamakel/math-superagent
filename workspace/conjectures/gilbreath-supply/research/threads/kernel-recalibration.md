# Kernel recalibration: a 2-dimensional kernel, and what it does to low-weight-image arguments

Operator directive 5. The fold-rank correction is accepted: under the operative
convention (rows `d = 2..n−1`, an `(n−2)×n` matrix) `rank Φ_n = n−2` — full
row rank, nullity 2 — with `ker Φ_n = span(even-alt, odd-alt)`. This thread
carries the two consequences the operator said not to assume, in the two
directions they cut.

```thread
id: kernel-recalibration
question: The kernel is 2-dimensional, not 1-dimensional: two independent
  collapse directions, even-alt and odd-alt, with all-ones their XOR. (1) Every
  low-weight-image argument calibrated against a one-dimensional kernel must be
  recomputed — specifically, does the prime switch bit h have a large component
  along even-alt / odd-alt, so the supply bound fights more structure than the
  five closed doors accounted for? (2) All-ones stays in the kernel, so closed
  door 1 survives untouched — the correction must not be read as reopening it.
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: fold-rank-is-n-2-nullity-2-alternating (checked n=2..20; all-n proof
  is task prove-fold-rank-all-n), hypergraph-coboundary-false-premise
blocked-by:
next: (a) compute ⟨h, even-alt⟩ and ⟨h, odd-alt⟩ over parity classes of the
  prime switch bit h (and near-kernel vectors), state whether h has a large
  kernel component — task kernel-component-of-prime-h, now question (d) of the
  directive-8 averaged push, answered with the 40000-term streamed pipeline
  (code/nu2_extended/track_smax.py), not with reading; (b) record the
  full-row-rank / surjectivity fact in a claim block (task
  state-fold-full-row-rank-surjectivity — deferred by 'nothing else'): Φ_n is
  surjective onto F₂^{n−2}, so every weight profile is attained by some input
  and the whole difficulty is which inputs the primes supply; (c) reprice any
  low-weight-image argument that used nullity 1 or span(all-ones) as its
  calibration.
```

## What is now known (and what it overturns)

- `ker Φ_n = span(even-alt, odd-alt)` — the period-2 strings — 2-dimensional,
  machine-verified `n = 2..20` and carried by the one-line all-n proof (the
  submask-XOR matrix `Z[d][s] = [s ⊆ d]` is unit lower-triangular).
- `Φ_n` has **full row rank** `n−2`: it is surjective onto `F₂^{n−2}`, the
  opposite of "nearly singular". The kernel being large does not make the map
  nearly singular here — rank and nullity are independent coordinates, and the
  correction moves the rank *up* to full.
- All-ones = even-alt ⊕ odd-alt, so it remains in the kernel; closed door 1
  (weight alone does not force ν₂ large) is untouched.
- The hypergraph-cut/Cheeger route was already refuted on the corrected
  2-dimensional kernel (`hypergraph-coboundary-false-premise`); this thread does
  not reopen it, it extends the recalibration to every other argument that
  assumed nullity 1.
