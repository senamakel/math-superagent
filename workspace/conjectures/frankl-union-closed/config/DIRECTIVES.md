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

## 8 — from steer

code/out/yugamma_global_sup.captured.txt is zero bytes. GOAL.md's capture rule says an empty capture is a failed run, not a missing one, and this one matters more than most: yugamma_global_sup.py is the script attacking the single open gap in your best result — whether Gamma-hat(1/2)=phi/2 is the global sup over alpha, which is currently the difference between a proved barrier and a numerically corroborated one. An empty file beside a claim that says 'sup only corroborated' will later read as though the check was run and returned nothing.

Re-run it, and either produce the capture with its first three lines stating what was run, which oracle function, and the exact alpha range and precision, or delete the empty file and record that the computation did not complete. Do not leave a zero-byte capture on disk.

Separately, on the scored search: code/search/uc-coupling has only _bench.py — PROBLEM.md and score.py are not written yet, and directive 6 is explicit that the scorer must exist and must calibrate to 0.38234 on Yu's own witness BEFORE any candidate runs. I can see you building the scorer with mpmath interval arithmetic, which is right. Hold the searcher until the calibration passes. If the scorer cannot reproduce 0.38234 on Yu's witness, that is the finding and it blocks the search — do not proceed to candidates with an uncalibrated verifier, because every score after that is unfalsifiable.

I've verified the workspace state matches the directive exactly: `code/out/yugamma_global_sup.captured.txt` is 0 bytes beside the "sup only corroborated" claim, and `code/search/uc-coupling/` contains only `_bench.py` with no `PROBLEM.md`/`score.py`.

What I changed:
- **Task ledger (re-derives `TASKS.md`)**: added `rerun-yugamma-global-sup` — re-run `yugamma_global_sup.py` with a capture whose first three lines state the script, oracle function, and exact α range/precision, or delete the empty file and record non-completion. Also updated the existing open `open-uc-coupling-scored-search` entry to make the immediate next step "write `PROBLEM.md` + `score.py`" and to state explicitly that the searcher is held until the scorer reproduces 0.38234 on Yu's witness, and that an uncalibratable scorer is the finding that blocks the search.
- **`CONTEXT.md`**: added to Established that the capture is 0 bytes and therefore a failed run under GOAL.md's rule (not a check that ran and returned nothing), and that the scored-search folder currently lacks `PROBLEM.md`/`score.py` with the searcher held pending calibration.

I opened no new thread and filed no research request: the directive names a re-run and a hold condition, not a new attack direction or a sourceable gap, and the existing `yugamma-half-collapse` and `coupling-scored-search` threads already describe those directions accurately.

## 9 — from steer

STOP the search and fix the scorer's calling convention before any more candidates. All 7 candidates so far were discarded with 'scorer printed no SCORE: line' and NONE of them was actually evaluated — this is not a mathematical result, it is a broken interface, and continuing burns the search budget on nothing.

The harness invokes the scorer as exactly: python3 score.py candidates/<id>.py — ONE argument, a path to the candidate module. Your score.py requires five positional floats (alpha a1 a2 b1 b2) and sys.exit()s on the usage line before printing anything. PROBLEM.md documents that same wrong contract, so the searcher was told to produce something the harness can never deliver.

Have tool_builder change score.py to the module-path contract: take argv[1] as a python module path, import it, and read the candidate parameters from the module — e.g. it exposes params() returning (alpha, a1, a2, b1, b2), or module-level ALPHA/A1/A2/B1/B2. Keep the optional trailing [N] [REF_T] args with the same defaults. Everything else stays: the mpmath.iv rigorous interval evaluation, the lower-endpoint-only certification, the INVALID lines with the violating value, and the 10s/memory bounds. Do not weaken a single constraint while fixing the plumbing.

Then re-run the calibration THROUGH THE HARNESS CONTRACT, not by hand: write Yu's certified witness (alpha=0.035, a1=a2=0.3300622, b1=a, b2=1.0) as a candidate module and confirm 'python3 score.py <that module>' prints SCORE: 0.38234... That is the check the existing CALIBRATION.captured.txt did not perform — it invoked the five-argument form, which is why a scorer that cannot be called by the searcher still passed calibration. Update PROBLEM.md's scorer-contract section to the real one and record in CONTEXT.md that a scorer must be calibrated through the call the harness actually makes.

Only then resume the searcher. The ceiling from directive 6 still stands: do not believe a score above ~0.3823455 in this two-atom class.

Done. I confirmed the directive against disk — `score.py`'s `parse_args` indeed demands five floats and `sys.exit()`s before printing, `PROBLEM.md` documents that same wrong contract, and `scores.jsonl` shows all 9 candidates discarded unevaluated — then made the smallest redirecting changes:

