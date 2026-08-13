# Eppstein 2011 — Anti-Gilbreath sequences

**Full text:** `research/sources/eppstein-anti-gilbreath-sequences.full.md` [[eppstein-anti-gilbreath-sequences.full]]
**Source:** https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html (D. Eppstein), and its predecessor "Gilbreath made practical".

## What it establishes

Refutes the blanket small-gap heuristic (attributed to Croft): small gaps + parity + slow growth are NOT sufficient for a sequence to be (eventually) Gilbreath.

**Theorem (Eppstein, constructive).** For any unbounded monotone f(n) ≥ 2, however slowly growing, there is a sequence X whose n-th gap is ≤ f(n) but whose triangle's right edge switches between 1 and other values **infinitely often**.

## The construction mechanism

Given a partial triangle ending in all-1s on the right, extend one row at a time **backwards from the right** (not forwards): put a column of 2s under the final 1 with zeros to its right, and compute each earlier entry as sum or difference (difference preferred) of the two entries above-and-to-the-right so entries stay small. This forces a big empty triangle of zeros on the right. Row sums then stay bounded by O(row length), so eventually the gap limit f exceeds the row sum; a sufficiently large gap then "survives" differencing past the whole row and escapes to the right as a value ≠ 1 (`g_i > s_i` ⇒ rightmost entry = g_i − s_i − 1). Repeat: every so often break the all-1s pattern with a large gap, then restore the 0/2 regime, make another big triangle, etc. — so the right edge hits non-1 infinitely often.

Key observable: "if the gap is larger than the sum of the other entries in the row, then the rightmost number in that row will be their difference (minus one)" — i.e. `s_i` (sum of row i−1 minus first and last) is the threshold a gap must beat to escape.

## Hypotheses held here?

The construction is fully general (no hypotheses on X beyond being built backwards with small retained gaps). It refutes the specific Croft claim that "any sequence with small gaps like the primes is Gilbreath". It does **not** refute the possibility that the *primes specifically* (deterministic, with their actual gap structure and non-concentration) are Gilbreath — indeed Eppstein explicitly notes GC "is really telling us that the prime numbers don't have any unlikely hidden patterns of this type encoded within them". So small-gaps alone is insufficient; the run's `two-separation-hypothesis` (non-concentration in a 2-separated set) is one way to carve out a sufficient class.

## Bearing on this run

- Kills any "gap bound alone" proof strategy for a general class — matches the run's `anti-gilbreath-construction` claim and the ROOT.md "does not lean on prime distribution from gap bounds" stance. An invariant proof must use more than the first row's gap bounds.
- The `s_i` (row-sum-minus-endpoints) threshold is a concrete, computable quantity the run could measure on real prime rows (how far above s_i are actual gaps / how often a hypothetical large gap could break out), a possible falsifier-oriented invariant.
- Echoed by CHT 2026 (ref [3]) and by the `{0,3}` exotic examples in Chase 2024.

## Claims

```claim
id: anti-gilbreath-construction
statement: For any unbounded monotone f(n)≥2 there is a sequence X with n-th gap ≤ f(n) whose triangle's right edge is 1 infinitely often and other values infinitely often; constructed backwards so a large surviving gap escapes to the right whenever the gap exceeds the sum of the other entries in its row.
hypotheses: none beyond f unbounded monotone.
holds-here: yes — refutes small-gaps-alone; does not apply to the actual primes specifically.
status: asserted by source (constructive, elementary; also quoted in CHT 2026)
bearing: rules out gap-bound-only proofs; motivates 2-separated non-concentration as the operative hypothesis.
anchor: research/sources/eppstein-anti-gilbreath-sequences.full.md
```
