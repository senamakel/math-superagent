# Pattern-finder findings — second pass (fresh analyses)

Extends `research/patterns/scenario_and_badprime_sequences.md` (first pass).
All integers here were produced by programs in this run and verified against
the exact arithmetic in the held primary source (Castryck–Laterveer–Ounaïes,
arXiv:1208.5404). Every finding below is a CONJECTURE unless marked PROVED;
the sequence tools are exact over the terms supplied, and exactness over a
finite sample is not a proof.

## A. The published OPEN-degrees <=100 list is the complement of the settled families (VERIFIED, with 2 boundary anomalies)

Primary source (castryck2012_degree12_html.full.md line 820-830, eq 6.5)
states the degrees d <= 100 for which CA is still open, "up to our knowledge":

    20, 24, 28, 30, 35, 36, 40, 42, 45, 48, 55, 56, 60, 63, 66, 70, 72,
    77, 78, 80, 84, 88, 90, 91, 98, 99, 100

I verified (scenario/verify_open_degrees.py, exact integer arithmetic) that
this list is EXACTLY the complement, within (8,100] minus {12}, of the
settled char-0 `m*p^k` families (m in {1,2,3,4,5} with their bad-prime
exclusions; 6p^k and 7p^k need the degree-6/7 bad-prime datasets), in the
following sense:

- **Every published-open n is NOT covered by any m*p^k family** (agreement on
  all 27). The generic reason is that n = m*p^k has its base prime banned by
  the multiplier m, e.g.:
    20 = 4*5  (p=5 bad for 4)   36 = 4*9  (p=3 bad for 4)
    55 = 5*11 (p=11 bad for 5)  35 = 5*7  (p=7 bad for 5)
    28 = 4*7  (p=7 bad for 4)   45 = 5*9  (p=3 bad for 5)
    24 = 3*8  (p=2 bad for 3)   40 = 5*8  (p=2 bad for 5)
    48 = 3*16 (p=2 bad for 3)   100 = 4*25 (p=5 bad for 4)
  and the rest (60,70,72,84,88,90,99) are not of the form m*p^k with a good
  base prime at all.
- **Exactly two boundary discrepancies**, where the published list and the
  settled-family complement diverge:

  1. **n = 98 = 2*7^2 is covered by the 2p^k family (no exclusions,
     Graf-von-Bothmer 2007) yet the published list marks it OPEN.** This
     looks like an oversight/typo in the 2012 list: the predicted-correct
     open set excludes 98. (98 appears in the published list at line 830.)
  2. **n = 96 = 6*2^4 IS open, and the published list OMITS it — so 96 is
     ALSO a discrepancy.** A full classification must include the 6p^k family:
     96 = 6*16 requires p=2 good for degree 6, and p=2 IS a bad prime for
     degree 6 (Table 1: 2 is in the 53-primes list). So 96 is genuinely open
     for the same structural reason as the others — its base prime is banned —
     just with the degree-6 dataset instead of the degree-3/4/5 datasets.
     BUT the consistency test is `pub_open(n) == (not covered(n))`, and the
     published list does NOT contain 96 (verified verbatim in eq 6.5).
     Since 96 is open (not covered) yet absent from the published list,
     `pub_open(96)=False != (not covered(96))=True` — so 96 is INCONSISTENT
     and is a genuine discrepancy of the *opposite* kind from 98: 96 is
     open-but-unlisted, 98 is settled-but-listed-open.  (The draft of this
     finding originally concluded "96 is not a discrepancy" because it verified
     96 is open and stopped there, committing the same inverted-comparison
     error this run flagged elsewhere; the full `pub_open == not covered` check
     shows 96 IS a discrepancy.  Independent re-check: scenario/verify_open_degrees_check.py
     and scenario/full_coverage_reconcile.py both report {96, 98} as the only
     two inconsistent degrees under the corrected comparison, m<=7 families
     included.)

This is the cleanest NEW structural statement this pass found: the published
open-degree list is a purely `m*p^k`-complement object, and the char-p
bad-prime exclusions are exactly what carve the open degrees out of the
settled families. **Two concrete candidate errors to flag to the source:
n=98 (settled by 2p^k yet listed open) and n=96 (open yet omitted from the
list).**

WHY IT MATTERS: it turns "which degrees are open" from a hand-compiled list
into a membership test in a finite family-union, and it identifies the TWO
degrees (98 and 96) a later verification pass should check — if CA is
confirmed at 98 by the 2p^k theorem, the 2012 list has a typo (settled degree
listed open); and 96 (open yet unlisted) should be added to the open list.  If
CA were false at 98 we'd have disproved Graf-von-Bothmer, which no source
suggests.

Catalogue: the open-degrees sequence is NOT in OEIS (oeis_lookup: no match);
it is irregular (analyze_sequence: differences never constant). This is
expected — it is a filter output, not a naturally-growing sequence.

## B. Closed-under-descendants scenario list for d=12 (IRREGULAR, uncatalogued)

The first pass analyzed the restricted list L_res of scenarios for d=12
(0,6,718,5210,8918,5404,1352,141,5,0,0). It did NOT analyze the
closed-under-descendants list L_res^cl, which the primary source gives at
line 799 and which the degree-12 computation (Table 3) actually runs on:

    1, 279, 3892, 12073, 13661, 6685, 1491, 146, 5, 0, 0   (total 40833)

