# SUPPLY — the weight-threshold ladder (where linear supply becomes typical)

This ladder owns GOAL.md's one unfinished computation: **does the minimum
weight ratio at which linear supply becomes typical tend to 0, or plateau near
1/8?** It is deliberately weaker than SUPPLY itself — the primes are switched
off, and the object is the fold `Φ_n` on *generic* binary strings of a given
density, not on the prime gap-parity string. That is what makes the bottom
rungs attackable: the whole ladder is about `Φ_n` alone plus a density
parameter, and the primes re-enter only at the top.

The measured column so far (CONCLUSION-PASS2.md §2; thread
`supply-class-characterisation`; exhaustive to n=16, 300 samples per weight
above):

```
n     8      10     12     14     16     32     64     128
w/n   0.375  0.300  0.250  0.286  0.188  0.156  0.125  0.125
```

"Typical" means: among weight-`w` strings in F₂ⁿ, at least half have
`ν₂/n ≥ 0.40` and the mean over them is `≥ 0.40`. The column fell
monotonically except for the n=14 wobble (0.286), then held at 0.125 twice. The
run was stopped before resolving the limit, and that resolution is what this
ladder weakens down to.

```ladder
goal: Determine the limit of the threshold ratio ρ_n(c) = min{ w/n : at least half of the weight-w strings in F₂ⁿ have ν₂(h)/n ≥ c }, for a fixed c (the measured column uses c = 0.40), and say whether ρ_n(c) → 0 or plateaus at a positive constant as n → ∞ — then name the weakest density input on the prime gap-parity string that the answer forces. This is GOAL.md's head question, itself already a weakening of SUPPLY (primes off, generic strings on).
difficulties: sampling-bound, limit-indeterminacy, boundary-spike, genericity-transfer, primes-transfer
status: open
```

- `sampling-bound` — the measured column reaches only n=128, exhaustive to
  n=16 and 300 samples per weight above; the tail of a limit question lives
  past what sampling reaches, and the frac column needs enough samples to be
  trusted.
- `limit-indeterminacy` — "tends to 0" vs "plateaus at a positive constant" is
  a *limit* distinction: no finite table, however long, decides it. Only a
  structural argument in the fold's submask/hit-set geometry (why is a
  weight-w string typically read by a linear number of depths, and does that
  mechanism survive at any positive density?) can settle the sign.
- `boundary-spike` — the single-boundary 1 `h = e_{n−1}` gives
  `wt(Φ_n h) = n−2` at `wt(h) = 1`, and `h = e_{n−2}` gives `⌈(n−2)/2⌉`
  (odd depths), but both are *per-window* families, not fixed strings — a
  fixed single 1 has `ν₂ = O(1)` (claim
  `fixed-single-1-fold-weight-bounded-by-j`). Any density input must be
  stated for a fixed string and must not be carried by the boundary spike.
