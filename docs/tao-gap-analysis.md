# What Tao does that this runtime could not

Terence Tao's problem-solving method, read off his own writing and off eleven of
his solved problems, set against what this runtime actually does — with the
`file:line` that shows it. The research it rests on is in
[`research/tao/`](../research/tao/): the heuristics with quotes and URLs
(`01`), the eleven problems dissected (`02`), the capability map read off this
code (`03`), and what Tao says about machines doing mathematics (`04`, `04b`).

Every row is one of three things, and the distinction is the point of the file:

- **Absent** — nothing in the runtime does this.
- **Unenforced** — a prompt asks for it. This repository's own standard is that
  a prompt instruction is not a control, so an unenforced rule is a rule the
  code stopped guaranteeing.
- **Unused** — the code produces it and nothing reads it.

Three rows were closed on this branch. They are marked **[closed]** and the
change is described at the end.

## The table

| Tao's move | Source | What this runtime did | Status |
|---|---|---|---|
| Turn off nine of ten difficulties, solve that, then re-merge | `01`§1, `02` A1–A5 | Nothing could lower the target. `reducer` decomposes it, `inventor` re-routes to it, both hold it fixed | **[closed]** |
| A no-go result is navigational — publish it and use it to pick the next encoding | `02`§4, §9, D1–D3 | `solved` was binary; a proved barrier scored as an unsolved attempt | **[closed]** |
| A proof is what the kernel accepted; everything else is a reason to believe | `01`§21–23, `04` R1/R8 | Lean and Mathlib in the image, no Rust ran either; `Status::Proved` was prose | **[closed]** |
| Reuse what is already proved; never re-derive | `01`§27, `04` R13 | Per-problem Cognee stack: `scripts/run-agent:110-126`. Every run starts from zero technique | Absent |
| Cheap tools first, the expensive reasoner last | `04` R5, EQT's 22M → ~1,000 | An attempt is a model call that may delegate. No ladder, no cost-per-subgoal instrumentation | Absent |
| Prove and disprove concurrently; look for the counterexample first | `01`§10, `04` R11 | No refutation arm. `sat_solver`/`smt_solver` exist but are delegated, not scheduled against proof | Absent |
| Propagate every established fact through the entailment relation before scheduling new work | `04` R5b (~37× in EQT) | `search_claims` retrieves; nothing closes the claim set under implication | Absent |
| Record which techniques are known not to apply to a subgoal | `01`§16, `04` R5c | `research/APPROACHES.md` closes a *route* with a reason; no per-subgoal immunity anything schedules on | Partly, unused |
| Check the literature *after* a solve — a short proof raises the prior it is known | `01`§19, `04` R33 | No post-solve novelty check. Erdős #728 is the live example: an AI solution matching Pomerance 2014 | Absent |
| Fund the branch that is not currently winning | `02` F4 — Polymath8's real lesson | One line of attack; `diversify` fires only after two consecutive unproductive attempts | Absent |
| Rewrite someone else's fresh proof in a cleaner formalism | `01`§—, `02` G1–G3 | No simplification mode. The librarian acquires, the scholar digests, nobody rewrites | Absent |
| A statement DAG with a status lattice, worked against admitted siblings | `04` R2/R3, the Lean blueprint | `research/BACKWARD.md` is the closest thing and is a flat skeleton-plus-gaps, not a DAG; no contract-first concurrency | Partly |
| Numerics before theory | `01`§20, `04` R10 | The method policy's first step is a naive oracle, and `attempt_step` spawns it rather than asking. This one the runtime already does | Present |
| Direction reaches a live run, queued, never a claim | `04` R20 | `./steer` → `config/directives.jsonl`, `director` denied `research/CLAIMS.md` | Present |
| Declare the harness's knobs, and report the run even on failure | `04` §III.5 | Six of seven knobs map to files that exist. Attempts abandoned are not counted | Partly |
| One monotone, legible statistic; watch for the Zeno regime | `01`§35, `02` F3 | The judge's 1–5 score is pushed to `state.scores` (`solutions_judging.rs:49`) and read by no code | **Unused** |
| Modularise so no participant needs the whole argument | `01`§34, `02` F2 | Nineteen tool-boundaried roles, enforced in code. The runtime's real strength | Present |

## The three that were closed, and why those three

They are not the three biggest gaps. They are the three where the runtime
already had the machinery and was one control short of using it — which is a
different and much cheaper kind of gap than "build a cross-problem library".

### Verification was held to a weaker standard than path traversal

Lean 4 with a pre-built Mathlib is the largest thing in the image. No line of
Rust ever invoked it: the only `#print axioms` and `sorry` references in the
crate were prompt text and a test asserting that the *prompt* contains those
rules (`orchestrator_roles_test.rs:94-97`). So the strongest artifact this
runtime can produce and a sentence claiming that artifact were the same row in
`research/CLAIMS.md`, and the ledger did not try to tell them apart.

That is this repository's own recurring failure — a prompt instruction is not a
control — landing in the one place it costs the most. Tao's stated reason for
caring is not ceremony: his own account of AI-generated mathematics is that
"the AI-generated proofs, they can look superficially flawless … no human would
have actually made that mistake" (`04`§I.3). A plausible-but-wrong argument is
precisely what a prose ledger cannot filter and a kernel can.

