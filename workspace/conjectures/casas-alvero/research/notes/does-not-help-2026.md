# Sources that do NOT help this run, and why

The scholar digested the held library this pass. The following downloaded
sources turned out to be **off the run's path** or **mislabeled**; each is
recorded so a later pass does not re-read it. Keep this alongside the other
"does not help" assessments (okolo/leggett cranks, gasull abstract, three-proofs,
battiston/dobrowolski/lu claimed-proofs — recorded in scholar-digest-assessment.md).

## Mislabeled (wrong paper under a held filename)

- **`sources/abdesselam-chipalkatti-hilbert-covariants.full.md`** — the file holds
  Campagna & Pagh, "On Finding Frequent Patterns in Event Sequences"
  (arXiv:1010.2358, cs.DS, RFID baggage data-mining), NOT Abdesselam–Chipalkatti
  "On Hilbert covariants" (arXiv:1010.2667). Full detail in
  `notes/abdesselam-chipalkatti-mislabel.md` (claim
  `abdesselam-chipalkatti-file-mislabeled`). The intended Hilbert covariants
  paper is NOT held. The Hessian-iff-perfect-power theorem the hessian-covariant
  approach cites is therefore currently unanchored. Approach was already refuted
  on the unproved bridge, so this does not change the adopted route.

## Off the CA path (combinatorial / stochastic / analytic / number-theoretic)

- **`sources/adeniran_yan_goncarov-partition-lattices_2019.full.md`** (arXiv:
  1907.07814) — generalized Gončarov polynomials for delta operators, parking
  functions, partition lattices. This is the *enumerative combinatorics* of
  Gončarov interpolation, a different line from the run's Abel–Goncharoff
  *analytic* toolchain (Yakubovich 2013/2014, Massri normal form). The run's
  root-difference-coloring approach needs the analytic Abel–Gontcharoff
  polynomials and their bounds, not the delta-operator/parking-function
  generalisation. **Does not advance the run.** Do not re-read.
- **`sources/dzhaparidze_janssen_abel-goncharov-interpolation_1994` (pdf and
  html)** — a *stochastic* approach to the Abel–Goncharov interpolation problem
  (nodes as random variables), applied to Hellinger integrals and the
  arithmetic-geometric mean. The Abel–Goncharoff *toolchain* relevant to this run
  is already held in the analytic form (Yakubovich 2013/2014, Macintyre 1949,
  Levinson-via-Macintyre). The stochastic framing adds no derivative-sharing
  content. **Does not help.** Retain only as evidence that the Abel–Goncharoff
  theory tier is covered. Do not re-read.
- **`sources/lang1990_old-new-conjectured-diophantine-inequalities.full.md`**
  (Bull. AMS 1990) — Lang, diophantine inequalities / heights on elliptic
  curves. Nothing to do with the CA derivative-sharing system. Likely fetched by
  an over-broad "interpolation / number theory" search. **Does not help.** Do not
  re-read.
- **`sources/casas-alvero_2012_siebeck-curves.full.md`** and
  **`sources/casas-alvero_2012_roots-and-foci.pdf.full.md`** — the original
  Casas-Alvero 2012 papers refining the Gauss–Lucas theorem by locating
  derivative roots in sets smaller than the convex hull (Siebeck curves, foci of
  real algebraic curves). These are the *originating motivation* (plane curves,
  out of scope per GOAL.md). The convex-hull refinement the run's
  root-difference-coloring thread needs is already held via **Polstra 2012**
  (Thm 3.1: a CA counterexample over C has a root not a vertex of its convex
  hull; claim `polstra-convex-hull-theorem`). The Siebeck/foci papers give the
  geometric machinery but nothing load-bearing the run does not already have.
  **Background only** — read enough to know the roots of the question, then leave.

## One genuinely-relevant-but-already-digested pair

- **Kostov 2017 "A property of discriminants"** (arXiv:1701.02912) and
  **Kostov 2020 "On higher-order discriminants"** (arXiv:1702.08216) — the
  higher-order discriminants D̃_m = Res(P, P^(m)) are the SAME resultant family as
  the run's R_i = Res(f, H_i f). Both fully digested already (summaries carry the
  Theorem + Prop 1 + structure); this pass added a claim block
  (`kostov-higher-order-discriminant-two-shared-roots`) capturing the
  load-bearing fact that C_{m,k}=0 = "P and P^(m) share two distinct roots",
  which is exactly the shared-root-multiplicity structure the coincidence thread
  targets. Char-0 only.
