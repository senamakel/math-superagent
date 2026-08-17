# PE1006 pattern-hunt, cycle 3 — new exact regularities (findings from the exact sequence tools)

Memory (Cognee/scratch) server was down this cycle; findings stored to disk.

All findings below were verified EXACTLY (exact integer/rational arithmetic),
over the stated ranges, by the scripts in `code/pattern_hunt/`. Each is a
conjecture (computationally verified), not a proof — with one exception, the
right-extension recurrence, which has a direct proof from the definition.

---

## 1. Right-extension (Sturmian) recurrence for Psi(k)  [NEW — load-bearing]

Every length-k factor set F_k has **exactly one right-special factor** R_k
(a length-k factor that has BOTH '0' and '1' as right extensions),
and every other factor has exactly one right extension. The extension sets
satisfy the exact set identity

    F_{k+1} = { w.b : w in F_k, b in ext(w) }.

Since V(w1) = 10·V(w)+1 and V(w0) = 10·V(w), letting
J(k)  = #{ (w,b) : b='1' right extension of w },
S1(k) = sum_{that set} V(w),
one gets the exact recurrence

    J(k)      = # length-(k+1) factors ending in '1' = c1(k+1) = 1 + floor((k+1)/phi^2)
    Psi(k+1)  = 100·Psi(k) + 100·V(R_k)^2 + 20·S1(k) + J(k)

**Verified exactly k = 1..40 (strong, exact, from the string oracle),
and mod M k = 1..400.** The closure J(k)=c1(k+1) also verified k=1..400
against the three-way c1 formula.

Why load-bearing: it is a recurrence in k with only polynomial-in-k
coefficients and simple additive corrections (V(R_k), S1(k), J(k)). The
exact tools confirm the general negative finding — no constant-coefficient
linear recurrence exists for Psi(k) mod M (order ≤ 12) or for its residues —
because the coefficients themselves grow with k. The work of an O(log) method
for k=10^18 is reduced to evaluating the corrections; S1(k) and V(R_k) are
the objects a solver must make O(log) (they are geometric floor-sums over the
mechanical word, cf. directive 2's route).

## 2. Pair-correlation Toeplitz defect is bounded by 1  [NEW, exact]

C(i,j) = #{ w in F_k : w_i = w_j = '1' } (1-indexed).
Toeplitz defect d(i,j) = C(i,j) - C(i-1,j-1), 2 ≤ i,j ≤ k.

Verified exactly for k = 1..400:

  (a) every nonzero defect has |d| = 1  (never |d| ≥ 2);
  (b) the matrix is fully Toeplitz (all defects 0, position-independence,
      the condition under which directive 1's lag-sum reduction holds)
      EXACTLY at k = 1,2,4,7,12,20,33,54,88,143,232,376 = F_n - 1.

This re-confirms under the exact tools that the pair-correlation /
autocorrelation route (directive 1) is valid only at k = F_n - 1, and adds
the new exact fact that at general k the deviation from translation-
invariance is bounded by 1 in every cell.

## 3. Right-special factors form constant-value runs (structure, unfinished)

V(R_k) is constant on runs whose lengths are only 2 or 3 (k=1..400: 154 runs,
histogram {3:94, 2:58, 1:2}). Run starts include the Fibonacci numbers
1,2,5,13,34,89,233,...

**Refuted hypothesis:** within a constant-value run it is NOT the case that
R_{k+1} = '0' + R_k (string check failed at every k). The constant-value
runs are not simple 0-prefix extensions. This rule must NOT be propagated.

## Negative results re-confirmed by the exact tools

- Psi(k) mod M, k=1..400: no constant-coefficient linear recurrence of
  order ≤ 12; not a low-degree polynomial; residues at Fibonacci indices
  (F_n, F_n−1, F_n+1) have no constant-coefficient recurrence either. All
  three Fibonacci-indexed residue subsequences fail find_linear_recurrence.
- ndef(k) = # nonzero Toeplitz-defect cells (k=1..400, written to
  code/out/topelitz_defects.txt): root sequence = 0,0,2,0,2,8,0,18,10,16,32,
  0,32,48,18,72,40,64,98,0,128,... NOT in OEIS (miss recorded).
- V(R_k) mod M and S1(k) mod M (saved): noise-flat / no catalogued form.
- exact Psi(1..25) too large (> 64-bit) for the sequence tools beyond k=10.

## Files (this cycle)

- code/pattern_hunt/check_ext_recurrence.py — exact recurrence, k=1..40.
- code/pattern_hunt/check_ext_recurrence_400.py — mod-M recurrence and
  Toeplitz probe, k=1..400; writes code/out/extrecur_res.txt.
- code/pattern_hunt/check_R_runs.py — run structure of R_k and S1(k);
  writes code/out/s1_res.txt, code/out/vR_res.txt.
- code/pattern_hunt/check_toeplitz_defect.py — full Toeplitz-defect scan
  k=1..400; writes code/out/topelitz_defects.txt.
- code/out/ext_recurrence.txt — (k, V(R_k), J, P1(k+1), S1(k)) k=1..40.
