# Pattern-finder fifth pass — exponent-residue structure of the survivors, mod powers of 3

Follow-on to `regularity_findings_4.md`. Prior passes established that the
survivor *exponents* `A_k` (residues `mod 2·3^(k-1)` whose `2^r mod 3^k` has low
`k` ternary digits in `{0,1}`) fill **every even class mod `2^m`** (no 2-adic
modular obstruction). This pass asks the symmetric question in the other
direction: do survivor exponents concentrate in, or avoid, any class **mod
powers of 3**? Prior passes never tested the `3^j` modulus directly.

All numbers below come from the exact survivor-lift program
(`pattern_fresh5.py`, `pattern_residues*.py`), which never materialises `2^n`
as a big integer — it lifts `A_k → A_{k+1}` by testing the three lifts
`r, r+L, r+2L` (`L = 2·3^(k-1)`) at digit position `k`. Verified to `k <= 24`.

## Recon firmed standing facts (fresh data, k <= 24)

- `|A_k| = 2^(k-1)` exactly for k = 1..24 (the sieve-count obstruction, intact).
- Every survivor exponent is even.
- Witnesses 0, 2, 8 present at every k (k >= 1, 2, 3 respectively — witness 8
  only appears once the period covers it, as expected since it is not ≡ 0 mod
  small periods).
- Nesting: `A_k mod 2·3^(k-2) = A_{k-1}` for all k (each level is a strict
  refinement of the previous — the survivor tree never dies, never merges).

## NEW — the exact regularity that holds

**`|A_k mod 3^j| = 2^j` for every `k > j`** (checked j = 1..12, k = j+1..24, all
hold). The `2^(k-1)` survivor exponents project onto exactly `2^j` distinct
classes modulo `3^j`, and this count is *independent of k* as long as `k > j`.

Numerically (k = 20): j=1→2 classes, j=2→4, j=3→8, j=4→16, j=5→32, j=6→64,
j=7→128, j=8→256, j=9→512, j=10→1024, j=11→2048, j=12→4096 = `2^j` each.
This holds already at the minimal k = j+1 (k=2,j=1: 2; ...; k=9,j=8: 256),
independent of how far above j the level k is.

**Nesting in j.** The mod-3^(j-1) reduction of the mod-3^j classes equals the
mod-3^(j-1) classes exactly (checked j<=12): the projected class sets form a
nested tower, one well-defined "2^j-leaf Cameron-Erdos-style" object at each
3-adic precision.

**Honest interpretation — exact count, NOT a density obstruction.** This is an
exact counting fact over `2^(k-1)` survivors, but it is *not* "maximal spread"
in any meaningful density sense: the exponent domain mod `3^j` contains
`(3^j + 1)/2` even residues, far more than `2^j`, so `2^j` is a *collapse* of
the `(3^j+1)/2` even exponent classes, not a filling. Combined with the prior
2-adic fact (fill every even class mod `2^m`), the honest summary is: there is
**no modular-valuation obstruction mod powers of 2 or 3** — no congruence
class mod `p^k` that the survivor exponents avoid, consistent with the sieve
never closing by counting (SIEVE-EXACT-COUNT). But it is also **not** a
closed-form identification of the survivor exponent set. The classes are
`{0,2,8,15,18,20,24,26} mod 27`, which is neither the value-domain
digit-{0,1} set nor any per-place digit-{0,1} condition (see below).

## The conceptual trap (why the obvious "digit-{0,1} set" match is wrong)

Tempting hypothesis (attack): "the survivor exponents mod `3^j` are exactly the
elements of `[0,3^j)` whose *ternary digits* lie in `{0,1}`". **This is false**,
and it is false for a reason worth stating: the survivor *exponents* and the
*values* `2^r mod 3^j` live in different worlds. An exponent `r mod 3` being in
the survivor set means `r` is even (so `2^r ≡ 1 mod 3`, unit digit 1), giving
exponent classes `{0,2} mod 3`, not the value digit-{0,1} set `{0,1} mod 3`.
The two are only related by the 3-adic exponential map `r ↦ 2^r mod 3^j`, which
is highly non-linear. Any claimed "the survivors are the digit-{0,1} classes"
statement must say which domain (exponent or value) it is about, or it is
conflating them. Recorded to stop a future pass making the same comparison.

## What was refuted this pass

- **Mixed-radix digit-{0,1} characterization of survivor exponents.** The
  natural coordinate system for `A_k` is the mixed radix with place values
  `2·3^(i-1)` (that is how the lift `r → r + j·2·3^(i-1)` builds the tree). The
  guess "a survivor exponent is exactly one whose mixed-radix digits are all in
  `{0,1}`" is **false**: the proportion of survivors violating it tends to 1
  (k=16: 32308/32768 ≈ 0.986). This is the cleanest precise statement of the
  earlier qualitative finding ("the excluded child is asymptotically uniform,
  not a simple residue function") — the survivor exponents are emphatically
  NOT characterised by a per-places digit-{0,1} condition.
- `|A_k mod 3^j| = 2^j` is an exact COUNT (nested in j) but is NOT an
  identification with the value-domain digit-{0,1} set: exponent survivor
  classes mod 27 = {0,2,8,15,18,20,24,26}, whereas the value digit-{0,1} set
  mod 27 = {0,1,3,4,9,10,12,13}. The two domains (exponents r and values 2^r)
  are related only by the non-linear 3-adic exponential map — a
  domain-conflation trap recorded here so nobody proposes it again.

## What the tools did NOT find (negatives, recorded so nobody searches again)

- `half(k)` = #{r in A_k : r < 2·3^(k-1)/2}, the count of survivors below half
  the period: 2,4,7,13,21,37,70,139,267,525,1041,2046,4100,8199,... —
  `find_linear_recurrence` finds no order <= 6 recurrence; `analyze_sequence`
  no polynomial fit; **not in OEIS** (lookup run).
- `max_survivor(k)` = {0,2,8,42,150,474,1446,4362,13110,...} — no order <= 8
  recurrence, not polynomial, **not in OEIS** (lookup confirmed absent).
- Mixed-radix-violation-count sequence 1,3,13,37,88,198,433,923,... — **not in
  OEIS**.

## Standing exact results (unchanged)

- PROVED: c1(n) even for all n >= 1.
- PROVED: c0 ≡ c2 + L(n) (mod 2).
- PROVED: |A_k| = 2^(k-1); sieve cannot close by counting.
- PROVED: c(n) = 0 ⟺ digit_free(2^n) (carry reformulation).
- REFUTED: various (c0≡c2 mod 2; #{c0 odd}==#{c2 odd}; max-survivor deficit
  fixed; mixed-radix characterization; value-digit-set identification).
- NEGATIVE: no low-order linear recurrence / polynomial / OEIS match for c0,
  c1, c2, carry-count, half-count, max-survivor.

## Why this matters for the symbolic-invariant route

The deliverable (GOAL.md) is a statistic Phi on the orbit {2^n} that is
preserved by ×2 and violated by the digit-{0,1} set S. Every congruence-mod-p^k
candidate is now closed on both flanks: survivors fill all even 2-adic classes
and all 2^j 3-adic exponent classes. So Phi cannot be any residue function; it
must be a statistic that the *value sequence itself* 2^n separates from the
tail — e.g. a carry/transducer path statistic, or a statistic distinguishing the
three known survivors' digit paths from all longer digit-avoiding candidates
(which do not exist as integers >8 but do exist as residues at every finite
precision). The middle-digit region (beyond Dimitrov–Howe's 26-ones bound) is
where any such statistic must act.