- `genericity-transfer` — a threshold over random weight-w strings is a
  statement about the *typical* string of a given density, not about any one
  fixed string; passing from "typical" to "this string" requires a named
  non-adversariality property (the first pass's genericity gap).
- `primes-transfer` — the primes sit at switch density ≈ 0.585, far above any
  measured threshold, but the real h is one fixed string and is not known
  generic; naming a *provable* non-adversarial property of the prime string is
  exactly the parity-barrier difficulty (ABGS 2011 §9).

```rung
id: R-threshold-measured-n128
statement: For the fold Φ_n on arbitrary binary strings (primes off, no fixed-string claim), the minimum weight ratio w/n at which linear supply is typical (≥ half of weight-w strings have ν₂/n ≥ 0.40, mean ≥ 0.40) is n=8→0.375, 10→0.300, 12→0.250, 14→0.286, 16→0.188, 32→0.156, 64→0.125, 128→0.125 — exhaustive to n=16, 300 samples per weight above. The column fell monotonically except n=14, then held at 0.125 twice. Numerical evidence, not a theorem.
off: sampling-bound, limit-indeterminacy, boundary-spike, genericity-transfer, primes-transfer
stance: settled
merge: Settled by CONCLUSION-PASS2.md §2 and thread supply-class-characterisation (the run's own measurement, cross-checked by two code paths at n≤16). Turn `sampling-bound` back on: GOAL.md's third pass explicitly requires *more than* 300 samples per weight before the frac column can support the plateau claim, so the next move is to raise the sample count at the two plateau points first, then extend. First move is R-threshold-high-sample.
```

```rung
id: R-threshold-high-sample
statement: For n=64 and n=128, using the canonical floored oracle (guards ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975 asserted on the produced array) and the fixed definition (at least half of weight-w strings have ν₂/n ≥ 0.40, mean ≥ 0.40), recompute w*/n with at least 1000 samples per weight. Determine whether the two consecutive 0.125 readings reproduce within the binomial ±2σ width, or whether the plateau was a 300-sample artifact.
off: limit-indeterminacy, boundary-spike, genericity-transfer, primes-transfer
stance: open
merge: If 0.125 reproduces at ≥1000 samples/weight, `sampling-bound` is dead at these two n and the next move is R-threshold-n512. If it fails to reproduce and the ratio actually fell, the plateau was noise — itself evidence for tends-to-0, to be confirmed at larger n. First move: rerun the accepted capture shape (code/out/linear_supply_by_weight.txt) at n=64,128 with the sample count raised and the same oracle cross-check, n=8 witness, and discriminating all-ones control. Falsifier: 0.125@64 or 0.125@128 moves by more than ±2σ while the mean column is unchanged.
```

```rung
id: R-threshold-n512
statement: Extend the threshold column to n = 256 and n = 512 (one and two doublings past the current ceiling), with at least 1000 samples per weight (the count settled in R-threshold-high-sample) so the frac column is trustworthy, and report w/n per n together with the mean and the fraction at each weight. Decide, from the data, whether the ratio continues to fall through 0.125 or holds at 0.125 for a third and fourth consecutive doubling. Numerical evidence only — the limit stays undecided whatever the table shows.
off: limit-indeterminacy, boundary-spike, genericity-transfer, primes-transfer
stance: open
merge: A finite table, even to n=512, cannot decide tends-to-0 vs plateau; it can only say whether the plateau is still holding. Turn `limit-indeterminacy` back on: name the structural mechanism (hit-set sizes |H_j| under the submask relation, and why a density-δ string is typically read by a linear number of odd/other depths) that determines the sign. First move is R-threshold-limit. Expected bite: `limit-indeterminacy` — this is where sampling stops being the method and the fold's geometry must take over.
```

```rung
id: R-threshold-limit
statement: Prove, by an argument in the fold's submask/hit-set geometry (not by extending the table), that ρ_n(c) → 0 or that ρ_n(c) plateaus at a positive constant — for a fixed c. If it tends to 0, the required input reduces to positive density plus non-adversariality; if it plateaus at 1/8 (or another constant), that constant is real and belongs in the statement. Either answer is a genuine result: a density bound instead of full switch density.
off: boundary-spike, genericity-transfer, primes-transfer
stance: open
merge: The limit, once known, is a statement about typical weight-w strings, not about a fixed string. Turn `boundary-spike` back on: define the class of fixed strings for which the limit applies — excluding the per-window boundary spike e_{n−1} and respecting the fixed-vs-per-window distinction (fixed single 1 is O(1), claim fixed-single-1-fold-weight-bounded-by-j). First move is R-generic-density-input. Expected bite: this rung is where `limit-indeterminacy` actually bites, since no computation resolves the sign.
```

```rung
id: R-generic-density-input
statement: There is a condition C(h), stated for a fixed binary string h, of the form "h has density ≥ δ for some δ below the prime switch density 0.585 AND h is non-adversarial in a named sense X", such that C(h) implies ν₂(h)/n ≥ c·n for all large n, and X is not implied by any of the five closed doors (all-ones, Thue–Morse, balanced anti-dyadic half-step strings are the negative controls) and is not carried by the boundary spike e_{n−1}. The value of δ comes from the threshold limit: δ → 0 if ρ_n → 0, δ = the plateau constant otherwise.
off: primes-transfer
stance: open
merge: This rung is about generic fixed strings, not the primes. Turn `genericity-transfer` back on: the real h is one fixed string and "typical" is not "this string" — replace the hypothesis "h is generic" with a property that is provable or at least named for the prime gap-parity string. First move is R-primes-density-input. Expected bite: `genericity-transfer` — the first pass's gap was exactly that being above a threshold does not prove the primes' h has linear supply.
```

```rung
id: R-primes-density-input
statement: The real prime gap-parity string h (switch density ≈ 0.585, above every measured threshold) satisfies a named, provable non-adversarial property X that, together with its density, forces ν₂(n) ≥ c·n for all sufficiently large n — the weakest arithmetic input the threshold ladder can deliver. If the only X that works is "positive mod-4 switch density" itself, the honest output is that the threshold reduction gives nothing beyond the known dead-end reduction, and the ladder's top is the rival negative statement.
off:
stance: open
merge: Terminal rung of this ladder — no threshold difficulty left to switch off. If settled positively, it hands a named density input to supply.md's R-submask-sufficiency and from there to R-full-supply (the full SUPPLY conjecture). If it settles negatively, the threshold ladder is exhausted at a real constant (density ≥ δ plus a non-adversariality hypothesis that is unavailable for the primes), and the result is a precisely-stated density bound, problem.md result type 4 — never written as SUPPLY solved.
```
