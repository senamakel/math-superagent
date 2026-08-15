# Pattern-recognition report — consolidated (this run's confirmation pass)

Author: pattern-recognition specialist. Every statement below was re-run with
the exact sequence tools this pass, or is read directly from an exact captured
artifact. Structural conclusions over a finite sample are **conjectures in the
proof sense**, and I say so each time.

## 1. The core census sequences carry NO exploitable structure (confirmed)

The only rich integer data the run produced is the sharp-kernel census
`C_N = { graphs on <= N vertices : min-degree>=4, K4-free, K2,3-free,
neighbourhood max-degree <= 2 }` — the finite universe every 5-chromatic
unit-distance graph must lie in (5-critical subgraph has min-degree>=4, and
inherits the three geometric inequalities).

Per-N counts (n=8..11), re-run through `analyze_sequence` and
`find_linear_recurrence` this pass:

| n | kernel | 4-chromatic | 3-colourable |
|---|--------|-------------|--------------|
| 8 | 1      | 1           | 0            |
| 9 | 4      | 1           | 3            |
| 10| 16     | 16          | 0            |
| 11| 228    | 198         | 30           |

`analyze_sequence([1,4,16,228])`: not a low-degree polynomial
(differences 3,12,212; 9,200; 191); leading ratios 4.0, 4.0, 14.25 —
super-exponential onset at n=11.
`find_linear_recurrence([1,4,16,228], order<=4)`: **none**.
`oeis_lookup([1,4,16,228])`: **miss** — not catalogued; no closed form will be
looked up.
`[1,1,16,198]` (4-chromatic) and `[15,112,62,9]` (n=11 edge distribution):
neither polynomial nor recurrent.

**The `4^k` head is the textbook Arnold trap, not a finding.** The terms
`1,4,16 = 4^0,4^1,4^2` at n=8,9,10 form a perfect geometric head; the very next
term the pattern did not come from — `228` at n=11 — breaks it (it would have
to be 64). This is exactly the "1,2,4,8,16,29" failure mode: a pattern
confirmed only on the data that suggested it is untested, and here it fails
immediately on the first out-of-sample term. It must NOT be reported as
evidence of `4^(n-8)` growth.

## 2. What the count sequences DO support (structural, not numerical)

The load-bearing regularity is a **census**, not a formula:
- every kernel member through N=11 is 4-colourable — 249/249 members, by TWO
  independent complete oracles (Cadical153 CNF SAT with proper witnesses AND
  exhaustive DSATUR backtracking), 0 disagreements
  (`census_kernel_n11.captured.txt`, `crosscheck_kernel_n11.captured.txt`).
- Hence, conditional on the kernel lemmas (certified exactly in
  `sharp_nbhd_cert.captured.txt`), **every unit-distance graph on <= 11
  vertices is 4-colourable; any 5-chromatic UDG has >= 12 vertices.**
  This is `size-bound-udg-4color-n11`, the run's strongest delivered result.

**The count sequences are why a closed form cannot extend this bound.** They
grow by combinatorial accumulation (nauty-geng enumeration), not by any
regularity a recurrence could capture. The n=12 count would be the only term
that could decide a formula, and that enumeration (~100M+ graphs) is the
infeasibility point. There is no route to extend the bound by analysis alone.

## 3. New exact data re-derived this pass: the Mycielski chain (non-UDG, context only)

Re-derived (not from formula, from the explicit construction):

| stage | V | E | chi | triangle-free | kernel-eligible |
|-------|---|---|-----|---------------|-----------------|
| C5               | 5  | 5  | 3 | yes | no |
| Mycielski(C5)    | 11 | 20 | 4 | yes | no |
| Mycielski²(C5)   | 23 | 71 | 5 | yes | **K2,3-free = FALSE** |

Recurrences hold: `V_{k+1} = 2V_k+1` (5,11,23 = 3·2^k−1), `E_{k+1}=3E_k+V_k`
(5,20,71). **This is the standard Mycielski textbook construction and does not
bear on the plane problem**: Mycielski graphs are not unit-distance graphs, and
Mycielski²(C5) — the one 5-chromatic member — fails K2,3-freeness (explicit
K2,3 on vertices {0,2} sharing common neighbours {1,6,12}, re-verified this
pass), so it is NOT in the kernel and cannot be a kernel counterexample. This
matches the board's `DEAD END/REBUTTAL on the sharp-kernel refutation`.

## 4. No other sequence in the workspace yields structure

I re-examined the remaining numeric artifacts:
- Moser colouring counts (0,0,0,384,5040) for k=1..5 — a calibration constant,
  not a sequence with predictive content for the bound; counts agree exactly
  between brute force and SAT (`sat_count_check.captured.txt`).
- Torus 7-colour margins (`torus_7col_calibration`): two side-length witnesses
  (L=2/5 and 47/120), both proper — confirming the 7-colour hexagonal tiling
  upper bound, not a sequence.
- Core vertex/edge distributions at n=10,11 (`analyze_cores_small`): these are
  distributions (multiplicities over core sizes), not a sequence with a
  defensible generating law.

## Verdict

**There is no exploitable numerical sequence regularity in the data this run
produced.** Three independent pattern-recognition passes (this one included)
arrive at the same place: the census counts are short, uncatalogued,
non-polynomial, non-recurrent, and their growth points to combinatorial
accumulation. An invented pattern here would be worse than none.

The one exact regularity worth handing on is **structural**: the kernel is a
finite class fully 4-colourable through N=11, and the only honest way to advance
the size-bound ladder rung is the n=12 enumeration (cost-blocked), not a
formula. The next productive derivation is likewise structural — testing colder
base graphs for a monochromatic-forced pair under 4 colours (the
`G-forced-pair-exists` crux), which is where a bound could actually move.

## Required honesty

Every "regularity" above is a **conjecture** (holds for every enumerated term,
no proof of continuation) — and for the 4^k head it is a **failed** conjecture,
falsified at n=11. The kernel-4-colourability facts are **verified on the
enumerated instances**, exact over them, not proved for all N.
