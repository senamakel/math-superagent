# The solution loop

`orchestrator::solutions` is a `TinyAgents` graph rather than a prompt. This file records how it routes, why each threshold is the number it is, and how a failure anywhere inside it is kept from ending a run.

The working agreement is [`AGENTS.md`](../AGENTS.md); this file is the part of it that goes deeper than a rule.


## The solution loop

`orchestrator::solutions` is a `TinyAgents` graph, not a prompt:

```text
  attempt ──> judge ──┬─ restart ──────────────────> attempt
     ▲                └─ reflect ──┬─ solved ──────> done
     │                             ├─ retry ───────> attempt
     │                             └─ stuck / scaling ──> diversify ──┐
     └────────────────────────────────────────────────────────────────┘
```

The judge and the reflection answer different questions. Reflection asks
whether the answer is right and what the run learned, and it alone can end the
loop. The judge asks whether the attempt was *conducted* in a way the next one
should inherit: it scores it out of five against what the attempt actually did
— executed and checked, executed but thin, wrote code without running it, prose
only — and returns PROCEED, STEER, or RESTART. STEER's one sentence is carried
into the next attempt's prompt; RESTART discards the direction and re-enters
`attempt` without reflecting.

It is given the workspace as well as the report, because the report is the first
thing lost: the ordinary way an attempt ends is the run cap killing it, which
destroys its context and its report and leaves every file it wrote. One evening
all three live Euler attempts died at exactly 30:00 and every verdict that
followed was 1/5 or 2/5 with "progress no" — one against a workspace holding both
check values its problem supplied, reproduced to ten digits, and 38 points
cross-validated two ways. The judge was scoring silence. `evidence_briefing`
counts what is on disk — `code/out/` entries, claims split by whether the run
established or read them, approaches, threads — and says which to believe when
the two disagree. It counts and never reads: what a file *means* is the
judgement the judge is about to make; whether the attempt executed, established,
or proposed anything is not. It also carries one fault — `code/` holding
`brute.py` and a faster program while nothing under `code/out/` names the oracle.
Keeping the naive oracle was enforced; agreeing with it was not, and PE241's
`solution.py` justified its pruning with a falsehood (no later σ factor supplies
the cancelling prime, when σ(13) = 14) and found 5 of 9 terms below 10⁸.

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

Reflection was the only collector, and that made the team's findings reachable
exactly once per *completed* attempt — so a run whose first attempt is long
never saw them at all. A live Erdős–Gyárfás run spent forty minutes in attempt 1
while its pattern team computed the C₄-free survivor counts, matched the
sequence against OEIS and pushed it past the terms that suggested it; none of it
reached the `goals` agent directing the work, which re-commissioned the same
`nauty-geng` enumeration from `tool_builder`. Draining at the attempt costs
nothing when reflection has already run — the mailbox is empty and the section
is omitted rather than rendered as a heading announcing that no analysis arrived
— and it is the only path that exists on the first attempt of every run.
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
writes those itself, and including them would have the team waking itself up
forever on its own notes. That is now free rather than arranged: its scratch
went to `note_scratch` and is no longer a file in the workspace at all.

`CONTEXT.md` has an owner, which it did not. It was written by whichever role
happened to think of it, so it drifted behind the run that reads it on every
model call, and nothing measured what it cost. The `context` team owns it now:
one standing team running `context_curator` every `MATH_AGENT_CONTEXT_MINUTES` —
fifteen by default — whose whole job is keeping that one file current and within
budget. It reads widely and writes once. Most of what it brings across is
Cognee's: `recall_memory` and `relate_memory` hold what earlier runs on this
problem, and on problems of its shape, established, and that is invisible to this
run until somebody carries it into the file every role already reads. It holds no shell, no web search, and no delegation, because each
of those is a way for curating what the run knows to turn into a second
investigation beside the solve.

Frequency and cycle length are separate axes, and bounding one is not enough.
A live Erdős–Gyárfás run had the curator as its largest consumer — 55 model
calls against `tool_builder`'s 38, growing five times faster than the role
actually doing the mathematics, and spending 69 `read_document` calls walking
`code/` and `research/` file by file. Throttling `MATH_AGENT_CONTEXT_MINUTES`
to fifteen left it one cycle in three minutes and it was *still* the top
consumer, because that single cycle cost eleven model calls. So the curator is
registered with `RunBudget::for_housekeeping()` as well: curating is bounded
work — read what changed, rewrite one file — and a role left with an
investigation's budget investigates, which is the organizer's lesson exactly.
Reaching the cap is safe, because `StopWithPartial` keeps the brief already
written.

