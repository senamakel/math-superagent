# The derived ledgers

Nine files beside the library are written by code, never by an agent, and
re-derived from disk on every relevant write. All nine follow the rule `INDEX.md`
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

`research/APPROACHES.md` was 86 KB of that, and the shape of the failure is the
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

`ledger_report` prints what each ledger costs on disk beside what the current
build would render, because those disagree until something writes to that ledger
— so a run started before a bound changed keeps paying the old price, and
reading only the on-disk column reports a fix as landed while every prompt still
carries the old file.

```sh
cargo run --example derive_ledgers -- workspace/conjectures/gilbreath
```

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

`research/THREADS.md` (`threads.rs`) is the topic axis. `L0`/`L1`/`L2` fold by
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

`research/APPROACHES.md` (`approaches.rs`) is what the run has tried to
*think* of, beside what it has tried to compute. A thread is already anchored
to the library, so nothing held the step before it: a candidate reformulation.
That went into one prose field on the solution state and was gone by the next
attempt, so an idea proposed at attempt three could be proposed again at
attempt six and the literature check that would have killed it never happened.
An approach is `research/approaches/<slug>.md` with a fenced `approach` block
— `idea`, `mechanism`, `status`, `precedent`, `first-step`, `killed-by` — whose
stances are a life cycle rather than a flag: `proposed`, `grounded`, `refuted`,
`adopted`, `spent`. Empty `precedent` means nobody checked, which is not the same
as nothing having been found; refuted and spent approaches are kept with their
reasons, on the dead-thread argument.

`research/BACKWARD.md` (`backward.rs`) is the other axis: not what the run has
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

`research/WEAKENED.md` (`weakened.rs`) is the third axis and the only one that
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

`research/FRONTIER.md` (`frontier.rs`) is the citation graph the converter used
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

`research/BLUEPRINT.md` (`blueprint.rs`) is the only one that adds no new file
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

`research/ENTAILMENT.md` (`closure.rs`) reasons over the claims rather than
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

`search_claims` and `request_research` travel with the document tools, for the
same reason the index tools do: whichever role is working is the one that needs
to know what the run establishes, or that walks into a gap.
