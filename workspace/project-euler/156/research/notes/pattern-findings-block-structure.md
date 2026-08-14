# Pattern findings on PE156 fixed-point data

```claim
id: R1-block-decomposition-verified
statement: >
  For every digit d=1..9, S_d = {n : f(n,d)=n} decomposes exactly into d
  blocks of size 10^10: S_d = ⨆_{k=0..d-1} {k·10^10 + x : x ∈ S_d ∩ [0,10^10)}.
  Equivalently every solution is k·10^10 + x with x<10^10 a block-0 solution,
  and every translate of a block-0 solution by k·10^10 (k=0..d-1) is a
  solution. Per digit: |S_d| = d·N0(d), s(d) = d·S0(d) + d(d-1)/2·10^10·N0(d),
  with N0 = [84,7,12,12,1,12,7,43,1] and S0 = [22786974071, 1868991481,
  4215999875, 5499999885, 0, 105783999905, 58131008510, 409040935919, 0].
hypotheses: f(n,d) counts digit d in the decimal writings of 0..n; solution
  files code/out/solutions-d{d}.txt are the run's verified complete sets.
holds-here: yes
status: checked (verified over complete data: code/pattern_block_structure.py
  checks B1-B4 by exact set equality on all 681 solutions of the nine files;
  mechanism R2 (residue identity) checked exhaustively for m<=4 and sampled
  for m=5..12 by code/pattern_residue_exact.py, 1,263,960 checks, 0 fails;
  a deductive proof of R2 is sketched in this note from the sourced
  place-value identity G1-digit-count-closed-form, so R1+R2 is a conjecture
  with a proof sketch, not a proven theorem).
bearing: >
  Exploitable structure: the entire search reduces to finding the small
  (block-0) solutions in [0,10^10) per digit; blocks 1..d-1, s(d) and the
  grand total 21295121502550 follow in closed form. This is the structural
  fact that makes the bound d·10^10 harmless.
anchor: research/notes/pattern-findings-block-structure.md
```

What this note reports, and the evidence behind each claim. All outputs are
exact (integer/rational), no floating point anywhere in this analysis.

## Data

The run computed complete solution sets S_d = {n : f(n,d)=n} for every digit
d = 1..9, stored one per line in `code/out/solutions-d{d}.txt`
(84+14+36+48+5+72+49+344+9 = 681 solutions including 0). These files were
produced by `code/solution.py` (jump iterator + place-value f) and agreed,
set-for-set, with the independent second route `code/verify.py` and with the
brute-force oracle on every reachable case; the per-digit counts equal OEIS
A130432. This pattern analysis treats the files as the ground-truth data.

## Regularity R1 — block decomposition (holds EXACTLY on every one of the 681 solutions)

For every digit d = 1..9, with B = 10^10:

  S_d  =  ⨆_{k=0..d-1}  { k·B + x : x ∈ S_d ∩ [0, B) }

i.e. the whole solution set is the union of d blocks, block k being an exact
translation of the block-0 (small) solution set by k·B. Equivalently:
every solution of f(n,d)=n is `k·10^10 + x` with the same small x solving
f(x,d)=x, and conversely every such translate is a solution.

Verified by `code/pattern_block_structure.py` (exact set-equality per block,
all digits): **B1 (set equality), B2 (k·B ∈ S_d ⟺ k ≤ d−1), B3 (|S_d| = d·N0),
B4 (s(d) = d·S0 + d(d−1)/2 · B · N0) all True for d=1..9** over the complete
files.

Derived sequences (d = 1..9), computed exactly from the files:
- N0(d) = number of block-0 solutions = [84, 7, 12, 12, 1, 12, 7, 43, 1]
- S0(d) = sum of block-0 solutions = [22786974071, 1868991481, 4215999875,
  5499999885, 0, 105783999905, 58131008510, 409040935919, 0]

Consequences:
- |S_d| = d·N0(d) — confirms the OEIS A130432 remark that the per-digit
  counts are divisible by d (84=7·12? no: 84 = 1·84, 14 = 2·7, 36 = 3·12,
  48 = 4·12, 5 = 5·1, 72 = 6·12, 49 = 7·7, 344 = 8·43, 9 = 9·1).
- The closed form s(d) = d·S0(d) + d(d−1)/2 · 10^10 · N0(d) reproduces every
  s(d) and the grand total 21295121502550 (B4 True; also re-derived by
  `code/pattern_sumcheck.py` earlier in the run).

