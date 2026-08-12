# ROOT — what the literature establishes on the 3×3 magic square of squares

Status note on attribution: every claim below is tagged **proved** (proved where
stated, in a primary source), **asserted** (stated by a source without a proof,
or with a proof the run has not independently reproduced), **checked** (verified
by this run's own exact program), or **catalogued** (a lookup / source-asserted
result the run has not reproduced). The claim ids refer to
`research/CLAIMS.md`; sources are the summaries under `research/summaries/` and
full texts under `research/sources/`. Nothing here was fetched for this
document — it is compiled from the library already on disk.

The question is **open**: no 3×3 magic square of squares over Q is known, and no
proof of non-existence is known. LaBar's problem (1984); Gardner's $100 prize;
the 4×4 Euler magic square of squares is a *different* problem (`problem.md`,
`research/summaries/wikipedia-magic-square-of-squares.md`).

---

## 1. The structure a hypothetical full solution must have

**The `(c, u, v)` parametrisation.** Every 3×3 magic square with magic constant
`M` has centre `c = M/3` and is fully determined by `c, u, v`:

```
  c + u        c - u - v    c + v
  c - u + v    c            c + u - v
  c - v        c + u + v    c - u
```

So the problem is: choose positive integers `c, u, v` so that all nine entries
are distinct positive perfect squares. This parametrisation is the equivalent of
Bremner's eq. (3),
`[[a−b, a+b+c, a−c],[a+b−c, a, a−b+c],[a+c, a−b−c, a+b]]`
(a renamed version of the same form — `problem.md`; `bremner-on-squares-of-
squares-1999`; `robertson-elliptic-reduction`). This run recomputed the
parametrisation's identity **and** completeness on a fresh exact rerun
(585,640 grids for identity, 68,026 grids for completeness, 0 mismatches):
`code/out/oracle_note.md`, claim `near-miss-baseline-and-incidence` (**checked**).
Independently, the affine space of magic assignments has dimension 3 over Q,
spanned by the constant, `u`- and `v`-grids — the incidence matrix of the 8
lines has rank 7 over Q (`code/out/oracle_note.md`; a "dimension 4" claim in the
task brief is contradicted by the computed value, which this run reports as 3).

**Centre is a square: `c = e²`.** The centre is itself one of the nine square
entries, so `c = e²` (`problem.md`; `morgenstern-properties-...-2007`).

**Four centre-line APs.** The two diagonals, the middle row and the middle
column are four three-term arithmetic progressions of squares, each with the
same middle term `e²`, whose common differences are `u, v, u+v, u−v` (up to
sign). `near-miss-baseline-and-incidence` (**checked**) confirms on all 65,025
grids with `c≤25, |u|,|v|≤25` that the four centre lines are 3-term APs with
differences `u−v, u+v, u, v`.

**The additive-dependence obstruction.** The four differences are *not*
independent: they satisfy `(u+v) − (u−v) = 2v` etc. Every attack has to
confront that the middle term `e²` lies in *four* 3-square APs with those four
differences in that additive relation. Three-term APs of squares are plentiful
and completely classified (Thm 1 of Zimmermann–Loria, claim
`ap-three-squares-unique-param`, **proved**: a primitive AP `x²,A²,y²` with
`A` odd is pinned uniquely by a square-free `p|A`, `p≡1 mod 4`, `A=p(m²+n²)`,
`b=4mn(m²−n²)`); but a middle term lying in *four* of them with those four
additively-linked differences is what nobody can produce and nobody can rule
out. On the Bremner witness the four differenced booleans are `[F,T,T,F]` —
exactly two of the four centre APs are realized, from Pythagorean splits of
`425²` (`near-miss-baseline-and-incidence`).

---

## 2. The current verification bounds

No bound is a proof; each is a fact about a finite range, stated with its method
and what it covered.

- **Morgenstern three-AP equal-`d` search, `d ≤ 2.4×10¹⁹`.** Exhaustive
  enumeration of *three* 3-square APs sharing a common difference `d`, all odd
  entries: complete to `d ≤ 2.4×10¹⁹`, partial beyond; 3809 instances found, all
  but two eliminated because two scale factors share a prime or a scale factor
  is a multiple of an `8k+3` prime (`research/summaries/morgenstern-extended-
  searches-2013.md`). This is the run's "three-AP search" bound.

