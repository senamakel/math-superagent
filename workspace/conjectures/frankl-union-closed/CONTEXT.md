# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

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

- **A scorer must be calibrated through the call the harness actually makes.** The uc-coupling harness invokes `python3 score.py candidates/<id>.py` (ONE module-path argument), not the five-float form the first `CALIBRATION.captured.txt` used — a scorer calibrated by hand can pass while the searcher's real call fails. Keep this lesson, but note it was only the plumbing half: the mathematical defect (missing inf) is the active one below.

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it.

- **The library is finished — stop adding sources.** 62 claims are in
  `research/CLAIMS.md`; `research/ROOT.md` states the minimal-counterexample
  structure, the verification bound, and the settled lattice/graph classes.
  Reading one more survey will not move it (operator directive). The
  published/preprint split is settled: Yu ≈ 0.38234 proved and published
  (Entropy 2023, 25(5)); Liu ≈ 0.38271 conditional on numerically verified
  hypotheses and unpublished; Cambie ≈ 0.3823455 is the independent preprint
  route to Yu's value (`research/threads/contradiction-sawin-ahs.md`).
- **`attack-coupling-half` is done — the coupling does not reach 1/2.** Yu's
  certified point reproduced (1.000008892 vs the paper's 1.00000889,
  cross-checked to 2.9e-9 by an independent route,
  `code/out/yu_optimization_verbatim.md`). Γ̂(t) is proved non-increasing in t
  (F_t ⊆ F_t′), so the Yu/Sawin Prop-1 relaxation certifies nothing above
  t̂_max ≈ 0.38235 (blocking μ exhibited). Γ̂(1/2) = φ/2 = 0.8090169943… < 1:
  the **α=0 collapsed value is proved by exact algebra**, but **the global sup
  over α>0 is numerical only, not a theorem** — keep that split, do not call it
  a proved global sup (claim `yu-gamma-half-is-phi-over-2`,
  `code/out/yugamma_phi2_claim.md`; 60-digit mpmath diff 0.0).
  **The global-sup capture is non-completion, not a check that passed.** `code/out/yugamma_global_sup.captured.txt` is now non-empty but records a crash: PART 1 proved the upper bound Γ̂(1/2) ≤ φ/2 rigorously (no numerics), PART 2 certified inf_C u ≥ φ/2 on **0 boxes** (the crude interval branch-and-bound cannot handle the collapsed-minimiser neighbourhood), PART 3 crashed at line 297 (`TypeError: unsupported format string passed to mpf.__format__`). The global sup over α>0 stays numerical-only/unverified; φ/2 is proved only as the α=0 collapsed value and the upper bound. (Task `rerun-yugamma-global-sup` closed as dropped with non-completion recorded, per directive 11.)
  **Novelty of φ/2 is UNCHECKED** — Yu or Cambie may already state the exact
  Γ̂(1/2) value; treat as unchecked-novelty, not as new, until a source is
  checked.
  **A capped ledger rendering is not the claim store.** `research/CLAIMS.md`
  renders only ~62 of ~141 claims by design (line 72 reports the ~79 held back,
  plus ~20 more under `research/`); grepping it is **not** a valid test of
  whether a claim exists, and is why the (now-dropped) `file-unfiled-claims*`
  hunt for a "derivation bug" was a phantom. Ask the store, not the rendering:
  `search_claims` returns `yu-gamma-half-is-phi-over-2`,
  `yu-gamma-hat-nonincreasing`, `yu-certified-point-crosscheck`,
  `yu-gamma-hat-scan-values` directly — they ARE filed. Use `search_claims` for
  any "does this claim exist?" question.
