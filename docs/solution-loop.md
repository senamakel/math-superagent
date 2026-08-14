# The solution loop

`orchestrator::solutions` is a `TinyFlows` graph rather than a prompt. This file
records how it routes, why each threshold is the number it is, and how a failure
anywhere inside it is kept from ending a run. The working agreement is
[`AGENTS.md`](../AGENTS.md); this file is the part that goes deeper than a rule.

```text
  research ──> seed goals ──> solve ─── done ──> report
                                │
                                └─ body ─> attempt ──┬─> reflect ────────┐
                                   ▲                 ├─> patterns ───────┤
                                   │                 ├─> invention ──────┤
                                   │                 ├─> refute ─────────┼─> merge
                                   │                 ├─> library (opens) ┤     │
                                   │                 └─> goals ─> cadence┘     │
                                   │                                        route
                                   │                                           │
                                   └──── pass <── escalate <── diversify ──────┤
                                   └──── pass <───── solved/retry/... ─────────┘
```

Three stages, and the middle one is one node. **Research** runs once: establish
what the workspace already has, then go looking for what it does not.
**Attempt** is one attempt. **Evaluation** asks six questions at the same time
and merges their answers before anything routes. Five are about the attempt;
the sixth is not, and is described below.

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
`research/BACKWARD.md` and the current rung of `research/WEAKENED.md` — because
those are exactly the propositions worth breaking. Its findings are read back
off disk beside the refuter's report, on the same argument the reduction arm
makes: a role's prose is a summary of its own work and the record is the work.

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

The judge and the reflection answer different questions. Reflection asks
whether the answer is right and what the run learned, and it alone can end the
loop. The judge asks whether the attempt was *conducted* in a way the next one
should inherit: it scores it out of five against what the attempt actually did
— executed and checked, executed but thin, wrote code without running it, prose
only — and returns PROCEED, STEER, or RESTART. STEER's one sentence is carried
into the next attempt's prompt.

RESTART is no longer a *route*, and that follows from the fan-out rather than
being a decision about restarts. The judge ran first while the two were in a
line, so a restart could skip the reflection and save a call; they are
concurrent now, so by the time anything routes the reflection has already
happened and there is nothing left to skip. What a restart does is everything
`judge_step` writes: the direction is discarded, the steer is set for the next
attempt, `restarts` is incremented, and the attempt is marked unproductive.
`MAX_RESTARTS` is enforced there, and always was — the ladder's copy of it was
belt-and-braces. There is one ladder now, and `orchestrator::parity` holds the
engine's jq to it.

It is given the workspace as well as the report, because the report is the first
thing lost: the ordinary way an attempt ends is the run cap killing it, which
destroys its context and its report and leaves every file it wrote. One evening
all three live Euler attempts died at exactly 30:00 and every verdict that
followed was 1/5 or 2/5 with "progress no" — one against a workspace holding both
check values its problem supplied, reproduced to ten digits, and 38 points
cross-validated two ways. The judge was scoring silence. `evidence_briefing`
counts what is on disk — captured output, claims split by whether the run
established or read them, approaches, threads — and says which to believe when
the two disagree. It counts and never reads: what a file *means* is the
judgement the judge is about to make; whether the attempt executed, established,
or proposed anything is not.

Captured output is every non-source, non-note file under `code/`, not `code/out/`
alone. The layout says outputs belong in `code/out/`; PE761 writes
`code/<program>_OUTPUT.txt` beside each program and left one empty `Untitled` in
`code/out/`, so a check reading only the tidy location reported a run with six
captured outputs as having produced nothing. A check that only sees the tidy
layout reports the untidy run as idle, which is the opposite of the truth.

Two faults ride along with the counts. The first is `code/` holding `brute.py`
and a faster program while no captured output names the oracle: keeping the naive
oracle was enforced, agreeing with it was not, and PE241's `solution.py`
justified its pruning with a falsehood (no later σ factor supplies the cancelling
prime, when σ(13) = 14) and found 5 of 9 terms below 10⁸. The second is the
question after it — the oracle *was* run and disagreed. PE761's
`indep_game_encoding_OUTPUT.txt` reads `agree? False` on every line, its only
independent solver returning 4.14159265 for the circle against a published
4.60333885, and nothing in the runtime read a word of it while the loop's
verdicts were decided by a report that never mentioned the file. Markers pair a
comparison word with a negative (`agree? false`, `mismatch`, `does not match`)
rather than standing on one: a bare `FAIL` is what an honest classification row
says — PE761's own `20 - FAIL - - NotAlgebraic` — and reading that as a broken
check would cry wolf on every run that enumerates cases properly. Whether the
disagreement is fatal stays the judge's call; a deliberately falsified model
*should* print that it disagrees. What is counted is that the words are there.

