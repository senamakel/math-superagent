# Sequence structure: the H(n) lower-bound family S_k

Source: Buzzi & Novaes, "A note on a recent attempt..." arXiv:2411.09594, Section 2,
citing Li et al. [5] (correction of Christopher–Lloyd [2]) and Han–Li [4].

`S_k` = number of limit cycles guaranteed for the polynomial systems `PH_k` of
degree `2k−1`. Exact closed form as printed in the source:

    S_k = 4^(k−1) · (k − 13/6) + (2k−1)/3 .

## Items verified by exact arithmetic

Every claim below was checked with `Fraction` exact arithmetic (programs in
`code/sk_*.py`); none is a curve-fit. The closed form is straight from the
paper, so the structural facts follow from it directly and are verified to large
index (k up to 400, subsequence up to j=29), then the recurrence is derived from
the exact closed form.

1. **Exponential growth.** `S_k` grows like `4^k·k` — exponential in k. This is
   CORRECT and is NOT a contradiction with the paper's own assertion that
   `H(n) ~ n² log n`. The polylog bound is the *asymptotic feasibility* bound of
   a different construction; `S_k` is an explicit lower count for one family.
   Decisive corroboration: `S_k` and [3]'s claimed formula
   `4(2^k−2)(2^(k+1)−5)` cross over at exactly **k = 35**, matching the paper's
   stated contradiction threshold "k ≥ 35". So the exponential reading of `S_k`
   is the correct one.

2. **Constant-coefficient order-4 recurrence (raw S_k):**
       S_{k+4} − 10·S_{k+3} + 33·S_{k+2} − 40·S_{k+1} + 16·S_k = 0
   i.e. annihilator `(E−4)²(E−1)²`. Zero failures for k = 1..399.

3. **Integerness:** `S_k ∈ ℤ  ⇔  3 | k`.
   Proof (mod 6): 6S_k = 4^(k−1)(6k−13) + 4k−2; for k ≥ 2, 4^(k−1) ≡ 4 (mod 6),
   so 6S_k ≡ 4k (mod 6), which vanishes iff 3 | k. Verified exactly for
   k = 1..400 (k=1 gives −5/6, consistent).

4. **Integer subsequence a_j = S_{3j}:** constant-coefficient order-4 recurrence
       a_{j+4} − 130·a_{j+3} + 4353·a_{j+2} − 8320·a_{j+1} + 4096·a_j = 0
   i.e. `(E−64)²(E−1)²` (since S_{3j} = (1/4)·64^j·(3j−13/6) + (6j−1)/3).
   Verified j = 1..29.

5. **Guaranteed-count integers (k = 3,6,9,...):**
   15, 3929, 447835, 41243997, 3444921695, ...

## OEIS status

None catalogued: checked both the guaranteed-count subsequence
`[15, 3929, 447835, 41243997, 3444921695]` and raw numerators — no match. The
structure is fully explained by the closed form; nothing hidden to look up.

## What this is worth

- The recurring **misreading trap**: a per-family lower count (`S_k`, here
  exponential) must not be conflated with the asymptotic `n² log n` feasibility
  bound. This is a genuine numeric discipline result: it explains why the two
  coexist and reproduces the paper's own k=35 contradiction threshold exactly.
- These are exact integer sequences from a held primary source — the kind of
  thing the pattern tools are for. They are fully derived from the closed form,
  so no further structural conjecture is warranted.
