# Repository Guidelines

This file is the working agreement for humans and coding agents in this
repository. `CLAUDE.md` points here so every agent follows the same rules.

## What this repository is

This repository contains a Dockerized mathematical problem-solving agent. Its specialty is
deep research: it combines mathematical reasoning with source discovery,
small programs, numerical experiments, and explicit verification.

The product should help a reader understand why an answer is true, not merely
produce a plausible final expression. Preserve that standard in prompts,
tools, examples, tests, and documentation.

## Expected problem-solving behavior

The runtime has fourteen roles plus an explicit solution loop.

- The orchestrator decomposes a problem, delegates focused tasks, and combines
  the results.
- The goals agent translates an objective into completion criteria and spawns
  specialist subagents until the goal is met or precisely blocked.
- The research agent uses Exa to find definitions, papers, official references,
  or current facts, and is deliberately reluctant: gathering costs a download,
  a digest, an index row, and a share of every later reader's attention, so it
  fetches only when the solver reports an attempt STUCK, when `ROOT.md` names a
  specific gap it knows a specific source for, or not at all. It works the open
  rows of `research/REQUESTS.md` — gaps other roles stated precisely — before
  anything it thought of itself, checks `search_claims` before going looking for
  what the library may already establish, and follows `research/FRONTIER.md`,
  the citations inside the sources it already has. The loop posts
  each attempt's verdict to the teams so "is the run short of something" is a
  signal rather than a guess. It returns source URLs, separates evidence from inference,
  and can save reusable notes to Qdrant.
- The tool-builder writes and executes shell or Python tools in `/workspace`.
  It handles numerical checks, counterexample searches, data extraction, and
  other reproducible calculations.
- The SAT solver answers a question that has already been reduced to a finite
  decision or optimisation problem, by *encoding* it for CP-SAT, a SAT solver,
  an SMT solver, or an MILP solver rather than by writing the search itself. A
  hand-written backtracking search over the same space is the answer-space
  search the method policy prohibits, written in the language most likely to
  hide its own bugs. Its failure modes are its own: reporting `UNKNOWN` or
  `FEASIBLE` as an answer, weakening a constraint until a model appears, and an
  unsound symmetry break that silently loses solutions. `UNSAT` is a result and
  is never to be relaxed away.
- The SMT solver settles a statement *modulo theories* rather than over a
  finite encoding, with Z3 and cvc5. Its one irreplaceable move is proving a
  universal claim by asserting the negation and getting `unsat` — the only tool
  here besides Lean that establishes something for all values rather than
  checking it on many. It is held to naming the logic it used, because
  `QF_LIA` is decidable and nonlinear integer arithmetic is not, and `unknown`
  is a statement about the solver rather than about the mathematics. It must
  check the hypotheses are satisfiable *alone* before believing any `unsat`:
  from contradictory hypotheses everything follows, and that is how a bad
  encoding looks like a proof.
- The theorem prover hands first-order statements to a saturation prover
  (`eprover`, TPTP). It sits between the SMT solver, which is weak once
  quantifier reasoning dominates, and Lean, which costs a human-scale effort
  per theorem. The axiomatisation is the whole job and the whole risk: a prover
  proves what was written down, not what was meant, so it reports the axioms in
  prose, checks them for consistency, and says "proved from these axioms"
  rather than "proved". `CounterSatisfiable` is a real result — the axioms are
  too weak, and the missing hypothesis is what to go find.
- The symbolic mathematician works with expressions rather than numbers:
  closed forms, summations, recurrences, generating functions, exact algebra,
  through sympy, mpmath, PARI/GP, Singular, and SageMath. It exists because the
  run's most common error is arithmetic that looks right — a float agreeing to
  twelve digits with something false, a closed form fitting six terms. It may
  not report an identity because both sides agree at sample points; the
  difference has to simplify to zero, and a residual that will not close is the
  finding.
- The Lean prover writes Lean 4 against a pre-built Mathlib. It is the only
  role whose output is not evidence: everything else here — a program's output,
  a numerical check, an argument that reads well — is a reason to believe
  something, and a proof that compiles with no `sorry` is the thing itself. It
  is held to reporting `#print axioms` and every remaining `sorry`, because a
  formalisation that hides one is worse than none.
- The reflection agent judges one attempt and extracts one lesson. It has no
  research or execution tools on purpose: a judge that can start solving stops
  judging. Its hardest job is refusing to call an unverified answer solved.
- The pattern-recognition agent runs exact sequence analysis over results the
  run already computed. Its tools report only what holds for every term
  supplied, and label the finding a conjecture, because an invented pattern
  costs more than no pattern. It can also execute code and commission it from
  the tool-builder: its own tools describe the terms handed to them and cannot
  extend a sequence, so without a way to generate more terms it could neither
  test a conjecture past the data that suggested it nor find the first term
  that breaks one. It has no *web* search, because a bounded structural
  question must not turn into a second investigation — but it recalls what the
  run and the note store already hold, since a regularity the library already
  explains is not a conjecture worth chasing.
- The inventor proposes a different line of attack when the current one has
  stalled, backed by research. It is told what failed so it does not re-propose
  it.
- The librarian builds a local reference library under `research/` so the rest
  of the run reads primary material instead of guessing.
- The scholar reads that library. It judges each source against the run's goal,
  current tasks, and existing beliefs, replaces each source's digest with what
  it actually establishes and what that implies here, records each statement as
  a `claim` block so it is retrievable one statement at a time, keeps the
  threads current, and describes it so `research/INDEX.md` is the way in. It exists because acquiring is not reading: a downloaded paper
  nobody has opened has cost the run context and taught it nothing. It has no
  search tool on purpose, so it digests the library instead of drifting into
  another search the librarian has already done.
- The organizer keeps the workspace navigable: folder indexes, the layout and
  naming of `research/`, and `code/lib/INDEX.md` matching the files beside it. It has files
  and index tools only — no search, no shell, no note memory — because every
  tool it lacks is a way a filing job cannot turn into an editing one. It may
  not delete anything carrying a result, a derivation, or a source, and may not
  change what a file says; an obsolete file is labelled obsolete in the index
  rather than removed.

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
whatever results are on disk, and posts what it finds to a mailbox the next
reflection collects. Nothing waits on it: a structural observation is worth as
much an attempt later, and an earlier version that gated the loop on one cost a
live run half an hour of stalled solve. An invented pattern costs the run more than no pattern, so it idles
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

## Run budget

`RunBudget` in `src/agent/budget.rs` is the single source of truth for what one
agent run may spend, and it applies to the orchestrator and every specialist
alike. The defaults are 250 model calls, 4000 tool calls, a two-hour run
ceiling, and a ten-minute ceiling per tool call. Each is overridable through
`MATH_AGENT_MAX_MODEL_CALLS`, `MATH_AGENT_MAX_TOOL_CALLS`,
`MATH_AGENT_RUN_MINUTES`, and `MATH_AGENT_TOOL_MINUTES`; an unset, empty,
unparsable, or zero value keeps the default.

These are far above the `TinyAgents` defaults of 25 model calls and 50 tool
calls, which fit a short question-answering turn rather than an investigation.
A run that reaches the model-call cap stops with partial results instead of
failing, so the work already done survives. Keep it that way: discarding a
completed derivation because a counter tripped is the worst outcome available.

The tool-call cap is the exception, and the reason it is set so far above the
model-call cap. `LimitBehavior::StopWithPartial` is honoured on the model-call
path in the vendored agent loop but not on the tool-call path, which still
fails the run outright. Until that is fixed upstream, the tool cap must stay out
of reach so the graceful cap is always the one that trips. Do not narrow it to
just above the model cap: one model turn can request several tool calls.

The wall clock is a third path with the same defect, and unlike the tool cap it
is *not* out of reach. `run_loop.rs` checks the deadline before each model call
and returns `TinyAgentsError::Timeout` — `StopWithPartial` is not consulted, so
a run that reaches its ceiling fails outright and its accumulated answer is
lost, exactly as a provider error would lose it. Only the long-lived agents can
reach this: a child spawned late inherits a fresh ceiling, but the `goals` run
driving an attempt starts with the run and ages with it. Two live runs spent
their first ninety minutes inside attempt 1 and were on course to meet it. When
that happens the loop itself survives — `delegate` turns the failure into a
report reflection can read — but the attempt's work product does not. Treat a
run ceiling reached mid-attempt as data loss, not as a clean stop.

