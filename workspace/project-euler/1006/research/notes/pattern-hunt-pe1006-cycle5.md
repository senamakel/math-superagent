# PE1006 pattern-hunt, cycle 5 — exact S1 within-run structure (d_j = A019587)

Verified EXACTLY over k = 1..3000 (1145 proper V-runs) by exact integer
arithmetic; no floats. All numbers come from the recorded
`code/out/s1_exact.txt` and `code/out/vR_exact.txt` (produced by
`code/pattern_hunt/verify_R_runs_wythoff.py`). Every regularity below is a
computational conjecture (verified), not a proof — except where marked.

## 1. S1 jumps by a pure power of ten at each V-run start  [NEW, exact]

Recall the k-step recurrence of the committed route:

    Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k),
    J(k) = 1 + floor((k+1)/phi^2),   S1(k) = sum_{w in F_k, w*'1' in F_{k+1}} V(w).

V(R_k) is constant on runs [s_j, s_{j+1}-1] with s_j = floor(j*phi^2) =
upper Wythoff (A001950).  NEW: on each such run S1 is flat from s_j+1 to
s_{j+1}-1 and jumps at s_j+1 by exactly

    S1(s_j+1) - S1(s_j) = d_j * 10^{s_j},   d_j a positive integer,

i.e. S1 on the run is  A_j at k=s_j,  A_j + d_j*10^{s_j} for s_j<k<=s_{j+1}-1.
Verified for all 1145 proper runs (S1(s_j+1)-S1(s_j) divisible by 10^{s_j}
with quotient d_j, and S1 flat on [s_j+2, s_{j+1}-1]).

Program: `code/pattern_hunt/check_dj_structure.py`, `check_s1_runstructure.py`;
outputs `code/out/dj_raw.txt` (j, d_j), `code/out/dj_mod.txt` (j, d_j mod M).

## 2. d_j is exactly OEIS A019587 (left budding)  [NEW, exact, sourced match]

Extracted d_j (j = 1..1145) equals the catalogued sequence A019587:

    d_j = #{ i : 0 < i <= j  and  0 < {phi*i} <= {phi*j} },  phi = (1+sqrt5)/2,

the "left budding sequence".  Verified TERM-BY-TERM over all 1145 runs by
direct high-precision (80-digit) fractional-part comparison, which is exact
here because phi is irrational and i <= 1145 (distance to nearest integer
>= 1/(2*phi*1145+2) >> 60-digit error).  Program:
`code/pattern_hunt/check_dj_oeis.py`.

Consequence: A019587 has a known O(log n) evaluation via a Zeckendorf
(Fibonacci) linear representation (Shallit 2025, in the OEIS entry), so a
single S1(k) can be located (binary search over the Beatty s_j) and evaluated
as S1(s_j) + d_j*10^{s_j} mod M.

## 3. Within-run Psi increment is closed-form in (s_j, L_j, V_j, A_j, d_j)  [VERIFIED]

The sum of [100 V(R_k)^2 + 20 S1(k) + J(k)] over k = s_j..s_{j+1}-1 equals the
closed expression using only the five run parameters (plus a prefix sum of J).
Verified exactly for all 1145 runs.  This makes the run-decomposition of Psi
exact but does NOT by itself yield O(log) for the whole recurrence at k=10^18:
V_j and A_j across runs have no catalogued closed form (mod M they are
noise-flat; find_linear_recurrence order<=12 fails on V_j mod M, A_j mod M,
d_j, run-gaps).  So the room's committed universal-Euclidean O(log) route is
still the right one; this S1 structure is a cross-check on the S1 floor-sum
object, not a replacement.

Program: `code/pattern_hunt/check_runsum_increment.py`.

## Refuted companion hypotheses (recorded dead ends, do not revive)

- S1(s_j) does NOT always have s_j decimal digits: len(S1(34)) = 35, so the
  "len(S1(s_j)) == s_j" claim is false (holds only for early runs).
- S1 does NOT left-append a single digit within a run (y = d*10^len + x).
  Holds only for the first ~12 runs; fails at run j=13 (k=34).
  Programs: `check_s1_leftappend.py`, `check_s1_inrun.py`.
- Across-run V_j, A_j mod M: no constant-coefficient linear recurrence of
  order <= 12, not polynomial (exact-tool verdicts).  Same negative result
  already recorded for Psi(k) mod M itself and its Fibonacci-indexed
  subsequences.

## Files (this cycle)

- code/pattern_hunt/check_dj_structure.py — extracts/verifies the d_j*10^{s_j} jump.
- code/pattern_hunt/check_dj_oeis.py — verifies d_j == A019587 over 1145 runs.
- code/pattern_hunt/check_s1_runstructure.py — verifies the 2-piece S1 structure per V-run.
- code/pattern_hunt/check_runsum_increment.py — verifies the closed-form run increment.
- code/pattern_hunt/check_s1_leftappend.py, check_s1_inrun.py — recorded refuted conjectures.
- code/out/dj_raw.txt, code/out/dj_mod.txt — the extracted d_j sequences.
