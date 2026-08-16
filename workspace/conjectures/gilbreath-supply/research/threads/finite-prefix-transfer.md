# The finite-prefix transfer: from ergodic randomization to the fixed string

Every skeleton in `research/backward/` ultimately rests on converting a theorem
about measures over infinite configurations converging in the weak-* topology at
density-one *times* into a statement about the fold weight of ONE fixed
deterministic string h (the prime gap parities) at ONE finite depth n. That
conversion — the finite-prefix transfer — is named in `research/notes/
pivato_lucas_mixing_equivalence.md` ("The open step (not in any source)") and in
`research/ROOT.md`, but it has no thread of its own and no technical statement.
This thread pins the gap so it can be attacked instead of rediscovered.

```thread
id: finite-prefix-transfer
question: Given an ergodic weak-* statement (Pivato-Yassawi 2006 Thm 7.1: Φ asymptotically randomizes µ iff µ is Lucas mixing; Takei 2017: Rule 90 drives strong-mixing input to uniform along Cesàro means), can it license a lower bound wt(Φ_n h) ≥ c·n for the single deterministic prime-gap-parity string h and all (or density-one) finite depths n?
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: lucas-mixing-iff-fold-randomization, takei-rule90-mixing-limits-uniform, lucas-submask-odd
blocked-by: the theorems are about (a) infinite sequences, (b) the empirical *law* (statistical convergence), and (c) density-one sets of *times*; SUPPLY needs (a') a fixed prefix h[0..n-1], (b') the actual Hamming weight of Φ_n h, not its distribution, and (c') a quantitative bound valid for all large n with an explicit c. Neither (a) nor (b) is quantitative in the sources, and (c) is the hard "density-one times → all sufficiently large n" promotion the parity barrier makes non-trivial.
next: (1) make it precise: what does "µ is Lucas mixing" mean for the empirical measure of the prime-gap-parity prefix, and under what prime-gap correlation hypothesis does it hold? — this is a concrete research request (G-weak-input-primes-satisfy-C next move) and the arithmetic heart; (2) quantify the weak-* convergence: the only quantitative handle in the library is Rampersad-Wiebe's 2-regularity/averages machinery (the fold's image grows ~1.2^n, not ~n, on structured inputs — a caution), and the submask-XOR expectation bound E[wt]= (n-3)/2 for uniform input; (3) attack the finite direction directly: fix h of length n, express wt(Φ_n h) in the submask-XOR character coordinates and seek a variance/second-moment bound on h along submask windows (G-var-vanishing) that is a pure arithmetic statement about the primes — this is exactly GOAL priority 2's bounded-autocorrelation/Walsh candidate.
```

## Why every skeleton needs this

- **Averaged (supply-averaged-second-moment):** the Chebyshev-over-n glue empties
  the lower tail once the mean is ≥c₀ and the variance →0. The variance is a
  second-moment statement about h along submask windows — the finite-prefix form
  of "the empirical measure's correlations decay".
- **Weak input (weak-input-fold):** G-weak-input-submask-density needs C(h) in
  the T(d) coordinates to force a positive density of odd depths; the transfer
  is where the ergodic "Lucas mixing ⇒ randomization" becomes "C(h) ⇒ weight".
- **Equivalence (supply-switch-equivalence):** G-sup-implies-switch is a
  finite-window statement about prime-realizable h; the transfer is the
  quantitative side of "density-one-time convergence ⇒ all-large-n lower bound".

## The precise open question to hand to research

Is there a provable inequality of the shape: for h the real prime gap-parity
string, if its submask-window autocorrelation / second moment is bounded (as the
primes empirically have), then wt(Φ_n h) ≥ c·n for all n ≥ N₀ with explicit
absolute c, N₀? The sources give the ergodic version (Lucas-mixing ⟺
randomization at density-one times) and the finite version's *absence* (no
source states a quantitative bound). Filling this is the run's central gap.
