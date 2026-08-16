# Pattern-finder findings on the run's computed data

Worked from the held sources (`research/sources/`) and the run's own oracle
outputs (`code/out/`). Every integer in this file came out of a program I ran
here, printed above the run, or is quoted verbatim from a held source.

## 1. Scenario-count law: the only clean structure found (VERIFIED)

Castryck et al. 2012 (arXiv:1208.5404, eq. 1.3) state that for degree d=12 the
number of *scenarios* of type 0..10 is

    1, 1023, 28501, 145750, 246730, 179487, 63987, 11880, 1155, 55, 1

(total 678570).  A scenario is a restricted growth string
(s_1,...,s_{d-1}) with s_1=0 and s_j <= max{s_i : i<j} + 1; its type is its
maximal entry.

**Result (conjecture promoted to verified-computational):** for degree d the
number of scenarios of type t equals the Stirling number of the second kind
S(d-1, t+1); the total is the Bell number Bell(d-1).  For d=12 this reproduces
the published row exactly: S(11,1..11) and total Bell(11)=678570.

Verified two independent ways (rule 11):
1. Direct Stirling computation: match == True.
2. Brute-force enumeration of all RGS of length 11 (s_1=0 fixed), counted by
   max value: match == True.  (A first attempt that forgot to fix s_1=0 gave
   4213596 and mismatched — the correction to s_1=0 restored the exact match,
   which is itself a check that the count really is RGS-with-fixed-first-entry.)
3. Extension over all degrees d=2..8: by-type counts == S(d-1,t+1) and
   total == Bell(d-1) for every d (Bell(1..7) = 1,2,5,15,52,203,877).

Catalogue: the sequence S(11,k) is A011560 (Stirling second kind, row 11);
the triangle is A008277.  So this particular row is a catalogued fact, not a
new sequence — but the *law* (scenario counts by type = Stirling row of d-1,
total = Bell(d-1)) is a clean, exact structural statement about the Casas-Alvero
scenario framework, and it holds for every degree I could check (d=2..8 and
d=12).

Why it matters: the scenario framework is Catastryck et al.'s combinatorial
classification of possible counterexamples.  Knowing the count of degree-d
scenarios by type is S(d-1,t+1) tells a later pass how large the scenario
space is before any determinant constraint is applied, and pins the total as
Bell(d-1).

## 2. Reduced scenario list for d=12 (IRREGULAR — no structure found)

The reduced list (eq (3) of the same source) is the count of scenarios of each
type 0..10 that survive the Theorem-2 determinant constraint:
   0, 48, 1668, 8172, 11586, 6298, 1469, 146, 5, 0, 0   (total 29392).

- analyze_sequence: differences never become constant (not a low-degree
  polynomial).
- find_linear_recurrence (order up to 5): no constant-coefficient linear
  recurrence fits all 11 terms.
- oeis_lookup: no entry matches.
Conclusion: no exploitable closed form; the structure, if any, must come from
the problem's determinant constraint, not from a catalogue.

## 3. Bad-prime count per degree (IRREGULAR — no structure, cannot extend)

Count of bad primes for degree d=3,4,5,6,7 (Castryck 2012):
   1, 3, 9, 53, 366
- find_linear_recurrence (order up to 3): none.
- oeis_lookup: no match.
- ratios 3, 3, 5.89, 6.91 — no simple growth law.

Tried to extend to d=8: the exact classification via the J_T minors criterion
needs the gcd of C=376740 minors (the run's own ledger flags this as
infeasible: C=( (8²−8)/2 choose 6 ) = 28 choose 6 = 376740).  The cheap
sufficient criterion `p | (d choose i) − 1 ⟹ p bad for d` (Schaub-Spivakovsky
`bad-prime-criterion`) gives for d=8 only {3,5,7,11,23} — a weak lower bound.
Calibrated against known lists: it captures only 1/1 (d=3), 2/3 (d=4), 2/9
(d=5), 4/53 (d=6) of the true bad primes.  So the sequence cannot honestly be
extended here; the honest report is that d=8's full set remains open.

## 9. Open-degree list vs settled-family coverage — CORRECTED comparison (VERIFIED)

Re-check of `scenario/verify_open_degrees.py` per a steering directive
(config/directives.jsonl).  The current on-disk script already uses the correct
set-difference comparison (pred vs published via only_in_pred/only_in_pub), not
an inverted collector.  An independent harness
(`scenario/verify_open_degrees_check.py`) implements BOTH comparisons:

- **Correct consistency** for a single n is `pub_open(n) == (not covered(n))`;
  a genuine mismatch is `pub_open == covered`.
- **Negative controls** (asserted to hold): n=16 (settled 2^4), n=20 (open
  4*5), n=28 (open 4*7) all land on the CONSISTENT side of the correct
  comparison; each would be FALSELY flagged by the old `pub != cov` comparison
  (which flagged 89 of 90 degrees, every n in 9..27 included).

**Result: exactly TWO genuine discrepancies** over n in (9,100]\{12}, both
verified against the verbatim published list (castryck2012 eq 6.5) and the
source's bad-prime data:

- **n=98**: published open list INCLUDES 98, but 98 = 2·7^2 is covered by the
  2007 `2p^k` family (m=2, p=7, no bad-prime exclusion).  A settled degree
  sits on the published *open* list.
