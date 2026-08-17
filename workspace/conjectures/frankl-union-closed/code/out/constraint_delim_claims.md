# constraint_delim.py — executed result and claims

<!-- regenerator-trigger -->

What ran: `python3 code/out/constraint_delim.py` (full, 12.8 s, exit 0), capture
`code/out/constraint_delim.captured.txt`. Oracle: `lib.uc.decide_union_closed`
+ `lib.uc.abundance` (exact integer counts); strict abundance test `2*c > |F|`.
Range: n=1..4 exhaustive (guard A102896 3,13,121,4959 and empty-free
1,6,60,2479 pass); n=5 exhaustive over the min-set-size-gt=3 class (2^16
subfamilies); n=6,7 k=3 closure-based construction probes; n=8 the KPT P_3^8
construction rebuilt by hand and oracle-verified.

```claim
id: no-two-abundant-k3-n7-found
statement: Across 190,415 union-closed empty-free k=3 families on ground set
  [7] — the closures of every <=3-generator set from the 99 size>=3 masks, of
  every 4-generator subset of the 35 three-sets, and 20,000 random generator
  sets of size 4..10 (Random(20260708)) — NO family with exactly two
  strict-abundant elements (a (2,3,7)-construction in the sense of
  Kabela-Polak-Teska) was found. Minimum f found: 3, attained already by the
  trivial {{abc}} singleton; the f-distribution is {3:15565, 4:55650,
  5:60417, 6:32600, 7:26183}. KPT Thm 5(2) gives f >= k-1 = 2 at (k,n)=(3,7),
  so the bound is not attained by any family in the probe. n=7 is the FIRST
  ground size at which constraint (C) (n >= 2k+1 for a counterexample) is
  compatible with k=3, and the probe's minimum f = 3 equals, not beats, the
  k=3 floor seen at every n <= 6 (where Thm 5(1) forces f >= k = 3).
hypotheses: F finite union-closed, empty NOT in F, smallest set size k=3,
  ground set [7]; strict abundance = in more than half the sets
  (2*c > |F|); the search is over closure-generated families, not all of 2^[7].
holds-here: yes
status: verified-computational (bounded probe, NOT exhaustive: the space of
  all empty-free k=3 union-closed families on [7] is not fully enumerated —
  the closure generation covers a wide but sample-based slice)
bearing: delimits how close the held minimal-counterexample constraints come
  to forcing UC. A counterexample (f=0) is excluded at n<=12 by
  machine-verified UC (Vuckovic-Zivkovic); at n=7, k=3, constraint (C) no
  longer excludes f=0 and KPT Thm 5(2) gives f>=2, but no f<=2 family was
  found in 190,415 constructions — consistent with the paper's own Thm 6(2)
  existence inequality FAILING at n=7 (it holds at n=8, where P_3^8 attains
  f=2). The genuine open question — does any (2,3,7)-construction exist —
  stays open with a substantial negative probe on record.
ceiling: exhaustive n=7 k=3 enumeration would need 2^99 subfamilies (the
  99 masks of size >= 3 on [7]) — infeasible; the probe is closure-based and
  random, not a proof of absence.
anchor: code/out/constraint_delim.captured.txt (PART 5),
  research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md
  (Thm 5(2), Thm 6)
```

```claim
id: kpt-p38-rebuilt-verified
statement: The Kabela-Polak-Teska P_3^8 two-abundant (2,3,8)-construction
  (their Thm 6(1)) was rebuilt by hand from its description — A = {A subset
  [8] : {0,1} subset A, |A| >= 3} (63 sets), E = {{0,2,4},{0,2,6},{0,4,6},
  {0,2,4,6}}, O = {{1,3,5},{1,3,7},{1,5,7},{1,3,5,7}}, |F| = 71 — and
  verified through the canonical oracle: decide_union_closed -> True,
  empty-free, min set size 3, max set size 8, every element present, counts
  (67,67,35,35,35,35,35,35), exactly 2 strict-abundant elements (0,1) with
  2*67 > 71 and 2*35 < 71. This is the closest the two-abundant construction
  idea reaches for k=3: ground set n=8 = 2k+2, and no f<2 family is possible
  at n<=6 (Thm 5(1): f >= k = 3).
hypotheses: the construction as stated in the paper; n=8, k=3, empty-free.
holds-here: yes
status: verified-computational (oracle recheck of the rebuilt family; the
  construction itself is PROVED in the source)
bearing: corroborates kpt-two-abundant-constructions by direct construction
  and pins the k=3 two-abundant frontier at n=8; the n=7 gap (no f=2 found,
  see no-two-abundant-k3-n7-found) is the live boundary the paper's Thm 6(2)
  inequality does not cover.
ceiling: verification is at n=8 only (the one explicit family); no claim
  about other (2,k,n) pairs is made here.
anchor: code/out/constraint_delim.captured.txt (PART 4),
  research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md
  (Thm 6(1))
```

## Operational note

The Cognee memory server was unhealthy at the time this run finished (two
`remember_memory` calls for these results were accepted-then-dropped, reported
by the tool as "cannot index right now"). The executed result therefore lives
in this file, in `code/out/constraint_delim.captured.txt`, and in CONTEXT.md
(Established + Numbers), NOT in Cognee. A later run that queries memory for
"constraint delimitation / (2,3,7)-construction" and finds nothing should
read this note and the capture rather than re-deriving.

## Decision — the Lean formalisation task (steering directive)

`formalise-gnm-envelope-in-lean` is **deferred, with a recorded reason**. The
envelope theorem IS the cleanest Lean target this workspace has — finite
combinatorics over `Finset (Fin n)` with upward-closed as a predicate, the
size lemma by the maximal-element induction already written in
`code/out/gnm_envelope_finding.md` §Proof, and two explicit constructions —
and `code/lean/` holds only the entropy file. But the task row also says the
envelope is a *suggestion* (directive 17), not an instruction, and the
counterexample-constraint front is the other open GOAL.md job. Running
`constraint_delim.py` (already written, never run, no capture) delivered an
executed result immediately, while the Lean formalisation would spend the
whole remaining run on infrastructure before any math result exists. So: work
the constraint front now (done above), formalise the envelope when a run has
budget to see it through — the notes needed are all on disk. This decision is
recorded here because the task ledger is not writeable by this role.

Also executed in the same run: part 1 (n<=4, 2546 empty-free families) shows
constraints (A) no-degree-1 + (C) n>=2k+1 hold simultaneously in 1848/2546
(72.6%) of families, f=0 never occurs (0/2546, as UC holds at n<=4), and the
minimal excess d = max_x(2c_x - m) is 1, hit by 70 families — the closest any
n<=4 family comes to a counterexample is one element at exactly density 1/2.
Part 2 (n=5, class-exhaustive k>=3): min f = k for k=3,4,5, so KPT Thm 5(1)
is tight there; f=0 count 0. Part 3 (n=6, k=3): min f = 3 over 289,469
constructions, f=0 count 0 (impossible by (C): would need max set size >= 7).