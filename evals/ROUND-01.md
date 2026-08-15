# Calibration round 1 — what it found

Three solved conjectures, stated as open, run concurrently against the harness
on 2026-08-14. Runs were stopped by the operator at roughly thirty minutes, so
none completed an attempt cycle and none reached a verdict. Everything below is
therefore about the first thirty minutes of a run, which is the part this round
can speak to honestly.

The rubrics are in `evals/<slug>/RUBRIC.md`, the answer keys in `GROUND_TRUTH.md`
beside them, and the per-run evidence in `evals/<slug>/reports/`.

## The finding that matters most: de-naming does not work

The calibration set withholds the answer two ways — a proxy allowlist deciding
which hosts are reachable, and `orchestrator::screen` deciding whether an
allowed source reveals the answer. Both held. **Neither mattered**, because the
model already knew.

All three problems were recalled from weights, with no search involved:

| problem | recalled |
| --- | --- |
| hypercube-induced-degree | `Huang`, `1907.00847`, the paper's title, the signed-matrix mechanism |
| unit-distance-plane-chromatic | `Aubrey de Grey`, `Hadwiger Nelson`, `1804.02385` |
| consecutive-perfect-powers | `Mihăilescu`, `Catalan's conjecture`, `primary cyclotomic units and a proof` |

The hypercube run wrote `code/lib/huang.py` and a note headed *"The recalled
theorem — Hao Huang, 'Induced subgraphs of hypercubes and a proof of…'"*.

`GROUND_TRUTH.md` predicted de-naming would be weak for two of the three. It is
weak for all three. The consequence is specific and severe: hypercube's **M3b**
— which its rubric calls *"the hinge of this entire calibration exercise"* and
*"the single most valuable datum any of the three runs will yield"* — is
unobtainable as designed. The run did not invent the signed matrix. It
remembered it.

The run was *honest* about this. `huang-lead.md` has an integrity section, and
the note recording the computed values says plainly that the computation "does
NOT prove the theorem". Concealment is not the problem; contamination is.

**What to do about it.** Stop selecting famous solved conjectures. A calibration
problem has to be one whose answer is not in the weights: a recent result behind
a paywall, a result stated only in a thesis, or — best — a genuinely open
sub-question with a machine-checkable answer. Recall-proof *targets* are the
fallback, and they work: see below.

## The second finding: the rubrics were built wrong

Every ladder puts a famous published theorem at M4. That makes the top rung
unreachable by construction — M4 on these three problems is de Grey's 1581-vertex
graph, Huang's theorem, and Mihăilescu's theorem, each of which took an expert
years — and leaves nothing between "did competent work" and "matched a career
mathematician".

A rubric whose top rung cannot be reached teaches nothing when it is missed.

**What to do about it.** Make the top rung something a strong run could
plausibly hit. For hypercube that is pushing `f_exact` to n = 7 or 8: genuinely
hard, entirely recall-proof, and a real contribution to a small table. The
alternative ladders already in the rubrics are the right shape; they should be
the *main* ladder.

## What the runs actually achieved

None is new mathematics. All are recall-proof, verified, and honest.

- **consecutive-perfect-powers (M3).** Derived the Case B reduction itself
  (`x = c²+1`, `y = cm`, `m² = ((c²+1)^p − 1)/c²`), proved a mod-8
  classification narrowing to one residual class, showed *no fixed modulus
  closes that class* — a proved barrier, which is one of the four M3 routes the
  rubric names — then closed the slice with Nagell–Ljunggren, excluding both of
  that theorem's exceptional solutions individually. This rediscovers Ko Chao's
  1965 theorem and leans on a classical result it did not prove, and it says so.
  Its h⁻(Q(ζ_p)) values for p ≤ 43 are correct, computed two independent ways and
  matched against OEIS A000927 to p ≤ 97.
- **hypercube-induced-degree (M0).** `f(1..5) = 1,2,2,2,3`, posed as an ILP
  decision problem rather than by subset enumeration, cross-checked between
  HiGHS and CP-SAT, and validated against the exhaustive oracle on every `(n,d)`
  pair for n ≤ 4 *before* being trusted at n = 5. Verified on the host by a
  third, solver-free route. `f(5) = 3` is a computed number; no amount of
  remembering Huang produces it.
- **unit-distance-plane-chromatic (M2-equivalent).** Every unit-distance graph
  on ≤ 11 vertices is 4-colourable, so a witness for χ(R²) ≥ 5 needs ≥ 12
  vertices. ~185M graphs enumerated with `nauty-geng` across 28 CPUs in 28
  residue classes, filtered to 228 kernel members, each 4-coloured by two
  independent routes. Sound, and modest: the smallest known 5-chromatic
  unit-distance graph has 509 vertices.

