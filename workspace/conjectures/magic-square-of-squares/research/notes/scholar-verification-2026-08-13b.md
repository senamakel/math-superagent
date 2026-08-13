# Scholar full-text verification — Garcia-Fritz–Pasten 2026, Rome–Yamagishi 2024, Bremner 1999, plus library sweep

Session 2026-08-13. Read end-to-end against on-disk full texts; every statement
below is checked against the source or flagged as not.

## Garcia-Fritz–Pasten, "A note on Bremner's conjecture and uniformity" (arXiv:2604.04850v2)

Full text at `research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md`
(6 pp). The existing digest (`research/summaries/garcia-fritz-pasten-bremner-uniformity-2026.md`)
is accurate. Verified from the text:

- **Theorem 1.8** (Strong form of Bremner's conjecture): absolute `C > 1` such
  that every elliptic curve E/Q of rank r has all APs of x-coordinates of points
  of E(Q) bounded in length by `C^(r+1)`. Proven (2021 IMRN via Nevanlinna +
  GGK uniform Mordell–Lang); the 2026 note **restates** it and proves the
  conditional uniformity consequence. The "holds over any number field, not just
  Q" note in the digest is confirmed by the final technical remark in §1.5.
- **Theorem 1.2** (conditional uniformity): if ranks over Q are uniformly
  bounded by R, then AP lengths are uniformly bounded. Proof is short and
  explicit: from an AP of length M ≥ 4, take N = M−3 terms whose first term is
  not 2-torsion; the hexic `s² = f(at²+b)` defines a genus-2 curve X with a
  rational map X → E exhibiting E as an isogeny factor of J = Jac(X), so
  `rank J(Q) ≤ 2R`; DGH height-uniform Mordell gives `#X(Q) ≤ c^(1+2R)`; the
  AP's own points give `2⌊√(M−4)⌋+1 ≤ #X(Q)`. **This is the construction behind
  the AP-length bound and it is exactly the configuration the Robertson
  reduction produces** (three x-coordinates in AP on E). The genus-2 curve here
  is auxiliary — a proof device, not the MSS surface.
- **Theorem 1.3 / Cor 1.4** (multiplicative groups): model-agnostic; for the
  run's purposes it is context, not an input.
- The constant C is ineffective (comes from GGK/Rémond quantitative ML); no
  number can be extracted. Consistent with the thread's `effective-constant-hms`
  resolution: HMS 2026 makes it effectively computable but astronomically large.
- **No contradiction with recalled memory.** The claim blocks
  `bremner-conjecture-proved`, `uniform-rank-ap-bounded`, and the thread
  "uniformity-bremner-ap-bound" all restated the same content the full text
  confirms.

## Rome–Yamagishi, "On the existence of magic squares of powers" (arXiv:2406.09364v2)

Full text at `research/sources/rome-yamagishi-magic-squares-of-powers-2024.full.md`
(37 pp). The existing digest is accurate; **two additions**:

1. **`btva22-quasihyperbolic-3x3-surface`** (new claim): the intro (p. 2) cites
   Bruin–Thomas–Várilly-Alvarado 2022 as having established that the 3×3 MSS
   surface (6 quadrics in P⁸) contains only finitely many curves of genus 0 or 1;
   with Lang's conjecture, only finitely many rational points outside them — so
   a 3×3 MSS is either non-existent or remarkably rare. **Second-hand**: BTVA22
   is not in this library; the statement is `asserted`. This is the strongest
   published structural-rarity hint and the cleanest n=3 vs n≥4 contrast.
2. **`ry-proof-nuance-explicit-examples-for-4-to-36`** (new claim, `status:
   checked` from the proof text): Theorem 1.2's n≥4 statement is a union of two
   ranges — the circle-method machinery yields existence for n ≥ 36, and
   4 ≤ n ≤ 64 is covered by Boyer's catalogue of explicit examples (the ranges
   overlap on 36..64). So the circle-method lower bound alone starts at 36.

The `n-by-n-mss-exist-for-n-ge-4` claim (holds-here: no; the n=3 case is
excluded and the coefficient-matrix column-independence threshold is not met at
n=3) is verbatim correct.

## Bremner 1999, "On squares of squares" (Acta Arith. 88) — reduction verified

