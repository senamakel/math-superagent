# The solution loop

`orchestrator::solutions` is a `TinyAgents` graph rather than a prompt. This file records how it routes, why each threshold is the number it is, and how a failure anywhere inside it is kept from ending a run.

The working agreement is [`AGENTS.md`](../AGENTS.md); this file is the part of it that goes deeper than a rule.

## The solution loop

`orchestrator::solutions` is a `TinyAgents` graph, not a prompt:

```text
  attempt ──> judge ──┬─ restart ──────────────────> attempt
     ▲                └─ reflect ──┬─ solved ──────> done
     │                             ├─ retry ───────> attempt
     │                             └─ stuck ──> diversify ──┐
     └──────────────────────────────────────────────────────┘
```

The judge and the reflection answer different questions. Reflection asks
whether the answer is right and what the run learned, and it alone can end the
loop. The judge asks whether the attempt was *conducted* in a way the next one
should inherit: it scores it out of five against what the attempt actually did
— executed and checked, executed but thin, wrote code without running it, prose
only — and returns PROCEED, STEER, or RESTART. STEER's one sentence is carried
into the next attempt's prompt; RESTART discards the direction and re-enters
`attempt` without reflecting.

The judge runs on a narrowed budget (`RunBudget::for_judging`): twelve model
calls and five minutes, against an attempt that takes the better part of an
hour. It reads a report and answers in four lines, so an investigation's budget
is the wrong size for it — and left with one, it investigates. A live judge
spent four minutes, fifteen model calls, and a 6,906-token turn reading
`CONTEXT.md` and the programs the attempt had written, while the finished
attempt waited on it. The tight cap is safe by construction rather than by
luck: the run stops with partial results, a judge cut off before its verdict
returns something unparsable, and an unparsable verdict is PROCEED.

Three rules in it are load-bearing. An unreadable reply is PROCEED, in the same
spirit as an unparsable verdict not counting as solved: a judge the loop cannot
read must not throw work away by accident. `MAX_RESTARTS` is two, because a
judge that dislikes the run's whole approach would otherwise reset it until the
attempt ceiling stopped the loop, and the run would end having explored nothing
to its conclusion. And the attempt ceiling outranks a restart — a run on its
last attempt reflects on what it has rather than discarding it and stopping
with nothing.

The prompt makes the judge reluctant rather than exacting. It is told to assume
the attempt was reasonable, that most are, and that a run which computed the
wrong thing or ended blocked has still done its job. RESTART is reserved for
four named faults in the *conduct* of a run — an answer no executed program
produced, a method that searches the answer space, a verification that checks a
program against itself, or building on a belief already disproved — and if it
cannot name which occurred and point at the words showing it, the verdict is
PROCEED.

Reflection runs after *every* attempt, not only after a failure, because the
lesson from a partial success is what stops the next attempt repeating it. The
pattern agent runs concurrently with it, on the same attempt, for the same
reason: the exploitable regularity in a sequence is usually visible in the
first few terms a run computes, and waiting for the loop to get stuck means
spending the budget the pattern would have saved. They run in parallel because
neither reads the other's output and reflection is on the critical path of
every attempt.

Past `RESEARCH_RESCUE_ATTEMPTS` — five — each reflection also re-opens the
literature. Diversification triggers on *consecutive* unproductive attempts, so
a run making thin but genuine progress every time never reaches it and can
grind most of its budget on a method that was never going to arrive. The search
is re-run rather than recalled because the workspace has changed: by then the
run knows what it tried, what failed, and what the numbers look like, which is
a far better query than anything available at the start. `MAX_ATTEMPTS` is
eight so the rescue has attempts left to pay off in; a ceiling that tripped
first would buy a fresh literature search and then stop.

Housekeeping runs on a narrowed budget, `RunBudget::for_housekeeping` — 25
model calls and 300 tool calls, and deliberately *no* wall-clock ceiling — for
the same reason the judge does.
Filing is bounded work, read a listing and write a row per file, and a role left
with an investigation's budget investigates. The measurement that forced this is
worth keeping: two live runs spent 60% and 64% of every model call they made
inside the organizer, and the cause was *not* frequency — it ran nine and ten
times. It ran long. One organizer run spent 62 model calls tidying, another 56,
against a solve that had spent 14 on the mathematics. Reaching the cap is safe:
`StopWithPartial` keeps the rows already written, and a file left undescribed
shows as a visible gap rather than as an index quietly disagreeing with its
folder, which is what the index tools were designed around anyway.

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
shared.
Filing is cheap to *do* and expensive to *decide*: an organizer asked to notice
that nothing has changed must walk the workspace and spend a model call to
discover it, which is most of what a cycle costs. Two live runs spent 49% and
38% of every model call they made on the organizer, against 11% and 4% on the
agent actually solving the problem — and the indexes still carried undescribed
rows, so the budget did not even buy the filing. `filing_unchanged` fingerprints
the tree, `INDEX.md` excluded, and both the standing `background` team and the
follow-up consult the *same* fingerprint: two separate gates would each read the
other's filing as new work and wake each other indefinitely. Excluding
`INDEX.md` is the load-bearing part — it is what the organizer writes, so
counting it would have the team waking itself forever on the filing it just did,
which is the pattern team's `SCRATCHPAD.md` lesson one folder wider.

