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
- **Active now (operator directive 6): scored program search on the coupling constant.** `code/search/uc-coupling/` is being opened: `tool_builder` writes `PROBLEM.md` + `score.py` and the searcher must **not** write the scorer; the scorer independently verifies every constraint and prints `SCORE: c` or `INVALID: <constraint, violating value>`, exact rationals + interval-arithmetic certified lower endpoints. Calibrate first on Yu's 0.38234 witness (hand-checked 1.000008892, `code/out/yu_optimization_verbatim.md`). From the already-proved Γ̂ non-increase, the two-atom class plateaus at t̂_max ≈ 0.38235 with `t` the binding constraint; a >0.38235 score *inside* that class falsifies that proof (re-check proof + scorer), and 0.5 means exploit/bug until independently re-verified. Improving the 0.38234 frontier needs a richer coupling class than Prop-1's two-atom reduction.

## Ruled out

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