The judge runs on a narrowed budget (`RunBudget::for_judging`): twelve model
calls and five minutes, against an attempt that takes the better part of an hour.
It reads a report and answers in four lines, so an investigation's budget is the
wrong size for it — and left with one, it investigates. A live judge spent four
minutes, fifteen model calls, and a 6,906-token turn reading `CONTEXT.md` and the
programs the attempt had written, while the finished attempt waited on it. This
is also why the evidence above is counted for it rather than left to it to go and
find. The tight cap is safe by construction: the run stops with partial results,
a judge cut off before its verdict returns something unparsable, and an
unparsable verdict is PROCEED.

Three rules in it are load-bearing. An unreadable reply is PROCEED, in the same
spirit as an unparsable verdict not counting as solved: a judge the loop cannot
read must not throw work away by accident. `MAX_RESTARTS` is two, because a judge
that dislikes the run's whole approach would otherwise reset it until the attempt
ceiling stopped the loop, and the run would end having explored nothing to its
conclusion. And the attempt ceiling outranks a restart — a run on its last
attempt reflects on what it has rather than stopping with nothing.

The prompt makes the judge reluctant rather than exacting. It is told to assume
the attempt was reasonable, that most are, and that a run which computed the
wrong thing or ended blocked has still done its job. RESTART is reserved for
five named faults in the *conduct* of a run — an answer no executed program
produced, a method that searches the answer space, a verification that checks a
program against itself, building on a belief already disproved, or a computation
run at a larger size than an earlier one without naming what the larger run
settles — and if it cannot name which occurred and point at the words showing
it, the verdict is PROCEED.

The score is not purely an execution ladder any more, and that was deliberate.
Every rung above 2 required "executed", which is right for the failure it was
written against — a small fast model reporting an answer nobody computed — but
it meant a new reformulation with a citation and a first step could score at
most 2, so the only scoreable act was running something. A run stuck scaling one
method had no way to be credited for the thing that would get it unstuck. A
reformulation now reaches 4 when it is checkable — named in mathematics, with
cited precedent, a reason it fits, a first step, and an alternative closed with
its reason — and 3 when nobody took it to the literature or weighed it against
anything. A suggestion to think differently still scores 1. The judge is
deliberately not routed `research/APPROACHES.md`: a judge holding the ledger
would credit an attempt for the *content* of approaches the report never
mentions. It is given their number, which is a narrower thing and answers a
question the report cannot when the run cap has destroyed it — whether the
attempt left anything behind at all. The original rule assumed a report exists;
where one does not, "the evidence has to be in the report" means no evidence.

Reflection answers in four verdicts now, and the fourth is the only one checked
against the workspace rather than against itself. `solved` was binary, so a run
that proved a weakened case, established a conditional result, or ruled a method
out with a reason had exactly one word available: unsolved. That is not how the
problems this runtime is pointed at are actually made progress on. Greenfeld and
Tao published two no-go results before the periodic tiling counterexample, and
the 2021 rigidity result is what told them their Wang-tile encoding could not
work and to switch to a Sudoku one — scored here, both would have read as
failures.

`BANKED` says the attempt settled something short of the goal. It never ends the
run, so a wrong one costs an attempt of optimism rather than a wrong final
answer. But it counts as progress, and progress resets `unproductive`, which is
the only route into `diversify` — so a verdict a model could assert freely would
let a stuck run keep itself out of diversification indefinitely by claiming a
small win every cycle. That is the failure `COMPUTATIONAL_THRESHOLD` was added to
close, one verdict wider. So it is honoured only when the claim ledger actually
grew: `established()` counts proved, formalised, and checked claims, and it is
derived from the notes on disk rather than from anything the reply says. A
`BANKED` over an unchanged ledger is rejected with a lesson naming what was
missing — a result that exists only in an attempt's report is lost when the
attempt ends. Nothing in `route` reads the counter, so the routing policy and its
parity harness are untouched; what it changes is what an attempt is credited for.

