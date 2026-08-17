# The solution loop

`orchestrator::solutions` is a `TinyFlows` graph rather than a prompt. This file
records its shape — the fan-out after an attempt, the two child workflows, and
how a failure anywhere inside it is kept from ending a run. Where a pass goes
next, and why each threshold is the number it is, is in
[`routing.md`](routing.md). The working agreement is
[`AGENTS.md`](../AGENTS.md); this file is the part that goes deeper than a rule.

```text
  research ──> seed goals ──> solve ─ done ─> stand down ─> novelty ─> judge ─> report
                                │
                                └─ body ─> attempt ──┬─> reflect ────────┐
                                   ▲                 ├─> patterns ───────┤
                                   │                 ├─> invention ──────┤
                                   │                 ├─> refute ─────────┤
                                   │                 ├─> verify ─────────┼─> merge
                                   │                 ├─> library (opens) ┤     │
                                   │                 └─> goals ─> cadence┘     │
                                   │                                        route
                                   │                                           │
                                   └──── pass <── escalate <── diversify ──────┤
                                   └──── pass <───── solved/retry/... ─────────┘
```

Three stages, and the middle one is one node. **Research** runs once: establish
what the workspace already has, then go looking for what it does not.
**Attempt** is one attempt. **Evaluation** asks seven questions at the same time
and merges their answers before anything routes. Five are about the attempt. The
other two are about the mathematics — is the statement true, and what does the
kernel make of the proposition the most rests on — and are the only scheduled
uses of the engines this image carries. Both are described below.

Three nodes sit on the way *out*, after the loop and before the report, and the
order between them is deliberate.

`stand_down` goes first and does one thing: it cancels the standing teams. They
were always cancelled — but in `orchestrator_runtime`, *after* the whole
workflow returns, and the judge runs inside that workflow. So every cycle a
team took between the loop ending and the judge finishing was work on a question
already answered, and the code looked right where it was.

A live `./euler 351` measured it. The loop recorded `verdict solved` at minute
29, on an answer two independent programs had agreed on at minute 15. Thirty
more sub-agents were spawned over the next 62 minutes, the judge did not start
until minute 92, and the run was killed at 96 — roughly 85% of the wall clock
and $32 of the $35 spent after the problem was solved. A standing team never
retires on its own, by construction: `Completion::Standing` maps "nothing
further to do" to `Idle` rather than `Finished`, because on an open conjecture
there is always one more source to fetch. Nothing but this node ends one.

Cancelling asks rather than kills — a team finishes the cycle it is in and does
not start another. Work already in flight has been paid for and may as well be
filed, and a team torn down mid-write is how a half-written note reaches the
workspace. The call in `orchestrator_runtime` stays as the backstop for paths
that never reach this node, and now reports which case happened, because "the
run finished and the teams were still going" is the thing the pair exists to
make visible.

One more thing came out of that run and is worth stating on its own: for those
62 minutes the console printed no orchestrator line at all. Which node was
holding could not be read off the log, only guessed at from which sub-agents
happened to be spawning. Every step now notes when it is entered and how long it
took — one line per node per pass, against a run that makes a thousand model
calls — so "the run stalled" is a question the log answers rather than a thing
somebody reconstructs afterwards.

`novelty` checks the literature — but only
when the run believes it has solved the problem, which is the exact inverse of
every other sweep here. `open_library` returns early on `state.solved`, so until
this node existed the one moment the literature was most worth reading was the
one moment nothing read it. Tao states the rule about his own work: a proof that
arrived surprisingly quickly is far more often already known, or wrong, than it
is new. `judge` then scores the finished run, and it runs second because "this
was published in 1974" is the single most important thing it could be told
before it does.

`novelty` cannot un-solve the run, and that is the point. What it produces is a
finding filed beside the answer for the reader who has to decide whether to
believe it. A runtime that retracted its own verdict on the strength of a web
search would be trusting a query over a verified program.

The fan-out is the change worth understanding. These arms used to run in a
line, and three of them were not nodes at all — the pattern agent, the inventor,
and the literature rescue were `tokio::spawn`s inside `reflect_step`'s body.
That made the reflection the place every other role was smuggled in: the graph
could not draw them, graph policy could not bound them, and no checkpoint could
land between them. A pass now costs the slowest arm rather than the sum.

Three rules the picture cannot show and the engine will not enforce. Every path
back to the head goes through one node (`pass`), because the engine's `nodes`
map is cumulative and a fold with more than one node to read eventually reads a
stale one. Every evaluation arm reads the *attempt* — not another arm, which may
not have run, and not the head's accumulator, which is a pass behind because the
head folds at the top of a pass. And the merge folds counters by **delta**: each
arm's value minus the base, summed. That is what makes a reset and an increment
compose, which they must, because the reflection zeroes `unproductive` on a
productive attempt while the judge adds one for a restart, from the same base, at
the same time.