The run ceiling and the tool ceiling are separate limits and must stay
separate. Collapsing them means a specialist that runs one long computation
dies with it. Whatever the run ceiling is, `await_agent` must be able to wait it
out, or the orchestrator is structurally unable to collect the result of the
deepest work it delegated.

Saying so in the schema was not enough. `wait_seconds` has always accepted up
to the run ceiling, but the harness applied the ten-minute *tool* ceiling on
top, so any wait longer than that died with a timeout error instead of the
child's result — a live `pattern_finder` asked for 600 seconds, was killed at
exactly 600,000 ms, and lost the run it had commissioned. `await_agent` and
`await_agents` therefore override `timeout_policy` with the requested wait plus
a minute of grace. The grace matters: the wait must be the thing that ends,
because it ends by *returning* the child's state as it stands, where a deadline
firing first replaces that with an error.

Each model turn is capped at 12000 output tokens
(`MATH_AGENT_TURN_OUTPUT_TOKENS`). Generation time is linear in output length,
so an uncapped turn is an uncapped wall clock: a measured turn ran to 9,361
tokens and 2.9 minutes, and longer ones exceeded seven.

Treat this as a safety ceiling, not a way to make the model concise. Set to
4000 it bound an ordinary turn exactly, truncating the model mid-generation so
it emitted no usable tool call and the loop retried — 66 seconds spent to
accomplish nothing. A cap that trips routinely is worse than the long turns it
prevents. Buy brevity in the prompt instead.

The retry is upstream `truncated_empty` recovery in `agent_loop/run_loop.rs`:
when a turn ends with `finish_reason == "length"`, no text, and no tool calls —
the model spent the whole budget on its hidden reasoning channel — the loop
re-issues with the cap doubled, clamped at 4x. So a bound turn shows as
`out=<cap>`, a `model RETRY`, then `out=<2x cap>`. Read that pair as one
truncation, not as evidence the cap is larger than it is.

`UntruncatedModel` is a second ladder beside that one, covering the shape
upstream excludes — a turn that produced text but no tool call. The two must
share a ceiling rather than compose into one. `MAX_CAP_GROWTH` is therefore
measured from the run's *configured* turn cap, passed in with `with_turn_cap`,
not from whatever cap the request happens to carry: read as an original, a turn
upstream had already doubled doubled again, and a live `goals` agent reached a
48,000-token re-issue — four times the ceiling, against a wrapper documented to
allow twice, and some twelve minutes of generation for one turn.

A timeout is a safety ceiling, not permission to run an intractable approach.
Before substantial execution, the tool-builder must state both time and space
complexity. Algorithms with exponential time or space complexity are
prohibited; choose a polynomial or better formulation.

`validate_complexity` enforces that, and the field it reads has been evaded
three times in three different ways. First by notation: a factorial search
wrote `polynomial (O((n!)²))` and the forbidden list looked for `o(n!` , which
the parenthesis defeated. Then by honesty running the wrong way: a truthful
`exponential` on the naive oracle rule 8 *requires* was refused outright, so
the gate punished accuracy and blocked the method policy's own first step —
which is why `exponential` and `factorial` are declarable with a concrete
`oracle_bound`. And then by saying nothing at all: a live run on Project Euler
185 declared `complexity: "backtracking with pruning"` against
`complexity_class: "polynomial"` and was allowed through, because that string
names a method and states no quantity, so neither the class check nor the
notation check had anything to match. Sixteen digits is ten quadrillion
candidates, and the run held a `sat_solver` it never spawned.

So a declaration naming a search strategy over candidate solutions —
`backtrack`, `brute force`, `exhaustive`, `branch and bound` — with no
`oracle_bound` is refused, and the refusal names `sat_solver`, because a gate
that blocks the wrong method without pointing at the right one costs the run a
turn to rediscover it. `enumerate` is deliberately not on that list:
"enumerate the divisors of n" is an honest description of an `O(√n)` method,
and refusing it would repeat the second evasion above. A bounded oracle
declares its bound and never reaches the check, so rule 8 is untouched.

The wider lesson is the one this document keeps recording. Five solver and
prover roles were registered, tool-equipped, prompt-written, and provisioned in
the image, and naming them in the planners' prompts did not get a single one
spawned; the run reached for `tool_builder` and commissioned the prohibited
method instead. A prompt instruction is not a control, and the control belongs
where the action happens.

A command that hits the ceiling is killed, but what it printed is kept and
returned with the timeout reported as its exit status. `Command::output()`
inside a `timeout` discards all of it — the read is dropped mid-flight — so a
program that printed for nine minutes taught the agent nothing, and it could
not tell a computation that was nearly done from one that never got past its
first loop. Two such commands cost one live run twenty of its first
forty-four minutes. The pipes are therefore drained by their own tasks, and
killing the child is what closes them. A timeout is evidence about the method,
and evidence belongs in the result rather than in an error string.

## Research gating

`MATH_AGENT_RESEARCH=off`, or the `--no-research` flag on `./agent` and
`./euler`, withholds `exa_search` and `oeis_lookup`, so a self-contained
problem tests the runtime's reasoning rather than its ability to look an answer
up. It is enforced by not registering the tool, not by asking the model to
abstain: a prompt instruction is not a control. The workspace note tools stay
available, so the agent can still record and recall its own findings.

## Observability

Every run in the tree carries a `RunTracer` (`src/agent/trace.rs`). It prints an
elapsed-time console line per model call, tool call, and tool result, labelled
with the agent that produced it, and appends every event as JSON to
`config/trace.jsonl` in the selected workspace. Alongside the event records it writes
a `model_accounting` line per model call carrying the agent, the provider and
model that served it, prompt/cached/output/reasoning tokens, and the USD cost
the provider reported. The event stream cannot supply these: `ModelCompleted`
names neither the route nor the price, and with `allow_fallbacks` on the route
genuinely varies per call. They are read from the response body by
`AccountingModel` (`src/agent/accounting.rs`), which is why it is a model
wrapper rather than an event listener. Cost is recorded as the provider
reports it; deriving it from a local price table would mean reporting fiction
the moment a price changed. The console profile carries the running total. It also prints a line when a
run *fails*, which it did not: a live `organizer` retried one call six times
over two and a half minutes and then died on `openai response contained no
choices`, and the console showed the retry ladder but not its outcome — the
run simply stopped appearing. The error was in `trace.jsonl` the whole time,
which is the wrong place to need it when someone is watching the console.
The document tools refuse to read it
back: a reflection run pulled its own 1.1 MB event log into a single
339,652-token call, blowing past the compression trigger and dropping the
cache hit rate to 26% to re-read a verbatim replay of what it had already
seen. Hiding it from `list_workspace` was not enough, because an agent can
name a path the listing never offered it. Specialist runs also export their own
observations to Langfuse, and payload capture is enabled, so a Langfuse trace
carries the prompts, tool arguments, and results rather than bare ids. Read
`trace.jsonl` or the Langfuse trace when diagnosing a run; do not add a
separate logging mechanism beside them.

When changing prompts or agent behavior, keep these rules intact:

1. State assumptions and define ambiguous notation.
2. Understand before computing, and gather context before implementing.
   Identify the mathematical objects involved and the theory that governs them
   before writing full-size code.
3. Show the main derivation or argument. Do not jump straight to the answer.
4. Do not search the answer space. Enumerating candidates, or every object up
   to the bound in the statement, until one matches is prohibited even when it
   would terminate. A method whose cost grows with that bound rather than with
   the size of the problem's description is the wrong method. Brute force is
   for validating the real method on small instances.
5. Solve by theory. The bound in the statement is chosen to defeat
   enumeration, so the intended solution is a structural fact — a recurrence,
   a bijection, a closed form, a symmetry, a classification — that makes most
   of the search space unnecessary to visit. Name it before implementing it.
6. Attack the method before trusting it. State what would make it wrong and go
   looking for that case; hunt a counterexample as seriously as a proof, and
   report what was searched and how far when none is found. Survive an attempt
   to break a conjecture rather than only confirming it.
7. Say how problems of this shape have been attacked before and why this
   approach beats the alternatives. Record failed approaches with the reason —
   a known dead end is a result.
8. Delegate external fact-finding to `research` and cite the returned sources.
9. Delegate meaningful computation to `tool_builder`. Report the program or
   command and the relevant output.
10. Check edge cases, dimensions, signs, domains, and limiting behavior when
   they apply.
11. Verify by a second, independent route, or say the result is unverified.
12. Distinguish a proof, a numerical check, a heuristic, and a sourced claim.
13. Say when the evidence is incomplete. Never invent a theorem, citation, or
    computation result.

