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

**Bremner's rank conjecture is proved — sourced, two independent routes**
(Garcia-Fritz–Pasten, arXiv:2604.04850v2, May 2026, 21KB; Theorem 1.8,
**ineffective** constant C) and (Harrison–Mudgal–Schmidt, arXiv:2603.06483, Mar
2026, 132KB HTML full text on disk; Theorem 1.1, **effectively computable**
constant C). Both prove: all APs in x- or y-coordinates of a rank-r E/Q have
length ≤ C^(1+r). GFP via Nevanlinna + uniform Mordell–Lang; HMS via additive
combinatorics (PFR of Gowers–Green–Manners–Tao) + David–Philippon. HMS also
bounds geometric progressions and consecutive squares, and extends to
generalised APs of arbitrary rank k (Corollary 2.2: |P| ≤ D^(1+r) for proper
GAPs in C(Γ)).

**Bearing on the MSS**: the Robertson reduction says an MSS exists iff there
is `e` with three points of `2E(Q)` on `E: y² = x(x²−c²)` with x-coordinates
in AP (length 3). GFP/HMS bound AP length by `C^(r+1)` for *any* points in
E(Q). **The doubled-point question is settled** from §1.1 of both papers: AP
is x(P_i) for P_i ∈ E(Q); 2Q_i ∈ E(Q), so doubled points are covered — no
mismatch. **GFP's C is ineffective** (Rémond→UMordell–Lang); **HMS's C is
effectively computable** but built from David–Philippon + PFR and almost
certainly >> 3, so C^(r+1) < 3 fails for any plausible rank. The theorem
reframes the problem as bounding rank(E_e) but does not close it. Theorem 1.2
(conditional): if ranks of elliptic curves over Q are uniformly bounded, then
AP lengths are uniformly bounded — this would reduce MSS to a finite
computation (though likely beyond reach). The conditional reduction is the
best structural result from this line.

**Hulse–Kuan–Lowry-Duda–Walker (2024) — sourced, just re-downloaded** (arXiv:2007.14324,
68KB, real paper, was a 19KB Springer paywall). Counts primitive three-term
APs of squares {a²,b²,c²} via a double Dirichlet series D(s,w) with
meromorphic continuation to C²; Tauberian estimates give asymptotic
#APs(middle ≤ X) ~ (√2/π²)log(1+√2)·X^{1/2}. **Bearing**: the building
blocks of the MSS are 3-square APs through the centre; Hulse gives analytic
control of their count. Consistent with but independent of the run's
algebraic |S(e)| formula. Not yet claim-blocked; scholar must digest.

**Wolird (2023) — sourced, just re-downloaded** (arXiv:2310.12164, 11KB, real
paper, was a 5.8KB arXiv abstract wrapper — fourth time a wrapper was fetched).
Shows arithmetic triplets of Gaussian squares are in 3-to-1 correspondence
with Pythagorean triples; an MSS solution over Q would generate non-trivial
near-misses in Z[i] ("backwards result"). **Bearing**: extends the
extension-field MSS picture from Bremner 1999 (Q(√3,√133)) into Gaussian
integers; the correspondence is explicit and checkable. Not yet claim-blocked;
scholar must digest.