`refute` is the sixth, and the one that is not about the attempt. Every other
arm asks how the attempt went; this one asks whether the thing being proved is
true at all, which is a question nothing else in the loop ever puts. The runtime
had four ways to prove something — `sat_solver`, `smt_solver`, `theorem_prover`,
`lean_prover` — and each is *delegated to* when a role decides to ask. None was
ever scheduled *against* the statement the run was pursuing, so a false
conjecture was attacked by proof for as long as the budget lasted.

The measurement that justifies the slot is the Equational Theories Project's:
524 small finite structures refuted 13.6 million of its 22 million implications,
13.3 million at size 3 alone, for 165 CPU-hours, before any clever proof search
ran. Most false statements are false small. What the arm attacks is read off the
two ledgers holding statements somebody committed to proving — the open gaps of
`derived/BACKWARD.md` and the current rung of `derived/WEAKENED.md` — because
those are exactly the propositions worth breaking. Its findings are read back
off disk beside the refuter's report, on the same argument the reduction arm
makes: a role's prose is a summary of its own work and the record is the work.

`verify` is the seventh, and it is the same argument one engine over. `lean.rs`
made a kernel check something the runtime *reads* rather than something a role
reports; it left `lean_check` granted to `lean_prover` and `lean_prover`
delegated to when somebody remembered. So what got formalised was whatever a
model found interesting, and across three live calibration runs the answer was
nothing at all — the strongest artifact this runtime can produce, never once
produced. This arm schedules it.

Three decisions make it affordable on a box with an eight-gigabyte container
cap, and they are the same decision seen from three sides.

**It picks rather than sweeps.** `Blueprint::targets` ranks the statement graph
by Scholze's criterion — *"as it will be used as a black box, a mistake in this
proof could remain uncaught"* — which is direct in-degree, with what the run is
already building on ahead of what it has yet to prove. Direct rather than
transitive, because a node is used as a black box by the nodes that cite it by
name; a transitive count would rank a leaf under a long chain above a lemma six
arguments depend on. He is his own evidence: a weight-monodromy proof that
"passed judgment of top mathematicians, but then it turned out to contain a
fatal mistake". Perelman prices the absence at five years and three teams.

Gauss is the other answer to the same question and the reason this one is
stated as a choice rather than a limit — thousands of concurrent agents, each
with its own Lean runtime, multiple terabytes of cluster RAM, and 25k lines of
Lean for the strong Prime Number Theorem in three weeks. Ranking is what fits
in one container instead. What it gives up is the tail, so the queue is rendered
into `derived/BLUEPRINT.md` under *Verify these first*: a bound that drops work
silently is the failure this repository keeps writing down.

**It asks for something different the second time.** A node that survived a
proof attempt is asked to be *decomposed* — name the sub-lemmas, state each in
Lean, prove what you can, leave `sorry` in what you cannot, and check the
combining step so the shape of the argument is verified while its leaves are
open. The unproved leaves are written as `gap` blocks, so they become blueprint
nodes, and a leaf whose dependencies are settled returns through this same
ranking as `ready` on a later pass. That is Seed-Prover's recursive sketch —
decompose what is too hard, prove the pieces separately — running at the speed
of the loop instead of inside one turn, which is what makes each step of it
checkpointable and each sub-lemma visible to every other role.

**It stops.** `verify::MAX_ATTEMPTS` is two, because there are two things to ask
and no third: a node that survived a proof attempt and a decomposition is one
this run does not know how to break down, and the honest move is to record that
and spend the next check further down the ranking. The attempt is recorded
*before* the prover is delegated to — the ordinary way a turn ends here is the
run cap killing it, which leaves no report, so a record written afterwards would
not exist and the same node would rank first every pass for the rest of the run.
A record that cannot be written means no delegation at all: an attempt the
runtime cannot count is one it cannot stop repeating.

### What one check costs, measured

The first run to use this arm priced it. On `hypercube-induced-degree`, two
schools reached the fan-out ten minutes apart and were assigned different nodes
— `f-lower-bound-ceil-sqrt-n` to `rising-sea` at 59:28, `huang-degree-bounds-lambda`
to `chisel` at 69:34 — which is the lock doing its job: one workspace, two
schools, no collision.

The first closed in about four minutes: three `lean_check` calls, one of them on
a scratch probe, and a passing verdict. The second was still going twenty-seven
minutes later, and not because it was thrashing — it had worked its way down to
writing real lemmas (`sum_half_neigh`, the half-and-half sum collapse) after
twelve probe files spent finding out which Mathlib names exist. One child run,
$2.37, still open.

