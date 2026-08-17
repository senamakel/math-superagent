# The derived ledgers

The files in `derived/` are written by code, never by an agent, and re-derived
from disk on every relevant write. The folder name is the invariant — nothing in
it is hand-written — and the file tools refuse it, so `read_ledger` is the way
in: it bounds what it returns and selects by `id`, `status` or `query`, where
`read_document` returned all 7,488 tokens of `CLAIMS.md` to answer about one
row. A workspace written before the folder existed is migrated once, at startup,
never overwriting — and on the host by `examples/migrate_derived`, because
startup only reaches a workspace somebody starts, and an unmigrated one fails
quietly: the prompts route `derived/*`, `load_workspace_files` skips a path that
is not there, and the role is told less with nothing saying so.

```sh
cargo run --example migrate_derived -- workspace/conjectures/*
```

All nine follow the rule `INDEX.md`
already established: what a source establishes is a judgement and stays with the
agent that made it; whether the summary agrees with the files is not, so it is
measured. Each is described through `record_description` when written, so no
derived file sits in `research/INDEX.md` as `_(undescribed)_` for a whole run.

Where they live in the tree, and what an agent writes to produce them, is in
[`workspace.md`](workspace.md).

## What a ledger may cost a prompt

Every one of these is routed into at least one role's system prompt, so its size
is a bill paid on every model call in that role. On one live workspace the nine
came to **393,995 of the 770,134 tokens** across all twenty-two assembled
prompts — 51% — and nothing measured it.

`derived/APPROACHES.md` was 86 KB of that, and the shape of the failure is the
part worth keeping. Every module had a `MAX_ROWS` and a `FIELD_CHARS`, and both
governed the *table*. The list sections underneath — *What closed, and why*,
*Not yet taken to the literature* — were written afterwards and bounded by
nothing, so the table was about 2 KB and the sections were 84 KB, one refutation
of them 5 KB on its own. Nothing was broken and no test failed. The file grew,
and it was a third of the orchestrator's 63,833-token prompt before anybody
counted.

Three things now stand between a renderer and that, and the order matters
because each catches what the one before it cannot.

**Every list section goes through `ledger::budget::listed`.** It renders at most
`MAX_LISTED` rows, truncates each prose field to `REASON_CHARS`, and returns how
many rows it left out — which the caller must render, with the directory the
rest is in. Both halves are load-bearing. Bounding the rows alone still admits
forty five-kilobyte reasons, which is the same file by another route; and a
section cut to its bound while reading as complete is worse than a long one,
because the reader concludes the run holds nothing more.

**The bounds are asserted, not intended** (`ledger/ceiling_test.rs`). Each
ledger is rendered from a deliberately absurd fixture — sixty entries, six
kilobytes of prose per field — and held under a stated ceiling. One test does
not check a size at all: it renders sixty entries and then a hundred and eighty,
and asserts the file grew by under two hundred characters. A ceiling alone
cannot catch a section that grows slowly, and *past the bound, more entries must
not mean more file* is the property that actually matters. Reintroducing the
original defect makes the approach fixture render 209,312 characters and fails
both.

**A per-file budget is enforced where the tokens are spent** (`ledger::fit`, in
`load_workspace_files`). Ten thousand tokens, the same `CONTEXT.md` gets, on the
argument that no derived table has a case for costing more than the shared
brief. This is a backstop and should never fire: a cut here lands wherever the
character count falls, where a renderer can drop the fortieth closed approach
and say so. It exists because the first two controls live in the modules that
failed, and this one does not — and because the brief can be handed to a curator
to compress, while a ledger is written by code and nothing in the run can make
it smaller.

## The index: what a prompt carries instead of the ledger

Bounding the sections took the nine from 404,873 tokens across the twenty-two
assembled prompts to 259,175. Most of what was left was still being re-sent on
every model call to answer a question nobody was asking yet.

The obvious next move is to replace each file with a sentence saying it exists
and how to read it. That fails, and the reason is worth stating precisely: the
obligation these files discharge is **specific**. It is not *be aware there are
approaches*, it is *do not re-propose this one*. It is not *claims exist*, it is
*do not re-prove this statement*. A description discharges neither, because
neither is about the ledger — both are about the entries.

So `ledger::index` keeps every entry's *identity* and drops the *reasoning*: one
line per entry with its id, its status, and a headline, ending in the exact
`read_ledger` call that fetches the rest. It is computed on the way into a
prompt rather than written to disk — a second file would be a second thing to
re-derive, keep in step, and describe — and `ledger::fit` still runs behind it.