Its cadence is configuration rather than a constant for one reason: it decides
how stale the brief every role reads may be. Everything else about its allowance
is the custodial one — the file keeps changing underneath it, so "nothing to add"
means come back later rather than stop. Idleness is decided before the agent
runs, by fingerprinting the workspace with `CONTEXT.md` excluded: counting its
own output would have the team waking itself forever on the brief it just wrote,
the pattern team's `SCRATCHPAD.md` lesson again. And the standing — what the file costs against its budget — is computed
per cycle and written into the brief, because it is the fact that decides what
the cycle is *for*: adding, or compressing.

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
inventor knows what this run has tried and what shape the problem has, research
knows what is already named, proved, and attempted elsewhere, and a line of
attack worth adopting has to be both new to this run and not something the
literature already closed. So `invention_arm` runs three children in sequence —
the inventor proposes three divergent candidates and writes each to
`research/approaches/<slug>.md`, research grounds or refutes each and fills in
its `precedent`, and the inventor adopts one or synthesises a better one from
what came back. The arm still runs beside the library arm's two, so a diversify
costs roughly one extra child run rather than three.

It was one inventor call before, concurrent with the library arm and blind to
it. That produced a paragraph of prose, once, merged into the next attempt's
context and then lost — so an idea proposed at attempt three could be proposed
again at attempt six, and the literature check that would have killed it never
happened. Writing to the approach ledger is what makes the next round start from
what this one closed.

Asking for that write is not the same as getting it. The inventor's system
prompt asks it to write each candidate before reporting, the arm's own prompt
asks again, and a live Project Euler 597 inventor ignored both — nine tool
calls, every one a read, and the candidates left in a turn that hit the output
cap. Across three concurrent runs `research/approaches/` had never been created.
A prompt instruction is not a control, so `ensure_approaches_written` is the
control: the arm samples the directory before delegating, and if the proposing
turn added no file it re-issues once, telling the inventor plainly that nothing
survived and to write down what it already has without revising it.

Two details decide whether that control is honest. It compares *names added*,
not a count or an mtime — proposing means new slugs, so a turn that rewrote an
existing file has not done what was asked, and mtime would score that a success.
And it re-issues once rather than until compliance: a second refusal means this
turn is not going to write, and the prose it did report is still worth carrying
into the attempt, so the re-issue's reply is appended to it rather than
replacing it.

`COMPUTATIONAL_THRESHOLD` is the second way into this step, and it exists
because "did the attempt establish something new" and "is the run getting
anywhere" turned out to be different questions and `route` only asked the first.
Pushing an exhaustive search from n=14 to n=16 honestly establishes something
the run did not have, so reflection answers `PROGRESS: YES`, which resets
`unproductive` — and since `unproductive >= STUCK_THRESHOLD` was the only route
to `diversify`, a run scaling one method never reached the inventor at all. It
could spend its whole budget that way, every attempt genuinely progressing and
the method never changing. Reflection now also answers `KIND: MATHEMATICAL |
COMPUTATIONAL | NONE`, and two consecutive COMPUTATIONAL answers route here. The
parse is conservative: only an explicit, recognised answer moves the counter, so
a reflection the loop cannot read never drives it — treating silence as "scaling
again" would divert a working run on two malformed replies.

A provider wall is not a failed attempt, and the loop must not spend the
attempt ceiling discovering that. `delegate` turns a child's failure into text
so the loop survives it, which is right, but it makes an outage
indistinguishable from a poor attempt unless something reads the text. Two live
runs met `HTTP 403: Key limit exceeded` and burned all eight attempts in
seconds — each recording the same quota error as the lesson learned, each
reflection failing the same way — and ended reporting "not solved within 8
attempts", which reads as a mathematical failure and was not one.
`provider_blocked` recognises the shape `delegate` writes, `route` checks it
before anything else including the ceiling, and `BLOCKED_THRESHOLD` is two
rather than one because a single upstream blip is precisely what the retry
ladder and `ReroutingModel` exist to absorb. The detector is deliberately
narrow — the failure wrapper must be present and the report substantially
nothing else — because a false positive stops a run that was working, which is
worse than the wasted attempts it prevents. The outcome says so in words: an
infrastructure failure, the workspace unchanged, the run continuing from disk
once calls are accepted again.

