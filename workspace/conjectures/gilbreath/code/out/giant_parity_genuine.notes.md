# Giant landing-row parity — corrected on the 15 genuine giants

TASKS.md Directive 36 item 1, executed this run. The 1e9 capture's parity
p-value counted all 16 giants including row 247 (genuine=False, the capped
no-intruder row). This recomputes on the 15 genuine giants only, with every
index convention pinned by asserts.

Program: `code/pattern_finder/giant_parity_genuine.py`
Capture: `code/out/giant_parity_genuine.captured.txt`

## Conventions (pinned by asserts in the program)

- `b[i]` = {0,2}-block length of 1-based row `i+1`.
- A (2,4)-event fires at 1-based row `r` (intruder pair at position `b[r-1]`)
  and lands at 1-based row `r+1`, whose 0-based index is `r`.
- `giants_1e9.json['giants_0based_rows']` = 0-based landing indices.
- Boundary files `e_bits.txt`/`c.txt` hold 161 entries; entry `k` is the
  boundary state of 1-based row `k+1`. The event set (edge=2, intruder=4)
  with landing index `k+1` reproduces the recorded base rate 36/60 = 0.600 —
  this is the assert that pins the convention and the population at once.

## Numbers (all exact integer arithmetic)

- Event population at 2e7 (rows 1..161): **60 events, 36 even landing
  indices**, base rate 0.600 — reproduced from raw files, matches the
  recorded 0.600 exactly.
- The 15 genuine giants (1e9, genuine=True), 0-based landing rows:
  `[34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161, 174, 238]`.
  **14 even, 1 odd (161).**
- Membership: all giants with landing ≤ 160 lie in the 2e7 (2,4)-event set
  (asserted); giants 174 and 238 verified by their 1e9-recorded jumps > 1000.

## P-values on the 15 genuine giants

| null | value | note |
| --- | --- | --- |
| fair coin, one-sided (>=14 even of 15) | 16/2^15 = **4.88e-4** | (C(15,14)+C(15,15))/2^15 |
| binomial, base rate p = 0.600 (with replacement) | **5.17e-3** | reproduces the settlement's 0.0052 |
| **exact hypergeometric, without replacement** | **1.82e-3** | population 60 events / 36 even, sample 15 |
| hypergeometric two-sided (>=14 even or <=1 even) | 1.82e-3 | 96,750,948,080 / 53,194,089,192,720 |

The exact hypergeometric is the honest null: it conditions on the actual
(2,4)-event stream rather than sampling with replacement, and it was never
computed before — the settlement quoted only the binomial 0.0052.

## What to quote

The **exact hypergeometric 1.82e-3** (base-rate null, without replacement),
with the fair-coin 4.88e-4 and the binomial 5.17e-3 as references. The giants
land on even 0-based rows 14/15 against a 36/60 even base in the same
convention — the direction of the earlier finding is confirmed and the
without-replacement correction is now exact.

```claim
id: giant-parity-genuine-15-1e9
statement: In the 1e9-sieve prime Gilbreath triangle (W = 50,847,534 primes), the 15 genuine giants (0-based landing rows [34,56,64,68,94,96,110,112,126,130,134,146,161,174,238]) land on even rows 14/15, odd row = 161. Against the measured (2,4)-event base rate 36/60 = 0.600 (re-derived from raw boundary files over rows 1..161 at 2e7, whose rows 1..161 the 1e9 run reproduces exactly), the exact hypergeometric (without replacement) p-value for >= 14 even of 15 is 96,679,035,360 / 53,194,089,192,720 = 1.82e-3; the binomial base-rate p = 0.600 gives 5.17e-3 (reproducing the settlement's 0.0052) and the fair-coin one-sided p is 16/2^15 = 4.88e-4.
hypotheses: 1e9 giants file genuine flags; event population = (2,4)-events at 2e7 rows 1..161 with landing-index parity; 1e9 rows 1..161 reproduce 2e7 (oracle cross-check, zero mismatches).
holds-here: yes
status: checked
bearing: corrects TASKS.md Directive 36 item 1 (the old figure counted the capped row 247); the exact without-replacement p was previously uncomputed. A parity concentration in the giant landing rows survives the correction but remains a 15-point observation — evidence about the regeneration mechanism, not a theorem.
anchor: code/out/giant_parity_genuine.captured.txt
```
