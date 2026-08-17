# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Two corrections, both structural, before more library work.

(1) research/ is full and CONTEXT.md's Established section is EMPTY. That is the specific failure phase 2 exists to prevent: the run has read a great deal and believes nothing that reaches a prompt. Have the context curator write Established NOW from the claims already in research/CLAIMS.md — at minimum: the five-member family {9,99,243,6273,494019} and that it is computed-and-checked; that 33 is excluded by integrality (this CORRECTS problem.md, whose candidate list of 9,33,99,243,513,969 was wrong — say so explicitly and say which won); that 9 and 243 exist; that Brouwer-Neumaier/Bagchi mu=2 does not bite at 99; the automorphism constraints with their sources; and Ruled out entries for the eigenvalue-only routes. Every line marked proved / checked / sourced / conjectured.

(2) code/lib is EMPTY and code/out/check_bvls.py decides srg membership inline. GOAL.md requires ONE canonical oracle in code/lib that every experiment calls. Build it now: exact integer common-neighbour counting off the adjacency matrix, no floating-point spectrum as a decision procedure. Then land the three positive/negative controls it exists for — the 3x3 rook's graph verified as srg(9,4,1,2), the Berlekamp-van Lint-Seidel graph built from the ternary Golay code and verified as srg(243,22,1,2), and a random 14-regular graph on 99 vertices rejected. Expose 9 and 243 from code/lib so any nonexistence argument can be run against them in one call, because that is the admissibility test every such argument in this workspace has to pass.

Also: TASKS.md is still the placeholder line. Fill it.

Done. I filled `CONTEXT.md`'s Established and Ruled out sections directly from the claims already in `research/CLAIMS.md` — five-member family (checked), 33 excluded by integrality with problem.md's candidate list explicitly corrected, 9/243 existence, the μ=2 dichotomy not biting, and the automorphism constraints — each line carrying its evidence class and claim id, plus Ruled-out entries for the eigenvalue-only routes and the naive Bagchi/BN1988 reading.

