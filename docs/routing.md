# Routing: the verdicts and every threshold

The solution loop's shape is in [`solution-loop.md`](solution-loop.md). This file
is the part that decides where a pass goes next: which role answers which
question, what each verdict routes to, and why every number in the ladder is the
number it is. Each threshold carries the live run that set it, because that is
the evidence a reader needs before changing one.

`route` and `judged_route` are no longer what a run executes — the engine runs
the jq generated from these constants — but they remain the executable
specification of this policy, and `orchestrator::parity` proves the two agree
exhaustively rather than by sampling.

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
deliberately not routed `derived/APPROACHES.md`: a judge holding the ledger
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
