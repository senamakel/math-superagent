# collision_table.txt — what it settles

`code/no-cycle-diophantine/collision_table.py` produced
`code/out/collision_table.txt` for m = 92..200. It pairs, per m:

- **H(m)** — the exact Hercher lower bound from Corollary 24, Table 1 of the
  published JIS version
  (`research/sources/hercher-2023-no-collatz-m-cycles-jis-published.full.md`,
  lines 1188–1212). Important: the table bounds **K, the number of odd
  members**, not the minimum element x_min. The task's phrase "min element
  bound" is a conflation; the program names the column H(m)=H_K(m) and the
  source line for each row.
- **log10(threshold)** — `log10(3*log(2)) - log10(c_0) + 8.616*log10(m)`,
  c_0 symbolic, plus its value at c_0 = 1.
- **deficit** — `log10(threshold at c_0=1) - log10(H(m))`.

Hand-checked rows: m=92 → threshold 10^(0.31795 + 8.616·log10(92)) =
10^17.23794; log10(7.76e19) = 19.88986; deficit −2.65192 ✓.
m=200 → threshold 10^20.14362; log10(4.68e18) = 18.67025; deficit +1.47338 ✓.
Row boundaries per the source's "if m ≤ ··· then K > ···": 92–98 → 7.76e19
(line 1190), 99–117 → 2.74e19 (line 1192), 118–200 → 4.68e18 (line 1194).

**Finding.** The deficit grows strictly with m over 92..200: min −2.6519 at
m=92, max +1.4734 at m=200. Within a constant-H interval the threshold rises
as 8.616·log10(m); at the table step 116→117 the H-bound drops (7.76e19 →
2.74e19), pushing the deficit up again. At c_0 = 1 the Diophantine threshold
overtakes Hercher's K-bound already at m = 135 (deficit crosses zero between
m=134 and m=135), but a real c_0 < 1 subtracts log10(c_0) from every
threshold, so the crossing moves to larger m; the deficit at m=200 (+1.4734)
means the threshold exceeds H by 10^1.4734 ≈ 29.7× at the top of the range.

```claim
id: hercher-table-K-bounds-m-92-200
statement: The published Hercher Corollary 24 Table 1 (JIS 2023, lines 1190-1210) gives exact K lower bounds: m<=98: K > 7.76e19; m<=117: K > 2.74e19; m<=276: K > 4.68e18; m<=3079: K > 3.97e17; m<=12055: K > 1.30e17; m<=948987: K > 4.30e15; m<=1.14e6: K > 3.81e15; m<=1.33e9: K > 1.64e12; m<=1.54e9: K > 8.90e11; m<=9.46e9: K > 1.37e11; all m: K > 7.20e10. The table bounds K (odd members), not the minimum element x_min.
hypotheses: m-cycle of the accelerated Collatz map; X0 = 695*2^60 (Definition 4); K = number of odd members.
holds-here: yes
evidence: checked — exact integers transcribed from source lines 1190-1210; reproduced by collision_table.py; hand-checked m=92, 200, and row boundaries.
status: checked
note: research/sources/hercher-2023-no-collatz-m-cycles-jis-published.full.md
```

```claim
id: collision-deficit-grows-with-m
statement: Over m = 92..200, deficit = log10(3*log2) + 8.616*log10(m) - log10(H(m)) grows strictly with m: min -2.6519 at m=92, max +1.4734 at m=200 (c_0 = 1). At c_0 = 1 the Diophantine threshold exceeds Hercher's K-bound from m >= 135.
hypotheses: mu = 8.616 effective irrationality measure; H(m) the published Hercher K-bound; float logarithms (numerical evidence, not a proof).
holds-here: yes
evidence: checked — collision_table.py output captured at code/out/collision_table.txt; rows hand-verified.
status: checked
note: code/out/collision_table.txt
```
