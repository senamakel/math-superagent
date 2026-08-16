# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Unblock attack-coupling-half. The blocker is fixable with tools you already have: research/sources/*.full.md for Yu (2212.00658), Liu (2306.08824) and Sawin (2211.11504) are ~5KB arXiv abstract pages, not full texts. Fetch the actual papers — try the ar5iv/arXiv HTML full text (arxiv.org/abs/NNNN.NNNNN -> arxiv.org/pdf/NNNN.NNNNN or ar5iv.labs.arxiv.org/html/NNNN.NNNNN) and re-download over the abstract-only stubs. You need Yu's finite-dimensional conditionally-iid coupling optimization in its stated form before implementing it; do not reconstruct it from the abstract and do not guess the objective. If the full text genuinely cannot be retrieved after real attempts, close the task with that as the recorded reason rather than leaving it blocked.

Second: stop putting the counting sequence of union-closed families (3, 13, 121, 4959, 2771103, ...) through analyze_sequence and find_linear_recurrence. Three identical calls have now failed schema validation on a float term, and the quantity itself is out of scope for GOAL.md — it is an enumeration curiosity (OEIS A102896), not a route to a bound on abundance. A recurrence for it, if one existed, would say nothing about whether an abundant element exists. Spend that effort on the abundance profile instead.

I unblocked `attack-coupling-half` by fetching the three actual full texts (Yu 2212.00658, Liu 2306.08824, Sawin 2211.11504) from ar5iv, which replaces the ~5KB abstract-page stubs the task had been blocked on. I dropped the A102896 counting-sequence task with the directive as the recorded reason, opened `abundance-profile-analysis` in its place, and recorded both under Ruled out in CONTEXT.md plus a new `research/threads/abundance-profile.md` so the redirected effort lands on the abundance profile rather than being re-proposed.

## 2 — from steer

attack-coupling-half has been the top open task for ~20 minutes and no code exists for it — code/out/ has 13 scripts and not one implements Yu's optimization. Meanwhile the librarian and scholar are still downloading and summarising further sources (AHS-EJC-2024, Lu-Raz-Reimer, the polymath page). The library is finished: 62 claims, the record is pinned at Yu 0.38234 published / Liu 0.38271 conditional, and reading one more survey will not move it. Stop adding sources.

Do this now, in this order:
1. Open research/sources/yu-dimension-free-bounds-2023.full.md, find Yu's finite-dimensional optimization as stated, and write it down verbatim in a note before writing any code — the objective, the constraint set, and the dimension of the auxiliary variable.
2. Implement it. Reproduce 0.38234 as a correctness check. If your implementation does not reproduce it, the implementation is wrong and that is the finding to fix, not to route around.
3. Only then push the same optimization toward c=1/2 and report which of the two happens: it certifies H(A∨B)>H(A) at density 1/2, or it exhibits the extremal mu that blocks it. The second outcome is GOAL.md result class 3 and is the realistic one — treat exhibiting the blocking mu as success, not as failure.

If after a genuine attempt Yu's formulation cannot be implemented faithfully, close the task with that as the recorded reason and say precisely which step of the paper you could not turn into code. Do not leave it open and unworked.

Done. The directive's three ordered steps are now the body of `attack-coupling-half`, which is the first open task in `TASKS.md`: extract Yu's optimization verbatim from the full text before any code, reproduce 0.38234 as the correctness gate, then push toward c=1/2 with the blocking-μ outcome recorded as success. I recorded `stop-adding-sources` as done (62 claims, record pinned at Yu 0.38234 / Liu 0.38271), opened `research/threads/coupling-half.md` for the direction, and added both facts to CONTEXT.md's Established section — no research request was filed since the directive names a file already on disk, not a gap.

## 3 — from steer

Correctness check on an artifact already on disk. code/out/refute/code_refute_uc_with_three_set.p.json records finding=refuted, status=CounterSatisfiable, against the rung R-uc-with-three-set ('every union-closed family containing a 3-element set has an abundant element'). That verdict is almost certainly an encoding bug, not a refutation, and it must not be allowed to reach a claim.

The reason: the counter-model has a 6-element domain. A genuine union-closed counterexample on 6 ground-set elements would refute Frankl's conjecture outright for n=6, which contradicts bosnjak-markovic-11 and verified-n12-comp — both already in CLAIMS.md, and UC is machine-verified to n=12. So either you have disproved a verified theorem with a model finder, or the TPTP encoding in code/refute/uc_with_three_set.p is missing an axiom. Assume the latter.

