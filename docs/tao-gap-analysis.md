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

Five rows were closed on this branch. They are marked **[closed]** and the
change is described at the end.

## The table

| Tao's move | Source | What this runtime did | Status |
|---|---|---|---|
| Turn off nine of ten difficulties, solve that, then re-merge | `01`§1, `02` A1–A5 | Nothing could lower the target. `reducer` decomposes it, `inventor` re-routes to it, both hold it fixed | **[closed]** |
| A no-go result is navigational — publish it and use it to pick the next encoding | `02`§4, §9, D1–D3 | `solved` was binary; a proved barrier scored as an unsolved attempt | **[closed]** |
| A proof is what the kernel accepted; everything else is a reason to believe | `01`§21–23, `04` R1/R8 | Lean and Mathlib in the image, no Rust ran either; `Status::Proved` was prose | **[closed]** |
| Reuse what is already proved; never re-derive | `01`§27, `04` R13 | Per-problem Cognee stack: `scripts/run-agent:110-126`. Every run starts from zero technique | Absent |
| Evolve *programs* that build the object, scored by a verifier | `04b` FunSearch, AlphaEvolve | Nothing searched over programs. A construction was reasoned toward or not found | **[closed]** |
| Cheap tools first, the expensive reasoner last | `04` R5, EQT's 22M → ~1,000 | An attempt is a model call that may delegate. No ladder, no cost-per-subgoal instrumentation | Absent |
| Prove and disprove concurrently; look for the counterexample first | `01`§10, `04` R11, EQT's 13.6M | Four proving roles, all delegated *to*, none scheduled *against* the statement | **[closed]** |
| Propagate every established fact through the entailment relation before scheduling new work | `04` R5b (~37× in EQT) | `search_claims` retrieved; nothing closed the claim set under implication | **[closed]** |
| Record which techniques are known not to apply to a subgoal | `01`§16, `04` R5c | `derived/APPROACHES.md` closes a *route* with a reason; no per-subgoal immunity anything schedules on | Partly, unused |
| Check the literature *after* a solve — a short proof raises the prior it is known | `01`§19, `04` R33 | No post-solve check, and `open_library` returned *early* on a solve. Erdős #728 is the live example: an AI solution matching Pomerance 2014 | **[closed]** |
| Fund the branch that is not currently winning | `02` F4 — Polymath8's real lesson | One line of attack; `diversify` fires only after two consecutive unproductive attempts | Absent |
| Rewrite someone else's fresh proof in a cleaner formalism | `01`§—, `02` G1–G3 | No simplification mode. The librarian acquires, the scholar digests, nobody rewrites | Absent |
| A statement DAG with a status lattice, worked against admitted siblings | `04` R2/R3, the Lean blueprint | `derived/BACKWARD.md` was the closest thing and was a flat skeleton-plus-gaps, not a DAG | **[closed]** |
| Test whether a conjecture is *informative* before testing whether it is true | Graffiti's Dalmatian heuristic, `04` R28 | Nothing filtered a proposal against what the library already gives | **[closed]** |
| A theorem given an assumed axiom is a conditional result, not a theorem | `01`§21–23, `04` R1, lean4checker | `lean_check` accepted any file that compiled and printed axioms — one `axiom` line passed every check | **[closed]** |
| Numerics before theory | `01`§20, `04` R10 | The method policy's first step is a naive oracle, and `attempt_step` spawns it rather than asking. This one the runtime already does | Present |
| Direction reaches a live run, queued, never a claim | `04` R20 | `./steer` → `config/directives.jsonl`, `director` denied `derived/CLAIMS.md` | Present |
| Declare the harness's knobs, and report the run even on failure | `04` §III.5 | Six of seven knobs map to files that exist. Attempts abandoned are not counted | Partly |
| One monotone, legible statistic; watch for the Zeno regime | `01`§35, `02` F3 | The judge's 1–5 score is pushed to `state.scores` (`solutions_judging.rs:49`) and read by no code | **Unused** |
| Modularise so no participant needs the whole argument | `01`§34, `02` F2 | Twenty-two tool-boundaried roles, enforced in code. The runtime's real strength | Present |

