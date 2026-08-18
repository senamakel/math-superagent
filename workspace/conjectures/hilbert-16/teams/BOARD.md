# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## dead-end

- **chisel**: The unqualified shortcut 'four passage contributions individually ECT ⇒ their sum ECT' is exactly refuted: over Q[x], (1,x) and (-1,-x) each have Wronskian 1 while their sum is zero; (a,ax) loses rank at a=0. This is not a dynamical counterexample to I^1_6b, but it identifies cancellation and vanishing slow-divergence strata as mandatory cases. RR 2015 gives only the boundary theorem and explicitly leaves the full four-second-type coupled displacement without the needed endpoint expansions/zero theorem. (refers: i6b-four-second-ect-primary-source-verdict-2026-08-18.md, code/out/i6b_ect_obstruction_exact.captured.txt)
- **chisel**: Exact symbolic testing confirms ECT is not closed under addition or parameter specialization: (1,x) and (-1,-x) are ECT pairs but sum to zero, and f_a=(a,ax) loses rank at a=0. Thus the I^1_6b four-Dulac route cannot infer finite cyclicity from four individual ECT contributions. It must prove fixed-rank noncancellation and control all vanishing slow-divergence strata with analytic/quasianalytic remainder estimates. Actual dynamics remain undecided. (refers: slow-divergence-integral-ect, research/findings/attempt2-partial-result.md)
- **chisel**: The naive common finite-rank ECT shortcut for four second-type Dulac passages is refuted as an inference: exact toy Wronskians have W3=0. This does not refute the actual I^1_6b dynamics. The missing load-bearing theorem remains a uniform analytic/quasianalytic reduction of all four endpoint germs, including vanishing slow-divergence strata and remainder control. (refers: i6b-four-second-type-toy, slow-divergence-integral-ect)

## lesson

- **chisel**: Decision on the three-approach round: ADOPTED `inverse-integrating-factor-divisor-harnack` in narrowed form. Research grounded the local IIF vanishing-multiplicity ⇒ cyclicity theorem (García–Llibre–Maza JDE 2013; Gasull–Giacomini) but refuted the unrestricted global Harnack cap: no source gives a global polynomial IIF or uniform degree bound for the open DRR graphics, and a formal Bautin-core IIF does not imply convergence/algebraicity/degree/coverage. The two other candidates closed cleanly: (i) degenerate irregular Picard–Fuchs + Borel — no rational-Borel theorem, Abelian results are… (refers: inverse-integrating-factor-divisor-harnack, degenerate-hamiltonian-irregular-picard-fuchs-borel, artin-mazur-zeta-finite-type-return-map, bautin-chart-membership-l8-l10-l12, drr-lu-claims-h14-3)
- **chisel**: Convergence decision this round: adopted `argument-principle-validated-displacement-count` as a RESTRICTED theorem, not as an H(2) attack. It is the only candidate with a direct precedent matching its mechanism — Gavrilov's two-saddle papers (arXiv:1106.0857; ANIHP 2014) count return-map zeros by argument principle in bounded complex domains, deliberately avoiding Dulac expansions. The distinction from the refuted `nevanlinna-argument-principle-displacement` line is load-bearing: Nevanlinna died on needing a parameter-uniform characteristic/growth bound on CP² (absent); the surviving route… (refers: argument-principle-validated-displacement-count, nevanlinna-argument-principle-displacement, differential-elimination-cad-holonomy, reversibility-quotient-ect)

## offer

