# Exact self-similar recursion for the Mersenne ν₂ affine constants

**Pattern-finder finding. Verified-numerically (conjecture, not proved).**

## Object

2-then-odds sequence with gap `q_{m+1}-q_m = 2` if bit else `4`, bit word =
**tail-1 word** `[0]*(P-1)+[1]` of Mersenne period `P = 2^k − 1`. ν₂(n) = #2s
in the maximal `{0,2}` suffix of the right diagonal δ(q_n).

`dyadic-oddfactor-affine-modulus-lifting.md` established ν₂ is **per-residue
affine** mod L = P: ν₂(n+P) − ν₂(n) = c_r (constant per residue r mod P). This
note gives a new, cleaner structural fact: an **exact self-similar recursion**
for the halved constant array `A_k[r] = c_r/2` (length 2^k−1) that generates
the entire array for every k, sharper than the previously documented
`Σc_r = 3^k − 3` and value-1-position facts.

## The recursion (conjecture)

Write A_k = (c_0/2, …, c_{2^k−2}/2), the length-(2^k−1) array. Then

    A_{k+1}[0] = 1
    A_{k+1}[1] = 2^k − 1
    A_{k+1}[i] = 2·A_k[i]                for 2 ≤ i ≤ 2^k − 2
    A_{k+1}[2^k − 1] = 2
    A_{k+1}[2^k]     = 1
    A_{k+1}[2^k + 1] = 2^{k−1}
    A_{k+1}[2^k + 2 + j] = A_k[2 + j]    for 0 ≤ j ≤ 2^k − 3

i.e. `A_{k+1} = [1] ++ [2^k−1] ++ (2·A_k[2:]) ++ [2, 1, 2^{k−1}] ++ A_k[2:]`.

## Verification — exact at every computed size, two independent routes

The recursion generates A_3 … A_10 (P = 7 … 1023) exactly:

| k | P | len | Σ(c_r/2) = (3^k−3)/2 | recursion matches |
|---|-----|-----|----------------------|-------------------|
| 3 | 7   | 7   | 12                   | yes |
| 4 | 15  | 15  | 39                   | yes |
| 5 | 31  | 31  | 120                  | yes |
| 6 | 63  | 63  | 363                  | yes |
| 7 | 127 | 127 | 1092                 | yes |
| 8 | 255 | 255 | 3279                 | yes (out-of-sample: predicted then recomputed) |
| 9 | 511 | 511 | 9840                 | yes (out-of-sample) |
| 10|1023 |1023 | 29523                | yes (out-of-sample) |

Every array was independently computed from a **from-scratch literal full
triangle** (build A_0 = q, iterate |a−b|, read the right diagonal, count the
{0,2}-suffix) — no `lib.rightdiag` dependency — over windows of width
P ≤ 1023, n ≈ 11,000 (affinity stable there; smaller windows for small P).
The recursion for k=8,9,10 was predicted from the recursion and then
verified against the fresh literal-triangle computation = true predictive
(out-of-sample) tests, not just reproduction of the data that suggested it.

Consistency with known facts:
- `Σ_r c_r = 2·Σ(A_k) = 3^k − 3` — recovers the documented closed form
  (OEIS A058809).
- The value-1 positions are `{0, 2^k − 2^j : 1 ≤ j ≤ k−1}` — the documented
  partial-sums law; the recursion produces exactly these.
- Every non-1 entry of A_k is a power of 2 (A_k[1] = 2^{k−1} − 1 is the sole
  non-power-of-2), so min c_r = 2, giving `ν₂(n) ≥ 2n/P − O(1)` positive
  linear supply.

## Scalar sum recurrence and closed form

The per-`k` sums `S_k = Σ_r (c_r/2)` themselves satisfy the affine recurrence

    S_k = 3·S_{k-1} + 3    (with S_3 = 12),

whose closed form is

    S_k = (3^k − 3)/2.

Every one of the eight verified rows — 12, 39, 120, 363, 1092, 3279, 9840,
29523 — equals both `3·(previous) + 3` and `(3^k − 3)/2`. A one-step recurrence
with a closed form is strictly stronger than the matched table: it is a
prediction for every `k`, not a catalogue of the rows already computed.

## Status / caution

**Verified-numerically, conjectural**, exact over P = 7 … 1023. This is a
*periodic-family* (Mersenne tail-1 word) structural statement; it does **not**
close G-supply for the aperiodic primes (`abgs-2011-s9-mod4-switch-limit-open`
stays the open hypothesis). The recursion itself is a clean closed-form family
with no prior matching the exact per-array concatenation law — this note is a
genuine sharpening of `dyadic-mersenne-affine` / `dyadic-oddfactor-affine-modulus-lifting`.
The first term that would falsify the recursion is the first index where the
literal-triangle c_r/2 array for P=2^k−1 differs from the recursion's
prediction; none found through k=10 (P=1023).

## Files
- `code/pattern_finder/dyadic_mersenne_constants.py` (+ captures): the arrays.
- `code/out/mersenne_recursion_verify.py`: recursion vs arrays (k=3..7).
- `code/out/mersenne_literal_indep.py`: literal-triangle independent check (k=3..7).
- `code/out/mersenne_recursion_falsify.py`, `_k9.py`, `_k10.py`: out-of-sample
  prediction tests for k=8,9,10.

```claim
id: mersenne-nu2-affine-selfsimilar-recursion
statement: For the Mersenne tail-1 word of period P = 2^k - 1, the halved per-residue affine constants A_k[r] = c_r/2 satisfy the self-similar recursion A_{k+1} = [1] ++ [2^k-1] ++ (2*A_k[2:]) ++ [2, 1, 2^{k-1}] ++ A_k[2:], and their sums S_k = sum_r (c_r/2) satisfy S_k = 3*S_{k-1} + 3 with closed form S_k = (3^k - 3)/2.
hypotheses: q is the 2-then-odds sequence with gap 2 iff the tail-1 bit word [0]*(P-1)+[1] has bit 1, else gap 4; P = 2^k - 1; A_k[r] = c_r/2 where c_r = nu2(n+P) - nu2(n) is the per-residue affine constant mod L = P.
holds-here: yes (periodic-family structural statement; does not close the aperiodic-prime G-supply, which stays abgs-2011-s9-mod4-switch-limit-open)
status: checked
bearing: a closed form and exact self-similar recursion for the Mersenne family's supply constants; sharper than the previously documented sum only; the recursion reproduces every verified row k=3..10 and predicts k=8,9,10 out-of-sample.
anchor: code/out/mersenne_recursion_verify.captured.txt, code/out/mersenne_literal_indep.py, code/out/mersenne_recursion_falsify.py
```