So a formalisation is an attempt-sized piece of work, not a step inside one:
`docs/calibration.md` measures an attempt at 13–20 minutes, and this sits at the
top of that range or past it. Three consequences the design already reflects, now
with a number behind them. One target per pass is not a concession to memory but
to *time* — two concurrent Mathlib elaborations would not halve this, and the
run has a four-hour ceiling. `MAX_ATTEMPTS` of two bounds a node at roughly an
hour of child time before the ranking moves on. And the arm must never be
awaited by anything: at this cost, a loop that blocked on the kernel would spend
its budget verifying rather than solving.

Most of that time is not proving. It is finding the names: `Mathlib.Data.Nat.Ceil`
and `Mathlib.Algebra.BigOperators.Basic` are both gone from current Mathlib under
those paths, and the prover discovered that a file at a time. The prompt already
offers the cheap route for it — run `lean` through `execute_command` while
iterating, which files no verdict — and the run took it for eleven of its twelve
probes.

### The filename a node is addressed by

The arm has to find a node's source and its verdict again a pass later, so both
paths are *derived* from the node id rather than chosen by the prover: a file a
model named is a file the model has to name identically next pass. Every
character outside the Lean-safe set folds to `_`.

That fold on its own is not injective, and the same run that priced the arm
showed why it has to be. Its ranking held `spectral-interlacing-sqrt-lower-bound/
G-eigenvalue-bounds-degree` beside plain hyphenated siblings, and `a/b` and
`a-b` fold to one `a_b`. Two statements would then share a `.lean` file — the
second overwriting the first's proof — and share an attempt record, so
`verify::attempts` would read the other node's count and the bound would be
spent on whichever asked second. The failure that matters is the last one: a
kernel acceptance read back against the wrong statement, which everything
downstream trusts.

So the readable fold carries a fingerprint of the id it came from —
`cauchy-bound` becomes `code/lean/cauchy_bound-d85af71b.lean`. FNV-1a written
out rather than `DefaultHasher`, whose output std does not promise to keep
stable across releases: this value sits *in a path*, so a run resuming a
workspace under a newer toolchain has to derive the same name the run that wrote
it did, or every node reads as unattempted and the kernel budget is spent twice.
A hash in a filename is a compatibility commitment. A workspace written before
this keeps its counts — the old path is read when the current one is missing,
never written — and `verify::counts` deduplicates on the node id, so a node
filed under both names is one statement in the denominator the judge is given
rather than two.

Choosing and recording are one critical section under `worklock::writes`, taken
at the arm's boundary and released before the delegation. Schools share a
workspace and run this arm concurrently, so without the lock two of them read
the same ranking, see the same zero attempts against the same top-ranked node,
and both spend the scarcest budget in the run proving it. The lock is released
before the prover runs, because the rule that keeps it from deadlocking is that
nothing below a tool-call boundary may take it again.

What the kernel said is read back off disk, beside the prover's report and not
instead of it. The verdicts say what was established; the report says what the
prover believes the Lean statement *means*, which is the judgement no file
records and the one place this arm can still be wrong. A Lean proof of a
neighbouring statement is worth less than no proof, because it reads as a check
that passed.

### The hypothesis blind spot, measured on the first run that used this

The arm's first live target was `f-lower-bound-ceil-sqrt-n` — *f(n) ≥ ⌈√n⌉ for
the hypercube* — and the kernel accepted it: compiled, no `sorry`, `propext,
Classical.choice, Quot.sound`. What it accepted was

```lean
theorem f_lower_bound_ceil_sqrt_n (f : ℕ → ℕ)
    (hspectral : ∀ n, 1 ≤ n → Real.sqrt n ≤ f n) :
    ∀ n, 1 ≤ n → Nat.ceil (Real.sqrt n) ≤ f n
```

`f` is arbitrary. The hypercube is absent. The spectral bound — the half that is
hard — is a hypothesis. The proof is `Nat.ceil_le.mpr`, one line, and it is a
perfectly good theorem: the rounding step is genuinely this node's content once
a sibling node carries the spectral bound, and the run said so at length in the
file's docstring, naming which binder carries which of the claim's hypotheses.

The fault is not in the proof. It is that `Verdict::verified()` passed, so the
claim could be filed `formalised` and the node's standing become `Verified` —
*"the Lean kernel checked it in this workspace"* — for a statement the ledger
makes about the hypercube's `f`.

And the existing control has an exact blind spot here:

```lean
axiom key_estimate : …                  -- caught by untrusted_axioms()
theorem main : … := … key_estimate …

theorem main (key_estimate : …) : …     -- propext, Classical.choice, Quot.sound
```

