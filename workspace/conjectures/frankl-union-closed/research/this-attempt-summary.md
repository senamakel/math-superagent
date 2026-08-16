# This attempt — what was executed and established

Run was a continuation of a cold workspace with substantial library sources but
an empty claims ledger. Four programs written and executed, all exit 0.

## 1. The oracle — `code/lib/uc.py` + `code/out/uc_oracle_check.py`

Exact integer bitmask library: `decide_union_closed`, `abundance` (exact counts),
`abundant_elements`, `closure`, `verify_uc_exhaustive(n≤4)`. All checks PASS:
guard 2^[n] density exactly 1/2; singleton abundant; negative-control antichain
rejected; exhaustive no-counterexample n=1..4 (counts 3, 13, 121, 4959 UC
families). n=2 count matched independent hand enumeration (second route).
Brute force declared exponential, oracle_bound=4 (allowed as oracle only).

## 2. The iid-OR barrier — `code/out/iid_barrier_exact.py` (sympy exact)

For X,Y iid product-Bernoulli(p) on {0,1}², ratio R(p)=h(2p−p²)/h(p):
- H(X∨Y)=H(X) exactly iff p ∈ {0, (3−√5)/2, 1} (exact polynomial branch solve).
- At p0=(3−√5)/2: 2p0−p0² = 1−p0 = 1/φ (φ=(1+√5)/2), so R(p0)=1 exactly.
- R(p) ≥ 1 on [0,p0]; first crossover R=1 at p0 (proved by branch solve; the
  R≥1-on-interval is exact-rational grid, labelled numerical).
- **Conclusion:** the iid-OR entropy method certifies no element density above
  (3−√5)/2 ≈ 0.38197. Extremal = product-Bernoulli at p0, NOT the small uniform
  family (whose ratio is ~0.622).
Claim block: `code/out/iid_barrier_claim.md`, status checked.
Verified by a second independent route (mpmath 60-digit) and by the exact
`saturation` equality. Matches sourced literature (AHS arXiv:2211.11731, Pebody).

## 3. Boppana inequality — `code/out/boppana_verify2.py` (sympy exact)

h(t²) ≥ φ·t·h(t), equality exactly at t=1/φ; φ↔(3−√5)/2 = 1/φ² relations proved
exactly. Derivation in `code/out/boppana_verify.md`.

## 4. Contradiction resolution — `research/threads/contradiction-sawin-ahs.md`

The three flagged contradictions are misreads. (3−√5)/2 is the ceiling of the
**iid coupling class**; Sawin/Yu/Cambie/Liu are lower bounds in the strictly
larger **dependent / conditionally-iid** class, which escapes it. Not
contradictory. **Published record to beat: 0.38234 (Yu, Entropy 2023, proved).**
Liu 0.38271 is conditional and unpublished.

## Status

GOAL.md objectives: oracle built (✓), one published result reproduced end to end
(✓, the (3−√5)/2 barrier via exact computation), frontier pinned (✓), and one
precise structural claim stated and checked (✓ — the iid-OR barrier lemma
`iid-barrier-exact`, GOAL.md result class 3 material: a proved barrier for the
iid coupling class, with the extremal object exhibited). Attack on the live
coupling-class gap `G-coupling-half` (UC via dependent coupling) is recorded as
the next step but NOT settled here: the library lacks the Yu/Liu optimization
math to reproduce 0.38234 from primary sources, so that reproduction remains a
gap (research/REQUESTS.md). No UC claim is made.