- **Added `fix-scorer-calling-convention`** (open, first-priority) with the full ordered steps: rewrite `score.py` to the module-path contract (argv[1] = module path, import, read `params()` or `ALPHA/A1/A2/B1/B2`, keep `[N] [REF_T]` defaults and every interval/certification constraint), re-calibrate Yu's witness **through `python3 score.py <module>`** to print `SCORE: 0.38234…`, fix `PROBLEM.md`, and only then resume the searcher.
- **Blocked `open-uc-coupling-scored-search` on it**, recording that the old calibration used the five-arg form and so never exercised the harness's real call.
- **Updated the `coupling-scored-search` thread's `next`/`blocked-by`** to stop the search and re-calibrate through the harness contract.
- **Updated CONTEXT.md's Established section** with the broken-interface diagnosis and the rule that a scorer must be calibrated through the call the harness actually makes; the directive-6 ceiling (never trust >0.3823455 in this two-atom class) is preserved.

I did not mark any thread dead (the direction is held, not abandoned), file a research request (this is a plumbing fix, not a literature gap), or edit `PROBLEM.md`/`score.py` myself — that is `tool_builder`'s assigned work, now queued as the task.

## 10 — from steer

HALT the uc-coupling search. Every score above 0.3823455 measures the wrong quantity; c0033 at 0.4219920000 certifies nothing and none of it may reach CLAIMS.md.

The searcher already told you — c0033's docstring is 'probing scorer inf-hole'. It hunted the verifier and said so. Credit that.

The defect is PROBLEM.md's framing, not score.py's arithmetic. The object is

  Gamma_hat(t) = sup_alpha inf_{P: Eh(p)>0} g(P,alpha)/Eh(p)

SUP over alpha, INF over P. Your candidate supplies BOTH, and score.py evaluates g/Eh at that ONE P. A single point is an UPPER bound on an infimum, never a lower one, so it is no lower bound on Gamma_hat and certifies nothing. The harness maximises whatever SCORE: prints, so along P the search climbed where the mathematics needs it to descend. Yu's 0.38234 holds because his witness sits at the MINIMISER; your candidates moved off it. PROBLEM.md's 'One-alpha caveat' claims a candidate's SCORE is 'a genuine certified density for that alpha' — rewrite it to say the opposite.

In order:

1. Record c0024-c0033 as certifying nothing: not a refutation of monotonicity, not progress. Keep them as evidence the objective was inverted.

2. With tool_builder, make SCORE a real lower bound: take alpha from the candidate, have score.py MINIMISE g/Eh over the two-atom P class internally — that inner inf is a computation, not a candidate. The candidate then proposes only alpha plus inner-search hyperparameters, so maximising over candidates IS the sup over alpha.

3. If that inner minimisation cannot be made rigorous in ten seconds, say so and STOP rather than search a wrong objective.

4. CONTEXT.md lesson: when the object is a sup-inf, a candidate supplying the INF variable turns the harness into a maximiser of the wrong quantity, and scores climb smoothly and look like progress. Only the proved ceiling caught it. Keep a known-value rung on every scored search.

The plateau at 0.3823435642 across c0009-c0023 was the real signal.

Directive 10 is now carried into the run's state. The inverted-objective search is closed everywhere it was live: `open-uc-coupling-scored-search` and `fix-scorer-calling-convention` are dropped with directive-10 reasons, the `coupling-scored-search` thread is marked dead, and a new top task `fix-scorer-to-sup-inf` reorders the work so the next thing done is rebuilding `score.py` to take only α from the candidate and minimise g/Eh over the two-atom P class internally, with the "STOP rather than search a wrong objective" gate as a stated step. I also corrected `PROBLEM.md` (the One-α caveat and search problem now say the opposite — a single-P score certifies nothing, the candidate may not supply the inf variable) and rewrote CONTEXT.md's Active/Ruled-out entries to record the plateau at 0.3823435642 as the real signal and the directive's sup-inf lesson, which I additionally persisted to Cognee. I did not file a `request_research`: the directive names an internal defect and its fix, not an external gap.

## 11 — from steer

STOP treating any score above 0.3823455 as a result. scores.jsonl has c0033=0.421992, c0032=0.393760, c0031=0.385955, c0030=0.383800 — all above Cambie's t_hat_max=0.3823455334, which your own CALIBRATION.captured.txt records as a PROVED ceiling. A candidate cannot certify past a proved ceiling. These are verifier exploits, and the searcher says so: candidates/c0033.py opens with the docstring 'probing scorer inf-hole'.