## The nine that were closed, and why those nine

Most of them are places the runtime already had the machinery and was one
control short of using it — a different and much cheaper kind of gap than
"build a cross-problem library". Two, scored program search and refutation, are
new capabilities; both are here because their loops are *programs* rather than
prompts, which is this repository's own thesis about where control flow belongs.

Four of the nine are pure *derivation*: they add no role, no tool, and no file
an agent writes. The statement graph, the entailment closure, the Dalmatian
filter and the assumed-axiom check are all computed from what was already on
disk, and each existed only as prose asking a role to check for it. That ratio
is the finding worth keeping from the whole exercise — the cheapest large gains
here were not missing capabilities but relations nothing had ever followed.

### The graph the ledgers already implied

`derived/BACKWARD.md` held every edge and drew none of them. A skeleton names
its gaps and the claims it rests on; a gap is discharged by a claim or by
another skeleton proving it outright. `blueprint.rs` follows those edges and
answers three questions no single file could.

Which lemma can somebody start on *now* — every dependency settled, no need to
have read the rest of the argument. That is what Massot's blueprint bought the
PFR formalisation: ~25 contributors in three weeks, the author writing about 5%
of the Lean. The detached sub-agents here were already concurrent and there was
no way to say which lemma was safe to hand one.

Whether the argument is circular. Skeleton `A` needing a lemma `B` proves from
`A` reads as two sound reductions in two files and proves nothing as a cycle. A
flat ledger cannot detect this in principle: the fault is in no single row.

And blocked against ready, which the open-gap list flattens — every unproved
lemma looks equally attackable there and most are not.

### The library knew more than it said

The claim ledger stored statements and never reasoned over them. One new field,
`follows-from:`, closed transitively, and three things fall out. A claim whose
support is established *is* established, whatever its own block says — a run
that proves one again has spent an attempt on something it held. EQT measured
what this is worth: 597,582 facts closed into answers for all 22,028,942
implications, about 37×. A statement the library already entails is not a
result, which is Fajtlowicz's Dalmatian heuristic exactly — more than half of
Graffiti was the triviality filter rather than the generator. And a
contradiction can be real while no block states it: `a` gives `c`, `c`
contradicts `b`, the run holds both.

Both readings are refused in the strict direction, because the permissive one
would be worse than no closure at all: `asserted` never propagates, and a claim
that supports itself settles nothing.

### One `axiom` line passed every check there was

`lean_check` already caught a file that failed to compile, one that compiled
with `sorry`, one that printed no axioms, and one resting on `sorryAx`. It
accepted this:

```text
axiom key_estimate : ∀ n, f n ≤ 2 * n
theorem main : … := by … key_estimate …
```

It compiles, warns nothing, prints its axioms honestly, and proves the theorem
*given* something nobody established. The verdict now fails on any axiom outside
Lean's own three and names it, so the role knows what to go and prove.
`Lean.ofReduceBool` is refused with them: `native_decide` trusts the compiler
rather than the kernel, and the whole argument for ranking a Lean result above
everything else here is that the kernel checked it.

This is the hole `lean4checker` is usually reached for, and it needed no second
binary. Kernel replay guards against an environment that lied about what it
checked; what actually happens is simpler and far likelier, because it is one
line a model writes while doing exactly what it was asked.

### Verification was held to a weaker standard than path traversal

Lean 4 with a pre-built Mathlib is the largest thing in the image. No line of
Rust ever invoked it: the only `#print axioms` and `sorry` references in the
crate were prompt text and a test asserting that the *prompt* contains those
rules (`orchestrator_roles_test.rs:94-97`). So the strongest artifact this
runtime can produce and a sentence claiming that artifact were the same row in
`derived/CLAIMS.md`, and the ledger did not try to tell them apart.

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

### Nothing searched over programs

FunSearch improved the cap-set lower bound from 2.2180 to 2.2202 — "a great
improvement compared to research in the last 20 years" — and AlphaEvolve matched
or beat the literature on 20 of 67 problems. Neither reasoned toward an answer.
Both wrote programs that build candidate objects, scored them, and proposed
again from what scored well.

