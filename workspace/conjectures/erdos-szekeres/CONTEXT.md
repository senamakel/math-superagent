# Shared context

What this run knows, in its own words. The context curator writes this file and
is normally the only role that writes it; the director amends it on a directive
that changes what every role should know. Nearly every other role is sent it on
every model call. So what is here is what the run knows without going to look,
and what is missing is what each agent rediscovers separately.

It carries what an agent would otherwise rebuild from disk, from the note store,
or from a session it was not present for: established results with their basis,
approaches that died and why, what the computed numbers look like, what durable
memory relates this problem to, and where two accounts disagree. It is not a
catalogue of files — `research/INDEX.md` is that — and not a narration of what
agents did.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). The
file is re-sent on every model call in every role that reads it, so length here
is a bill the whole run pays many times over; a brief past its budget is cut
where it exceeds it on the way into a prompt, with a notice saying so. Link the
file that still holds any detail compressed away — source notes under
`research/summaries/`, untouched full texts under `research/sources/`,
reflections, threads. Durable findings belong in Cognee. A statement nobody can
trace to a source is worth less than no statement.

## Established

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it. Each belief names
what would falsify it.

- **Exact values ES(3..6) = 3, 5, 9, 17.** ES(3)=3 (any 3 non-collinear points);
  ES(4)=5 (Klein's 1930s proof from 5 points); ES(5)=9 (Makai/Turán; Bonnice and
  Lovász hand proofs via the (3,3,2)/(4,3,1)/(3,4,2) lemma); ES(6)=17
  (Peters–Szekeres 2006 computer proof, SAT/backtracking on signature functions).
  *Evidence:* proved (hand) for n≤5, verified-numerically for n=6.
  *Falsified by:* an exact orientation table of 9 points with no convex pentagon,
  or of 17 points with no convex hexagon. `research/ROOT.md` §3.

- **Lower bound and its realizability.** ES(n) ≥ 2^{n-2}+1: blocks T_0..T_{n-2}
  with |T_i| = C(n-2,i), each free of an (i+2)-cap and (n-i)-cup with slopes
  bounded by 1 in absolute value, placed near circle angles θ_i = π/4 − iπ/(2(n-2)).
  Largest convex subset has ≤ n-1 points. Realizable with integer coordinates in
  grid size O(n² log³ n) (Duque–Fabila-Monroy–Hidalgo-Toscano, arXiv:1602.03075).
  *Evidence:* proved. *Falsified by:* a convex n-subset found by an exact
  orientation table in any realization. `research/ROOT.md` §2.

- **Tóth–Valtr binomial bound.** ES(n) ≤ C(2n-5, n-3) + 2. *Evidence:* proved
  (1998). Exact-form, but far above the conjectured 2^{n-2}+1 — it does not
  resolve the constant. *Falsified by:* an n-avoiding set of size
  > C(2n-5,n-3)+2. `research/ROOT.md` §1.2.

- **Asymptotic upper bounds — NOT bearing on the exact conjecture.** Suk:
  ES(n) ≤ 2^{n + 6n^{2/3} log n} for n ≥ n₀ (n₀ a large absolute constant).
  Holmsen–Mojarrad–Pach–Tardos: ES(n) ≤ 2^{n + O(√(n log n))} (current best).
  Both are of the form 2^{n+o(n)}: **asymptotic**, so they cannot settle the exact
  constant ES(n)=2^{n-2}+1. *Evidence:* proved. *Falsified by:* a set violating
  the stated inequality — but as asymptotics they are recorded as context, not as
  tools for the exact conjecture. `research/ROOT.md` §1.4–1.5.

- **Baek–Balko split/decomposable result.** ES_split(k) = 2^{k-2}+1 proved
  exactly (tight threshold for split k-gons); the conjecture holds for
  decomposable sets; the ordered 3-uniform hypergraph generalization is false.
  *Evidence:* proved (SoCG 2025). *Falsified by:* a split-k-gon-free set of size
  2^{k-2}+1, or a decomposable set of 2^{k-2}+1 points with no convex k-gon.
  `research/ROOT.md` §5.1.