- **Morgenstern primitive equal-`d` bound.** For three *primitive* equal-`d`
  APs only 5 instances exist in total, the largest at `d = 3.31×10¹⁵`, with none
  beyond that up to `d = 6.4×10²²` (claim `three-primitive-equal-d-bound`,
  **catalogued**). A true MSS needs *four* linked centre APs, strictly stronger.

- **Bremner / Boyer six-square and centre searches.** Bremner II (2001) proves
  all sixteen six-square configurations are attainable (see §3) and in his
  Category VII search over the region `p+q+n(λ)+d(λ) ≤ 1000` finds the **only**
  7-square solution (up to symmetry), namely his witness — claim
  `seven-square-category-vii-unique` (**proved**). Boyer (2004) surveys problem
  (B) (maximise square entries): no fully-magic 7-square example beyond
  Bremner's is known (`boyer-square-of-squares-search-v2`). On the elliptic
  reduction (`robertson-elliptic-reduction`) Bremner's search finds only one
  non-torsion AP triple on a rank-3 curve (`bremner-on-squares-of-squares-1999`).

- **Morgenstern entry lower bound.** All nine entries of any distinct-entry MSS
  of squares are ≥ squares of 8-digit numbers, by a complete generator-and-
  termination enumeration (`morgenstern-smallest-entry-8-digit`; claim
  `morgenstern-8-digit-smallest-entry`, **catalogued** — Morgenstern's own
  completed computer proof, not reproduced here).

- **Buell hourglass `25×10²⁴`, with coprimality caveat.** Buell's search shows
  no 7-square "magic hourglass" (two diagonals + central column) with central
  element `< 25×10²⁴` — but **only under the assumption that the diagonal/column
  triples are coprime**. Zimmermann–Loria show that assumption is not automatic
  and, relaxing it, find hourglass solutions with ~10-digit central elements
  congruent mod `2⁴⁷` (claim `buell-hourglass-25e24-coprime`, **asserted**:
  Buell's paper is not on disk, known via Bremner II, Zimmermann–Loria, and
  Michaud-Rodgers citations). Therefore the `25×10²⁴` figure is **not** a bound
  on the full-MSS centre; several sources (Michaud-Rodgers) over-broaden it, and
  this run does not.

- **This run's own small box.** `code/brute.py` scanned magic grids with
  positive entries ≤ 100 and the near-miss box `c = e², e ≤ 80, |u|,|v| ≤ 120`
  (4,052,328 grids): best distinct grid has 5 square entries, no distinct
  6-square magic grid exists in either box. Range facts only
  (`code/out/oracle_note.md`).

---

## 3. Restricted classes already settled (exact hypotheses)

- **7-of-8 line-sums achievable (Sallows LS1).** There is a squared square with
  all 9 entries distinct squares, all 7 lines (rows, columns, one diagonal)
  summing to `147² = 21609`, the other diagonal failing (38307) — claim
  `ls1-witness` (**checked**: reproduced exactly by `check_near_misses.py` into
  `code/out/near_misses.json`). It is the `(p,q,r,s)=(1,3,4,11)` low member of
  Lucas's 3×3 semi-magic family, magic sum `147²` (claim `ls1-in-lucas-family`,
  **catalogued**). Hypothesis: distinct square entries; no magic-square
  requirement beyond 7 of 8 sums.

- **7-square-entry magic square exists (Bremner).** A genuine 3×3 magic square
  (all 8 line sums `541875`) with **exactly seven** square entries:
  `[373² 289² 565²; 360721 425² 23²; 205² 527² 222121]`, centre `425²`,
  non-squares `360721` and `222121` — claim `near-miss-baseline-and-incidence`
  (**checked**, reproduced exactly), and in Bremner 1999 p. 290. One non-trivial
  example together with its symmetries is all that is known.

- **No 8-square-entry example is known over Q.** Bremner 1999/2001: "no
  examples known of non-trivial squares with eight square entries" (unless the
  ground field is extended). Claim `extension-field-mss-exist` (below) and
  `boyer-square-of-squares-search-v2`. This is the open boundary: 7 is the
  current maximum number of square entries in a fully-magic square over Q.

- **All sixteen six-square configurations attainable (Boney/Boyer citing
  Bremner).** Up to symmetry there are exactly sixteen ways to choose six
  entries of a 3×3 square; for *each* there are infinitely many magic squares
  with those six entries square, via one-variable parametrisations (intersection
  of three quadrics in P⁵). The smallest has magic sum `3·145 = 435`. Claim
  `six-square-all-attainable` (**asserted**, compiled from Bremner 2001);
  `bremner-on-squares-of-squares-II-2001` section 1. Consequence: the
  obstruction lives entirely in the seventh, eighth, and ninth entries.