The runtime is not a formal proof assistant. Do not describe sampled evidence or a
floating-point experiment as proof.

## Runtime architecture

The Rust crate vendors TinyAgents and keeps the integration deliberately small.

```text
src/
├── lib.rs              # public exports
├── prompts/            # built-in role prompts, included at compile time
├── agent/              # TinyAgents facade, OpenRouter, Langfuse
│   ├── budget.rs       # per-run call, wall-clock, and capture policy
│   ├── reflection.rs   # in-run middleware that reflects on failing tools
│   ├── resilient.rs    # tool-error and request-timeout wrappers
│   └── trace.rs        # live console and trace.jsonl event listener
├── orchestrator/       # registry, specialists, compression, workspace tools
│   ├── async_subagents.rs # graph-backed asynchronous child-run controls
│   ├── claims.rs       # claim blocks, the derived ledger, and search_claims
│   ├── code_layout.rs  # measures duplication and grouping in code/
│   ├── digest.rs       # structural digest of a downloaded source
│   ├── documents.rs    # bounded workspace documents and local search index
│   ├── frontier.rs     # citation graph of the library, ranked and deduped
│   ├── oeis.rs         # sequence lookup adapter, filed and cross-referenced
│   ├── patterns.rs     # exact sequence analysis and recurrence search
│   ├── requests.rs     # stated gaps, deduped against the ledger and closed
│   ├── threads.rs      # the library's topic axis beside its arrival axis
│   ├── solutions.rs    # graph-backed attempt/reflect/diversify loop
│   └── vector.rs       # Qdrant tools and deterministic local feature vectors
├── hello_agent/        # minimal single-agent example
├── error/              # crate-wide Error and Result<T>
└── greeting/           # legacy template example
examples/
├── orchestrator.rs     # Docker runtime entry point
└── hello_agent.rs      # direct provider example
vendor/tinyagents/      # pinned upstream TinyAgents checkout
agent                   # user-facing helper
euler                   # Project Euler problem-number wrapper
compose.yaml            # agent and Qdrant services
scripts/run-agent       # Docker Compose implementation
scripts/solve-euler     # official statement fetch and solve workflow
workspace/              # selectable writable agent workspaces
└── template/           # seed instructions, prompts, config, and memory
```

The executable registry contains `goals`, `research`, `tool_builder`, `coder`,
`sat_solver`, `smt_solver`, `theorem_prover`, `symbolic_math`, `lean_prover`,
`reflection`, `judge`, `pattern_finder`, `inventor`, `librarian`, `scholar`,
and `organizer`.

Seven of those — `tool_builder`, `coder`, `sat_solver`, `smt_solver`,
`theorem_prover`, `symbolic_math`, `lean_prover` — carry
exactly the same authority: shell, file write, `apply_patch`, and the document
tools. They are separate roles because they differ in *mandate*, and because
their failure modes have nothing in common: a program that ran but computes the
wrong thing, an `UNKNOWN` reported as solved, an `unsat` from hypotheses that
were already contradictory, a `Theorem` proved from axioms nobody checked, an
identity confirmed by sampling, a `sorry` left undeclared. One prompt hedging
between seven of those is strict about none of them. They are
built from one list in `register_code_writing_agents`, so the shared authority
boundary is visible rather than buried in four near-identical blocks — a tool
granted there reaches all four.
Agents are exposed to the orchestrator as TinyAgents `SubAgentTool` instances.
The goals agent also receives the research and tool-builder delegation tools,
so it can pursue a goal through nested, focused work.
All model-visible delegation uses the graph-backed asynchronous controls:
`spawn_agent`, `peek_agent`, `steer_agent`, and `await_agent`. A spawn returns a
run ID immediately. Callers may launch independent work in parallel, inspect
or redirect live runs, and must await every result needed for their final
answer. Do not reintroduce blocking `SubAgentTool` calls.

Fifty runs may execute at once (`MATH_AGENT_MAX_CONCURRENT_AGENTS`); the rest
queue for a slot, and spawning stays non-blocking either way, so a caller gets
its run ID immediately whether or not a slot was free. The cap bounds provider
concurrency rather than rationing work: unbounded fan-out becomes upstream rate
limiting, which the retry ladder then absorbs as simultaneous backoff across
every run. Keep it far above the fan-out the registry can produce. A run holds
its slot while it waits in `await_agent` for children it spawned itself, so a
pool that could fill entirely with parents waiting on queued children would
deadlock; the headroom is what makes that unreachable.
The session dataset is named for the *project*, not the run:
`math_agent_sessions__project_euler_185`. It briefly carried the run id too —
`…__s18cb030630d9e2be-1`, nanoseconds and a pid — which made the name unique per
process, so every restart opened a fresh dataset, and because a run is shown
only its own session dataset, every restart silently *discarded* the session
memory of every earlier run on that problem. One problem restarted eight times
in a day left eight datasets, seven of them unreachable. The run id belongs
inside the document, where `remember_session` already writes it as a `Session:`
line; the dataset is the scope, and the scope is the problem. `visible_datasets`
also accepts `<project>__<anything>`, so the per-run datasets the old naming
stranded are readable again — with the `__` separator required, because without
it project `euler_18` would read `euler_185`'s memory.

Every role with memory gets three tools, not two: `remember_memory` writes,
`recall_memory` returns the passages nearest a phrase, and `relate_memory`
returns the *edges* the graph holds around a subject. The third is the one that
justifies a graph store at all — chunk search is what the vector store already
did, so a runtime that only ever recalls chunks is paying for a knowledge graph
and using it as a search box. The distinction is worth stating in each prompt
that needs it: the inventor asks what the memory relates the obstruction to
before proposing a new line, the scholar asks what is already connected to a new
source's central object so its digest can say where the source agrees or
conflicts, and the pattern agent asks before calling a regularity new. Both
searches share one request path on `VectorStore::search`, differing only in
Cognee's `search_type`, so a correction to one cannot drift from the other.

The research agent has Exa plus `recall_research` and `remember_research` tools.
Cognee persists the notes, and the server is **shared rather than per-checkout**:
it scopes its graph by project, so one instance serves every checkout on the box
with the datasets kept apart. `compose.yaml` therefore joins an external network
named by `COGNEE_NETWORK` (default `cognee-local_default`) and reaches the
server as `cognee:8000`, with no `depends_on` — the memory server outlives any
one run, and a run must never be able to take it down.

The self-hosted stack is still defined but parked behind `--profile own-memory`,
so `docker compose config --services` yields `agent` alone. Starting a second
copy alongside the shared one is not a preference, it is a failure: both bind
`127.0.0.1:8000` and `127.0.0.1:3000`, so the second simply does not come up,
and running two graph stores against one project splits the run's memory in
half.

The parent and both children use context-compression middleware with an
estimated 300,000-token trigger. The summary should retain mathematical
assumptions, intermediate results, source URLs, tool output, and unfinished
work.

OpenRouter uses `deepseek/deepseek-v4-flash-0731` unless `OPENROUTER_MODEL`
overrides the model. `DeepInfra` is preferred through `provider.order`, overridable with
`MATH_AGENT_PROVIDER`, and `allow_fallbacks` is enabled.

Preferring one provider is what makes prompt caching pay: the cache is
per-provider, and these agents carry a large fixed prefix, so bouncing between
routes re-sends the whole system prompt at full price every turn. Allowing
fallbacks is what stops a busy provider halting the runtime. Do not restore
`provider.only`: an exclusive pin makes every other provider unreachable, so a
rate limit on one route stalls everything while providers serving the same
model sit idle. Verify any slug before relying on it — `streamlake` sat here
and silently matched nothing.

Preference alone is not enough, because every fallback costs twice: once for
the cold call on the new provider, and again next turn when routing swings back
to the preferred one and finds its cache cold too. `StickyProviderModel`
(`src/agent/sticky.rs`) closes that gap by reading which provider actually
served each response and pinning subsequent requests to it, so a fallback
becomes the new home rather than an oscillation. The pin keeps
`allow_fallbacks` on — it is an affinity, not an exclusion — and each
specialist holds its own, because agents differ in the prefix they cache and
one agent's fallback must not drag the others onto a route where their prefix
is cold. Exa handles search. Langfuse ingestion
is best effort and must not turn a successful answer into a failed run.