- **n=96**: published open list OMITS 96, but no `m·p^k` family (m≤7) covers
  it: 96=3·2^5 needs p=2 (BAD for 3), 96=6·2^4 needs p=2 (BAD for 6 — the
  d=6 bad-prime list's first entry IS 2, verified in the source), and 96 is
  neither a prime power nor 2/4/5/7·p^k.  So 96 should be open per the
  families, yet is absent from the published list.

Both discrepancies hinge on the 6/7-family bad-prime handling and the exact
list transcription (verified verbatim), NOT on a predicate error: the coverage
predicate correctly makes 20=4·5 and 28=4·7 open because p=5, p=7 are 4p^k
bad-prime exclusions.  Recorded so a later pass does not re-derive the open
list from the families and quietly "fix" 96 and 98 as if the predicate were
wrong.

## 4. Stirling/Bell law extended past every degree on disk (d=13,14,15 — VERIFIED)

Re-checked the same law by brute force at d=13, 14, 15 (n = d−1 = 12,13,14),
all new degrees beyond the run's earlier d=2..8 and d=12:

  d=13: S(12,1..12) row == brute RGS counts by max; total Bell(12) = 4213597
  d=14: S(13,1..13) row == brute RGS counts by max; total Bell(13) = 27644437
  d=15: S(14,1..14) row == brute RGS counts by max; total Bell(14) = 190899322

Held at every new degree checked (`scenario/check_d13.py`, `scenario/check_d14_15.py`).
This is the classical RGF↔set-partition bijection: an RGS of length n with
max entry t counts set partitions of an n-set into t+1 nonempty blocks, the
Stirling row (A008277).  So the law is a catalogued fact, exact for all d —
not a fit that could break later.

## 6. Fixed-type columns are C-finite, order t+1 (NEW, DERIVED not fitted — VERIFIED to d=120)

Refining section 1: holding type t fixed and letting degree d grow, the count
S(d-1, t+1) as a function of d satisfies a constant-coefficient recurrence of
exact order t+1 whose characteristic polynomial is prod_{j=1}^{t+1}(x - j),
i.e.

    a(n) = e_1 a(n-1) - e_2 a(n-2) + ... + (-1)^t e_{t+1} a(n-t-1)

with e_r the elementary symmetric sums of {1..t+1}.  This is DERIVED, not
guessed: it follows from the exact closed form
S(n,k) = (1/k!) sum_{j=0}^k (-1)^(k-j) binom(k,j) j^n, which writes the column
as a Z-linear combination of the exponentials 1^n,...,k^n.

Concrete verified rows (find_linear_recurrence independently recovered the
exact same coefficients):
  t=0 (k=1): a(n)=a(n-1) [char x-1]
  t=1 (k=2): a(n)=3a(n-1)-2a(n-2)            [2^(d-2)-1; the catalogued A000225 / Mersenne]
  t=2 (k=3): a(n)=6a(n-1)-11a(n-2)+6a(n-3)
  t=3 (k=4): a(n)=10a(n-1)-35a(n-2)+50a(n-3)-24a(n-4)
Held EXACTLY through degree d=120 for every type t=0..8 (scenario/attack_eigen_recurrence.py).

Boundary: the TOTAL column (Bell(d-1), sum over all types) does NOT satisfy any
constant-coefficient recurrence (find_linear_recurrence up to order 8 returns
none; Bell numbers are the classic non-C-finite example).  So the C-finite
structure is exactly per-column, and is lost in the aggregate.

Distance of the claim: it is a theorem (derived from the exact Stirling closed
form), not a conjecture.  The numerical hold to d=120 is an independent check
that the derivation is right, not the evidence for it.

## 8. Bad-prime-CRITERION count per degree d=2..40 (IRREGULAR — no structure, recorded as dead end)

NEW data from `scenario/criterion_counts_extended.py` (output printed in
code/out/commands.log), an extension of section 3's criterion.  Count of
primes p satisfying the Schaub-Spivakovsky sufficient bad-prime criterion
`p | binom(d,i) - 1` for some 1<=i<=d-1, for d=2..40:

    0, 1, 2, 2, 4, 4, 5, 4, 7, 7, 10, 8, 11, 11, 13, 13, 14, 13, 18, 16,
    19, 20, 20, 17, 21, 26, 23, 25, 27, 26, 31, 28, 33, 39, 37, 35, 37,
    43, 39

(distinct primes dividing the product over i of (binom(d,i)-1)).
- find_linear_recurrence (order up to 12): no constant-coefficient linear
  recurrence fits all terms.
- analyze_sequence: differences never become constant within 12 levels (not a
  low-degree polynomial).
- oeis_lookup: no entry matches.
Conclusion: no exploitable closed form/recurrence.  This is a LOWER-BOUND
subset of the true bad primes (calibration: captures only 1/1 d=3, 2/3 d=4,
2/9 d=5, 4/53 d=6), so it is a separate object from section 3's true bad-prime
count (1, 3, 9, 53, 366, which was already recorded irregular).  Recorded so
nobody re-searches either the criterion-count or the true bad-prime-count.

## 7. OPTIONAL cross-check note (earlier numbering preserved)

A second restricted list in the same source (research/sources/castryck2012_degree12_html.full.md,
around line 777): the list closed under descendants after imposing s_1≠s_11,
s_3≠s_9, s_4≠s_8 and the determinant condition (omitting the Proposition 8
contribution):

  0, 6, 718, 5210, 8918, 5404, 1352, 141, 5, 0, 0   (total 21754)

- analyze_sequence: differences never constant within 10 levels (not low-degree
  polynomial).
- find_linear_recurrence (order up to 5): none.
- oeis_lookup: no entry matches.
Like the eq(3) reduced list (section 2), this list has no exploitable closed
form; the structure, if any, lives in the problem's determinant condition, not
in a catalogue.  Recorded so nobody re-searches either restricted list.