Do this: re-read the encoding and check specifically that it asserts (a) closure under union for ALL pairs of members, (b) that the abundant element ranges over the whole ground set and not just {x,y,z}, and (c) the counting/cardinality semantics of 'at least |F|/2' — a first-order encoding of a counting statement is where this usually breaks. Then take the produced counter-model and run it through the canonical oracle code/lib/uc.py: decide_union_closed on it, and abundance. If the oracle says it is union-closed and has no abundant element, you have something extraordinary and it must be reported as such with the family written out explicitly. If the oracle rejects it — which is what I expect — the encoding is wrong: record that as the finding, and either fix the encoding or delete the artifact so it cannot be mistaken for a result later. WEAKENED.md still lists the rung as open, which is correct; keep it that way unless the oracle says otherwise.

Queued `check-three-set-refute-encoding` as the directive's work (re-read the TPTP encoding for the three checks, decode the counter-model, run it through `code/lib/uc.py`, then fix the encoding or delete the artifact), opened `research/threads/three-set-refute-encoding.md` to carry the direction, and put a Contradictions warning in CONTEXT so the `CounterSatisfiable` verdict cannot be cited as a claim. The rung `R-uc-with-three-set` stays open in WEAKENED.md, per the directive. The task landed third in the queue behind the two existing open tasks; the thread's `next` field restates the directive verbatim so the check runs as specified, and the JSON model already shows the suspected bug (six slots collapsed to three distinct sets, making the counting axioms vacuous) for the executor to confirm.

## 4 — from steer

Two things, both about not losing work you have already done.

FIRST — yugamma_highprec.py just reported that the collapsed Gamma at t=1/2 equals phi/2 = 0.80901699437494742410229341718281905886 to 60 digits, diff exactly 0.0. You were right to suspect a coincidence, but 60 digits is not a coincidence. Try to prove it symbolically: at t=1/2 the binary entropies should collapse (h(1/2)=1) and the ratio should reduce to an algebraic expression in Q(sqrt5). If it proves, you have a sharp quantitative barrier statement and it is the best result this run has produced: the Yu/Sawin coupling optimization does not merely fail to reach 1/2, its certificate value AT 1/2 is phi/2 = 0.809, and certification requires >= 1. Pair that with the monotonicity of Gamma-hat you already proved and you have the barrier with a number on it, not just a direction. If it does not prove symbolically, say so and report it as high-precision numerical with the digit count.

SECOND — file what you have. CLAIMS.md has been stuck at 62 for two ticks while the substantive results piled up on disk uncited: (a) the faithful reproduction of Yu's certified point, 1.000008892 vs the paper's 1.00000889, cross-checked to 2.9e-9 by an independent route; (b) the proof that Gamma-hat(t) is non-increasing in t via F_t subset F_t'; (c) the Gamma-hat scan over t=0.30..0.38 showing 1.13443 down to 1.00521; (d) Gamma-hat(1/2)=phi/2; (e) the three-set oracle sweep (n=3: 90 UC families with a 3-set, 0 lacking an abundant element; n=4: 4838 and 0) that established the refute artifact was an encoding bug. Each needs a claim block in the note beside its output, with its status and its ceiling stated. A result that is not in CLAIMS.md will not be cited by the write-up, which means it did not happen.

Also close attack-coupling-half and check-three-set-refute-encoding. Both are done — Yu reproduced and pushed, artifact tested and deleted — and they are still sitting in Do next, which will make a later role redo them.

The workspace now reflects the directive accurately. Everything changed is in place; the external-novelty check could not be queued because `request_research` answers from the run's own library, which already holds the proof — I've recorded that gap in the thread instead of silently dropping it.

Summary of what I changed and why:

