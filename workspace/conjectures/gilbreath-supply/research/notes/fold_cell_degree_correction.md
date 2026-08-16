# Fold cell degree correction (O'Donnell digest)

## The error found

The newest digested source (`research/summaries/odonnell_analysis_boolean_functions.md`)
and its claim block `odonnell-boolean-fourier-degree-k-toolkit` both stated that each
fold cell is a "Walsh object of **degree = popcount(d)**".

That is wrong by an exponential. The canonical floored cell is

    T(n,d) = XOR_{o ⊆ d} h[n−1−d+o]

The `o` range over **all binary submasks of `d`**, and there are exactly
`2^popcount(d)` of them (each set bit of `d` is present or absent in `o`). They map
injectively to distinct positions (adding the constant `n−1−d` preserves distinctness),
so the cell is the parity (XOR) of `2^popcount(d)` distinct bits, i.e. a Walsh
character of **degree `2^popcount(d)`** — a power of two, not `popcount(d)`.

## Hand verification (independent of any run)

- n=8, d=3: submasks of 3 = {0,1,2,3}; positions 4+{0,1,2,3} = {4,5,6,7} → 4 bits = 2^2 = 2^popcount(3). (popcount(3) = 2 ≠ 4.)
- n=8, d=2: submasks of 2 = {0,2}; positions 5+{0,2} = {5,7} → 2 bits = 2^1 = 2^popcount(2). (popcount(2) = 1 ≠ 2.)

So even at d=2 the claimed "degree = popcount(d) = 1" misses 1 bit.

```claim
id: fold-cell-degree-is-2^popcount
statement: >
  The fold cell T(n,d) = XOR_{o⊆d} h[n−1−d+o] is a parity (Walsh character) over
  2^popcount(d) distinct h-positions (the 2^popcount(d) binary submasks of d,
  injectively shifted), so its multilinear degree is 2^popcount(d) — a power of
  two — NOT popcount(d) as the O'Donnell digest originally claimed. The correlation
  / gram order of a cell, i.e. the number of distinct bits it XORs, is
  2^popcount(d), which runs up to the largest power of two ≤ n−1 (≥ n/2).
hypotheses: canonical floored fold, d ∈ [2,n−1]; submask-XOR cell (problem.md facts 1–2).
holds-here: yes — pure combinatorics of Φ_n, no primes.
status: proved by hand (per-submask injectivity; two explicit cases d=2,3 at n=8
  verified in the witness note); program code/scholar/cell_degree_check.py handed
  to tool_builder/coder as an independent mechanical confirmation (NOT yet run here).
bearing: >
  Fixes a factual error in the newest digest. The correction STRENGTHENS the
  reopened budget: cells reach correlation order ~n/2 (the measured K*(n) ≈ n/2),
  consistent with `collapse-witness-n8-kstar-ge-2`; it does not change the main
  conclusion (O'Donnell is machinery for a route; the arithmetic input on the
  prime string is still the open part).
contradicts: odonnell-boolean-fourier-degree-k-toolkit (as first written; the
  claim block and digest prose are corrected in place)
anchor: research/summaries/odonnell_analysis_boolean_functions.md (corrected);
  code/scholar/cell_degree_check.py (handed off, not run)
```

## Consequence

This is a genuine new finding this pass: a claimed structural fact in the newest
library addition was wrong, and correcting it (degree `2^popcount(d)`, not
`popcount(d)`) *reinforces* rather than weakens the reopened pass's measured budget
`K*(n) ≈ n/2`. No other source uses the "degree = popcount(d)" phrasing (grep: only
the odonnell summary and its claim block).