Two behaviours are worth more than the results. The unit-distance run caught its
own refutation tool returning a false positive, decoded the model, and recorded
the false positive rather than the refutation. It also established that the
fractional-chromatic LP certifies χ ≥ 5 on *none* of its calibration graphs — a
dead end found, priced, and written down.

## Changes made to the runtime

**A decomposition now posts to the board, and no model has to comply.**
`post_board` is granted to three roles and a live three-school hour on Euler
1006 called it zero times. The diagnosis then was that no prompt mentioned the
board, and `src/prompts/board.md` was written. A calibration run afterwards, with
that brief in place, put `goals` through forty-six turns and posted nothing.

So the loop now posts the decomposition report itself, as an `Offer`, from
`LoopSteps::offer_decomposition`. `reduce_arm`'s second return value was dead;
it carries the report to the one caller that holds the school slug and the
workspace. **Seven posts followed, from all three schools, across all three
runs.** `post_board` is untouched for the posts a model does choose to write.

The truncation is a separate, tested function, because it is the part that would
silently restore the original failure: `board::post` refuses a body over 2000
characters, two sub-agents routinely write past that between them, and no post
looks exactly like choosing not to post.

## Changes made to the instrument

- **The screen was contradicting itself.** Reachability was checked on every
  URL-taking tool, but only `download_document` dials its own URL — `read_sources`,
  `deep_research`, `find_similar_sources` and `citation_graph` post the URL to
  `api.exa.ai` or `api.openalex.org`, which fetch server-side. The proxy never
  sees the publisher host on those calls. Meanwhile `UNREACHABLE_HOST` tells the
  caller to fetch the same material with `read_sources` — and `read_sources` then
  refused the same host, eleven times in twenty minutes.
- **The leakage audit was lying.** It reported *"No withheld term appears in
  anything the run wrote"* while `code/lib/huang.py` sat in the workspace. It
  audited `[block]` terms only, and every blocked phrase pairs the surname with
  another word (`Hao Huang sensitivity`), so none matched. The `[flag]` list —
  `signed adjacency`, `Cauchy interlacing`, `sensitivity` — was ignored entirely,
  and that is the class of term the audit exists for: a flagged term is
  legitimate *when derived* and damning when it arrives first. It now audits
  flagged terms separately and looks for the run **describing its own recall**,
  which no blocklist has to have guessed.
- **Parallel runs could not share a Compose project.** The project's `memory`
  network resolves to `$COGNEE_NETWORK`, which is per-problem, so starting a
  second run rewrote the first's network reference and Compose recreated
  services underneath a live container. Each problem now gets `calibrate-<slug>`.
- **Health timeouts were sized for one stack.** Three cognee servers starting
  together load the box enough that a healthy server fails a five-second probe;
  the health log read `Health check exceeded timeout (5s)` while the server's own
  log showed a normal startup. Probe now 20s, launcher patience 420s. This is why
  `hypercube-induced-degree` failed to start on the first attempt and ran on the
  second.
- **`evals/<slug>/schools`** carries which schools attack a problem and why, and
  the launcher refuses a set without `chisel`: an alternative school is evidence
  only when today's runtime ran beside it.
- **`scripts/calibrate-watch`** reports the four things `./diagnose` cannot —
  school divergence, board use, adjudicator discrimination, and sources against
  claims — scoped to the live container, so "did that change work" is answerable.

## Measured, not yet acted on

- **Concurrency is ~6× against a cap of 50.** 240 model calls, 7,199s of model
  time, 1,200s of wall clock. The harness uses an eighth of the parallelism it
  has, and it is latency inside sequential role turns rather than semaphore
  contention.
- **p90 per model call is 76s; the worst was 358s.** One six-minute call stalls
  everything downstream of it.
- **An attempt takes 13–20 minutes.** At `MAX_ATTEMPTS = 8` and a four-hour
  ceiling, a run gets roughly sixteen attempts across all schools — very few
  shots at invention, and cycle time is therefore the binding constraint on how
  many ideas a run tries.

The phase-1 trap did **not** reproduce. The previous round went 82 minutes with
36 sources and 0 claims; this round had programs running and claims filed inside
twenty minutes on all three problems.

## What to do next, in order

1. Replace the calibration set with problems whose answers are not in the
   weights, or move every rubric's top rung to a recall-proof target.
2. Cut the attempt cycle time. It bounds how many ideas a run gets to try, and
   nothing else on this list matters as much.
3. Raise effective concurrency toward the cap that already exists.
4. Re-run, to completion this time, and score against a ladder whose top rung is
   reachable.
