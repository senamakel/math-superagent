# CHT Theorem 1.6 hypothesis check against the real prime rows

**Date:** this run. **Sieve:** primes ≤ 2e7 (1,270,607 primes), the sieve used
for the depth-1000 prime triangle. **Window:** the first G = 1,270,605
normalized gaps — exactly the window of gaps the depth-1000 triangle spans.

Normalized gap (claim `cht-normalized-gap-definition`):
`a_n = (p_{n+2} − p_{n+1})/2 − 1`.

## Measured values

| Quantity | Meaning | Value |
| --- | --- | --- |
| `max a_n` | largest normalized gap in window | **89** (prime gap 180, between consecutive primes 17051707 and 17051887) |
| `M` | `ceil(log2(max a_n))`, so `a_n ≤ 2^M` | **7** (2^7 = 128 ≥ 89 > 2^6 = 64) |
| `L` | longest run of consecutive 0s among `a_n` | **2** (a_1=0, a_2=0; nothing longer in the window) |
| `R_0` | `100 · L · 8^M` (CHT first no-{0,d}-block threshold) | **419,430,400** = 100·2·8^7 |

`log10(R_0) ≈ 8.6`, `log2(R_0) ≈ 28.6`.

First ten `a_n` = `0,0,1,0,1,0,1,2,0,2` — matches the claim's stated first nine
values (0,0,1,0,1,0,1,2,0).

## Verdict: `holds-here: no` — the theorem does not bite at reachable depths

CHT Theorem 1.6 needs, among its hypotheses, that no `{0,d}`-block of length
`≥ R_m − 3R_{m−1}` occurs at depth `≤ 2R_{m−1}`, with `R_m ≥ 4R_{m−1}` and
`R_0 ≥ 100L·8^M`. The first-protection-depth threshold is `R_0 = 419,430,400`.

The depth-1000 triangle reaches **depth 1000**. Since `R_0 = 419,430,400 ≫
1000`, there is **no depth `≤ 1000` at which the `{0,d}`-block hypothesis can
even begin to be checked** — the theorem demands protection over a depth window
of order `R_0 ≈ 4.2×10^8` rows, which is far beyond the reachable 1000. The
inverse theorem is true but its bite is shifted out of range; it neither proves
nor refutes anything at the depths this run can generate. (For comparison,
literature verification reaches ~10^15 rows, still ≪ R_0.)

The two CHT obstruction families are therefore **not numerically surveyable
here**: any `{0,d}`-block of the length Theorem 1.6 controls is astronomically
far down. This claim is independent of the theorem's truth — it records that the
hypotheses are unsatisfiable at the depths at hand.

```claim
id: cht-inverse-theorem-hyp-check
statement: For the prime-difference triangle to depth 1000 (sieve 2e7,
  1,270,607 primes), the normalized gaps a_n=(p_{n+2}-p_{n+1})/2-1 over the
  1,270,605-gap window give max a_n=89, M=ceil(log2 89)=7, longest 0-run L=2,
  hence the CHT no-{0,d}-block threshold R_0=100·L·8^M=419430400.
hypotheses: CHT Theorem 1.6 demands the no-{0,d}-block condition hold over a
  depth window of order R_0; the depth-1000 triangle reaches only depth 1000.
holds-here: no (R_0 = 419430400 ≫ 1000; the theorem's protection threshold is
  ~4.2e8 rows, so no {0,d}-block hypothesis is satisfiable at any depth ≤ 1000 —
  the theorem does not bite at reachable depths)
status: checked
bearing: The CHT inverse-theorem route cannot be applied to the reachable
  prime rows: its two obstruction families (long zero-blocks, long shallow
  {0,d}-blocks) are not surveyable within 1000 rows. Confirms the gap noted in
  CONTEXT.md — the theorem's hypotheses, though true, fail to hold at any
  reachable depth.
anchor: code/out/cht_hyp_check.notes.md, code/cht_hyp/check_cht_hyp.py,
  code/out/cht_hyp_check.captured.txt
```

Independent confirmation: `max a_n = 89` (gap 180, consecutive primes
17051707, 17051887), `longest 0-run = 2`, computed by a second program that
re-sieves and recomputes the gaps directly (not reading the first output).
Both agree.
