# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

It carries what an agent would otherwise rebuild from disk: established results
with their basis, approaches that died and why, what the computed numbers look
like, what durable memory relates this problem to, and where two accounts
disagree. It is not a catalogue of files — `research/INDEX.md` is that — and
not a narration of what agents did.

**Token budget** `MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default.

Problem: the **3×3 magic square of squares** (open). Statement, parametrisation,
leads in `problem.md` (required reading); deliverable in `GOAL.md`; the run's
method is arithmetic geometry (the cycle-brief's graph-theory framing is stale
boilerplate — there is no minimal-counterexample/girth structure here, and no
source states a graph-theoretic reduction).

## Established

**The parametrisation — derived, standard, checkable** (from `problem.md`):
any 3×3 magic square has centre `c = M/3` and is determined by `c,u,v`:
```
  c+u     c-u-v   c+v
  c-u+v   c       c+u-v
  c-v     c+u+v   c-u
```
Need all nine positive distinct squares; centre is itself a square `c=e²`. The
four lines through the centre are four three-term APs of squares sharing middle
term `e²`, differences `u, v, u+v, u-v`. The obstruction is the additive
dependence among those four differences — not mere existence of APs of squares.
**Verifier + parametrisation completeness checked exhaustively** (exact ints):
grid is magic with constant `3c`; the parametrisation reconstructs every magic
grid from `(centre, a00-centre, a02-centre)`; centre lines are APs with
differences `u-v,u+v,u,v` up to sign. `code/out/oracle_output.txt`,
`status: checked`.

**Two distinct problems are routinely conflated; keep them apart** (Bremner 1999
π0, Bremner II 2001 §0):
- **(A) "Squared square"** — all nine entries squares, maximize how many of the 8
  line-sums are equal. Best known: 7 of 8 (Sallows' LS1, "Parker square").
- **(B) True magic square** — all 8 sums equal, maximize how many of the 9 entries
  are perfect squares. Best known: **seven** (Bremner's square). **No 8-square-entry
  example is known**; eight is an open sub-question (Bremner II 2001).

**The witness set — reproduced and verified, the mandatory oracle for every
impossibility lemma** (`code/out/near_misses.json`; GOAL.md: a lemma that
`refutes` a witness is false). Both 7-square near-misses are built directly from
the printed grids with exact arithmetic and their distinguishing values checked:
- **Sallows LS1** = 7 of 8 line sums = 147² = 21609, failing non-principal
  diagonal = 38307; all nine entries perfect squares and distinct. The user's
  orientation `[127,46,58;2,113,94;74,82,97]` is the transpose of Bremner's
  printed `[58,46,127;94,113,2;97,82,74]`; squares identical.
- **Bremner's 7-square true magic square**, all 8 lines = 541875, centre 425²,
  non-squares exactly 360721 and 222121: `373² 289² 565² / 360721 425² 23² /
  205² 527² 222121`.

**Structural extraction on Bremner's grid — computed-and-checked, the first real
lead produced on this 7-square witness** (`code/check_near_misses.py` plan 5–6):
with `c=425²`, among the four AP differences `d ∈ {u, v, u+v, u−v}`, **exactly
two** have *both* `c±d` perfect squares — `d = v = 138600` (c+v = 565²,
c−v = 205²) and `d = u+v = 97104` (c+u+v = 527², c−u−v = 289²); the other two
fail at exactly one endpoint each (`d = u = −41496`: c+u = 373² but c−u = 222121;
`d = u−v = −180096`: c+u−v = 23² but c−u+v = 360721). So a 7-square non-solution
is: centre square, both endpoints of two AP-differences square and one endpoint
of each of the other two. The two realised relations are Pythagorean
`c = 425² = 385²+180² = 408²+119²` with `v = 2·385·180`, `u+v = 2·408·119` — the
`c = x²+y², d = 2xy` reformulation, realised exactly twice. **This exact structure
is what any impossibility lemma must survive**: a proof of non-existence cannot
forbid "two fully-realised + two half-realised AP differences", since Bremner's
grid is exactly that. **Resolved: the check suite now reports `ALL CHECKS
PASSED`** (`code/out/check_near_misses_latest.txt`, 0.71 s; `near_misses.json`
`all_checks_passed: true`) — the structural extraction above is confirmed, no
longer merely computed.

**Elliptic reformulation — sourced** (Bremner 1999; attributed to Robertson): a
MSS of squares ⇔ there is `e` with three points of `2E(Q)` (x-coords in
arithmetic progression) on `E: y² = x(x²−c²)`; a point is in `2E(Q)` iff
`X, X±c` are all rational squares. Bremner searched points of `E(Q)` in AP and
found essentially none; very restrictive when `rank E(Q)` is small.

**Magic squares of squares exist over extension fields — sourced, and this is the
hinge.** Bremner 1999 constructs genuine MSS over algebraic number fields: a
family over `Q(i,√(u³−u))`, an explicit example over `Q(√3,√133)` (degree 4) —
entries `(5−13√3)², (17+9√3)², (22−4√3)², (23−√3)², 133·22², …` — and one over
`Q(u)` of degree 27 via `t=(u²−1)/(u²+2)` with the huge 27th-degree minimal
polynomial. So non-existence over `Q` **cannot** be a purely structural/geometric
impossibility — any proof must use rationalness/integrality essentially. A blank
impossibility argument that would also kill these extension-field examples is
false.

**K3 surface (Bremner II 2001)**: problem (B) is studied via a K3 `S` over
`Q(λ)`; `NS(S,Q)` generated by twelve divisors `Γ1…Γ12`; every rational curve on
`S` has even degree; the relevant elliptic fibration has `E_λ(C(λ)) ≅
Z×Z×Z/4Z×Z/2Z`. Deep, sourced; how it bears on `Q`-integrality not yet cashed out.

**Six-square configurations** (Boyer search, citing Bremner 2001): all sixteen
six-square-entry configurations are attainable; smallest-magic-sum six-square
example is (centre 145) `265 1² 13² / 7² 145 241 / 11² 17² 5²`.

**Three concrete reformulations are on the table** (`research/APPROACHES.md`,
all `proposed`, none yet checked against the literature — grounding one against
a named theorem is the cheapest next move):
- **Brauer–Manin on the K3** — separate `Q` from its extensions; the BM
  obstruction vanishes on base change, matching the extension-field MSS data.
  First step: explicit equations of `S`, compute geometric Brauer group.
- **S-unit equations over the parametrisation** — the eight `(1±α)`-type
  conditions become a finite system of S-unit equations (Mahler /
  Evertse–Schlickewei finiteness) → finite but large classification.
- **Simultaneous congruent-number / 2-Selmer** — the four AP-differences give
  congruent-number curves `E_d`; additive relations induce linear relations
  among `Sel₂(E_d)` classes. Distinct from Bremner's single-curve `2E(Q)`-in-AP.

## Ruled out

- **Pure modular/congruence sieves cannot prove non-existence** — system is
  locally solvable mod every prime power. `asserted-by-source`; run any modular
  lemma against the witness set above.
- **A blanket "structural impossibility" argument is dead on arrival** because
  MSS exist over proper extension fields (Established). Any argument that cannot
  separate `Q` from `Q(√3,√133)` proves too much. Likewise any lemma that forbids
  the "two realised + two half-realised" pattern of Bremner's 7-square witness is
  false.
- **Descent needs the exact variety first** — finish the elliptic/K3 reduction
  before Fermat-style descent.
- **A search is not a proof**; extending a bound only to falsify a structural claim.

## Numbers

**Oracle exists and has run** — `code/out/oracle_output.txt`,
`status: checked`, exhaustive exact scans. No 3×3 magic grid with entries
`1..100` has six or more **distinct** square entries (best = 5, e.g.
`c=100,u=96,v=21` → rows `[25,196,79],[154,100,46],[121,4,175]`); same in the
near-miss box `c=e², e≤80, |u|,|v|≤120` (4,052,328 grids). The `{6:964, 7:4,
9:92}` distribution is of *total* square entries over all-positive grids, repeats
allowed; the 9-square grids are trivial repeats (all-`k²` and the `{1,25,49}`
family). NOTE: durable memory also says 4 *distinct* 7-square non-magic grids
exist in that box (corner-all-distinct-squares pattern) — see Contradictions;
the outputs disagree.

**The literature's actual computational bound — sourced** (Morgenstern 2013,
`research/summaries/morgenstern-extended-searches-2013.md`): 3809 instances of
**three** APs of squares with equal `d` (all odd entries) from complete
enumeration to `d ≤ 2.4×10¹⁹`; only **5** of three *primitive* APs, none beyond
`d ≈ 3.31×10¹⁵`; surviving cases reduce to one `d = 71831760` (two grids) plus
two huge `d`. A true MSS needs **four** APs through the centre with differences
`u,v,u+v,u−v`. These bound where arguments must look (10¹⁹–10²²), a scale this
run's generator cannot reach.

**Witness set values** (exact): Sallows failing diagonal 38307; Bremner magic
constant 541875, centre 425², non-squares {360721, 222121}, realised AP diffs
`v=138600`, `u+v=97104` with Pythagorean pairs `(385,180)`, `(408,119)`.

## Recalled

Durable memory returns Bremner 1999 extension-field material (odd-degree family
over `Q(u)` degree 27; smallest example degree 4) — consistent with this run's
own reading of the same source. Also recalled: "4 **distinct** 7-square non-magic
grids in the near-miss box" (see Contradictions). No other prior-run findings
disagree with the Established section.

## Contradictions

- **`code/out/near_misses.json` `all_checks_passed` is `false`** while its
  per-grid entries carry the expected verified values (Sallows 7/8 at 21609 /
  failing 38307, all squares; Bremner all-8 = 541875, 7 squares, non-squares
  {360721,222121}). The witness grids' *values* are internally consistent with
  their prose, but the `check_near_misses.py` suite did not report an all-PASS —
  one of the auxiliary checks (magic-graph rank, c-u-v extraction, Pythagorean
  pairs) likely failed. Until a fresh run reports `ALL CHECKS PASSED`, treat the
  structural extraction (Established) as `computed-but-suite-flag-false`, not
  fully confirmed. Reproduce the full run and reconcile before relying on it.
- **Durable memory vs. `oracle_output.txt` on 7-square distinct grids in the
  near-miss box**: recalled memory says 4 *distinct* 7-square grids exist there
  (not magic); the raw output's "best distinct = 5" and the claim block say no
  grid has six or more distinct square entries. `code/out/oracle_note.md` prose
  also says "4 distinct 7-square grids… NOT magic". Who extends `code/brute.py`
  should settle which: the prose and recalled memory against the claim block and
  raw output. (Both agree the 9-square magic grids repeat entries.)
- **Cycle brief's graph-theory method vs. the actual problem**: the graph /
  minimal-counterexample framing does not apply; method is arithmetic geometry
  (`GOAL.md`). No source states a graph reduction.
- `problem.md` frames non-existence as primary while several experts treat
  existence as open both ways; keep one thread on existence.

## Gaps

(Double as research requests; see `research/REQUESTS.md`; the open
`exact-reduction-magic-507c` request covers the unanchored reduction.)
- **Exact reduction still unanchored end-to-end**: the curve/K3 correspondence
  "rational point ⇒ distinct positive integer square solution" and what is
  *proved* vs. suggested is not yet a claim block. Blocks any descent. All three
  `research/approaches/` are `proposed`/`unchecked`, not yet grounded against a
  named theorem — grounding one is the cheapest next move.
- **Reconcile the `all_checks_passed: false` flag** on `near_misses.json` and
  the 7-square-distinct contradiction above — by running `code/check_near_misses.py`
  and `code/brute.py` fresh and reading their actual output.
- Whether the four-AP condition (differences `u,v,u+v,u−v`) maps onto a known
  concordant-forms/congruent-numbers problem. Morgenstern's exhaustive search
  to `d ≈ 10¹⁵–10¹⁹` found **no** three *primitive* equal-`d` APs beyond
  `3.31×10¹⁵` — settling that family up to the bound; four linked differences
  remain open.
- **The eight-square sub-question**: no example known, no proof — an exact
  statement of "what an 8-square grid would force" is a plausible partial result.
  Bremner's 7-square witness has exactly two half-realised endpoints; going from
  7 to 8 means realising one more — a precise target for an impossibility lemma.
