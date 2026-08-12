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
impossibility lemma** (`code/out/near_misses.json`, `all_checks_passed: true`;
GOAL.md: a lemma that `refutes` a witness is false). Both 7-square near-misses
are built directly from the printed grids with exact arithmetic:
- **Sallows LS1** = 7 of 8 line sums = 147² = 21609, failing non-principal
  diagonal = 38307; all nine entries perfect squares and distinct. The user's
  orientation `[127,46,58;2,113,94;74,82,97]` is the transpose of Bremner's
  printed `[58,46,127;94,113,2;97,82,74]`; squares identical.
- **Bremner's 7-square true magic square**, all 8 lines = 541875, centre 425²,
  non-squares exactly 360721 and 222121: `373² 289² 565² / 360721 425² 23² /
  205² 527² 222121`.

**Structural extraction on Bremner's grid — computed-and-checked**
(`code/check_near_misses.py`, `code/out/check_near_misses_latest.txt` ALL CHECKS
PASSED): with `c=425²`, among the four AP differences `d ∈ {u, v, u+v, u−v}`,
**exactly two** have *both* `c±d` perfect squares — `d = v = 138600` (c±v =
565², 205²) and `d = u+v = 97104` (c±(u+v) = 527², 289²); the other two fail at
exactly one endpoint each (`u = −41496`, `u−v = −180096`). The two realised
relations are Pythagorean `425² = 385²+180² = 408²+119²` with `d = 2xy`. **A
proof of non-existence cannot forbid "two fully-realised + two half-realised AP
differences", since Bremner's grid is exactly that.**

**Φ rational reduction — the run's own structural line, computed-and-checked**
(code `ap_structure2.py`, `phi_exact_search.py`, `phi_extend.py`,
`bremner_phi_anchor.py`; verified sieve==x-loop for `e ≤ 1500`; membership test
verified vs brute force). Define `S(e) = {d>0 : e²±d both squares}`; then
- `d ∈ S(e)` ⇔ `e = k(m²+n²)`, `d = 4k²mn(m²−n²)` for primitive `m>n≥1`;
- dividing out `e²`: `d/e² = 4mn(m²−n²)/(m²+n²)² =: f(m,n) ∈ Φ`, with
  `Φ = {f(m,n)} = {sin(4·arctan(n/m))}` the **universal rational set,
  independent of e**; `d ∈ S(e)` iff `d/e² ∈ Φ` and `(m²+n²) | e`.
- Hence every MSS satisfies: exist `q1>q2>0` with `q1, q2, q1+q2, q1−q2` all in
  Φ (q = u/e², v/e²). **A Φ-triple lifts to a 7-square magic grid and a
  Φ-quadruple lifts to a full MSS** with centre `e = lcm(mᵢ²+nᵢ²)`.
- Exact membership test (uncapped): reduced `A/B ∈ Φ` ⇔ integer `s≠0` with
  `s² = B²−A²` and `(B±s)/2B` both rational squares.
- **Anchor**: Bremner `e=425`: `q_v = 5544/7225 ∈ Φ` via `(9,2)` [85 | 425],
  `q_{u+v} = 336/625 ∈ Φ` via `(4,3)` [25 | 425]; the two unsatisfied
  differences are **not** in Φ; and `q_v + q_{u+v} = 1.305 > 1` — the near-miss
  dies at the rational level on the additive/clip condition.
- **Conjectured (NOT proved)**: no additive triple `q1+q2 ∈ Φ` exists at all,
  hence no MSS over Q. Checked **exactly** for all pairs with `m,n ≤ 400`
  (156,988,030 unbounded membership tests, zero triples; also none through
  `m,n ≤ 200`). Status: verified-numerically on a finite range, conjectural as
  a theorem — **not a proof of non-existence**. Any claim beyond the range is
  `conjectured` until attacked.

**|S(e)| analytic form and records — computed-and-checked** (`ap_structure2.py`
[0], `pattern_seq.py`, exact sieve vs direct enumeration `e ≤ 1500`):
`|S(e)| = (∏_{p≡1 mod 4, p^a || e} (2a+1) − 1) / 2`. Max `|S(e)| = 202` at
`e = 9,773,725` over `e ≤ 10⁷`. Number of `e ≤ 10^k` with `|S(e)| ≥ 4`:
0, 2, 81, 1491, 20806, 254549, 2924760 (k=1..7) — **millions of centres admit
four AP-differences**; scarcity of differences is not the obstruction, the
additive relation among `u,v,u+v,u−v` is.

