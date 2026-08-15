# Pattern-finder pass: tail refinement of the Route-B supply bound (n≥1000)

Status: all exact over the supplied terms from the run's own computation; none
is a proof beyond them.

## What was checked fresh (not a re-derivation of recorded findings)

The one genuinely active open content of this run is the **supply-side linear
bound** `ν₂(q_n) ≥ c·n` (Granville Route B), conditional at Hardy–Littlewood /
Lemke Oliver–Soundararajan level. The deviation sequence
`D(n) = 2·ν₂(n) − n` extracted from `code/out/nu2_dense.txt` (n=1..30000,
exact sieve) was re-probed:

- `max |D| = 639` at n = 27625; max D = 558, min D = −639.
- `max |D|/√n = 3.845` at n = 27625 — confirms the recorded LIL-flavoured
  concentration `|D| ≤ 3.85√n`.
- sign split: +13266 / 0:139 / −16595 over 30000 (negative side more common;
  bias genuinely oscillates — Littlewood-style, already established).

**Tail (the regime G-supply actually needs):**

| regime | min ν₂/n | at n | min log ν₂/log n | at n |
|--------|-----------|------|-------------------|------|
| n≥1000 | 0.4587   | 1212 | 0.8879           | 1005 |
| n≥5000 | 0.4761   | 5656 | 0.9138           | 5078 |
| n≥10000 | 0.4844  | 11491| 0.9218           | 10045 |

Tightest margin for `ν₂ ≥ 0.40 n` over n≥1000 is **+61** (at n=1005); for
`ν₂ ≥ 0.45 n` it is **+11** (at n=1212); `ν₂ ≥ 0.49 n` fails (margin −78 at
n=5656). So the strongest linear lower bound the data supports with a positive
margin at every n≥1000 is only just about `c ≈ 0.45` — *well below* the
measured `ν₂/n ∈ [0.4587, 0.54]` because the deviation envelope is largest
exactly where the ratio is smallest. This is a genuinely refining number not
previously stated as a margin-by-regime table.

## Tool verdict on the natural structural sequences

`analyze_sequence` and `find_linear_recurrence` run (exact over supplied terms)
on the second-entry sequence, the block profile, the edge sequence, and the
intruder sequence:

- **second-entry sequence** `S_k` (the conjecture object, {0,2}-valued): no
  low-degree polynomial (differs do not vanish within 12 levels), every term
  even → residue mod 2 periodic with period 1; OEIS identity `S_k = A089582`
  already recorded.
- **block profile** `b_k` (2,7,13,13,24,...): no constant-coefficient linear
  recurrence of order ≤ 8, no low-degree polynomial; OEIS identity
  `b_k = A000232(k) − 1` already recorded.
- **edge sequence** (A_k[b_k], {0,2}-valued): no polynomial structure; mod 2
  periodic with period 1 (all even, tautological).
- **intruder sequence** (values {4,6,8,10,...}): no polynomial structure; mod 2
  periodic period 1.
- **giant gaps** `[22,8,4,26,2,14,2,14,4,4,12,15,13,64]`: OEIS lookup returns
  **no entry** (uncatalogued; confirms recorded miss, do not re-search).

## Conclusion — what is exploitable

The sequence tools find **no arithmetic (recurrence / polynomial / period)
lever** in any of the candidate sequences beyond the two known catalogue
identities. This confirms the run's standing claim
`pattern-finder-no-loworder-plus-surplus`.

The only structural regularity that survives is the **monotone recharge
surplus** `S_k = b_k − b_1 + (k−1)`: a *proved* theorem of the step law
(`S_{k+1} − S_k = (b_{k+1} − b_k) + 1`, nondecreasing, increments exactly at
(2,4)-events), whose equivalent-conjecture form is "`S_k ≥ k−2` never returns
to zero", i.e. a lower bound on the (2,4)-event arrival rate. The supply side
`ν₂ ≥ c·n` — which Route B needs — is a named open problem (two-point
consecutive-prime mod-4 switch frequency; ABGS 2011 §9), NOT a low-order
arithmetic fact, and the honest deliverable there is a conditional fluctuation
bound (Rubinstein–Sarnak / Lemke Oliver–Soundararajan level), never an
unconditional one-sided density.

The fresh margin-by-regime table above is the one new contribution of this
pass: it quantifies exactly how much slack the *real* supply bound has over the
regimes Route B would run, and shows the honest constant is `c ≈ 0.45` (not the
naive `n/2`), because the deviation envelope bites where ν₂/n is minimal.
