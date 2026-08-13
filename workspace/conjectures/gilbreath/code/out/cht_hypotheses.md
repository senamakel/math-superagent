# CHT Theorem 1.6 hypothesis check against the real prime rows

Computed by `code/cht/check_cht_hypotheses.py` (sieve to 2e7, exact integer
arithmetic), output captured in `code/out/cht_hypotheses.captured.txt`.

Theorem 1.6 (Chase–Hunter–Tao 2026, arXiv:2607.08712, deterministic inverse
theorem) concludes `a(N-1,1) in {0,1}` from three axioms:

- (i)   `a_n <= 2^M` for all n in the window;
- (ii)  no 0-block of length L anywhere in the array;
- (iii) no {0,d}-block (`2^{M-m} < d <= 2^{M-m+1}`) of length
  `>= R_m - 3 R_{m-1}` at depth `<= 2 R_{m-1}`, with `R_m >= 4 R_{m-1}`
  and `R_0 >= 100 L 8^M`.

## Numbers (window: primes <= 2e7, primes = 1,270,607, normalized gaps = 1,270,605)

- **max a_n = 89** (prime gap 180, first at n = 1094420)
  → **M = 7** (smallest M with `a_n <= 2^M`:
  `2^{M-1} = 64 < 89 <= 128 = 2^7`)
- **L = 2** = longest run of consecutive 0s in the a_n string (occurs at
  n = 1..2).  Note: three consecutive zeroes are
  provably impossible (p, p+2, p+4 cannot all be prime, one is divisible by
  3), so L = 2 is exact for all time.
- **longest {0,d}-block over all d >= 1: length 7** (attained by
  d = 1)
- **R_0 = 100 * L * 8^M = 100 * 2 * 8^7 = 419430400**
  (log10(R_0) = 8.62)

Axiom (iii) must hold with no {0,d}-block at depths up to `2 R_{m-1}`,
the smallest scale being R_0, and condition (1.6) of the theorem needs
`R_M < (N - N')/2`, i.e. the array itself must span depth ≳ 2 R_0 ≈
838,860,800 rows.  R_0 = 419,430,400 is 419,430.4 times the run's reachable
depth (1000), so the theorem's hypotheses are **not satisfiable at any depth
this run can reach**: the two obstruction families the theorem names (long
zero-blocks, long shallow {0,d}-blocks) live at scales ~419,430,400 and are not
surveyable within 1000 rows.

**Verdict: holds-here = no** — the theorem's constants do not bite at
reachable depths; the inverse theorem gives no information about the prime
rows at depth <= 1000.

```claim
id: cht-inverse-theorem
statement: If a_n <= 2^M, no length-L 0-block, and no {0,d}-block (2^{M-m} < d <= 2^{M-m+1}) of length >= R_m - 3 R_{m-1} at depth <= 2 R_{m-1} (R_m >= 4 R_{m-1}, R_0 >= 100 L 8^M), then a(N-1,1) in {0,1}; long zero-blocks and long shallow {0,d}-blocks are the only obstructions to decay.
hypotheses: nonneg-integer initial data with a_n <= 2^M; R-tower hierarchy with R_0 >= 100 L 8^M; axioms (ii) no-L-zero-block and (iii) no-shallow-{0,d}-block verified at depths up to order R_0, with the array spanning depth > 2 R_0.
holds-here: no (R_0 = 419430400 ≫ 1000: the theorem's no-{0,d}-block protection threshold is ~4.2e8 rows, so the hypothesis is not satisfiable at any depth <= 1000 — the theorem does not bite at reachable depths)
status: checked — computed from the real prime rows (sieve 2e7, 1,270,607 primes, 1,270,605 normalized gaps a_n = (p_{n+2} - p_{n+1})/2 - 1): max a_n = 89 -> M = 7, longest 0-run L = 2 (provably exact: p, p+2, p+4 cannot all be prime), longest {0,d}-block = 7 (d = 1), so R_0 = 100*L*8^M = 419,430,400 = 419,430x the run's max reachable depth (1000). First nine gaps match OEIS A100820.
bearing: the CHT inverse-theorem route cannot be applied to the reachable prime rows; the attack must either rule out long zero-blocks and long shallow {0,d}-blocks for the primes (needs analytic hypotheses) or find an invariant bypassing the dichotomy.
anchor: code/out/cht_hypotheses.captured.txt, code/cht/check_cht_hypotheses.py, research/sources/chase-hunter-tao-2026-full-html.full.md (Theorem 1.6)
```