## Regularity R2 — the residue identity (conjecture; the mechanism of R1)

For 1 ≤ d ≤ 9, 1 ≤ k ≤ d−1, m ≥ 1 and every 0 ≤ x < 10^m:

  f(k·10^m + x, d) − f(x, d)  =  k·m·10^(m−1).

At m = 10 (the problem's block size) the increment RHS is exactly k·10^10, so
f(n,d) − n is invariant under n ↦ n + B within blocks 0..d−1, which is why
the fixed-point sets are exactly translation-invariant (R1).

Status: **conjecture, verified by `code/pattern_residue_exact.py`** —
- E1: m=1,2,3 EXHAUSTIVE over every x, raw string-counting f (definition
  level, no closed form): 39,960 checks, 0 failures.
- E2: m=4 EXHAUSTIVE over every x, place-value closed form: 399,960 checks,
  0 failures.
- E3: m=5..12, 3000 random x per (d,k): holds on every sampled x.
- Total 1,263,960 checks, 0 failures.
Controlled break at k = d: f(d·10^10 + x, d) − f(x, d) − d·10^10 = x + 1
holds on 200 sampled x per d — so the translation invariance genuinely stops
at k = d−1 (this is the mechanism of the bound n ≤ d·10^10).

**A proof sketch (now a derived fact, not just sampled):** place-value
decomposition. Write f(n,d) = Σ_i c_i(n,d) where c_i is the count contributed
by the 10^i-place digits of 0..n, and split the positions above the top of
x (the new leading digit k, and the positions that were 0 in x). Writing
n = k·10^m + x with 1 ≤ k ≤ d−1 ≤ 9, position m has digit k < d and higher
positions are 0, so by the standard identity the added contribution from
position m is k·m·10^(m−1) and all higher positions add 0 while lower
positions are unchanged — giving exactly k·m·10^(m−1). This is the classical
per-position digit-count identity (claim `G1-digit-count-closed-form` in the
ledger); the deduction is exact.

## Tool outputs (exact statements, all conjectures over their terms)

- `analyze_sequence` on the full 84-term d=1 list: not a low-degree
  polynomial; leading ratios collapse to 1.0000 after a few terms (block
  structure qualitatively confirmed by the tool); residues mod 5 repeat with
  period 42 — no clean polynomial fit.
- `analyze_sequence` on the 43 block-0 d=8 solutions: same qualitative
  picture (runs of consecutive integers, first-level differences 1 inside
  runs).
- `find_linear_recurrence` (order ≤ 12) on N0(d) = [84,7,12,12,1,12,7,43,1]:
  **no** constant-coefficient linear recurrence of order ≤ 12 fits. N0 is
  not C-finite. (9 terms is also short; the no-fit is exact over them.)
- `oeis_lookup` on N0(d) = [84,7,12,12,1,12,7,43,1]: **no match** — the
  block-0 count sequence is not catalogued.
- `oeis_lookup` on S0(d) (7 block-0-sums given): **no match** — not
  catalogued.
- The run-count sequence [20,7,3,3,1,3,7,11,1] (number of consecutive runs
  in block-0 sets) is not polynomial; not sent to OEIS (very short, and the
  two decisive misses above already bound the search).

## Why N0/S0 have no structure the tools can find

N0(d) is dictated by where the small solutions of f(n,d)=n land in [0,10^10).
Those solutions are not digit-arithmetic objects in any fixed pattern — the
d=1 set alone contains six runs of ten, ten pairs and four isolated numbers
(confirmable from the b0 runs: {1:4, 2:10, 10:6} for d=1), and the block-0
counts are 84, 7, 12, 12, 1, 12, 7, 43, 1 with no evident law. The
exploitable structure is not in N0/S0 but R1+R2: once the small set S_d∩[0,B)
is known, EVERYTHING else (all blocks up to d−1, s(d), the grand total) is a
closed-form consequence. No enumeration up to the bound is needed at all.

## Status summary

- R1 (block decomposition): **holds over the complete solution data — every
  one of the 681 solutions; exact.**
- R2 (residue identity): holds over 1,263,960 checks including exhaustive m≤4;
  a deductive proof is written above from the sourced place-value identity —
  so R1 is a theorem given R2, and R2's proof is standard. Both labeled
  conjecture-with-strong-evidence unless/until a checker certifies the proof.
- OEIS misses recorded: N0(d) and S0(d) are not catalogued sequences.