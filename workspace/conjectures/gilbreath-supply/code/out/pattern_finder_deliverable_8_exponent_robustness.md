# Pattern-finder deliverable — pass-3 regularity audit

## The one owed computation (GOAL.md) was already answered; I attacked the headline claim instead

The third-pass GOAL was: does the min weight ratio at which linear supply
becomes typical tend to 0 or plateau near 1/8? The prior pass resolved it: the
**exact-mean** half (no sampling) gives a monotonically falling ratio and a
fitted sublinear exponent `w*(n) ~ n^0.5568` (sequence `3,3,3,4,3,5,7,11,16,24,
35,52,77,112,164,239,349` at n=8..65536 powers of 2; exact). The 1/8 plateau is
broken; the column supports "tends to 0."

My contribution here is to **attack the exponent itself** rather than re-confirm
the column — a conjecture tested only on the data that suggested it is untested.

## What I ran (exact/quantitative, not a re-claim)

1. **`analyze_sequence` / `find_linear_recurrence`** on the exact threshold
   sequence: not a low-degree polynomial, no constant-coefficient linear
   recurrence of order ≤ 8, **not in OEIS** (no closed form can be looked up).
   Exact over the terms supplied; a conjecture, not a law.

2. **Competing-model attack** (`code/pattern_finder/break_exponent_competing.py`),
   full 28-point exact dataset (power-of-2 + intermediate phase):
   - Pure power `log w* = a + E log n`: E = 0.5547 ± 0.0051.
   - Add a log-power factor `+ B log(log n)`: E=0.604±0.025, **B=−0.28±0.14
     (not significant, |B|<2.1σ)**, RSS barely improves 0.332→0.284.
   - Forced-sqrt model `√n·(log n)^B` fits **worse** (RSS 0.488 vs 0.332).
   - Conclusion: the data do **not** support `√n·(log n)^B`; the exponent is
     genuinely above 1/2. The clean `E≈0.555` reading survives this attack.

3. **Direct log-drift test** (`check_exponent_identifiability.py`): correlation
   of `log2(log2 n)` with the pure-power residual = **+0.045**, slope +0.008
   over the n≥128 tail — no systematic `(log n)^B` drift; the residual is the
   bounded log2-periodic oscillation (amplitude ~0.07) the pass already found.
   This independently confirms `w* = n^0.555·P(log n)` with P bounded periodic,
   rather than a hidden log factor masquerading as an exponent.

## What this establishes

The sublinear threshold-weight claim is **robust to the standard competing
functional form**. The arithmetic demand on the primes to make `nu2(n) ≥ 0.4n`
typical is a **sublinear switch count** (`n^0.555`), strictly weaker than a
positive fraction (`n^1`) — `problem.md` result type 4, an input strictly
weaker than pointwise mod-4 switch density.

## Honest limits (unchanged, restated)

- Per-n `w*` are **exact** (verified closed-form threshold formula
  `P_d(w)=(C(n,w)−[z^w](1−z)^k(1+z)^{n−k})/(2C(n,w))`, k=2^popcount(d),
  cross-checked against brute s_sos digit-for-digit).
- The exponent 0.555 and the tend-to-zero limit are **numerical fits**, not
  proved for all n. My attack removed the `√n·(log n)^B` alternative but cannot
  prove the limit is 0 (nor rule out an eventual plateau at positive c).
- Genericity gap: "typical is not this string" — being above the threshold does
  not prove the primes' particular h has linear supply. That gap is unchanged.

## Files
- `code/pattern_finder/break_exponent_competing.py`
- `code/pattern_finder/check_exponent_identifiability.py`
- Underlying data: `code/out/threshold_exponent_pass3.md`,
  `code/out/threshold_weight_logperiodic_extended.txt`,
  `code/out/threshold_limit_exact.txt`.