Full text at `research/sources/bremner-on-squares-of-squares-1999.full.md`.
The **`robertson-elliptic-reduction` claim on disk is complete** — the CONTEXT.md
gap note "claim is truncated" is stale. Verified from pp. 290–291:
- Any 3×3 magic square of rationals has the form (2) `[[a−b, a+b+c, a−c],
  [a+b−c, a, a−b+c], [a+c, a−b−c, a+b]]` with a,b,c ∈ Q; trivial iff
  `bc(b²−c²)(b²−4c²)(4b²−c²) = 0`.
- E: y² = x(x²−c²); (X,Y) ∈ 2E(Q) iff {X, X±c} all rational squares; hence
  a−b, a, a+b must be x-coordinates of points in 2E(Q); the existence of a MSS
  ⇔ three points in 2E(Q) with x-coordinates in AP (attributed to Robertson).
- The doubling formula `x(2P) = (ξ²+c²)²/(4η²)` is the (4) entry formula.
- The claim's parameter meanings are right: a = centre entry (a square, e.g.
  425² on the witness), c = anti-diagonal half-difference (138600 on the
  witness — NOT the centre), b = main-diagonal half-difference (41496).
- Also verified: the rank-3 curve example `y² = x(x²−1254²)` with AP triple
  (−528,26136), (−363,22869), (−198,17424); the degree-4 MSS over
  Q(√3,√133) (claim `bremner-deg4-centre-532`, centre 532 = 133·2²); the
  degree-27 family over Q(u) (the monic word "m11" etc. are the square entries).

No contradiction with the summary; the digest is accurate.

## Rabern 2003 and the DP07-adjacent tier

The librarian cycle (note `librarian-cycle-2026-08-13e.md`) already filed
accurate claims for Rabern (full text now on disk, `rabern-entry-prime-restrictions`
upgraded to proved-where-stated), Viada (arXiv:0711.3533 — effective Bogomolov
in E^g via David–Philippon/Rémond constants; does not give the DP07 constant),
and Galateau 2016 (survey-level only). The `dp07-explicit-constant-for-e3-ap`
request remains open; the DP07 primary text is paywalled and unobtainable this
cycle. Nothing in those summaries contradicts the full texts on disk.

## Does-not-help sources (recorded so nobody re-reads them)

- **Open Problem Garden** — bibliographic stub, no content. `Does not help`.
- **Wikipedia** — tertiary restatement, no theorem beyond the primary sources.
  `Does not help`.
- **Wolird arXiv:2310.12164** (Gaussian 3-to-1 sibling correspondence) —
  math.HO exposition; author disclaims bearing on Q-existence; distinct from
  Cain's reformulation. `Dead end`, holds-here: no.
- **Multimagie index page** — navigation frame only.
- **Ferreira arXiv:1506.06621** — claimed proof of non-existence; **refuted**
  (invalid (46)→(47) step), claim `ferreira-1506-06621-refuted` checked.
- **Robertson 1996 original** — paywalled, unobtainable; the reduction is
  carried in full by Bremner 1999 which IS on disk. Recorded dead end.
- **Buell 1999** — full text corrupt at every host (claim
  `buell-fulltext-corrupt-unobtainable`); the `25×10²⁴` hourglass bound stays
  secondary-sourced with the coprimality caveat.

## Coordination-state corrections (stored to Cognee)

1. **CONTEXT.md's "robertson-elliptic-reduction claim is truncated" gap is
   stale** — the claim block on disk is complete (see above). Do not re-open.
2. **TASKS.md "RUN THE PHI PROGRAMS — never executed" is stale** — all four ran
   with captures in `code/out/phi_program_runs.txt`; see that record for the two
   benign artifacts, one program bug (orbit oracle range truncation), and the
   genuinely false `[5b]` dominance bound (2980 counterexamples). The Faltings
   fibre attack is confirmed dead (genus 0 on all fibres, as expected from
   homogeneity).
3. The spurious `contradicts` rows (`catIII-k3-has-q-point contradicts (none`,
   `as`, `a`, `claim;`, `resolves)`, `the`) that appeared in an earlier
   search_claims recall were **malformed entries from a block whose `contradicts`
   field was itself free text**; after this session's re-derivation the ledger is
   clean.

## What the run still lacks

- **BTVA22 primary text** (to upgrade `btva22-quasihyperbolic-3x3-surface` from
  asserted to proved).
- **DP07 explicit constant** (request `dp07-explicit-constant-for-e3-ap` open).
- **Rank of the Robertson curve E: y² = x(x²−c²) for putative MSS centres**,
  and the exact full-MSS⇔variety reduction as a claim block (the run's own
  outstanding gap in CONTEXT.md; nothing in this session's sources closes it).