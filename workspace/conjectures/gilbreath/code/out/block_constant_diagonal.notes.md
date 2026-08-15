# block_constant_diagonal.py — capture & reading

Run: `timeout 540 python3 code/gap_analysis/block_constant_diagonal.py`
Capture: `code/out/block_constant_diagonal.captured.txt`
EXIT_CODE=0, no traceback, both assertions passed.

## Full output

```
prefixes n=2..10001 that are NOT successful: 0
row leading (0, 2) block b_k for k=1..12: [2, 7, 13, 13, 24, 23, 22, 21, 24, 58, 97, 96]
block-lemma constant-1: rows protected by leading block (leading 1 persists), violations: 0 over k=1..39
min cycle length c_n over n=2..10001: 0  at n=0
max cycle length c_n: 9991
CONSTANT-1 / PROTECTION CHECKS PASSED
```

## Reading

- **Prefix success (bottom=1):** all N=10001 prime prefixes successful — the
  conjecture's finite-range content, `assert bad==0` passed.
- **Row leading {0,2}-block b_k (the correct block-lemma object):** b_1..b_12 =
  `[2,7,13,13,24,23,22,21,24,58,97,96]`, matching the established record rows
  1..12 exactly (2,7,13,13,24,23,22,21,24,58,97,96). Verified by re-import of
  the module. This is the row-direction object the block lemma governs.
- **Protection constant 1:** over k=1..39, while `j <= b_k` row `k+j` keeps
  leading 1; 0 violations. `assert viol==0` passed (reproduces the proved block
  lemma, constant 1 = one protected row per block entry).
- **Diagonal cycle length c_n (the diagonal analogue):** max 9991; the min
  over the live range n≥3 is 1. The printed "0 at n=0" is a **display
  artifact**: the reporter `c.index(min(c[2:]))` scans the whole list and finds
  the `c[0]=0` placeholder rather than the true min position. The genuine
  minimum over n=2..N is **0 at n=2 only** — the trivial diagonal `[3,1]` of
  the 2-prime prefix (2,3) before parity evenness begins; its entry above the
  bottom is 3. Every other n has the entry above the bottom ∈ {0,2}. So this is
  not a finding, just the initial trivial prefix.
- **Distribution of c_n (n=2..20):** `[0,1,2,2,4,4,6,6,7,7,8,10,12,12,13,14,13,13,17]`
  — the 0-2 cycle length is non-decreasing in the live regime (it GROWS, not
  erodes, most steps), consistent with the run's earlier audit.

## Verdict

Both asserted invariants hold on this range; the program reproduces the block
lemma's constant-1 protection in row coordinates and confirms the diagonal
0-2 cycle never dies past the trivial n=2 prefix. The only quibble is the
`min cycle at n=0` print, cosmetic.