`lean_check` (`src/orchestrator/lean.rs`) runs the kernel, parses what came back,
and files a verdict under `code/out/lean/`. `Status::Formalised` is a new class
beside `Proved` rather than a redefinition of it, and that distinction is
load-bearing: `Proved` in this ledger has always meant *the source* proves it —
a cited theorem, resting on somebody else's word — while the new one means this
workspace holds an artifact the kernel accepted. Gating `Proved` on Lean would
have conflated a paper's theorem with a local proof.

The check runs at ledger-derivation time, not at write time, which is what makes
it hold: a claim whose Lean file is later edited into a `sorry` loses its
standing on the next derivation rather than keeping a verdict it has outgrown.

### `solved` was binary, so a barrier scored as a failure

Greenfeld and Tao published two no-go results before the periodic tiling
counterexample. The 2021 rigidity result proved that a one-tile Wang encoding
*cannot* work, and that is what sent them to the Sudoku encoding that did
(`02`§9). Tao wrote his own Collatz barrier in 2011 and then in 2019 went around
it by not proving the conjecture (`02`§3). Of eleven programmes dissected, two
were preceded by an explicit no-go and one *was* the no-go — and in both
navigational cases the barrier was written by the same author who later stepped
around it.

Scored here, every one of those would have read as an unsolved attempt.

`BANKED` is the fourth reflection verdict. It never ends the run, so a wrong one
costs an attempt of optimism rather than a wrong final answer — but it counts as
progress, and progress resets `unproductive`, which is the only route into
`diversify`. A verdict a model could assert freely would therefore let a stuck
run keep itself out of diversification forever by claiming a small win every
cycle, which is the failure `COMPUTATIONAL_THRESHOLD` was added to close one
verdict over. So it is honoured only when the claim ledger actually grew, read
off disk. A `BANKED` over an unchanged ledger is rejected with a lesson naming
what was missing.

### Nothing could make the problem smaller

This is the gap that most surprised the reading. It is Tao's single most-repeated
move — "if there are 10 things that are making your life difficult, find a
version of the problem that turns off nine of the difficulties, but only keeps
one of them and solve that" — and of the eleven problems in `02`, four were
solved by weakening the target along a named axis and a fifth by weakening the
*hypothesis* instead of the conclusion.

The runtime had two of the three directions and not the third. `reducer` asks
what would be *enough* and answers with lemmas; `inventor` asks what *else*
reaches the goal and answers with a route. Both hold the goal fixed. Nothing
asked what would be *easier*.

`weakener` is the third. It names the difficulties, then writes a ladder of
rungs from the version with all of them switched off up to the real one, each
rung saying which are off and what turning the next one back on would take. Its
dangerous failure is obvious and specific — reporting a rung as the goal — so
the ledger records which difficulties were off when each rung landed, and the
prompt says plainly that a rung does not imply the goal and is not meant to.

It shares the reduction arm rather than getting a node of its own, because it
shares everything that decides when to run. It is deliberately *not* gated on
the run being stuck: `open_invention`'s stuck-gate was reachable in principle and
not in practice, and across a day of live runs the inventor was spawned once.

## The largest gap was not closed

**Every run starts from zero technique.** `scripts/run-agent:110-126` gives each
problem its own Cognee and Neo4j stack, so `recall_memory` reaches only what
earlier runs *on this problem* established. There is no cross-problem library of
lemmas, techniques, or code.

Set against `02`'s ladder statistics, this is the expensive one. The median
programme there rests on three prior partial results, and the two fastest
results in the set — Tao's sunflower rewrite eleven months after ALWZ, and PFR's
revival of Gowers' twenty-year-old entropy idea — both consisted of picking up
someone else's existing output. Mathlib is the mechanised version of the same
thing. A runtime that cannot carry a lemma from one problem to the next is
structurally unable to make the move that produced the two fastest solves in the
sample.

It was not closed here because the comment at that line records a real reason: a
shared server was the earlier arrangement and it failed on availability — four
concurrent runs turned `recall_memory` into a ten-minute hang ending in `409
Conflict`. `COGNEE_NETWORK` already opts back into sharing. This is an
operational decision about a store's availability, not a missing capability, and
it is the user's to make.

## Two findings unrelated to Tao, raised rather than folded in

**`--no-research` withholds discovery but not retrieval.** Only `exa_search` and
`oeis_lookup` sit behind `research_enabled` (`orchestrator_registry.rs:13-14`);
`download_document` is in the unconditional `document_tools` array (line 46). A
run with research off can still fetch any URL it can name, including an OEIS
page — which is the one lookup most likely to hand a self-contained problem its
answer outright. The gate is enforced by not registering the tool, which is the
right mechanism; it is registered one array too high.

**The judge's score is written and never read.** `state.scores.push(score)` at
`solutions_judging.rs:49`, serialised into the accumulator, and consumed by
nothing. The judge itself now runs once after the loop exits (`workflow.rs:56`),
so `STEER` and `RESTART` route nothing and `MAX_RESTARTS` is unreachable. That
is recent and looks deliberate, so it is described rather than changed — but it
means the runtime currently has no monotone progress statistic anything acts on,
which is the one thing `01`§35 says a long programme needs.