The three that were there first are unchanged. SOLVED needs a specific final
answer *and* a second independent route, and it needs a program on disk — a
claimed answer with nothing executable in the workspace is rejected outright, and
that gate covers the third verdict too. It also needs the reflection to agree
with itself: `SOLVED` beside `PROGRESS: NO` is rejected, because solving the
problem is progress and a reply asserting both is contradicting itself. A live
Gilbreath run ended on exactly that. Its `goals` agent timed out, the salvage
path re-ran an already-queued script that re-confirmed an already-hand-checked
refutation, and the reflection wrote SOLVED over PROGRESS: NO. The program gate
did not catch it, because the salvage really had run a program — what no file on
disk can show is that it established nothing the run already had. The reflection
knew, and said so in the lesson it left for the next attempt, but the verdict had
already routed the run to `done`. All three conditions exist because a live run
ended on the case each one rules out. UNVERIFIED is the third: a specific final
answer that exactly one route supports, where the reflection can say concretely
why no second route is available. Said twice it routes to `Route::Reported`,
which is terminal, and the run ends saying what it has and what is missing.

The loop had two words for an attempt and needed three. PE761 reached
`V_hexagon = 5.05505046`, reduced it to the exact surd `2 + 2√21/3`, and
reproduced the formula's published anchors at n=3, n=4 and n→∞ — and could not
close, correctly, because the value rests on one Math.SE answer while Abel et al.
(arXiv:2007.08965) list regular n-gons with n>4 as an open problem. There is no
second route to build. With only SOLVED and UNSOLVED available the loop said
retry, and would have spent every remaining attempt re-deriving a number already
on disk, its own workspace recording the contradiction: `GOAL.md` ticking
"verified by a second independent route" while `CONTEXT.md` called that an
overclaim. `Route::Reported` sits above both stuck arms deliberately — an attempt
reaching the answer it already had reports no progress, so `unproductive` is
exactly what an UNVERIFIED run accumulates, and diversifying on it spends three
child runs hunting a new line of attack on a problem whose answer is settled.
`UNVERIFIED_THRESHOLD` is two on the same evidence bar as every other threshold
here: once is an attempt saying it could not find a second route, twice is the
run having tried.

Reflection runs after *every* attempt, not only after a failure, because the
lesson from a partial success is what stops the next attempt repeating it. The
pattern agent runs concurrently with it, on the same attempt, for the same
reason: the exploitable regularity in a sequence is usually visible in the
first few terms a run computes, and waiting for the loop to get stuck means
spending the budget the pattern would have saved. They run in parallel because
neither reads the other's output and reflection is on the critical path of
every attempt.

Past `RESEARCH_RESCUE_ATTEMPTS` — five — each reflection also re-opens the
literature. Diversification triggers on *consecutive* unproductive attempts, so a
run making thin but genuine progress every time never reaches it and can grind
most of its budget on a method that was never going to arrive. The search is
re-run rather than recalled because the workspace has changed: by then the run
knows what it tried, what failed, and what the numbers look like, a far better
query than anything available at the start. `MAX_ATTEMPTS` is eight so the rescue
has attempts left to pay off in; a ceiling that tripped first would buy a fresh
literature search and then stop.

Housekeeping runs on a narrowed budget, `RunBudget::for_housekeeping` — 25
model calls and 300 tool calls, and deliberately *no* wall-clock ceiling — for
the same reason the judge does.
Filing is bounded work — read a listing, write a row per file — and a role left
with an investigation's budget investigates. The measurement that forced this is
worth keeping: two live runs spent 60% and 64% of every model call they made
inside the organizer, and the cause was *not* frequency, since it ran nine and
ten times. It ran long: one organizer run spent 62 model calls tidying, another
56, against a solve that had spent 14 on the mathematics. Reaching the cap is
safe — `StopWithPartial` keeps the rows already written, and a file left
undescribed shows as a visible gap rather than an index quietly disagreeing with
its folder, which the index tools were designed around anyway.

The wall clock is left alone on purpose, and the attempt to narrow it is worth
recording because it made things worse. A ten-minute housekeeping ceiling looked
consistent with 25 model calls and was not: at the turn lengths this runtime
actually sees, 25 calls do not fit in ten minutes, so the organizer reliably met
the clock instead of the call cap. Two live organizer runs died on `run timed
out: exceeded its remaining wall-clock` after spending 20 and 13 model calls
each, and because the wall-clock path does not honour `StopWithPartial`, every
row they had written was discarded and the filing had to be done again — which
is how a cap meant to *reduce* organizer cost raised its share from 49% to 52%.
Whatever else a narrowed budget bounds, the graceful cap must be the one that
trips.