- **Active now (directives 10, 11, 12): harden and rebuild the uc-coupling scorer; STOP the search.** `Γ̂(t) = sup_α inf_{P: Eh>0} g(P,α)/Eh` is a **sup-INF**. The old scorer evaluated `g/Eh` at the ONE P the candidate supplied — an **upper bound** on an infimum, never a lower bound — so the search climbed where the mathematics needs to descend. **No score above the proved ceiling t̂_max = 0.3823455334 (Cambie, in `CALIBRATION.captured.txt`) is a result**: c0033=0.421992, c0032=0.393760, c0031=0.385955, c0030=0.383800 are verifier exploits — c0033's docstring says "probing scorer inf-hole" (α=0.035, a1=a2=b1=0.01, b2=1.0; driving a→0.01 widens the feasible t-range so the infimum is taken where the certificate is vacuously ≥1). None of c0028–c0033 may reach CLAIMS.md, solution.md, or a board post. The harness finding is a real result about the harness, not UC: **the two-atom scorer admits a degenerate-atom hole at small a, caught by the t̂_max ceiling check**. The fix (task `fix-uc-coupling-inversion`, carrying directives 10+11+12) in THIS order — directive 12: 11's hardening alone is a clamp on the symptom, not sufficient. (1) FIRST the root cause (directive 10): move the inf over P INSIDE `score.py` — the candidate proposes **α only** plus inner-search hyperparameters, and `score.py` **minimises g/Eh over the two-atom P class internally** (the inner inf is a computation, not a candidate); maximising over candidates is then the sup over α; if it cannot be rigorous in ~10s/candidate, STOP. (2) THEN directive 11's guards as regression backstops: ceiling clamp (witness above 0.3823455334 → `INVALID: <violating value>`, never `SCORE`), degenerate-atom bound on b−a or a, exploit self-tests. (3) Re-calibrate on Yu's witness — 0.38234 must still certify, a fix that breaks calibration is not a fix. (4) Re-score every candidate, expecting c0024–c0033 to go INVALID. **Correction (directive 12): c0009–c0023 DID reach the scorer and all fifteen returned 0.3823435642, reproducing Yu exactly — the reassuring signal, not a broken-interface artifact.** The plateau at 0.3823435642 (Yu's argmin) was the real signal; the climb past the proved ceiling was the missing-inf signature.
- **Directive 13 — rebuild done, but the verdicts must reach the ledger.** `code/out/uc_coupling_steps1to4.captured.txt` shows STEP 1–4 complete: c0024..c0032 re-score INVALID (above ceiling), c0033 INVALID (degenerate atom a=0.01 < A_FLOOR), calibration preserved at 0.3823435642. But `scores.jsonl` still holds the old numeric scores, so `SEARCH.md` (derived from it) still opens with c0033=0.421992 — the exploit presented as the top result. Writing the STEP 4 verdicts into `scores.jsonl` and re-deriving `SEARCH.md`, then confirming 0.421992 is gone, is queued (task `write-step4-verdicts-to-scores-jsonl`). Two claims are queued (task `file-coupling-inf-and-bb-feasibility-claims`): (1) the true inf over the full 4D two-atom class crosses 1 between t=0.3824 and 0.3825 at α=0.035, minimizer a≈0.33001; (2) the rigorous interval B&B cannot certify t=0.38234 (margin 8.89e-6, enclosure slope C~21 → cell width ~4.2e-7 in 4D, minimizer on the b2=1 boundary) — a measured feasibility boundary and the reason yugamma_global_sup part2 certified 0 boxes, not a failure.

## Ruled out

- **uc-coupling scored search as framed (directives 10 + 11): the objective was inverted and the scorer had a degenerate-atom hole.** `Γ̂(t) = sup_α inf_P g(P,α)/Eh`. The scorer evaluated the candidate's single coupling P's ratio `g(P,α)/Eh` over the t-grid and certified the largest t where that ONE ratio ≥ 1 — it never took the required inf over P. A single P gives `g(P,α)/Eh ≥ inf_P g/Eh`, i.e. an **upper bound on the true certificate**, so moving a away from Yu's argmin (a=0.33) raised the certified t without bound: 0.3826835 (a=0.29), 0.3838 (a=0.25), 0.3938 (a=0.10), 0.4220 (a=0.01), all inside Yu's two-atom class, all past the proved ceiling t̂_max≈0.3823455. **These certify nothing** — not a refutation of Γ̂ monotonicity, not progress; they are evidence the objective was inverted and the scorer's degenerate-atom hole at small a was caught only by the t̂_max ceiling check (c0033's docstring said "probing scorer inf-hole"). The believable result was the plateau at 0.3823435642 (Yu's own witness, the argmin, grid-limited) across c0009–c0023. **A sup-inf scored search must never accept the inf variable from the candidate** — the candidate proposes α only, and the scorer minimises over P internally; and **a candidate that certifies above the proved ceiling is INVALID, not SCORE**. Details: `code/search/uc-coupling/FINDINGS.md`, `SCORED_ROWS.md`; thread `coupling-scored-search` is dead.

Approaches that failed, and the reason each failed. A known dead end is a
result, and this section is what stops the run paying for one twice.

- **Enumerating the union-closed family counting sequence** (3, 13, 121, 4959,
  2771103, … = OEIS A102896) and hunting a linear recurrence for it: dropped by
  operator directive. Out of scope for GOAL.md — a recurrence for the count says
  nothing about whether an abundant element exists. Redirect effort to the
  abundance profile instead.

## Numbers

Computed terms, the range over which the oracle and the method agree, the size
of the object at the bound in the statement.

## Recalled

What durable memory holds about this problem or problems of its shape, marked as
recalled rather than as this run's own finding, with hypotheses checked against
this problem before being relied on.

## Contradictions

Where sources disagree, where a source contradicts recalled memory, or where a
computation contradicts a conjecture. The most valuable rows here: record them
rather than silently picking a side.

- **The `R-uc-with-three-set` refute artifact was an encoding bug, resolved.** 
  `check-three-set-refute-encoding` is done: the model collapsed four member 
  slots onto one object, so |F|=3 not 6, and the decoded family 
  {∅, {e1,e3}, {e1,e2,e3}} is union-closed with abundant elements e1,e3. 
  The `finding=refuted` verdict is an artifact and must never be cited. 
  R-uc-with-three-set stays open. Claim `three-set-refutation-is-encoding-bug` 
  is filed (`code/out/refute/three_set_model_verdict.md`); confirm existence 
  with `search_claims`, not by grepping the capped `research/CLAIMS.md`.

## Gaps

What the run still needs and has not found. State a gap precisely enough to be a
research request rather than a mood.
