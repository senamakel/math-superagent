# Roles, adapters, and what each one can reach

The twenty-one roles the runtime registers, the sources they read through, and the two ways any of them gets back to what the run already knows. What a role is *told* is in [context routing](#workspace-context-routing) at the end of this file; what it is *allowed to do* is the tool boundary each section describes.

The working agreement is [`AGENTS.md`](../AGENTS.md); this file is the part of it that goes deeper than a rule.



## The frontier ranks citations, not indexes

Two link classes flooded it, and each needed a different rule.

Publisher furniture came first: an arXiv abstract page carries a toolbar of
third-party services, and because it appears on *every* abstract page it
accumulates citers faster than any reference can. A live Erdős–Gyárfás frontier
had its top seventeen rows tied at six citers, all of them Connected Papers,
alphaXiv, DagsHub, Hugging Face and the rest, above every paper. Named hosts and
path fragments handle that, plus a rule that a host with no dot is not on the
public internet — 64 candidates were on `backend:8080`, a container name reachable
only from the page that rendered it.

Reference works needed the other rule. An OEIS page lists every cross-referenced
sequence and a Wikipedia article links hundreds of articles; both are indexes,
exhaustive by design, and a live Project Euler 241 frontier was two thirds
Wikipedia and OEIS with seventeen rows whose whole stated reason was
`cross-referenced from A159907`. So a reference work linking *itself* is dropped
and a reference work linking *outward* is kept — a Wikipedia article's reference
list is papers and DOIs, which is what the run cannot reach on its own. The rule
is deliberately not "same host is never a citation": an arXiv paper citing
another arXiv paper is the ordinary case and the frontier's whole point.

## The research team gathers by default

It did not, and that is why four live runs made zero `exa_search` calls between
them. The team's brief opened *"Keep this run's reference library useful, which
mostly means not adding to it"* and made fetching conditional on an attempt
reporting STUCK or `research/REQUESTS.md` naming a gap. Neither can hold at t=0:
attempt 1 has only just started and a fresh workspace has no `REQUESTS.md`. So
it replied NOTHING FURTHER, and because it was `Completion::Attainable` that
reply retired it permanently — inside ninety seconds on every run, leaving hours
with no research beside the solve.

A goal reached before the work starts was never attainable; it was abstention
with a completion flag on it. The team is now `Standing`, so a quiet cycle is a
pause, and its brief leads with searching widely, names `exa_search` as the
instrument most often left unused, and forbids downloading a URL that did not
come from a search result, `FRONTIER.md`, or a held source — because a fetch of
an invented address *succeeds* and files the wrong paper under the name the
model wanted. A live Project Euler run did exactly that, storing *Graded Lie
Algebras of Maximal Class II* as `pitman_ballot_theorem.md`.

## Expected problem-solving behavior

The runtime has twenty-one roles plus an explicit solution loop.

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
  something, and a proof that compiles with no `sorry` is the thing itself.

  It *was* held to reporting `#print axioms` and every remaining `sorry` by its
  prompt — this repository's own recurring failure, in the one place it costs
  most. Lean and Mathlib were the largest thing in the image and no line of Rust
  ran either, so `research/CLAIMS.md` could not tell a kernel-checked lemma from
  a sentence claiming one, and did not try. Formal verification was held to a
  weaker standard than path traversal.

  `lean_check` is the control: it runs the kernel, parses what came back —
  compiled or not, every `sorry` warning, every `#print axioms` line — and files
  the verdict under `code/out/lean/`. A claim may be `status: formalised` only
  with a `formalisation:` line naming a `.lean` file whose verdict passed;
  otherwise the ledger records it as `asserted` and says why, under *Called
  formalised, not backed by the kernel*. The fourth passing condition reads as
  strict on purpose — the file must contain a `#print axioms` line — because a
  proof whose foundations are unstated has told the runtime nothing, and the
  rule costs one line. The tool reaches this role and nothing else, since it
  decides what the ledger's strongest evidence class may say.
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
  stalled, and does it *with* research rather than beside it. At a diversify the
  loop runs it twice: it proposes three divergent candidates and writes each to
  `research/approaches/<slug>.md`, research grounds or refutes each against the
  literature, and it then adopts one or synthesises a better one from what came
  back — that combination being where a new line of attack usually comes from.
  It also holds a one-role delegation bench (`INVENTION_BENCH`) so a single
  literature check need not wait for the next diversify; recursion is bounded at
  one level because research has no delegation tools. It is handed a dossier
  assembled from disk at delegation time rather than the workspace as it stood
  when the container started, which on a twelve-hour run is the difference
  between seeing the work and seeing an empty workspace. It is one of the four
  roles on the stronger reasoning model — see `REASONING_ROLES` and
  [`docs/runtime.md`](runtime.md) — because its whole output is a judgement
  nothing mechanical can check.
- The reducer works backward from the goal, and is the inventor's opposite
  number rather than its variant. The inventor asks what *else* could get us
  there and answers with a route; the reducer asks what would be *enough* and
  answers with lemmas. It writes a proof skeleton to
  `research/backward/<slug>.md` — the goal, the inference combining the lemmas,
  and one `gap` block per lemma nobody has proved — and `research/BACKWARD.md`
  is derived from those files. Every open gap carries a first move a
  tool_builder could run today, which is what makes it a task rather than a
  wish; a lemma with no first move belongs in `request_research`. It exists
  because a run can report genuine progress on every attempt, verify more and
  more data, and spend its whole budget having never written down what a proof
  would consist of. Its tool set is the narrowest of any role that writes: the
  document tools and the memory tools. No search (a role that can search turns
  "what would suffice" into a literature survey), nothing that computes (a gap
  is discharged by a proof or a claim, never by a program this role wrote), no
  delegation bench (a skeleton is checked by the forward loop attacking its
  gaps), and no scratch (a gap opened on unsettled arithmetic is a task nothing
  can close). It is also denied `research/APPROACHES.md`, in its prompt context
  and in its dossier, because a role holding the method ledger drifts into
  proposing methods. Like the inventor it is on the stronger reasoning model:
  whether a set of lemmas actually implies the goal is the definition of a
  judgement no tool can check.
- The weakener is the third direction, and the only role permitted to move the
  target. The inventor asks what *else* reaches the goal and the reducer asks
  what would be *enough*; both hold the goal fixed. This one asks what would be
  *easier*, and answers with a problem that is deliberately smaller. It names
  the difficulties that make the goal hard, then writes a ladder of weakened
  versions to `research/weakened/<slug>.md` — each rung saying which
  difficulties are switched off and what turning the next one back on would
  take — and `research/WEAKENED.md` is derived from those files. It exists
  because `solved` was binary: a run that proved a weakened case had one word
  for it, and that word was *unsolved*. A rung does not imply the goal, which is
  not a defect in it. A rung that was attacked and failed stays on the ladder
  with the reason, because deleting it is how the same one is proposed again
  three attempts later. Its tool set is the reducer's exactly, for the reducer's
  reasons, and it is on the stronger reasoning model because a statement
  weakened until it is vacuous reads exactly like one weakened until it is
  tractable. Its one dangerous failure is reporting a rung as the goal, so the
  ledger records which difficulties were off when each one landed.
- The searcher does not reason toward an object; it writes programs that build
  one, keeps what scores well, and proposes again from those. What makes the
  FunSearch loop worth having is not the loop but its output — "not the set of
  512 eight-dimensional vectors in itself, but a program that generates it" —
  since a construction with a readable program behind it is an explanation where
  a number is only an answer. Three of the four ingredients (one evolved
  function, best-shot prompting, an island population) are bookkeeping and live
  in Rust: a model recalling which of four hundred programs scored best is
  spending its turn on arithmetic nothing can get wrong in code.

  **Its authority is a set of absences.** No `write_tool_file`, no
  `execute_command`, no patch tool. `submit_candidate` is its only route to
  disk, and it writes into `candidates/` and scores what it wrote in the same
  call — so a candidate cannot be recorded without having been executed, and
  `score.py` is unreachable. The second is the load-bearing one and the risk is
  measured rather than hypothetical: AlphaEvolve proved "extremely good at
  locating exploits in the verification code", satisfying a minimum-distance
  constraint by stacking points nearly on top of one another, and Tao's team
  rewrote every verifier in exact arithmetic in response. A searcher that could
  edit its verifier would be grading its own work. A test asserts the absences,
  because this boundary is the kind that erodes one convenient grant at a time.

  A rejected candidate costs one line and no lesson — a search is wrong
  thousands of times cheaply, and per-rejection guidance would be re-read on
  every one — but it is still *recorded*, so the board can say how many
  candidates bought the best score. Four hundred without improvement is a
  finding no leaderboard of winners can show.
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
- The director is the only role a person talks to directly. It receives one
  operator directive from `config/directives.jsonl` and carries it into the
  files that decide what happens next — reordering `TASKS.md`, opening or
  killing a thread, amending `CONTEXT.md`, filing a research request. It exists
  because the next attempt already gets the directive verbatim, and a directive
  that does not change the plan on disk changes nothing once that attempt is
  over. It has the document tools and nothing that computes: no shell, no tool
  writing, no delegation. It is also the one reasoning role denied
  `research/CLAIMS.md`, because a directive is asserted rather than established
  and a role acting on an unevidenced instruction should not be holding the
  evidence ledger while it does. Its reply is written to
  `config/DIRECTIVES.md`, which is what the operator reads, so a directive it
  declines has to say why there rather than be silently dropped.

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
run reads, so it stays with the roles whose output is durable knowledge:
research, the scholar, the inventor, and the reducer. A test asserts that split,
because it is the kind of boundary that erodes one convenient grant at a time.

The reducer is on that list for the strongest version of the argument. A
conjecture reduced to lemmas, with the claim that closed each one named beside
it, is the most durable thing this runtime can produce about a problem — it
survives the workspace, it survives the approach that produced it, and a later
run re-deriving it is the most expensive way to find out it was already known.
It is also why the reducer holds all three memory tools rather than the reading
pair: `relate_memory` is the query a decomposition actually wants, since a
reduction usually comes from a link between two things the run learned
separately and never stated together.

Three exclusions, each the same argument the rest of this document makes about
tools being authority. The **judge** gets neither: it answers four lines on
twelve model calls against an attempt that took the better part of an hour, and
a search over the whole workspace is precisely the invitation to spend them
reading — a live judge already did that with the document tools alone. The
**organizer** gets neither, because every tool it lacks is a way a filing job
cannot turn into an investigation. The **tool-builder** gets `recall_research`
but not `search_workspace`: it writes probes and throwaway experiments, so a
similarity search over its own output would mostly return them.

## Workspace context routing

Context is authority, and it is also noise. `role_context` in
`src/orchestrator/mod.rs` decides which working files enter each agent's system
prompt. Only `AGENTS.md`, the method policy, goes to everyone.

| Role | Additional files |
| --- | --- |
| orchestrator, goals | `config/config.toml`, `GOAL.md`, `TASKS.md`, `code/lib/INDEX.md`, `research/CLAIMS.md`, `research/THREADS.md`, `research/APPROACHES.md`, `research/BACKWARD.md`, `CONTEXT.md` |
| tool_builder, coder, sat_solver, smt_solver, theorem_prover, symbolic_math, lean_prover | the planners' files, minus the threads, plus `code/AGENTS.md` and `code/INDEX.md` |
| judge | `GOAL.md`, `INDEX.md` |
| reflection | the judge's files plus `TASKS.md` |
| pattern_finder | `GOAL.md`, `code/lib/INDEX.md`, `CONTEXT.md` |
| librarian, research | `GOAL.md`, `research/CLAIMS.md`, `research/THREADS.md`, `research/APPROACHES.md`, `research/FRONTIER.md`, `CONTEXT.md` |
| inventor | `GOAL.md`, `research/THREADS.md`, `research/APPROACHES.md`, `research/CLAIMS.md`, `CONTEXT.md`, plus a dossier built at delegation time |
| reducer | `GOAL.md`, `research/BACKWARD.md`, `research/CLAIMS.md`, `research/THREADS.md`, `CONTEXT.md`, plus its own dossier built at delegation time — and deliberately **not** `research/APPROACHES.md` |
| weakener | `GOAL.md`, `research/WEAKENED.md`, `research/CLAIMS.md`, `research/THREADS.md`, `CONTEXT.md` — and deliberately **not** `research/APPROACHES.md` or `research/BACKWARD.md` |
| searcher | `GOAL.md`, `research/CLAIMS.md`, `CONTEXT.md` — everything about the search itself arrives through `search_brief`, because it changes with every candidate |
| scholar | `GOAL.md`, `TASKS.md`, `research/CLAIMS.md`, `research/THREADS.md`, `CONTEXT.md` |
| context_curator | `GOAL.md`, `TASKS.md`, `INDEX.md`, `research/CLAIMS.md`, `research/THREADS.md`, `research/APPROACHES.md`, `research/BACKWARD.md`, `CONTEXT.md` |
| director | `GOAL.md`, `TASKS.md`, `research/THREADS.md`, `research/APPROACHES.md`, `CONTEXT.md` |
| organizer | none — it falls through to the empty default |

That table is what `role_context` returns today, and it is narrower than what
this document described for a long time. `MEMORY.md`, `research/ROOT.md`,
`research/INDEX.md`, `reflections/ROOT.md`, and `reflections/INDEX.md` appear in
no arm of the match, and the organizer has no arm at all.

**The code is right, and `MEMORY.md` is retired.** It was a file every role was
told to append to and none owned, which is how it drifted: a live conjecture run
reached a kernel-checked Lean lemma, a verified graph reconstruction and
seventeen claims without writing a line of it, because it was being asked to
maintain a file no prompt would ever show it. What it did is now done by three
things that are each owned and each measured. `CONTEXT.md` carries the beliefs —
the curator owns it, it is routed to every reasoning role, it is held to a token
budget, and it separates `Established` from `Recalled (durable memory — not this
run's own findings)`, which `MEMORY.md` never did. `research/CLAIMS.md` carries
the statements one at a time with hypotheses, `holds-here` and `status`, derived
from the notes rather than asserted. Cognee carries what outlives the workspace.
The launchers' phase-2 text points at `CONTEXT.md` and the claim ledger for the
same reason.

The inventor's failed-approaches need is met by `CONTEXT.md`'s `Ruled out`
section and, more directly, by `research/APPROACHES.md`, where a closed line of
attack keeps the reason it closed. The organizer having no arm is not a gap either —
the role was removed; see `docs/runtime.md` if its name still appears in the
registry list there.

`research/ROOT.md`, `research/INDEX.md` and the two reflection files remain
genuinely unrouted, and that one is **unresolved**. It is recorded here rather
than quietly reconciled, because a routing table that flatters the code is how a
role comes to be missing the one file its prompt is written around.

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
  to do. **It does not currently receive it**: no arm of `role_context` names
  `MEMORY.md` for any role. The inventor can still reach the same material with
  `recall_memory` and `search_workspace`, so this is a rule the code stopped
  guaranteeing rather than one it contradicts — but the whole argument for
  routing a file into a prompt is that the role should not have to think to go
  and look. Either route it again or strike the rule; leaving both is what makes
  a document stop being evidence about the runtime.
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

## The standing teams run on a custodial budget

`CONTEXT.md` has an owner, which it did not. It was written by whichever role
happened to think of it, so it drifted behind the run that reads it on every
model call, and nothing measured what it cost. The `context` team owns it now:
one standing team running `context_curator` every `MATH_AGENT_CONTEXT_MINUTES` —
fifteen by default — whose whole job is keeping that one file current and within
budget. It reads widely and writes once. Most of what it brings across is
Cognee's: `recall_memory` and `relate_memory` hold what earlier runs on this
problem, and on problems of its shape, established, and that is invisible to this
run until somebody carries it into the file every role already reads. It holds no
shell, no web search, and no delegation, because each of those is a way for
curating what the run knows to turn into a second investigation beside the solve.

Frequency and cycle length are separate axes, and bounding one is not enough. A
live Erdős–Gyárfás run had the curator as its largest consumer — 55 model calls
against `tool_builder`'s 38, growing five times faster than the role actually
doing the mathematics, and spending 69 `read_document` calls walking `code/` and
`research/` file by file. Throttling `MATH_AGENT_CONTEXT_MINUTES` to fifteen left
it one cycle in three minutes and it was *still* the top consumer, because that
single cycle cost eleven model calls. So the curator is registered with
`RunBudget::for_housekeeping()` as well: curating is bounded work — read what
changed, rewrite one file — and a role left with an investigation's budget
investigates, which is the organizer's lesson exactly. Reaching the cap is safe,
because `StopWithPartial` keeps the brief already written.

Its cadence is configuration rather than a constant for one reason: it decides
how stale the brief every role reads may be. Everything else about its allowance
is the custodial one — the file keeps changing underneath it, so "nothing to add"
means come back later rather than stop. Idleness is decided before the agent
runs, by fingerprinting the workspace with `CONTEXT.md` excluded: counting its
own output would have the team waking itself forever on the brief it just wrote,
the pattern team's `SCRATCHPAD.md` lesson again. And the standing — what the file
costs against its budget — is computed per cycle and written into the brief,
because it is the fact that decides what the cycle is *for*: adding, or
compressing.

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