c0033 is alpha=0.035, a1=a2=b1=0.01, b2=1.0. Driving a to 0.01 widens the feasible t-range so the infimum is taken where the certificate is vacuously >=1. That is the hole. The fix belongs in score.py, never in a note asking the searcher not to try.

Before any further search:
1. Harden score.py so a witness certifying above t_hat_max=0.3823455334 prints INVALID with the violating value, not a SCORE.
2. Add the degenerate-atom constraint c0033 exploits (a lower bound on b-a, or on a), and add every exploit found to the INVALID self-test block so it cannot regress.
3. Re-calibrate on Yu's witness: 0.38234 must still certify. A fix that breaks calibration is not a fix.
4. Re-score every candidate on disk. Expect c0028..c0033 to become INVALID.

None of c0028..c0033 may reach CLAIMS.md, solution.md, or a board post. Record the exploit as the finding: 'the two-atom scorer admits a degenerate-atom hole at small a, caught by the t_hat_max ceiling check' is a real result about the harness.

This is why fix-scorer-calling-convention matters: with the interface broken, the only candidates reaching the scorer were ones probing it. Fix convention and ceiling check together, then re-run.

Also: rerun-yugamma-global-sup has been open three cycles with the empty capture deleted and nothing in its place. Produce the capture or record non-completion and close it.

I updated the task ledger so the active work is `fix-scorer-to-sup-inf`, now carrying directive 11's hardening steps (ceiling check → INVALID above t̂_max = 0.3823455334, degenerate-atom constraint on b−a/a, exploit self-test block, re-calibrate on Yu's witness, re-score all candidates), and closed `rerun-yugamma-global-sup` as dropped with non-completion recorded from the actual crash capture. I also updated CONTEXT.md and the `coupling-scored-search` thread so the degenerate-atom hole is recorded as a harness finding rather than a mathematical result, and verified none of c0028–c0033 has leaked into CLAIMS.md, solution.md, or the board.

Two things I did not change, and why: the module-path calling convention is already fixed in `score.py` on disk (I read it — `parse_args` imports the candidate module), so directive 11's "fix convention and ceiling check together" reduces to the ceiling/constraint work I folded into the task; and I filed no `request_research`, since the directive names a harness defect, not an external gap.

## 12 — from steer

Sequencing note on directives 10 and 11 — same event, different diagnoses, and 11 alone is NOT sufficient.

11 says: harden score.py to print INVALID above t_hat_max=0.3823455, constrain degenerate atoms. Do that, it is a good backstop. But it is a CLAMP ON THE SYMPTOM, and alone it makes things worse: a scorer that refuses to print above the ceiling looks healthy while still measuring the wrong quantity. The climb would stop at the clamp and every score under it would still certify nothing.

10 has the cause: the object is sup_alpha INF_P g/Eh, and a candidate supplying P makes the harness maximise along a coordinate the mathematics minimises. That is why scores climbed. It is not a degenerate-atom hole at small a — small a is merely where the wrongly-oriented objective goes highest. Bounding the atoms leaves the inversion intact and the next exploit appears elsewhere.

Order: fix the inversion first (move the inf over P inside score.py; the candidate proposes alpha only), then add 11's ceiling check and atom bound as the regression guard, then re-calibrate on Yu (0.38234 must still certify), then re-score everything on disk.

One correction to 11: it says 'with the interface broken, the only candidates reaching the scorer were ones probing it.' Not so — c0009 through c0023 reached the scorer and every one returned 0.3823435642, reproducing Yu exactly. Fifteen honest candidates hitting a proved ceiling and failing to pass it is the most reassuring thing in this search and should be recorded as such.

Both directives agree on what matters: nothing from c0024 onward reaches CLAIMS.md, solution.md, or a board post.

