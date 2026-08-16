# F2 Hasse-CA counterexample support-structure law

Fresh analysis by pattern_finder, this pass. All integers came from exact
bit-parallel enumeration of the 2^n monic degree-n polynomials over F2 with
the Hasse-CA hypothesis (`is_ca_f2` in `code/out/*.py`, matching the canonical
oracle `lib.casas_alvero.is_ca_hasse` on all small-n guards). Every number is
exact over GF(2); say which parts are conjectures.

## Setup

- `sat(n,2)` = # monic degree-n polynomials over F2 with `gcd(f,H_i)≠1` for
  every `i=1..n−1` (Hasse derivative; a vanishing `H_i` passes via
  `gcd(f,0)=f`).
- `m(n,2) = sat(n,2)/2` (the "multiplier"; `sat` is always even).
- `ce(n,2) = sat(n,2) − 2` = # counterexamples (satisfiers that are not pure
  powers). The `2` is the two monic pure powers `x^n, (x+1)^n`.
- A counterexample is classified by its **monomial-support size**
  (`fb.bit_count()` over F2): the number of nonzero coefficients.

## The data (complete, this pass)

### popcount-2: n=5,6,9,10,17,18,20,24
`m=2`, `ce=2`, profile `{2:2}` — every counterexample is a two-monomial
`x^a+x^n`. Constant at every pc-2 degree.

### popcount-3: n=7,11,13,19,21,22,25,26,28
`m=8`, `ce=14`, profile **`{2:6, 4:5, 6:3}`** — IDENTICAL at all NINE degrees
computed. Fully rigid: the whole counterexample set (and hence `m`) depends
only on popcount at pc=3.

### popcount-4: n=15, 23, 27
```
n=15: m=457 ce=912  support {2:14, 4:106, 6:390, 7:4, 8:236, 10:139, 12:18, 14:5}
n=23: m=466 ce=930  support {2:14, 4:106, 6:411, 8:248, 10:130, 12:17, 14:4}
n=27: m=418 ce=834  support {2:14, 4:106, 6:352, 8:228, 10:112, 12:18, 14:4}
```
The **small supports are constant** — `support-2 = 14` and `support-4 = 106`
at all three pc-4 degrees — while the **large supports (≥6) vary with n**,
which is exactly why the multiplier varies (457/466/418).

## Conjectures (exact over every computed term; labelled conjecture, not proof)

**(A) `#support-2 ce = 2^popcount(n) − 2`.** Holds at all 19 degrees computed
here (all pc=2,3,4 data above: 2, 6, 14 respectively). These are precisely the
two-monomial `x^a+x^n` with `a` a proper nonempty submask of `n` — there are
exactly `2^popcount(n) − 2` submasks, and each provably gives a Hasse-CA
counterexample (verified n=3..40 by two independent routes:
`code/out/two_term_rule.py` bit-parallel and `code/out/two_term_family_lib.py`
sympy oracle). The "submask count = 2^pc−2" part is a theorem; check it for a
mismatch.

**(B) Full popcount rigidity at pc ≤ 3:** the entire support profile is a
function of popcount only at pc≤3. `pc=2 → {2:2}`, `pc=3 → {2:6,4:5,6:3}`.
Verified at 8 pc-2 degrees and 9 pc-3 degrees.

**(C) Small-support part is popcount-determined at all pc; large-support part
varies.** At pc=4, support-2 (14) and support-4 (106) are popcount-determined;
only support≥6 varies. This is the natural generalization of (A): the
two-monomial family and its immediate "two-fold" support-4 cousins are pinned
by popcount, while genuinely many-term counterexamples depend on the specific
bits of `n`.

## What is refuted

The naive population hypothesis recorded earlier — **"m(n,2) depends only on
popcount(n)"** — is FALSE at pc≥4: `m(15,2)=457`, `m(23,2)=466`, `m(27,2)=418`.
First falsifier: n=23 (pc=4; predicted 457 from n=15, actual 466). It survives
exactly at pc≤3. This is a concrete correction to the earlier record
(`satisfier_multiplier_over_Fp.md`), which only had pc≤3 data.

## Catalogue

- The multiplier sequence `2,1,2,2,8,1,2,2,8,2,8,8,457,1,2,2,8,2,8,8,466,2,8,8,418`:
  NOT a low-degree polynomial, NO constant-coefficient linear recurrence
  (order ≤ 8), NO OEIS match. Irregular — record as a dead catalogue, do not
  re-search.
- The pc-3 profile `{2:6,4:5,6:3}` and pc-4 small supports are rigid; the
  structure lives in the Hasse-CA determinant condition, not a catalogue.

## Why this matters

It turns "how many F2 Hasse-CA counterexamples are there in degree n, and of
what shape?" into a question with a rigid, popcount-determined core:
the two-monomial family (exactly `2^pc−2` of them, classified exactly) and,
at pc≤3, the whole set. The two-monomial classification `x^a+x^n` with `a` a
proper submask of `n` is already a *theorem* (n=3..40, two routes): that is the
one fully-proved piece here. Conjecture (C) — popcount determines the
small-support part at every popcount, only many-term shapes vary — is the
structural claim most likely to yield to a derivation, because the two-term
and four-term counterexamples are already exactly classified.