Both prove a conditional. `#print axioms` sees the first and cannot see the
second; the files differ only in where the assumption sits. `TRUSTED_AXIOMS` is
a careful argument about the first case, and the first live run walked into the
second.

What is built is the surfacing, not the decision: `Verdict::declarations`
records each checked theorem's signature, read from the source rather than from
a second Mathlib elaboration, and a passing verdict that takes arguments says
plainly that a hypothesis among them makes the result conditional. So a row
reading `formalised` now says *of what*.

Deciding it needs two things this runtime does not have. Whether a binder is
data or an assumption is a question for Lean's elaborator, not for a parser —
`(f : ℕ → ℕ)` and `(hspectral : …)` are the same shape in the source. And
whether an assumption is discharged is a question about the statement graph,
which can answer it only once a hypothesis can be matched to a node. Until both
exist, the honest position is that a kernel check establishes what its signature
says and a reader has to look.

### `lean_check` is also the prover's iteration tool

The same run wrote `code/lean/ceil_test.lean` — five `#check` lines, no theorem
— and checked it twice while hunting the right Mathlib import, which is exactly
what a prompt telling it to search Mathlib before proving anything asks for.
Every check files a verdict, so `code/out/lean/` accumulates probes.

That is harmless until something counts them. The judge's briefing did: a run
that probed ten names and proved nothing would report *"10 file(s) handed to the
Lean kernel, 0 of which it accepted"*, which reads as ten failed proofs. The
denominator has to be statements the run was *asked* about, so it comes from
`code/out/verify/` — the attempt records — and the arm's own finding reports the
verdict for the source it commissioned rather than every verdict on disk. A
commissioned source with no verdict is reported as such, because "the prover
never checked the file it was asked to write" is a fact worth having.

One arm is deliberately not awaited. `library` starts a literature sweep and
returns immediately, because a paper is no less relevant for being found a cycle
later — while a report about *this attempt* arriving next cycle is a report
about the wrong attempt. Its findings reach the next attempt through a mailbox.
The `diversify` escalation is the same sweep, awaited: a run that has stopped
making progress should read what it gathered before attempting again.

The graph runtime is `TinyFlows`', reached through `agent::flow`; the agent
turn each node runs is `TinyAgents`'. The two used to be one crate, and the
distinction is worth keeping in mind while reading the rest of this file: every
threshold below bounds a *turn*, and every arrow bounds which turn happens
next.

How the reflection and the judge divide the question between them, what each
verdict routes to, and why every threshold is the number it is — each one
carrying the live run that set it — is in [`routing.md`](routing.md).

## The reduction runs beside the loop too

The decomposition is a child workflow, `orchestrator::workflow_goals`. The loop
calls it twice — once from `start`, before the first attempt, and once after
every reflection — and it answers the question the loop never asks by itself. Every cycle asks how the
last attempt went. None of them asks what a proof of the goal would *consist
of*, and the two have different answers: a run can report genuine progress every
single attempt — a bound pushed further, more cases verified — and spend its
whole budget with a great deal of data and nothing that says what would have
been enough. A live Gilbreath workspace holds exactly that statement, reducing
the conjecture to an event-rate bound, and it took sixteen operator directives
to produce.

Two roles run in that arm now, concurrently, and they share it rather than
getting one node each because they share everything that decides *when* to run:
the same cadence, the same "has the workspace moved" fingerprint, and the same
single-writer gate. A second node whose only difference is which prompt it sends
would be a second answer to the question of how often a run reconsiders what it
is attacking. They are concurrent rather than sequential because the arm is
awaited and neither child reads the other's output, so a pass costs the slower of
the two — the same argument the evaluation fan-out itself is built on.

The `weakener` is the second, and it asks the question the reducer's dual leaves
open. The reducer asks what would be *enough* and answers with lemmas that imply
the goal; the weakener asks what would be *easier* and answers with a target that
deliberately does not. It writes `research/weakened/<slug>.md` — the
difficulties that make the goal hard, then a ladder of rungs each naming which of
them are switched off — and `derived/WEAKENED.md` is derived from those files.
It is deliberately *not* gated on the run being stuck, and that is a lesson this
repository has already paid for: `open_invention`'s stuck-gate was reachable in
principle and not in practice, and across a day of live runs the inventor was
spawned once. A ladder is most useful before the budget has gone on the
full-strength statement, not after.

So the `reducer` is delegated a decomposition: the goal, the lemmas that would
imply it, the inference combining them, and one `gap` per lemma nobody has
proved. It writes `research/backward/<slug>.md`, `derived/BACKWARD.md` is
derived from those files, and the open gaps reach the next attempt under their
own heading — as targets rather than as gathered material, which is why they
travel in a third `Mailbox` rather than in `fresh_context`.

