# Llibre et al. 2024 — From Abel's equations to Hilbert's 16th problem

Full text: [[llibre-abel-to-hilbert16-survey-2024.full]]. CDM/Survey, 2024.

## What the source establishes (held full text)

Independent recent survey of the state of the problem. Key statements:

- **Dulac's finitude problem is again considered open (2024):** "Écalle and
  Il'yashenko asserted that each individual vector field of the form (1) has a
  finite number of limit cycles. Nevertheless, nowadays these proofs are not fully
  accepted by the mathematical community ... In fact, in the recent preprint [137]
  the author shows a gap in Il'yashenko's proof. At the moment this individual
  finitude problem, also known as Dulac's finitude problem, begins to be
  considered again as an open problem." — independent corroboration of the Yeung
  2024 contention's standing in the community.
- **Lower bounds:** H(2) ≥ 4 ([CW],[Shi]); it is "thought that H(2) will be 4,
  but this seemingly simple problem is resisting all the available approaches";
  "it is not even known if H(2) exists although there are proofs of Bamón and
  **Romanovskii** that each individual quadratic differential equation has
  finitely many limit cycles"; Chicone–Shafer proved the same restricted to any
  compact region. H(3) ≥ 13; H(4) ≥ 28.
- **H(n) growth:** H(n) grows at least O(n² log n) (Christopher–Lloyd 1995). Note
  on conjectured upper growth: Lloyd conjectured O(n³); Smale asks if there is a
  universal q with H(n) ≤ n^q. (Both open.)
- **Roussarie's program / finite cyclicity:** compactify phase space + parameter
  space, reduce global finiteness to finite cyclicity of "limit periodic sets";
  for n=2, DRR's list of all possible limit periodic sets, with which are known
  finitely cyclic and which remain — cross-confirms the DRR frame.
- **Liénard/Abel:** Lins–Melo–Pugh conjecture false for n≥6; best lower bound
  n−2 cycles for n≥6 (De Maesschalck–Dumortier); for ODD F_n the LMP conjecture
  is still open (all more-cycles examples have non-odd F_n); n=3,5 LMP holds.
- The last section: Abel equations are strongly related to determining H(2) — the
  Abel-equation route is a named (different) approach to H(2).

## What it implies here

- Corroborates h16-dulac-proof-contested and adds: the community treats Dulac's
  problem as re-opened; the n=2 pointwise finiteness has independent proofs
  (Bamón, Romanovskii) — so the n=2 frame does not depend on the contested step.
- Adds Romanovskii and Chicone–Shafer to the pointwise-quadratic source list.
- Confirms the lower-bound block (H(2)≥4, H(3)≥13, H(4)≥28, n²log n growth).
- The Abel-equation route to H(2) is a different attack than the DRR graphic
  program; record as an alternative approach (see approaches ledger), not the
  run's frame.

```claim
id: h16-dulac-reopened-community-view
statement: As of 2024, the mathematical community (per the Llibre survey)
  treats Dulac's finitude problem for individual fields as again under review:
  the proofs of Ecalle and Ilyashenko are not fully accepted, with a preprint
  (Yeung) showing a gap in Ilyashenko's proof.
hypotheses: status report, not a theorem.
holds-here: yes -- corroborates the 2024/25 gap contention via a second survey.
status: asserted
bearing: the run must report pointwise finiteness as 'settled modulo a disputed
  proof'; n=2 pointwise stands independently (Bamon, Romanovskii).
anchor: research/sources/llibre-abel-to-hilbert16-survey-2024.full.md
contradicts: (none -- same fact, second source)
follows-from: h16-dulac-proof-contested
```

```claim
id: h16-bamon-romanovskii-quadratic-pointwise
statement: Each individual quadratic vector field has finitely many limit
  cycles; proofs by Bamon (1986) and Romanovskii; Chicone-Shafer proved the same
  restricted to compact regions.
hypotheses: fixed individual quadratic field.
holds-here: yes
status: asserted
bearing: the n=2 pointwise pillar is multi-sourced and independent of the
  contested general proof.
anchor: research/sources/llibre-abel-to-hilbert16-survey-2024.full.md
follows-from: h16-bamon-quadratic-finiteness
```