**Elliptic reformulation — sourced** (Bremner 1999; attributed to Robertson): a
MSS of squares ⇔ there is `e` with three points of `2E(Q)` (x-coords in
arithmetic progression) on `E: y² = x(x²−c²)`; a point is in `2E(Q)` iff
`X, X±c` are all rational squares. Bremner searched points of `E(Q)` in AP and
found essentially none; very restrictive when `rank E(Q)` is small.

**Magic squares of squares exist over extension fields — sourced, and this is the
hinge.** Bremner 1999 constructs genuine MSS over algebraic number fields: a
family over `Q(i,√(u³−u))`, an explicit example over `Q(√3,√133)` (degree 4),
and one over `Q(u)` of degree 27. So non-existence over `Q` **cannot** be a
purely structural/geometric impossibility — any proof must use
rationalness/integrality essentially. A blank impossibility argument that would
also kill these extension-field examples is false.

**K3 surface (Bremner II 2001)**: problem (B) is studied via a K3 `S` over
`Q(λ)`; `NS(S,Q)` generated by twelve divisors `Γ1…Γ12`; every rational curve on
`S` has even degree; the relevant elliptic fibration has
`E_λ(C(λ)) ≅ Z×Z×Z/4Z×Z/2Z`. Deep, sourced; how it bears on `Q`-integrality not
yet cashed out.

**Six-square configurations** (Boyer search, citing Bremner 2001): all sixteen
six-square-entry configurations are attainable; smallest-magic-sum six-square
example is (centre 145) `265 1² 13² / 7² 145 241 / 11² 17² 5²`.

**Approach statuses** (`research/APPROACHES.md`):
- **Brauer–Manin on the K3** — **adopted**. `S` is the intersection of three
  quadrics in P⁵ from configuration III; Bremner computed NS(S,C) (rank 20),
  NS(S,Q) (rank 12, generators Γ₁…Γ₁₂), intersection form, singular fibres.
  Missing step: compute `Br(S)/Br(Q)` (algebraic part H¹(Gal,NS) + transcendental)
  and evaluate the BM pairing on adelic points from local solubility.
- **S-unit equations over the parametrisation** — **refuted**: correct but adds
  no leverage; Bremner II already shows the constraints reduce to genus ≥ 3
  hyperelliptic curves (finite rational points by Faltings), and S-unit
  finiteness is a weaker form of the same conclusion.
- **Simultaneous congruent-number / 2-Selmer** — **refuted**: the four curves'
  Selmer data is already encoded in Bremner II's NS and singular-fibre geometry;
  no advantage over working directly with the K3.

## Ruled out

- **Pure modular/congruence sieves cannot prove non-existence** — system is
  locally solvable mod every prime power. `asserted-by-source`; run any modular
  lemma against the witness set above.
- **A blanket "structural impossibility" argument is dead on arrival** because
  MSS exist over proper extension fields (Established). Any argument that cannot
  separate `Q` from `Q(√3,√133)` proves too much. Likewise any lemma that forbids
  the "two realised + two half-realised" pattern of Bremner's 7-square witness is
  false.
- **S-unit equations** — refuted, reason above (no new leverage; weaker than the
  Faltings finiteness Bremner II already gets).
- **Simultaneous 2-Selmer of the four congruent-number curves** — refuted,
  reason above (subsumed by Bremner II's K3 data).
- **Descent needs the exact variety first** — finish the elliptic/K3 reduction
  before Fermat-style descent.
- **A search is not a proof**; extending a bound only to falsify a structural claim.

## Numbers

**Oracle exists and has run** — `code/out/oracle_output.txt`, `status: checked`,
exhaustive exact scans. No 3×3 magic grid with entries `1..100` has six or more
**distinct** square entries (best = 5, e.g. `c=100,u=96,v=21` → rows
`[25,196,79],[154,100,46],[121,4,175]`); same in the near-miss box
`c=e², e≤80, |u|,|v|≤120` (4,052,328 grids). The `{6:964, 7:4, 9:92}`
distribution is of *total* square entries over all-positive grids, repeats
allowed; the `7:4` are repeated-entry near-misses, **not** four distinct
7-square grids (resolved Contradiction below); the 9-square grids are trivial
repeats (all-`k²` and the `{1,25,49}` family).

**Φ no-triple range** (exact, unbounded membership; `phi_exact_search.py`,
`phi_extend.py`): `|Φ(M)|` = 22, 86, 331, 737, 1314, 2040, 2930, 4582 for
M = 10..150; 8156 (M=200); 32495 (M=400). No additive triple for any pair from
`m,n ≤ 400` (156,988,030 tests). A triple would have lifted to a 7-square magic
grid — none found. Necessary-condition check, not a proof.

**The literature's actual computational bound — sourced** (Morgenstern 2013,
`research/summaries/morgenstern-extended-searches-2013.md`): 3809 instances of
**three** APs of squares with equal `d` (all odd entries) from complete
enumeration to `d ≤ 2.4×10¹⁹`; only **5** of three *primitive* APs, none beyond
`d ≈ 3.31×10¹⁵`; surviving cases reduce to one `d = 71831760` (two grids) plus
two huge `d`. A true MSS needs **four** APs through the centre with differences
`u,v,u+v,u−v`. Bound on where arguments must look (10¹⁹–10²²).