- **MSS exist over extension fields, none over Q.** Genuine 3×3 MSS (all nine
  entries distinct squares) exist as *explicit constructions* over proper
  algebraic number fields: a degree-4 example over `Q(√3,√133)`, a
  one-parameter family over `Q(i,√(µ³−µ))`, a degree-27 family over `Q(u)`
  (Bremner 1999); and an **infinite family of 8-square magic squares over
  `Q(√3)`** via curves `Y²=X(X²+8X+4)` (rank 1) and `Y²=X(X²+2X−2)` (rank 2)
  (Bremner 2001). Claim `extension-field-mss-exist` (**proved** — explicit
  constructions, entries distinct). This is the critical "proves too much"
  guard: any impossibility argument that runs purely structurally is refuted by
  these, so a proof over Q must use rationalness/integrality essentially.

- **Three-AP primitive results (Morgenstern).** See §2: the `d ≤ 2.4×10¹⁹`
  complete equal-`d` three-AP search and the primitive five-instances `d ≤
  6.4×10²²` classification (`three-primitive-equal-d-bound`, **catalogued**).
  Entry-level congruences are proved (`primitive-mss-entry-congruences`,
  **proved**): in a primitive MSS all nine entries are odd and `≡1 mod 3`, no
  entry carries a `3 mod 8` prime factor, no middle-side entry a `5 mod 8`
  factor, the central entry is `1 mod 4`-only, and the step ratio excludes
  `p ∈ {0,1,2,3,4} ∪ {4k+3 prime or ±1}`. Conjoined with Zimmermann–Loria:
  a primitive MSS has all entries `≡1 mod 24` and magic sum `≡3 mod 72`
  (`primitive-mss-modular-124-72`, **proved**). These sieve the *search*; they
  do not refute existence (extension-field MSS satisfy the same congruences
  where defined) — there are solutions modulo every prime power.

- **Small partial / asserted restrictions (weaker).** Brown/MathPages Prop. 1
  (`centre-five-representations`, **asserted**): a MSS whose centre is a sum of
  two positive squares in at most 4 distinct ways is impossible — so a real MSS
  centre needs ≥5 two-square representations (Bremner's `425²` has a full split
  list, and the realized AP-difference endpoints `v, u+v` come from two of
  them: `near-miss-baseline-and-incidence`). Michaud-Rodgers (*talk*, no proof):
  the full magic-square variety `X ⊂ P⁸` is a surface with 256 singular points
  and contains no lines, and its degree-8 curves carry no rational point —
  claim `magic-variety-is-surface-no-lines`, **asserted, unchecked**; do not
  cite as proof-level. Bremner II's K3 (Category III, *six-square*) has complex
  Neron–Severi rank 20 but Q-defined `NS(S,Q)` rank 12, every rational curve on
  `S` even degree, and no irreducible rational curves of degree 4 or 8 —
  claim `k3-ns-rank-12-not-maximal` (**proved**); note it is the *six-square*
  surface, not the full nine-square variety.

---

## 4. Caveats and open gaps

- **`buell-hourglass-25e24-coprime`** is secondary-sourced (Buell's paper is not
  on disk); its coprimality hypothesis is essential and was relaxed by
  Zimmermann–Loria. Do not quote `25×10²⁴` as a general MSS centre bound.
- **Load-bearing but unverified** (`research/CLAIMS.md`): `fixed-start-ap-
  generators`, `near-miss-baseline-and-incidence`, `six-square-all-attainable`
  are asserted by their sources and not independently reproduced here (the
  near-miss *grids* themselves are checked; the surrounding structural claims are
  asserted).
- **Catalogued** (taken on a source/sequence's word, no local derivation):
  `ls1-in-lucas-family`, `morgenstern-8-digit-smallest-entry`,
  `three-primitive-equal-d-bound`, `sum-of-two-squares-multiplicity`.
- **Mis-attributions to avoid:** "dimension 4" for the magic-assignment space
  (computed = 3); `25×10²⁴` as a full-MSS centre bound (it is Buell's hourglass
  bound under a coprimality assumption); Robertson = Bremner 1999 duplicate in
  this library (the `2E(Q)` reduction is due to Robertson but *reported* by
  Bremner).
- **Live gap** (`research/REQUESTS.md`, `exact-reduction-magic-507c`): the exact
  reduction variety (elliptic surface / K3) and which points correspond to
  solutions, needed before any descent is sound.