Awaited now, and the change is worth stating precisely because the old reason
for detaching it was real. Nothing in `route` reads a skeleton, so a gap is
worth as much an attempt later — and awaiting a reducer *after* the reflection
put a child run of unbounded length between the reflection and the next attempt,
which is the failure `Mailbox` was written about, where a live run sat 33 minutes
unable to start an attempt it was ready for.

What changed is that it no longer runs after the reflection. It runs *with* it,
as one of the evaluation arms, so a pass costs the slowest arm rather than the
sum and the next attempt sees this cycle's skeleton instead of the previous
cycle's. The cadence is what keeps that affordable: most cycles hold, and a
cycle that holds costs one expression.

Three conditions, because there are three separate ways this goes wrong. The
first is in the child's opening `switch`, as jq, because "how often" is the
decision an operator most wants to change without a rebuild. The other two are in
`reduce_arm`, because a workspace that has not moved and a reducer already in
flight are facts about the world rather than about the loop's state, and neither
is expressible as an expression over an accumulator.

`REDUCTION_INTERVAL = 3` bounds what the ledger *costs*. It is the one threshold
here that is not two, and deliberately: every two answers "is this a pattern or a
one-off", and this is a refresh interval on a document whose inputs move slowly.
A skeleton is worth rewriting only once something has landed that could discharge
one of its gaps, which takes a full cycle plus whatever the standing teams
delivered beside it. Against `MAX_ATTEMPTS = 8` it buys two or three skeletons.
Because the arm is detached the interval bounds spend rather than latency, so it
is set on what the ledger costs rather than on how long the loop can afford to
wait. `since_reduction` starts *at* the threshold, and the `seed_goals` node runs
the child from that state before the loop starts, so the first skeleton is
written beside the first attempt rather than after it. Waiting for a completed cycle was the
same mistake `open_invention` recorded one role wider: on a conjecture run an
attempt/judge/reflect pass is the better part of an hour, and every role spent it
working without a statement of what would be enough. Nothing justified the wait —
the reducer works backward from the problem statement, so its input is present
before the run starts, and the arm is detached, so opening it early delays the
graph by nothing. It goes through the same gate as every later reduction, so the
first completed cycle cannot open a second on top of it, and a resumed workspace
is decomposed from what is already on disk rather than from the statement alone.

A workspace fingerprint bounds *waste*. The reducer's inputs are what the run has
established, so a tick over a tree that has not moved would rewrite the same
skeleton from the same evidence. `fingerprint_excluding` skips what the reducer
itself writes, or it would wake forever on its own output — the pattern team's
`results_unchanged` argument applied one folder wider. A declined tick
deliberately does *not* reset the counter, so the next cycle asks again rather
than waiting another full interval for evidence that may have arrived meanwhile.

`ReductionGate` bounds *collision*, and this is the one `open_invention` does not
need. Two inventors produce two approach files under two slugs, which is untidy.
Two reducers decompose the same goal, so they write the same file,
`write_document` is last-writer-wins, and the loser's gaps are gone with no error
anywhere — two containers on one workspace, one level down. The gate is claimed
before the spawn and released inside it, so a reduction outliving the cycle that
opened it still holds it.

`ensure_skeleton_written` is the same control `ensure_approaches_written` is,
with the discriminator inverted and for a stated reason. Approaches compare
*names added*, because proposing means new files. That is wrong here from the
second cadence onward: refining a live skeleton — closing a gap, adding a lemma
the run now needs — is exactly the correct work and adds no name. So it compares
a fingerprint of every `(skeleton, gap, status)` triple, which is strictly
stronger: an unchanged fingerprint means the turn moved nothing any downstream
reader consumes, whatever it did to the bytes. A plain before-and-after
comparison is sound in a runtime where everything else is racing because that
folder has exactly one writer and the gate admits one of it at a time.

What travels back is read off disk rather than taken from the reply, so a turn
that wrote good files and then produced a truncated report still delivers its
gaps.

`COMPUTATIONAL_THRESHOLD` is the second way into this step, and it exists because
"did the attempt establish something new" and "is the run getting anywhere"
turned out to be different questions and `route` only asked the first. Pushing an
exhaustive search from n=14 to n=16 honestly establishes something the run did
not have, so reflection answers `PROGRESS: YES`, which resets `unproductive` —
and since `unproductive >= STUCK_THRESHOLD` was the only route to `diversify`, a
run scaling one method never reached the inventor at all. It could spend its
whole budget that way, every attempt progressing and the method never changing. Reflection now also answers `KIND: MATHEMATICAL |
COMPUTATIONAL | NONE`, and two consecutive COMPUTATIONAL answers route here. The
parse is conservative: only an explicit, recognised answer moves the counter, so
a reflection the loop cannot read never drives it — treating silence as "scaling
again" would divert a working run on two malformed replies.