- **Closed the two done tasks** (`attack-coupling-half`, `check-three-set-refute-encoding`) with reasons naming the evidence, so a later role won't redo work the directive says is finished.
- **Rewrote the task order**: `file-unfiled-claims` is now first (the directive's SECOND point), with `abundance-profile-analysis` blocked behind it. During the work, two of the five "unfiled" results — Γ̂(1/2)=φ/2 and the three-set sweep — turned out to be *already filed* as claims (`yu-gamma-half-is-phi-over-2`, `three-set-refutation-is-encoding-bug`), and the symbolic proof the directive's FIRST point asks for is *already on disk* in `code/out/yugamma_phi2_claim.md`; I did not re-queue either.
- **Opened a thread** (`yugamma-half-collapse`) capturing the one part still genuinely open: the global sup over α>0 is only numerically corroborated, not proved, so the "certificate value AT 1/2 is φ/2" barrier must not be overclaimed as a theorem. Marked `coupling-half` and `three-set-refute-encoding` dead, and amended CONTEXT.md to say Γ̂(1/2)=φ/2 is proved (not "60-digit numerical") and that the live task is filing the three remaining claims.

The only thing I could not do was the external-novelty check for the φ/2 barrier: `request_research` declined it twice because the run's own claim store already carries the result, so I recorded the unchecked novelty in the thread rather than let it be silently assumed.

## 5 — from steer

Your directive-4 report says Γ̂(1/2)=φ/2 and the three-set sweep 'turned out to be already filed as claims (yu-gamma-half-is-phi-over-2, three-set-refutation-is-encoding-bug)', and on that basis you did not re-queue them. That belief is wrong, and it caused you to skip the work.

Check it yourself: grep research/CLAIMS.md for those two ids and they are not there. Of the eight claim ids that now have blocks in code/out/*.md — kfold-barrier-maximised-at-k2, iid-barrier-exact, nagel-profile-equality, yu-certified-point-crosscheck, yu-gamma-hat-nonincreasing, yu-gamma-hat-scan-values, psi-alpha-tieback, yu-gamma-half-is-phi-over-2 — only kfold-barrier-maximised-at-k2 appears in CLAIMS.md. A  block sitting in a note is NOT a filed claim; the ledger is derived, and until the derivation runs and the row appears in CLAIMS.md the result is invisible to search_claims and to every role that reads the index. Writing the block and confirming the row exist are two different steps and you did only the first.

So: trigger the re-derivation and then VERIFY by reading research/CLAIMS.md back and confirming each of the eight ids has a row. Report the count before and after. If a block fails to derive, the block is malformed — print the offending block and the reason rather than assuming it landed.

Two things you got right and should keep: the refusal to call Γ̂(1/2)=φ/2 a proved global sup when only the α=0 collapse is symbolic and the sup over α>0 is numerical — keep that distinction in the claim's status line, do not let it drift to 'proved' in CONTEXT.md; and reporting that request_research declined the external-novelty check twice instead of assuming novelty. The novelty question is still open and matters: φ/2 as the exact certificate value at t=1/2 is the kind of thing Yu or Cambie may already state. Record it as unchecked-novelty, not as new.



## 6 — from steer

Open a scored program search on the coupling constant. code/search has never been used by any run on this box, and attack-coupling-half is exactly its shape: a constant nobody derives in closed form, improved by constructing a better witness and scoring it.

1. Have tool_builder write code/search/uc-coupling/PROBLEM.md and score.py. The searcher must NOT write the scorer — a scored search learns to exploit its verifier first, and the exploit here is obvious: claim a large c with a witness violating a constraint nobody rechecked.

The candidate module exposes the auxiliary object Yu's finite-dimensional optimization ranges over. The scorer independently VERIFIES every constraint, then prints 'SCORE: c' for the constant the witness certifies. A violated constraint prints 'INVALID: <constraint, violating value>'. Exact rationals where possible; where reals are needed, interval arithmetic reporting the certified LOWER endpoint, never a midpoint. A floating-point c is not a certificate.

2. Calibrate first: the scorer must reproduce 0.38234 on Yu's own witness. If it does not, the scorer is wrong and that is the finding — fix it before running any candidate. This is your one cheap chance to catch a verifier exploit, and it is the check attack-coupling-half already asks for.

3. Then spawn searcher against slug uc-coupling. Fifty candidates is a search, three is not. Anything above 0.38234 improves the published frontier and must be re-verified independently before you report it; 0.5 would prove Frankl and should be disbelieved until it survives that.

Keep the scorer under ten seconds per candidate and bounded in memory — this container has an 8 GiB cap and a scorer allocating without limit kills the run, not the candidate.

I want SEARCH.md filling with scored rows, 0.38234 reproduced, and where candidates plateau plus which constraint binds there. That constraint is the finding. Say plainly whether you believe the top score.

I've read the workspace and reconciled the directive against what the run has already established. The key tension: the run has **proved** Γ̂(t) is non-increasing in `t`, so within Yu's two-atom class the plateau is `t̂_max ≈ 0.38235` and the binding constraint is `t` itself — meaning the search's expected finding is the plateau plus the empirical map of the 5-parameter space, and any score above 0.38235 *inside* that class would falsify that proof (so it must trigger re-checking the proof and the scorer, not belief).

What I changed, and why the directive required it:

1. **Recorded task `open-uc-coupling-scored-search`** in the tasks ledger, carrying the directive's exact steps in order: `tool_builder` writes `code/search/uc-coupling/PROBLEM.md` + `score.py` (searcher must not write the scorer), the scorer independently verifies every constraint and prints `SCORE: c` / `INVALID: <constraint, value>` with exact rationals or interval-arithmetic certified lower endpoints, calibrate on Yu's 0.38234 witness first (hand-verified 1.000008892), then ≥50 candidates, then fill `SEARCH.md`. I embedded the reconciliation so the search does not chase a class already proved capped.
2. **Opened thread `coupling-scored-search`** and **added one "Active now" line to CONTEXT.md**, so every role sees the directive, the calibration target, and the plateau/binding-constraint expectation.
3. **Filed no `request_research`** — the gap the directive implies (what richer coupling class could beat 0.38234) is already answered by the library's `liu-conditionally-iid` (0.38271, conditional) and `liu-9dim-reduction` claims, so queuing a request would duplicate what the library holds.

One note for the operator: `request_research` refused to queue because the claim store already carries the answer, which is the correct outcome — the genuine open frontier is Liu's conditionally-iid class, not re-searching Yu's capped two-atom class.

## 7 — from steer

Correction — directive 5 was based on my error, and you should stop acting on it.

I claimed your claim blocks had not derived into CLAIMS.md, based on grepping that file for the eight ids and finding one. That was a bad test. CLAIMS.md line 72 says '79 further claims not shown', and the trailing note says 20 more are in research/ — the table is capped by design and reports what it left out, exactly as the ledger contract requires. So the file I grepped renders 62 of roughly 141 claims, and the ids I could not find are simply past the display cap. Confirmed independently: THREADS.md cites yu-gamma-half-is-phi-over-2 and yu-gamma-hat-nonincreasing as live claim ids in the coupling-scored-search and yugamma-half-collapse threads, which it could only do if they are in the store.

Your directive-4 report was therefore right and my correction of it was wrong: those results ARE filed. Drop any task I caused you to open about triggering re-derivation, fixing malformed blocks, or verifying the eight ids appear in CLAIMS.md — there is no derivation bug to find, and hunting one costs you the rest of this run for nothing. If you already opened such a task, close it with this directive as the reason.

Nothing else in directive 5 changes: keep the Gamma-hat(1/2)=phi/2 status honest (alpha=0 collapse proved by exact algebra; that it is the global sup over alpha only numerically corroborated), and keep the external novelty of the phi/2 value recorded as unchecked rather than assumed.

The lesson worth keeping in CONTEXT.md is about the tool, not the mathematics: a capped ledger rendering is not the claim store, and grep over CLAIMS.md cannot decide whether a claim exists. Use search_claims for that question.

Three changes, all directly from Directive 7:

1. **Closed `file-unfiled-claims-v2`** — the task was hunting for a derivation bug that does not exist. `search_claims` confirms `yu-gamma-half-is-phi-over-2`, `yu-gamma-hat-nonincreasing`, `yu-certified-point-crosscheck`, and `yu-gamma-hat-scan-values` are all in the claim store; they were never missing, they were just past the display cap of `CLAIMS.md`. The operator confirms this directive was based on their own error.

2. **Unblocked `abundance-profile-analysis`** — it was held behind `file-unfiled-claims-v2` so it could cite the Yu claims. That blocker is gone now; the claims are confirmed filed and the profile analysis already cites them in its done status.

3. **Replaced the "Block ≠ filed claim" paragraph in CONTEXT.md** with the lesson the operator asked for: a capped ledger rendering is not the claim store, and `grep` on `CLAIMS.md` cannot decide whether a claim exists — use `search_claims` for that. Also fixed the parallel note in the Contradictions section that referenced the phantom `file-unfiled-claims-v2` task.

The only open task remains `open-uc-coupling-scored-search` (from directive 6), which directive 7 explicitly leaves unchanged.
