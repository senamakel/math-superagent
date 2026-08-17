# Ceil-sequence structure: c_k = ceil(S_k) for the H(n) lower-bound family

Derived from the closed form S_k = 4^(k-1)(k - 13/6) + (2k-1)/3
(Buzzi–Novaes arXiv:2411.09594 / Li et al., degree 2k-1). The earlier
findings files covered the raw fractions and the integer subsequence S_{3j};
the ceil sequence was printed in commands.log but never analyzed. This file
closes that gap.

Program: `code/sk_ceil_structure.py` (exact Fraction arithmetic, k up to 200).

## What was verified exactly

Let c_k = ceil(S_k).

1. **Fractional part periodic mod 3, k >= 2.** From 6S_k = 4^(k-1)(6k-13) + 4k-2
   and 4^(k-1) ≡ 4 (mod 6) for k >= 2, we get 6S_k ≡ 4k (mod 6), so
   frac = 0, 2/3, 1/3 for k ≡ 0, 1, 2 (mod 3). k=1 is the exception (frac 5/6).
   Zero failures for k = 2..200.
2. **delta_k = c_k - S_k has period 3 for k >= 2**: 0, 1/3, 2/3 for
   k ≡ 0, 1, 2 (mod 3). Zero failures.
3. **c_k satisfies the constant-coefficient order-6 recurrence**
       c_{k+6} - 9 c_{k+5} + 24 c_{k+4} - 17 c_{k+3} + 9 c_{k+2} - 24 c_{k+1} + 16 c_k = 0,
   annihilator (E-4)^2 (E-1)^2 (E^2+E+1) — the least common multiple of the
   raw-S annihilator (E-4)^2(E-1)^2 and the period-3 (E^3-1)/(E-1) = E^2+E+1.
   Zero failures for k = 2..199. **Order 5 does not fit** (exact sympy
   elimination on k=2..31 fails at r=5), so order 6 is minimal.
   The `find_linear_recurrence` tool independently confirmed the order-6
   recurrence on a 12-term slice starting at k=1 — a welcome contrast to its
   false-negative behaviour on the raw S_k subsequence (see
   findings/sequence-tool-validation-sk.md).
4. **c_k = S_k exactly for 3 | k** (the guaranteed-count subsequence sits
   inside ceil at indices multiple of 3). Zero failures.

c_k for k=1..16: 0, 1, 15, 120, 729, 3929, 19802, 95579, 447835, 2053468,
9262429, 41243997, 181753182, 794121567, 3444921695, 14853428576.

## Status

Derived identity, not an independent discovery: everything follows from the
paper's closed form by the same mod-6 argument recorded in
findings/naive-oracle-verified.md and sequence-s-k-findings.md. True over
every term computed (k=2..200), minimal order established by exact
elimination. No OEIS lookup performed/needed: like the rest of the S_k
family this is fully explained by the closed form.