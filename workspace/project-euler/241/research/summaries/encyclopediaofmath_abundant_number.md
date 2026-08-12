# Encyclopedia of Mathematics — Abundant number

Source: https://encyclopediaofmath.org/wiki/Abundant_number — `[[encyclopediaofmath_abundant_number.full]]`

## What it establishes

Standard definitions and classical history of the abundancy trichotomy:

- n is **abundant** if σ(n) > 2n, **deficient** if σ(n) < 2n, **perfect** if
  σ(n) = 2n (some authors use σ(n) ≥ 2n for "abundant", including perfects).
- History: Nicomachus (~100) classified even numbers; Boethius (~500) repeated
  it; Jordanus (~1236) proved (correctly) that **every multiple of a perfect or
  abundant number is abundant** — this is the monotonicity I(kn) ≥ I(n) in its
  earliest specific form (only the "abundant" side, not the full index
  monotonicity of Laatsch).

## Relation to PE 241

- The hemiperfect condition σ(n)/n = k + 1/2 sits strictly between perfect
  (σ/n = 2) and abundant (σ/n > 2) for k ≥ 2 (7/2, 9/2, 11/2 all exceed 2, so
  every such hemiperfect n is abundant; 3/2 and 5/2 are deficient).
- The Jordanus result is a remote ancestor of the run's monotonicity pruning
  (a completion n' of a partial n with I(n) ≥ T is impossible if I(n) > T, and
  I(kn) ≥ I(n)), but the EoM article proves nothing the run uses that Laatsch
  (claim `laatsch-multiplicativity-density`) does not establish exactly.
- No enumeration technique, no bound, no half-integer-abundancy content.

## Verdict

**Does not help the solver** beyond background: it is the classical history of
abundance, all of which is subsumed by sourced claims already on disk
(`property22-denominator-divides`, `laatsch-multiplicativity-density`).
Nobody needs to re-read it for the DFS method or the answer sum.

Does not contradict anything in the library (agrees with the evenness lemma:
Jordanus's "all abundant numbers are even" conjecture was false — odd abundant
numbers exist, e.g. 945, which is why hemiperfect evenness must use parity of
σ(n)/n, not abundance).