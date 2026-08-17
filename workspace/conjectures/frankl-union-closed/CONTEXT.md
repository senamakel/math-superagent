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
- **Constraint delimitation executed (`constraint_delim.py`, full run, capture `code/out/constraint_delim.captured.txt`).** The held minimal-counterexample constraints (A no-degree-1, C = KPT n≥2k+1, Karpas |F|<2^{n−1}, Roberts–Simpson |F|≥51) delimit the boundary of the abundance-profile front: no (2,3,7)-construction (f=2, k=3, n=7) found across 190,415 k=3 families — min f=3 matching the n≤6 k=3 floor, while KPT Thm 5(2) only gives f≥2; P_3^8 attains f=2 at n=8. The (2,3,7) existence question stays open (closure-based probe, not exhaustive). Claims `no-two-abundant-k3-n7-found` and `kpt-p38-rebuilt-verified` filed at `code/out/constraint_delim_claims.md`; **the Lean formalisation task was deferred with that reason recorded on the same note.**

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it.

- **Directive 21 (statement bug) is RESTATED on disk — the restate is done, do not redo it.** The two sorry-goals were originally FALSE (they demanded the *entropy* `hsum p` be negative). `gilmer_refuted_boundary` is now **PROVEN** (no sorry: `refine ⟨3/10, …⟩` to `ellis_lhs_negative` + `boundary_distribution`). `gap_perturbed_strict` has been restated around the correct object — the difference `LHS_of p < 0` (union-pushforward cross-entropy minus entropy), not `hsum` — and is still a `sorry` needing a continuity lemma for `LHS_of` as a function of the distribution (finite sum of `log(1/·)` terms on the positive simplex). `gap_union_weights` and `gap_entropy_rewrite` remain correctly-stated mechanical sorries. A prover can now be assigned to `gap_perturbed_strict` / `gap_union_weights` / `gap_entropy_rewrite`; `gilmer_refuted_boundary` is discharged (`code/lean/ellis_gilmer_conjecture_refuted.lean`). The 8 kernel-clean core declarations are untouched.
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
- **Directive 13 cleanup is COMPLETE — do not redo it.** Both queued items are done on disk. (1) The two capture findings ARE filed: `search_claims` returns `coupling-true-inf-crossing-4d`/`-0-3824` (the true inf over the 4D two-atom class crosses 1 between t=0.3824 and 0.3825 at α=0.035, minimizer a≈0.3300622, verified-numerically NOT proved) and `coupling-interval-bb-infeasible-10s` (rigorous interval B&B cannot certify t=0.38234: margin 8.89e-6, enclosure slope C~21 → cell width ~4.2e-7 in 4D, minimizer on b2=1 boundary — a measured feasibility boundary, the reason yugamma_global_sup part2 certified 0 boxes, not a theorem failure). (2) `scores.jsonl` now carries the STEP 4 verdicts (c0024..c0032 INVALID above ceiling, c0033 INVALID degenerate-atom, Yu block SCORE 0.3823435642) and `SEARCH.md` is re-derived with **0.421992 gone** — its top row is the Yu block at 0.3823435642. Tasks `write-step4-verdicts-to-scores-jsonl` and `file-coupling-inf-and-bb-feasibility-claims` are both recorded open but resolved on disk; they should be closed, not re-run. Do not re-file the claims or re-verify the exploit is gone.
- **The g(n,m) envelope is PROVED for all n and is prose-anchored (directive 17).** `g(n,m) = max(1, m−2^{n−1})` (min over UC F, |F|=m, of the rarest element's count) — lower bound elementary (sets avoiding x are subsets of [n]∖{x}, no union-closure), tightness proved constructively. **The proof text is the anchor** (`code/out/gnm_envelope_finding.md §Proof`), not the program: `gnm_envelope_verify.py` verifies instances at n in 1..6 / all m / exhaustive n≤4; it is verification, not the argument. The one step the general claim rests on, **the size lemma** — every size s in 0..2^N is an upset of 2^[N] — is now **written by induction** (complement of an upset is a downset; a maximal element of the non-empty complementary downset moves in and the result is still an upset). It is **not a proof of Frankl**: g constrains the minimum (rare) density, Frankl asks for an abundant (maximum) element, and this is kept stated plainly. New open thread `gnm-envelope-lean` (directive 17 suggestion): formalise this in Lean 4 (Finset over Fin n, upward-closed predicate, size lemma by induction, two explicit constructions) — far better target than the entropy work, no real analysis/transcendentals/interval arithmetic; task `formalise-gnm-envelope-in-lean`.

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

Exact/computed, with the oracle verified by a second route (A121921 catalogue;
independent hand enumeration; independent no-lib brute force). `code/lib/uc.py`
is the one canonical oracle; guards all pass (`code/out/uc_oracle_check.captured.txt`).

- **Verified range**: UC holds by machine for all families on ground set `n ≤ 12`
  (Vučković–Živković 2017, computer-assisted; any counterexample has `n ≥ 13`)
  and for `|F| ≤ 50`; by Karpas, UC holds for `|F| ≥ 2^{n−1}`. A minimal
  counterexample therefore has `n ≥ 13`, `|F| ≥ 4·13−1 = 51`, and `|F| < 2^{n−1}`
  (`research/ROOT.md`).
- **Oracle exhaustive scan** (`lib.uc`, n ≤ 4): UC family counts 3, 13, 121,
  4959 (matches OEIS A121921). **WORST(n)** = min over UC families of min
  element-frequency = 1/2, 1/3, 1/5, 1/9 = `1/(2^{n−1}+1)`, achieved uniquely up
  to isomorphism by the near-k-cube `2^[n−1] ∪ {[n]}` (denominators = A000051;
  general statement is the sourced Das–Wu Nagel sharpness, claim
  `daswu-nagel`/`nagel-profile-equality` — **not** proved here).
- **Barrier constants**: iid-OR entropy certifies nothing above
  `(3−√5)/2 ≈ 0.381966` (claim `iid-barrier-exact`, proved). Record constants:
  **published ≈ 0.38234 (Yu, Entropy 2023, proved)**, Cambie ≈ 0.3823455,
  Liu ≈ 0.38271 (unpublished/conditional). **Proved ceiling for the Yu/Sawin
  two-atom coupling: t̂_max = 0.3823455334** (Γ̂ non-increasing, claim
  `yu-gamma-hat-nonincreasing`); Γ̂(1/2) = φ/2 = 0.80901699… exactly at the
  α=0 collapse (claim `yu-gamma-half-is-phi-over-2`, proved), global-sup over
  α>0 numerical-only (open).
- **Yu's witness reproduced**: Γ̂(0.38234) = 1.0000088929 (paper 1.00000889),
  minimizer a ≈ 0.3300622, b2=1 (`yu_optimization_verbatim.md`). Scorer
  plateau at 0.3823435642 is grid-limited, the believable testimony. **The true
  inf over the 4D two-atom class crosses 1 between t=0.3824 and 0.3825**
  (`coupling-true-inf-crossing-4d`, verified-numerically); **rigorous interval
  B&B cannot certify it** — margin only 8.89e-6, slope C~21 forces cell width
  ~4.2e-7 in 4D (`coupling-interval-bb-infeasible-10s`, measured).
- **Constraint delimitation** (`code/out/constraint_delim.captured.txt`):
  over all 2546 empty-free UC families at n≤4, constraints (A) no-degree-1
  and (C) KPT n≥2k+1 hold simultaneously in 1848 (72.6%), f=0 never occurs,
  minimal excess d=max(2c−m)=1 (70 families). n=5 class-exhaustive k≥3:
  min f = k (KPT Thm 5(1) tight). n=6 k=3: min f = 3 over 289,469
  constructions. KPT P_3^8 rebuilt, oracle-verified (|F|=71, counts 67/35,
  exactly 2 strict-abundant). **n=7 k=3 boundary: NO (2,3,7)-construction
  found over 190,415 families** — min f=3 vs KPT Thm 5(2) bound f≥2,
  matching the paper's Thm 6(2) inequality failing at n=7 (holds at n=8).
  Existence of a (2,3,7)-construction stays OPEN; the probe is closure-based,
  not exhaustive (`no-two-abundant-k3-n7-found`,
  `kpt-p38-rebuilt-verified`).
- **Odd-filter min-max, settled: value correct, uniqueness FALSE.** Among
  NON-Boolean union-closed families, min over F of max density = `2^{n-1}/(2^n-1)`
  — but the odd filter `2^[n]\{∅}` is NOT the unique minimizer. For every n≥2
  there are n+1 minimizers: the odd filter plus the n power-set-minus-singleton
  families `2^[n]\{{x}}` (each |F|=2^n−1, same bound). The n+1-minimizer
  refutation of uniqueness is unconditional for every n≥2; exhaustive
  enumeration ceiling is n≤4 (claim `odd-filter-max-density-extremal-nonboolean`,
  `code/out/odd_filter_claim.md`, `odd_filter_minmax.captured.txt`). Not
  counterexample-relevant (those families sit far above 1/2); it is a stale-
  extremal cleanup on the abundance-profile front.

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

State a gap precisely enough to be a research request rather than a mood.

- **Prove (or refute) that φ/2 is the GLOBAL sup of Γ̂(1/2)** — i.e. no α>0 or
  4-param two-atom coupling gives g/Eh > φ/2 at t=1/2. The α=0 collapsed value
  is proved (`yu-gamma-half-is-phi-over-2`); the global-sup is numeric
  corroboration only. `yugamma-half-collapse` is open; its part-2 interval B&B
  certified 0 boxes (`coupling-interval-bb-infeasible-10s`), so a rigorous proof
  needs an exact/analytic inf or a tailored interval bound, not generic 4D B&B.
- **Novelty of Γ̂(1/2) = φ/2 is UNCHECKED**: whether Yu/Cambie already state
  the exact value is unknown; treat as unchecked-novelty, not new, until a
  source is checked (could not be queued externally — the request tool answers
  only from this run's claim store).
- **`abundance-profile` open**: whether the coupling-class inequality constrains
  a minimal counterexample's profile (max density < 1/2) enough to force an
  abundant element is unsettled; the near-k-cube (WORST family, min-density
  `1/(2^{n−1}+1)`) must be tested against any proposed structural claim.
- **The published-record request `exact-current-published-c8b8` is SETTLED — do
  not re-run freshness searches.** Operator directive 15: the librarian ran
  record-freshness searches three times (ticks 2, 4, 6) on "improved constant
  2024/2025" and Liu publication status; the frontier is pinned and reproduced
  and nothing returned changes a number. It stands as CONTEXT records: Yu
  0.38234 proved and published (Entropy 2023, 25(5)); Cambie 0.3823455 the
  independent preprint route to Yu's value; Liu 0.38271 conditional on
  numerically verified hypotheses and unpublished. Re-run a variant search
  only if a result changes one of these numbers; otherwise spend the calls on
  the abundance-profile front (task `abundance-profile-front-continue`), the
  other open job in GOAL.md.
- **`R-uc-with-three-set` stays open** (the refuted verdict was an encoding bug,
  resolved; see Contradictions).
- **Three open ledger rows are settled on disk — close them, do not re-run:**
  `verify-odd-filter-minmax` (claim `odd-filter-max-density-extremal-nonboolean`
  + capture filed), `restate-false-lean-goals-ellis-gilmer` (`gilmer_refuted_boundary`
  proven, `gap_perturbed_strict` restated — see Established/Directive 21), and
  the coupling pair `write-step4-verdicts-to-scores-jsonl` /
  `file-coupling-inf-and-bb-feasibility-claims` (see Established/Directive 13).
  The genuinely open work is `abundance-profile-front-continue` and the three
  `sorry` gaps in the Ellis Lean file.