A finished `tool_builder` run automatically triggers an `organizer` run, and a
finished `research` run triggers a `scholar` then an `organizer`
(`FOLLOW_UPS` in `src/orchestrator/async_subagents.rs`). That moment is when
the workspace is least tidy and most legible — the files are new and their
purpose is settled — and leaving the tidying to whoever runs next means it
competes with mathematics and loses. The follow-up is fire-and-forget, so
`await_agent` returns as soon as the tool-builder itself is done and
housekeeping never sits on the critical path; it is spawned separately so the
tool-builder's concurrency slot is released first; and follow-ups are
serialised, because two organizers refreshing one `INDEX.md` at once would each
write the list it read and the later write would drop the other's descriptions.
A follow-up that was itself followed up would tidy forever, so the chain is
asserted acyclic in a test.

A trigger's follow-ups are a *sequence*, run in order inside one lock
acquisition rather than each triggering the next. Order is the point after
research: acquiring is not reading, so the scholar says what each new source
establishes before the organizer files it, and an organizer running first would
index excerpts nobody had read. Running them as a sequence rather than a chain
is what keeps the acyclic invariant simple — no follow-up agent is itself a
trigger — and a failed step does not cancel the rest.

The first attempt also opens its own oracle run. The method policy's first step
is a naive program executed against the statement's worked examples, and the
goals agent is asked to delegate that immediately; two live runs instead spent
ten minutes each on `read_document` and `list_workspace`, and both burned a
whole 12,000-token turn on hidden reasoning without emitting a tool call. Two
prompt revisions failed to move it, so `attempt_step` stopped asking and spawns
the oracle itself — fire-and-forget, first attempt only, never blocking. If the
goals agent does delegate promptly the two simply agree: a duplicate oracle
costs one child run, where no oracle at all costs the whole attempt.

The pattern agent is a *team*, not a step. It runs its own async loop beside
the solve — like research and background — cycling on its own cadence over
whatever results are on disk, and posts what it finds to a mailbox the loop
drains at the next `attempt` or `reflect`, whichever reaches it first. Nothing
waits on it: a structural observation is worth as much an attempt later, and an
earlier version that gated the loop on one cost a live run half an hour of
stalled solve.

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
`attempt_prompt` is a plain function of the state for the same reason `route`
is: what an attempt is actually told must be testable without a provider. An invented pattern costs the run more than no pattern, so it idles
readily — and idleness is decided *before* the agent runs, by fingerprinting
`code/` and `code/out/` and comparing against what the team last analysed.
Asking the agent to notice that nothing changed would cost a model call and a
walk of the workspace to discover, which is most of what a working cycle costs:
a live team spent thirty `read_document` calls in two minutes doing exactly
that on runs that had computed almost nothing. A workspace with no results at
all reads as unchanged, so an early cycle idles rather than analysing an empty
folder. Its own notes are deliberately not part of the fingerprint — the team
writes those itself, and including them would have the team waking itself up
forever on its own notes. That is now free rather than arranged: its scratch
went to `note_scratch` and is no longer a file in the workspace at all.

`CONTEXT.md` has an owner, which it did not. It was written by whichever role
happened to think of it, so it drifted behind the run that reads it on every
model call, and nothing measured what it cost. The `context` team owns it now:
one standing team running `context_curator` every
`MATH_AGENT_CONTEXT_MINUTES` — five by default — whose whole job is to keep that
one file current and within budget. It reads widely and writes once. Most of
what it brings across is Cognee's: `recall_memory` and `relate_memory` hold what
earlier runs on this problem, and on problems of its shape, established, and
that is invisible to this run until somebody carries it into the file every role
already reads. It holds no shell, no web search, and no delegation, because each
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
how stale the brief every role reads may be. Everything else about its
allowance is the custodial one — the file keeps changing underneath it, so
"nothing to add" means come back later rather than stop. Idleness is decided
before the agent runs, by fingerprinting the workspace with `CONTEXT.md`
excluded: counting its own output would have the team waking itself forever on
the brief it just wrote, which is the pattern team's `SCRATCHPAD.md` lesson
again. And the standing — what the file costs against its budget — is computed
per cycle and written into the brief, because it is the fact that decides what
the cycle is *for*: adding, or compressing.

`diversify` runs three arms concurrently — the librarian followed by the
scholar, the pattern agent, and the inventor — and only when repeated attempts stop making progress; it is the
step that breaks a loop reflection alone cannot.

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