**p-adic/modular obstruction to Φ no-triple — checked and bounded** (DIRECTIVE 8).
`code/witness_padic_falsification.py` verified both near-miss witnesses
against the proved p-adic facts: every positive fully-realised Φ-element from
Bremner (5544/7225, 336/625) and Sallows (3360/12769) satisfies v2≥3, v3≥1,
res=0 mod 3, res=0 mod 5. For every p∈{2,3,5,7,11,13} and p^a≤2000, the
residue set is additively closed; mod 3/5 collapse to {0}. Claims
`phi-padic-no-obstruction`, `phi-padic-consistent-with-witnesses`,
`phi-padic-residue-closure` all `status: checked` in CLAIMS.md with exact
bounds — NOT the stronger unbounded statement. A proof must use
rationalness/integrality beyond congruences.
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
- **The Faltings-fibre attack on the Φ-triple is dead — confirmed by execution**
  (`phi_fibre_genus_run.py`, `phi_fibre_genus_check.py`, both captured in
  `code/out/`). f is homogeneous degree 0, so f(m,n) depends only on the ratio
  r=n/m; the fibre f(p,q)=C is a quartic g(r)=C in ONE ratio, ≤4 roots, and each
  root sweeps a whole line through the origin (genus 0). There is no genus-≥2
  curve in this fibration, so Faltings' finiteness never engages. Also confirmed:
  the f(P_k,P_{k−1}) = 1 − 1/P_{2k−1}² Pell-pair identity (record maxima of |Φ(B)|),
  extended |Φ(B)| closed-form values (|Φ(500)|=50765, |Φ(1000)|=202861,
  |Φ(2000)|=811155, |Φ(3000)|=1824231), and the canonical-pair→f bijection (with
  orbit-collision caveat in `phi_canonical_check.py`).
- **Do not build on a Φ "dominance" argument — that bound is false** (`phi_identity_verify.py`
  [5b], correct self-flag; in durable memory). Although record maxima of
  f occur at Pell pairs f(P_k,P_{k−1}) = 1 − 1/P_{2k−1}², the claim
  "f(m,n) < 1 − 1/P_{2k−1}² whenever m < P_{2k−1}" is FALSE: 2980 real
  counterexamples, e.g. f(12,5) = 1 − 1/169² > 1 − 1/29² while 12 < 29 = P₅.
  Record placement does not bound values below its own index; any argument
  sieving near-1 Φ-values by a Pell-index ceiling is dead.

**Φ 2,3-adic and modular structure — proved/checked** (`phi_pattern_findings.md`,
`phi_valuation_proof_check.py`, `phi_padic_closure_exact.py`): every
`q = f(m,n) ∈ Φ` (primitive `m>n≥1`, reduced) has `v2(q) ≥ 3` and `v3(q) ≥ 1` —
every centre-AP difference `d/e²` is `0 mod 8` and `0 mod 3` (proved, confirmed
over all 48,677 primitive pairs `m≤n≤400`). This is **necessary, not a sieve**:
a sum of two 0-mod-8 values is 0-mod-8, so the additive relation `q1+q2=q3` gives
no residue contradiction. No pure p-adic modular sieve can prove the no-Φ-triple:
for every `p ∈ {2,3,5,7,11,13}` and `p^a ≤ 2000` the residue set
`R = {f(m,n) mod p^a}` is non-degenerately **additively closed** (checked two
independent ways). Reinforces the Ruled-out "locally solvable mod every prime
power": a proof must use rationalness/integrality beyond congruences. Also:
`f(m,n) < 1` strictly (sup = 1 only at the irrational `tan(π/8) = √2−1`), so the
additive-chain clip `q1+q2 < 1` is real and is what kills Bremner's near-miss.

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

**Existence for n×n, n ≥ 4 — sourced but does not touch 3×3** (Rome–Yamagishi
2024, arXiv:2406.09364, `research/summaries/rome-yamagishi-magic-squares-of-powers-2024.md`):
Theorem 1.2 proves an n×n magic square of squares exists for every n ≥ 4 (circle
method), settling Várilly-Alvarado's conjecture; Theorem 1.3 extends to d-th
powers. The n = 3 case is **excluded** — the circle method's column-independence
threshold is not met there. So the obstruction is genuinely 3×3-specific;
higher-n existence is settled and gives no structural handle on n = 3.
A supporting hint (not a proof): Bremner/BTVA22 note the 3×3 surface cut by 6
quadrics in P⁸ contains only finitely many genus-0/1 curves, and (per Lang) only
finitely many rational points outside them.

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
yet cashed out. **`S(Q)` is explicit nonempty — computed+checked this cycle**
(`reconciliation_2026-08-12.txt` Task D, exact): P = (345,196,−304,255,−396,−25)
realises T²+U²=V²+W²=X²+Y²=157441 and TU+VW+XY=0 (a=2TU=135240, b=2VW=−155040,
a+b=−2XY); the grid is a genuine six-square magic square (all 8 lines = 472323).
Consequence: no Brauer–Manin obstruction can prove S(Q)=∅ — the
brauer-manin-k3-surface approach is dead *outright*. The NS-rank-12 and
even-degree facts stand because they concern curves/divisors on S, not isolated
Q-points.