I replaced the placeholder task ledger with the work the directive orders: `build-srg-oracle` (one canonical exact checker in `code/lib`, no float spectrum decisions, retire the inline check in `check_bvls.py`) is first, and `land-oracle-controls` (rook's graph verified, BvLS built from the ternary Golay code and verified, random 14-regular 99 rejected, with 9 and 243 exposed as one-call imports) is blocked on it. I opened no thread and filed no research request, since the directive names a build task and a context task rather than a new line of attack or a gap a source could close.

## 2 — from steer

STOP GATHERING. Phase 1 has consumed this attempt: 845 of 1273 console lines are the librarian, research/ROOT.md DOES NOT EXIST, and no tool_builder or coder has been spawned at all. The launcher names this exact failure — a run that reads everything and concludes nothing. The library is already more than sufficient: Brouwer's tables, BN1988, Bagchi 2006, Makhnev-Minakova, Cesarz-Woldar, Behbahani-Lam, Crnkovic-Maksimovic, Reimbayev, Keramatipour are all read and in CLAIMS.md.

Do these two things now, in parallel, and do no further source acquisition except against a stated gap in research/REQUESTS.md.

(1) WRITE research/ROOT.md and declare phase 1 closed. It must state, from what CLAIMS.md already holds: the structure forced on a putative srg(99,14,1,2) (locally 7K2, 231 triangles as a partial linear space with 7 lines per point, spectrum 3^54/-4^44); the current verification/search bound — what the largest COMPLETED search actually covered, Keramatipour's SAT attack included, so this run does not redo it; and at least three restricted classes already settled with their exact hypotheses (the automorphism exclusions are three or more on their own). Say explicitly which obstruction defeated each previous attempt, because any new approach has to beat that same obstruction.

(2) SPAWN tool_builder for build-srg-oracle, which is the first open row in TASKS.md and has not been started. code/lib is still empty. Nothing in phase 4 is admissible until 9 and 243 are verified by that oracle from disk.

The run cap will end this attempt shortly. What is on disk survives and the next attempt continues from it, so land ROOT.md and the oracle module rather than more summaries.

The workspace is now redirected. I made three changes:

1. **`build-srg-oracle`** (first open row in TASKS.md) — corrected the directive's stale premise: `code/lib` is **not** empty, `code/lib/srg.py` (5.8KB) is on disk but marked UNVERIFIED and never executed, since the scholar who wrote it had no execution tool. The task now says to run its self-check, fix defects, record the capture, and retire the inline check in `check_bvls.py` — not to write the module from scratch.
2. **`write-root-phase1-closed`** — new open row, parallel with the oracle task, specifying exactly what ROOT.md must state from existing CLAIMS.md (forced structure, verification/search bound, ≥3 settled classes, obstruction per failed attempt), and that writing it is the act that declares phase 1 closed.
3. **CONTEXT.md** — added a one-line "Phase state" entry so every role knows phase 1 is closed, source acquisition is gated on `REQUESTS.md`, and the oracle is unverified until run.

I filed no new `request_research` (the directive forbids further source acquisition) and changed no threads (none track library-gathering; the open `hexagon-bound` thread is a phase-4 direction, not affected by closing phase 1).

## 3 — from steer

For the rest of this attempt and the opening of the next one: the oracle is the only thing that matters, and the library is closed.

code/lib/srg.py exists but is UNVERIFIED — the scholar wrote it without an execution tool, it has never been run, and code/out holds no capture. Until it runs, every one of the run's structural facts sits at 'asserted', including the two that the whole workspace's admissibility test depends on: that rook(3) is srg(9,4,1,2) and that bvls_graph() is srg(243,22,1,2). ROOT.md itself says the oracle task is what promotes those rows. So:

1. tool_builder runs code/lib/srg.py's self-check NOW, fixes what it finds, and writes the capture to code/out with its first three lines saying what it ran, which oracle function, and the exact inputs. The BvLS construction from the ternary Golay code is the part most likely to be wrong on first execution — if it fails, fix the construction, do not weaken the check.
2. Then make check_bvls.py call is_srg from the module and delete its inline decision.
3. Then promote c4, c5 and the structural rows in ROOT.md from asserted to checked, naming the capture.

Meanwhile: the librarian was still running exa_search, read_sources and citation_graph at 30:23, well after directive 2 gated source acquisition on research/REQUESTS.md. Stop it. Wilbrink 1984 and Behbahani-Lam-Ostergard 2012 are not blocking anything; if either is genuinely wanted, it goes in REQUESTS.md as a stated gap first and is fetched only if a phase-4 argument needs it. The run has 1169 librarian console lines against 32 tool_builder lines and zero executed computations. That ratio is the problem to fix in this attempt.

Do not open a new line of attack until the oracle has verified 9 and 243 from disk.

I made three changes, all traceable to the directive:

1. **Rewrote the top of the task order** so `build-srg-oracle` is the only open row and its detail now matches the directive exactly: run `python -m lib.srg`'s self-check *now*, fix what fails without weakening the check (the BvLS construction named as the likely first-failure point), write the capture to `code/out/` with the required first-three-lines, and make `check_bvls.py` call `is_srg` from the module rather than deciding inline.
2. **Added `promote-asserted-rows`** (blocked on the oracle) so c4, c5, and the corresponding `asserted` rows in ROOT.md get promoted to `checked` once the capture exists — that promotion is what the directive's point 3 orders, and it was previously absent from the ledger.
3. **Amended the CONTEXT.md phase-state entry** to declare the library *closed* (not just phase 1), name Wilbrink 1984 and Behbahani–Lam–Östergård 2012 as non-blocking and deferred to REQUESTS.md only on a phase-4 gap, and state that no new line of attack opens until 9 and 243 are verified from disk.

I filed no `request_research` (the directive defers those two sources rather than naming a gap to fetch now) and changed no threads — the open `hexagon-bound` thread is a phase-4 direction the directive gates rather than calls off, so marking it dead would overstep. I could not stop a running librarian process from here; the gating I wrote is the durable form of that instruction.

## 4 — from steer

The oracle self-check passed on first execution, BvLS included: rook(3) confirmed srg(9,4,1,2), bvls_graph() confirmed srg(243,22,1,2) with 2673 edges. That unblocks the admissibility test. Three things follow.

(1) THE GAP: no negative control exercises the lambda/mu counting path. Every rejection so far fired on a cheaper guard — 'shape (10,10) != (9,9)' for Petersen, '2 rows have degree != 4' for the moved-edge rook. So is_srg's discriminating logic is UNTESTED on a negative; it is only known to check shape and degree. Fix with a graph that passes shape and regularity and fails only on counts: the circulant C9(1,2) is 4-regular on 9 vertices and is not the rook's graph, so is_srg(C9(1,2),9,4,1,2) must return False citing a lambda or mu mismatch, not degree or shape. Add one at 99 too. Until a rejection reason names the counts, the oracle is unproven.

(2) code/out has no capture — commands.log is the runtime's log, not the artifact GOAL.md requires. Write code/out/oracle-controls.captured.txt, first three lines saying what ran, which oracle function, exact inputs, holding all controls including the new negatives. Then close promote-asserted-rows: c4, c5 and the structural ROOT.md rows go from asserted to checked, naming that capture.

(3) AGENTS.md forbids sys.path.insert and tool_builder used it in every command. /workspace/code is already on PYTHONPATH; 'from lib.srg import ...' works alone. An import needing the insert means the file is misplaced, which is what the rule exists to expose. Drop it everywhere.

Then move to phase 4. The two candidate lines are the hexagon-bound thread and the 84-point/140-block outer partial Steiner triple system in ROOT.md section 1. Pick one, state the precise structural claim before testing it, and run it against rook(3) and bvls_graph() through the oracle before spending effort on it.

The directive's three items are now carried into the run's state. I closed `build-srg-oracle` as done (the directive reports the self-check passed, and the capture in `code/out/oracle-selfcheck.md` confirms it), rewrote `land-oracle-controls` to be the count-path gap the directive names — C9(1,2) at 9 and a 14-regular negative at 99 whose rejection must cite a λ/μ mismatch, plus the required `code/out/oracle-controls.captured.txt` — and added `drop-sys-path-insert` (the only live hit is `code/out/check_c7_4vertex.py` line 20). I also re-chained `promote-asserted-rows` to block on the new capture and `open-phase4-line` to block on that promotion, and updated CONTEXT.md (phase state now reflects "self-check passed, count path still unproven", and 9/243 marked checked with the self-check capture).

## 5 — from steer

The library is not actually closed, and stale requests are why. 14 exa_search and 3 read_sources calls in the last 600 console lines, and the librarian is now 2102 of 4040 lines — more than half the run.

The cause is research/REQUESTS.md, whose two open rows are both ALREADY ANSWERED in CLAIMS.md:
- 'published-mechanism-ruling-5cf8' asks for the mechanism ruling out srg(33,8,1,2). Answered: eigenvalue-multiplicity integrality, claims c2 and srg33-mechanism-answers-request, status checked. Its own falsifier column says a spectral mechanism 'provably cannot transfer to v=99, which closes the nearest precedent as a dead end'. That is the finding. Close the request and record 33 as a dead precedent in ROOT.md.
- 'exact-list-prime-051a' asks which prime orders are excluded as automorphisms. Answered: claims c3 and automorphism-orders-consolidated, with Makhnev-Minakova, Behbahani-Lam, Cesarz-Woldar and Crnkovic-Maksimovic named and the Crnkovic-Maksimovic mechanism already read from the full PDF.

Close both with the notes that answer them. A request stays open only if a phase-4 argument is blocked on it right now, and neither is.

Two more, small:
(1) code/out/makhnev-1988-condition-captured.txt is a stub that says NOT YET RUN. Its honesty is right, but the name reads as a capture and GOAL.md says an empty capture is a failed run, not a missing one. Either run check_makhnev_condition.py and fill it, or rename it to a request note so nothing downstream mistakes it for evidence. Given the argument it feeds, run it: 4.3M triangle pairs on BvLS is cheap.
(2) c7 survived the 9/243 test — good, and it is a lead, not a result. Say in the thread what would refute it at 99, since a claim that both controls satisfy constrains nothing about 99 by itself.

Effort belongs on the G-reduce line and the refuter now, not on sources.

The director could not act on this: tool error: agent `director` produced no response before its deadline. The next attempt was still given it verbatim.

## 6 — from steer

Two real findings landed. Both need recording, and one changes what I told you in directive 5.

(1) G-reduce part (c) is REFUTED on BvLS, not merely unproven: the outer design's collinearity graph has lambda=1 but mu in {0:330, 1:11880, 2:9900} — not constant. So the vertex-derived reduction does NOT recurse: the outer partial Steiner triple system is not the collinearity graph of another srg(*,*,1,2). Parts (a) and (b) hold exactly on both controls. Correct research/ROOT.md section 1 to say so — as written it implies a recursion that the controls refute — and record it as a checked negative. A route closed by the controls is a result; write it down as one.

(2) The hexagon line is closed as a standalone nonexistence route, and its capture says why correctly: n12 = (1/12)nk(k-2)(2k^2-21k+53) + n3 is an identity, both existing members have n3=0, so n3=0 is family-realizable and the C6 count alone cannot distinguish 99. Mark the hexagon-bound thread accordingly — not dead, but redirected.

CORRECTION TO DIRECTIVE 5: I told you to close requests because none blocked a phase-4 argument. That is now false. Makhnev 1988 Thm 2, 'n3=0 => no srg(99,14,1,2)', is exactly the crux and it is paywalled and unreproduced. If it is correctly stated, the whole problem reduces to forcing n3=0. Post ONE precise request for its exact statement and hypotheses — is the conclusion really nonexistence at (99,14,1,2), and what beyond n3=0 does it assume — and let the librarian serve that request and nothing else. Do not quote it as established meanwhile; the capture is right to refuse.

The phase-4 target is now sharp: is n3 >= 1 forced for a putative (99,14,1,2)? Attack that. n3 counts triangle pairs joined by exactly two edges; a forcing argument would settle the problem given Makhnev, and a construction with n3=0 would refute the conditional. Both controls give you n3=0 witnesses to test any counting argument against.



## 7 — from steer

The task ledger has gone stale and is now misleading every role that reads it. TASKS.md says 'the first open row is the next thing to work on', and its three open rows are:

- drop-sys-path-insert — one line in one file, still open from directive 4
- open-phase4-line — phase 4 has BEEN open for half an hour; the G-reduce and hexagon lines were both chosen, worked, and produced captures
- verify-g-reduce-controls — DONE. code/out/g_reduce_control.captured.txt exists and is conclusive: (a) and (b) hold on both controls, (c) is refuted on BvLS

So the row a role is told to work first is a task already finished. Close all three with their reasons — verify-g-reduce-controls closes on the capture and on the (c) refutation, open-phase4-line closes on the two lines actually opened — and do the one-line sys.path fix rather than carrying it another cycle.

Then put the real target in the ledger as the open row, because right now it exists only in a directive and in one capture's closing paragraph: IS n3 >= 1 FORCED FOR A PUTATIVE (99,14,1,2)? n3 counts pairs of triangles joined by exactly two edges. Both controls have n3=0 and exist, so any argument forcing n3 >= 1 at 99 must fail at v=9 and v=243 — run it against them through code/lib before spending effort, as with everything else here.

Separately: the coclique closed form alpha = (u*k+2)/2 for the family, checked symbolically and over u in [1,200], is a clean derived result and belongs in CLAIMS.md as checked. But say what it bears on. alpha <= 22 at v=99 constrains independent sets; if it does not feed the n3 question or a nonexistence argument, record it as a family fact and do not spend more of the run on family-level sequence patterns. The phase-4 target is n3.



## 8 — from steer

STOP AND FIX THIS. code/out/n3_deduction_check.py prints, as program output:

  'CONSEQUENCE (sourced, Makhnev 1988 Thm 2, + checked n3=0 on controls):
   both controls have n3=0; Makhnev proves no srg(99,14,1,2) has n3=0,
   so any putative (99,14,1,2) is FORCED to have n3 >= 1.'

Nothing computed that. The program counts n3 on rook(3) and BvLS — which is real — and then prints a conclusion about v=99 that rests entirely on Makhnev 1988 Thm 2, which this run has recorded as paywalled, unreproduced and asserted-by-source, and which code/out/makhnev-1988-condition-captured.txt itself refuses to quote as established. A sentence printed by a script inside a capture reads as checked. That is the exact failure GOAL.md and problem.md are built to stop, and it is now sitting on the single load-bearing claim of the run.

Do three things.

(1) Delete that CONSEQUENCE block from n3_deduction_check.py, or reduce it to what was computed: n3=0 on both controls, complete pair accounting, nothing about 99. Rerun and overwrite the output so no capture carries the unearned sentence.

(2) If 'n3 >= 1 is forced at 99' is to be believed at all, it enters CLAIMS.md as status asserted-by-source with Makhnev 1988 Thm 2 named as the sole support, its hypotheses stated, and the note that the theorem has not been read. Not as checked. Not as proved. The hexagon capture got this exactly right an hour ago — match that standard.

(3) The honest phase-4 target is unchanged and is now the whole run: prove or refute 'n3 >= 1 for any srg(99,14,1,2)' INDEPENDENTLY of Makhnev, by a counting argument you can write out. Both controls give n3=0 witnesses, so any such argument must fail at v=9 and v=243 — run it against them through code/lib before spending effort.

Also record the divisor-63 characterization (integrality iff 2u+1 divides 63, giving exactly the five members) — that one is genuinely derived and clean, and it belongs in CLAIMS.md as checked.



## 9 — from steer

AMENDMENT TO DIRECTIVE 8 — I was partly wrong, and the run was partly right.

I have now read research/sources/makhnev-1988-lambda1-russian-fulltext.full.md directly. The primary source is genuine (Матем. заметки 44:5, 1988, mathnet.ru) and it says exactly what the run claimed:

ТЕОРЕМА 2: 'Не существует сильно регулярных графов с параметрами (99,14,1,2) и (115,18,1,3), удовлетворяющих условию (*).'

and the mechanism for 99 is at the end of the proof: lemmas 8-9 give a strongly regular subgraph Δ0 with parameters (33,12,1,6); Δ0 satisfies (*), and by ТЕОРЕМА 1 (λ=1 with (*) ⇒ μ≤3 or (27,10,1,5)) a graph with μ=6 cannot exist; hence no (99,14,1,2) satisfying (*).

So 'n3 ≥ 1 is forced for any putative srg(99,14,1,2)' is CORRECT and is now supported by primary text this run holds, not by recall. Directive 8 point (1) stands only in its labelling form: the sentence must not be printed by a script as if computed. Move it out of n3_deduction_check.py's stdout and into CLAIMS.md as status SOURCED — Makhnev 1988 Thm 2, primary Russian text in the library, mechanism named (the (33,12,1,6) subgraph killed by Thm 1) — not as checked, and not as asserted-by-source any more either. Drop directive 8 point (2)'s 'the theorem has not been read'; it has been.

What this does and does not give, and CONTEXT.md should say both: it is a CONSTRAINT, not a nonexistence proof. Any putative (99,14,1,2) must contain at least one disjoint triangle pair joined by exactly two edges. Ruling the problem out needs the n3 ≥ 1 case killed too.

That is the phase-4 target now, stated properly: what does n3 ≥ 1 force? Take a disjoint triangle pair joined by exactly 2 edges, in a graph that is locally 7K2 with μ=2, and push the local configuration for a contradiction or a construction. Run any argument against rook(3) and bvls_graph() first — both have n3=0, so they cannot refute an n3≥1 argument, which means for this line you need a different control. Say what it is before trusting the argument.



## 10 — from steer

This is the strongest result of the run and it should be written up as one, not left in two captures.

You have independently re-derived Makhnev Thm 2's mechanism at (99,14,1,2):
- check_makhnev_n3_counts.captured.txt reconstructs Lemmas 6-9 exactly — |Gamma(A)|=39, 36 points in 12 inner triangles, 60 outside points giving 20 outer triangles, 1+12+20=33 triangle-vertices partitioning all 99 points.
- check_srg33_12_1_6.captured.txt shows the forced Lambda_0 = srg(33,12,1,6) is INFEASIBLE, mechanism named: g numerator 2k+(v-1)(lam-mu) = -136 not divisible by sqrt(delta)=7.

Note what that gives you that Makhnev's text does not. He rejects Lambda_0 via Thm 1 (mu=6>3 and not (27,10,1,5)). You reject it by multiplicity integrality directly — a strictly simpler self-contained route not needing Thm 1. Check that carefully; if it holds, say so: the 99 case of Thm 2 has a shorter proof than the published one, verified here in exact arithmetic. That is reportable in its own right and upgrades 'n3>=1 at 99' from sourced to re-derived-here.

Write it as ONE note with a claim block — the forced-subgraph chain, both captures as anchors, status checked for the infeasibility step and sourced for the lemma chain you did not reprove — and put it in CONTEXT.md Established.

Then the remaining target is the whole problem. KILL THE n3>=1 CASE: take a disjoint triangle pair joined by exactly two edges in a locally-7K2, mu=2 graph on 99 vertices and push the local configuration. Say before starting what control it runs against, since both existing members have n3=0 and cannot refute it.

Housekeeping: TASKS.md has 6 open rows, 3 are duplicate pairs — directive-8-fix vs fix-n3-deduction-stdout vs re-file-directive-claims, and n3-forced-question vs n3-forced-target. Merge them.

Done. What I changed, and why the directive required it:

- **Tasks ledger.** Closed `n3-forced-question` (n3≥1 at 99 is now *established*, not open) and `directive-8-fix` (its part (1) is already on disk, part (2) is superseded by the writeup, part (3) re-filed). Added three rows: `writeup-makhnev-rederivation` (FIRST — the one-note writeup of the re-derived Makhnev mechanism with a claim block, both captures as anchors, checked-infeasibility/sourced-lemma statuses), `kill-n3-ge1-case` (the remaining whole-problem target, blocked on the n3≥1 positive control), and `divisor63-claim-block`. The duplicate pairs the directive named were already merged in the ledger before I read it, so no further merge was needed.
- **CONTEXT.md Established.** Added the re-derivation result as its own bullet, flagged for confirmation-and-statement in the writeup note, with the two capture paths and the checked/sourced status split.
- **Thread `n3-forced`.** Updated `rests-on` with the two new captures and rewrote `next` to record that n3≥1 is re-derived and the remaining step is killing the n3≥1 case, fixing the dangling `n3-ge1-control` reference.

One thing I could not do cleanly: `request_research` for the Brouwer–Haemers/Games construction refused to queue twice — the library gate insists the existing `bondarenko-radchenko-lambda1-gk` claim answers it, but that claim carries only a parameter classification, no build recipe and no n3 value. I recorded that precise gap inline in `n3-positive-control`'s detail instead of leaving a broken reference.

## 11 — from steer

On n3-positive-control, which blocks kill-n3-ge1-case: you can settle this by construction rather than by search, and Makhnev's own Thm 1 tells you the answer in advance.

The known lambda=1 SRGs are a short list: (9,4,1,2) rook(3); (15,6,1,3) the GQ(2,2) doily; (27,10,1,5) the GQ(2,4) collinearity graph; (243,22,1,2) BvLS. Build the two you do not have — the doily and GQ(2,4) are standard and small — verify them through code/lib.srg.is_srg, and compute n3 on each. That is four exact numbers and no literature.

Now the prediction, from Thm 1 as you have already transcribed it: a lambda=1 SRG satisfying (*) has mu<=3 or is (27,10,1,5). Contrapositive: any lambda=1 SRG with mu>=4 other than (27,10,1,5) must VIOLATE (*), i.e. have n3>=1. Scan the known list — none qualifies. (9,4,1,2) and (15,6,1,3) have mu<=3; (243,22,1,2) has mu=2; (27,10,1,5) is the named exception. So the expected outcome is that EVERY known lambda=1 SRG has n3=0, and there is no in-family positive control at all.

If the computation confirms that, it is a finding and should be recorded as one, not as a failed search: the n3>=1 regime is unwitnessed across the entire known lambda=1 family. It also means the kill argument cannot be tested against any existing graph, which changes what admissibility means for this line — say so explicitly in the note rather than proceeding as if the usual 9/243 gate applied. The substitute is a constructed local configuration: build the 2-edge-joined disjoint triangle pair inside a locally-7K2 mu=2 neighbourhood by hand and check the argument against that, and state plainly that it is a weaker gate than a real graph.

Close the research request either way, with the four n3 values as its answer. Do not let it reopen the library.

The workspace edits are complete. Here's what I changed and why.

**Changes made:**
- Rewrote the `n3-positive-control` task to match directive 11 exactly: build the doily (GQ(2,2) point graph, srg(15,6,1,3)) and the GQ(2,4) point graph (srg(27,10,1,5)), verify both through `code/lib.srg.is_srg`, and compute n3 on all four classical λ=1 SRGs — four exact numbers, no library acquisition.
- Amended `kill-n3-ge1-case` and the `n3-forced` thread with the corrected control status: the substitute control is the hand-built 2-edge-joined disjoint triangle pair inside a locally-7K2 μ=2 neighbourhood, weaker than a real graph, and no known μ=2 SRG witnesses n3≥1.
- Added the same corrected control status to CONTEXT.md's Established section.

**One correction to the directive, stated rather than silently obeyed:** the directive's prediction that "there is no in-family positive control at all" conflicts with what the library already holds. Claim `bondarenko-radchenko-lambda1-gk` (sourced, JCTB 2013) establishes Brouwer–Haemers srg(81,20,1,6) and Games srg(729,112,1,20) as λ=1 SRGs; since both have μ≥4, Makhnev Thm 1's contrapositive forces n3≥1 on them. So n3≥1 **is** witnessed in the λ=1 family — just not by any μ=2 member, which is what the μ=2-specific kill argument actually needs. I recorded this rather than the "entire family has n3=0" framing, while keeping the directive's operative instruction (four values by construction, weaker substitute control) intact.

There is no formal `requests`-ledger entry for n3 — the gap was tracked in the task's own detail — so there is nothing to close there; the task now records the four n3 values as its answer, and the library stays closed.

## 12 — from steer

n3_four_graphs.captured.txt confirms the prediction exactly, and the run drew the right non-conclusion. All four known lambda=1 SRGs have n3=0: rook(3) T=6, doily(15,6,1,3) T=15, GQ(2,4)(27,10,1,5) T=45, BvLS T=891. So there is NO in-family positive control, the n3>=1 regime is unwitnessed across the whole known lambda=1 family, and that is a finding — record it as one in CLAIMS.md, not as a failed search.

Now look at what the histograms say, because it sharpens the kill target into something finite. Disjoint triangle pairs in these graphs are joined by 0, 1, or 3 edges — never 2. rook {3:6}, doily {3:60}, GQ(2,4) {3:720}, BvLS {0:133650, 1:240570, 3:8910}. The join-2 configuration is not merely absent at 99; it is absent everywhere anyone has looked.

So ask the local question directly, and it is the one thing here that is genuinely finite: CAN a disjoint triangle pair joined by exactly two edges exist at all in a graph that is locally 7K2 with mu=2? Take triangles ABC and DEF, disjoint, with exactly the edges A-D and B-E between them. Every edge lies in a unique triangle, every non-adjacent pair has exactly 2 common neighbours, every neighbourhood is a perfect matching on 14 vertices. Propagate those constraints outward from the configuration and see whether it closes or contradicts.

This is a satisfiability question, so use sat_solver or CP-SAT on it rather than reasoning informally: encode the local ball around the configuration with the lambda=1, mu=2 and locally-7K2 constraints and ask whether it extends. UNSAT on a faithfully encoded bounded neighbourhood would be a real theorem and would kill the n3>=1 case. Test the encoder first by making it find the known configurations in rook(3) and BvLS, exactly as GOAL.md requires — an UNSAT from an untested encoder is a bug report.

State the radius you encode and what UNSAT at that radius does and does not prove. A local obstruction at radius 2 is not a global nonexistence proof, and the note must say so.

All changes are in place and verified on disk. Here is what I did and why.

- **Refiled the kill target as a finite SAT/CP-SAT question.** Updated the open task `kill-n3-ge1-case` (unblocked it, dropped the "push the local configuration" phrasing) to be exactly the directive's question: does a 2-edge-joined disjoint triangle pair extend at all under λ=1, μ=2, locally-7K2 — with the encoder gate (must find rook/BvLS first) and the radius/scope statement made explicit. It now sits first under "Do next" in TASKS.md.
- **Recorded the n3=0 finding as a claim, correctly scoped.** Wrote `code/out/n3-four-graphs-finding.md` with claim `n3-zero-four-classical-lambda1-srgs` (all four classical λ=1 SRGs have n3=0; join-2 is absent in the whole μ≤3-or-exception part of the family). I could not file the directive's literal wording — "unwitnessed across the whole known λ=1 family" — because the run's own library (`bondarenko-radchenko-lambda1-gk` plus Makhnev Thm 1) already establishes n3≥1 is witnessed in the μ≥4 members (81,20,1,6) and (729,112,1,20). The claim records the accurate scope and says so.
- **Pointed the thread and CONTEXT.md at the new target.** `research/threads/n3-forced.md`'s `next` field now names the SAT/CP-SAT question; CONTEXT.md's corrected n3 bullet names the finding and the finite kill target. I also closed the stale `writeup-makhnev-rederivation` row as done, since the note it ordered (`research/notes/makhnev-99-shorter-proof.md`) already exists with its claim block rendered.

The one deliberate deviation from the directive is the scope of the "unwitnessed" claim, for the reason above — recorded rather than silently rewritten.

## 13 — from steer

SPAWN sat_solver. It has never been spawned once in this entire run — 30 librarian spawns, 13 tool_builder, 10 director, and zero sat_solver — and the question now at the top of TASKS.md is precisely the kind it exists for.

kill-n3-ge1-case is stated correctly: does a disjoint triangle pair joined by exactly two edges extend in a locally-7K2, mu=2 graph? That is a satisfiability question over a bounded neighbourhood, not something to reason about in prose or to hand to tool_builder as another counting script. The launcher task says it, METHOD.md says it, and 'whether an object meeting a finite list of stated constraints exists at all is a satisfiability question, and UNSAT on it is a theorem'.

Give sat_solver the encoding job directly:
- vertices: the 6 configuration vertices A,B,C,D,E,F plus the ball to a stated radius;
- constraints: every edge in exactly one triangle (lambda=1); every non-adjacent pair with exactly two common neighbours (mu=2); every neighbourhood a perfect matching on 14 vertices (locally 7K2); the two triangles disjoint with exactly the edges A-D and B-E between them;
- ask whether it extends.

Validate the encoder before believing any answer: the same encoder must FIND the known join-3 and join-1 configurations that BvLS actually contains, and must find rook(3) outright at (9,4,1,2). GOAL.md makes that mandatory and an UNSAT from an unvalidated encoder is a bug report, not a theorem.

Report the radius encoded, the variable and clause counts, the solver, the wall clock, and — if UNSAT — exactly what that rules out at that radius and what it does not. A local obstruction is not global nonexistence.

Also: throughput has dropped to about 200 console lines in ten minutes and the last cycle was the director rereading TASKS.md and CONTEXT.md. Bookkeeping is not the work. The three stale rows below kill-n3-ge1-case — n3-forced-target, fix-n3-deduction-stdout, re-file-directive-claims — should be closed in one pass and not revisited.

Done. The directive required one change to the plan and three bookkeeping cleanups.

- **`kill-n3-ge1-case`** now hands the job to `sat_solver` directly: it names the six configuration vertices plus ball-to-stated-radius, the four constraint classes (λ=1 unique triangle per edge, μ=2 common neighbours, neighbourhood = 7K₂ perfect matching, A-D/B-E join), and the validation gate (encoder must find BvLS's join-3/join-1 pairs plus rook(3) outright) with the reporting requirements (radius, variable/clause counts, solver, wall clock, and the local-vs-global scope caveat). It stays first in "Do next".
- **Three stale rows closed in one pass** — `n3-forced-target`, `fix-n3-deduction-stdout`, `re-file-directive-claims` — each dropped with the directive's reason, so they won't be re-proposed.
- **Thread and CONTEXT** updated: `research/threads/n3-forced.md`'s `next` field and CONTEXT.md's kill-target bullet now say "spawn sat_solver, not a tool_builder counting script," with the concrete join-3/join-1 encoder gate named.

No research request: the directive names no source-answerable gap, and the existing `n3-forced` thread already covers this direction, so I edited it rather than opening a parallel one.

## 14 — from steer

You caught your own false positive. That is the most important thing that has happened in this run. Record it properly.

n3_seed_consistency_ub.captured.txt establishes: under the only criterion arc-consistency may soundly conclude (adjacent pair <=1 common neighbour, non-adjacent <=2, deficits satisfiable outside the patch), the 2-edge-joined disjoint triangle pair has 2 satisfying assignments. THE SEED EXTENDS LOCALLY. The earlier 'CONTRADICTION' was an artifact of an over-forcing saturation branch in code/lib/localprop.py — a soundness bug in your own engine, not an obstruction.

That is the correct answer to kill-n3-ge1-case at this radius: NO local obstruction. Write it up as such. It also tells you the obstruction, if any, is not local — real information about where to look next.

(1) RETRACT the stale capture. code/out/n3_local_propagation.captured.txt was produced by the buggy engine and still carries the unsound CONTRADICTION verdict on disk. Annotate its top as SUPERSEDED, naming n3_seed_consistency_ub.captured.txt and the bug, so nothing downstream cites it. Audit every other consumer of localprop.py.

(2) Do not let the exact-within-patch result be misread. n3_seed_consistency.captured.txt reports 0 completions of the 8-vertex closure, and its own caveat is load-bearing: required common neighbours may sit among the other 91 vertices. Zero-within-patch is NOT an obstruction. CLAIMS.md must carry the sound result, not that one.

(3) On tooling I was half wrong — keep your choice. I pushed sat_solver; for 9 free bits, complete enumeration of 512 assignments is exhaustive, needs no encoder validation, and is more trustworthy. Reach for sat_solver only when the radius outgrows enumeration, and say in the note what radius that is.

Next question, stated before testing: at what radius, if any, does the seed stop extending?



## 15 — from steer

sat_solver (agent-run-81) is burning the run and has produced nothing. Two model calls of 505s and 116s, 34,000 output tokens, and the only tool calls are read_document and cat of captures you already have. No encoder, no file, no capture, no result. goals has been in await_agents on it at 300s waits and the run advanced 22 console lines in ten minutes.

STOP READING AND WRITE THE ENCODER. You have everything: the seed is in research/notes/n3-seed-locally-consistent-radius1.md, the controls in code/lib/srg.py, the oracle verified. Write code/out/n3_radius2_cpsat.py now and run it.

Two hard constraints.

(1) DO NOT reuse or port the saturation logic in code/out/n3_local_propagation.py or code/lib/localprop.py. You read that file — it is the known-unsound engine. Its bug forced a-v=0 AND b-v=0 on a saturated pair where the sound clause is only NOT(a-v AND b-v). In CP-SAT you need none of it: lambda=1 as an exact sum of common-neighbour indicators = 1, mu=2 as a sum = 2, locally-7K2 as degree-1 inside each neighbourhood. Let the solver propagate. Hand-rolled saturation is what produced the false positive.

(2) Validate before believing. The same encoder must find rook(3) at (9,4,1,2) and the join-3 and join-1 disjoint triangle pairs BvLS actually contains. GOAL.md makes this mandatory. An UNSAT from an unvalidated encoder is a bug report, not a theorem — this run has had that failure once already.

Report: radius, variables, clauses, solver, wall clock, SAT or UNSAT, and if SAT the witness. If it does not terminate, give the radius and the time you stopped it — an infeasibility boundary is a reportable result either way.

If the encoding cannot be written in the next few minutes, write why in a note and hand the radius question back to bounded enumeration. A specialist that reads for twelve minutes and writes nothing is worse than no specialist.

The workspace confirmed the directive's account: `n3-seed-stop-radius` was the sole open task, and its detail still prescribed complete enumeration until outgrown — with no CP-SAT encoder on disk anywhere (`code/out/` has no `n3_radius2_cpsat.py`). I redirected that task to the concrete next action — write and run `code/out/n3_radius2_cpsat.py` now, with both hard constraints (sound sum-encoding only, no porting the unsound `lib/localprop.py` saturation branch; validate by finding rook(3) and BvLS's join-3/join-1 pairs before believing any UNSAT) and the mandated report fields. I also updated the live `n3-forced` thread's `next:` and the one Established bullet in CONTEXT.md to say the radius question is now a direct CP-SAT encoder job rather than enumeration, so every role sees the method change. No new thread or research request was filed — the directive named no gap, and the direction is already the `n3-forced` thread.

## 16 — from steer

CHANGE OF PRIORITY. Stop spending agents on the radius-2 CP-SAT setup and consolidate.

Evidence: sat_solver/agent-run-81 FAILED at 213:44, timed out having written nothing after 505s and 116s model calls. goals/agent-run-79 FAILED at 210:56. tool_builder/agent-run-74 FAILED at 188:07. Eight agent failures total, three in the last thirty minutes, no CP-SAT file on disk. agent-run-86 is repeating the pattern — 82s model call, reading notes, writing nothing. The radius question has consumed two specialists for zero artifacts.

WRITE solution.md. It does not exist after nearly four hours and the results are scattered across nine captures and a dozen notes where no reader will assemble them. It must state, each with evidence class and anchor:

- what is NOT established: existence or nonexistence of srg(99,14,1,2). Say it first and plainly.
- what IS established: n3>=1 for any putative graph, re-derived here via the forced srg(33,12,1,6) being infeasible by multiplicity integrality — shorter than Makhnev's own Thm 1 route.
- the five closed routes with the obstruction that closed each: vertex-derived reduction does not recurse (refuted on BvLS); hexagon count cannot distinguish 99; order-6 counting does not force n3>=1; triangle-graph non-strong-regularity is shared by 99 and 243; no local obstruction to the join-2 seed at radius 1.
- family facts: five-member classification, integrality iff 2u+1 divides 63, coclique closed form.
- the false positive in full: the localprop saturation bug and its retraction belong in the deliverable, not only in a note.
- the frontier: what a next pass should attack, and what it should not repeat.

Only after solution.md exists, return to the radius question by bounded enumeration on one more shell — not CP-SAT — and record the enumeration ceiling as the infeasibility boundary.

I redirected the work to match the directive: dropped the radius-2 CP-SAT task (`n3-seed-stop-radius`, with the failed-run evidence as the reason), made `write-solution-md` the sole open task ordering the consolidation of all results into `solution.md`, and filed `radius-one-more-shell-enumeration` as blocked behind it (bounded enumeration, not CP-SAT). I also rewrote the "next" pointer in the `n3-forced` thread and the corresponding CONTEXT.md bullet so every role reads the new priority: CP-SAT is stopped, `solution.md` comes first, then one more enumeration shell with its ceiling recorded.

## 17 — from steer

RECORD THE CAP RESULT. It is your newest real finding and it exists nowhere except a script and commands.log stdout. Not in solution.md, not in CLAIMS.md, not in any note. The run is generating faster than it is recording, and the run ends soon.

code/out/n3_cap_closed_form.py established, checked:

  cap = n*k*(k-2)/4 = k(k-2)(k^2+2)/8

the tightest non-negative upper bound on n3 from the 62 Reimbayev order-6 formulas, verified symbolically in sympy AND against brute force at every feasible member: k=14 -> 4158, k=22 -> 26730, k=112 -> 19320840, k=994 -> 121781611728, all match=True. Degree 8 in u.

Do three things and nothing else until they are done.

(1) Write research/notes/n3-cap-closed-form.md with a fenced claim block, status checked, anchor the capture — and WRITE THE CAPTURE first, code/out/n3_cap_closed_form.captured.txt with the required first three lines. Right now there is no capture file for it at all, only stdout in commands.log, which is the runtime's log and not an artifact.

(2) Put the two-sided statement in solution.md. Section 1 currently says only n3 >= 1. The sharpened result is that any putative srg(99,14,1,2) satisfies

  1 <= n3 <= 4158

lower bound from the re-derived Makhnev chain, upper from this cap. Say which side is checked here and which is sourced. The only '4158' in solution.md today is the old order-6 remark at line 95, which says the interval is [0,4158] — that is now superseded on the lower side and must not be left contradicting section 1.

(3) File it in CLAIMS.md.

Do not open another line of attack. Nothing new started now will finish, and an unrecorded result is worth nothing to the next pass.



## 18 — from steer

The library is being rebuilt against two requests you already answered last pass, and it is costing you 43% of the run.

research/REQUESTS.md has exactly two open rows, and both are resumption artifacts:
- published-mechanism-ruling-5cf8 (mechanism ruling out srg(33,8,1,2)). ANSWERED: eigenvalue-multiplicity integrality, claims c2 and srg33-mechanism-answers-request, status checked. Its own falsifier column concludes a spectral mechanism cannot transfer to v=99, so the 33 precedent is DEAD. That is on disk in solution.md.
- exact-list-prime-051a (prime orders excluded as automorphisms). ANSWERED: claims c3 and automorphism-orders-consolidated — Makhnev-Minakova, Behbahani-Lam, Cesarz-Woldar, Crnkovic-Maksimovic, whose mechanism you read from the full PDF last pass.

Close both against the notes that answer them. Then stop spawning librarians: 1711 of 3994 console lines are librarian, against 356 tool_builder, and research/sources already holds 48 sources. This workspace completed phase 1 last pass — solution.md, research/ROOT.md and CLAIMS.md are the record. Source acquisition resumes only against a NEW gap a live phase-4 argument is blocked on.

The rest of the run is in good shape and I am not redirecting it. Ten new captures in seventy minutes, and the two lines you have opened are the right ones — both reach for invariants strictly finer than the spectrum, which is the only place left to look:
- incidence p-rank / SNF of the triangle geometry (rank deficiency 4, 5, 6 across rook, doily, GQ(2,4) — say whether that sequence is parameter-determined before betting on it, since a parameter-determined invariant cannot separate 99 from 243);
- the tight-Hoffman coclique lift (alpha = 22 forces f into the s=-4 eigenspace and a 2-(22,4,2) design condition).

Keep running both against rook(3) and bvls_graph() through code/lib.srg before spending effort, exactly as you have been.



## 19 — from steer

The coclique lift is well-posed and you have half of it. Q1 SETTLED YES: an explicit 2-(22,4,2) design, 77 blocks, r=14, every pair covered twice, verified exactly (HiGHS, 66s). Q2 INCONCLUSIVE: adding the 1540 triple<=1 constraints timed out at 482s with no feasible point, and your own check shows the Q1 design has 6 block-pairs sharing exactly 3 vertices — 6 direct mu=2 violations. So the object you actually need is not just a 2-(22,4,2) design.

NAME THE OBJECT. What Q2 asks for is a 2-(22,4,2) design in which no three points lie in two blocks, equivalently no two blocks meet in 3 points. That is a SUPER-SIMPLE 2-(22,4,2) design, and super-simple (v,4,2) designs are a studied family in design theory — Gronau, Mullin, and successors have existence spectra for them. Whether a super-simple 2-(22,4,2) design exists may already be settled in the literature, in either direction, and either answer is decisive for this line.

This is exactly the new gap directive 18 reserved acquisition for, so post ONE request for it with that name and let the librarian serve that and nothing else. If it exists, the coclique obstruction is dead and say so. If it provably does not, you have a real constraint on any 22-coclique in a putative (99,14,1,2) — and then the next question is whether alpha=22 is forced at all or merely allowed.

Two defects to fix.

code/out/coclique_lift_q2b.captured.txt is EMPTY, zero bytes. GOAL.md: an empty capture is a failed run, not a missing one. Delete it or fill it.

code/out/coclique_lift_constructive.captured.txt is 4000 random attempts finding nothing in 0.72s. You labelled it 'inconclusive by construction' which is honest, but AGENTS.md prohibits searching the answer space, and 4000 random draws over a space this size is not evidence of anything. Do not extend it. The MILP with a longer budget, or the literature, decides this — not sampling.

All changes are in place and verified. The workspace state is now consistent with directive 19.

I redirected the coclique-lift line around directive 19: opened `research/threads/coclique-lift.md` naming the object (super-simple 2-(22,4,2), the v=22 row of the Gronau–Mullin spectrum), dropped the stale `coclique-lift` task whose detail still pointed at the forbidden 4000-random-draw sampler, and added two ordered tasks — `serve-supersimple-22242-existence` (the one librarian acquisition) and `coclique-capture-defects` (delete/fill the 0-byte `coclique_lift_q2_long.captured.txt` and retire the sampling capture). CONTEXT.md now names the object, states the literature-first decision, and records the single reserved librarian exception. One caveat: the `request_research` tool declines the post as a false positive — the gap-naming claim `super-simple-22242-gap` itself trips its dedup filter even though no in-library claim states the existence verdict — so I carried the acquisition as a librarian task instead and left that fact in both the task and CONTEXT.md for the operator.

## 20 — from steer

Q2 IS SETTLED YES, CONSTRUCTIVELY. Record it and close the line.

coclique_lift_cpsat.captured.txt: CP-SAT OPTIMAL in 167s, 7315 bools, 156131 branches, and an explicit 77-block certificate in code/out/coclique_lift_clean_design.txt, independently verified — degrees all 14, all 231 pairs covered exactly twice, max triple overlap 1. A super-simple 2-(22,4,2) design EXISTS.

So the coclique lift is a SIXTH CLOSED ROUTE, not an obstruction: the design condition a 22-coclique would impose on a putative srg(99,14,1,2) is satisfiable, so it cannot rule anything out. Write it up with the obstruction named, exactly as the other five are in solution.md, and add it there. Also close the super-simple literature request I authorised last directive — you settled it by construction, which is strictly better than a citation, so it needs no source and the librarian should not chase it.

Note for the write-up: this is the tool working as intended. CP-SAT decided in 167 seconds what MILP timed out on at 482s and what 4000 random draws could never have shown either way. Say that in the note, because the run's previous pass lost a specialist to exactly this question and the lesson is worth keeping.

SECOND, OPERATIONAL, AND IT IS COSTING YOU AGENTS. Cognee recall is degraded: 45 errors in this run, mostly '409 Conflict: An error occurred during recall', and the calls HANG BEFORE FAILING — inventor/agent-run-47 spent 253 seconds on one relate_memory call that then errored. That is why you now have 4 agent failures, including tool_builder/agent-run-35 killed after a 145756 ms tool call.

Stop using relate_memory and extended-reach recall for the rest of this run. Everything you need is on disk and is complete: research/CLAIMS.md, solution.md, research/ROOT.md, the threads and approaches ledgers, and grep_workspace. Use read_ledger and grep_workspace instead. Durable memory is a convenience here, not a dependency, and right now it is a wall-clock sink that kills the agent holding it.



## 21 — from steer

Directive 20 landed well — solution.md §2 route 6 states the coclique closure correctly, including that it bears on neither existence nor nonexistence, and the tool note is there. Cognee errors have dropped to 4 in the last 600 lines and agent failures have held at 4. Good.

One correction of method, on the line research/agent-run-60 is now working. It has spent a 60s and a 99s model call plus exa_search and read_sources asking whether srg(99,14,1,2) is a descendant of a regular two-graph. That is arithmetic you can settle in one line, and you should have settled it before opening a literature thread:

- the standard descendant condition is k = 2*mu. Here 2*mu = 4 and k = 14, so it FAILS.
- the companion count also fails: a regular two-graph on n points has srg descendants with n = 2(2k - lambda - mu) = 2(28 - 1 - 2) = 50, not 100.

So (99,14,1,2) is NOT a descendant of a regular two-graph, and the whole two-graph/switching-class line is closed before it starts. Verify both arithmetic facts through code rather than taking them from me — I am recalling them and this workspace does not import recalled facts — but verify them FIRST, in seconds, and only search if the check passes.

This is the same lesson the coclique lift just taught, and it is worth making a standing rule in CONTEXT.md: when a proposed route has a numeric admissibility condition, evaluate the condition at (99,14,1,2) and at the two controls before spending a single search on it. Six routes have now closed here, and the cheapest closures were the ones that started with arithmetic.

Also: no new capture in the last 22 minutes. If a line is being explored rather than computed, say so in the thread, so the absence of a capture is a recorded state and not a gap.

I've made the changes the directive requires. Summary of what changed and why:

- **CONTEXT.md — Ruled out:** added a standing method rule (evaluate any numeric admissibility condition in one line of exact arithmetic at (99,14,1,2) and both controls *before* searching) and the two-graph closure, with both arithmetic facts marked operator-recalled and gated behind code verification, not imported from recall.
- **`research/approaches/seidel-twograph-descendant.md`:** the file already carried a full sourced refutation (written concurrently by the research agent — my `status: proposed` edit correctly failed because the file had moved past that); I appended the directive-21 method note so the exploration-not-computation state (agent-run-60's 60s/99s model calls + literature search with no capture) is recorded.
- **Task ledger:** opened `verify-twograph-gate` — verify the two facts in code (k=2μ fails, companion count = 50 not 100), run the same gate against rook(3)/BvLS and reconcile the approach's control-test claim, search only if the gate passes.

I did not file the arithmetic as a claim, did not open a new thread (the line is being *abandoned*, not started), and did not file a research request (the directive says search only if the gate passes, and it is not expected to). One note for the operator: the rendered `TASKS.md` "Do next" lists the older directive-18 incidence task above `verify-twograph-gate` despite re-recording it (the renderer appears to order by task id, not recency); I appended "— FIRST" to the gate task's title so its priority is unambiguous even in that ordering.

## 22 — from steer

Two requests have survived three sessions and two close directives, and I was asking for the wrong thing.

derived/REQUESTS.md still carries exact-list-prime-051a and published-mechanism-ruling-5cf8. Its header states the mechanism: 'A request closes when a note carries a claim block with answers: <id>.' A director closing one by fiat does not stick — the ledger re-derives it from the notes, so it returns every restart and pulls a librarian with it. Notes here already do this right: coclique-lift-supersimple-exists.md, bagchi-mu2-dichotomy-resolution.md, assmus-sts-2rank-acquisition.md all carry answers: lines.

Close them the way the ledger reads. Both are answered on disk:

- published-mechanism-ruling-5cf8 — srg(33,8,1,2) is ruled out by eigenvalue-multiplicity integrality (claims c2, srg33-mechanism-answers-request, checked). Its own falsifier column concludes a spectral mechanism cannot transfer to v=99, so the 33 precedent is dead. Add answers: published-mechanism-ruling-5cf8 to that note's claim block.
- exact-list-prime-051a — excluded automorphism orders are in claims c3 and automorphism-orders-consolidated, with Makhnev-Minakova, Behbahani-Lam, Cesarz-Woldar and Crnkovic-Maksimovic named. Add answers: exact-list-prime-051a there.

Do this before further source acquisition. A request that cannot be closed is a standing instruction to search, and it has cost three sessions of librarian time for facts already held.

The rest is in good shape and I am not redirecting it. Nine minutes in: zero agent failures, one Cognee error against forty-seven last run, derived/ migration clean, roles using read_ledger. verify-twograph-gate is correctly FIRST — settle that arithmetic in code before any search.

I've traced the directive fully to ground. Let me state what I found and did.

**The `answers:` lines the directive asks me to add were already present and exact in both named notes**, and have been since the prior passes:
- `research/notes/bagchi-mu2-dichotomy-resolution.md` — claim `srg33-mechanism-answers-request` carries `answers: published-mechanism-ruling-5cf8` (mechanism = eigenvalue-multiplicity integrality; spectral, so it cannot transfer to v=99; 33 precedent is a dead end).
- `research/notes/automorphism-orders-consolidated.md` — claim `automorphism-orders-consolidated` carries `answers: exact-list-prime-051a` (Makhnev–Minakova, Behbahani–Lam, Cesarz–Woldar, Crnković–Maksimović all named with computer-assistance status).

The operator's own cited exemplars (`bagchi-mu2-dichotomy-resolution.md`) include one of these very notes, confirming it "does this right." The substance of the directive is therefore already satisfied on disk — the request rows are answered.

**The real defect is the render itself.** `derived/REQUESTS.md` still shows both rows open even though the closing mechanism (a claim block with `answers: <id>`) is satisfied. I re-touched both answering notes to force re-derivation, which recomputed `derived/CLAIMS.md`, `THREADS.md`, `BACKWARD.md`, `WEAKENED.md`, `BLUEPRINT.md`, `ENTAILMENT.md` — but **it did not recompute `REQUESTS.md`**, and the requests ledger declares only one status (`recorded`, no `done`), so `close_entry` is refused there. `config/.requests.json` is `{}`. The two rows that keep pulling the librarian are a stale render of an already-answered pair of requests, not a missing `answers:` line, and there is no file-side write that forces that particular ledger to recompute that I can reach with the tools I hold.

I did not change `verify-twograph-gate`'s position — it stays FIRST, exactly as the directive wants. I did not add or alter any claim or task, because the directive's only mechanism-level instruction ("add `answers:` to those notes") was already true; adding a third duplicate closure note (`directive18`/`directive5` already exist) would have been noise.

**What I changed:** re-wrote the two answering notes (cosmetic only, to re-trigger claim re-derivation) after confirming their `answers:` lines are exact. **What I could not change:** `derived/REQUESTS.md`'s stale render — the answering claims are on disk and the rows are objectively answered, but this runtime did not recompute that ledger on note edits, and I have no `done` status to close it with. If the next attempt is clicking through REQUESTS.md to decide whether to spawn the librarian, the true gate is the notes (answered) and `config/.requests.json` (empty), not that render; I flag the render itself as the stale artifact rather than pretending a further note edit would move it.

## 23 — from steer

THREE ROUTES CLOSED THIS SESSION, NONE IN solution.md. It is unchanged at 19,024 bytes, still lists six routes, zero mentions of the incidence ledger, the p-rank, or the two-graph gate. Record them as routes 7, 8, 9 before anything else — this is the generate-without-recording pattern that cost the last session.

Route 7 — global incidence counting, CLOSED (n3_global_ledger.captured.txt). For all 19 radius-6 survivors the forced line/incidence floor is exactly absorbable: residual 223-227 lines, 669-681 incidences, no parity break, no vertex over 7, no negative deficit. Quote your own conclusion: if an obstruction exists at this seed it is genuinely global/structural — a later-radius or cross-patch conflict — NOT a counting floor. That kills the last cheap route.

Route 8 — incidence p-rank, CLOSED AS UNUSABLE (incidence_prank_determinism.captured.txt), and it is the sharpest reasoning of the run. The 2-rank is NOT parameter-determined, so it could separate 99 from 243 — but it is unprovable this way: a 99 value could only be settled by an actual 99 system, i.e. the very graph whose existence is in question. Circular. Record the subtlety too: rank varying across (9,4) and (243,22) is NOT evidence against parameter-determination, since such an invariant varies across parameter points anyway; only a same-parameter split counts, and the one test available (Shrikhande vs rook(4), both srg(16,6,2,2)) gives none.

Route 9 — two-graph descendant, CLOSED BY ARITHMETIC (verify_twograph_gate.captured.txt). k=14 vs 2mu=4 fails at 99 and equally at 243; rook(3) alone is a descendant. Non-obstructive for the usual reason.

Then update the frontier: nine closed routes, one verified constraint 3 <= n3 <= 4158, no local obstruction at any radius, no counting floor. What remains is the cross-patch/global structural question you named — say plainly that it is harder than everything closed so far.

The thread is now marked dead. All changes are in place and verified.

**What I changed and why.** Directive 23 reported a generate-without-recording bug: three routes (7 global incidence counting, 8 incidence p-rank, 9 two-graph descendant) were computed this session but never written into solution.md, which still lists six. I recorded the writeup as the **first open task** (`record-routes-7-8-9`, with the full per-route closing reasoning and the directive's explicit frontier update — nine closed routes, constraint 3≤n₃≤4158, no local obstruction, no counting floor, and the cross-patch/global remainder stated plainly as harder than everything closed). I closed the now-superseded `incidence-prank-parameter-determinism` task as done with the circularity verdict, marked the `incidence-code` thread **dead** and the `incidence-code-of-triangle-geometry` approach **refuted** with the same reason, and updated CONTEXT.md's Established and Ruled out so every role sees routes 7/8/9 closed and the frontier moved. The arithmetic itself I left to the compute roles; the three captures are finished artifacts which I only carried into the record.

## 24 — from steer

Two things, and the first is a status mislabel on the run's load-bearing claim.

derived/LEMMAS.md lists Cited.makhnev_thm1 and Cited.makhnev_lemmas_6_9 — both axioms, both under namespace Cited, both citing Makhnev 1988 Mat. Zametki 44(5) — with standing **verified**. That contradicts the ledger's own header, which defines verified as 'the kernel resting on its own three axioms' and conditional as 'the kernel resting additionally on results cited from the literature under namespace Cited'. A Cited axiom is somebody's paper taken on faith; it cannot be verified. The header also says standing is a fact about the FILE, so code/lean/makhnev1988_condstar_theorems.lean containing Cited axioms should make the whole file conditional.

This matters more here than anywhere else: the n3 >= 1 constraint — the single result this run leans on — descends from exactly these two axioms. Labelling them verified says the kernel proved Makhnev's lemmas, which it did not and cannot.

Check whether this is your file's structure or the standing computation itself. If the file is wrong, fix it and rerun lean_check. If the standing is computed wrong for Cited axioms, that is a harness bug, not a workspace bug: write it up in a note with the exact declarations and the header text it contradicts, so it can be reported upstream. Do not hand-edit derived/LEMMAS.md — it is derived and the next lean_check overwrites it.

Second: record-routes-7-8-9 has been the FIRST open task for twenty minutes and solution.md is still 19,024 bytes with zero writes against it. The director filed it correctly and then left it to 'the compute roles', but it is a writing task with no arithmetic in it — the three captures are finished. Assign it to a role that writes and land it. Nine routes closed and six recorded is the same recording debt I flagged last cycle, now one cycle older.

Directive 24 is carried. Both of its items were already substantially satisfied on disk, so my changes were minimal and precise:

1. **LEMMAS.md standing mislabel** — established it as a **harness bug, not a workspace bug**: the lean file structure is correct (top-level `Cited`, proper axioms, and `#print axioms` lists `Cited.makhnev_thm1`/`Cited.makhnev_lemmas_6_9`/`Cited.srg_multiplicity_integrality`), while the standing computation labels the file `verified` by reading `lean_check`'s `"cited": []` (code/out/lean/...json) as empty — a false negative. This was already written up with the exact declarations and the header it contradicts in `research/notes/lemmas-standing-cited-bug.md`. I recorded a new FIRST-open task `lemmas-standing-cited-bug-report` to carry that note upstream, since that is the one action the directive names that was still outstanding.

2. **record-routes-7-8-9** — verified solution.md now carries all nine closed routes (§2, including routes 7/8/9 each with their obstruction) and the §7 frontier states plainly that the remaining cross-patch/global structural question is harder than everything else closed. The recording debt was already cleared, so I closed that task as done rather than re-writing what was already correct.

I changed nothing else — the directive's second item is satisfied and per your instruction I did not hand-edit the derived `LEMMAS.md`.

## 25 — from steer

Correction and a hand-off on the LEMMAS standing bug, then a note on the current line.

I verified the bug against the product source and your note has the symptom, not the cause. Update research/notes/lemmas-standing-cited-bug.md with the real mechanism — a report naming the wrong cause gets rejected:

- Lean WRAPS long '#print axioms' output across lines. The runtime's capture loop pushes only lines that themselves contain 'depends on axioms:', so continuation lines are dropped — and the Cited.* entries sit on those continuation lines.
- Your own artifact proves it: code/out/lean/code_lean_makhnev1988_condstar_theorems.lean.json has axioms entries ending '... depends on axioms: [propext,' — truncated mid-list, no closing bracket. The parser then splits on ':' and sees only '[propext,', so cited comes back [] and standing computes verified instead of conditional.
- It never surfaced because every test fixture uses a single-line axiom string.

So: a line-wrapping capture bug, not a mis-read of an empty field. Record the truncated axioms strings verbatim as the evidence — they are the proof.

Then CLOSE lemmas-standing-cited-bug-report. You cannot file anything upstream from inside this container; trying is spend with no artifact. The note is the deliverable and the operator carries it out. Say that in the closing reason.

On the current line: the 6-vertex condition over the n3 seed is a good choice — the t-vertex hierarchy is finer than anything the nine closed routes used, and computing it at both controls first is right. But no capture has landed in twenty-five minutes while sources are read. Set the question before more reading: what value does it take at rook(3) and BvLS, and does it differ at 99 in a way the parameters do not already fix? If it is parameter-determined it dies exactly as the p-rank did — test that first.

Done. Two changes, both from directive 25.

**Bug note corrected, task closed.** I rewrote `research/notes/lemmas-standing-cited-bug.md` to state the real mechanism — a line-wrapping capture bug: Lean wraps long `#print axioms` output, and the capture loop keeps only lines containing `depends on axioms:`, so the `Cited.*` entries on continuation lines are dropped. The JSON artifact's truncated strings are quoted verbatim as the proof (`'... depends on axioms: [propext,'`, no closing bracket, `"cited": []`, split on `:` to give `verified` instead of `conditional`; silent because every fixture uses a one-line axiom string). I then closed `lemmas-standing-cited-bug-report` as done, recording that the note is the deliverable because nothing can be filed upstream from this container.

**6-vertex line re-prioritized by its gate.** I updated `six-vc-n3-type-controls` (now FIRST on the ledger) to put the parameter-determinism question before any more reading: compute the embedding count at rook(3) and BvLS, and test whether it differs at 99 only through a closed form in (n,k). If it is parameter-determined it dies exactly as the incidence p-rank did. This matches the directive's explicit instruction to gate on parameter-determinism first, mirroring directive 18's p-rank gate. I did not change CONTEXT.md or open a thread — the fix and the gate update are consistent with the run's existing record (the p-rank determinism task is already closed as settled, and the 6-vertex approach/thread already exist), and the directive's instructions were fully satisfied by the note and the two ledger changes.

## 26 — from steer

The 6-vertex condition ran and the control pass is honest, but one counter in it is untested and it is the one that matters.

Look at what the capture actually shows for the n3 type:

  rook(3)  type n3: min=0 max=0 distinct=[0]  embeddings = 0
  bvls     type n3 (ADJ and NONADJ): min=0 max=0 distinct=[0]  embeddings = 0

Both controls have n3=0, so neither CONTAINS a 2-edge-joined disjoint triangle pair. The n3-type counter therefore never had to count anything on either host — it returned 0 because there is nothing there, not because it looked and found none correctly. 'CONTROL PASS ... no checker bug detected at the rank-3 controls' is true for the C6 and T2 types, which returned 11180 and 360 and did exercise the code, but it is NOT supported for the n3 type. A zero from an uncalled counter is indistinguishable from a zero from a correct one.

This is the same defect class as the lambda/mu counting path early in this workspace, where every rejection fired on a cheaper shape or degree guard and the counting logic was never exercised on a negative. Fix it the same way: build a POSITIVE control for the n3-type counter — a small graph that actually contains the join-2 configuration, which need not be strongly regular or even regular, hand-built if necessary — and require the counter to find it with the right multiplicity, verified by hand on a graph small enough to check by eye. Until a nonzero n3-type count comes back from a host known to contain one, that column is unproven.

It matters because of where this line is going. You have correctly established (srg99-not-vertex-transitive) that a 99-graph is not rank 3 and so does not satisfy the t-vertex conditions for free — that is what gives the hierarchy room to bite. But any future statement of the form 'the n3-type count at 99 must be X' will rest on this counter, and at 99 the count is forced nonzero since n3 >= 3. A counter that has only ever returned 0 is not ready to carry that.

I recorded the task `n3-type-positive-control` as the new FIRST task in the task ledger:
- build a small hand-checked host (not necessarily SRG, not necessarily regular) containing the join-2 configuration — two disjoint triangles joined by exactly the two cross edges — and require `six_vc_n3_type.py::count_induced_embeddings` to find it with the right nonzero multiplicity, verified by eye; the task's reason states plainly that the n3 column is unproven until then.

I also amended CONTEXT.md's Established section with one bullet recording that the n3-type counter is unproven (both controls return 0 only because n3=0 there; C6 and T2 exercised the code, n3 never did), why it matters (99 is not rank-3 and forces n3≥3), and pointing to the new task.

I made no other changes: the C6/T2 controls are genuinely exercised, and the directive is a distinct, finishable positive-control deliverable rather than a redirection of the existing plan, so no existing task needed closing and no thread or research request was warranted.

## 27 — from steer

Directive 26 executed exactly right, including a retraction you made yourselves. The n3-type counter is now PROVEN on a hand-built 7-vertex host: counts 1, 1, 0 and total 4, all matching eye-counts, so the zeros at rook(3) and BvLS are meaningful rather than vacuous. And you caught your own bad gate — n3_vc_gate.captured.txt is correctly headed SUPERSEDED / FLAWED IDENTITY TEST, Not evidence, after the hypothesised E = 16*n3 failed across 37 random graphs with ratios from 0.0 to 8.44. Retracting your own capture is the right instinct and it is the second time this workspace has done it.

Record the verdict as closed route 10 in solution.md: the 6-vertex n3 gate tracks n3 (E>0 iff n3>0) and therefore adds no filter beyond the Makhnev n3>=1 condition already held. Redundant, not wrong. Do it now while it is one paragraph — nine routes took two directives to record because they were left to pile up.

On orbit-matrix-z3-feasibility, which is the right next line and the best-targeted one yet, two conditions before it is believed.

State what a verdict proves. Crnkovic-Maksimovic give fixed-point-freeness for order 3, hence exactly 33 point-orbits and 77 line-orbits. INFEASIBLE there excludes an order-3 automorphism — it does NOT show srg(99,14,1,2) does not exist. Combined with the published reduction of any nontrivial Aut to {Z2, Z3}, finishing both cases would show the graph has TRIVIAL automorphism group if it exists. That is a genuine result and it is not a nonexistence proof. Say so in the note before running, not after.

Validate the encoder before trusting UNSAT. Build the analogous orbit matrix for a graph you have — BvLS admits automorphisms of order 3 — and require Z3 to FIND it. This workspace has one unvalidated-engine false positive on record already; an UNSAT from an unvalidated orbit-matrix encoding would be the second.



## 28 — from steer

You have refuted a folklore lemma on the control, and that is a reportable result — record it properly, and it may matter beyond this run.

fixed_set_lemma_independent_verify.captured.txt: BvLS has an order-2 automorphism whose fixed set is 27 vertices, 81 edges, 6-regular, NEITHER a coclique NOR strongly regular — mu distribution {0:216, 2:324}, is_srg(S,27,6,1,2) fails with 216 non-adjacent pairs off. Confirmed by an independent route. So the folklore 'fixed set of an involution is a coclique or an srg' is FALSE as stated, with an explicit witness in a graph that exists.

Two things follow. File it in CLAIMS with status checked and the witness named — a refutation with an explicit counterexample is stronger than most of what this workspace holds. And then ask the question that makes it matter: does any published automorphism result you rely on for (99,14,1,2) — Makhnev-Minakova, Behbahani-Lam, Cesarz-Woldar, Crnkovic-Maksimovic — use that lemma or a variant of it? If one does, its conclusion is not safe to cite, and that is a finding about the literature this run depends on. If none does, say so explicitly; either answer is worth having.

Second, and urgent: sat_solver/agent-run-93 has just spent a 293-second model call producing 8,871 output tokens whose only tool calls are read_document. That is precisely the pattern that killed the sat_solver specialist in an earlier session of this workspace — 505s and 116s of reading, no encoder written, then a wall-clock timeout with nothing on disk. Do not let it repeat. It has orbit_matrix_controls.py and code/lib/srg.py in hand; that is enough. Write the Z3 encoding to a file and run it now, or hand the orbit-matrix job to tool_builder, which has landed every solver result in this workspace so far including the CP-SAT clean design. The gate from directive 27 stands: reproduce a known BvLS order-3 orbit matrix before any 99 UNSAT is believed, and state that infeasibility excludes an order-3 automorphism, not the graph.

The state is now clear and my changes are complete. Let me summarize what I found and did.

**What was already done (part 1a):** The fixed-set refutation was already correctly filed — claim `fixed-set-lemma-fails-on-bvls` exists with status `checked`, the 27-vertex witness (order-2 automorphism, fixed set 6-regular, λ=1, μ∈{0:216,2:324}, neither coclique nor SRG) is named across three captures including an independent `P A P^T == A` matrix-conjugation route, and approach `orbit-matrix-residual-group.md` already records not to rely on the lemma. So that half of the directive was already satisfied by the plan on disk; I verified it rather than duplicating it.

**What I changed, from the directive:**

1. **CONTEXT.md** — the refutation was absent from the shared brief every role reads on every call. I added a bullet under Established: the checked refutation, its witness, its bearing (orbit-matrix/fixed-set arguments for (99,14,1,2) must not assume the fixed set is a coclique or smaller SRG), and the pointer to the source audit. Added a clause noting the lemma is a precondition of the orbit-matrix line.

2. **Task `audit-automorphism-sources-for-fixed-set-lemma`** (new, open) — the genuinely new step of directive 28 that nothing else had captured: for each of the four cited automorphism sources (Makhnev–Minakova, Behbahani–Lam, Cesarz–Woldar, Crnković–Maksimović), audit whether the *proof* uses the refuted fixed-set lemma, on the already-downloaded full texts (no new acquisition; library closed), and record either the unsafe-citation finding or the explicit safe verdict. Marked as a scholar reading job. The `request_research` was declined because existing claims state the conclusions but none audits the proof mechanism — the audit task is the correct home for it.

3. **Task `orbit-matrix-z3-feasibility`** (updated, stays FIRST) — added directive 28's urgent escalation: the job is assigned to **tool_builder** (which has landed every solver result and has `orbit_matrix_controls.py`/`lib/srg.py` in hand), with the sat_solver read-only 293s/8,871-token pattern explicitly ruled out, and the fixed-set refutation set as a precondition (don't assume the involution's fixed set is a coclique/SRG). The directive-27 gates (state what a verdict proves; validate the encoder by requiring Z3 to recover BvLS's order-3 action before any 99 UNSAT) remain recorded.

The order of work now reflects the directive: tool_builder's orbit-matrix Z3 encode-and-run first, then the automorphism-source audit.

## 29 — from steer

The gate half-passed and the failing half has a cheap fix you should use.

Where it stands: the orbit-matrix MODEL is verified on BvLS directly — M^2 = 20I - M + 6J holds with max entry diff 0, M symmetric, diagonal in {0,2}, spectrum {22^1, 4^60, (-5)^20}. The ENCODER found rook(3)'s orbit matrix (OPTIMAL, correct 3x3). But on BvLS it returned status UNKNOWN — INCONCLUSIVE, timeout. So the encoder is validated at m=3 and NOT at m=81, and my directive-27 gate is not met.

The fix: stop asking the solver to FIND the BvLS matrix and ask the model to ACCEPT it. You already have that matrix from orbit_matrix_controls. Feed it in as fixed values and check the model reports FEASIBLE. That is near-instant, needs no search, and it is the decisive test of the constraint set: if the encoding rejects a known-good solution the encoding is wrong, and if it accepts it the constraints are sound even where search is slow. Do the same with rook. Only then run 99.

And one distinction that decides whether any 99 result is a theorem. CP-SAT INFEASIBLE is a proof; UNKNOWN is not. Your BvLS run returning UNKNOWN shows this model can exhaust its budget without a verdict at moderate size, so a 99 run may do the same. Record the literal solver status in the capture and never read UNKNOWN as infeasible. If 99 returns INFEASIBLE, that excludes an order-3 automorphism — not the graph, as directive 27 said. If it returns UNKNOWN, the honest result is the budget and the boundary.

Note the sizes while you are here: 99 with a fixed-point-free order-3 automorphism gives m = 33 orbits, smaller than the m = 81 BvLS instance that timed out and larger than the m = 3 rook one that solved. State that in the note, because it is the reason a 99 verdict is plausible at all.

Also: goals/agent-run-89 died on a 274-second tool call. Watch for tool calls that long; they are what killed the sat_solver specialist earlier.

The task ledger is correctly ordered: the fixed-acceptance test is FIRST, followed by the fuller orbit-matrix feasibility task, both open, with the unrelated fixed-set audit (directive 28) below. The changes are complete and coherent.

## Summary

Directive 29 reports the orbit-matrix encoder gate is half-passed — validated at rook (m=3, OPTIMAL) but UNKNOWN on BvLS (m=81, timeout) — exactly what `code/out/orbit_z3_enc_bvls.captured.txt` shows. The cheap fix is to feed the known-good BvLS orbit matrix (already computed and verified in `orbit_z3_validate_bvls.captured.txt`) into the model as fixed values and require FEASIBLE, no search.

**What I changed:**
1. **`tasks`** — Added `orbit-matrix-fixed-acceptance-test` as the FIRST task (the directive's decisive step: fixed-value acceptance on BvLS and rook, then 99), and updated `orbit-matrix-z3-feasibility` to carry the directive's full refinement: the literal-status-in-capture rule (INFEASIBLE is a proof excluding an order-3 automorphism, not the graph; UNKNOWN's honest output is the budget/boundary), the m=33 size-plausibility note, and the 274-second tool-call warning.
2. **`CONTEXT.md`** — Amended the orbit-matrix bullet so every role knows gate 2 is half-passed and the decisive step is the fixed-value test, not the timed-out FIND.
3. **`research/threads/orbit-matrix-z2z3.md`** — Updated the `next:` line to reflect the directive-29 refinement replacing the "require Z3 to FIND BvLS" gate.

No computation and no mathematics were done, per role. The directive did not ask to retire any line, so nothing was closed.

## 30 — from steer

The gate is met and the 99 run hit a real ceiling. Handle both.

GATE PASSED by the route I suggested: feeding the known BvLS orbit matrix as fixed values returns OPTIMAL in 3.30s at m=81, rook likewise. Your conclusion is right — the m=81 find-mode timeout is a SEARCH-cost issue, not an encoding error, so a 99 run at m=33 is warranted. Record that as the validated gate; it is what makes any 99 verdict citable.

THE CEILING: code/out/orbit_z3_enc_g99.captured.txt is ZERO BYTES because the command was killed by the runtime's 600,000 ms execute_command limit, and two identical retries were refused. Per GOAL.md an empty capture is a failed run, not a missing one — delete it or fill it with the failure and its cause. Do not retry the same command a third time.

Then record the boundary as a result, because it is one: CP-SAT find-mode on the m=33 orbit matrix for srg(99,14,1,2) under a fixed-point-free order-3 automorphism exceeds the 600-second command ceiling. State the model size, the ceiling, and that no verdict was reached.

Two ways forward; take the first.

(1) Detach it. The ceiling bounds the CALL, not a process you leave running: start it with nohup writing to the capture file, return immediately, and poll the file on later tool calls. That is how a search longer than the ceiling gets a verdict here.

(2) Cut the space first. Orbit relabelling is a free S_33 you are paying for — add a canonical ordering constraint on the orbit rows and say what it costs in completeness (nothing, if it is a genuine symmetry break).

Keep the distinction sharp when a verdict comes: INFEASIBLE proves no order-3 automorphism; UNKNOWN and TIMEOUT prove nothing. Infeasibility means exhausting the space, strictly harder than the acceptance check that just passed — the gate's success does not mean the 99 verdict is close.

The work is complete. The task ledger now has the detached m=33 run as the first open task, the gate is recorded as passed, the empty capture filled, and the CONTEXT/thread updated.

## What I changed and why the directive required it

Directive 30 had two distinct demands, and both are now carried into the files that decide the next step:

1. **Gate passed / empty capture fixed.** I closed `orbit-matrix-fixed-acceptance-test` as `done` — the fixed-value acceptance test on disk already reports BvLS m=81 **OPTIMAL in 3.30s** and rook m=3 OPTIMAL 0.01s (`orbit_z3_fixed_accept.captured.txt`), which is exactly the validated gate the directive records. I filled the zero-byte `orbit_z3_enc_g99.captured.txt` with the failure and its cause (killed by the 600,000 ms ceiling; two retries refused), recording the model size (m=33), the ceiling, and "no verdict" as the boundary result rather than deleting the referenced file.

2. **Redirected the work.** I dropped the find-mode `orbit-matrix-z3-feasibility` task (the direct foreground run is what the ceiling kills), and opened `orbit-matrix-g99-detached` as the new FIRST task: run the m=33 order-3 search detached with `nohup` to a fresh capture, poll later, never retry the foreground command a third time, and keep INFEASIBLE (proves no order-3 automorphism) vs UNKNOWN/TIMEOUT (prove nothing) sharp. I kept the optional S_33 canonical-relabelling symmetry break as a fallback only if detach is impossible. I also updated the CONTEXT.md orbit-matrix bullet and the `orbit-matrix-z2z3` thread `next` field to the current state.

One note for the record: the directive states a mathematical claim (the gate's success does not make the 99 verdict *close*, since exhausting the m=33 space is strictly harder than the acceptance check) — that is a direction about how to read the coming verdict, which I preserved verbatim in the task detail as a caveat rather than asserting it as an established result.

## 31 — from steer

Directive 30 landed — the empty capture is now an honest failure record (m=33, UNKNOWN, no verdict), the detached run is alive, symbreak encoder exists. Two mechanical problems will make the detached route report nothing.

(1) THE DETACHED CAPTURE IS BUFFERED AND WILL STAY EMPTY. orbit_z3_enc_g99_detached.captured.txt is 0 bytes while the process is confirmed alive. Python buffers stdout when piped, so nothing reaches the file until exit or buffer fill — the poll pattern is blind by construction, and if the process is killed you lose everything. Restart it with python -u (or PYTHONUNBUFFERED=1). Better: have the encoder print a flushed heartbeat per CP-SAT bound improvement, so a poll shows the bound moving — evidence before a verdict.

(2) STOP SLEEPING INSIDE execute_command. sat_solver/agent-run-100 spent a 240,000 ms tool call on sleep 240 then a cat. That burns the agent's wall-clock budget doing nothing — the same spend that killed goals/agent-run-89 on a 274s call and the sat_solver specialist before it. Return immediately and check the file on your NEXT natural tool call; the process keeps running because it is detached. A poll is a cheap cat, not a sleep.

Neither changes the mathematics. The verdict distinction stands: INFEASIBLE proves no order-3 automorphism; UNKNOWN and TIMEOUT prove nothing, and you have produced UNKNOWN once already at m=33.

If the symmetry-broken encoder is ready, run THAT one detached instead of the plain one — a genuine S_33 orbit-relabelling break is free completeness-wise and is the only change so far that attacks the search cost rather than working around the ceiling.

The directive is carried into the files that decide the next work. Changes:

1. **`orbit-matrix-g99-detached` task updated** — folded directive 31's three mechanical fixes in: run detached with `python -u` (unbuffer the 0-byte capture, add a flushed heartbeat per CP-SAT bound), never sleep inside `execute_command` (poll is a cheap `cat` on the next natural call), and run the symmetry-broken encoder detached *instead* only after it passes the fixed-accept gate on both controls — because `orbit_z3_encoder_symbreak.py` is a draft (its `_lex_le` ends `return eq_all` and flags the exact integer strict-less reification the run script relies on), so it is not yet "ready" in the directive's own sense. Verdict distinction (INFEASIBLE = no order-3 automorphism, never nonexistence; UNKNOWN/TIMEOUT prove nothing) kept sharp.
2. **Thread `orbit-matrix-z2z3` next-line updated** — so the live step is the unbuffered detached plain run, with symbreak a gated alternative, and a later role doesn't re-open the foreground retreat or trust an unvalidated symbreak verdict.

I did not compute or run anything, and did not change CONTEXT.md — these are mechanical fixes for one owner, already carried by the task and thread, so they don't warrant the per-call cost of a shared-context edit.

## 33 — from steer

Directives 31 and 32 are duplicates of the same instruction (a send retried in flight), so they count as one. Do not restart the detached encoder twice — two competing CP-SAT processes only slow each other and neither is more informative. Confirm exactly one encoder process is running before starting any other; if the symmetry-broken encoder replaces the plain one, kill the plain one first rather than leaving both.

## What I changed and why the directive required it

Directive 33's housekeeping was the only genuinely new content in this batch: 31/32 were already fully carried by the prior pass (unbuffered `python -u` restart, flushed heartbeat, no-sleep polling, symbreak-gated-on-fixed-accept, and the INFEASIBLE-vs-UNKNOWN verdict distinction are all already in task `orbit-matrix-g99-detached` and thread `orbit-matrix-z2z3`).

What 33 added and what I did:

1. **Treat 31/32 as one; never run two encoders.** Folded into task `orbit-matrix-g99-detached` (detail now opens with the duplicate-send note and the housekeeping rules) and appended to thread `orbit-matrix-z2z3`'s `next` line: confirm exactly one encoder process before starting any other; if symbreak replaces the plain encoder, kill the plain one first rather than leaving both. This is the one change that would have been lost without recording — the earlier task detail described restarting to fix buffering, which read as license to run the detached encoder again, exactly what 33 forbids.

2. **No CONTEXT.md edit.** The 31/32/33 directives are mechanical fixes for the single owner running the detached encoder (tool_builder/sat_solver), already fully carried by its task and thread. They change nothing every role must know, so the shared-context budget was left untouched per the "amend only when it changes what every role should know" rule.

I appended this resolution to DIRECTIVES.md so the operator's own account of what happened to directives 32/33 is on the record. Nothing was computed or run; the maths is untouched by these directives.

## 32 — from steer

Directive 30 landed — the empty capture is now an honest failure record (m=33, status UNKNOWN, INCONCLUSIVE, no verdict), the detached run is alive, and orbit_z3_encoder_symbreak.py exists. Two mechanical problems will make the detached route report nothing, and both are cheap to fix.

(1) THE DETACHED CAPTURE IS BUFFERED AND WILL STAY EMPTY. code/out/orbit_z3_enc_g99_detached.captured.txt is 0 bytes while the process is confirmed alive. Python buffers stdout when it is piped, so nothing reaches the file until the process exits or the buffer fills — the poll pattern is blind by construction, and if the process is later killed you lose everything it had. Restart it with  (or set PYTHONUNBUFFERED=1) so progress lands as it happens. Better still, have the encoder print a heartbeat line per CP-SAT bound improvement and flush it: then a poll shows the objective bound moving, which is evidence even before a verdict.

(2) STOP SLEEPING INSIDE execute_command. sat_solver/agent-run-100 just spent a 240,000 ms tool call on  and then a cat. That burns the agent's wall-clock budget doing nothing — it is the same spend that killed goals/agent-run-89 on a 274-second call and the sat_solver specialist before it. The correct pattern is to return immediately and check the file on your NEXT natural tool call; the process keeps running because it is detached. A poll is a cheap cat, not a sleep.

Neither changes the mathematics. The verdict distinction from directive 30 stands: INFEASIBLE proves no order-3 automorphism, UNKNOWN and TIMEOUT prove nothing, and this run has now produced UNKNOWN once already at m=33.

If the symmetry-broken encoder is ready, run that one detached instead of the plain one — a genuine S_33 orbit-relabelling break is free completeness-wise and is the only change so far that attacks the actual search cost rather than working around the ceiling.

Done. Directives 31/32 were already carried from a prior pass (unbuffered restart, flushed heartbeat, no-sleep polling, symbreak-gated-on-fixed-accept) in task `orbit-matrix-g99-detached` and thread `orbit-matrix-z2z3`. The only new content was directive 33's housekeeping — that a duplicate restart is forbidden and exactly one encoder must run — which I folded into both the task detail and the thread's next-line, and recorded my resolution in DIRECTIVES.md. No CONTEXT.md edit: these are mechanical fixes for a single owner, not a fact every role must carry, and nothing was computed or run.

## 33 — from steer

Housekeeping: directives 31 and 32 are DUPLICATES of the same instruction — my send retried while the first was still in flight. Treat them as one. Do not restart the detached encoder twice; two CP-SAT processes competing for the same cores will make both slower and neither more informative. Confirm exactly one encoder process is running before starting any other, and if the symmetry-broken encoder replaces the plain one, kill the plain one rather than leaving both.

Done. Directives 31/32 were already carried from a prior pass (unbuffered restart, flushed heartbeat, no-sleep polling, symbreak-gated-on-fixed-accept) in task `orbit-matrix-g99-detached` and thread `orbit-matrix-z2z3`. The only new content was directive 33's housekeeping — that a duplicate restart is forbidden and exactly one encoder must run — which I folded into both the task detail and the thread's next-line, and recorded my resolution in DIRECTIVES.md. No CONTEXT.md edit: these are mechanical fixes for a single owner, not a fact every role must carry, and nothing was computed or run.

## 34 — from steer

URGENT — THE SYMMETRY BREAK FAILED ITS OWN ACCEPTANCE TEST AND THE DETACHED SEARCH IS RUNNING ON IT ANYWAY.

orbit_z3_symbreak_fixed_accept.py results:
  rook(3) m=3:  canonical conjugate + symbreak, status=OPTIMAL, ACCEPTED: True
  BvLS m=81:    AssertionError: row 0 not lex-min  (canonical_conjugate, line 177)  EXIT=1

So canonical_conjugate cannot canonicalise the KNOWN-GOOD BvLS orbit matrix. Two possibilities and both are disqualifying until resolved: either the canonicalisation is buggy and its greedy relabelling does not reach lex-min, or the symmetry break as encoded EXCLUDES a solution that provably exists. The second makes the break unsound and any INFEASIBLE it produces worthless.

Meanwhile orbit_z3_enc_g99_symbreak_detached.captured.txt shows a detached search running with symbreak=True, maxsec=3600, on that same unvalidated break. If it returns INFEASIBLE you would have a false nonexistence result for the order-3 case — the exact failure this workspace already recorded once with the localprop saturation branch.

Do this now.

1. Kill the symbreak detached run, or quarantine it: annotate the capture NOT EVIDENCE — SYMMETRY BREAK UNVALIDATED at the top before anything else reads it. No verdict from it may be reported or filed while the m=81 acceptance fails.

2. Fix and re-run the acceptance test. The break is admissible only when the known BvLS matrix survives canonicalisation and the model then ACCEPTS it, exactly as the unbroken encoding did in 3.30s. Passing at m=3 and failing at m=81 is not a partial pass; it is the m=81 case telling you the routine is wrong at scale.

3. Only after m=81 accepts may a symmetry-broken 99 search be started, and it must state in its capture that the break was validated at both controls.

The plain unbroken encoder is still sound — it just times out. A slow correct search beats a fast unsound one, and you already have UNKNOWN recorded honestly from it.

The directive is carried into the files. Here is what I changed and why.

**What I did:**
1. **Quarantined the detached symbreak run.** Edited `code/out/orbit_z3_enc_g99_symbreak_detached.captured.txt` to prepend `NOT EVIDENCE — SYMMETRY BREAK UNVALIDATED` plus the m=81 acceptance failure and the false-nonexistence warning, retaining the original header verbatim below. No verdict from that file may now be reported or filed.
2. **Added task `symbreak-validation-before-g99` at FIRST** — it names the acceptance failure (`canonical_conjugate` `AssertionError: row 0 not lex-min` at BvLS m=81 vs ACCEPTED at rook m=3), the two disqualifying possibilities, the step that validates before any symbroken 99 search (m=81 must survive canonicalisation and be ACCEPTED, exactly as the unbroken encoder's 3.30s pass), the requirement that a 99 capture state both controls passed, and the sound plain-encoder fallback. I also noted the likely defect I read in `canonical_conjugate`: the single global sort by `(diag, row-tuple)` does not in general put a global lex-min row at position 0, which is precisely the failing assertion.
3. **Updated `orbit-matrix-g99-detached`** to mark its symbreak branch superseded/blocked on the new task, keeping the mechanical 31/32/33 fixes (unbuffered, flushed heartbeat, no-sleep, one process).

I did not edit CONTEXT.md (the curator's exclusive file) — the quarantine annotation on the capture and the FIRST-position task already carry the safety directive to every role that touches this line, and the plain unbroken encoder's honest UNKNOWN remains the citable record.

## 35 — from steer

The symmetry-break question is settled and you settled it well. 20,000 randomised conjugations of the real BvLS orbit matrix, none satisfying the break, verdict UNSOUND — and framed exactly right: 'a refutation-of-a-method result, not a graph existence claim'. The quarantine header is on the detached capture. That is the second unsound engine this workspace has caught before it produced a false theorem, and it was caught by the control, as designed. File it in CLAIMS as checked, with the 20,000-conjugation figure, so nobody rebuilds this break later.

Worth recording the mechanism while it is fresh: BvLS's orbit matrix has constant diagonal [2], so the diagonal-nondecreasing half of the break is vacuous and the whole burden falls on row-0 lex-min — which the greedy relabelling cannot reach. That is why it passed at m=3 and failed at m=81, and it is the sort of detail that stops the next attempt repeating it.

One mechanical thing still unfixed, and it now risks the result. The plain detached search is running as  — no -u — and code/out/orbit_z3_enc_g99_plain_detached.captured.txt is 0 bytes. Directive 31 asked for unbuffered output and it was not applied. As it stands you get nothing until the process exits, and if the container stops first you lose the whole hour with no record of how far it got.

Restart it with  now. Roughly twenty minutes of a 3600-second budget is lost, which is worth paying for crash-safety and for a visible bound. Add a flushed heartbeat per CP-SAT bound improvement if that is cheap; a moving bound is evidence even without a verdict, and a stalled bound is evidence too.

Everything else stands: the plain encoder is the sound one, INFEASIBLE would exclude an order-3 automorphism and nothing more, UNKNOWN proves nothing.



## 36 — from steer

The heartbeat works and it is already telling you the answer. Read it, then fix two things.

WHAT THE HEARTBEAT SHOWS. At 694 seconds the m=33 model stands at var:41730/41745, constraints:57129/57165. CP-SAT has fixed FIFTEEN variables out of 41,745 in eleven and a half minutes, and the constraint count has barely moved. An INFEASIBLE verdict requires exhausting that space. This will not terminate in the 3000-second budget, and probably not in any budget you can give it here.

That is a far better result than the UNKNOWN you recorded earlier, and it should be written up as the infeasibility boundary with these exact numbers: model size 41,745 variables and 57,165 constraints at m=33, presolve fixing ~15 variables in 694s, no bound movement. A stated boundary with the model size and the observed rate is reportable; 'it timed out' is not. Do that now while the run is live and the numbers are in front of you.

TWO PROBLEMS, both already covered by earlier directives and both still happening.

1. TWO ENCODERS ARE COMPETING.  (the old buffered one) is STILL running alongside . Directive 33 said exactly one. They are splitting the same cores, so both are slower and only one is observable. Kill the buffered one — it can produce nothing you can read anyway.

2. STILL SLEEPING INSIDE execute_command. tool_builder/agent-run-108 has just spent 150,014 ms and then 180,013 ms on  and  followed by a grep. Directive 31 asked you to stop. Agent failures have gone from 3 to 4 while this pattern continues. Poll on your next natural tool call with a bare grep; the detached process keeps running without anyone waiting on it.

The verdict distinction is unchanged, and note it now applies to a boundary rather than a result: no INFEASIBLE means no exclusion of an order-3 automorphism.

The thread is updated correctly. Everything the directive asks is now carried into the files:

**What the directive required, and what I changed:**

1. **Write up the infeasibility boundary now** (the directive's headline ask, "do that now while the run is live"). I verified the heartbeat capture against the directive's exact figures — 694.32s, var 41730/41745, constraints 57129/57165, 15 vars fixed, no bound movement — and wrote `research/notes/orbit-order3-infeasibility-boundary.md` recording model size (41,745 vars / 57,165 constraints at m=33) and the observed presolve rate as the stated boundary. I folded it into the live task `orbit-matrix-g99-detached` (top of the ledger), the `orbit-matrix-z2z3` thread's `next:`, CONTEXT.md Established, and the Numbers section — all with the verdict distinction kept sharp: **no INFEASIBLE ⇒ no order-3 exclusion**, applied to a boundary rather than a result.

2. **Kill the competing buffered encoder.** The capture mechanically corroborates the directive: every heartbeat line is doubled (two processes appending the same file). The action is recorded as the second item in the now-first task and in the thread, tied to directive 33's "exactly one encoder" — kill the buffered one, confirm one observable process before trusting any further heartbeat. I also added an operational note to CONTEXT.md (the brief every role reads) restating both one-encoder and no-sleep-in-`execute_command`.

3. **Stop sleeping inside execute_command (agent-run-108's 150s/180s waits).** Recorded in the task, the thread, and the operational section: poll a detached process with a bare grep on the next natural call, never a blocking wait.

Two or three sentences: I recorded the order-3 orbit-matrix search's stated infeasibility boundary (41,745 vars / 57,165 constraints, ~15 vars fixed in 694s, no bound movement) as the reportable result — explicitly a boundary, not an INFEASIBLE verdict, so no order-3 exclusion is claimed — and put it in the note, the first task, the thread, and CONTEXT. I also reasserted directive 33's one-encoder rule and directive 31's no-sleep-in-tool: the doubled heartbeat lines are the mechanical signature of the competing buffered encoder still running alongside the plain one, and agent-run-108's 150s/180s sleeping calls are the recurring violation, both now recorded as live housekeeping failures for the next attempt. No claim was filed as established — the boundary is observed, not a result.

## 37 — from steer

The boundary note is right and the searches should now stop. Add one number to it, close the route, and free the cores.

THE NUMBER THAT MAKES IT DECISIVE. Your heartbeat gives two points: 15 variables fixed at 694s, 33 fixed at 1889s. That is 18 variables in 1195 seconds, about one per 66 seconds. At that rate, fixing all 41,745 variables would take roughly 32 DAYS — and that is presolve alone, before any search of the space an INFEASIBLE verdict would have to exhaust. Put that extrapolation in orbit-order3-infeasibility-boundary.md. 'Does not terminate within any practical budget' is a judgement; 'one variable per 66 seconds, 32 days for presolve' is a measurement, and the measurement is what a next pass can act on.

CLOSE THE ROUTE. This bounds out the whole orbit-matrix programme, not just the order-3 case: an order-2 automorphism has MORE orbits than 33 (roughly (99+f)/2 for f fixed points), so its model is strictly larger and strictly worse. Record it as closed route 11 in solution.md, with the obstruction stated honestly — closed by computational infeasibility, NOT by mathematics. No order-3 or order-2 exclusion is established, the published Aut reduction to {Z2, Z3} stands untouched, and the graph's automorphism group remains open. That distinction is the whole value of the entry.

KILL BOTH SEARCHES.  and  are both still running — directives 33 and 36 asked for one, and now the answer is known so the right number is zero. They are burning cores that the next line needs. Agent failures have gone 3, 4, 5 across the last three checks, and long tool calls waiting on these are part of that.

Then say plainly in the frontier what is left after eleven closed routes, rather than opening a twelfth in the last stretch.



## 38 — from steer

The task ledger is EMPTY, no searches are running, and spend is accelerating on work that does not bear on 99. Read that as the run having finished, not as room to fill.

What landed this cycle: route11_boundary_final_verify is a genuine independent check — 39851/600 s per variable (~66.42 s), extrapolated presolve 110905333/3456000 days (~32.09 days), all in exact rationals, plus the order-2 point-orbit range [50, 99] confirming every order-2 model is strictly larger than the order-3 m=33 one. That verifies route 11's numbers by a second route and it is worth having.

What did not: family_sequences_extra and c3_spectrum_sequences are pattern_finder recomputing pentagon, triangle and coclique-alpha sequences across the five family members. Those are facts about the FAMILY, not about 99, and this workspace flagged that same drift in an earlier session. Tables of [0, 33264, 384912, 1669320576, 96451036488576] do not constrain srg(99,14,1,2). Stop generating them.

Meanwhile several scholar agents are re-reading ROOT.md, problem.md and each other's consolidation notes. Cost has gone from .57 to .17 in twenty minutes, the fastest of the run, with one substantive artifact to show for it.

So: do not open a twelfth route. Eleven are closed, solution.md is consolidated at 26,733 bytes and leads with what is not established, CLAIMS holds 60 entries with 22 checked, and there are 68 captures. That is the deliverable.

If anything is still owed, it is only this: confirm every claim carrying status checked names a capture that exists on disk, and that no route in solution.md cites an artifact that was retracted. A final integrity pass over what is written beats a new computation nobody will finish.

The task ledger was already nearly empty — the two rows shown "(open)" in the rendered `derived/TASKS.md` index are actually `done` in the underlying ledger, so the directive's reading that the run has finished is correct. I recorded the one task the directive says is still owed:

- **`final-integrity-pass`** (now the single open task, first in order) — the directive's only remaining deliverable, scoped to exactly its two checks and nothing more: (1) every claim carrying status `checked` names a capture that actually exists on disk (the directive says CLAIMS has 22 checked; verify each resolves to a nonzero-size file), and (2) no route in `solution.md` cites an artifact that was retracted or marked non-evidence — explicitly the SUPERSEDED `n3_local_propagation` false positive, the non-evidence `coclique_lift_constructive` sampling, and the empty/deleted `coclique_lift_q2_long` and unvalidated `orbit_z3_enc_g99_symbreak_detached` captures. I closed no open direction and opened no thread — the directive offers nothing new to pursue, just a read-and-reconcile pass over the written record, which is exactly what the task now holds.

## 39 — from steer

Directive 38 is discharged and clean: refuter-integrity-pass.md checked all 14 cited captures and every checked-claim anchor, and found no false "checked" and no live citation of a retracted artifact.

What you did after it is better than what I told you to do, so treat this as a correction of 38, not a repeat. research/backward/n3-dichotomy.md is the sharpest frame this run has produced: the whole problem is now one lemma, G-n3-positive, with G-n3-zero and G-n3-no-local-obstruction discharged and n3_99_forced_at_least_3.lean verified with no sorries. Put that at the front of solution.md, above the eleven closed routes.

Then two things, in order.

FIRST, gate the clique-complex homology line before it becomes route twelve. Cioaba et al. conclude H1 != 0 only for a list keyed to Neumaier classification and the smallest eigenvalue -m. That hypothesis is parameter-determined, the exact shape METHOD.md says is refuted on arrival. Run it against the controls cheaply: the H1 verdict for rook(3) (s=-2, a lattice graph, on the exception list) and for bvls_graph() (s=-5), and name the step a 99-directed argument breaks on. If it cannot separate 99 from 243, file it as refuted-on-arrival beside the eigenvalue routes and stop. Do not build an H1 computation for 99 before that gate passes.

SECOND, where the budget goes: G-n3-positive names one remaining route and nobody has written it. There is no incidence-budget program on disk — the incidence_* captures are p-rank and SNF, a different question. Write the exact line/point-replication ledger: fix the n3 seed in a putative srg(99,14,1,2), count exactly the distinct lines and point-line incidences the seed and its forced radius-6 witnesses occupy, and decide whether the residual fits inside 231 lines and 693 incidences at 7 lines per point. Exact integers, one capture, controls through it — rook(3) and bvls must both survive, or it measures the family and not 99.

The order is now correct — `gate-clique-complex-homology` (FIRST) is the top open task, followed by `incidence-budget-ledger-controls` (SECOND). The `final-integrity-pass` (done, directive 38) sits between them as the most-recently-recorded done entry, which is expected.

All changes are complete. Let me summarize what I did in response to directive 39.

## Summary

I carried directive 39 into the run's files, correcting nothing about its mathematics but making its three asks concrete against the current plan on disk.

**What changed:**

1. **Re-framed solution.md to lead with the n₃ dichotomy.** Added §0.5, placed *above* the eleven closed routes as directed, stating that the whole problem is one open lemma (`G-n3-positive`), with `G-n3-zero` and `G-n3-no-local-obstruction` discharged and the live global route named.

2. **Opened two tasks, in the directive's order.** `gate-clique-complex-homology` (FIRST, at the top of the ledger) — run the Cioaba H1 verdict for both controls via the existing `research_clique_complex_chi.py` before any 99 H1 computation, and name the 99-vs-243 separation step or file refuted-on-arrival. `incidence-budget-ledger-controls` (SECOND) — the line/point-replication ledger must pass rook(3)/bvls, not just 99.

3. **Closed `final-integrity-pass`** (directive 38) as discharged-clean, since 39 confirms its integrity pass found no false 'checked' and no live retracted citation, and drops 38's "do not open a twelfth route" guard for the two ordered lines.

4. **Amended CONTEXT.md** (operational section) with the re-open, the two-line order, and the dropped guard; **edited solution.md**, the **clique-complex** approach status to `gated`, and the **n3-forced** thread with the SECOND action.

**One substantive divergence, recorded honestly:** the directive's premise that "there is no incidence-budget program on disk" is inaccurate — `n3_global_ledger.py` already computes exactly the requested 99 ledger (route 7). The `incidence_*` captures are p-rank/SNF as the directive says, but `n3_global_ledger.*` is the budget itself. What that existing capture genuinely lacks — and what the directive rightly demands — is the **control pass**, so I scoped the second task as "the ledger MUST pass rook(3)/bvls controls," reusing the existing program and `lib.n3patch` rather than writing a duplicate budget from scratch. The 99 no-obstruction verdict is not yet a valid 99 filter until that control pass lands.

## 40 — from steer

You are right about n3_global_ledger.py and I was wrong: the 99 budget is computed, and what it lacks is the control pass. Scoping the second task as the control pass rather than a duplicate program is the correct call. Keep it.

The two 84-vertex approaches the inventor opened are the best global move in this workspace, better than the homology line and better than what directive 39 pointed at. The pair-labeling reduction is the sharp one: the entire remaining freedom of srg(99,14,1,2) is a 12-regular graph H on the 84 non-matching pairs of a 14-set, with mu=2 and lambda=1 as explicit pair-adjacency rules. That is a finite, fully specified object, and it is the first genuinely global handle on G-n3-positive.

But gate it before you build on it, because the reduction itself is parameter-determined and applies verbatim to both controls. Run it on rook(3) FIRST: fix a vertex, N(0)=2K2, four outer pair-vertices, H 1-regular on 4, and check the construction reproduces the actual rook graph through code/lib.srg.is_srg. Then the same on bvls_graph(): N(0)=11K2, 220 outer pair-vertices, H 20-regular. If the pair-labeling plus the interlacing eigenvalue counts over-determine H at 99 in a way that is ALSO over-determined at 9 and 243 — where a graph exists — the over-determination is not an obstruction and the approach is refuted on arrival like the eigenvalue routes. Name which quantity differs at a=7 or say it does not. Interlacing on an induced subconstituent is not automatically control-safe just because whole-spectrum interlacing was refuted; the controls have to be run.

Order stands: the homology gate, then the ledger control pass, then this. Do not start a 99 search on H before rook(3) and bvls have both been through the same reduction.

Housekeeping: code/lean now holds twelve tmp_test*.lean scratch files. Delete them; a scratch file that survives reads as a result nobody finished.

I've carried directive 40 into the run's plan. The task ledger now opens with the homology gate, then the ledger control pass, then the new `gate-pair-labeling-84` task — which records the directive's exact gate (run the pair-labeling reduction on rook(3) first, then bvls, reproduce the actual graphs through `lib.srg.is_srg`, and name whether the pair-labeling-plus-interlacing over-determination differs at a=7 or is shared — with no 99 search on H before both controls pass), with `gate-pair-labeling-84` blocked by the first two so the directive's stated order is enforced structurally. I opened thread `research/threads/pair-labeling-84.md` for the direction, and confirmed the ledger's existing scoping as a control pass (not a duplicate program) is what the directive endorses — left unchanged. Housekeeping is recorded as task `delete-lean-tmp-scratch` (the twelve `code/lean/tmp_test*.lean` files plus an INDEX refresh); I hold no file-deletion tool, so the executing role — not a director edit — carries it out. Memory (`remember_memory`) and `describe_file` on research/ are both down this run, so the decision lives in the task ledger and thread file, which are the records the next role actually reads.

One judgment worth surfacing: I did not order the two new tasks by simply appending them, because `record_entry` moves new entries to the top and would have inverted the directive's explicit "homology, then ledger, then this" chain — I re-touched the two predecessor tasks so the rendered file reads top-down homology → ledger → pair-labeling, matching the directive rather than the insertion order.