Langfuse is also available for querying and reviewing recorded turns. Use
`./langfuse-turns --hours 24 --limit 50` for normalized observations or
`./langfuse-turns --trace <trace-id>` for one trace. Use
`./langfuse-review --hours 24 --limit 100` to retain those turns while flagging
errors, status messages, and missing outputs as improvement candidates. The
helpers load the ignored local `.env`, query Observations API v2, and pass Basic
Auth through curl configuration on standard input so credentials never appear
in process arguments or output. Treat returned inputs and outputs as sensitive.

Do not add memory domains, channels, Web3, SQLite persistence, REPL, or RLM
features unless the user explicitly expands the product scope.

## Running and watching a run

Starting a run and watching one are separate commands on purpose.

```sh
./euler 763                     # start or continue problem 763
./euler 763 --no-research       # the same, with web search withheld
./euler-tui 763                 # watch it, a tab per team
./euler-tui 763 --replay        # read the last run's log; touch nothing
./euler-tui 763 --plain         # no tabs, stream to stdout, as when scripting
```

A Project Euler problem has one number as its answer and a ceiling on how long
it can reasonably take. An open conjecture has neither, so it gets its own
launcher and its own task shape — build the library, extract what is known,
build the oracle, then loop — and the workspace rather than a number is its
identity:

```sh
./conjecture erdos-gyarfas      # start or continue workspace/conjectures/erdos-gyarfas
./euler-tui --workspace conjectures/erdos-gyarfas
```

`./conjecture <slug>` requires `workspace/conjectures/<slug>/problem.md` to
exist and reads `GOAL.md` beside it. The statement, what counts as a result,
and the leads into the literature are the workspace's, not the script's: a
launcher that carried the mathematics would need editing for every problem.

`./euler-tui` **only watches**. It finds the container that has the workspace
mounted and follows it, and it cannot start, stop, or restart anything. That is
the design, not a gap: when starting was part of the same command, opening a
second view started a second run on the same workspace — both writing the same
files and both making checkpoint commits over each other. That happened three
times in one evening, twice unnoticed for minutes. A viewer that cannot launch
cannot do it, and one start command means "is something already running for
this problem" has a single answer rather than one per terminal.

Start a run detached so it outlives the terminal, then watch it:

```sh
nohup ./euler 763 > workspace/project-euler/763/config/start.log 2>&1 &
```

`start.log` holds the image build and the statement fetch, which happen before
any container exists and are therefore the only place a failed start says why.
Everything after that is the container's, readable with `docker logs` or
`./euler-tui`.

Before starting anything, check nothing is already running for that workspace:

```sh
docker ps --format '{{.Names}}' | grep riemann-agent-run
docker inspect <name> --format '{{range .Mounts}}{{.Source}}{{"\n"}}{{end}}' | grep project-euler
```

Two containers on one workspace is the failure to look for, and it is silent:
both runs work, both write, and the damage shows up later as a checkpoint
history that interleaves two investigations. Stop a run with
`docker rm -f <name>`; the workspace survives and the next `./euler` on it
continues from what is on disk.

The runtime's console arrives on the container's **stderr**, not its stdout —
a live container had 643 lines there and none on stdout — so `docker logs`
needs `2>&1` and any follower must read both streams.

## Docker and workspace rules

The orchestrator must run through `./agent`, which starts the runtime and Qdrant
through Docker Compose. Do not add a host-side fallback for tool execution.

The Docker boundary is part of the security model:

- Run as an unprivileged user.
- Drop all Linux capabilities and keep `no-new-privileges` enabled.
- Keep the root filesystem read-only.
- Do not mount the repository, home directory, Docker socket, or broad host
  paths into the runtime.
- Mount only the selected directory below `workspace/` at `/workspace` for
  agent-written files.
- Keep process, memory, command-time, and command-output limits. Keeping a
  limit is the requirement; the value is a judgement, and 2 GiB was the wrong
  one. A live Erdős–Gyárfás container was OOM-killed mid-attempt — `oom` then
  `die exit=137` in `docker events` — and an OOM kill is the worst failure shape
  available here: the kernel stops the process, so nothing is written to the
  console, the run simply ceases to appear, and everything in flight is lost.
  Read `docker events --filter event=oom` when a container vanishes without an
  error. The cap covers the Rust runtime, every concurrent child run, and every
  Python subprocess they spawn between them, against work that is graph
  enumeration and BFS over millions of states; problem 763 had already recorded
  the old cap in its own `MEMORY.md` as a mathematical ceiling, "exact BFS stops
  at N=14", which is a sandbox limit masquerading as a result.
- Keep network access because provider, search, and telemetry calls need it.

Every agent working directory is `/workspace`. The helper accepts
`--workspace <relative-subfolder>` or `MATH_AGENT_WORKSPACE` and must reject
absolute paths, traversal, and symlinks that resolve outside the repository's
`workspace/` root. File tools must accept relative paths, reject traversal and
absolute paths, and verify canonical parents before writing. Command tools run
with `/workspace` as their current directory. A prompt instruction is not a
security control; enforce boundaries in code and Docker configuration.

Workspace contents are committed. The derivation, the program, and the per-run
notes are the record of how an answer was reached, which is the point of the
product, so they belong in history rather than only on the machine that produced
them.

They belong in history, not in every commit. A live run writes into `workspace/`
continuously, so a host-side auto-commit hook firing on each tool call turns
that into commit spam: one measured hour produced 97 commits on `main`, 87 of
them touching nothing but `workspace/`, with model-written subjects that did not
always match their diffs — one read `remove outdated project euler problem 763
files` for a change that removed nothing and added five lines to a prompt.
`.claude/settings.json` therefore sets `AUTO_COMMIT_EVERY=25` for this
repository. Everything is still committed and nothing is excluded; it is
batched. The fine-grained record is not lost either, because the runtime keeps
its own per-write checkpoint in each workspace's `.workspace-history`, which is
what `WorkspaceCheckpoint` is for. Do not add a generated artifact to a source directory; leave it in its
workspace.

Three things are ignored: `.python-packages/` (pip installs, which land in the
workspace only because the container root filesystem is read-only), bytecode
caches, and `trace.jsonl`. The trace is several megabytes per run and the
derivation and notes already carry the reasoning worth keeping; read it locally
or in Langfuse instead.

## Document conversion

`readable::to_markdown` converts every downloaded document before it is
stored. HTML becomes Markdown, a PDF's text layer is extracted, plain text
passes through, and genuinely binary content returns an error that names the
format and says to find another source.

Two details are deliberate and should not be simplified away:

- The HTML converter is hand-written rather than taken from a crate because
  mathematical sources carry TeX, delimited `\(…\)` or `$…$`, and a
  general-purpose converter escapes the backslashes and destroys it. There is a
  regression test using a real Project Euler statement.
- Magic bytes beat the declared content type. Servers mislabel routinely, and a
  PDF served as `text/html` is still a PDF.

A download lands as two files side by side: `<name>.md` holding a bounded
excerpt, and `<name>.full.md` holding the complete converted text. One real
reference page converted to 91,190 characters, about 23,000 tokens, and three
of those fill a specialist's context before it has done any work — so reading
the short one is the default and reading the long one is a decision, which is
what the split buys. Both stay in `research/`, because a source whose detail is
genuinely needed must be reachable without leaving the workspace.

The short one is a *structural digest*, not the leading characters
(`src/orchestrator/digest.rs`). It was the leading four thousand characters,
which for a paper is the title, the abstract, and half the introduction —
precisely the part the scholar is told to throw away, so the run paid a
thousand tokens for the wrong thousand tokens and still had to open the full
text to decide whether it was worth opening. A mathematical source carries its
payload in labelled statements, and `Theorem`, `Lemma`, `Definition`,
`Proposition`, `Corollary`, and `Algorithm` are mechanically locatable; so is
the heading outline and so is the abstract. The digest is those three under the
same budget. `Proof` is excluded — it is the argument for a statement already
captured and the longest block on the page. A document with no headings and no
labelled statements falls back to the leading characters, because for that
shape the leading characters genuinely are the document.

The digest is still a placeholder with a job: it names its companion and asks
the scholar to replace it with a summary of what the source establishes, under
a thousand tokens. The bound is mechanical for a fresh download and a standard
the scholar is held to thereafter. A document already short enough is stored
whole, with no truncation notice for truncation that did not happen.

Every folder carries an `INDEX.md` saying what each file is for
(`src/orchestrator/folder_index.rs`). `list_workspace` answers what exists and
cannot answer what anything is *for*, and after a long run nothing on disk
distinguishes the oracle from the answer, or a superseded experiment from the
file the result came out of. `describe_file` records a purpose;
`refresh_index` re-derives the file list from disk, keeps existing
descriptions, marks new files undescribed, and drops rows for files that are
gone. Descriptions are left to explicit tool calls because only the agent that
wrote a file knows why; agreement between the index and the directory is not,
so a forgotten description shows as a visible gap rather than as an index that
quietly disagrees with its folder.