The reason to want it here is not the loop. It is what the loop leaves behind:
"we do not just discover the set of 512 eight-dimensional vectors in itself, but
a program that generates it … Through inspecting the code, we obtain a degree of
understanding of what this set is." Jordan Ellenberg on the same output: "When I
study them, I learn something." A number is an answer; a program is an
explanation, which is what this repository says a result has to be.

It also fits the architecture better than it fits most harnesses. Three of
FunSearch's four ingredients — one evolved function, best-shot prompting, an
island population — are bookkeeping, and bookkeeping in this runtime lives in
Rust. A model asked to remember which of four hundred programs scored best, and
to order them worst-to-best, is spending its turn on arithmetic nothing can get
wrong in code. The fourth, asynchronous scaling, already exists.

**The verifier is where the risk is, so it is a tool boundary.** AlphaEvolve is
"extremely good at locating exploits in the verification code" — on a packing
problem it satisfied a minimum-distance constraint by placing points nearly on
top of one another, and scored beautifully. Tao's team rewrote every verifier in
exact arithmetic and warned that trusting the numbers "can be risky as they may
be a consequence of verifier exploits rather than any true progress." An
autonomous agent occupies that row by default, because the search and the
verifier are written by the same process.

So the `searcher` holds no `write_tool_file`, no `execute_command`, and no patch
tool. `submit_candidate` is its only route to disk; it writes into `candidates/`
and runs the scorer over what it wrote in the same call. A candidate cannot be
recorded without having been executed, and `score.py` is unreachable. Two
mechanical checks back that up: a score that is not finite is a rejection rather
than a leaderboard entry, which is the shape a verifier exploit usually takes,
and a scorer printing both a rejection and a score has contradicted itself, so
the rejection wins.

**One design tension was resolved rather than inherited.** FunSearch discards
what does not run — silently and cheaply, because its method is to be wrong
thousands of times. This runtime reflects on failures and writes a lesson from
each, which is right for an attempt that costs an hour and ruinous at this
volume. Both survive by splitting the two meanings of "silent": a rejected
candidate costs no reflection, no lesson, and one line of output, but it is
recorded, and the board reports discard reasons with counts. A search that ran
four hundred candidates without improving is a finding; a leaderboard of winners
cannot show it.

### Nothing was ever scheduled against the statement

The runtime has four ways to prove something — `sat_solver`, `smt_solver`,
`theorem_prover`, `lean_prover` — and every one is *delegated to*, when a role
decides to ask. None was ever scheduled *against* the statement the run was
pursuing. So a false conjecture was attacked by proof for as long as the budget
lasted, and nothing in the loop ever asked whether the thing being proved was
true.

The measurement that settles how much this costs is the Equational Theories
Project's: 524 small finite structures refuted 13.6 million of its 22 million
implications — 13.3 million at size 3 alone — for 165 CPU-hours, before any
clever proof search ran. Refutation was not the consolation prize for a failed
proof. It was the cheap majority of the work, because most false statements are
false small.

`refuter` runs as a sixth evaluation arm beside every attempt. It takes the open
gaps and the current weakened rung — the statements somebody has committed to
proving, which are exactly the ones worth breaking — tries small cases by hand,
then encodes the smallest fragment that could still be false and hands it to
`find_counterexample`.

**Vampire is what makes this possible, and it is the one binary worth adding.**
`eprover` saturates toward a refutation of the negated conjecture, so on a
statement that is actually false it runs until its clock stops and reports
nothing. Vampire's `--saturation_algorithm fmb` searches for a *finite model*
instead, and such a model is exactly a counterexample: it answers
`CounterSatisfiable` and prints the interpretation. Prover9/Mace4 is the tool
this job usually names and Debian dropped it; cvc5's `--finite-model-find` works
over theories rather than a TPTP axiomatisation. Nothing already in the image
did this.

