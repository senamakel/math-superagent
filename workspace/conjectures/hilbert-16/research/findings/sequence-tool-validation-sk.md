# Sequence-tool validation on the S_k lower-bound family

## What I checked (independently of the run's sk_*.py notes)

Reproduced the exact terms of the Buzzi–Novaes / Li et al. lower-bound family
`S_k = 4^(k-1)(k - 13/6) + (2k-1)/3` and ran both sequence tools on them, plus
an independent exact-elimination cross-check with sympy.

## Results that stand (confirmed exactly)

- **Integer subsequence** `a_j = S_{3j}`:
  `[15, 3929, 447835, 41243997, 3444921695, 272014595425, ...]`
  satisfies the constant-coefficient order-4 recurrence
  `(E-64)^2 (E-1)^2`, i.e.
  `a_{j+4} - 130 a_{j+3} + 4353 a_{j+2} - 8320 a_{j+1} + 4096 a_j = 0`
  (coefficients `[1, -130, 4353, -8320, 4096]`).
  Verified by exact sympy elimination to j=29 and by direct annihilator check
  with zero failures to j=196. Order 3 fails at term 3, so **order 4 is
  minimal**. This matches the run's closed-form derivation.
- **Raw S_k** is fractional except k ≡ 0 (mod 3) (S_1 = -5/6, S_2 = 1/3, ...);
  S_k integer ⇔ 3|k is correct.

## The genuinely new (method-level) finding

The `find_linear_recurrence` tool is **unreliable on large, fast-growing
sequences** — it gives BOTH types of error:

1. **False negative**: on the true order-4 integer subsequence above it
   reported "No constant-coefficient linear recurrence of order 6 or less
   fits" — flatly contradicting the exact recurrence that holds with zero
   failures. (Its internal exact rational elimination apparently does not
   span enough terms to see the 4^k·k growth.)
2. **False positive**: on a 6-term slice it produced a *spurious* order-3
   fit with huge rational coefficients (1242508422/9536035, ...) that does
   NOT survive even 29 terms (order-3 fails at term 3 on the full sequence).

**Lesson**: never trust the sequence-tool recurrence verdict on sequences with
large coefficients / exponential-times-polynomial (4^k k) growth. Always
cross-check with exact elimination (sympy `solve_linear_system` or a direct
annihilator check), which is authoritative and agrees with the paper's closed
form here.

## Consequence for this run

The S_k structure (a derived closed form) is fully explained; the run's
findings file already records all of it. There is **no new integer-sequence
regularity to conjecture** from the data on disk — the selection of observed
sequences is fully derived from the closed form. The only durable contribution
is the tool-caveat above, which is worth recording so a later pass does not
build a false structure claim on a `find_linear_recurrence` fit (or miss a
true one) for an exponential lower-bound family.