Keep the routing policy in `route` a plain function of the state. It is the
part of this design most likely to be wrong and the part a live run is least
able to demonstrate cheaply, so it must stay unit-testable without a provider.
Two rules in it are load-bearing: an unparsable verdict must not count as
solved, and the attempt ceiling must outrank the stuck rule or the loop can
diversify forever.

The loop is the only execution path. Do not add a single-turn mode back: it
differed only in discarding the reflection, and a switch between them is one
more thing to get wrong.

## Judging before the attempt returns

The judge scores an attempt when the attempt returns, and the attempt is a single `goals` run told to pursue the goal until it is met. On an open conjecture it is never met. Four live runs sat inside attempt 1 for thirty-six minutes with zero judge verdicts, zero reflections and zero inventor spawns between them, while all the work happened in children the attempt had spawned — 231 model calls, 47 searches and 36 downloads on one of them, none of it ever assessed. `open_invention` needs a completed cycle and `diversify` needs two consecutive stuck attempts, so both were unreachable by construction.

Two changes make the loop turn over. The run wall clock is thirty minutes rather than two hours, so an attempt concludes and is judged four times in the span it used to be judged once. And a `review` team runs beside the solve every twenty minutes (`MATH_AGENT_REVIEW_MINUTES`), spawning the judge against the workspace as it stands and posting the verdict into the mailbox the attempt already drains. It asks the three questions worth asking mid-flight: whether the method can settle the question or is scaling something that already failed smaller, whether what the run believes is supported by what it computed, and what the single most valuable next move is.

The review is the judge rather than a second solver, so it inherits `RunBudget::for_judging` — twelve model calls and a five-minute ceiling — and an unchanged workspace is skipped before the agent runs rather than by asking a model to notice. The wall-clock change is the one with a cost: it bounds every agent run, not only the attempt, and a live `tool_builder` spent 1,362 seconds inside a single model call. That path does not honour `StopWithPartial`, so a child that meets it loses its context and its report — but not its files, and `continuation_briefing` is what lets the next attempt resume from them.

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
which counts the lines it has consumed. Neither side needs a lock because
neither writes what the other writes, and the one number they share is owned by
the side that advances it. A directive's identifier is its line number rather
than a stored field, so a line the reader cannot parse is skipped *and still
counted* — a torn append, which a checkpoint commit landing mid-write could
produce, costs one directive rather than the alignment of every later one.

### Two deliveries, deliberately unequal

Nothing waits for a person. That is the same decision the `Mailbox` records for
the pattern team — a live run spent 56 of its 74 minutes unable to start its
second attempt because a support agent had been made a gate — and a human is
slower than any support agent, so a loop that blocked on one would be that
failure with no ceiling at all.

**Verbatim, to the next attempt.** The `director` team drains the queue and
posts the text, unchanged, to a second `Mailbox`. `attempt_step` collects it and
`direction_briefing` renders it above the judge's steer, labelled as coming from
the operator and as taking precedence. The attempt is the only collector, unlike
the pattern mailbox that reflection drains as well: reflection folds what it
collects into `fresh_context`, which reaches the next attempt as *material
gathered* rather than as an instruction, and losing that distinction would lose
the only thing this channel exists to carry.

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
forty-cycle budget would have retired the team thirteen minutes into an
eight-hour run with nothing saying direction had stopped being read. What bounds
its spending instead is `directives_waiting`, a file read in front of the model
call — the same shape as the fingerprint gates beside it.

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

The scientific stack — `sympy`, `numpy`, `scipy`, `gmpy2`, `networkx` — is
baked into the image from apt rather than installed per run. A run that has to
install `sympy` before it can factor anything spends minutes of its budget on
setup, fails outright when the index is slow, and every workspace pays again.
They come from apt rather than pip because the container root filesystem is
read-only at runtime, so system packages are the only ones importable without
writing to `/workspace` first.

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
rather than a missing variable. The image is smoke-tested on both at build
time, so a Lean install that cannot import Mathlib fails the build rather than
the run.

Two more failure modes on the same class of tool
are worth stating: a truncated tool call and a corrupt document index. Both are
covered under the reflection middleware and `documents.rs` respectively, and
neither may be allowed to end a run.