**Six-square configurations** (Boyer search, citing Bremner 2001): all sixteen
six-square-entry configurations are attainable; smallest-magic-sum six-square
example is (centre 145) `265 1² 13² / 7² 145 241 / 11² 17² 5²`.

**Approach statuses** (`research/APPROACHES.md`):
- **uniform-height-bound-elliptic-ap** — **adopted** (this round). Uses
  Garcia-Fritz & Pastén (2026) and Harrison–Mudgal–Schmidt (2026) uniform
  Mordell–Lang / sum-product to bound AP length on E_e: y² = x(x²−c²).
  GFP gives C^(r+1) with C ineffective; HMS gives C^(r+1) with C effectively
  computable but astronomically large. Doubled-point question settled
  (x(2Q) is x(P) for P = 2Q ∈ E(Q)). Constant size blocks a contradiction;
  conditional reduction to a finite computation (Theorem 1.2, assuming uniform
  rank boundedness) is the best structural result. Thread:
  `uniformity-bremner-ap-bound`, status: effective-constant-advance-hms-2026.
- **root-number-parity-four-curves** — **refuted** (this round). Birch–Stephens
  fixes parity by n mod 8; no additive-relation→root-number contradiction
  exists; Q-level mod-2 cannot separate Q from extension fields with MSS.
- **Brauer–Manin on the K3** — **refuted** (S(Q) explicit nonempty via the
  Category III point P=(345,196,−304,255,−396,−25); an analytic BM obstruction
  cannot prove S(Q)=∅ — see K3 section).
- All others: **refuted** with reasons in APPROACHES.md.

## Ruled out

- **Pure modular/congruence sieves cannot prove non-existence** — system is
  locally solvable mod every prime power. `asserted-by-source`; run any modular
  lemma against the witness set above.
- **A blanket "structural impossibility" argument is dead on arrival** because
  MSS exist over proper extension fields (Established). Any argument that cannot
  separate `Q` from `Q(√3,√133)` proves too much. Likewise any lemma that forbids
  the "two realised + two half-realised" pattern of Bremner's 7-square witness is
  false.
- **p-adic/modular obstruction to Φ no-triple** — **checked.** For every
  prime p ∈ {2,3,5,7,11,13} and p^a ≤ 2000, the achievable residue set is
  non-degenerately additively closed; mod 3 and mod 5 collapse to the single
  trivial residue {0}. Verified on both near-miss witnesses. No pure p-adic
  sieve over these primes can prove the no-triple conjecture; a proof must
  use rationalness/integrality beyond congruences.
  `phi-padic-no-obstruction`, `phi-padic-consistent-with-witnesses`,
  `phi-padic-residue-closure`, all `status: checked` in CLAIMS.md.
  Bounded claim: primes {2,3,5,7,11,13}, p^a ≤ 2000 — not an unbounded
  statement.
- **S-unit equations** — refuted, reason above (no new leverage; weaker than the
  Faltings finiteness Bremner II already gets).
- **Faltings fibre of the Φ-triple** — refuted, now executed (`phi_fibre_genus_run.py`,
  `phi_fibre_genus_check.py`): f is homogeneous-degree-0, so the fibre f(p,q)=C
  degenerates to ≤4 lines through the origin (genus 0); Faltings (genus ≥ 2 ⇒ finite)
  never applies. This is the "phi-triple-curve-genus-faltings" approach closed for
  its actual mechanism.
