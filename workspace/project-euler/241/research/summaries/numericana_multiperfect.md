# Numericana — multiply perfect and hemiperfect integers (Michon)

Source: http://www.numericana.com/answer/numbers.htm — `[[numericana_multiperfect.full]]`

## What is in it / what it is

A large reference page (153k chars) on number theory, including the multiply-perfect and hemiperfect sections cited by Wikipedia and OEIS (abundancy 11/2, 13/2, 15/2, 17/2 tables by G. P. Michon and M. Marcus). Its main value to the library is as the source behind the A088912 / Wikipedia smallest-abundancy tables and as the citation anchor for the Marcus upper bounds on 15/2 and 17/2 hemiperfects.

## What it establishes for this run

- Confirms the hemiperfect abundance-value data already captured from A088912 / Wikipedia (smallest of abundancy k/2; Marcus's bounds for 15/2 and 17/2 ≈ 1.27e88 and ≈ 2.72e190).
- The recurrences/sections about multiplicativity of σ, abundancy, and the multiply-perfect/hemiperfect classification are background, not a bound for n ≤ 10^18.

## Does not help directly (why)

It is an encyclopedia-style reference and does not provide a proof that its tabulated "smallest" numbers are the true minima (the A088912 comment carries Robin's-theorem lower bounds, which are the load-bearing completeness argument). No computational shortcut for the run's sum. Read for the numbers, rely on A088912 for the bounds; do not treat it as an independent proof.

## Contradiction check

No contradiction with memory or with A088912: the numericana numbers agree with A088912 threshold values. (Status: corroboration, not independent proof.)
