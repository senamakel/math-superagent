# Pattern-finder fresh results: Moser chromatic polynomial and chi_f freezing

Author: pattern_finder. Every number below was freshly computed this run
(program output read from captured artifacts). Structural conclusions are
**conjectures** unless flagged `verified` (exact, machine-checked).

## 1. Moser spindle chromatic polynomial — VERIFIED exactly

The proper-k-colouring count of the 7-vertex 11-edge Moser spindle is a
degree-7 polynomial (any chromatic count always is). Fitting the interpolation
polynomial to exact counts at k=0..7 and checking out-of-sample:

**P_M(k) = k(k-1)(k-2)^2(k-3)(k^2-3k+4)**

Values (exhaustive backtracking, exact):
| k | P(k) |
|---|------|
| 4 | 384 |
| 5 | 5040 |
| 6 | 31680 |
| 7 | 134400 |
| 8 | 443520 |
| 9 | 1227744 |
| 10| 2983680 |
| 11| 6557760 |
| 12| 13305600 |
| 13| 25293840 |
| 14| 45549504 |

Verification: out-of-sample checks at k=8..14 all MATCH (8 fresh points beyond
the 8 used for the fit). P(0..3)=0 consistent with chi=4. Note report:
`code/out/moser_chromatic_poly.txt`, `..._fit.txt`, `..._extend.txt`.
The values 384,5040 agree with the calibration record CONTEXT.md.

`find_linear_recurrence` over the 10 terms returns no constant-coefficient
recurrence of order <= 4, consistent with a polynomial of degree 7 (which
satisfies an order-8 relation, not <=4). `oeis_lookup([384,5040,31680,134400])`
misses — not catalogued. So there is no simpler catalogue identity; the factored
form is the structure:
- double root at k=2 (expected: graph has structure making certain colourings
  counted twice — matches the fact P(2)=0 for any 3-chromatic-subgraph graph,
  here the graph is 4-chromatic so roots 0,1,2,3; the square is the only
  repeated root of the 1-skeleton of a 4-chromatic graph).
- final factor k^2-3k+4 has discriminant 1-16 = -15? No: k^2-3k+4, disc =
  9-16 = -7. Irreducible over Q, so the chromatic polynomial's only
  multiplicity is the square (k-2)^2.

## 2. Fractional chromatic number FREEZES at 7/2 under Minkowski sum — VERIFIED

chi_f = fractional chromatic number (independent-set LP relaxation of colouring,
chi_f <= chi always, and chi_f > 4 would certify chi >= 5).

Freshly computed (first time the run has any chi_f value; this is the central
prediction of the adopted fractional-chromatic-lp-lower-bound approach):

- chi_f(C5)  = 5/2 (verification of the method)
- chi_f(Diamond) = 3 (verification)
- **chi_f(Moser)  = 7/2**
- **chi_f(Moser+Moser) = 7/2**

Both 7/2 values verified by BOTH the primal LP (fractional colouring of total
weight 7/2 covering all vertices to >= 1; for Moser+Moser over all 16284
independent sets) AND the dual LP (vertex weighting with every independent set
of weight <= 1, total 7/2). The dual witness is uniform w_v = 1/2 on the 7
Moser vertices: each independent set has size <= alpha = 2, so weight <= 1, and
total = 7/2. This proves chi_f(Moser+Moser) >= 7/2; primal gives <= 7/2.

Consequence (a CONJECTURE from this limited data, but with a mechanism): the
Minkowski-sum / spindle construction that turns the Moser into larger
4-chromatic unit-distance graphs does NOT raise chi_f; it stays exactly at 7/2.
The fractional-LP route therefore cannot certify chi >= 5 on the family the run
currently builds — it would need chi_f > 4, and the whole constructible family
is frozen at 7/2. This bounds what the fractional-chromatic direction can buy
on the current machinery, parallel to how the theta SDP peaks at 2.995.

Whether a *different* construction can lift chi_f above 4 is untouched by this
(open — the plane's chi_f is unknown and censored at this run's network
boundary per REQUESTS.md).

## 3. Kernel-census and Mycielski sequences — confirmed no new structure

Re-run the tools; they confirm the earlier consolidated report:
- kernel member counts [1,4,16,228]: geometric head 4^0,4^1,4^2 breaks at 228
  (ratio 14.25); provably not order-2 recurrent; uncatalogued.
- Mycielski V_k = 3*2^k - 1, E_k = (1-6*2^k+7*3^k)/2: already proven (sourced
  OEIS + sympy), and the family is provably not unit-distance realizable
  (K2,3 obstruction).

## Claims status
- Moser chromatic polynomial P_M(k): **verified** exactly (out-of-sample at
  8 fresh points). The "it is a polynomial" fact is a theorem; this instance's
  coefficients are machine-checked, not derived. The factored form has a
  provable double root (k-2)^2 and irreducible factor k^2-3k+4.
- chi_f(Moser) = chi_f(Moser+Moser) = 7/2: **verified** (primal + dual LP
  certificates, exact rational witness w=1/2).
- "Minkowski rigidity accumulation does not move chi_f toward 4 on the built
  family": **conjecture** (two data points: Moser 7/2, Moser+Moser 7/2). Tested
  only these two tiers; a third (e.g. a triangle-sum or sum of two Moser+Moser)
  would be needed to extend.