**Witness set values** (exact): Sallows failing diagonal 38307; Bremner magic
constant 541875, centre 425², non-squares {360721, 222121}, realised AP diffs
`v=138600`, `u+v=97104` with Pythagorean pairs `(385,180)`, `(408,119)`.

## Recalled

Durable memory holds the **Φ no-triple to m,n ≤ 400** (tool-builder run,
`phi_extend.py`, exact, zero triples) — consistent with this run's code, and it
is the verified-numerical basis for the conjecture above. Memory also holds
Bremner 1999 extension-field material (degree-4 and degree-27 examples),
consistent with this run's source reading. The earlier recalled "4 **distinct**
7-square non-magic grids in the near-miss box" is **resolved against** by the
computed oracle (see Contradictions). No other prior-run finding disagrees with
the Established section.

## Contradictions

- **Durable memory vs. `oracle_output.txt` on 7-square distinct grids**: resolved
  in favour of the computed oracle. `near_miss_scan` (code/brute.py) reports
  best-with-distinct-entries = 5 in the box `c=e², e≤80, |u|,|v|≤120` (4,052,328
  grids); the `{7:4}` count is over all-positive grids with repeats allowed.
  Claim block and raw output are the authority (a scratch prose note claiming 4
  distinct 7-square grids is wrong, as durable memory itself flags).
- **Approaches status vs. CONTEXT.md's stale "all three proposed"**: resolved in
  favour of `research/APPROACHES.md` — Brauer–Manin adopted, S-unit and 2-Selmer
  refuted with reasons; this file now says the same.
- **Cycle brief's graph-theory method vs. the actual problem**: the graph /
  minimal-counterexample framing does not apply; method is arithmetic geometry
  (`GOAL.md`). No source states a graph reduction.
- `problem.md` frames non-existence as primary while several experts treat
  existence as open both ways; keep one thread on existence.

## Gaps

(Double as research requests; see `research/REQUESTS.md`.)
- **Φ and |S(e)| results are not yet claim blocks in `research/CLAIMS.md`** —
  they live in scratch + durable memory + code only. Promote them (with
  falsifiers) before any impossibility lemma is built on them: the absence of a
  Φ-triple through m,n ≤ 400 is the current structural frontier, and its
  natural falsifier is a Φ-triple found beyond the range (a true hit would
  *construct* a 7-square magic grid, not merely refute).
- **Exact reduction unanchored end-to-end**: the curve/K3 correspondence
  "rational point ⇒ distinct positive integer square solution" is not a claim
  block. Blocks any descent.
- **k3_surface_checks.py exists but unverified** (`code/out/`): its docstring
  asserts Bremner II's Category III six-square yields a `Q`-rational point on
  the K3 `S`, so `S(Q)` nonempty and no Brauer–Manin obstruction could prove
  `S(Q)=∅`. If true this closes `brauer-manin-k3-surface` outright (nothing to
  obstruct) — run it and decide before spending budget on Br(S)/Br(Q).
- Whether the four-AP condition (differences `u,v,u+v,u−v`) maps onto a known
  concordant-forms/congruent-numbers problem. Morgenstern's exhaustive search
  found no three *primitive* equal-`d` APs beyond `3.31×10¹⁵`; four linked
  differences remain open.
- **The eight-square sub-question**: no example known, no proof. Bremner's
  7-square witness has exactly two half-realised endpoints; going 7 → 8 means
  realising one more — a precise target for an impossibility lemma.