A provider wall is not a failed attempt, and the loop must not spend the attempt
ceiling discovering that. `delegate` turns a child's failure into text so the
loop survives it, which is right, but it makes an outage indistinguishable from a
poor attempt unless something reads the text. Two live runs met `HTTP 403: Key
limit exceeded` and burned all eight attempts in seconds — each recording the
same quota error as the lesson, each reflection failing the same way — and ended
reporting "not solved within 8 attempts", which reads as a mathematical failure
and was not one.
`provider_blocked` recognises the shape `delegate` writes, `route` checks it
before anything else including the ceiling, and `BLOCKED_THRESHOLD` is two
rather than one because a single upstream blip is precisely what the retry
ladder and `ReroutingModel` exist to absorb. The detector is deliberately
narrow — the failure wrapper must be present and the report substantially
nothing else — because a false positive stops a run that was working, which is
worse than the wasted attempts it prevents. The outcome says so in words: an
infrastructure failure, the workspace unchanged, the run continuing from disk
once calls are accepted again.

Keep the routing policy in `route` a plain function of the state. It is the part
of this design most likely to be wrong and the part a live run is least able to
demonstrate cheaply, so it must stay unit-testable without a provider. Two rules
in it are load-bearing: an unparsable verdict must not count as solved, and the
attempt ceiling must outrank the stuck rule or the loop can diversify forever.

The loop is the only execution path. Do not add a single-turn mode back: it
differed only in discarding the reflection, and a switch between them is one
more thing to get wrong.

## Judging before the attempt returns

The judge scores an attempt when the attempt returns, and the attempt is a single `goals` run told to pursue the goal until it is met. On an open conjecture it is never met. Four live runs sat inside attempt 1 for thirty-six minutes with zero judge verdicts, zero reflections and zero inventor spawns between them, while all the work happened in children the attempt had spawned — 231 model calls, 47 searches and 36 downloads on one of them, none of it ever assessed. `open_invention` needs a completed cycle and `diversify` needs two consecutive stuck attempts, so both were unreachable by construction.

Two changes make the loop turn over. The run wall clock is thirty minutes rather than two hours, so an attempt concludes and is judged four times in the span it used to be judged once. And a `review` team runs beside the solve every twenty minutes (`MATH_AGENT_REVIEW_MINUTES`), spawning the judge against the workspace as it stands and posting the verdict into the mailbox the attempt already drains.

This team and the loop's own `judge` arm are now the same role asked the same kind of question from two places, and the same is true of `patterns`/`eval_patterns`, `context`/`init_context`, and `research`/`eval_library`. Four of the five standing teams overlap an arm. The teams are idle-gated on a workspace fingerprint so the duplication is bounded rather than doubled, but it is duplication nobody chose, and on a run whose binding constraint is its budget it should be resolved by measurement rather than left standing. It asks the three questions worth asking mid-flight: whether the method can settle the question or is scaling something that already failed smaller, whether what the run believes is supported by what it computed, and what the single most valuable next move is.

The review is the judge rather than a second solver, so it inherits `RunBudget::for_judging` — twelve model calls and a five-minute ceiling — and an unchanged workspace is skipped before the agent runs rather than by asking a model to notice. The wall-clock change is the one with a cost: it bounds every agent run, not only the attempt, and a live `tool_builder` spent 1,362 seconds inside a single model call. That path does not honour `StopWithPartial`, so a child that meets it loses its context and its report — but not its files, and `continuation_briefing` is what lets the next attempt resume from them.

That cost is also why the judge is handed `evidence_briefing`. The cap makes a lost report the *normal* ending rather than an edge case, so a judge reading only the report is normally reading nothing — which is what produced three 1/5-and-2/5 verdicts in one evening against workspaces holding verified exact values and exhaustive enumerations.

## Direction from a human

Until this existed a run was closed once it started. It was launched with argv,
nothing read standard input or watched a control file, the budget variables were
read at launch, and every role's system prompt was assembled once — so editing
`GOAL.md` on the host mid-run changed nothing, because the file had already been
read into every system message that would ever be sent. Someone watching a run
take a wrong turn could only keep watching.