| | routed whole | bounded | indexed |
| --- | ---: | ---: | ---: |
| `APPROACHES` | 25,763 | 8,822 | ~1,900 |
| `WEAKENED` | 7,808 | 7,630 | ~1,300 |
| `CLAIMS` | 8,248 | 7,488 | ~3,700 |
| `BACKWARD` | 7,801 | 5,186 | ~800 |
| **all 22 prompts** | **770,134** | — | **491,924** |

Three things that table settles, each of which is now a rule:

### The ledgers an index reaches

The four above were the four `ledger::indexed` had an arm for, and for a while
they were the four it indexed. That left the largest file in the runtime routed
whole, because the match fell through to `None` for everything it did not name:

| | routed whole | indexed | in _n_ prompts |
| --- | ---: | ---: | ---: |
| `TASKS.md` | 8,539 | 1,073 | 13 |
| `derived/BLUEPRINT.md` | 2,604 | 1,617 | 3 |
| `derived/THREADS.md` | 1,122 | 449 | 10 |
| **all 24 prompts** | **445,575** | **338,815** | — |

`TASKS.md` is the lesson. It is a *declared* ledger rather than a Rust-module
one, so no arm named it and none ever would have — the fix is not another arm
but a fallback keyed on each declaration's own `derived` path, which covers the
built-in queues and any ledger a run declares mid-flight, on the pass that
renders it. Most of what it dropped was history: closed and abandoned rows,
whose `detail` and `reason` fields came to 8,539 tokens in each of thirteen
prompts — 25% of everything assembled — to discharge an obligation (*do not
re-propose this*) that an id beside the word `dropped` discharges on one line.

### What an index cuts, and what it never cuts

An index is read top-down for what to do next, so the open rows are the work and
the closed ones are the archive. Every open and blocked row is carried; each
*closed* status keeps its five most recent and the header says how many it left
and in which status, so a reader who needs the rest calls
`read_ledger { ledger: "tasks", status: "done" }` rather than concluding the run
finished nothing else. Closedness is read off the declaration rather than off a
status name, so a ledger a run defines mid-flight gets the same treatment and
the ledgers that declare no closed status — most of them — are untouched.

The cut is per status rather than one bound over the archive, because `done` and
`dropped` answer different questions. Re-proposing something already ruled out
is the cheapest mistake available, and a shared cap would let a busy `done` list
push every `dropped` row out of the file that prevents it.

### The catalogue

The reader brief used to say *"`list_ledgers` names every one"* and stop, which
puts the answer behind a call a model has to think to make — the `post_board`
failure exactly. Every role that reads a ledger is now told which ledgers exist:
one line each, the slug, a truncated purpose, and whether that role may write
it. It is derived from the registry at assembly, so a ledger declared mid-run is
named in the next prompt built, and `writable_by` is what prints "yours to
write" — a role learns which ledgers are its own from the list rather than from
a refusal.

`define_ledger` and `retire_ledger` are told to the two planners that hold them,
in a brief of their own, and to nobody else: a paragraph about declaring an axis
reads to the other twenty roles as an invitation to ask somebody to.

Two deliberate exclusions. `derived/ENTAILMENT.md` is under
`index::worth_indexing`, for the reason below. `derived/FRONTIER.md` is not:
its entries are keyed by URL, so an index would keep the longest part of every
row and drop the citation count that is the reason to open it — the same
finding, reached by hand rather than by the threshold.

`BLUEPRINT` is the one index that carries something besides rows. A cycle means
some node's standing was computed from itself, so every line beneath it
describes an argument that does not close; leaving that to `read_ledger` would
be a warning that arrives only if somebody pulls the file, about the rows they
are already reading. It goes in the purpose, above the list.

**The win is per-ledger, not uniform.** `APPROACHES` collapses furthest because
its payload is refutation prose nobody needs until they are considering that
approach. `CLAIMS` only halves, because a claim's *statement* is the payload and
cannot be indexed away — so it indexes at 240 characters of statement where the
approach ledger keeps 110 of reason. The headline width is the caller's, not a
constant.

**Indexing a small ledger costs more than it saves.** `derived/ENTAILMENT.md`
is 266 tokens and an index of it, carrying a header explaining how to read the
rest, comes to about 440. `index::worth_indexing` is that made mechanical; a
uniform rule would have made two files larger.

