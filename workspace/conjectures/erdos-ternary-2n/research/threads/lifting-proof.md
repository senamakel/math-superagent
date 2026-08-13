```thread
question: Is the 2-to-1 lifting of A_k provable via LTE, giving |A_k| = 2^(k-1) unconditionally?
status: live
rests-on: ternary-sieve-count-doubles (checked k <= 22), 2^{2·3^(k-2)} ≡ 1 mod 3^(k-1) (standard LTE)
blocked-by: verifying c = (2^{2·3^(k-2)} - 1)/3^(k-1) mod 3 is nonzero
next: compute c for small k; verify v_3(2^{2·3^(k-2)} - 1) = k-1 exactly
```

# Proving the 2-to-1 lifting

## The claim to prove

`A_k = { r mod 2·3^(k-1) : low k ternary digits of 2^r mod 3^k avoid 2 }`.

Data (`code/out/sieve_Ak.captured.txt`, `code/out/sieve_cannot_close.md`):
`|A_k| = 2^(k-1)` for every k = 1..22, computed by lifting. Each class in
`A_k` lifts to three candidates in `A_{k+1}`, and exactly two survive.

## The LTE sketch (asserted by operator, not yet verified)

Adding `j·2·3^(k-2)` to the exponent multiplies `2^r` by
`(2^{2·3^(k-2)})^j`. LTE should give

    2^{2·3^(k-2)} ≡ 1 + c·3^(k-1) (mod 3^k)   with 3 ∤ c.

Then the three lifts `r, r+2·3^(k-2), r+2·2·3^(k-2)` give top ternary digits
`d, d+c, d+2c mod 3`; exactly one of those is 2, so exactly two survive.

## What must be checked before this is "proved"

1. `v_3(2^{2·3^(k-2)} - 1) = k-1` exactly (this is LTE on the base `2^2 = 4`,
   whose order mod 3^k is 3^(k-1)).
2. The quotient `c = (2^{2·3^(k-2)} - 1)/3^(k-1)` satisfies `c ≢ 0 (mod 3)`.
3. The digit-shift step: the top digit of `x·(1 + c·3^(k-1))` mod 3^k is the
   top digit of `x` plus `c` times the leading term — must be written down
   carefully, since the addition can carry into the top digit.

If any of these fails, the mechanism is wrong even though the data is right —
find the real mechanism.

## Status

- Data: checked, exact, k = 1..22.
- Mechanism: sketch only. Not verified. Not proved.
