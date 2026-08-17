# Grounding verdicts — three inventor approaches (research role)

## DECISION (inventor, converging pass, appended 2025)

Decided after the grounding: **ADOPT `delsarte-union-closed-code`**;
refute the other two.

- `second-moment-cooccurrence` — REFUTED (killed-by in its file): Reimer
  double-counting / pair version of the averaging method; Ellis EJC 29(1):P1.23
  (2022) refutes overlap-forces-abundance; Raz (2017) shows average-size
  conditions do not force abundance; Wu (2412.03863) & Das–Wu (2412.03862)
  attack the exact c_xy LP object and stop at |F|/3 (Nagel).
- `coordinate-rank-recursion` — REFUTED (most decisively): the 3-way coordinate
  split is already the recursive decomposition of Moore co-families in
  Colomb–Irlande–Raynaud–Renaud (Ann. Math. & AI 67, 2013); that structural
  induction reaches only a proper class of Frankl families, explicitly not the
  conjecture. Bouchard's UC_{n−1}⟹UC_n is an equivalence reduction, not a
  closing step.

Why Delsarte won: (a) genuinely novel — no source applies Delsarte/
association-scheme moments to the OR-closed abundance (marginal ≥ 1/2)
question; Yu's OR-channel bound is first-moment only, capped ≈0.38234, the
exact gap this line attacks; (b) the machinery is real and active for
constrained/monotone codes (Rameshwar–Kashyap arXiv:2301.05098; IEEE-TIT dual
Delsarte programs 2024; Coregliano–Jeronimo–Jones ITCS 2022); (c) the hinge is
now a MEASURED gap rather than a vague worry.

First step (tool_builder can start today): for n ≤ 5 (n≤6 if cheap), from the
canonical oracle, decide exactly whether the "all coordinate marginals < 1/2"
slice is empty in each of three nested regions — R_true = hull of actual
OR-closed codes (slice MUST be empty, else oracle bug, since UC is verified to
n≈11), R_cont = Delsarte over containment-constrained codes C⊆A, R_del =
unconstrained Delsarte quasicode. Outcomes: hull-empty = computational UC
evidence from a non-entropy route; Delsarte-nonempty with hull-empty = barrier
theorem for the Delsarte relaxation locating exactly the missing finite-positive
description of OR-closure. Do not scale past n=6 (hull is 2^n-dimensional).

Re-store all of this into Cognee (`remember_memory`) once the server recovers.

Durable findings recorded here because the Cognee memory server was temporarily
unavailable at write time (`remember_memory` refused). These are the same
findings that would otherwise be stored in durable memory; re-store them when
the memory recovers.

## 1. `second-moment-cooccurrence` — REFUTED

The overlap/co-occurrence second-moment mechanism is (a) already the known
Reimer double-counting and averaging method, and (b) the "overlap forces
abundance" forcing claim is FALSE.

- David Ellis, "Union-Closed Families with Small Average Overlap Densities",
  Electron. J. Combin. 29(1):#P1.23 (2022), doi:10.37236/10121 — builds
  union-closed families with Average Overlap Density as small as
  Θ((log log|F|)/log|F|) for infinitely many n, disproving the Polymath
  conjecture that a universal second-moment/overlap lower bound would imply UC.
- Raz, EJC 2017, doi:10.37236/6989 (and Lu–Raz arXiv:2405.10639) — Reimer's
  average-size conditions do NOT force the abundant element.
- Shi-Chao Wu, arXiv:2412.03863 ("second frequency") and Das–Wu arXiv:2412.03862
  ("Frequent elements") already attack second-frequency by LP over incidence
  patterns (the c_xy object) and reach only Nagel's 2-good bound |F|/3, not
  |F|/2.
- The endgame identity Σ_x C(d_x,2) − Σ_A C(|A|,2) is the pair version of the
  classical first-moment identity Σ_u|A_u| = Σ_A|A| (Bruhn–Schaudt survey eq. 4)
  and Reimer's theorem (average set size ≥ ½ log₂|F|, CPC 2003), sharpened by
  Balla–Bollobás–Eccles JCTA 2013.

Verdict: refuted. The machinery is published and provably stops at |F|/3
(Nagel) and Θ(loglog/log) AOD (Ellis).

## 2. `coordinate-rank-recursion` — REFUTED

The exact 3-way coordinate split (F_0, F_x, F_x' + interaction constraint) is
already the published "recursive decomposition" of union-closed / Moore
co-families.

- Colomb, Irlande, Raynaud, Renaud, "A new generic class of Frankl's families"
  (2013) and "Recursive decomposition and bounds of the lattice of Moore
  co-families", Annals of Math & AI 67 (2013) 109–122,
  doi:10.1007/s10472-013-9345-y — decompose M_n by the last element into
  M_sup/M_inf with the f-map capturing the interaction; the structural-induction
  attempt on exactly this split reaches only a PROPER class of Frankl families,
  explicitly not the conjecture.
- Poonen, JCTA 59 (1992) 253–268 — coordinate decomposition for |∪F|≤7 and
  |F|≤28.
- Bouchard UC_{n−1} ⟹ UC_n (claim bouchard-ucn-minus1-to-ucn) confirms the
  induction direction is live but is an equivalence reduction, not a closing
  argument.

Verdict: refuted as a new line — the reformulation is previously attempted with
the same interaction mechanism, and it stopped short.

## 3. `delsarte-union-closed-code` — GROUNDED (genuinely novel application; hinge named)

Delsarte's LP is real and actively extended to constrained/monotone (OR-closed)
codes; NO source applies it to the OR-closed abundance (marginal ≥ 1/2) question.

- Rameshwar–Kashyap, arXiv:2301.05098 — extend Delsarte's LP to constrained
  codes C ⊆ A (Del(n,d;A)), handles monotone/OR-closed constraints.
- "New Solutions to Delsarte's Dual Linear Programs", IEEE Trans. Inf. Theory
  2024 (Sberlo–Shpilka; Loyfer–Linial arXiv:2211.12977 dual solutions) — applies
  to monotone (upward/OR-closed) codes and fractional/average-weight constraints.
- Coregliano–Jeronimo–Jones, ITCS 2022, doi:10.4230/lipics.itcs.2022.51 —
  higher-order Krawtchouk LP hierarchy confirms Delsarte moments beyond level 1
  encode pair structure.
- Yu, Entropy 25(5):767, 2023, doi:10.3390/e25050767 — frames UCSC as an
  OR-channel problem but is FIRST-MOMENT only, capped at ≈0.38234, confirming
  the higher-moment gap this line would attack.

The open hinge (the inventor's own flag, confirmed open by the literature):
whether OR-closure is expressible as finitely many POSITIVE moment/PSD
inequalities. The constrained-code papers handle OR-closure as code-containment
(C ⊆ A), not as a finite positive-moment description of the quasicode polytope.

Worth exactly one small-n (≤5/6) probe: is the "all-marginals < 1/2" slice of
the true OR-closed code hull empty, and separately of the Delsarte quasicode
region empty? (a) hull slice empty → computational evidence for UC from a
non-entropy route; (b) Delsarte slice nonempty → the Delsarte relaxation
provably cannot prove UC (a barrier theorem), and the gap between hull-empty and
Delsarte-nonempty is precisely the missing finite positive description.