Links are compressed. Anchors become reference-style `[text][n]` with one
`## Links` list at the end, so a URL repeated a dozen times on a page is
written once; tracking parameters (`utm_*`, `fbclid`, and similar) are stripped.
A reference page's navigation targets otherwise fill the context with URLs the
agent will never follow.

The PDF extractor runs inside `catch_unwind` because it panics on malformed
input, and a panic there would destroy work unrelated to the document.

## Workspace layout

The workspace root is an allowlist, not a default. It holds the run's Markdown
— goal, tasks, memory, scratchpad, context, derivation — plus `README.md`,
`AGENTS.md`, `INDEX.md`, and the problem statement. Everything else is filed:

| Kind | Folder |
| --- | --- |
| programs (`.py`, `.sh`, `.c`, `.rs`, …) | `code/` |
| what a program produced | `code/out/` |
| downloaded sources | `research/L0.<n>/`, digested into `research/L1.<n>/` |
| directions of attack | `research/threads/` |
| reflections | `reflections/L0.<n>/` |
| what other programs import | `code/lib/<subject>.py` |
| programs attacking one question | `code/<question>/` |
| plumbing: `config.toml`, `problem.url`, `trace.jsonl`, the document index, the frontier and request ledgers | `config/` |
| untouched download bytes | `raw/` |

`layout::placed` decides this in the write path — `write_document` and an
`apply_patch` `*** Add File:` — for the same reason `documents::research_path`
enforces `research/`: a prompt asking for tidiness holds only until a model is
busy. One live run reached thirty-one Python programs, four JSON tables, and a
scatter of `.out.txt` captures at its root, so the listing every agent reads
before deciding anything was mostly noise and the two files carrying the
derivation were buried in it.

A path that already names a folder is left alone. Naming a folder is a
decision, and the layout has no better information than the caller that made
it. A move is reported in the tool result rather than performed silently: a
model not told where its file went writes the next one to the same place and
then cannot read either back.

`code/` carries its own `AGENTS.md` — one job per file, name for what it
computes, state the complexity before running, keep the naive oracle, never
delete a program carrying a result — so the rules for working there travel with
the folder. Its `INDEX.md` says what established each program is correct, which
is the part that is not readable from the source.

## Inside `code/`

`code/` is a Python package tree, not a drawer. `/workspace/code` is on
`PYTHONPATH` (see the `Dockerfile`), so every folder in it is importable by
name from any working directory and any invocation: `code/lib/perms.py` is
`from lib.perms import lex_ranks`. That line is the whole foundation. Before
it, `PYTHONPATH` held only the pip prefix, so an import resolved by accident —
when a program happened to be started as `python code/<name>.py` and Python put
that folder on the path itself — and failed under every other invocation. The
committed workspaces carry three separate `sys.path.insert` dialects from
agents working that out the hard way, and an agent burned once inlines the
routine instead. Reuse has to be the cheap path or it does not happen.

`code/lib/` holds what other programs import, one subject per module; every
other program is grouped by the question it attacks, one folder per question,
each with its own `INDEX.md`, and what those programs produced under
`code/out/`. `layout::placed` deliberately does not decide which question a
program belongs to. That is a judgement about the mathematics, and a rule
guessing at it would file by extension, which sorts a folder by the one fact
nobody cares about. So the default sink stays `code/`, a caller that names a
folder is trusted, and whether the sink has grown into a pile is measured after
the fact.

`code_layout::plan` is that measurement, and it is built like
`context_tree::plan`: it walks `code/`, reports one fault at a time, writes
nothing, and `briefing` renders the highest-priority one into the organizer's
next cycle. The faults are ordered by cost. A top-level `def` or `class`
defined in three or more programs comes first — copies drift, and a check
passing against one says nothing about the other two; two copies are not a
fault, because a program and the naive oracle it is checked against are
supposed to hold the same routine. Then a `code/` past ten loose programs,
which is what makes the copying invisible. Then a folder of programs with no
`INDEX.md`, which is only illegible rather than wrong.

Measuring this rather than requesting it is the same argument the rest of this
document makes about tidiness, and the same evidence. Six committed Euler
workspaces were asked in a prompt to build a toolkit: one reached forty-six
sibling programs defining `H(n)` seven times, `lex_ranks` six and `power` five;
another wrote thirteen helpers and imported none of them, because what it filed
under `toolkits/` were one-off scripts with their data pasted into the source.
The folder was renamed `lib/` for that reason — a folder called `toolkits`
reads as somewhere to put tools, where `lib/` reads as things other files
import. Asking an organizer to notice a routine typed out three times would
cost it a read of every program in `code/` to discover, which is most of what a
cycle costs; it is a count rather than a judgement, so it is counted.

Every write path enforces it: `write_document`, an `apply_patch` addition, and
`write_tool_file`. That last one was the hole — it wrote wherever it was asked,
so `write_tool_file` with `path: "brute.py"` put a program at the root while
every other path was guarded. A live run did it within four minutes of starting
and left two different `brute.py` files, one filed and one loose, with nothing
to say which was current.

What the write path cannot catch is a shell redirect or a heredoc:
`cat > solve.py <<'EOF'` and `python solve.py > out.txt` reach the filesystem
directly, and the tool sees only a command and an exit code. Asking the
organizer to sweep was not enough — one live workspace collected six root
programs in nineteen minutes, written entirely through the shell while its
organizer was running. So `layout::sweep` runs at the end of every
`execute_command`, where the files appear, and the organizer's sweep is the
backstop rather than the defence.

Three rules keep a sweep that frequent safe. A destination that already exists
is left alone, because a file carrying a result must never be overwritten by
one that shares its name — but the collision is *reported*, because silence
leaves the stray at the root for the rest of the run with nothing to say which
of the two files is current. A failure to move anything is silent, because the
command succeeded and tidying must not turn that into an error. And every move
is named in the tool result, for the same reason `layout::note` exists: an
agent not told where its file went runs `python solve.py` again and cannot
find it.

## Research folder

Every downloaded document is filed under `research/`, enforced by
`documents::research_path` rather than requested in a prompt. Downloads are the
one kind of file that arrives from outside the run, and separating them from the
run's own derivations is what lets an agent tell at a glance what it gathered
from what it worked out.

`research/` and `reflections/` are summary trees, not flat folders
(`src/orchestrator/context_tree.rs`):

```text
research/
├── ROOT.md          what the whole library now establishes
├── INDEX.md         what each file is — maintained by the index tools
├── L0.0/            the first ten originals, sealed
├── L0.1/            the next ten, still filling
├── L1.0/            one note per sealed L0 batch: L0.0.md, L0.1.md, …
└── L2.0/            one note per sealed L1 batch, once L1.0 fills
```

`L0` is the untouched original — the complete converted document, or the
reflection the loop wrote. A *batch* holds at most ten notes; when it fills it
is sealed by one note a level up, named for the batch it covers, and never
revisited.

Two budgets, and the difference is the point. `CONTEXT.md` and each tree's
`ROOT.md` are held to a thousand tokens because they are routed into system
prompts, so every model call in every role pays for them. A seal is held to
four thousand, because nothing carries it in a prompt — it is read on demand by
whoever follows a link down. Applying the tighter cap to both was the wrong
reading of why the cap exists, and it showed: a live seal covering four sources
came to 1,417 bytes against 7,800 bytes of notes, and what survived was one
line per source. That is a catalogue, and `INDEX.md` already is one. A seal is
what a reader opens *instead of* the ten notes below it, so it carries every
distinct result with its hypotheses, not their titles. Sealing once is the point: a flat level
is re-summarised every time anything is added, so the same sources are
re-compressed indefinitely and the summary drifts. `CONTEXT.md` is a root in
its own right under the same cap.

`ROOT.md` is deliberately not `INDEX.md`. The index says what each file *is*
and is derived from the directory by the index tools; the root says what the
library *means* and is written by an agent. Holding both in one file put a tool
and an agent in contention over it and cost three separate rounds of lost
descriptions — a refresh overwriting a synthesis, then a synthesis overwriting
rows, then rows rewritten in a spelling the refresh could not match.

