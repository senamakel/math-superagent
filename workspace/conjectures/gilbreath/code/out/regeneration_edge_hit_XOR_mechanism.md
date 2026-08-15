# Regeneration = drain-to-4 + interior-bit-1 hit — edge dynamics, and what is PROVED

**Two-layer status.** The XOR edge laws and the firing identity below are
**PROVED theorems** (one-line from the recurrence + block entries halving to
{0,1}). The stall bound is **verified-numerically** (genuine regime rows
1..161) and is the genuine conjectural crux — the run's Route A stall-bound.

## Proof layer (each line verified 0-violation AND derivable from the recurrence)

Notation (halved interior): `b_k` leading {0,2} block length of row k;
`e_k = A_k[b_k]/2`, `i_k = A_k[b_k-1]/2`, `w_k = A_k[b_k-2]/2` (all in
{0,1} by definition of the block); `c_k = A_k[b_k+1]` intruder.

1. **Edge/inner XOR laws — PROVED, holding on ALL erosion rows**
   (`b_{k+1}=b_k-1`). On erosion the edge moves left: `e_{k+1} = A_{k+1}[b_k-1]/2`
   `= |A_k[b_k-1]-A_k[b_k]|/2 = |2i_k-2e_k|/2 = i_k XOR e_k`
   (both bits, so |i-e| = i^e). Likewise `i_{k+1} = w_k XOR i_k`.
   Verified: 0 violations over all 101 erosion rows; both laws fail only at
   the 26 regen rows (where `b_{k+1} ≠ b_k-1`, block shifts).
   ⇒ the boundary is a deterministic Rule-90 shove while the block erodes.

2. **Stall → hit identity — PROVED.** At a stall (`e_k=0`), the XOR law gives
   `e_{k+1} = i_k ^ 0 = i_k`. So on an edge-0 erosion row the edge flips to 1
   **exactly when the interior bit `i_k` turns 1**. Verified 0 violations
   (`e_{k+1}=i_k` on every edge-0 erosion row). The interior bit `i_k` is
   itself a Rule-90 fold of the block's halved pattern (proved
   `rule90-interior-xor`), so regeneration timing past a stall is entirely a
   wave-front hitting time of the interior — not primality.

3. **Firing condition — the step law, already PROVED to depth 800.**
   `b_{k+1} ≥ b_k ⟺ (c_k=4 AND e_k=1)`. 0 violations over k=1..160.
   `c_k=4` is necessary but not sufficient (36 genuine rows have c=4 yet don't
   fire — precisely the stalls where e=0). Combined with (2): at c=4 with
   e=0, the system waits for interior bit i to turn 1, then fires next row.

## Numerical layer (genuine regime rows 1..161; conjecture beyond)

Waiting blocks at `(c=4, e=0)`: 20, lengths `[1,1,6,3,1,4,3,2,1,1,2,2,1,1,1,
1,1,1,1,2]`, **max 6, mean 1.8, median 1**, all < block length at start
(max stall/b ≈ 0.0103). Verified in every long erosion run (13/12/12/8/7-row)
that the intruder drains 14→12→10→8→6→4 steadily and the c=4 stall is 1 row
(k=27 shows the 6-row stall). Falsifier: any k beyond 161 with stall > 6, or
a `(c=4,e=1)` non-regen row.

## What is and is not proved

- **PROVED**: the edge/inner XOR laws on erosion; regeneration fires exactly
  when interior bit i=1 at c=4; step law (regen ⟺ (2,4)). These are the
  deterministic mechanism, all derivable from the recurrence, 0 violations.
- **OPEN (the crux)**: that the interior bit i actually turns 1 within a
  bounded number of rows of c reaching 4 — the stall bound. Proved
  `edge-interior-invertibility-sharpened` says a *nonzero* block shows edge=2
  at least once in its n erosion reads, so a stall cannot last the block's
  whole life; but the primes' observed stall ≤ 6 is numerical, and Eppstein's
  class shows long zero-blocks (stall) are realisable in the wider class. The
  stall bound dependent only on block length (Route A `≤ 2·b_k`, observed
  ≪ that) is the honest open regeneration statement this note isolates.

falsifier: (numerical) stall > 6 or a (c=4,e=1) non-regen row beyond row 161;
(bound, conjectural) a c=4 stall that outlasts the block erosion.

```claim
id: regeneration-edge-hit-xor-mechanism
statement: On the prime Gilbreath rows (genuine regime k=1..161), the halved
  edge/inner boundary bits obey the XOR laws e_{k+1}=i_k XOR e_k and
  i_{k+1}=w_k XOR i_k on EVERY erosion row (b_{k+1}=b_k-1) — 0 violations over
  all 101 erosion rows, failure only at the 26 regen rows — and regeneration
  fires exactly when interior bit i_k=1 while intruder c_k=4 (the step-law
  (c=4,e=1) ⟺ regen, 0 violations, with c=4 necessary but not sufficient).
  On an edge-0 stall e_{k+1}=i_k exactly (0 violations), so regeneration delay
  past drain-to-4 is entirely the interior Rule-90 wave-front hitting time of
  bit i. Waiting blocks at (c=4,e=0): 20 in genuine regime, max length 6, mean
  1.8, all < block length (max stall/b ~0.0103).
hypotheses: rows are iterated absolute differences of the primes below sieve
  2e7; genuine regime rows 1..161 (row >=162 is the finite-width artifact);
  halved interior.
holds-here: yes (rows 1..161, exact); the XOR laws and firing identity are
  proved from the recurrence; the stall bound (<= 6) is verified-numerically.
status: checked (XOR laws: proved; stall bound: numerical over genuine regime)
bearing: isolates the regeneration-timing crux as the c=4-stall bound (how
  long interior bit i stays 0 while intruder is 4). Composes with the proved
  edge-interior-invertibility-sharpened (nonzero block shows edge=2 at least
  once) and step-law-and-recharge-identity; the stall bound for all k is the
  open statement.
anchor: code/out/regeneration_edge_hit_XOR_mechanism.md
```