**The saving is only real if the pull happens.** A role that never calls
`read_ledger` is cheaper *and dumber* — strictly worse than before the bound,
because it reads a shortened list, concludes the run holds nothing more, and
re-proposes what was cut. Every index therefore ends with the call that fetches
the rest, and a test asserts every role reading one is told the copy is
shortened. The judge and the searcher are the two exceptions, both told in their
own prompts not to read around the investigation; they keep the tools and lose
only the instruction.

`ledger_report` prints what each ledger costs on disk beside what the current
build would render, because those disagree until something writes to that ledger
— so a run started before a bound changed keeps paying the old price, and
reading only the on-disk column reports a fix as landed while every prompt still
carries the old file.

```sh
cargo run --example derive_ledgers -- workspace/conjectures/gilbreath
```

`derived/CLAIMS.md` (`claims.rs`) is the retrieval change. The unit of the
library was a file, and a file is the wrong thing to retrieve: an agent about
to compute something needs one statement with its hypotheses, not the note that
happens to contain it. A note may carry fenced `claim` blocks — `id`,
`statement`, `hypotheses`, `holds-here`, `status`, `bearing`, `anchor`,
`contradicts`, `answers`, `search-frame` — and `search_claims` retrieves those
rows. Two checks
fall out that were previously asked for in a prompt and never verified.
`contradicts` naming another claim produces a contradiction the run can see,
which the scholar prompt calls the most valuable thing it can find and which
nothing detected. And `holds-here: yes` with `status: asserted` is a
load-bearing belief nobody verified, which is the distinction the method policy
requires and the one a long run forgets it made. A block missing its `id` or
`statement` is reported rather than dropped: a claim silently discarded leaves
the note reading as though it recorded something.