The cap is the point. These files are re-sent on every model call in every role
that reads them, and asking a prompt for "a few hundred words" produced a 6.8 KB
`CONTEXT.md` inside an hour, because each cycle appends what it learned and
nothing ever asks what the file now costs. So compression is a tree rather than
a rewrite: a flat rewrite drops what the last pass judged unimportant, records
nothing about what it dropped, and ends up confident about things no longer
traceable to a source. Every node links what it covers with Obsidian wikilinks,
so the workspace opens as a vault and what a fold leaves out is one step down
rather than gone.

Every seal must link back to each note it compressed, and that is checked
rather than requested: a seal that drops a link has not compressed that note,
it has replaced it — nothing points at the detail any more, and a claim nobody
can trace to a source is worth less than no claim.

`context_tree::plan` measures this on disk and reports one fault at a time —
over budget, then waiting to be sealed, then sealed without its links, then
behind what it covers — and `briefing` renders
the highest-priority one into the research team's next cycle. It writes
nothing: a fold is a judgement about meaning, so an agent writes it; whether a
node is within budget and reflects what is under it is not a judgement, so it
is measured. Structure is recovered from the links themselves rather than a
manifest, because a fold that has stopped linking a note has stopped covering
it — exactly the fact a manifest would hide.

`documents::research_path` and the reflection log both file into the *open*
batch, which `context_tree::open_batch` derives from disk: the highest-numbered
batch still under the fan-out, or the next one when it is full. No writer needs
to know the tree's history.

The librarian receives the root as context so it does not download the same
paper twice. Toolkits keep the older flat shape: a folder, an `INDEX.md`, and
one small file per helper.

## The four derived ledgers

Four files beside the library are written by code, never by an agent, and
re-derived from disk on every relevant write. All four follow the rule
`INDEX.md` already established: what a source establishes is a judgement and
stays with the agent that made it; whether the summary agrees with the files is
not a judgement, so it is measured. Each is described through
`record_description` when it is written, so no derived file sits in
`research/INDEX.md` as `_(undescribed)_` for the life of a run.

`research/CLAIMS.md` (`claims.rs`) is the retrieval change. The unit of the
library was a file, and a file is the wrong thing to retrieve: an agent about
to compute something needs one statement with its hypotheses, not the note that
happens to contain it. A note may carry fenced `claim` blocks — `id`,
`statement`, `hypotheses`, `holds-here`, `status`, `bearing`, `anchor`,
`contradicts`, `answers` — and `search_claims` retrieves those rows. Two checks
fall out that were previously asked for in a prompt and never verified.
`contradicts` naming another claim produces a contradiction the run can see,
which the scholar prompt calls the most valuable thing it can find and which
nothing detected. And `holds-here: yes` with `status: asserted` is a
load-bearing belief nobody verified, which is the distinction the method policy
requires and the one a long run forgets it made. A block missing its `id` or
`statement` is reported rather than dropped: a claim silently discarded leaves
the note reading as though it recorded something.

`research/THREADS.md` (`threads.rs`) is the topic axis. `L0`/`L1`/`L2` fold by
*arrival* and are sealed once, which keeps provenance honest and scatters a
subject across batches — a reader asking what the run knows about the pass rule
gets a seal covering whichever ten things arrived together. One live workspace
built the missing axis by hand, growing a `research/folds/` folder nobody
designed with `game-core.md`, `passes.md`, `counting-arithmetic.md`, and
`deadends.md`. A thread is `research/threads/<slug>.md` with a fenced `thread`
block — `question`, `status`, `rests-on`, `blocked-by`, `next` — and unlike a
seal it is live and rewritten as the direction changes. Dead threads are kept:
a known dead end is a result, and the reason is what stops the next attempt
paying for it again. A thread resting on a claim id that is not on disk is
reported, and so is a blocked thread with no blocker stated, because a blocker
stated precisely is the next research request and one left blank is a mood.

`research/FRONTIER.md` (`frontier.rs`) is the citation graph the converter used
to throw away. `readable.rs` has always parsed every anchor into a reference
table and kept nothing; a converted PDF yields nothing at all, though a
mathematical paper's reference list is exactly where the primary literature on
its subject is named — as arXiv identifiers and DOIs, which are now read too.
Ranking is mechanical and costs no model call: in-degree first, then how well
the citing sentence overlaps `GOAL.md`. In-degree is the signal no search can
provide — a URL three of the library's own sources cite is the standard
reference for the subject, and rephrasing a query will not surface that. The
citing *sentence* is stored with each row, because it says why the source
thought the target mattered, which is the difference between a reading list and
a list of URLs. It doubles as the fetch ledger: a second download of a URL
already in the library is refused with the path of the file that holds it. One
live workspace holds two notes derived from the same arXiv abstract for want of
that check.

`research/REQUESTS.md` (`requests.rs`) is the demand side. Gathering was
triggered by inference — a `STUCK` verdict, a gap named in `ROOT.md`, an
attempt count — and none of those can be closed, so nothing could say whether a
search answered the thing that prompted it. `request_research` states it
instead: what is missing, what the asker would do with it, and what would
falsify the belief they are working from. That last field is what turns a topic
into a question, and it is the best query the run can hand a search. A request
is checked against the claim ledger *before* it is queued, so the common case —
the run knows this and has forgotten — costs a lookup rather than a download;
that is the runtime's reluctance made mechanical rather than requested. Its id
is derived from its text, so the same gap stated by two roles is one row. It
closes when a note carries a claim with `answers: <id>`, so whether the gap was
filled is read off the library rather than asserted by whoever went looking.

`search_claims` and `request_research` travel with the document tools, for the
same reason the index tools do: the role that needs to know what the run
establishes, or that walks into a gap, is whichever one is working.

## Source adapters

`oeis_lookup` (`oeis.rs`) is the first adapter for a structured source, and the
one lookup in the runtime with no phrasing problem. Every other search depends
on guessing what a subject is called — the research prompt spends a paragraph
on that — while a sequence of integers either matches a catalogued entry or
does not, and a match usually carries the closed form that turns an enumeration
into an evaluation. It was a sentence in the research prompt, which is to say
it happened when a model remembered; as a tool it is something a run can be
seen not to have done. A miss is a result: one live workspace recorded `S(n) ∉
OEIS` as a finding, which nobody obtains by rephrasing a query.

Two things it does beyond answering. The entry is filed under `research/` like
any other source, because a formula quoted into a tool result and nowhere else
is a citation the run cannot check later. And the entry's `Cf.` line — the
encyclopedia's own citation graph — goes into the frontier, so a hit on one
sequence surfaces the neighbours describing the same structure.

It is gated with `exa_search` under `MATH_AGENT_RESEARCH`, by not registering
it rather than by asking the model to abstain, because the encyclopedia is the
lookup most likely to hand a self-contained problem its answer outright. It is
granted to `pattern_finder`, which has no web search on purpose — a bounded
structural question must not become a second investigation — and a lookup keyed
on terms that role has already computed cannot become one. It is also the role
holding the terms, so delegating the lookup would spend a child run to pass a
list of integers along.

## Recall: the two ways back into what is known

A run accumulates faster than any one agent can hold, and four tools answer
four different questions about it. `search_documents` matches literal terms
against documents someone called `index_document` on, so it finds a downloaded
source and nothing else. `search_claims` retrieves one statement with its
hypotheses out of the claim ledger. Those two cover the library. The run's own
thinking was covered by neither.

`search_workspace` (`recall.rs`) closes that. It walks the workspace rather
than an index and ranks by cosine similarity over the same deterministic
feature-hashing encoder the notes use, so `MEMORY.md`, `reflections/`,
and `code/lib/` are reachable by wording rather than by a path
an agent already knew. Before it, the inventor re-proposed approaches whose
failure was recorded three files away and the pattern agent rebuilt helpers
that already existed. It hides exactly what `list_workspace` hides: an agent
must not reach the event log through a search when it cannot reach it through a
path.

`recall_research` is the other half and a different question — not what did
*this* run write down, but what has been established before. The notes are in
Qdrant and outlive the workspace.

Both travel to every reasoning role, and `remember_research` does not. Reading
a note costs a lookup; writing one puts a statement into a store every later
run reads, so it stays with the three roles whose output is durable knowledge:
research, the scholar, and the inventor. A test asserts that split, because it
is the kind of boundary that erodes one convenient grant at a time.

