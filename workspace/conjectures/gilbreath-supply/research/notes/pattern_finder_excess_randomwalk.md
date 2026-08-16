# Pattern-finder report: the excess E2(n) = 2·nu2(n) − (n−2) = −S(n)

Date: pattern_finder pass. Data: `code/out/excess_E2_30000.txt` (n=2..30000),
plus fresh dyadic computation to n=65536 via `lib.supply_fold.s_sos` (exact,
cross-checked against brute oracle n=4..60 and reproducing nu2(4000)). All
statements are MEASUREMENT, not proof; none is a theorem for all n.

## The cleanest framing

SUPPLY pointwise (nu2(n) ≥ c·n for any fixed c < 1/2) is **exactly equivalent**
to E2(n) = o(n), since nu2(n) = (n−2−S(n))/2 and E2 = −S. So the whole question
reduces to the growth of the signed excess E2.

## Structural facts (exact over the computed range, all conjectural for all n)

1. **Random-walk scale.** σ(E2) ≈ 0.77·n^0.49; std(E2)/√n is flat at 0.71 ± 2.5%
   over N = 500..30000. max|E2| = 634 at n = 27624 (max/n ≈ 0.023).
2. **Pointwise o(n) empirically.** Dyadic E2/√n stays within ±2.3 and E2/n → 0
   out to n = 65536. So nu2(2^k)/2^k → 1/2 empirically.
3. **Anti-persistence.** Increment sign lag-1 autocorrelation ≈ −0.34, ~0 at
   lag ≥ 2 — mean-reverting, not a growing random walk.
4. **Increments all odd integers** (E2 parity = n parity, from the definition
   E2 = 2·nu2 − (n−2) ≡ n mod 2). The period-2 residue report from the tools is
   this trivial fact, not structure.

## Sequence tools

- E2(n) and the dyadic subsequence nu2(2^k): **no constant-coefficient linear
  recurrence** (orders ≤ 10 / ≤ 6), not low-degree polynomial.
- **OEIS: both miss** (uncatalogued). No closed form to look up.

## The critical caveat (genericity)

Both the √n scale (0.71–0.73) and the negative lag-1 autocorr (−0.33..−0.37)
are **reproduced by iid random h** at p = 0.5 (0.726, −0.333) and p = 0.585
(0.714, −0.335). So neither is prime-specific; they are generic fold behaviour
on balanced input, consistent with the prior `pattern_finder_fold_generic_balance`
finding. The primes' only needed property is *being unstructured enough*, which
is a much weaker input than positive mod-4 switch density — but this remains a
measurement, not a proof, and no arithmetic input that *proves* G-weak-input has
been found.

## Verdict

No exploitable pointwise/prime-specific structure beyond the already-recorded
averaged form (GOAL priority 1). The excess is cleanly framed as
    0.77·√n · (bounded fluctuations, anti-persistent),
empirically o(n) to 65536 — exactly what SUPPLY needs pointwise — but all of it
is fold-generic and offers no new arithmetic handle over the prior run's
findings. `max|S|/√n = 3.80` at N=20000 reconfirms the prior ≤3.8 band.