A formalised or conditional claim is joined to its verdict here, and the join
now asks two more questions than "what did Lean say". A verdict whose recorded
`source_digest` does not match the file on disk is **stale** — the kernel
accepted text the file no longer contains — and the claim drops to `asserted`
naming the file. A verdict carrying no `collector` block at all is reported
under *Formalised on a verdict with no provenance* and keeps its standing, which
is a migration allowance rather than a judgement:
[`docs/lean-library.md`](lean-library.md#the-collector-stamp-collected-against-supplied)
has both halves and the honest limit of each.

`search-frame` is the field a computational claim is worth. A claim with
`status: checked`, or any claim naming a `refutation`, rests on a program that
swept a space, and the claim is worth the space and no more — so the ones that
never say what they swept render as *Searched, with no frame recorded*. The
asymmetry is why it is a section and not a nicety: a sweep that *found*
something is evidence with or without a frame, while a sweep that found nothing
is evidence of nothing at all until the space is stated, and is indistinguishable
in a table from a question nobody asked.

ProofAtlas supplied the failure
([`research/proofatlas/02-refutation-path.md`](../research/proofatlas/02-refutation-path.md)).
Its Domineering counterexample sits on a 9×8 board; every earlier search had been
bounded at 7×7 and at twenty empty cells, so the witness was outside every frame
tried and no additional compute inside them would ever have reached it. Neither
published page records a frame, so nothing on either could have shown that. The
frame is rendered as a gap rather than enforced as a downgrade — a sweep really
did run, and calling it asserted would be false in the other direction; what is
missing is one sentence, and the row asks for that sentence by name.

`status: catalogued` renders its own section, *Taken from a catalogue*, rather
than joining the unverified list, because the two debts differ: an asserted claim
is settled by a proof or a second source, a catalogued one only by a program that
reproduces the terms without reading the catalogue. Project Euler 241 is why this
is code rather than a prompt. Its answer came from twenty lines summing a
hardcoded copy of OEIS A159907's b-file — a sequence whose definition is the
problem's condition restated — while the run's own enumeration found 5 of the 9
terms below 10^8, and both files sat in `code/` with equal standing. A lookup is
good evidence that a result is right and none about why, so it may confirm a
final answer and never be the reason for one.

`derived/THREADS.md` (`threads.rs`) is the topic axis. `L0`/`L1`/`L2` fold by
*arrival* and are sealed once, which keeps provenance honest and scatters a
subject across batches — a reader asking what the run knows about the pass rule
gets a seal covering whichever ten things arrived together. One live workspace
built the missing axis by hand, growing a `research/folds/` folder nobody
designed with `game-core.md`, `passes.md`, `counting-arithmetic.md`, and
`deadends.md`. A thread is `research/threads/<slug>.md` with a fenced `thread`
block — `question`, `status`, `rests-on`, `blocked-by`, `next` — and unlike a
seal it is live and rewritten as the direction changes. Dead threads are kept: a
known dead end is a result, and the reason is what stops the next attempt paying
for it again. A thread resting on a claim id not on disk is reported, and so is a
blocked thread with no blocker stated — a blocker stated precisely is the next
research request, and one left blank is a mood.

`derived/APPROACHES.md` (`approaches.rs`) is what the run has tried to
*think* of, beside what it has tried to compute. A thread is already anchored
to the library, so nothing held the step before it: a candidate reformulation.
That went into one prose field on the solution state and was gone by the next
attempt, so an idea proposed at attempt three could be proposed again at
attempt six and the literature check that would have killed it never happened.
An approach is `research/approaches/<slug>.md` with a fenced `approach` block
— `idea`, `mechanism`, `status`, `precedent`, `first-step`, `killed-by` — whose
stances are a life cycle rather than a flag: `proposed`, `grounded`, `refuted`,
`adopted`, `spent`, `narrowed`, `reserved`. Empty `precedent` means nobody
checked, which is not the same as nothing having been found; refuted and spent
approaches are kept with their reasons, on the dead-thread argument.

The last two stances were read off ProofAtlas, whose route dispositions are
seven-valued where this was five
([`research/proofatlas/05-open-workspace-shape.md`](../research/proofatlas/05-open-workspace-shape.md)).
Both hold a *result* the other five discard by collapsing it into `refuted`:

- `narrowed` failed in general and holds on a restriction, named in a required
  `survives` line. It is deliberately **not** closed — the restriction is live
  work, and an inventor forbidden to propose it loses the one thing the failure
  bought. It renders in its own section, *Narrowed, and what survived*.
- `reserved` did not fail at all; it is unaffordable now, and a required
  `revive-when` line names the condition that changes that. It **is** closed, so
  nothing picks it up today, but its rendered reason is the revival condition
  rather than a refutation it never suffered. A reserved approach with no
  condition can never be revived, so the renderer says so in those words.

Each stance's field is required by the reader, not by the prompt: a missing one
is a fault naming the file and the line to add. A stance that records a result
is worthless as a bare flag, which is what makes these two controls rather than
vocabulary.

`derived/BACKWARD.md` (`backward.rs`) is the other axis: not what the run has
tried, but what would be *enough*. An approach is a route to the goal; a
skeleton is the goal decomposed into propositions that can each be attacked
alone. Without one, an investigation can verify data for twelve hours having
never written down what a proof would consist of, which is the failure this
ledger exists to make visible. A skeleton is
`research/backward/<slug>.md` carrying one fenced `skeleton` block — `goal`,
`implies`, `status`, `rests-on`, `killed-by`, with stances `sketched`, `live`,
`discharged`, `broken`, `spent` — and one fenced `gap` block per missing lemma:
`id`, `lemma`, `status`, `discharged-by`, `thread`, `next`. Two block kinds
rather than a `gaps:` list because a gap needs an identity that survives a
rewrite; a list cannot carry per-gap status or say which claim closed which
lemma. `implies` is load-bearing: three attractive lemmas that do not recombine
into the goal is what a decomposition gets wrong, and a file that never stated
the inference cannot be checked for it. Unlike the approach ledger this one is
re-derived on a *note* write as well as its own, because a gap is discharged by
a claim — so the same note that adds or removes one can close a gap or strand
it. `discharged` is deliberately not a closed stance: it is the one terminal
state that is a result.

`derived/WEAKENED.md` (`weakened.rs`) is the third axis and the only one that
moves the target. An approach is a route to the goal and a skeleton is the goal
decomposed; a ladder is the goal made *smaller*. A ladder is
`research/weakened/<slug>.md` carrying one fenced `ladder` block — `goal`,
`difficulties`, `status`, with stances `open`, `exhausted`, `abandoned` — and one
fenced `rung` block per weakened target: `id`, `statement`, `off`, `stance`,
`merge`. `difficulties` is load-bearing the way `implies` is: every `off` entry
must name a difficulty the header declared, and a rung switching off something
the ladder never named is reported as a fault rather than guessed at, because it
means the two disagree about what the problem's difficulties actually are. Rungs
render weakest-first, since that is the order they are meant to be climbed, and
the table names the *current* rung — the weakest one still open — because that is
the single fact the next attempt needs. A rung that was attacked and failed keeps
its row and its reason: deleting it is how the same one is proposed again three
attempts later. Like the skeleton ledger it is re-derived on a note write as well
as its own, because a claim can settle a rung, and a ladder still pointing at a
rung the run has already proved is how the next attempt spends itself re-proving
it.

`code/search/<slug>/SEARCH.md` (`search.rs`) is the odd one out: it is derived
like the rest, but from a score ledger rather than from notes, and it lives
under `code/` because what it ranks is programs. A search holds `PROBLEM.md`,
the scorer `score.py`, `candidates/` and the append-only `scores.jsonl` the
board is derived from. Two rules about it are worth stating here. Nothing may
put an `INDEX.md` anywhere under `code/search/` — `index_allowed` refuses it —
because the board already carries the only fact anyone wants about a candidate,
which is what it scored, and a search runs hundreds of them against a role twice
measured spending 60% of a run's model calls on filing. And the board lists the
discard *reasons with counts* rather than the discarded programs: a search whose
rejections are all "did not finish in time" has a scorer too slow to search
with, and one whose rejections are all the same constraint has found the
constraint that actually binds. Neither is visible from a list of winners.

`derived/FRONTIER.md` (`frontier.rs`) is the citation graph the converter used
to throw away. `readable.rs` has always parsed every anchor into a reference
table and kept nothing; a converted PDF yields nothing at all, though a
mathematical paper's reference list is exactly where the primary literature on
its subject is named — as arXiv identifiers and DOIs, which are now read too.
Ranking is mechanical and costs no model call: in-degree first, then how well
the citing sentence overlaps `GOAL.md`. In-degree is the signal no search can
provide — a URL three of the library's own sources cite is the standard
reference for the subject, and rephrasing a query will not surface that. The citing
*sentence* is stored with each row, because it says why the source thought the
target mattered — the difference between a reading list and a list of URLs. It
doubles as the fetch ledger: a second download of a URL already in the library is
refused with the path of the file holding it. One live workspace holds two notes
derived from the same arXiv abstract for want of that check.

`derived/REQUESTS.md` (`requests.rs`) is the demand side. Gathering was
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

`derived/BLUEPRINT.md` (`blueprint.rs`) is the only one that adds no new file
for an agent to write. It is the *graph* the other two already imply: a skeleton
names the gaps it needs and the claims it rests on, and a gap is discharged by a
claim or by another skeleton proving it outright. Read one file at a time those
edges are invisible, and three things go with them.

The first is what Massot's blueprint bought the Polynomial Freiman–Ruzsa
formalisation. A node whose dependencies are all settled can be worked on by
somebody who has not read the rest of the argument, which is how roughly
twenty-five contributors formalised PFR in three weeks with the author writing
about five per cent of the Lean. The detached sub-agents here are already
concurrent; what was missing was any way to say which lemma is safe to hand one.
The **ready** section is that list, and it is the file's reason to exist.

The second is circularity. Nothing noticed when skeleton `A` needed a lemma that
skeleton `B` proved from `A` — as two files it reads as two sound reductions, and
as edges it is a cycle that proves nothing. A flat ledger cannot detect this in
principle, because the fault is in no single row. It is reported above everything
else, since a cycle means every standing below it was computed from itself.

The third is **blocked** against **ready**, which the open-gap list flattens.
Every unproved lemma looks equally attackable there and most are not. A standing
is the minimum over what a node rests on, so a refuted lemma reaches the goal
above it and a kernel-checked one does too — which is what makes `lean_check`
worth anything to a planning role rather than only to the file it ran on.

`derived/ENTAILMENT.md` (`closure.rs`) reasons over the claims rather than
listing them. A `claim` block may carry `follows-from: a, b`, meaning `a` and `b`
together give it, and that one edge — closed transitively — answers three
questions the claim ledger cannot.

A claim whose whole support is established **is** established, whatever word its
own block carries. Nothing noticed, and the failure is the expensive direction: a
run spends an attempt proving a lemma its own library already hands it. The scale
of what that leaves on the floor is the Equational Theories Project's
measurement — 597,582 facts closed into answers for all 22,028,942 implications,
about a thirty-sevenfold return. Most of what a library knows is not what it
says, which is also why the closure is a fixed point rather than one pass: stop
at one hop and every sound step above the first is discarded.

A statement the library already entails is not a result, however true it is.
That is Fajtlowicz's Dalmatian heuristic under its own name — Graffiti's hard
problem was never generating conjectures but filtering the uninformative ones,
and more than half of that program was the filter rather than the generator.

And a contradiction can be real while no single block states it: `a` gives `c`,
`c` contradicts `b`, and the run holds both `a` and `b`. Following the edges is
the only way to reach it, and it is reported first for the same reason the cycle
is.

Two readings are refused in the strict direction, both because the permissive
one would be worse than having no closure at all. `asserted`, `heuristic` and
`catalogued` never propagate — a chain of guesses would otherwise manufacture an
establishment out of nothing, each step looking sound. And a claim that supports
itself transitively settles nothing and is excluded from every other section,
because two claims each said to follow from the other would otherwise bootstrap
each other into an establishment neither has.

Both reasoned ledgers can be re-derived on the host, over any workspace,
without a container or an API key:

```sh
cargo run --example derive_ledgers -- workspace/conjectures/singmaster
```

It prints both files and both briefings. That is how a change to either
derivation is checked against a workspace a live run produced rather than only
against a fixture, and it is how the stale dependency in `singmaster`'s
`boundary-finite-collisions` skeleton was found — the header still says
`sketched` while a lemma under it is `refuted`.

## The order a work queue renders in

`TASKS.md` rendered in first-seen order, and a section's blurb told the reader
what to do with that: *"In order. Work the first one you can."* Which is correct
only if the first row is still the most important one — and nothing kept it so.

A human directive reached a live conjecture run. The `director` turned it into
task rows correctly, and then reported what it could not do:

> The task ledger renders by first-recorded order, so
> `gsplit-exhaustive-line-test` still appears first in the literal `TASKS.md`
> list; I could not reorder it with the sanctioned ledger tools, and I judged
> hand-editing `config/tasks.jsonl` too risky.

Every part of that is the runtime working as built. The queue is append-only and
the file is derived, so hand-editing either is the thing the write guard exists
to refuse — the director was right to refuse it too. The fold ordered by first
event because that is the order a reader expects a list to keep. And the
consequence was that the newest and most urgent row landed at the *bottom* of
the section every role is told to work from the top of, with no tool anywhere
able to move it.

So a section now declares its `order`, and the two work queues — `Do next` and
`Blocked` — declare `recent`.

**Most-recently-touched, not most-recently-created.** The distinction is the
whole design. `record_entry` merges into an existing id, so ordering by the line
number of an entry's *last* event means a role raises an old task by recording
against it, with a tool it already holds and no new authority. Newest-created
would have fixed the arriving directive's task and permanently buried the
year-old row that is still the most important thing on the ledger — the same
failure in the other direction.

The two archives stay in recorded order, and that is not an oversight. `Do not
do` and `Recently done` are read *for what is on them* — "have I already ruled
this out" — rather than worked from the top, and a list that reshuffles is a
list nobody can scan twice.

Three properties keep this from becoming another thing to get wrong:

- **`recorded` is the default**, so every ledger that declares nothing renders
  exactly as it did. The change is two sections of one built-in.
- **`order` is a closed set of two, parsed on the way in.** An unrecognised one
  is a spec fault, not a silent fallback — the opposite reading from an unknown
  `check`, and deliberately: a dropped check costs one unreported fault, while a
  dropped order renders a section in an order nobody asked for and nothing says
  so. `read_ledger`'s `sort` takes the same two names and, like `ledger`, is a
  checked string rather than an enum, because the tool schema vec is built once
  per run; an unknown value comes back with the real ones.
- **Ordering happens at the render, never in the fold.** `collect` still returns
  first-seen order and every reader takes its own view, so nothing that reads
  entries had its meaning changed underneath it. An `items` ledger has no queue
  and therefore no touch order, and keeps recorded order under either name —
  file modification time is *not* the stand-in, because the run rewrites those
  files for reasons unrelated to priority (a one-field merge, a checkpoint
  restore, a checkout), which would shuffle the section on events no reader can
  see.

The bounds are untouched. Ordering decides which rows a section shows first, not
how many it shows or how much prose each carries, and `ledger/ceiling_test.rs`
holds both of those where they were.

## The attempts ledger

`spawn_candidates` puts several candidate solutions on their own git branches at
once (see [`workspace.md`](workspace.md#candidate-branches)). Git answers half
the question that raises — the branches are on disk and `attempt_diff` reads
them — and cannot answer the other half, because **the reason a candidate lost
is not in its diff**. Without somewhere to put it the next round re-proposes a
dead candidate, which is the failure `TASKS.md` had and the same fix.

It is a declaration rather than a module: `source: queue`, backed by
`config/attempts.jsonl`, rendered to `derived/ATTEMPTS.md`. A queue for the
reason the board is one — several candidates finish at once and each records
itself, so one `write_all` of one whole line needs no lock, and the events fold,
so a candidate that is proposed, then scored, then adopted is three events and
one row.

Two decisions in it are worth keeping:

- **`score` is a field, not a status.** The number is the scorer's and the ledger
  has no opinion about it; the *decision* is the status. Keeping them apart is
  what lets a candidate be the highest scoring one and still be rejected, with
  the reason saying why — exactly the case a search over programs produces.
- **Two prose fields, and no more.** The engine gives every prose field its own
  bounded line on every rendered row, so a field costs `REASON_CHARS` times the
  row cap whether or not anybody fills it in. A first draft carried `branch` and
  `approach` as well and rendered 76 KB on the ceiling fixture; `branch` is
  determined by the id and `approach` said again what the headline says.

The sections are capped well below the engine's default of forty, because this
ledger is read at the top of every round rather than opened once — its cost is
paid over and over, and a round explores at most ten candidates.

The `searcher` is deliberately not a writer. It holds no write tool at all (see
[`roles.md`](roles.md)), and a role that could record its own candidate's verdict
is one that can grade its own homework.

## The reduction ledger: what the run is driving the problem down to

`backward` answers *what would be enough* and answers it with a decomposition —
lemmas that recombine into the goal. That is one kind of reduction, and the
ledger's own output shows it is the only kind this runtime could express. Every
skeleton a live casas-alvero run produced is a restatement of a published
equivalence: `G-resultant-scheme` is Schaub–Spivakovsky's resultant
reformulation, `G-macaulay-rank` is Macaulay 1916, `G-good-prime` is the
degree-20 case of the lift theorem. Real work, and not the other kind:

> Normalise the failure until two real numbers describe it. Show the obstruction
> forces `1 + λ ≤ (m+1)·E_m(λ)`. Prove the strict reverse. Collide them.

That is the whole architecture of the ProofAtlas Sendov proof
([`../research/proofatlas/01-sendov-bundle-anatomy.md`](../research/proofatlas/01-sendov-bundle-anatomy.md)),
and before `reductions` existed no role could state it as a goal, so no role
pursued it and nothing recorded a run getting closer to one.

`source: queue`, backed by `config/reductions.jsonl`, rendered to
`derived/REDUCTIONS.md`. Three decisions in it:

- **`parameter` is required.** Naming what the problem is being collapsed onto,
  and how it is defined from the problem's data, is the hard part and the part a
  row is worthless without. `λ = m(1−a)` is a target; "a size parameter" is a
  mood.
- **`lower` and `upper` are separate fields**, because they are separately
  provable and usually proved by different arms — the obstruction forces one, an
  estimate plus a certificate forces the other. A run holding one of them is
  halfway rather than nowhere, and a single `gap` field could not say which half.
- **`identity` is a status, and it is the one that makes this a bank.** A
  reduction is a chain whose middle links are algebraic identities with no
  consequence yet: an integration by parts, a cleared factorisation, a
  coefficient bridge. None is a claim, none earns a verdict, and under every
  other ledger here a turn that produced one filed *nothing* — so the loop
  scored it as a pass with no progress and the restart cap ate the chain before
  it closed. A link recorded against its target is progress the next attempt
  reads.

The `inventor` is deliberately not a writer. It proposes *routes*, and a route
recorded as a reduction target is a wish with a parameter in it.

## The thesis ledger: the one thing that crosses runs

Every other ledger records what the run *did*. None recorded what it believed,
and that is the gap a long investigation turns on. The Sendov development had a
human holding one argument steady across months and many dead ends — the
disclosure calls it selecting and reconciling outputs — while the model explored
under it. This runtime had no such holder: `archivist` adopts a candidate,
`inventor` proposes a route, and neither carries an argument from one run into
the next.

It persists for free, which is the point: a workspace's `config/` is committed
and a run continues one rather than starting it, so a thesis written in run one
is in front of run nine with no mechanism at all. What the ledger adds is a shape
that can be **revised** rather than accumulated.

- **`refuted-by` is required before the row opens.** A belief with no stated way
  to lose is not a thesis, it is a mood, and it survives every round that should
  have killed it while spending the run's whole budget.
- **Capped at three live rows.** Two live theses is a run hedging; four is a run
  with none.
- **Four writers, not twenty.** A thesis every role may rewrite is one nobody
  holds, which is the failure it exists to fix. The two planners set it,
  `reflection` revises it against what a round actually produced — the only
  moment in the loop where a round's evidence meets what the run believed before
  it — and the `archivist`, already the role that decides what the trunk
  believes, settles it.

## A ledger a run can declare

Nine of these are Rust modules, and eight of the nine should stay that way:
`closure` computes a transitive closure to a fixed point, `blueprint` detects
cycles across files, `claims` reconciles a `formalised` status against kernel
verdicts on disk. None of that is expressible as configuration and none of it
should be.

But a *module* is something only a release can add, and the run is the thing
that discovers it needs an axis. The `research/folds/` folder above is the
evidence: a live workspace built the topic axis by hand, badly, out of files
nobody designed, and `threads` was written months later in response. That will
happen again.

So a ledger is also a **declaration** — `ledger/spec.rs` — and the engine
renders a declared one and a built-in one the same way. A spec names its source
(`queue`, an append-only jsonl; or `items`, one file per entry with a fenced
block), its fields and what each is for, its statuses and which of them close an
entry, and the sections its file renders. The static set a run starts with is
`tasks`, `goals` — the sub-goal decomposition under `research/backward/` — and
the board, plus the nine registered so `list_ledgers` and `read_ledger` reach
every ledger rather than eight of twelve.

Six tools serve all of them, and the count does not grow when a ledger is added.
That is forced rather than chosen: the tool schema vec is built **once per run**
(`agent_loop::run_loop`, with a regression test keeping it that way), so a
ledger declared mid-run can get no tool of its own and can appear in no `enum`
in anybody's schema. `ledger` is therefore a plain string checked against the
registry at call time, and an unknown slug returns the list of real ones — which
is the discovery path a model actually follows, in one turn, without having
thought to call `list_ledgers` first.

Four rules keep a declaration from undoing what the rest of this file argues
for, and all four are code:

- **It cannot raise a bound.** A section's `cap` is clamped against
  `ledger::budget` when the spec is read. A ledger that could declare its own
  bound would be a second route back to the 86 KB file.
- **It cannot reach a system prompt.** Prompts are assembled once at container
  start, so a mid-run ledger could not reach one even if the engine tried.
  Nothing tries; the way in is `list_ledgers` then `read_ledger`.
- **It cannot shadow a built-in or claim a built-in's derived path.** Every
  prompt naming `tasks` is written against what `tasks` holds, and two writers
  on one derived file is how each one's work disappears.
- **It cannot reason.** The checks are a closed set — a required field, a known
  status, a close with no reason — not an expression language.

A declaration also carries **how that ledger is actually written**, and that is
load-bearing rather than documentation. The write guard refuses an edit to a
derived file and has to say what to do instead — and the answer is not the same
for every ledger. A `queue` or `items` ledger takes `record_entry`; a
runtime-rendered one does not.

A live run found this the expensive way. The librarian tried to write
`teams/BOARD.md`; the guard correctly refused and told it to use `record_entry`
with `ledger: "board"` — which the board also refuses, because it is rendered by
its own module and written with `post_board`, a tool the librarian does not even
hold. One wasted call that time, because the role did not retry; a role that
believed the message would have spent two and learned nothing. A refusal naming
the wrong remedy is barely better than one naming none.

The guard now reads the route off the spec, and a test asserts the two agree:
an engine-written ledger must name `record_entry`, and a runtime-rendered one
must not. Reintroducing the board's old message fails it by name. That gap was
invisible to the original tests, which checked that the guard *refuses* and
never that what it *recommends* can be followed — the kind of thing only a live
run surfaces.

Write authority is the *spec's*, not the grant's, and it has to be: the set of
ledgers is not fixed when the tools are registered. Holding `record_entry` is
not permission to write every ledger. The acting role is baked into the tool at
construction, never an argument, on `post_board`'s reasoning — which is also why
five new tools arrived with a brief and a test asserting every role that may
write one is told how. `post_board` was granted to three roles, mentioned in no
prompt, and called **zero** times in a live three-school hour.

`search_claims` and `request_research` travel with the document tools, for the
same reason the index tools do: whichever role is working is the one that needs
to know what the run establishes, or that walks into a gap.