Three exclusions, each the same argument the rest of this document makes about
tools being authority. The **judge** gets neither: it answers four lines on
twelve model calls against an attempt that took the better part of an hour, and
a search over the whole workspace is precisely the invitation to spend them
reading — a live judge already did that with the document tools alone. The
**organizer** gets neither, because every tool it lacks is a way a filing job
cannot turn into an investigation. The **tool-builder** gets `recall_research`
but not `search_workspace`: it writes probes and throwaway experiments, so a
similarity search over its own output would mostly return them.

## The scratch

`SCRATCHPAD.md` was the third store and the only one still a file, and it was
the wrong shape for what it held. Being in `role_context` meant every model call
in every role holding it paid for every number anyone had jotted down, whether
or not the turn was about them, and appending a line meant reading the file
whole. `note_scratch` and `recall_scratch` (`vector.rs`) make it the same trade
`remember_memory` and `recall_memory` already make: written once, read back by
wording.

It is a third store rather than a flag on the durable one, and the separation is
the point. `visible_datasets` excludes `math_agent_scratch__*` outright, so
neither `recall_memory` nor `relate_memory` can return provisional work — a
half-finished calculation cannot come back looking like something the run
established, which is the distinction the method policy rests on. It is also
not the knowledge graph: `relate_memory` answers what the run's entities are
connected to, and no amount of traversal recovers what a solve was in the
middle of.

Access is a tool boundary rather than a routing decision, since the file is
gone. `register_scratch` grants both halves to the roles that do provisional
work — the seven code writers, `pattern_finder`, and `goals` — the read half
alone to the scholar and the context curator, which judge provisional work
without producing any, and neither to reflection or the judge, for exactly the
reason the file was withheld from them: unsettled arithmetic read as progress is
what keeps a loop retrying. A test asserts that split.

The dataset is scoped to the project, not the run, for the reason recorded on
the session dataset: `./euler 763` continues from what is on disk, and a scratch
that vanished on restart would be worse than the file it replaces. Ingest is
backgrounded, because a note is written mid-derivation and waiting on an index
would put the memory on the critical path of the arithmetic it describes, which
is the one thing a file did not do.

## Workspace discovery and the reflection log

`list_workspace` renders a bounded tree with file sizes. Agents previously knew
only the file names their prompt happened to mention, so work already on disk
went unread; sizes matter because they distinguish a finished derivation from
an empty placeholder. The listing hides `.workspace-history`,
`.python-packages`, `__pycache__`, the document index, the frontier ledger, and
`trace.jsonl`, and truncates rather than dumping an unbounded tree.

Every reflection is archived to `reflections/L0.<n>/<epoch_ms>_<outcome>.md`, where the
outcome is `nothing` or `<n>_learnings`, and indexed in `reflections/INDEX.md`
in the same step. The folder carries an index for the same reason `research/`
and `code/lib/` do: a directory of epoch-stamped filenames says when each
attempt was judged and nothing about what any of them found. Each row records
the attempt number, the verdict, and the lesson, so the planners and the
inventor can see which attempt is worth continuing without opening any of them.
The loop writes both the file and the row itself — no agent is in that path —
which is why `refresh_index` and `describe_file` refuse the folder outright
(`folder_index::loop_owned`): a hand refresh would replace verdicts and lessons
with `_(undescribed)_`. The organizer's prompt said to leave it alone and a
live organizer refreshed it anyway, which is the usual lesson — a prompt
instruction is not a control. The name carries the result so a
directory listing alone shows which attempts taught the run something. Writing
the log is best effort: the lesson is already in the loop state, and losing the
archive copy must not cost the run the lesson.

## Workspace context routing

Context is authority, and it is also noise. `role_context` in
`src/orchestrator/mod.rs` decides which working files enter each agent's system
prompt. Only `AGENTS.md`, the method policy, goes to everyone.

| Role | Additional files |
| --- | --- |
| orchestrator, goals | `config/config.toml`, `GOAL.md`, `TASKS.md`, `MEMORY.md`, `code/lib/INDEX.md`, `research/ROOT.md`, `research/INDEX.md`, `research/CLAIMS.md`, `research/THREADS.md`, `CONTEXT.md`, `reflections/ROOT.md`, `reflections/INDEX.md` |
| tool_builder, coder, sat_solver, smt_solver, theorem_prover, symbolic_math, lean_prover | the planners' files plus `code/`, minus the threads and the reflection files |
| judge | `GOAL.md`, `MEMORY.md`, `INDEX.md`, `reflections/INDEX.md` |
| reflection | the judge's files plus `TASKS.md` and `reflections/ROOT.md` |
| pattern_finder | `GOAL.md`, `MEMORY.md`, `code/lib/INDEX.md`, `CONTEXT.md` |
| librarian, research | `GOAL.md`, `MEMORY.md`, `research/ROOT.md`, `research/INDEX.md`, `research/CLAIMS.md`, `research/THREADS.md`, `research/FRONTIER.md`, `CONTEXT.md` |
| inventor | the planners' research files plus `research/THREADS.md` and both reflection files |
| scholar | `GOAL.md`, `TASKS.md`, `MEMORY.md`, `research/ROOT.md`, `research/INDEX.md`, `research/CLAIMS.md`, `research/THREADS.md`, `CONTEXT.md` |
| organizer | `GOAL.md`, `TASKS.md`, `INDEX.md`, `code/INDEX.md`, `code/lib/INDEX.md`, `research/ROOT.md`, `research/INDEX.md` |

The tool-builder accumulates what a second program would repeat under
`code/lib/`, one subject per module, described through `describe_file` so
`code/lib/INDEX.md` carries each function's signature, its return, and what
established it correct. One subject per module is what keeps it cheap: reading
the helper you need costs a few hundred bytes rather than the whole library. It
was one *function* per file, which was the tighter reading of the same rule and
cost more than it saved — a routine needing a companion function did not fit,
so it was inlined instead, and the folder filled with helpers nothing imported.
The catalogue is context for the planners too, because what has already been
built and verified changes what is worth delegating next. A row that has
drifted from its function is worse than no row: the next agent calls it as
described rather than reading the source.

Four of these are load-bearing rather than tidy-minded:

- Reflection must see `GOAL.md`. It judges whether the criteria are met, and
  judging against criteria it cannot see is guesswork; a wrong `SOLVED` ends
  the investigation.
- The inventor must see `MEMORY.md` for its failed-approaches section. Without
  it, it re-proposes what already failed, which is the one thing it exists not
  to do.
- Reflection must not reach the scratch. Provisional arithmetic is not
  evidence of progress, and treating it as such keeps the loop retrying. That
  was a routing decision while the scratch was `SCRATCHPAD.md`; now that it is
  a Cognee store it is a tool boundary, enforced by `register_scratch`.
- Only the librarian and research see `research/FRONTIER.md`. It is a list of
  things nobody has read, useful exactly to the roles deciding what to fetch
  next and noise to everyone else.
- The tool-builder and the coder see `research/CLAIMS.md` but not the threads.
  A closed form the library establishes changes what they implement; which
  direction the run is pursuing is the planners' decision, not theirs. The
  `holds-here` column is the load-bearing part — implementing a theorem whose
  hypotheses fail here produces a program that runs and computes the wrong
  thing.

Indexes are the cheap exception to that rule. An index costs a few hundred
tokens where the files it describes cost tens of thousands, so a role that
might otherwise re-derive or re-fetch something gets the relevant catalogue:
both to the planners, the research index to research, the librarian, and the
inventor so none re-establishes what is on disk, the toolkit index to `pattern_finder`
so it reuses a verified helper. Reflection gets the workspace index and nothing
more of the kind — deciding whether an answer was actually produced means
knowing which artifacts exist, and the index says what each one is without the
derivations themselves.

Adding a file to every role is the easy mistake. Ask what the role has to
decide, and give it only what that decision needs. The scholar is the one
legitimate exception: judging whether a source is worth anything requires
knowing what the run wants, what it already believes, and what it is currently
attempting, so it needs all three — and `recall_scratch` besides, because a
half-finished derivation is exactly the kind of thing a paper resolves. It gets
the read half only: it judges provisional work rather than producing any.

## Workspace checkpointing

`checkpoint::WorkspaceCheckpoint` commits the workspace after every successful
write, so a rewritten `solution.py` or an edited belief in `MEMORY.md` is
recoverable instead of lost, and the commit sequence reads as an account of how
the answer was reached.

History lives in `.workspace-history`, not `.git`, with an explicit work tree.
A conventional `.git` would make the product repository treat each workspace as
an embedded repository and refuse to track through it. Only writing tools
trigger a commit, an unchanged tree is a no-op rather than an error, and a
failed checkpoint never fails the tool that succeeded.

