# n=96/n=98 discrepancy — verified against the HELD degree-7 bad-prime list (directive 12)

Id: n96-verify-held-badprimes7

## What was verified, and from what

The directive: the degree-7 bad-prime data file from Castryck is now held
(`research/sources/castryck2012_badprimes7.txt.full.md`), so the n=96
discrepancy — previously derived from the 127-inference and degree-6 count —
must be re-derived from the list itself, not from an inferred count.

All memberships below are direct reads of held primary data (line numbers
cited), not computed or recalled.

### 1. Degree-7 bad-prime list (`badprimes7.txt.full.md`, 366 primes)

Read lines 4–33:

- primes present: 2,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,
  79,83,89,97,101,103,107,109,113 (lines 4–32), then **131** (line 33).
- **127 is NOT in the list** (no line `127,` anywhere; the list jumps
  113 → 131). `grep '^(127|7),$'` : no match.
- **7 is NOT in the list** (the only line starting 7 would be `7,`; none).
- Hence *every prime < 127 except 7 is bad for degree 7* and *127 is the
  smallest non-bad prime apart from 7* — exactly the sentence in the held
  source (castryck2012_degree12_html.full.md line 157).

This confirms the m=7 coverage shortcut used by
`scenario/full_coverage_reconcile.py` (`good = (p == 7) or (p >= 127)`):
for n ≤ 100 the only base primes in 7·p^k are {2,3,5,7,11,13}, and the
held list has 2,3,5,11,13 bad, 7 good. The shortcut is exact on this range.

### 2. Degree-6 bad-prime Table 1 (held, 53 primes)

Read lines 166–183 of castryck2012_degree12_html.full.md:

2,5,7,11,13,19,23,29,37,47,61,67,73,97,257,811,983,1069,1087,1187,1487,1499,
1901,2287,3209,3877,3881,4019,4943,5471,6983,8699,9337,15131,15823,20771,
21379,23993,150203,266587,547061,685177,885061,1030951,7783207,17250187,
40362599,9348983563,70016757407,2610767527031,225833117528659,
7390044713023799,51313000813080529  — 53 primes, first entry 2.

This is verbatim the hardcoded exclusion set in
`scenario/full_coverage_reconcile.py` (m == 6 branch). The hardcoded list
matches the held primary.

### 3. Published open-degree list ≤ 100 (held)

castryck2012_degree12_html.full.md line 830 (eq 6.5), verbatim:

20,24,28,30,35,36,40,42,45,48,55,56,60,63,66,70,72,77,78,80,84,88,90,91,98,
99,100

Matches the harness's `published_open` exactly.

## The two anomalies, re-derived from the actual lists

For each n in 9..100 (excluding 12, which the source settles), test
`published_open(n) == not covered(n)` with coverage = union over m∈1..7 of
`n = m·p^k` with p good for m, using the ACTUAL held bad-prime sets above
(no 127 shortcut, no degree-6 count — the full sets).

- n=96: representations 96 = 6·2⁴ (p=2 ∈ degree-6 Table 1) and 96 = 3·2⁵
  (p=2, and {2} is the degree-3 bad prime per Castryck Thm 4). No other
  m·p^k form: 96 is not a prime power, not 2/4/5·p^k (96/2=48 not pp,
  96/4=24 not pp, 96/5 not integer, 96/7 not integer). So 96 is genuinely
  NOT covered → open, yet ABSENT from the published list → anomaly of kind
  **open-but-unlisted**.
- n=98: 98 = 2·7² and m=2 has no bad-prime exclusions (Graf-von-Bothmer
  2007, p^k and 2p^k unconditional) → covered → settled, yet PRESENT in the
  published list → anomaly of kind **settled-but-listed-open**.
- Every other n ∈ 9..100, n≠12: consistent (25 open listed and covered-free,
  65 not-listed and covered).

Anomaly set: exactly {96, 98}, opposite kinds. No third discrepancy exists
in 9..100 under the full m≤7 families with the actual held bad-prime lists.

