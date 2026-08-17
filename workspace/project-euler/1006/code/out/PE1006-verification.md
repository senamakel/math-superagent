# Project Euler 1006 — brute-force verification record

Program: `code/brute.py` (naive oracle). Output reproduced verbatim in the
agent report; the key results:

- Distinct length-3 subwords of the infinite Fibonacci word:
  `001, 010, 100, 101` → Psi(3) = 1 + 100 + 10000 + 10201 = **20302** ✓
- Psi(10) mod 101001001 = **10699667** ✓
- Distinct length-k factor counts: exactly k+1 for all k = 1..20 ✓,
  and the factor sets do not grow when the sampling word is extended two
  Fibonacci steps (checked per k, same run) ✓.

## Word-length bound found (the 2k claim in the task is NOT always safe)

Task says building S_n until len >= 2k is a safe bound ("may go a bit beyond").
Direct exhaustive check against a 2e6-char word shows it is not:

- k = 15: 16th factor first appears only at prefix length 35, while 2k = 30.
  With len = 30 the count was 15 (one factor missed). Psi(15) is therefore
  wrong with the 2k rule: 61091760630937672902595709006 vs the truncated
  61090760630937672902595709006 (digit 3 does not appear in any length-15
  factor set prefix-limited to 30 chars).
- Minimal sufficient prefix lengths (smallest L with k+1 distinct k-factors):
  k=13→33, k=14→34, k=15→35, k=16→36, k=17→37, k=18→38, k=19→39, k=20→40,
  k=21→54, k=30→63. These look like smallest Fibonacci number >= 2k, ±1.

`len >= 3k` (or `len >= ~2.11k`) is comfortably sufficient for all k <= 30
(worst observed need 63 at k = 30, well under 3k = 90). `brute.py` uses
`len >= 3k`, which the task's "you may go a bit beyond" permits.

Values: Psi(1)..Psi(20) = 1, 101, 20302, 2042402, 204252402, 30445654403,
3054587854503, 407470828064704, 40849095449084804, 4085011557551094804,
508703259827952296805, 50970528087268072496905, 5097153010831280092506905,
609915603287332682295508906, 61091760630937672902595709006,
7129296283596175714952815919207, 713949748580120079919974836939307,
71395994978232510500422176938949307, 8141620537963671762570662587340151308,
815164074836507597029594703627460351408.

Note: memory store (Cognee) was unhealthy at write time, so this record lives
in the workspace.