A directive is the input that was missing. `./steer` and the `i` key in
`./euler-tui` both call `math_agent::directives::enqueue`, which appends one
JSON object to `config/directives.jsonl` in the workspace the container has
mounted. That mount is the only thing crossing the sandbox boundary, and it is
worth keeping that way: an inbound port would be the first hole in a container
that drops every capability, runs a read-only root filesystem, and mounts
exactly one directory, and it would buy nothing a file does not already give.

The queue has one writer on each side. The host only ever appends to
`directives.jsonl`; the runtime only ever writes `config/.directives-cursor`,
which counts the lines it has consumed. Neither side needs a lock because neither
writes what the other writes, and the one number they share is owned by the side
that advances it. A directive's identifier is its line number rather than a
stored field, so a line the reader cannot parse is skipped *and still counted* —
a torn append, which a checkpoint commit landing mid-write could produce, costs
one directive rather than the alignment of every later one.

### Two deliveries, deliberately unequal

Nothing waits for a person. That is the same decision the `Mailbox` records for
the pattern team — a live run spent 56 of its 74 minutes unable to start its
second attempt because a support agent had been made a gate — and a human is
slower than any support agent, so a loop that blocked on one would be that
failure with no ceiling at all.

**Verbatim, to the next attempt.** The `director` team drains the queue and posts
the text, unchanged, to a second `Mailbox`. `attempt_step` collects it and
`direction_briefing` renders it above the judge's steer, labelled as coming from
the operator and as taking precedence. The attempt is the only collector, unlike
the pattern mailbox reflection drains as well: reflection folds what it collects
into `fresh_context`, which reaches the next attempt as *material gathered*
rather than as an instruction, and losing that distinction would lose the only
thing this channel exists to carry.

**Interpreted, to the workspace.** The same drain then runs the `director`
agent, which reads the workspace and changes the files that decide what happens
next — `derived/TASKS.md`, a thread under `research/threads/`, `CONTEXT.md`, a
`request_research`. Those edits reach the other standing teams for free, because
they already gate on workspace fingerprints. The ordering matters: the mailbox
is posted *before* the agent runs, so the next attempt gets what was typed even
when the director's own model call fails. A directive is the one input to a run
that cannot be regenerated.

### What it deliberately cannot do

- **Change routing.** `route` stays a pure function of state, and the
  `SOLVED`-needs-a-program evidence gate is untouched. A human cannot force
  diversification, reject a verdict, or end the run through this channel.
- **Become a claim.** A directive is asserted, never established. The `director`
  is not given `derived/CLAIMS.md`, so the role acting on an unevidenced
  instruction is not also holding the evidence ledger.
- **Compute.** No shell, no `write_tool_file`, no delegation. A role that could
  both reinterpret the goal and run programs against it would be a second
  investigation answering to nobody.
- **Redirect the attempt itself, mid-turn.** The attempt is briefed at its own
  boundary through the mailbox, and a live attempt has run forty minutes. The
  director's file edits remain the mitigation for that one — they land within a
  team cycle and are visible to any role that reads the workspace.

### The third delivery, and the runs that were missing it

The two deliveries above both stop at the orchestrator. That was recorded here
as an accepted limit, on the argument that reaching further would mean driving
`AsyncSubagentManager::steer` from *outside* the run, where no handle exists.
The argument was right about the outside and wrong about the cost, and two live
investigations paid it.

A detached specialist holds the instruction it was spawned with. It does not
re-read the mailbox, and it does not read `derived/TASKS.md` mid-run. So a directive
aimed at a role already working never arrived: the loop wrote it to
`config/DIRECTIVES.md`, the director rewrote the task ledger, the operator saw a
receipt — and the role carried on. In the `gilbreath-supply` second pass a
`tool_builder` produced **eight** artifacts re-confirming a settled number
across three consecutive directives telling it to stop, each of which was
acknowledged in the ledger. The same shape had already cost the first pass a
comparable stretch on scratch-file consolidation, where a directory grew
31 → 35 → 47 → 52 files under four directives asking for the opposite.

`deliver_to_live_runs` closes it, from *inside* the drain where the manager is
in scope. Every run still `Pending` or `Running` is sent the directive text as
its own `SteeringCommand::Redirect`, prefixed to say it outranks the instruction
the run was spawned with. Three properties are load-bearing:

- **A terminal run is skipped, not an error.** The queue's exactly-once
  guarantee is the cursor; a specialist finishing between the drain and the
  redirect is ordinary. Erroring there would let one finished role suppress the
  directive for every other.
- **The count is traced, never assumed.** `directive N delivered to K live
  run(s)` is what separates a directive nothing was working to receive from one
  that reached the role it was written for. Without it, an operator is back to
  inferring delivery from behaviour, which is exactly how the failure survived
  two investigations.
