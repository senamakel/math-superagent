# nu2 averaged-form structure — pattern-finder findings (revisited)

Data: nu2(n) for n=2..4000, primes, from the mod-4-switch endpoint character
sum (code/out/supply_endpoint_density.txt), nu2 = (n-2-S)/2. Cross-checked
against the gap-parity SOS fold (nu2_fast / s_sos): 0 difference at
n=100,500,1000,2000,4000 (convention edge h[0] cancels here).

## Averaged-form evidence (GOAL priority 1: density-1 linear bound)

- Mean of nu2/n: 0.4439 @100 → 0.4728 @250 → 0.4911 @1000 → 0.4973 @4000. No
  downward drift; consistent with truth c≈0.49.
- Pointwise variance sigma^2 of nu2/n decays: 1.64e-2 @100 → 7.21e-4 @4000.
- Last-half-window sigma^2 (window [N/2,N)): 7.78e-4 @N500, 3.44e-4 @1000,
  1.62e-4 @2000, 9.11e-5 @4000. Fits N^{-a} with a flattening from -1.18 to
  -0.83 over 500→4000 (finite-N crossover; exponent not settled).
- Density-1 tails: points with nu2/n < c within [50,4000]:
    c=0.30: none; c=0.35: 1 (n=53, 0.3396); c=0.40: 3 (all ≤105);
    c=0.42: exactly 10, all n ≤ 274 (largest 274);
    c=0.45: 51, all ≤763; c=0.48: 347, largest 3858.
  Every modest threshold's violations lie at bounded n and die out. This is
  exactly the shape a density-1 linear bound would have (porous pointwise,
  dying tail) — the strongest structural handle for a theorem.

## Failed structural hypotheses (attack results)

- No constant-coefficient linear recurrence of order ≤12 fits the 98-term nu2
  sequence; not a low-degree polynomial. Confirmed exact over the terms.
- OEIS: no match for nu2 terms (uncatalogued). The dyadic subsequence was also
  tested previously and over-fit then refuted.

## Residue / dyadic

- nu2(2^k)/2^k = 0.25,0.75,0.41,0.42,0.52,0.53,0.47,0.49,0.49 for k=3..11 —
  bounded away from 0, no dyadic collapse (consistent with note).

## Status

All of the above is exact numerical evidence over n≤4000 only. None is a proof
for all n. The variance decay and dying sub-0.42 tail favour a real theorem on
the averaged form (GOAL priority 1), and the strongest next step is to bound
the submask-window autocorrelation / variance of the prime h (G-var) rather
than the pointwise statement.
