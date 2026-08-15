# Thue–Morse subset-zeta + corner-family supply — exact verification result

**Capture:** `code/out/thue_dyadic_supply_verify.captured.txt` (EXIT_CODE=0)
**Program:** `code/out/thue_dyadic_full.py` (this run, exact integers)
**Diagnostic:** `code/out/thue_dyadic_ident_diag.py`

All core computations are exact integer arithmetic; densities are reported as
exact fractions.

## PART A — Thue–Morse subset-zeta identity: **CONFIRMED** (first machine check)

h[j] = wt(j) mod 2, subset-zeta ζ(h)[d] = XOR_{j⊆d} h[j]:

- fast O(N log N) transform agrees with naive O(N·2^wt) double loop on N=4096
- **# {d ∈ 0..N : ζ=1} = 17** at N=100000, exactly the 17 powers of two ≤ 1e5
- popcount identity Σ_{j⊆d} wt(j) ≡ wt(d)·2^{wt(d)-1} (mod 2) holds, d ≤ 699

So ζ(h)[d] = 1 ⟺ d is a power of two is true.

## PART B — identification nu2(n) == #{powers of two ≤ n}: **REFUTED**

Direct exact triangle of the Thue-Morse 2-then-odds to D=4000 (one row at a
time), validated against **both** `lib.gilbreath.rows_generator` and
`lib.rightdiag.cycle_and_nu2`:

```
n      nu2(n)   #pw2<=n   match
1        0        1       NO   <- first mismatch
100     27        7       NO
500     39        9       NO
1000    41       10       NO
2000    43       11       NO
4000    45       12       NO
```

**The load-bearing identification does not hold at any sample.** Cause:
ζ=1 marks the *parity* (odd half) of a tail cell, while nu2 counts *even*
{0,2} tail cells — the actual tail is dense in 0s/2s with runs that
parity-cancel in the XOR fold. The fold bit is the *opposite* statistic.

**Qualitative conclusion survives:** fine scan n≤4000 shows ν₂ is sublinear
and small (max ~219, bobbing 27..219, not growing with n) — so Thue-Morse
remains a valid aperiodic witness that aperiodicity does not force linear
supply.

## PART C — corner-family density table (N=200000, d∈0..N, denom=200001)

| family | count ζ=1 | density | class |
| --- | --- | --- | --- |
| all-zeros | 0 | 0 | {0} |
| all-ones | 1 | 1/200001 | sublinear |
| alternating 0,1 | 1 | 1/200001 | sublinear |
| period4 0,0,1,1 | 1 | 1/200001 | sublinear |
| period3 0,1,0 | 133333 | 133333/200001 ≈ 0.6667 | **{≥c>0}** |
| period5 | 106667 | 106667/200001 ≈ 0.5333 | **{≥c>0}** |
| Thue-Morse | 18 | 6/66667 ≈ 9.0e-5 | sublinear |
| Rudin-Shapiro | 17 | 17/200001 ≈ 8.5e-5 | sublinear |
| LCG pseudo-random | 99983 | 99983/200001 ≈ 0.4999 | **{≥c>0}** |
| real prime switch bit | 100323 | 33441/66667 ≈ 0.5016 | **{≥c>0}** |

Rows with positive density (odd-factor periods, LCG, primes) are the
supply-friendly classes; the others collapse. This is consistent with the
dyadic-linear-complexity supply picture.

## Filed

- Claim `thue-morse-subset-zeta-confirmed-identification-refuted` +
  `research/notes/thue-morse-identification-refuted.md` — corrects the
  over-precise part of `thue-morse-sublinear-supply-witness` (its ≡-reading of
  ζ is right; its identification to nu2 is wrong).
- Memory stored.