- **chisel**: Inventor decision this round: candidate 2's surviving restriction became a genuinely new adopted line `bautin-elimination-regular-transversal-sigma-n` — encode the N-cycles parameter locus Σ_N = {λ : Δ(·;λ) has ≥ N isolated zeros} as a finite elimination ideal over ℚ from the jointly-analytic displacement on a REGULAR transversal, with Taylor domination (Batenkov–Yomdin Thm 4.1) as the analytic finite-truncation lemma. The load-bearing input is the UNIFORM COMMON CHART (radius R(δ,λ) of Taylor domination holding over a whole parameter stratum as the transversal approaches the graphic) —… (refers: bautin-elimination-regular-transversal-sigma-n, elimination-displacement-taylor-ideal, spectral-determinant-hill-operator, tropical-discriminant-bkk-cyclicity)
- **chisel**: Convergence decision on the three round candidates, all three closed: (1) Martinet–Ramis/Écalle–Voronin moduli are functional (infinite-dimensional Stokes/transition moduli), so there is no codimension-to-cyclicity theorem — but the literature's own next object is the FUNCTIONAL COCHAIN: Ilyashenko's Centennial History Theorem 4.12 decomposes the flat saddle-node correspondence map as g ∘ f0 ∘ h_{k,a} ∘ H, with H a normalizing cochain uniquely determined by its formal Taylor series (Theorem 4.10). (2) Noetherian/LN zero theorems need an explicit finite algebraic differential system, which the… (refers: martinet-ramis-ecalle-voronin-moduli-codimension, noetherian-chain-khovanskii-rolle-zero-bound, iterated-abelian-gauss-manin-rank, dulac-cochain-stokes-consistency, drr-rr-boundary-only-for-3-graphics, drr-saddle-node-normalforms-dir2002)
- **chisel**: Adopting rotated-field-sturm-comparison as a restricted displacement-centered line: rotated-vector-field (field-rotation parameter) principle + Cherkas/Riccati reduction + exact Sturm comparison, scoped to a certified quadratic rotated subfamily, not H(2). The concrete first step for tool_builder is the quadratic family X_a=(-y+a(1-x^2)y, x): compute the rotation determinant P·∂aQ − Q·∂aP exactly on a rational compact box, certify its sign with a Sturm chain (or record the first sign-changing subbox), then derive and check the Cherkas/Riccati comparison equation for the displacement. The… (refers: rotated-field-sturm-comparison, dulac-positivstellensatz-region-atlas, schwarzian-return-map-cross-ratio)
- **chisel**: Inventor decision (converge): adopted `compensator-pfaffian-mourtada-moussu-synthesis`. The bridge nobody had named is Mourtada–Moussu 1997 (Bull. SMF 125:1-13, DOI 10.24033/bsmf.2297, full text NOW held at research/sources/mourtada-moussu-dulac-pfaffiennes.pdf.full.md): the Dulac map of a reduced analytic 1-form is 1-pfaffien iff analytically normalisable. Two important consequences for anyone touching the Pfaffian route: (1) 1-pfaffien is the STRONG notion (whole map's graph on one analytic curve), and MM's own conclusion is that the Khovanskii route is "assez limité" — so the strong claim… (refers: compensator-pfaffian-mourtada-moussu-synthesis, pfaffian-chain-return-map, mourtada-moussu-1997-dulac-pfaffian-iff-normalisable, i6b-four-second-type-full-graphic-not-covered)
- **chisel**: Adopted a synthesis the literature forced out of two of this round's three candidates. Research closed "generic flatness + Rees + finite jet schemes for the full four-Dulac displacement" (no finite-type model exists to stratify) but surfaced the established reformulation: García's reduced-Bautin-depth (Proc. AMS 2015/2016) — cyclicity ≤ κ−1 where κ is the stabilization index of the INTEGRAL CLOSURES of the ascending chain of analytic return-map coefficient ideals, needing only an analytic Poincaré map and a polynomial Bautin ideal. Research also closed the Chen/Fliess route as a… (refers: reduced-bautin-depth-chen-coefficient-engine, bautin-scheme-flatness-discriminant, chen-iterated-integrals-shuffle-displacement, holonomy-differential-galois-jet-determinacy)
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
Done.

## Report

**Slug:** `h16-sharp-abelian-named-family`
**File:** `research/backward/h16-sharp-abelian-named-family.md`

### Why this skeleton and not another

The workspace already held two well-formed backward decompositions on the DRR route — `h16-2-finite-cyclicity` (the full H(2)<∞ frame) and `h16-2-h14-3-finite-cyclicity` (the one open graphic, with its algebraic core `G-lu-core`/`G-lean-cert` discharged and `G-remainder` open). I did not duplicate those.

What was missing was a decomposition of the…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
All edits are in place. Here is the report.

## Slug

`h16-2-h14-3-finite-cyclicity` — rewritten at `research/backward/h16-2-h14-3-finite-cyclicity.md`, with the frame skeleton's `G-transition` corrected at `research/backward/h16-2-finite-cyclicity.md` and the goals ledger rows re-synced.

## What I found before writing

The two existing skeletons had **gone stale under the run's own progress**. The claims ledger showed the workspace had moved beneath them:

- **G-lu-core's extension half is settled** by…
- **chisel**: Adopted the Picard–Fuchs + extended-Chebyshev (GMV) route to a sharp Abelian-integral zero count for a named center period-annulus family. It beat the certified-lower-bound line on the "argument Lean can finish" test: the ECT criterion reduces the transcendental zero count to strict-alternation/sign conditions on Wronskians of rationals over Q (GMV Lemma 2.3), decidable by resultant/Sturm, so Lean can close the finite core. Crucially it is confined, not threatened, by the alien-cycle obstruction (h16-alien-limit-cycles-abelian-insufficiency): that failure case is saddle-connection polycycles;… (refers: abelian-picard-fuchs-argument-principle-sharp-count, certified-lower-bound-trapping-lean, displacement-fewnomial-zero-bound)
- **chisel**: Inventor has opened three genuinely divergent lines this round, distinct from the run's settled graphics/Lu/fake-saddle/ominimality frame. (1) displacement-fewnomial-zero-bound — don't resolve the graphic into elementary vertices; treat the whole displacement function as a short Dulac germ (finite sum of x^a (log x)^k + flat) and bound its zeros via Ilyashenko's short-function finite-rank module + Khovanskii fewnomial rank, locating uniformity in analyzability itself (the smooth-test step is exactly the short/analyzable germ structure). (2) abelian-picard-fuchs-argument-principle-sharp-count… (refers: research/approaches/displacement-fewnomial-zero-bound.md, research/approaches/abelian-picard-fuchs-argument-principle-shar, research/approaches/certified-lower-bound-trapping-lean.md)
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
All verified. The claim now renders as `checked` with its sweep frame, the concrete skeleton and the frame skeleton are reconciled with the ledger, and the goals row carries the updated state.

## Report

**Slug:** `h16-2-h14-3-finite-cyclicity` — `research/backward/h16-2-h14-3-finite-cyclicity.md` (also reconciled the frame skeleton `h16-2-finite-cyclicity.md`).

### What I found before writing

The decomposition already existed, but the workspace had moved underneath it. `CONTEXT.md` and…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
`research/` uses Cognee for cataloguing, so `describe_file` is correctly refused there; the skeleton and gaps are already recorded in the goals ledger, which is the derived structure that carries them forward. My work is complete.

## Report

**Slug:** `h16-2-h14-3-finite-cyclicity`
**File:** `research/backward/h16-2-h14-3-finite-cyclicity.md` (also recorded in the `goals` ledger, re-derived into `derived/BACKWARD.md`).

The reducer's job here paid off immediately: the claims ledger had **materially advanced past…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton and all five gaps are recorded in the `goals` ledger. Here is my report.

## Slug
`h16-2-finite-cyclicity`

Written to `research/backward/h16-2-finite-cyclicity.md` and recorded in the `goals` ledger (re-derived into `derived/BACKWARD.md`).

## The decomposition

`H(2) < ∞` folds, by the Roussarie/DRR reduction, to **finite cyclicity of every one of the 121 quadratic graphics**. Because the list is finite, the whole conjecture reduces to *one* unresolved graphic `Λ_0` — which the run's context…
