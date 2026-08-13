# Is Gilbreath's Conjecture Garden-Variety Numerology? — Ross, July 2026

<!-- source: https://michaelmross.github.io/gilbreath-parity-note.html | full text: sources/ross-gilbreath-parity-note.full.md -->

A precise answer to "is the conjecture just a parity fact?": **half yes, half no.** The
parity wave is a theorem; the pinning to exactly 1 is a separate, open claim. This is the
sharpest independent restatement of the run's central "which side" question on disk.

## What it establishes

- **Parity wave (proved, elementary, prime-independent).** Any sequence
  `(2, odd, odd, ...)` has every row's leading term odd. Induction: `A_1 = (odd, even,
  even, ...)`; `(odd, even, even, ...) → (|even−odd|, |even−even|, ...) = (odd, even,
  even, ...)`. The conjecture's content is precisely the step from *odd* to *exactly 1*.
- **Odd is not 1 (with concrete witnesses).** `2,3,13` gives rows `(1,10),(9)` — leading
  9, parity intact. The pyramid on every sixth prime `(2,17,41,67,...,13 terms)` has
  leading column `2,15,9,7,5,3,1,1,1,1,1,7,3` — the 1 comes and goes within a parity-sound
  pyramid. The leading entry at row r depends only on the first r+1 terms (light-cone
  locality), which is why such transients are exact, not statistical.
- **Second mechanism = the {0,2} regime.** `{0,2}` is closed under absolute differencing
  and a leading 1 against 0 or 2 stays 1. The conjecture is that the prime pyramid
  *reaches and indefinitely sustains* that regime. Double edge: **`{0,d}` is closed for
  every d ≥ 2**, so the same closure that pins 1 at d=2 preserves large disturbances at
  large d. That double edge is the crux.
- **Matched-scale comparison.** A 2-then-odds sequence below 100 with mean gap 5.1, max
  gap 8 vs the primes' 3.6/6 wanders on the left edge (`1,7,7,3,3` before settling). The
  primes never wander *for the local reason* that their second gap is 2, so the wall
  reads `|2−1|=1` immediately.
- **Eppstein already kills "gap size bound only".** A Cramér-type gap bound controls only
  entry *size*, not their *arrangement*; arrangement governs decay. The correct general
  hypothesis is that gaps do not *concentrate in an arithmetically rigid set*; the precise
  notion is **2-separation** (a set containing no two consecutive integers — evens,
  multiples of 3). If gaps were trapped in a 2-separated set, the array would be trapped
  with them.
- **State of the art (as of 2026).** Randomised versions are theorems: Chase 2024
  (uniform data, slowly growing range); Chase–Hunter–Tao 2026 (Cramér geometric model; any
  independent model neither linearly growing nor 2-separated-concentrating). Averaged
  decay rate still open: `Σ_{i≤n} c_i ≥ log(n+e)` so decay is no faster than 1/i, and
  boundedness of `(c_i)` is unproved.

## Bearing on this run

- Confirms the reduction and the "not about primes" framing from the general-class side,
  while sharpening exactly what hypothesis a general class needs: **no arithmetic rigidity
  (2-separation)**, not merely bounded gaps. Eppstein's construction (itself in the
  library) is the operative counterexample to any gap-bound-only claim.
- Gives the run two **explicit small counterexample-shape witnesses** (2,3,13; every-sixth
  prime) that any proposed invariant must not rule out as impossible — the parity-only
  traps.
- The locality statement (row r leading entry depends only on first r+1 terms) is the same
  light-cone fact the run's own reduction uses; stated independently here.
- Claims the run should record: **parity-wave theorem**, **{0,d}-closure double edge**,
  **2-separation as the operative randomness hypothesis**, **decay-rate lower bound
  log(n+e)** (sourced here as a CHT result; CHT is also in the library).

## Source status

Primary-quality expository note by M. M. Ross (author of the decay-constants study), July
2026, cited by the Zenodo decay constants record. Not peer-reviewed; its theorem statements
(parity wave, closure, locality) are elementary and independently checkable; its literature
claims (CHT theorems, Eppstein) agree with sources already in this library.