When a workspace is first used, the helper copies
the template into it without replacing existing files. The runtime appends
`AGENTS.md`, `config.toml`, `MEMORY.md`, and the relevant role prompt to each
agent's built-in system policy. `GOAL.md` and `TASKS.md` are also loaded. Workspace context must never replace built-in tool or container
restrictions.

The tool-builder also gets `apply_patch` (`src/orchestrator/patch.rs`), which
applies a Codex-format envelope — `*** Begin Patch`, `*** Add File:` /
`*** Update File:` / `*** Delete File:` sections, `@@` hunks with ` `/`-`/`+`
line prefixes — across several files at once. Two deviations from upstream are
deliberate and should stay. Context matching is **exact**, and an ambiguous
hunk is refused rather than resolved: Codex falls back to fuzzy matching, which
suits an interactive tool with a human watching and not a run where a patch
landing in the wrong place yields a program that executes and computes
something else. Application is **atomic**: every operation is resolved against
the current files before a byte is written, so a bad hunk in the third file
cannot leave the first two rewritten. A context line missing its leading space
is read as context anyway — that reading is unambiguous, and it is the most
common way a small model malforms the envelope.

The format is borrowed rather than invented because a documented one the model
may already have seen beats a private dialect it has to learn from a schema.

Every runtime agent receives the workspace document tools: bounded download,
read, write, exact edit, index, and search. The index is
`/workspace/config/.document-index.json` and contains only relative paths in the
selected workspace. Keep the 5 MiB per-document limit and reject non-HTTP
downloads, traversal, symlink escapes, non-UTF-8 content, and missing exact-edit
targets.
Do not move generated artifacts into source directories unless the user asks
to promote a specific artifact into the product.

## Secrets

`.env` is local and ignored by Git. Never read, print, log, commit, or paste its
contents. Document variable names and placeholders in `.env.example`.

The runtime currently expects:

- `OPENROUTER_API_KEY`
- optional `OPENROUTER_MODEL`
- `EXA_API_KEY`
- `LANGFUSE_BASE_URL`
- `LANGFUSE_PUBLIC_KEY`
- `LANGFUSE_SECRET_KEY`
- `QDRANT_URL`, normally supplied by Compose

Compose loads the trusted local `.env` and passes configuration to the agent.
Do not put secret values directly in Docker command arguments.

## Build and test contract

Run these commands from the repository root before reporting code complete:

```sh
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo build --all-targets --all-features
cargo test --all-features
```

Also run the checks that match the changed surface:

```sh
RUSTDOCFLAGS="-D warnings" cargo doc --no-deps --all-features
sh -n agent euler langfuse-turns langfuse-review scripts/run-agent \
  scripts/solve-euler scripts/langfuse-turns scripts/langfuse-review
./agent build
docker compose config --quiet
```

Use a live `./agent` smoke test when changing provider setup, delegation,
research, tool execution, environment forwarding, or Docker behavior. Live
tests spend provider credits, so keep the prompt focused. Never put live network
tests in the deterministic unit-test suite.

Use `./euler <number>` for Project Euler smoke tests. Keep fetched statements
and generated solutions under `workspace/project-euler/<number>`. The wrapper
must fetch the official statement, reject invalid problem numbers, and avoid
prompts that ask agents to find published answers.

Do not ignore or delete a failing test to make CI pass. Fix the cause or report
the blocker with the failing output.

## Rust conventions

Use Rust 2024 and standard `rustfmt` output. The minimum supported Rust version
is 1.96.

- Use `snake_case` for modules, functions, fields, and locals.
- Use `PascalCase` for types and traits.
- Use `SCREAMING_SNAKE_CASE` for constants.
- Keep public exports in `src/lib.rs`.
- Default to private APIs and expose only what callers need.
- Put substantial types in `types.rs` when a module grows large.
- Put module tests in `src/<module>/test.rs`, wired with `mod test`.
- Do not create general `utils.rs` or `helpers.rs` dumping grounds.
- Do not use `unsafe`; the crate forbids it.

Public items need rustdoc. Public fallible functions need an `# Errors` section,
and public functions that can panic need `# Panics`.

Library code must not use `unwrap()`, `expect()`, `panic!()`, `todo!()`, or
`unimplemented!()`. Tests and examples may use `expect()` only when the message
states the invariant.

Use the crate-wide error type for application errors. Add a specific variant
when callers need to distinguish the failure. Keep error messages lowercase
and omit trailing punctuation.

## Tools and research changes

Tools are authority boundaries. Give each specialist only the tools it needs.
The research agent gets Exa and both Qdrant note tools. The tool-builder gets
workspace file and command tools. The orchestrator gets specialist delegation
tools, not direct shell access. Recall is the one thing granted broadly rather
than narrowly, and the argument for it is the same one: reading what the run
already established is how a role avoids re-establishing it. See *Recall: the
two ways back into what is known* for who is excluded and why.

For a new tool:

- define a narrow JSON schema with required fields and no extra properties;
- validate every argument before side effects;
- bound network responses, command duration, and output size;
- return enough context for the model to verify what happened;
- test successful behavior and rejection paths;
- update the specialist prompt and registry metadata.

Prefer primary sources for mathematical definitions and results: original
papers, official documentation, standards, and maintained institutional
references. Search output is evidence to inspect, not text to copy blindly.
Keep URLs in the research result so the orchestrator can cite them.

## Dependencies and vendored code

Check the standard library and existing dependencies before adding a crate. For
new dependencies:

- use a caret-compatible version, not an exact pin;
- disable default features when that meaningfully reduces the graph;
- enable only required features;
- add a comment in `Cargo.toml` explaining the dependency;
- keep `Cargo.lock` committed.

TinyAgents lives at `vendor/tinyagents` as a Git submodule. Initialize it with:

```sh
git submodule update --init --recursive
```

Do not edit vendored code through the parent repository. Make TinyAgents
changes upstream, push them there, then update this repository's gitlink in a
separate commit.

Never export `CARGO_TARGET_DIR` or send build output to a temporary directory.
Use the checkout's normal target configuration.

## Git workflow

- Work in the current checkout. Do not create or use Git worktrees.
- Do not create feature branches.
- Commit directly to `main` and push `main` to its configured remote.
- Never force-push, rewrite published history, or bypass hooks.
- Keep commits focused, with concise imperative subjects.
- Preserve unrelated user changes in a dirty working tree.

An auto-commit hook may checkpoint edits while work is in progress. Those
commits are expected. Do not reset or rewrite them. Commit manually only when a
specific boundary matters.

## Prompts

The built-in prompts live in `src/prompts/*.md` and are pulled in with
`include_str!`, not written as Rust string literals. They were literals, and
the escaping made the most consequential text in the runtime the most awkward
to edit: every line ended in a `\` continuation, every newline was `\n`, and a
reflow produced a diff nobody could read. A Markdown file has none of that, and
`include_str!` keeps them compiled in, so the container still needs no prompt
files mounted.

Inspect the assembled result with `./agent prompts` (add `--workspace <path>`
to render a specific workspace), which prints every role's full system prompt
with character and token counts. It runs on the host and needs no container,
provider key, or spend. Use it after changing a prompt or the context routing:
until it existed the only way to see what an agent was actually told was to
start a run and read a provider trace, which made a misrouted file or a rule
that reads as optional invisible until it changed a run's behaviour. The token
counts are the other half — every prompt is re-sent on every model call in that
role's run, so a prompt that has grown is a bill that has grown.

Keep the shared method policy leading every assembled prompt. The provider
cache is keyed on the exact leading prefix, so role-specific text first would
make each agent its own cache namespace. A test asserts both the ordering and
that no prompt file's stray trailing newline can change the prefix.

## Documentation rules

Keep `README.md`, this file, rustdoc, examples, and runtime behavior consistent.
Write for a reader who has not seen the code. Prefer a concrete command or
example over broad claims.

Keep every Markdown file at 500 lines or fewer. Put durable operational guidance
in this file and user-facing instructions in `README.md` instead of creating a
separate documentation tree.

## Working agreement for coding agents

1. Inspect the surrounding code before editing and match its conventions.
2. Execute a clear task directly. Do not stop for a plan when the next step is
   obvious.
3. Stay within scope. Raise unrelated problems instead of folding them into the
   change.
4. Deliver finished code without placeholders or commented-out alternatives.
5. Preserve security checks, tests, lints, and Docker restrictions.
6. Report commands actually run and their real outcomes.
7. Ask only when an irreversible choice or genuine product fork blocks work.