**The verdict worth having built it for is neither of the obvious two.** One run
distinguishes four outcomes, and the valuable one is `ContradictoryAxioms`: from
contradictory hypotheses everything follows, so a broken axiomatisation *proves
the goal*, which is how a bad encoding comes to look like a triumph. The SMT
role was held to checking for that in its prompt; the engine now reports it as a
status the runtime reads.

The role writes files, because the axiomatisation is the whole job and the whole
risk. It has no `execute_command`: a role hunting a counterexample with a shell
writes its own search over small cases, which is the answer-space search the
method policy prohibits, in the language most likely to hide its own bugs. And a
claim citing a refutation is checked against the filed verdict, exactly as a
formalised claim is checked against the kernel — a counterexample does not
merely fail to establish the goal, it asserts the goal is false, so it is the
worst thing to be able to claim without evidence.

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
Conflict`. This is an operational decision about a store's availability, not a
missing capability, and it is the user's to make.

*Since this reading:* the decision was made on the deployment side — one Cognee
for the box, one tenant per problem (`compose.shared.yaml`). That is not the
same as making the *brain* shared, which is what this gap is about and which is
still open; `docs/tao-proposals.md` #6 has what is left.

## What is still open, and why each was left

Four rows in the table are still `Absent` or `Partly`, and none of them is
cheap in the way the nine closed ones were.

**Cheap tools first, the expensive reasoner last.** An attempt *is* a model
call, so there is no ladder to climb and no cost-per-subgoal measurement to
climb it by. Building one means instrumenting every delegation with a price and
a success rate, then routing on the pair. That is a real subsystem, not a
control, and it is worth doing after the statement graph has produced enough
ready nodes to make the scheduling question concrete.

**Fund the branch that is not currently winning.** `diversify` fires only after
two consecutive unproductive attempts, which is the opposite of Polymath8's
lesson — the winning branch was funded *while* another was ahead. Doing this
properly means running two lines of attack concurrently and splitting budget
between them, which changes what a run *is* rather than adding an arm to it.

**Rewrite someone else's fresh proof in a cleaner formalism.** Two of the
fastest results in `02`'s sample came from exactly this. It is a role and a
prompt, and it is cheap — but it only pays once the librarian is reliably
acquiring proofs worth rewriting, and on the runs measured so far it is not.

**Techniques known not to apply, scheduled on.** `derived/APPROACHES.md` closes
a route with a reason and nothing reads that reason when choosing the next one.
Now that the entailment closure exists, the natural form of this is an edge in
the same relation rather than a new ledger, which is a reason to wait rather
than to build it twice.

**A monotone statistic to steer on** is listed below rather than here: the
score already exists and is simply not read, which is a wiring question and
described with the other two findings.

## What testing them against real work found

The nine closures were built against fixtures. Fixtures are text this repository
wrote, so a check that only ever met them is a check against its own
assumptions, and three of the four newest were wrong in ways no fixture could
show. `ledger_report` and `examples/derive_ledgers` exist so that the two
reasoned ledgers can be re-derived on the host, without a container or a key,
over a workspace a live run actually produced.

**The statement graph, over eight committed workspaces.** Three carry
decompositions; the other five have no `research/backward/` content and the
graph correctly says nothing about them. Across the three it resolved 25 nodes
into 23 ready and 5 blocked-or-refuted. The blocked ones are the finding, and
one is a fault nothing could previously report: `singmaster`'s
`boundary-finite-collisions` skeleton is headed `sketched` with four open gaps,
while one of the lemmas it rests on is `refuted` — refuted by the run's own
directive 24, whose note says the route was re-derived without it. Nobody
updated the skeleton's dependency list, so the file still says the goal rests on
something known to be false. Read one file at a time that is invisible; as a
graph, refutation propagates upward and the goal comes back broken.

**The Lean check, against the container's own `lean`.** Four probe files —
clean, `sorry`, self-declared `axiom`, `native_decide` — run through the image's
Lean 4 and Mathlib. Two of the four disagreed with the parser:

- Lean writes the warning as ``declaration uses `sorry` ``, with backticks. The
  parser looked for the straight-quoted form, so **no `sorry` was ever
  recorded**. The verdict still came out false, because the same proof also
  prints `sorryAx` — right answer, wrong reason, and an empty `sorries` list on
  the record a later reader is meant to trust.
- A proof needing no axiom at all prints `does not depend on any axioms`, which
  contains neither `axioms:` nor a list. It was read as *no `#print axioms`
  line* and refused. **The strictest possible result was the one result the
  check rejected.**