Frequency is gated separately, on the workspace having changed, and the gate is
shared. Filing is cheap to *do* and expensive to *decide*: an organizer asked to
notice that nothing has changed must walk the workspace and spend a model call to
discover it, which is most of what a cycle costs. Two live runs spent 49% and 38%
of every model call they made on the organizer, against 11% and 4% on the agent
actually solving the problem — and the indexes still carried undescribed rows, so
the budget did not even buy the filing. `filing_unchanged` fingerprints
the tree, `INDEX.md` excluded, and both the standing `background` team and the
follow-up consult the *same* fingerprint: two separate gates would each read the
other's filing as new work and wake each other indefinitely. Excluding
`INDEX.md` is the load-bearing part — it is what the organizer writes, so
counting it would have the team waking itself forever on the filing it just did,
which is the pattern team's `SCRATCHPAD.md` lesson one folder wider.

A finished `tool_builder` run automatically triggers an `organizer` run, and a
finished `research` run triggers a `scholar` then an `organizer` (`FOLLOW_UPS` in
`src/orchestrator/async_subagents.rs`). That moment is when the workspace is
least tidy and most legible — the files are new and their purpose is settled —
and leaving the tidying to whoever runs next means it competes with mathematics
and loses. The follow-up is fire-and-forget, so
`await_agent` returns as soon as the tool-builder itself is done and
housekeeping never sits on the critical path; it is spawned separately so the
tool-builder's concurrency slot is released first; and follow-ups are
serialised, because two organizers refreshing one `INDEX.md` at once would each
write the list it read and the later write would drop the other's descriptions.
A follow-up that was itself followed up would tidy forever, so the chain is
asserted acyclic in a test.

A trigger's follow-ups are a *sequence*, run in order inside one lock acquisition
rather than each triggering the next. Order is the point after research:
acquiring is not reading, so the scholar says what each new source establishes
before the organizer files it, and an organizer running first would index
excerpts nobody had read. A sequence rather than a chain keeps the acyclic
invariant simple — no follow-up agent is itself a trigger — and a failed step
does not cancel the rest.

The first attempt also opens its own oracle run. The method policy's first step
is a naive program executed against the statement's worked examples, and the
goals agent is asked to delegate that immediately; two live runs instead spent
ten minutes each on `read_document` and `list_workspace`, and both burned a
whole 12,000-token turn on hidden reasoning without emitting a tool call. Two
prompt revisions failed to move it, so `attempt_step` stopped asking and spawns
the oracle itself — fire-and-forget, first attempt only, never blocking. If the
goals agent does delegate promptly the two simply agree: a duplicate oracle
costs one child run, where no oracle at all costs the whole attempt.

The pattern agent is a *team*, not a step. It runs its own async loop beside the
solve — like research and background — cycling on its own cadence over whatever
results are on disk, and posts what it finds to a mailbox the loop drains at the
next `attempt` or `reflect`, whichever reaches it first. Nothing waits on it: a
structural observation is worth as much an attempt later, and an earlier version
that gated the loop on one cost a live run half an hour of stalled solve.

Reflection was the only collector, making the team's findings reachable exactly
once per *completed* attempt — so a run whose first attempt is long never saw
them. A live Erdős–Gyárfás run spent forty minutes in attempt 1 while its pattern
team computed the C₄-free survivor counts, matched the sequence against OEIS and
pushed it past the terms that suggested it; none of it reached the `goals` agent
directing the work, which re-commissioned the same `nauty-geng` enumeration from
`tool_builder`. Draining at the attempt costs nothing when reflection has already
run — the mailbox is empty and the section omitted rather than rendered as a
heading announcing that no analysis arrived — and it is the only path that exists
on the first attempt of every run.
`attempt_prompt` is a plain function of the state for the same reason `route` is:
what an attempt is actually told must be testable without a provider. An invented
pattern costs the run more than no pattern, so it idles readily — and idleness is
decided *before* the agent runs, by fingerprinting `code/` and `code/out/` and
comparing against what the team last analysed. Asking the agent to notice that
nothing changed would cost a model call and a walk of the workspace, most of what
a working cycle costs: a live team spent thirty `read_document` calls in two
minutes doing exactly that on runs that had computed almost nothing. A workspace with no results at
all reads as unchanged, so an early cycle idles rather than analysing an empty
folder. Its own notes are deliberately not part of the fingerprint — the team
writes those itself, and including them would have it waking itself forever on
its own notes. That is now free rather than arranged: its scratch went to
`note_scratch` and is no longer a file in the workspace at all.