- **It does not widen what a directive may do.** The text is the same text, and
  it arrives as an instruction to a role that already has its own tools. No new
  capability reaches anything.

`async_subagents::test::a_directive_reaches_every_live_run` pins the delivery,
and `a_finished_run_is_skipped_rather_than_failing_the_delivery` pins the
skip — the second matters more, because it is the one a plausible "return an
error on any unreachable run" implementation gets wrong.

The director's `TeamBudget::attentive()` is the one allowance shaped by waiting
rather than working: every cycle counts including idle ones, so a custodial
forty-cycle budget would have retired the team thirteen minutes into an eight-hour
run with nothing saying direction had stopped being read. What bounds its
spending instead is `directives_waiting`, a file read in front of the model call —
the same shape as the fingerprint gates beside it.

`config/DIRECTIVES.md` records every directive and what became of it, including
a cycle that failed. On a channel that never blocks that receipt is not
decoration: without it an operator cannot tell "not picked up yet" from
"silently dropped", and only one of those needs acting on.

## Failure handling

A recoverable tool failure must never end a run. Tools are registered through
`ResilientTool`, which turns an `Err` into a `ToolResult` carrying the error so
the model can correct itself; `ReflectionMiddleware` then appends advice, and
escalates when the same tool fails repeatedly. Before this existed, a Qdrant
`409`, a `/workspace/`-prefixed path, a `403`, and a non-UTF-8 download each
destroyed an entire run's accumulated work. Do not reintroduce a tool whose
argument or transport failure propagates out of the run.

A model error is the same class of loss one level up. It propagates out of a
child run as that child's whole result, so a specialist that meets one on its
first turn dies before doing anything and the solution loop records the attempt
that delegated to it as having executed nothing. `ReroutingModel`
(`src/agent/reroute.rs`) closes the one case the retry ladder cannot:
`OpenRouter` reports an upstream provider's failure as its own HTTP 400
carrying `Provider returned error`, and a 400 is classified as permanent, so
nothing retried it. It is matched on the status *and* the message, because a
genuine request-shape 400 is permanent and retrying it would replace a fast
honest failure with a slow identical one. It wraps outermost so each retry
passes back through the affinity wrapper's one-request block and reaches a
different provider rather than the one that just failed.

The runtime image must expose both `python` and `python3`, plus `pip` and
`pip3`. Pip installs belong under `/workspace/.python-packages`; do not make the
container root filesystem writable for package installation.

The scientific stack — `sympy`, `numpy`, `scipy`, `gmpy2`, `networkx` — is baked
into the image from apt rather than installed per run. A run that has to install
`sympy` before it can factor anything spends minutes of its budget on setup,
fails outright when the index is slow, and every workspace pays again. They come
from apt rather than pip because the container root filesystem is read-only at
runtime, so system packages are the only ones importable without writing to
`/workspace` first.

The constraint stack sits beside it for the same reason and pays for the
`sat_solver` role: `python3-z3`, `python3-pulp`, `python3-pycosat`,
`python3-igraph`, the `z3`, `cvc5`, `minisat`, `cryptominisat`, `glpsol`, and
`cbc` binaries, and `nauty` — whose Debian binaries are prefixed, so it is
`nauty-geng`, not `geng`. CP-SAT (`ortools`) and PySAT (`python-sat`) come from
pip at *build* time, into the system site-packages, because Debian ships
neither: `apt-cache show python3-ortools` resolves as a name and has no
installation candidate. Exhaustive generation up to isomorphism is what turns a
solver's `UNSAT` from an assertion into a cross-checked bound, which is why
`nauty` is here rather than left to a hand-rolled generator grinding through
`n!` relabellings.

Lean 4 with a pre-built Mathlib is the largest thing in the image and pays for
`lean_prover`. `lake exe cache get` downloads the compiled `.olean` files
rather than building Mathlib from source; the difference is minutes against
many hours. Two details are load-bearing. `elan default` is set globally rather
than as a directory override, because an override is scoped to `/opt/mathlib4`
and every agent's working directory is `/workspace`, where `lean` would
otherwise fail with "no default toolchain configured". And `lean` is a wrapper
script rather than an `ENV LEAN_PATH`, because the value is the search path of
every Mathlib dependency and is known only after the build ran — `ENV` cannot
take a command substitution, and without the full path an `import Mathlib.…`
fails on `unknown module prefix 'Batteries'`, which reads as a broken install
rather than a missing variable. The image is smoke-tested on both at build time,
so a Lean install that cannot import Mathlib fails the build rather than the run.

Two more failure modes on the same class of tool are worth stating: a truncated
tool call and a corrupt document index. Both are covered under the reflection
middleware and `documents.rs` respectively, and neither may end a run.