- **Cups-and-caps tightness.** f(k,l) = C(k+l-4, k-2) + 1 exactly, and
  ES(n) ≤ f(n,n) = C(2n-4, n-2) + 1. *Evidence:* proved (Erdős–Szekeres 1935;
  tightness per Morris–Soltan). *Falsified by:* a set of f(k,l) points with
  neither a k-cup nor an l-cap. `research/ROOT.md` §1.1.

- **4-point criterion (oracle backbone).** A finite set in general position is in
  convex position iff every one of its 4-subsets is. *Evidence:* proved
  (Erdős–Szekeres 1935). *Falsified by:* a convex set with a non-convex 4-subset,
  or the reverse. Underpins the phase-3 oracle. `research/ROOT.md` §6.

- **Signotope / CC-system foundation (the SAT arm's axioms).** Rank-3 signotopes
  (triple-orientation sign maps with at most one sign change per 4-set) are in
  bijection with simple pseudoline arrangements with a fixed top cell (Felsner &
  Weil 2001); a triple orientation is such an arrangement exactly iff it obeys
  the generalized transitivity law; a realizable point set = a stretchable
  (straight-line) arrangement, and realizability is ∃ℝ-complete
  (Goodman–Pollack–Sturmfels). The CC-system axioms (Knuth: cyclic symmetry,
  antisymmetry, nondegeneracy, interiority, transitivity) are the exact axioms
  the orientation-variable SAT encoders (SMQH, Dumitru, Scheucher, Balko–Valtr)
  post. Abstract CC systems count ~exp(n²) vs ~exp(Θ(n log n)) realizable ones —
  the quantitative realizability trap. *Evidence:* proved (Felsner–Weil primary;
  the CC-system axiom/count statements are asserted-by-secondary-source, Knuth via
  Wikipedia). *Falsified by:* a rank-3 signotope with one sign change per 4-set
  whose marked arrangement is not simple; or a realizable order type failing a
  CC axiom. `research/summaries/felsner-weil-sweeps-arrangements-signotopes-2001.md`,
  `research/summaries/wikipedia-cc-system.md` (claims `fw-rank3-signotope-pseudoline`,
  `cc-system-axioms`).

- **Splitting-line induction holds on the es_construct template through n=6,
  fails at n=7. (checked, scoped strictly)** For the verified `es_construct`
  ES construction (N = 2^{n-2} points, no convex n-gon), the rotating directed-line
  enumeration (validated exactly against a 2^N convex-hull-separation oracle at
  N=8,10,12,14,16: N(N-1) distinct open half-plane sides, zero missing/zero
  extra) finds over all N(N-1) open half-plane bipartitions: splits into two
  (n-1)-avoiding halves of size exactly 2^{n-3} **exist at n=5 (4) and n=6 (2)
  and do NOT exist at n=7 (0)**. The n=5,6,7 counts were re-captured with full
  provenance (`EXIT: 0`) on the validated enumerator. *Evidence:* computed and
  checked, exact integer determinants. *Falsified by:* an exact orientation table
  finding a valid split at n=7, or re-running the validated enumerator giving
  different counts. **Scope: this template only, at these n.** It shows the
  splitting-line induction f(n) ≤ 2f(n-1) succeeds on this construction for
  n≤6 and fails on it at n=7 — NOT a statement about other extremal sets or the
  general G-split lemma. `code/out/gsplit_phase2.captured.txt` (claim
  `gsplit-enum-completeness-and-n7-zero`, status checked).

- **es-nogon scored search (53 candidates × k=6,7): complete, found nothing new.
  (computed and checked)** `code/search/es-nogon/score.py` (exact integer via
  verified `lib.es_geom`, C(N,k) subset enumeration as authority + onion-layer
  precheck) certified, with a self-test that SCOREs 16/32 and rejects a collinear
  and an over-16 set: k=6 cap is exactly 16 (matches ES(6)=17); k=7 top score is
  32, reached only by ~20 affine/perturbation copies of the one verified
  `es_construct` construction (all isomorphic), and every random/layered/dense
  candidate is INVALID with a convex-k-gon witness. *Evidence:* computed and
  checked (106 invocations, ~281 s; 20 full 32-pt k=7 exact C(32,7) runs each
  ~7-12 s). *Falsified by:* a candidate certifying size 33+ no-convex-7 at k=7
  (would refute ES(7)=33 and must be re-verified independently), or a genuinely
  non-isomorphic 32-pt no-7-gon set. **Bounds on its meaning:** the affine orbit
  is degenerate — one construction counted many times — so the 32 record is
  reproduced, NOT improved; it contributes nothing toward an ES(7) upper bound.
  `code/search/es-nogon/SEARCH.md`, `scorer_selftest.captured.txt`.

- **Single open half-planes: 4/2/0 valid splits at n=5/6/7 on es_construct —
  the single-line splitting induction fails on this template at n=7.
  (computed and checked, scoped strictly)** Already recorded above
  (`gsplit_phase2.captured.txt`, EXIT 0, on the validated rotating-line
  enumerator): over all N(N−1) open half-plane bipartitions, splits into two
  (n−1)-avoiding halves of size 2^{n−3} exist at n=5 (4) and n=6 (2) and do NOT
  exist at n=7 (0). *Falsified by:* re-running the validated enumerator giving
  different counts. This is a property of single-line cuts on this one template,
  not of all cut families — see the next two bullets, which are exactly why.

- **Double-wedge (side-pair) family: 27 valid splits at n=7 — the n=7 failure
  is a property of single-line cuts, not of two-ray separations.
  (computed and checked, scoped strictly)** Enumerating pairs of the 992
  validated open half-plane sides (C(992,2)=491,536 pairs; 13,030 with
  |inter|=16; 2,454 distinct size-16 bipartitions), intersecting two sides per
  pair, gave **27 distinct VALID splits** (both halves 6-avoiding) at n=7 on
  `es_construct`. Since a convex wedge (angle<π) or its reflex complement is an
  intersection of two half-planes, the side-pair family is a SUPERSET of every
  wedge-realizable bipartition — so zero here would have been strictly stronger
  than zero over wedges, and the 27 is a genuine two-ray separation. Positive
  control: witness apex (2400,2725) gives a valid split whose bipartition
  appears among the intersections (PASS). *Falsified by:* an exact orientation
  table (or a re-run) showing one of the 27 is not a valid split.
  **Caveat carried from the adjudication: full apex-cell wedge-realizability
  (a lower bound per split: both boundary lines translatable to one common apex
  without crossing a point) is NOT claimed for all 27 — they are verified as
  side-pair intersections only.** `code/out/wedge_sidepair.captured2.txt`,
  `code/out/wedge_sidepair_adjudication.md` (claim `wedge-sidepair-27-valid-n7`,
  status checked).

- **The even/odd block bipartition is a side-intersection at n=5,6 but is
  NEITHER a single side NOR a side-intersection (hence not a wedge cut) at n=7,
  while both halves remain 6-avoiding. (computed and checked, scoped strictly)**
  The even/odd split (alternating blocks: at n=7 the even-index blocks
  T_0,T_2,T_4 = 1+10+5 = 16 points {0,6,7,…,15,26,…,30} vs odd T_1,T_3,T_5 =
  16 points {1,…,5,16,…,25,31}) is NOT any single open half-plane at n=5,6,7,
  IS a double-wedge side-intersection at n=5,6, and at n=7 is NEITHER, although
  each half independently has largest convex subset 5 (no convex 6-gon, exact
  2^16 verification). *Falsified by:* an exact orientation re-check showing the
  even/odd bipartition IS a side-intersection at n=7, or a half failing
  6-avoidance. This is the sharpest open thread: WHICH cut family (if any)
  realizes the even/odd 16–16 split at n=7 (task
  `evenodd-cutfamily-which-family-realizes`). `code/out/wedge_evenodd_alln.captured.txt`,
  `code/out/wedge_evenodd_check.captured.txt` (claim
  `wedge-evenodd-not-side-intersection-n7`, status checked).

- **Allowable/circular-sequence encoder on es_construct: convexity is readable
  for |S|≥4; reversal-depth=block-index failed. (computed and checked on this
  template)** `code/out/allowable_encoder.py` builds the exact Goodman–Pollack
  circular sequence of `es_construct` (all arithmetic `fractions.Fraction`;
  directions via exact cross-product, never float), confirmed C(N,2) events and
  all x distinct at n=4..7. Two findings, each with its own status: (1) *tentative,
  needs a bug-fix before trusting* — the [A] axiom check is internally
  inconsistent at n=6,7 (per-event tally says all 120/496 events are single
  adjacent reversals, replay reports 'non-adjacent swap 11,13 / 11,12 / 2,4');
  the two sub-checks disagree, so the encoder's own axiom verification is not yet
  accepted until the replay inconsistency is resolved. (2) *refuted on this
  template* — the reversal-depth = block-index mechanism FAILED for every
  statistic S2–S5 at n=4..7 (`exact==blockidx:False`, non-monotone in block
  everywhere), so the approach file's conjecture 'the C(n−2,i) are reversal
  depths' is not supported by these statistics and stands refuted here unless a
  genuinely different order-type-INVARIANT depth statistic recovers the blocks.
  (3) *checked, holds for k≥4* — the convexity-from-sequence
  (extreme-in-projection) criterion agreed with the exact oracle on every
  |S|≥4 subset (n=6: 58651/58659 agree, disagreed only on the 3-subsets
  [0,1,2],[0,1,3],[0,1,4], where sequence=False but oracle=True because every
  3 points form a convex triangle — a trivial artefact), so
  'S in convex position ⟺ every p is extreme in some S-projection' holds for
  k≥4 and is the live sequential direction. *Evidence:* computed and checked,
  exact. *Falsified by:* an |S|≥4 subset on which sequence-criterion and oracle
  disagree (n≥6), or an order-type-invariant depth statistic that does recover
  the blocks. **Scope: this template; the direction may still generalize.**
  `code/out/allowable_encoder.captured.txt` (and identical `.captured2.txt`).

- **Wedge (two-ray) cut family on es_construct: 27 valid (n−1)-avoiding splits at
  n=7, so the split failure is single-line-only; the even/odd blocks are NEITHER a
  single side NOR a side-intersection at n=7. (computed and checked, scoped
  strictly)** On the verified `es_construct` (N=2^{n-2}, no convex n-gon), the
  double-wedge cut family — every pairwise intersection of the validated N(N−1)
  = 992 open half-plane sides (a SUPERSET of wedge-realizable bipartitions, so
  richer than wedges) — was enumerated on 28 workers (EXIT 0, positive control
  apex (2400,2725) PASS): over the 13,030 pairs with |inter|=16 / 2,454 distinct
  size-16 bipartitions, **27 distinct VALID splits** (both halves 6-avoiding) exist
  at n=7. So the n=7 split failure seen with single open half-planes (4/2/0 at
  n=5/6/7) is a property of *single-line* cuts, not of *two-ray* separations: some
  double-wedge cut does realize an (n−1)-avoiding split of this 2^{n−2}-set into
  two 2^{n−3}-halves. Separately, the even/odd block bipartition is an intersection
  of two half-plane sides at n=5,6 but is **NEITHER a single side NOR a
  side-intersection at n=7**, although both halves remain 6-avoiding (largest
  convex subset = 5 each, exact 2^16 verification) — so the even/odd split is not
  wedge-realizable on this template at n=7. *Evidence:* computed and checked, exact
  integer/Fraction determinants, 28 workers. *Falsified by:* an alternate exact
  capture finding a valid single-line split at n=7 (above the 4/2/0), or finding
  the even/odd bipartition as a side-pair intersection at n=7, or a different
  count of valid side-pair splits than 27. **Caveat carried from the adjudicator's
  own note (wedges): full wedge-realizability of all 27 (a lower bound per split,
  requiring a common-apex translation test) is NOT claimed** — they are shown as
  side-pair intersections only; the even/odd non-membership is exact. **Scope: this
  template only, at these n** — not other extremal sets, not the general G-split
  lemma. `code/out/wedge_sidepair_adjudication.md`,
  `code/out/wedge_sidepair.captured2.txt`, `code/out/wedge_evenodd_check.captured.txt`,
  `code/out/wedge_evenodd_alln.captured.txt`.
## Ruled out

Approaches that failed, and the reason each failed — plus what is excluded from
counting as progress.

- **Empty-hexagon and higher-dimensional SAT results are adjacent problems, not
  progress.** H(6)=30 (Heule–Scheucher) and the higher-dimensional
  acyclic-chirotope SAT numbers concern different questions; they do not bear on
  ES(n) and are kept out of Established. Recorded as context only in
  `research/ROOT.md` §5.4–5.5.
- **The even/odd block bipartition is not a line-separability obstruction.**
  `gsplit_line.py` found the even- vs odd-index blocks of `es_construct` not
  strictly line-separable; that is a property of this one realization, not a
  refutation of G-split (a valid radial placement exists per the literature). The
  genuine question is the exhaustive any-line test, task
  `gsplit-exhaustive-line-test`.
- **Reversal-depth = block index is NOT an order-type invariant on this template.
  (refuted)** The adopted allowable-sequence approach's central conjecture — that
  the ES block sizes C(n−2,i) are the counts of an order-type-invariant per-point
  reversal-depth statistic in the circular sequence — failed for every statistic
  tried (S2–S5) at n=4..7 on the verified `es_construct` (`allowable_encoder.py`
  capture: `exact==blockidx:False` and non-monotone everywhere), and the
  realization-invariance rows in capture D show only S3 is invariant under both
  stretch and reflection while S2/S4/S5 are placement artifacts. Do not re-propose
  "the C(n−2,i) are reversal depths" as a route; the convexity-readable direction
  (which does hold for k≥4) is where the allowable-sequence line continues.

- **Steering rule in force (steer 4): no new sources.** Phase 1's exit test is
  met; gathering is admissible only against a stated gap in
  `research/REQUESTS.md`. The pending computation must be run first.
- **All prior wedge apex-sweep counts are retracted (directive 15).** The
  capture `code/out/wedge_enum_full_captured.txt` (387 apexes) is a FALSE ZERO,
  not a result: every apex shares the SAME y-coordinate 3000000001/1000000 —
  it sweeps x along one horizontal line, so it enumerates wedge partitions for
  apexes on that one line, not for the set. It misses the known-good n=7 witness
  apex (2400,2725) (y=2725), so a 387/387 has_valid=False would be an artefact
  of the apex family, exactly the line-family artefact of 2·C(N,2)+1. Do not
  cite this capture as a completed negative result. The task now requires an
  asserted positive control on (2400,2725), enumeration over the CELLS of the
  C(N,2) point-line arrangement (one apex per cell, constant angular order), and
  partial-progress-with-wall-clock reporting (the old capture timed out at order
  66/387 with no summary).
- **All earlier gsplit counts are SUPERSEDED (steer 10).** The
  `gsplit_exhaustive.captured.txt` run was a shell error, not a result: its
  command used `${PIPESTATUS[0]}` (a bash array) under `/bin/sh` and died
  `exit: 2 ... Bad substitution`, so the script never re-ran. The operator's
  recheck of the pair-line scheme on `es_construct` gives 50/222/946 distinct
  bipartitions at n=5,6,7 — not the 57/241/993 the old capture reported — with
  33-40 false positives per set. The pair-line enumeration is wrong in both
  directions. The 6/4/2/0 valid-split decay and the un-provenanced
  `gsplit_enum_definitive` capture are superseded too, pending the rotating-line
  re-run (task `gsplit-enumeration-recheck`).

### Steer 10 — the pair-line numbers were wrong in both directions; all prior gsplit counts superseded

The operator's recheck of the pair-line scheme on `es_construct` produced
50/222/946 distinct bipartitions at n=5,6,7 — not the 57/241/993 the original
`gsplit_exhaustive.captured.txt` reported — with 33-40 false positives per set.
The old numbers came from a different code path than the one in the file, and
the pair-line enumeration is wrong in both directions. In addition, the
`gsplit_exhaustive.py` capture was a shell error, not a run: its command used
`${PIPESTATUS[0]}`, which is a bash array, under `/bin/sh` (dash), and died
`exit: 2 ... Bad substitution` before the script executed.

The executable core is unchanged in direction and is now the head of the queue:
task `gsplit-enumeration-recheck` — (1) drop PIPESTATUS and all bashisms, capture
as `cd /workspace && timeout 550 python code/out/X.py > code/out/X.captured.txt
2>&1; echo EXIT: $?` (no pipe, no tee, no arrays); (2) replace
`candidate_bipartitions` in `gsplit_exhaustive.py` with the rotating-line
enumerator — for each point p, sort the other N−1 points by angle around p and
sweep a directed line through p, N−1 bipartitions per p, N(N−1) total,
O(N² log N), exhaustive by the rotation argument; (3) validate it element-wise
against the 2^N disjoint-convex-hulls oracle at N=8,10,12,14,16 with zero missing
and zero extra; (4) re-run n=5,6,7 fresh and treat that output as the only record.
**(Superseded by steer 11: steps (2)–(3) are now accepted done; only the
provenance re-capture in step (1)/(4) remains — see the next note.)**

`code/out/gsplit_enum_definitive.py` already implements the rotating-line
construction as `ordered_pair_sides` (ordered pairs + 4 boundary inclusions) and
its Phase-1 capture shows the exact N(N−1)=56,90,132,182,240 match against the
2^N oracle with 0 missing / 0 extra — that logic is reusable, but its capture
lacks the command+exit line and it still repeats the stale 2·C(N,2)+1 pair-line
claim, so it must be re-captured under the safe command. The stale files
`gsplit_enum_validate.py` / `gsplit_enum_recheck.py` disagree with each other and
must not be cited again (see `gsplit_enum_definitive_claim.md`).

### Steer 11 — Phase 1 accepted done; remaining work is one provenance re-capture

The operator accepted Phase 1 of the rotating-line enumerator: `code/out/gsplit_enum_definitive.py` matches the 2^N disjoint-convex-hulls oracle exactly at N=8,10,12,14,16 — zero missing, zero extra, count N(N−1). That part needs nothing further. What remains is one command, not another design pass: re-capture the n=5,6,7 split counts with provenance into `code/out/gsplit_phase2.captured.txt` (the exact command is in the Gaps head-of-queue note and in task `gsplit-enumeration-recheck`), then — if it reproduces 4 splits at n=5, 2 at n=6, 0 at n=7 — promote `gsplit-enum-completeness-and-n7-zero` to checked for the split counts, retire `gsplit-exhaustive-esconstruct` pointing at the new capture, and write the scoped Established finding. If it does not reproduce, report the new numbers plainly. Do not start another enumerator.

## Numbers

- ES(3..6) = 3, 5, 9, 17.
- Lower-bound construction sizes at n=5,6,7: 8, 16, 32 points (2^{n-2}).
- **GOAL.md criterion 3 (oracle) is met**: `lib/es_geom` passed its self-test on
  hand-known sets and `lib/es_construct` is verified (largest convex = n−1 at
  n=4,5,6; no convex 7-gon at n=7) by two independent hull algorithms. Captures:
  `code/out/checker_vs_construction_resolution.md`, `code/out/verify_es_construct.py`,
  `code/out/verify_es_construct_indep.py` (see `build-oracle` close reason).
- `es_construct` convex-layer profiles (hull peeling, exact): n=4 [3,1],
  n=5 [4,4], n=6 [5,5,3,3], n=7 [6,6,6,5,6,3]. These are *onion-layer* sizes,
  NOT the binomial block sizes C(n-2,i)=[1,4,6,4,1]/[1,5,10,10,5,1] — the fact
  that the ES construction's layers are not its blocks is what refuted the
  Gale-transform approach. Conjecture A (resolved PASS at n=5,6,7): the outer
  convex hull is exactly one point per block T_0..T_{n-2}, n−1 vertices, in
  block order — `code/out/layer_conjecture_A.captured.txt`.
- es-nogon search: 53 candidates; k=6 sizes {8,12,14,16} capping at 16; k=7
  sizes {12,16,20,28,30,32} capping at 32, top reached only by the degenerate
  ES affine orbit. ~281 s total wall (~7-12 s per full 32-pt k=7 exact run).

## Recalled

Nothing promoted from durable memory yet. Fill this section from `recall_memory`
before relying on any cross-run finding.

## Contradictions

- **Resolved: the run's ES construction was defective, not the checker.** The
  checker `lib/es_geom` is correct (survives every hand-known set); the defective
  realizations were `es_construction.es_lower_set`, `es_lower.py`, and `esz.py`.
  `es_construct.py` is the verified 2^{n-2}-point no-convex-n-gon construction
  (largestConvex = n−1 at n=4,5,6; no convex 7-gon at n=7), checked by two
  independent hull algorithms. The three other construction modules are
  **quarantined — do not import them** (see `code/lib/INDEX.md`). Resolution:
  `code/out/checker_vs_construction_resolution.md`.

## Gaps

What the run still needs and has not found.

- **gsplit Phase 2 re-capture — DONE (steer 11 fully executed).** The split
  counts were re-derived with full provenance: `code/out/gsplit_phase2.captured.txt`
  (command + `EXIT: 0`) reproduces 4 splits at n=5, 2 at n=6, 0 at n=7 on the
  validated rotating-line enumerator, which also re-matches the 2^N oracle at
  N=8..16 (zero missing/extra, count N(N−1)). Claims promoted: `gsplit-enum-
  completeness-and-n7-zero` checked, `gsplit-exhaustive-esconstruct` retired to
  the new anchor. Task `gsplit-enumeration-recheck` is closed. The old
  6/4/2/0 and 57/241/993 / 50/222/946 counts are dead (steer 10: pair-line
  enumerator wrong in both directions).

- **STEERING — head of queue (directive 22): no more spectra of es_construct.** Directive 21's rule stands and directive 22 sharpens it: pattern_finder computes no further counting statistics of es_construct — no k-subset convex spectra (the 09:58-10:06 convex_spectrum round was a violation filed honestly, not work), no OEIS lookups on numbers off this placement, no n=8 extensions of any template quantity. A pattern is worth finding only if defined for EVERY n-avoiding set of size 2^{n-2} and computed on two non-isomorphic sets and compared (e.g. the 32-point record set vs es_construct at the same N, or an order-type invariant that survives re-realization); a quantity computable on only one set is a coordinate, not a pattern. Two tasks lead the queue: (1) `lift-or-declare-strongest-template-fact` — state the strongest surviving template fact (the (n-1)-convex block-shape classification) over EVERY n-avoiding set of size 2^{n-2} and hunt a violating set (perturb es_construct off the corridor, the 32-point record set, any realizable order type), or declare it template-only and stop; do NOT extend template claims to n=8. (2) `nullstellensatz-grid-first-target` — the Nullstellensatz/Alon-Furedi Boolean-cube idea (approach polynomial-rank-nullstellensatz, now adopted): the smallest n where the polynomial criterion can be written/checked exactly with the degree bound stated; critical check that the 2^{n-2} constant is the HOST SIZE (not a recurring 4^n simplex — if so, close it). Do not claim the conjecture proved. The cut-family question (task `evenodd-cutfamily-which-family-realizes`) is DROPPED by directive 21 as template-mapping. Prior steer notes (10/11) above are historical; their work is done.
- **ADJACENT-PROBLEM STOP (directive 17): Horton/empty-polygon work is drift,
  not progress.** The tool_builder recall of 'horton verify empty convex 7-gon'
  is the EMPTY-hexagon problem (H(6)=30, Heule–Scheucher, ROOT.md §5.4) —
  adjacent per Ruled out, NOT progress toward ES(n)=2^{n-2}+1. ES(n) counts n
  points in convex position with no emptiness condition; a Horton set has
  arbitrarily large convex subsets and is no obstruction to ES. Do not spend
  calls there unless a stated reduction connects it back. (The `horton_verify.py`
  handoff exists; it confirms a freshly-digested secondary and does not bear on
  ES.)
- **Balko–Valtr SAT encoding still only at DOI/abstract.** Needed to reproduce
  ES(5)=9 / ES(6)=17 with our own encoder. Filed as `balko-valtr-attack-baa4` in
  `research/REQUESTS.md`.

## The ledgers, and how to reach them

This workspace keeps its state in **ledgers** — the task list, the sub-goals,
the claims, the approaches, the threads, and any axis this run has added for
itself. `list_ledgers` names every one and says what it holds.

**The rendered files in your context are shortened.** `research/APPROACHES.md`
and the rest carry a bounded row per entry, because everything in this prompt is
re-sent on every call you make. The whole of a refutation, the full statement of
a claim, the complete detail of a task — those are on disk, and `read_ledger`
is how you get them:

```
read_ledger { ledger: "approaches", status: "refuted" }
read_ledger { ledger: "tasks", query: "sieve" }
```

Two habits worth having, because they are cheap and the alternative is not:

- **Read before you conclude a ledger holds nothing.** A section that says
  `12 more not shown here` means exactly that. Treating the bounded copy as the
  whole record is how a run re-proposes something it already closed.
- **Read one entry in full before acting on it.** A one-line summary is enough
  to decide an entry is relevant and never enough to decide what to do about it.

Never edit a derived file by hand. They are rewritten from their sources on the
next write, so an edit is not a change — it is work queued for deletion, and you
will not be told when it goes. The write tools are the only way in, and if you do
not hold them, whoever does is the role to hand it to.

## Recording into a ledger

You hold `record_entry` and `close_entry`. Use them instead of writing the state
out as prose, and instead of editing any derived file by hand — those are
rewritten from their sources, so an edit to one is discarded without warning.

**Which ledgers you may write is checked when you call.** Each one names the
roles that keep it, so holding these tools is not permission to write all of
them; `list_ledgers` says what exists and a refusal says who owns it. Write to
the ones that are yours and leave the rest to the roles whose job they are.

The task ledger, as the example — the same two calls work on every ledger you
keep, with that ledger's own field names:

```
record_entry { ledger: "tasks", id: "fix-the-audit-verdict",
               fields: { title: "Fix the audit's verdict logic",
                         detail: "A refuted sub-check must not print ALL CHECKS PASSED.",
                         status: "open" } }

close_entry  { ledger: "tasks", id: "fix-the-audit-verdict", status: "done",
               reason: "verdict now prints (D) refuted separately; re-captured to
                        code/out/reduction_audit.captured2.txt" }
```

**Only the fields you name change.** Adding a blocker to a task costs one field,
not a re-statement of the task. This matters more than it looks: re-emitting a
whole file to change one line is the largest source of accidental loss here,
because a dropped row looks exactly like the file you meant to write.

**Closing is not deleting.** A closed entry stays on the ledger with its reason,
and that is the whole point of closing it. `status: "done"` says it was carried
out; `status: "dropped"` says it will not be. Both demand a reason and the
reason is the part that is worth anything later:

- *"the verdict logic now reports (D) separately, captured2 confirms it"* tells
  the next role what it can rely on.
- *"the empirical route is at its ceiling — row 248 is still capped at 1e9, and
  a 4e9 sieve would cost eight hours to hit the same wall"* stops somebody
  proposing the sieve again in three attempts' time.
- *"done"* tells nobody anything, and you have then spent the call for nothing.

Write the reason for a reader who was not there and cannot ask you.

**What one entry is.** One thing somebody can pick up and finish, with what to
do in the `detail`. Not a theme, not a heading, and not the whole of the next
attempt. If you cannot say what would make it finished, it is a research
request or a thread, and there are ledgers for both.