The third probe is the one the control was written for and it behaved: a
theorem proved from `axiom key_estimate` compiles, warns nothing, and is now
refused by name. The fourth validated the design rather than the code — this
toolchain prints `big._native.native_decide.ax_1_1` for `native_decide`, not the
`Lean.ofReduceBool` the comment predicted, and the check holds anyway because it
names what is *not* on the trusted list rather than denylisting what is.

**The entailment closure could not be tested retrospectively**, and that is
itself a measurement. `follows-from:` is new, so no committed workspace has one
— the closure reports nothing over all eight. Grepping the corpus for
entailments stated in prose finds about 110, of which all but one point at an
*external* theorem ("follows from Theorem 3.2") rather than at a claim the run
holds. The runs almost never wrote an internal derivation down, which is both
why nothing could follow the edges and a caution about the yield: the closure is
worth exactly what the scholar puts into it. Re-run against a copy of the
`gilbreath` library with one edge added where that library's own prose already
states the derivation, it upgrades the consequence and briefs the next attempt
not to prove it again. It also exposed a rendering fault, since fixed: an
entailed claim filed weaker appeared under both *established for free* and
*already entailed*, one heading saying settle it and the other saying it is not
a result.

**A live run, and the third bug.** `./euler 351` — chosen because brute force
over 10^8 is impossible, so the problem has to be reduced before it can be
computed. Eight minutes in, `reducer` wrote its skeleton and the graph was
derived from it correctly: three lemmas ready to be picked up independently, the
goal blocked on all three, which is the right shape for a problem whose whole
difficulty is one summatory-totient evaluation. It also reported eleven edges
resting on things that do not exist — on `is`, on `the`, on `covers`. Asked what
its skeleton rested on, `reducer` had written `rests-on: none (derived/CLAIMS.md
is empty; no claim in the ledger covers this)`, which is a good answer to the
question and not a list, and `identifiers` split it on whitespace. The split is
older than any of this work; the graph is simply the first thing that ever
*read* those edges out loud. Eleven invented faults are worse than none, because
the report that finds a real misspelling is the same report. A field opening
with `none` now lists nothing, a parenthetical is a comment rather than a
member, and a token that is not id-shaped is dropped instead of reported —
while a misspelled id, still id-shaped, is still reported, which is the case
worth keeping. `precedent:` holds URLs rather than ids and needed its own
splitter, which is how the shape rule announced that it was one rule doing two
jobs.

**The fourth bug is the one worth stating plainly: the closure could not have
worked at all.** Eleven minutes in, the run derived `derived/ENTAILMENT.md` and
it was empty — as it is over all eight committed workspaces, and for the same
reason. No prompt in `src/prompts/` contained the string `follows-from`. The
field was parsed, closed transitively, rendered, routed to three roles and
briefed into every attempt, and the one role that writes claim blocks was never
told the field exists. A feature complete in every part except the sentence
asking for it produces exactly the reading a fixture gives: all the code paths
work. `scholar.md` now carries `follows-from` in the block schema and a
paragraph on why to draw the edge, and a test asserts that prompt names every
field the claim parser reads — because a parsed field no prompt asks for is a
field nothing ever writes, and nothing else would have caught it.

**What the two new files cost.** Both are routed narrowly — the graph to the
orchestrator, the goals agent and the reducer, the closure to the orchestrator,
the goals agent and the scholar, and to nobody else, which `dump_prompts`
confirms by name. Over the `gilbreath` library, which is 3.4 MB and the largest
committed, they add about 18,000 tokens across all nineteen assembled prompts
against roughly 731,000 — under three per cent, and the two roles that plan are
where it lands.

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