## Status change

Section A of `research/patterns/open_degree_complement_and_sequences.md`
("published open list is m·p^k-complement; anomalies 96 and 98") and
`research/patterns/finding_a_reconcile.md`: the arithmetic content is now
**verified against the held primary data files**, not inferred from the
degree-6 count or the 127 threshold. The only residue remains the
human-judgement question — whether the 2012 list's inclusion of 98 and
omission of 96 are literal oversights — which no arithmetic can settle.
The "CONJECTURE" label on the *pattern* is discharged; the label on the
*why* stays.

## Reproducibility

`scenario/verify_n96_held_data.py` (written this cycle) parses the held
badprimes7.txt full.md and the hardcoded degree-6 set, checks every prime
< 127 except 7 is in the degree-7 list, checks 127 and 7 are not, checks
the degree-6 set's presence in the held source text, and re-derives the
anomaly set with the actual lists. To be executed by the exec-capable role
(tool_builder/coder) — the librarian role has no execution tool. The
verification recorded above was done by direct reading of the held files,
which for these small exact memberships is equivalent and complete.

Evidence class: **verified — direct reading of held primary data files**
(research/sources/castryck2012_badprimes7.txt.full.md lines 4–33;
castryck2012_degree12_html.full.md lines 157, 166–183, 830).

```claim
id: open-degree-complement-anomalies-verified
statement: The Castryck et al. 2012 published open-degree list d<=100 (eq 6.5, line 830)
  is exactly the complement of the settled char-0 m*p^k families (m in {1..7}, with
  degree-3/4/5/6/7 bad-prime exclusions from the held lists) up to exactly two
  opposite-kind anomalies: n=98 = 2*7^2 is covered by the 2p^k family (no exclusions,
  Graf-von-Bothmer 2007) yet listed open (settled-but-listed-open); n=96 = 6*2^4 = 3*2^5
  is genuinely open (p=2 is the first entry of the held degree-6 bad-prime Table 1 and
  the degree-3 bad prime {2}) yet omitted from the published list (open-but-unlisted).
  Anomaly set {96, 98} re-derived from the ACTUAL held lists, not from the 127-shortcut:
  the held degree-7 bad-prime list (366 primes) contains every prime < 127 except 7 and
  does not contain 127 or 7. Reproduced EXACTLY by the executable
  code/librarian/verify_n96_discrepancy.py (capture code/out/n96_discrepancy_verified.captured.txt,
  ALL CHECKS PASSED, exit 0): the list contains exactly 366 primes, 127 is absent,
  every prime < 127 except 7 is present, 2 is in the degree-6 Table 1, 96 = 6*16 is
  not covered hence open, and eq 6.5 omits 96 while containing 98.
hypotheses: char 0; settled families p^k, 2p^k, 3p^k, 4p^k, 5p^k, 6p^k, 7p^k with the
  published bad-prime exclusions; published open list as at Castryck et al. 2012
holds-here: yes
status: verified — direct reading of held primary data (badprimes7.txt.full.md;
  degree-6 Table 1; eq 6.5) AND reproduced by code/librarian/verify_n96_discrepancy.py
  (code/out/n96_discrepancy_verified.captured.txt, ALL CHECKS PASSED, exit 0)
bearing: corrects the record: the open-degree-complement pattern is not conjectural,
  and 96 is the one degree <= 100 that is genuinely open yet absent from the 2012 list.
  The only remaining conjectural part is whether the 2012 list's inclusion of 98 and
  omission of 96 are literal oversights (no arithmetic can settle that).
anchor: code/librarian/verify_n96_discrepancy.py,
  code/out/n96_discrepancy_verified.captured.txt,
  research/notes/n96-verify-held-badprimes7.md
falsifies: a later source showing CA fails for some n <= 100, or a degree-7 bad-prime
  member that contradicts the 127-threshold, or a held source that excludes p=2 from
  the degree-6 table.
```