- **Simultaneous 2-Selmer of the four congruent-number curves** — refuted,
  reason above (subsumed by Bremner II's K3 data).
- **Descent needs the exact variety first** — finish the elliptic/K3 reduction
  before Fermat-style descent.
- **A search is not a proof**; extending a bound only to falsify a structural claim.
- **Substituting a solved root back into the equation it solved** — the Ferreira
  (arXiv:1506.06621) failure mode. The paper solves (46) for z, keeps the root
  z2, substitutes z2 back into (46), and reads the result as a constraint on
  m,n,w. Since z2 is by construction a root of (46), the substitution is
  identically 0. This manufactures a vacuous identity that looks like a
  constraint. Audit this run's own p-adic, Φ-identity, and descent code for
  the same anti-pattern before trusting any elimination step. Claim
  `ferreira-1506-06621-refuted`, status: checked, in CLAIMS.md.

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
grid — none found. Necessary-condition check, not a proof. Extended exact
`|Φ(M)|` (closed form, `phi_canonical_check.py`): |Φ(500)|=50765, |Φ(1000)|=202861,
|Φ(2000)|=811155, |Φ(3000)|=1824231; record max f values follow
`f(P_k,P_{k−1}) = 1 − 1/P_{2k−1}²` with odd Pell hypotenuses 5,29,169,985,…
(i.e. maxima occur on Pell pairs; m=2→24/25, m=5→840/841, m=12→28560/28561, …).

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
- **Garcia-Fritz–Pasten constant C is ineffective, HMS constant C is effectively
  computable but astronomically large** — C^(r+1) < 3 fails for any plausible
  rank. The approach `uniform-height-bound-elliptic-ap` is sound on definitions
  (doubled points covered), blocked by constant size. The conditional
  reduction to a finite computation (Theorem 1.2, assuming uniform rank
  boundedness) is the best available structural result from this line.
- **Rank of the Robertson curve** `E_e: y² = x(x²−c²)` for candidate c:
  Bremner's witness c=138600 gives rank 2; a putative MSS would need rank ≥ ?
  Can we bound rank(E_c) in terms of the number of sum-of-two-squares
  representations of the parameters?
- **Φ-triple beyond m,n ≤ 400** — the absence of a Φ-triple through m,n ≤ 400 is
  the current structural frontier, but it is verified-numerical only, not a proof;
  its natural falsifier is a Φ-triple found beyond the range (a true hit would
  *construct* a 7-square magic grid). The φ-universal-set and φ-no-triple-m400
  claims are now claim blocks in `research/CLAIMS.md` (via `code/out/phi_claim_blocks.md`,
  status checked-as-recorded). The two remaining open thread steps: write the
  additive-triple condition as a polynomial variety and correlate with Morgenstern's
  (a,b,a+b) equal-start census.
- **Exact reduction unanchored end-to-end**: the curve/K3 correspondence
  "rational point ⇒ distinct positive integer square solution" is not a claim
  block. Blocks any descent.
- Whether the four-AP condition (differences `u,v,u+v,u−v`) maps onto a known
  concordant-forms/congruent-numbers problem. Morgenstern's exhaustive search
  found no three *primitive* equal-`d` APs beyond `3.31×10¹⁵`; four linked
  differences remain open.
- **The eight-square sub-question**: no example known, no proof. Bremner's
  7-square witness has exactly two half-realised endpoints; going 7 → 8 means
  realising one more — a precise target for an impossibility lemma.
- **Wu 2103.01784 re-downloaded — source is real, digest is not.** The full
  paper is now 78KB of real content (previously 6.6KB abstract wrapper). The
  auto-generated digest in `research/summaries/wu-non-invariance-brauer-manin.md`
  still needs the scholar to replace it with a proper summary. The claim
  `wu-bm-noninvariance-under-base-change` now has a real source behind it
  (conditional on Stoll's conjecture, with unconditional special cases for
  Q/Q(i)).