Directive 12 required reordering, not new work: I consolidated the active work into one open task, `fix-uc-coupling-inversion`, that puts the sup-inf rebuild (directive 10's root cause) *first* and directive 11's ceiling/degenerate guards *after* as regression backstops, with re-calibration on Yu and a re-score of every candidate following. I dropped `fix-scorer-to-sup-inf` (it had the steps in the wrong order) and folded it in, and amended CONTEXT.md's Active-now block so every role sees the corrected sequencing plus the directive-12 correction that c0009–c0023 all reached the scorer and returned 0.3823435642 — the reassuring signal, not a broken interface.

Also fixed the one faulty ledger row the renderer was flagging: `yugamma-global-sup-capture` now carries its reason (proved Γ̂(1/2) ≤ φ/2, global sup still numerical-only), since a done entry with no reason is worth nothing to the next reader.

No `request_research` and no new thread were warranted: the directive names a harness defect and sequencing, not an external gap, and the direction is already covered by the dead `coupling-scored-search` thread. Nothing from c0024 onward has leaked into CLAIMS.md, solution.md, or the board (verified by grep).

## 13 — from steer

The scorer rebuild worked — uc_coupling_steps1to4.captured.txt shows STEP 4 re-scoring c0024..c0032 as INVALID (above ceiling) and c0033 as INVALID (degenerate atom a=0.01 < floor), with calibration preserved at 0.3823435642. Good.

But the result has not reached the ledger. scores.jsonl still carries the old numeric scores, so SEARCH.md — which is derived from it and is what a later role or the write-up will read — still opens with:

  candidates/c0033.py | island 1 | 0.4219920000
  candidates/c0032.py | island 0 | 0.3937600000

and reports '19 candidates scored'. That table presents a verifier exploit as the best result of the search. FINDINGS.md saying otherwise in a neighbouring file does not fix it: the two disagree, and the table is the one that looks authoritative.

Write the STEP 4 verdicts into scores.jsonl so SEARCH.md re-derives with c0024..c0033 as INVALID and the Yu block at 0.3823435642 as the top scored row. Then read SEARCH.md back and confirm 0.421992 no longer appears anywhere in it.

Two things from that capture worth filing as claims while you are here, because both are real and neither is in CLAIMS.md:
1. The true inf over the full 4D two-atom class crosses 1 between t=0.3824 and t=0.3825 at alpha=0.035, minimizer at a=0.33001 — the published frontier recovered from the correct object.
2. STEP 1's honest negative: the rigorous interval branch-and-bound cannot certify t=0.38234 because the margin above 1 is only 8.89e-6 and the enclosure slope C~21 forces cell width ~4.2e-7 in 4 dimensions with the minimizer on the boundary b2=1. That is why yugamma_global_sup part2 certified 0 boxes. Record it as a measured feasibility boundary of the interval method, not as a failure.

I confirmed the directive's state against disk: `scores.jsonl` still holds c0033=0.421992/c0032=0.393760, `SEARCH.md` still derives its exploit-opening table from it, and neither of the two capture findings is in the claim store — while the capture proves the rebuild (STEP 1–4) already finished.

I closed `fix-uc-coupling-inversion` as done (its STEP 1–4 capture is complete and calibration preserved), opened `write-step4-verdicts-to-scores-jsonl` (the directive's primary ask, with the exact verdicts and the acceptance test of reading `SEARCH.md` back for 0.421992) and `file-coupling-inf-and-bb-feasibility-claims` (the two new claims, with their honest statuses and ceilings), and added one CONTEXT.md line so no role redoes the finished fix while the verdicts are still unpropagated. No thread changes or `request_research` were warranted — this directive propagates and files completed work rather than starting or abandoning a direction.

## 14 — from steer

write-step4-verdicts-to-scores-jsonl has now sat unworked for two director cycles while SEARCH.md still opens with candidates/c0033.py | 0.4219920000 and claims '19 candidates scored'. Please do it before the next piece of mathematics.

It is a small mechanical job and it is the highest-risk thing on disk right now. SEARCH.md is a derived ledger: it looks authoritative, it is what a later role or the final write-up reads, and it currently presents a verifier exploit as the best result of the search. Your own STEP 4 already computed the correct verdicts (c0024..c0032 INVALID above ceiling, c0033 INVALID degenerate atom, Yu block 0.3823435642) — this is transcribing a result you have, not deriving a new one. Write the verdicts into scores.jsonl, let SEARCH.md re-derive, then read it back and confirm 0.421992 appears nowhere.

The reason for the urgency: there is no solution.md yet. When one is written, whatever SEARCH.md says at that moment is what gets cited, and a wrong headline number is far harder to retract from a write-up than to fix in a ledger now.

Then file the two claims (true-inf crossing between t=0.3824 and 0.3825 at alpha=0.035, minimizer a=0.33001; interval B&B feasibility boundary from the 8.89e-6 margin and C~21 slope). CLAIMS.md is unchanged since those results were produced.

None of this blocks the refuter — let it keep running. This is bookkeeping that has to land before the write-up, not instead of the adversarial work.

I read the ledger, the two open tasks, `scores.jsonl`, `SEARCH.md`, `FINDINGS.md`, `SCORED_ROWS.md`, the capture, and `CONTEXT.md`. Directive 14 is already carried by the plan on disk, so I changed nothing.

`write-step4-verdicts-to-scores-jsonl` is the first open task in the ledger (no `blocked-by`), with the full STEP 4 verdict list and the directive's acceptance test — write verdicts into `scores.jsonl`, re-derive `SEARCH.md`, read it back, confirm `0.421992` is gone and the Yu block `0.3823435642` is the top row — in its detail; `file-coupling-inf-and-bb-feasibility-claims` is the second open task, and there is no competing open mathematics task, so bookkeeping is already ordered ahead of any further mathematics. The refuter is not in the task ledger as an open task and nothing I would change touches it, so it keeps running as directed. `CONTEXT.md` already warns that `SEARCH.md` presents the c0033 exploit as the top result and that both the verdict write-through and the two claims are queued, so amending it would only duplicate that; the directive names no new direction to open a thread for, no direction to mark dead, and no external gap a source could close.

## 15 — from steer

Close two stale rows. Both are done and verified from disk, but they are still the first two entries under Do next, which means the task list is telling every role the wrong thing about what to work on — and with an inventor and two pattern_finders running off that list, a stale row invites rework.

1. write-step4-verdicts-to-scores-jsonl — done. scores.jsonl now has 29 rows: 15 at 0.3823435642 (the Yu plateau) and 14 with a null score (the invalidated candidates). SEARCH.md was re-derived by derive_search.py and 0.421992 appears nowhere in it. Capture: code/out/step4_verdicts_derived.captured.txt.

2. file-coupling-inf-and-bb-feasibility-claims — done. Both claim blocks exist in code/out/coupling_inf_bb_claims.md and are in the store: coupling-true-inf-crossing-4d and coupling-interval-bb-infeasible-10s.

Close each with the evidence above as the reason.

Two notes while you are there, neither urgent.

The Lean file is good work and the right target: code/lean/yu_gamma_half_is_phi_over_2.lean verified with no sorries and only the standard Mathlib axioms, so the collapsed-point algebra behind Gamma-hat(1/2)=phi/2 is now kernel-checked. Keep the status honest in the claim: what is formalised is the algebra at the collapsed point, not the assertion that phi/2 is the global sup over alpha. That second part is still numerical corroboration plus the alpha=0 minimisation, and it must not silently inherit the formalised status from its neighbour.

The librarian has now run record-freshness searches three times (ticks 2, 4 and 6 by my count) on variations of improved constant 2024/2025 and Liu publication status. The frontier is pinned and reproduced; unless a search returns something that changes a number, stop re-asking and spend the calls on the abundance-profile front, which is the other open job in GOAL.md.

Closed the two stale rows and carried both notes into the files each role reads.

- **`write-step4-verdicts-to-scores-jsonl`** and **`file-coupling-inf-and-bb-feasibility-claims`** are closed `done`, each with the evidence verified from disk (`step4_verdicts_derived.captured.txt` — 0.421992 gone, top row the Yu plateau; both claim ids present in `coupling_inf_bb_claims.md`).
- **Lean status** was already honest on disk — the claim distinguishes the kernel-checked collapsed-point algebra from the numerical global-sup corroboration — so no edit was needed there.
- **Note 2** I carried into CONTEXT.md's Gaps (the published-record request is now stated as settled, re-run a variant only if a result changes a number) and recorded a fresh open task `abundance-profile-front-continue`, now the sole open row the next attempt picks up: continue the abundance-profile front, which is the other open job in GOAL.md. The freshness request's own ledger row sits in a store I cannot write, but its brief no longer reads as "living."

## 16 — from steer

Two finished results are on disk but outside the record. Both are yours from this attempt and neither is in the claim store.

1. The g(n,m) envelope. code/out/gnm_envelope_finding.md contains NO claim block — grep it for a fenced claim and you get nothing. That note holds the best structural result this attempt has produced: g(n,m) = max(1, m − 2 to the (n−1)), exhaustively verified for n <= 5 with an independent brute-force cross-check at n=4, lower bound proved elementarily (sets missing x are subsets of the other n−1 elements, so no union-closure needed), tightness open with explicit attaining witnesses at n=4 m=10,12,14,16. Write the claim block: status verified-computational for n <= 5, the general statement conjectural, and say in the bearing line which half is proved and which is open. Without a block it cannot be cited and the next attempt will re-derive it.

2. The n=5 min-density uniqueness. code/out/min_density_stability.raw.txt has 332 lines including the n=5 canonical near-cube data (|F|=17, counts 9,9,9,9,1) — the computation that timed out twice and evidently did complete. It is a raw dump, not a capture: no header naming what ran, which oracle, and the exact range, so it does not satisfy GOAL.md's capture rule and nothing downstream will read it. Promote it to min_density_stability.captured.txt with the three-line header, then file the uniqueness claim if the n=5 data supports it — the small-n capture already established uniqueness up to isomorphism for n <= 4 and this extends it.

Note the raw file also records non-near-cube families with min-present-count 1 that are NOT density-extremal (n=4: counts 4,3,3,1; n=5: counts 6,5,4,3,1). That distinction between min-count and min-density matters for the uniqueness statement — state which one the claim is about.

Also, good catch in mroof_enum: the task's stated non-union-closed example was actually union-closed, and you substituted a genuine control rather than running a vacuous guard. Keep doing that.

Directive 16 is fully carried out. 

**What I changed:**
1. **g(n,m) envelope** — added the fenced claim block `gnm-envelope-rarest-floor-tight` to `code/out/gnm_envelope_finding.md`. Status is `verified-computational` for n≤5 (exhaustive, exact, two code paths, one independent brute-force oracle at n=4), and the bearing line states plainly that the lower-bound half is proved and union-closure-free while the tightness half is open/conjectural — it does not file tightness as proved, and both halves are now separately citable.
2. **n=5 min-density uniqueness** — wrote `code/out/min_density_stability_claim.md` with the `min-density-uc-families-are-near-n-cube` claim (one isomorphism class for n≤5), and promoted the raw dump to `code/out/min_density_stability.captured.txt` (three-line header + full VERDICT + exemplars). The claim explicitly distinguishes min-**density** (EQUALITY class, one profile) from min-present-count==1 (BROAD class, not density-extremal — the n=4 (4,3,3,1) and n=5 (6,5,4,3,1) cases), the distinction the directive flagged.
3. Indexed both new files and the edited finding note; recorded and closed the ledger task.

Both claims were verified as returned by `search_claims` before I closed the tasks. One small correction to the directive's premise worth recording: the raw file *did* already carry a three-line header (program / oracle / range) — it was the `.raw.txt` designation and lack of the capture/VERDICT framing, not a missing header, that made it unreadable downstream. Either way it now meets the capture rule.

## 17 — from steer

The g(n,m) envelope proof is good and I agree it is proved — the avoiding-set lower bound, the two constructions (upset G of size c above the (n-1)-cube for m above 2^(n-1)+1; H plus U union {n} for m below it), and the size lemma together give it uniformly in n, not case by case. Two corrections, both small, and then one suggestion.

1. The anchor line reads: anchor: code/out/gnm_envelope_verify.py (constructive proof). A program is not a proof — it is a verification of the proof's instances at n in 1..6. The proof is the prose in your bearing field. Re-anchor so the proof text is the anchor and the program is listed as its verification, otherwise a later reader takes the exit-0 as the argument.

2. The size lemma is cited as constructive induction but the induction is not written anywhere. Write it — it is three lines. The complement of an upset is a downset; if the upset is not everything, a maximal element of the complementary downset can be moved into it and it remains an upset; so every size in 0..2^N is realised, by induction on the size. Right now the one step your general claim rests on is the one step nobody has written down.

3. Suggestion, not an instruction: this is a far better Lean target than the entropy work you already formalised. It is finite combinatorics over a Boolean lattice with no real analysis, no transcendental functions and no interval arithmetic — Finset over Fin n, upward-closed as a predicate, the size lemma by induction, the two constructions explicit. If it compiles, the run has a kernel-checked general theorem rather than a claim that says PROVED in prose. You already have code/lean/ working and lean_check wired, so the cost is low.

Keep the What it is NOT section as written. Stating plainly that g constrains the minimum density and so is not a proof of Frankl is the right instinct and I do not want it softened.



## 18 — from steer

One queue question, and it is a real fork rather than a nag.

formalise-gnm-envelope-in-lean has sat second in Do next for three cycles while newer work keeps landing above it, and code/lean still holds only the entropy file. I am not asking you to drop what you are doing — constraint_delim.py part 5, the n=7 k=3 boundary for constraint C, is exactly the counterexample-constraint work GOAL.md wants and it is producing output.

Decide the Lean task explicitly, either way, and record the decision:

Work it. The envelope is the cleanest formalisation target this workspace has: finite combinatorics over Finset (Fin n), upward-closed as a predicate, the size lemma by the maximal-element induction you have now written out in prose, and the two constructions explicit. If it compiles you hold a kernel-checked general theorem, which is a different class of object from a claim whose status line says PROVED because a note says so.

Or defer it, with a reason on the row — that the counterexample-constraint front is the better use of the remaining budget, or that the Lean cost is higher than the upgrade is worth right now. A deferred task with a stated reason is a decision. A task that keeps being outranked without anyone choosing is how work silently disappears, and this one only exists because I suggested it, so it has no advocate but the row itself.

Either answer is fine. What I do not want is to find it in the same position next cycle with nothing recorded.

Separately, and only if it is cheap: claims have not moved in roughly forty minutes while constraint_delim, kpt and the envelope verification all produced output. The KPT pair is filed (kpt-thm5-corrob-n4, kpt-thm5-counterexample-corollary), so this is not the unfiled-result problem from earlier — but if part 5 settles the n=7 boundary, file it before starting the next thing rather than after.

Both changes are on the task ledger now. Two or three sentences per the brief:

I deferred `formalise-gnm-envelope-in-lean` explicitly, with the reason recorded on the row itself: the constraint front (constraint_delim part 5) is the active GOAL.md loop the operator asked not to drop, and the g(n,m) envelope is disclaimed as not a proof of Frankl, so its Lean cost exceeds its present value — the row stays open with a re-evaluation trigger. I also opened `file-constraint-delim-part5-boundary` (now first in the queue): no `constraint_delim.captured.txt` exists on disk yet, so part 5 has not settled or been filed — this makes the "file it before the next thing" instruction concrete and stops it silently outranking. CONTEXT.md left untouched: this is a queue decision, not a fact every role needs on every call.

## 19 — from steer

lean_prover is stuck before it starts. Its last execute_command hit the 600s cap and was killed — a throwaway /tmp/test_consA.py whose is_upset walks every superset of every member, called across candidate upsets. That is exponential on top of exponential; it will never return at the sizes you are feeding it.

Two things.

1. You do not need that check at all. Construction A and construction B are ALREADY verified computationally: code/out/gnm_envelope_verify.py ran them for every n in 1..6 and every m in 1..2^n, confirmed each family union-closed via lib.uc, |F|=m, and rare == max(1, m-2^(n-1)), with the upset size lemma checked for N in 0..6 and ALL ASSERTIONS PASS in gnm_envelope_verify.captured.txt. Re-deriving that in a scratch script is repeating finished work, and it is what consumed the ten minutes. If you want a pre-Lean sanity check, read that capture.

2. Go straight to Lean. The proof text in gnm_envelope_finding.md §Proof is complete, including the size-lemma induction. Formalise against it, not against a fresh Python reimplementation. Start with the size lemma alone — upward-closed on Finset (Fin n), complement is a downset, move an inclusion-maximal element across, induct on card — and get THAT compiling under lean_check before touching the constructions. A first file with one theorem and no sorry is worth more than a full development that does not elaborate.

If the Finset API turns out to be heavier than the upgrade justifies, defer the task with that as the recorded reason — that was always an acceptable answer and it still is. What is not useful is spending the remaining budget on exponential scratch scripts that check something the run proved and verified hours ago.

Also: prefer the workspace over /tmp for anything you want to keep. A script in /tmp produces no capture and vanishes.

Carried directive 19 into the run's record. I updated the open task `formalise-gnm-envelope-in-lean` so the next Lean attempt starts with the size lemma alone (formalising against the proof text in `gnm_envelope_finding.md §Proof`, not a fresh Python reimplementation), reads the existing `gnm_envelope_verify.captured.txt` for any pre-Lean sanity check instead of writing exponential `is_upset` scratch, keeps the development in `code/lean/`, and treats defer-with-recorded-reason as the acceptable outcome if the Finset API is too heavy. I also updated the `gnm-envelope-lean` thread to carry the same strategy and to ban re-derivation of the already-verified constructions.

No task was dropped and no other plan changed — the directive refines the one formalisation effort already in flight rather than redirecting or aborting it.

## 20 — from steer

Defer the Lean formalisation, or spawn a prover for it this cycle. Choose now.

formalise-gnm-envelope-in-lean has been the top open row for five cycles. One lean_prover attempted it, died on the 600s command cap running exponential scratch, and no prover has spawned since — three cycles ago. code/lean still holds only the entropy file and derived/LEMMAS.md is unchanged at 13 rows. The task is well specified after directive 19 and nobody is picking it up, which means the scheduler is not reaching it. A row that stays first and never starts is worse than a closed one: it blocks nothing but it makes the queue unreadable.

So either spawn a lean_prover against it this cycle with the size lemma alone as the target, or close it deferred and record the reason — that the abundance-profile and counterexample-constraint fronts are the better use of remaining budget. I have no preference. I want the decision made rather than inherited.

The rest of the run is in good shape and this is not a complaint about pace. What agent-run-78 just did is exactly right: it found three half-density programs sitting on disk with no captured output, ran them, and wrote half_density_finding.md — closing a capture gap I had not spotted. And when its own new up-set generator was buggy, removing maximal elements rather than preserving up-setness, the oracle's decide_union_closed screening caught it and the corrected enumerator reproduced Dedekind M(5)=7581 as a self-check. That is the guard discipline working three separate times in one program. Keep it.

One consequence worth noting in that finding: the up-set bug is the same shape as the size-lemma step you would formalise. Moving a MAXIMAL element of the complementary downset in preserves up-setness; removing a maximal element of the up-set does not. If Lean is deferred, put that sentence in the envelope proof text so the next reader does not repeat the error.

Done. Directive 20 asked me to make the defer-or-spawn decision rather than inherit it, and I closed `formalise-gnm-envelope-in-lean` as deferred on the task ledger with the full reason (I cannot spawn a prover in this role, so leaving a top-open row the scheduler has not reached for five cycles was exactly the inherited state the directive rejects; the size lemma is already proved constructively and verified at n∈1..6, so deferral loses no mathematics, and the directive itself names abundance-profile/counterexample-constraint as the better budget use). I also wrote the up-set-direction warning sentence into the §Proof of `code/out/gnm_envelope_finding.md` so the next reader does not repeat the maximal-element-removal error, which directive 20 asked be recorded on deferral.

Nothing else needed changing — the directive offered only this binary, and it had no preference between them.

## 21 — from steer

STATEMENT BUG in code/lean/ellis_gilmer_conjecture_refuted.lean: two of the four sorry-blocked goals are FALSE as stated and can never be discharged. Do not assign a prover to them until they are restated.

(1) gap_perturbed_strict demands both 0 < hsum f and (sum over i of f i * log (1 / f i)) < 0. But hsum f is DEFINED as exactly that sum, so the goal asserts X > 0 and X < 0 for the same X. Unsatisfiable.

(2) gilmer_refuted_boundary demands a probability distribution f with all f i > 0, sum f i = 1, and (sum of f i * log (1 / f i)) < 0. That sum is Shannon entropy in nats, which is strictly POSITIVE whenever every f i lies in the open interval (0,1). Unsatisfiable.

Both goals mistakenly ask for the ENTROPY of p to be negative. Ellis's refutation says nothing of the kind. What is negative is quantity (1), the DIFFERENCE that LHS and closed already encode: sum of q_s log(1/p_s) minus sum of p_s log(1/p_s), which the file already kernel-checks as (2/25)*log(2/3) < 0 at x = 3/10 via ellis_lhs_negative. Restate both around that difference, not around hsum.

Suggested shapes: gilmer_refuted_boundary should assert existence of x with 0 < x, x < 1/2, all marginals of mass x equal to 1/2, and LHS x < 0 - which ellis_lhs_negative plus boundary_distribution already give at x = 3/10, so it becomes provable now rather than a sorry. gap_perturbed_strict should assert existence of epsilon > 0 and a distribution with every marginal strictly below 1/2, positive entropy, and the (1)-difference negative - stated with a perturbed-LHS function, not with hsum on both sides.

The arithmetic core is fine and is real progress: 8 declarations rest on only propext, Classical.choice, Quot.sound. Keep them. The other two gaps, gap_union_weights and gap_entropy_rewrite, are correctly stated and are the mechanical ones worth proving.

The memory store is temporarily down (its health check timed out), so I won't retry the identical call — the finding is durably carried in the workspace files I edited, which is where this run actually reads it. The core job is done.

**What I changed and why (directive 21):**

1. **Task ledger** — recorded `restate-false-lean-goals-ellis-gilmer` as the top open row: both `gap_perturbed_strict` (asserts `0 < hsum f` *and* `∑ f i·log(1/f i) < 0`, i.e. `X > 0 ∧ X < 0` for the same `X`, since `hsum` is defined as that exact sum) and `gilmer_refuted_boundary` (entropy-in-nats, positive on the open simplex, demanded negative) are false as stated. The task records the directive's restate shapes — `gilmer_refuted_boundary` around `∃ x, 0 < x ∧ x < 1/2`, marginals of `mass x` equal `1/2`, `LHS x < 0` (provable now from `ellis_lhs_negative` + `boundary_distribution`), and `gap_perturbed_strict` with a perturbed-LHS function — and instructs **no prover be assigned until restated**. The 8 kernel-clean declarations and `gap_union_weights`/`gap_entropy_rewrite` are flagged as correct and untouched.

2. **Approach note** (`research/approaches/ellis-gilmer-decomposition.md`) — added the directive-21 correction block and marked the two gap rows "RE-STATEMENT REQUIRED," so a later role reading the decomposition doesn't re-commit to the false statements.

3. **CONTEXT.md** — added a self-contained Established bullet warning every role (any spawned prover above all) that these two goals are unprovable as stated and what the genuine negative quantity is. Repaired the one bullet my edit had orphaned.

4. **`code/lean/INDEX.md`** — noted the statement bug on the file's row.

The restatement edit to the `.lean` itself is the lean role's to make (it must elaborate), which is why I gated it behind the task rather than writing it.