`CONTEXT.md` has an owner — the standing `context` team, running
`context_curator` every `MATH_AGENT_CONTEXT_MINUTES`. Why it exists, what it
may reach, and why it runs on the housekeeping budget are in
[`docs/roles.md`](roles.md#the-standing-teams-run-on-a-custodial-budget).

`diversify` runs three arms concurrently — the librarian followed by the
scholar, the pattern agent, and the invention exchange — and it is the step that
breaks a loop reflection alone cannot.

The invention exchange also runs at the end of *every* completed cycle, not only
a stuck one. That gate was reachable in principle and not in practice:
`diversify` needs two consecutive unproductive attempts, which needs two
completed attempt/judge/reflect cycles, and a run whose attempts take the better
part of an hour spends its whole wall clock inside the first one. Across a day of
live runs on three workspaces the inventor was spawned once, and
`research/approaches/` — the ledger it writes — never existed on disk. The
cheapest question in the runtime, "is there a different line of attack", was the
one never asked.

`open_invention` is the pattern agent's argument one role wider. A proposal is
worth as much an attempt later, so nothing waits on it: the arm is detached at
the end of `reflect` and its report is posted to the same mailbox the next
attempt drains, which is why that briefing names neither role and says only
what arrived beside the loop. It is spawned last, after the verdict and the
lesson are in the state, so the inventor is told what the attempt just
established. And it runs only on `Retry` — `Diversify` runs the same arm one
step later and *awaits* it, so opening one here too would spend two inventor
runs on a single cycle, while `Solved` and `Blocked` end the loop and have
nobody to hand a new direction to. The gate is `route`, which is a plain
function of the state, so all four cases are asserted without a provider.

Two of those arms are errands and finish in one delegation. The third is a
conversation, because what it produces exists in neither agent alone: the
inventor knows what this run has tried and the shape of the problem, research
knows what is already named, proved, and attempted elsewhere, and a line of
attack worth adopting must be both new here and not something the literature
already closed. So `invention_arm` runs three children in sequence —
the inventor proposes three divergent candidates and writes each to
`research/approaches/<slug>.md`, research grounds or refutes each and fills in
its `precedent`, and the inventor adopts one or synthesises a better one from
what came back. The arm still runs beside the library arm's two, so a diversify
costs roughly one extra child run rather than three.

It was one inventor call before, concurrent with the library arm and blind to it.
That produced a paragraph of prose, once, merged into the next attempt's context
and then lost — so an idea proposed at attempt three could be proposed again at
attempt six, and the literature check that would have killed it never happened.
The approach ledger is what makes the next round start from what this one closed.

Asking for that write is not the same as getting it. The inventor's system prompt
asks it to write each candidate before reporting, the arm's own prompt asks again,
and a live Project Euler 597 inventor ignored both — nine tool calls, every one a
read, and the candidates left in a turn that hit the output cap. Across three
concurrent runs `research/approaches/` had never been created. A prompt
instruction is not a control, so `ensure_approaches_written` is: the arm samples
the directory before delegating, and if the proposing turn added no file it
re-issues once, telling the inventor plainly that nothing survived and to write
down what it has without revising it.

Two details decide whether that control is honest. It compares *names added*,
not a count or an mtime — proposing means new slugs, so a turn that rewrote an
existing file has not done what was asked, and mtime would score that a success.
And it re-issues once rather than until compliance: a second refusal means this
turn is not going to write, and the prose it did report is still worth carrying
into the attempt, so the re-issue's reply is appended to it rather than
replacing it.

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
them are switched off — and `research/WEAKENED.md` is derived from those files.
It is deliberately *not* gated on the run being stuck, and that is a lesson this
repository has already paid for: `open_invention`'s stuck-gate was reachable in
principle and not in practice, and across a day of live runs the inventor was
spawned once. A ladder is most useful before the budget has gone on the
full-strength statement, not after.

So the `reducer` is delegated a decomposition: the goal, the lemmas that would
imply it, the inference combining them, and one `gap` per lemma nobody has
proved. It writes `research/backward/<slug>.md`, `research/BACKWARD.md` is
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
next — `TASKS.md`, a thread under `research/threads/`, `CONTEXT.md`, a
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
  is not given `research/CLAIMS.md`, so the role acting on an unevidenced
  instruction is not also holding the evidence ledger.
- **Compute.** No shell, no `write_tool_file`, no delegation. A role that could
  both reinterpret the goal and run programs against it would be a second
  investigation answering to nobody.
- **Redirect an attempt already in flight.** Delivery is at the attempt
  boundary, and a live attempt has run forty minutes. The director's file edits
  are the mitigation — they land within a team cycle and are visible to any role
  that reads the workspace. Reaching further would mean driving
  `AsyncSubagentManager::steer` from outside the run, which holds no handle for
  it today.

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
