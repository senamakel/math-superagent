# Pattern found: the run's minus class number sequence is OEIS A000927 (exact)

Status: verified-numerically (exact rational arithmetic), a finding for the run,
not a proof of the theorem.

## What was found

The run had computed h^-(Q(zeta_p)) at the sparse primes {3,5,7,11,13,23,31,37,43}
and flagged `minus-class-number-formula` as the one unchecked, load-bearing number
— the previous "two independent routes" were both float comparisons against the
same hardcoded table. That left a real gap: the primes 17,19,29,41 were skipped,
so the sequence was never verified on a consecutive run, and the earlier evidence
could plausibly agree with a wrong normalisation on a lucky sparse sample.

I computed h^- with **exact rational arithmetic** (`lib.cyclo.Cyclo`, `Fraction`
coefficients, `as_fraction()` asserting rationality) for **every odd prime
p <= 100** and compared against the **catalogued** OEIS sequence A000927 — not
against a table the same formula produced. Exact match, 24/24 consecutive primes.

## The exact sequence (p = 3,5,...,97)

```
1,1,1,1,1,1,1,3,8,9,37,121,211,695,4889,41241,76301,853513,
3882809,11957417,100146415,838216959,13379363737,411322824001
```

New information the sparse table missed:
- h^-(17) = h^-(19) = 1  (trivial region extends to all odd primes <= 19)
- h^-(29) = 8  (first value > 1, first even value; the sparse table had no 29)
- h^-(41) = 121

## Structural facts (exact over the terms computed; conjectures beyond)

- `p | h^-(p)` exactly for p in {37, 59, 67} — the **irregular primes below 100**.
  This confirms the h^- sequence carries the p-torsion of the class group, i.e.
  the classical regular/irregular split, and therefore that the run's h^- routine
  captures the right arithmetic. (Known classical: irregular primes start at 37.
  Not a new result — a validation of this run's number.)
- No constant-coefficient linear recurrence of order <= 8 fits; not eventually
  polynomial (differences never constancy). So h^- has no recurrence shortcut of
  the simple kinds; it is genuinely near-exponential in p (p=97 -> 4.1e11).

## What this means for the run

Upgrade `minus-class-number-formula` evidence: exact + catalogue-verified over
all odd p <= 100, from this file's computation. The claim that the formula's
normalisation is right is now independently anchored (exact arithmetic, OEIS
cross-reference) rather than float-vs-own-table at 9 sparse primes.

## Caveat

Exact over p <= 100 is verified-numerically, not a proof for all p. The formula
itself is still asserted-by-source (classical analytic class number formula).
None of this touches the open both-odd content; h^- is a quantity the descent
evaluates, not a theorem about it.
