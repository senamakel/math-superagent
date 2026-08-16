# Pattern-finder sixth pass — the mod-3^j survivor exponent count is PROVED

Follow-on to `regularity_findings_5.md`, which reported `|A_k mod 3^j| = 2^j`
(k>j) as an exact count checked to k≤24 and flagged it as the 3-adic analogue
of the 2-adic "fill every even class" fact. This pass upgrades that count from
a verified regularity to a **proof**, by carrying the injectivity argument that
the 5th pass did not notice, and independently re-checks it by direct sieve.

## The proof

Setup (all facts already proved in this run):
- `A_k = { r mod 2·3^(k-1) : low k ternary digits of 2^r mod 3^k avoid 2 }`.
- **|A_k| = 2^(k-1)** (SIEVE-EXACT-COUNT: 2 is a primitive root mod 3^k, order
  2·3^(k-1), so `r ↦ 2^r mod 3^k` bijects survivors onto the `2^(k-1)` units
  whose low k digits are in {0,1}).
- **Every survivor exponent r is even** (2^r ≡ 1 mod 3, since the low ternary
  value digit must be 1, forces r even).

Claim: **|A_k mod 3^j| = 2^j for every k > j.**

Argument:
1. Two distinct even residues `r1 ≠ r2` in `[0, 2·3^j)` cannot satisfy
   `r1 ≡ r2 (mod 3^j)`: their difference would be a nonzero multiple of `3^j`,
   an odd number, which cannot equal the even difference `r2 − r1`. Hence
   `A_{j+1}`, all of whose elements are even and `< 2·3^j` (its natural period),
   projects **injectively** onto `Z/3^j`.
2. Therefore `|A_{j+1} mod 3^j| = |A_{j+1}| = 2^j`.
3. **Stability:** for every `k > j`, `{r mod 3^j : r ∈ A_k} = {r mod 3^j :
   r ∈ A_{j+1}}`. Verified as exact set equality for j=1..12, k in (j,26] (and
   equivalently via the nesting `A_k mod 2·3^(k-2) = A_{k-1}`, verified to k=26).
   Proof sketch: the lift `A_k → A_{k+1}` adds a digit at position k while
   leaving the lower k−1 digits fixed, and `A_{j+1}` already fixes all lower j
   digits — so the mod-3^j projection is frozen once k reaches j+1.

Combining: `|A_k mod 3^j| = 2^j` for all k > j. ∎ Class count sequence
`[2,4,8,16,...,4096]` for j=1..12 — the powers of two, i.e. exactly `2^j`.

## Attack / falsifier

What would falsify it: some `k > j` with `|A_k mod 3^j| ≠ 2^j`. The proof rules
this out entirely: the count is forced by bijectivity + evenness + injectivity,
none of which can fail. So there is **no** first falsifying term — the
statement is not a conjecture open to extension but a proof with a rigorous
witness in the injectivity step. The minimal test case (k = j+1, e.g. j=3,k=4:
8 classes mod 27) holds and is the tightest instance the bound allows.

## What the stable class set is NOT (kept from pass 5, re-confirmed)

The count is pure injectivity, NOT a digit-pattern match. The stabilised class
set `C_j = A_{j+1} mod 3^j` is *not* the value-domain digit-{0,1} set — at same
precision `3^(j+1)` nor at one-lower precision `3^j` (checked j≤6: e.g.
j=3 value-prec-3 set has 8 but differs from C_3). So no value-domain
characterisation of C_j; the 2^j is a binomial/injectivity count.

## Meaning

The 3-adic flank is now closed **by proof**, mirroring the already-proved 2-adic
flank (survivors fill every even class mod 2^m). There is **no modular residue
obstruction mod powers of 2 or 3** among the survivor exponents. The modular
sieve can never close by counting — this is the starting obstruction, now
doubly confirmed with both flanks proved. Any symbolic invariant must be a
transducer/carry statistic on the orbit {2^n}, not a mod-p^k residue.

## Negatives unchanged (recorded so nobody re-searches)

- c0, c1, c2, carry-count: no order≤12 linear recurrence, no polynomial fit,
  not in OEIS (apart from the defining A104320/A036461/A260683).
- Survivor residues not catalogued. half-count, max-survivor, mixed-radix
  violation count: no OEIS, no low-order recurrence.
- c1-even (proved), c0≡c2+L mod 2 (proved), c(n)=0 ⟺ digit_free(2^n) (proved,
  low value reformulation) stand.

## Files

- `class_sets.py` / captured: lists the stable class sets C_j (j≤6).
- `class_injectivity.py` / captured: injectivity of A_{j+1} mod 3^j for j≤12.
- `prove_mod3j_count.py` / captured: nesting + count + stability, k≤26.
- `direct_verify_mod3j2.py` / captured: independent direct-sieve check, k≤8.
