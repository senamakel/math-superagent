# Rejected: `code_refute_uc_with_three_set.p.json` — encoding bug, not a refutation

**Status:** DELETED (replaced by this note). The artifact `finding=refuted,
CounterSatisfiable` must not be treated as a mathematical result.

## The claimed finding

The artifact purported to refute the rung R-uc-with-three-set ("every
union-closed family containing a 3-element set has an abundant element") by a
finite-first-order counter-model on a 4-element domain.

## Why it is an encoding bug, not a counterexample — three independent reasons

1. **It contradicts a verified theorem.** UC is machine-verified for all
   families on a ground set of up to 12 elements (Bošnjak–Marković n=11;
   Vučković–Živković n=12 — claims `bosnjak-markovic-11`, `verified-n12-comp`
   in CLAIMS.md). A genuine union-closed counterexample on ≤4 ground-set
   elements would refute that whole verified range. The prior probability of a
   model finder overturning a machine-verified theorem is ~0; the prior that
   the *encoding* is wrong is high.

2. **The exact oracle rejects it.** I ran every union-closed family on `[n]`
   (`n ≤ 4`) that contains at least one 3-element set through the canonical
   oracle `lib.uc` (exhaustive, exact integer counts):
   ```
   n=3: 90 union-closed families contain a 3-set, 0 lack an abundant element
   n=4: 4838 union-closed families contain a 3-set, 0 lack an abundant element
   ```
   Every such family has an abundant element. **No counterexample exists at
   this size** (`code/out/three_set_sanity.py`, declared exponential
   oracle-bound n≤4).

3. **The TPTP encoding has a concrete cardinality bug** (the directive's
   predicted failure, candidate (c)). The axioms enumerate 6 member *slots*
   `s1..s6` and a `slots_distinct_sets` axiom intended to force them to be
   distinct *as sets*. But the finder returned the counter-model
   ```
   s1 = s2 = s3 = s4 = fmb_$i_1
   s5 = fmb_$i_4,  s6 = fmb_$i_3
   ```
   i.e. **the 6 "members" collapse onto the same few domain values**, so `|F|`
   is not 6 at all. Every constraint that depends on distinctness of the three
   witnesses — "some element is in ≥ |F|/2 = 3 of the 6 members" — is
   **vacuous** because `I≠J≠K` can never name three distinct members. The
   "no abundant element" conclusion is an artifact of a collapsed domain, not
   a statement about a 6-member family.

   Mechanically: `slots_distinct_sets` says two distinct *slots* differ on some
   element, but when the model maps distinct slots to equal domain values the
   antecedent `I=J`-path is satisfiable, and the finite-domain finder chose
   that collapse to satisfy everything vacuously. First-order finite model
   finding is well known to do this with a numeric cardinality constraint that
   is only encoded as pairwise-distinctness against the SAME finite domain the
   finder may shrink.

**Bearing.** R-uc-with-three-set remains OPEN (`research/WEAKENED.md` lists it
open — correct). This is a known dead end worth recording: a bounded
first-order encoding that carries `|F|` as a slot-count + distinctness axiom
has no protection against domain collapse, so a "CounterSatisfiable" verdict
from it is not credible until the model is re-checked by an exact oracle for
genuine union-closure and genuine abundance. That re-check is now the standard
gate before any such artifact can reach a claim.

**Prevention (recorded so the run stops paying for this).** Any future
finite-model "refutation" of a UC-rung must be gated by `code/lib/uc.py`:
decode the model to an explicit family, `decide_union_closed` it, and compute
`abundance` — before it is allowed to be recorded. The exact oracle is the
authority, and here it confirms: **no** union-closed family on n≤4 with a
3-set is a UC counterexample.