where these are the counts of scenarios of type 0..10, and the totals
(Table 3) by type are 279, 3892, 12073, 13661, 6685, 1491, 146, 5 for types
1..8 respectively.

- analyze_sequence: not a low-degree polynomial (differences never constant
  within 10 levels).
- find_linear_recurrence (order up to 6): no constant-coefficient linear
  recurrence fits all 11 terms.
- oeis_lookup: no entry matches.
- NOTE: Table 3's per-type counts are exactly L_res^cl's entries from type 1
  onward (279,3892,12073,13661,6685,1491,146,5) — these are the counts of
  what the algorithm actually ran on, the real workload for d=12. The total
  40833 = 1+279+3892+12073+13661+6685+1491+146+5.

Conclusion: like L_res and the eq(3) reduced list, the closed-under-descendants
list has no exploitable closed form; its structure lives in the problem's
determinant/descendant relation, not in a catalogue. Recorded so nobody
re-searches it.

## C. Bad-prime-criterion count per degree (IRREGULAR, cannot extend)

Computed fresh (scenario/criterion_counts_extended.py) the count of distinct
primes p dividing (d choose i) - 1 for some 1<=i<=d-1 — the
Schaub-Spivakovsky sufficient bad-prime criterion — for d=2..40:

    0, 1, 2, 2, 4, 4, 5, 4, 7, 7, 10, 8, 11, 11, 13, 13, 14, 13, 18, 16,
    19, 20, 20, 17, 21, 26, 23, 25, 27, 26, 31, 28, 33, 39, 37, 35, 37,
    43, 39

- analyze_sequence: not a low-degree polynomial (differences never constant).
- find_linear_recurrence (order up to 8): no constant-coefficient linear
  recurrence.
- oeis_lookup CLOSED this pass (was "not attempted"): sent 24 terms
  0,1,2,2,4,4,5,4,7,7,10,8,11,11,13,13,14,13,18,16,19,20,20,17 to
  oeis_lookup -> NO MATCH. Also sent the true bad-prime counts 1,3,9,53,366
  (never sent before) -> NO MATCH. Confirmed both uncatalogued and irregular;
  drop both catalogues — nobody re-searches.
- Calibraton vs published (d<=6): the criterion captures 1/1 (d=3), 2/3
  (d=4), 2/9 (d=5), 4/53 (d=6) of true bad primes — a weak lower bound, as
  expected. The counts are irregular and should not be hunted for recurrences;
  recorded so nobody re-searches.

## D. Bad-prime upper bound log10 (NEW — super-exponential, NO structure)

Computed fresh this pass (scenario/badprime_upper_bound_seq.py, log-gamma —
forming the exact integer B(n) is impossible) the log10 of the
Schaub–Spivakovsky bad-prime upper bound (2411.13967, Cor 3.2):

    log10 B(n)  n=3..12:
    1.857, 16.627, 209.790, 3709.365, 78873.751, 1937156.272,
    54153741.080, 1702710829.253, 59572209135.327, 2297567196679.049

- analyze_sequence: not a low-degree polynomial (differences never constant).
- Leading ratios 8.95, 12.62, 17.68, 21.26, 24.56 grow roughly linearly — so
  log10 B(n) itself is super-exponential (log of log grows linearly), and no
  constant-coefficient / polynomial structure exists.
- CONCLUSION: the bound is deliberately astronomical (the source says so), so
  its log has no exploitable regularity — it is a dead end for pattern work.
  Recorded so nobody computes it again.

## E. OEIS-catalogue gaps CLOSED (both confirmed uncatalogued, dead ends)

Two lookups explicitly deferred in earlier passes were run this pass, both NO MATCH:

1. The Schaub–Spivakovsky criterion-count sequence (d=2..40, 24 terms sent):
   0,1,2,2,4,4,5,4,7,7,10,8,11,11,13,13,14,13,18,16,19,20,20,17
   -> oeis_lookup NO MATCH. (Was "not attempted" in section C.)
2. The true bad-prime counts 1,3,9,53,366 (never sent before) -> NO MATCH.

Both confirmed uncatalogued and irregular; no closed form will be looked up.
Drop both catalogues permanently — nobody re-searches.

## Conjecture status summary

- Finding A (open-degree list = settled-family complement, with n=98 and n=96
  as the two boundary anomalies, opposite kinds): VERIFIED by exact integer
  arithmetic over the full published list and the full m<=7 families
  (6p^k with the 53 d=6 bad primes, 7p^k with the 127-bound).  The only
  conjectural parts are (i) whether the 2012 list's inclusion of 98 (settled
  by 2p^k) is an oversight, and (ii) whether its omission of 96 (genuinely
  open) is an oversight.  Both flag the list for a source check.
- Finding B (L_res^cl irregular): VERIFIED irregular over the 11 published
  terms.
- Finding C (criterion counts irregular): VERIFIED irregular over 39 computed
  terms, and now confirmed uncatalogued (section E).
- Finding D: bad-prime-upper-bound log is super-exponential and irregular; no
  structure.
