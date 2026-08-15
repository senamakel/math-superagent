# Relative class number of Q(zeta_p) — consecutive-prime verification

`status: checked` (exact rational arithmetic, independent of any hardcoded table)

## What this establishes

The run's earlier `minus-class-number-formula` evidence was float-only
(`N(re(h_rel),12)`) and compared against a hardcoded 9-row table at the sparse
primes {3,5,7,11,13,23,31,37,43} — which *skip* 17,19,29,41. So the formula was
not verified on a consecutive run of primes, and its "two independent routes"
were not independent.

This file supplies the missing verification:

- **Exact** arithmetic: `lib.cyclo.Cyclo` over `Fraction` coefficients, each h^-
  value pulled out by `as_fraction()`, which asserts the element is rational
  (throws otherwise). No floats anywhere.
- **Consecutive** coverage: every odd prime p <= 100.
- **Independent target**: compared against the *catalogued* sequence OEIS
  A000927 (not a table the same formula produced).

## Program

`code/hminus_full.py`, run `timeout 540 python3 code/hminus_full.py 100`
-> `code/out/hminus_full100.captured.txt`, runtime 47.7s.

## The sequence (p = 3,5,7,...,97)

```
1,1,1,1,1,1,1,3,8,9,37,121,211,695,4889,41241,76301,853513,
3882809,11957417,100146415,838216959,13379363737,411322824001
```

Match against OEIS A000927 tail (prime(2..24) = 3..97): **exact, 24/24 terms.**

Note the previously-missing primes:
- p=17,19 -> h^- = 1 (the sparse table would have ended its "all 1" run at 13;
  the consecutive run shows the trivial region extends to 19)
- p=29 -> h^- = 8   (first even value; h^- starts growing)
- p=41 -> h^- = 121

## What this means for the run

- `minus-class-number-formula` is now *exact and catalogue-verified over all
  primes p <= 100*, not float-verified at 9 sparse primes. The claim's evidence
  class is upgraded to: exact computation reproducing A000927.
- No constant-coefficient linear recurrence fits the terms (checked, order <= 8)
  and the sequence is not eventually polynomial: no recurrence shortcut to the
  minus class number exists of those simple kinds. h^- is genuinely
  multiplicative/exponential-ish in p (it grows very fast: p=97 -> 4.1e11).
- h^- = 1 for p in {3,5,7,11,13,17,19} (all odd p <= 19). h^-(29)=8 is the first
  value > 1, and the first even one.

## Caveats

- Exactness over p <= 100 is a verified-numerically claim, not a proof that the
  formula holds for all p. The Bernoulli-product formula it validates is the
  classical analytic class number formula (source: relative-class-number-
  analytic.md), still asserted-not-proved in this workspace.
- Nothing here touches the open both-odd content directly; h^- is a quantity it
  evaluates, not a theorem about it. The value of this check is that the one
  class-group number the run banks on is now exact and cross-checked against the
  catalogue.
