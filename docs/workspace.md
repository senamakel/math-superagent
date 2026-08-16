# The workspace: layout, library, and what is derived from it

Everything under `/workspace` — where a file goes, what the research tree means, which files are written by code rather than by an agent, and how the whole thing is checkpointed. The working agreement is [`AGENTS.md`](../AGENTS.md); this file is the part of it that goes deeper than a rule.

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
| candidate reformulations | `research/approaches/` |
| proof skeletons and their open gaps | `research/backward/` |
| reflections | `reflections/L0.<n>/` |
| what other programs import | `code/lib/<subject>.py` |
| programs attacking one question | `code/<question>/` |
| the ledgers this runtime renders | `derived/` |
| one candidate solution's own checkout | `attempts/<id>/` |
| plumbing: `config.toml`, `problem.url`, `trace.jsonl`, the document index, the frontier and request ledgers | `config/` |
| operator direction: the queue, its cursor, and the receipt | `config/` |
| untouched download bytes | `raw/` |
| one school's own working files | `teams/<slug>/` |
| what the schools tell each other | `teams/board.jsonl`, derived into `teams/BOARD.md` |

`layout::placed` decides this in the write path — `write_document` and an
`apply_patch` `*** Add File:` — for the same reason `documents::research_path`
enforces `research/`: a prompt asking for tidiness holds only until a model is
busy. One live run reached thirty-one Python programs, four JSON tables, and a
scatter of `.out.txt` captures at its root, so the listing every agent reads was
mostly noise and the two files carrying the derivation were buried in it.

A path that already names a folder is left alone: naming one is a decision, and
the layout has no better information than the caller that made it. A move is
reported in the tool result rather than performed silently, because a model not
told where its file went writes the next one to the same place and then cannot
read either back.

`code/` carries its own `AGENTS.md` — one job per file, name for what it
computes, state the complexity before running, keep the naive oracle, never
delete a program carrying a result — so the rules travel with the folder. Its
`INDEX.md` says what established each program is correct, the part that is not
readable from the source.

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

`code/lib/` holds what other programs import, one subject per module; every other
program is grouped by the question it attacks, one folder per question, each with
its own `INDEX.md`, and what those programs produced under `code/out/`.
`layout::placed` deliberately does not decide which question a program belongs
to. That is a judgement about the mathematics, and a rule guessing at it would
file by extension, sorting a folder by the one fact nobody cares about. So the
default sink stays `code/`, a caller that names a folder is trusted, and whether
the sink has grown into a pile is measured after the fact.

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
The folder was renamed `lib/` for that reason — `toolkits` reads as somewhere to
put tools, where `lib/` reads as things other files import. Asking an organizer
to notice a routine typed out three times would cost it a read of every program
in `code/`, most of what a cycle costs; it is a count rather than a judgement, so
it is counted.

Every write path enforces it: `write_document`, an `apply_patch` addition, and
`write_tool_file`. That last one was the hole — it wrote wherever it was asked,
so `write_tool_file` with `path: "brute.py"` put a program at the root while
every other path was guarded. A live run did it within four minutes of starting
and left two different `brute.py` files, one filed and one loose, with nothing
to say which was current.

What the write path cannot catch is a shell redirect or a heredoc:
`cat > solve.py <<'EOF'` and `python solve.py > out.txt` reach the filesystem
directly, and the tool sees only a command and an exit code. Asking the organizer
to sweep was not enough — one live workspace collected six root programs in
nineteen minutes, written entirely through the shell while its organizer ran. So
`layout::sweep` runs at the end of every `execute_command`, where the files
appear, and the organizer's sweep is the backstop rather than the defence.

Three rules keep a sweep that frequent safe. A destination that already exists
is left alone, because a file carrying a result must never be overwritten by
one that shares its name — but the collision is *reported*, because silence
leaves the stray at the root for the rest of the run with nothing to say which
of the two files is current. A failure to move anything is silent, because the
command succeeded and tidying must not turn that into an error. And every move
is named in the tool result, for the same reason `layout::note` exists: an
agent not told where its file went runs `python solve.py` again and cannot
find it.

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
reference page converted to 91,190 characters, about 23,000 tokens, and three of
those fill a specialist's context before it has done any work — so reading the
short one is the default and reading the long one is a decision, which is what
the split buys. Both stay in `research/`: a source whose detail is genuinely
needed must be reachable without leaving the workspace.

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
file the result came out of. `describe_file` records a purpose; `refresh_index` re-derives the file list from
disk, keeps existing descriptions, marks new files undescribed, and drops rows
for files that are gone. Descriptions are left to explicit tool calls because
only the agent that wrote a file knows why; agreement between index and directory
is not, so a forgotten description shows as a visible gap rather than as an index
that quietly disagrees with its folder.

Links are compressed. Anchors become reference-style `[text][n]` with one
`## Links` list at the end, so a URL repeated a dozen times on a page is
written once; tracking parameters (`utm_*`, `fbclid`, and similar) are stripped.
A reference page's navigation targets otherwise fill the context with URLs the
agent will never follow.

The PDF extractor runs inside `catch_unwind` because it panics on malformed
input, and a panic there would destroy work unrelated to the document.

## Research folder

Every downloaded document is filed under `research/`, enforced by
`documents::research_path` rather than requested in a prompt. Downloads are the
one kind of file that arrives from outside the run, and separating them from the
run's own derivations is what lets an agent tell at a glance what it gathered
from what it worked out.

`research/` and `reflections/` are summary trees, not flat folders (`src/orchestrator/context_tree.rs`):

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
came to 1,417 bytes against 7,800 bytes of notes, and what survived was one line
per source. That is a catalogue, and `INDEX.md` already is one. A seal is what a
reader opens *instead of* the ten notes below it, so it carries every distinct
result with its hypotheses, not their titles. Sealing once is the point: a flat
level is re-summarised whenever anything is added, so the same sources are
re-compressed indefinitely and the summary drifts.

`CONTEXT.md` is a root in its own right, and it is the one with a budget of its
own: `MATH_AGENT_CONTEXT_TOKENS`, ten thousand by default. It used to sit under
the thousand-token cap with the tree roots, and that was the wrong size for what
it is. A thousand tokens buys a list of what the library established, which is
close to what `research/INDEX.md` already says. Ten thousand buys the thing an
agent otherwise spends a quarter of an hour rebuilding from disk: what the run
believes and on what basis, which approaches are dead and why, what the computed
numbers look like, what durable memory relates the problem to. That is worth
re-sending on every model call; a catalogue is not. The budget is read by
`shared_context::budget_tokens`, measured against the file by
`shared_context::standing`, and enforced where it is *spent* —
`load_workspace_files` cuts a brief that exceeds it on the way into a prompt and
says in the file's place that it was cut. Enforcing it in the write path was the
alternative and is worse: refusing a write costs the run whatever the agent was
about to record, where cutting the prompt copy keeps the material and turns the
overrun into the curator's next cycle.

`ROOT.md` is deliberately not `INDEX.md`. The index says what each file *is* and
is derived from the directory by the index tools; the root says what the library
*means* and is written by an agent. Holding both in one file put a tool and an
agent in contention and cost three rounds of lost descriptions — a refresh
overwriting a synthesis, then a synthesis overwriting rows, then rows rewritten
in a spelling the refresh could not match.

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

`context_tree::plan` measures this on disk and reports one fault at a time — over
budget, then waiting to be sealed, then sealed without its links, then behind
what it covers — and `briefing` renders the highest-priority one into the
research team's next cycle. It writes nothing: a fold is a judgement about
meaning, so an agent writes it; whether a node is within budget and reflects what
is under it is not, so it is measured. Structure is recovered from the links
themselves rather than a manifest, because a fold that has stopped linking a note
has stopped covering it — exactly the fact a manifest would hide.

`documents::research_path` and the reflection log both file into the *open*
batch, which `context_tree::open_batch` derives from disk: the highest-numbered
batch still under the fan-out, or the next one when it is full. No writer needs
to know the tree's history.

The librarian receives the root as context so it does not download the same
paper twice. Toolkits keep the older flat shape: a folder, an `INDEX.md`, and
one small file per helper.

## The derived ledgers

Nine files beside the library are written by code, never by an agent, and
re-derived from disk on every relevant write. What each one holds, and the
failure each was written to stop, is in [`ledgers.md`](ledgers.md).

## Candidate branches

A workspace has its own git repository in `.workspace-history` — a separate git
directory with an explicit work tree, so the product repository sees ordinary
files rather than an embedded repo. The trunk of an investigation is the branch
`work`, and `WorkspaceCheckpoint` commits to it after every successful write.

`spawn_candidates` puts several candidate solutions on that repository at once.
Each gets a branch `attempt/<id>` and a **linked worktree** checked out at
`attempts/<id>`, and a role whose file tools are rooted there. So five
candidates all write `code/solution.py` and all write a different file, and each
commits to its own branch: a candidate's work never reaches `work` by accident,
and `attempts/` is in the trunk's exclude list so the trunk never commits their
trees as ordinary files.

What forks and what does not is the point of the design:

- **Forked** — everything in the workspace tree. `code/`, `research/`, the
  ledgers. A candidate recording a task records it in its own file.
- **Shared** — memory. Cognee and Qdrant live outside the mount entirely, on a
  network shared per problem, so `remember_memory` and `recall_memory` are not
  re-rooted and must not be. Candidates must not overwrite each other's files
  and *should* see what each other established; that is the whole trade.

The slots are fixed (`candidates::SLOTS`) because a subagent's harness is
registered once at container start with its tools already rooted, so the
directories have to be chosen up front. A slot is reused once its candidate is
decided, which is what `abandon_attempt` frees — it removes the checkout and
keeps the branch, so the work stays readable through `attempt_diff` afterwards.

Reading and keeping are separate authorities. `list_attempts`, `attempt_diff`
and `attempt_log` go to any role that reviews; `adopt_attempt` and
`abandon_attempt` are the archivist's alone. Adoption copies *named paths* out
of a branch and commits them with the reason — deliberately not a merge, which
would also bring the losing candidate's own notes and its account of why it was
right into the trunk, where the next attempt reads them as the trunk's own.

There is no general git tool and there must not be: every operation is a named
verb with checked arguments, and one taking a command line would be
`execute_command` reachable by roles that were deliberately denied a shell.

## The scratch

`SCRATCHPAD.md` was the third store and the only one still a file, and the wrong
shape for what it held. Being in `role_context` meant every model call in every
role holding it paid for every number anyone had jotted down, and appending a
line meant reading the file whole. `note_scratch` and `recall_scratch`
(`vector.rs`) make it the same trade `remember_memory` and `recall_memory`
already make: written once, read back by wording.

It is a third store rather than a flag on the durable one, and the separation is
the point. `visible_datasets` excludes `math_agent_scratch__*` outright and
`durable_node_sets` omits `scratch:<project>`, the second being the one the
server honours, so neither `recall_memory` nor `relate_memory` can return
provisional work: a half-finished calculation cannot come back looking like
something the run established, which is the distinction the method policy
rests on. It is also not the knowledge graph: `relate_memory` answers what the
run's entities are connected to, and no amount of traversal recovers what a
solve was in the middle of.

Access is a tool boundary rather than a routing decision, since the file is
gone. `register_scratch` grants both halves to the roles that do provisional
work — the seven code writers, `pattern_finder`, and `goals` — the read half
alone to the scholar and the context curator, which judge provisional work
without producing any, and neither to reflection or the judge, for exactly the
reason the file was withheld from them: unsettled arithmetic read as progress is
what keeps a loop retrying. A test asserts that split.

The dataset is scoped to the project, not the run, for the reason recorded on the
session dataset: `./euler 763` continues from what is on disk, and a scratch that
vanished on restart would be worse than the file it replaces. Ingest is
backgrounded: a note is written mid-derivation, and waiting on an index would put
the memory on the critical path of the arithmetic it describes — the one thing a
file did not do.

## Workspace discovery and the reflection log

`list_workspace` renders a bounded tree with file sizes. Agents previously knew
only the file names their prompt happened to mention, so work already on disk
went unread; sizes matter because they distinguish a finished derivation from
an empty placeholder. The listing hides `.workspace-history`,
`.python-packages`, `__pycache__`, the document index, the frontier ledger, and
`trace.jsonl`, and truncates rather than dumping an unbounded tree.

Every reflection is archived to `reflections/L0.<n>/<epoch_ms>_<outcome>.md`,
where the outcome is `nothing` or `<n>_learnings` — so a directory listing
alone shows which attempts taught the run something — and indexed in
`reflections/INDEX.md` in the same step. The folder carries an index for the
same reason `research/` and `code/lib/` do: a directory of epoch-stamped
filenames says when each attempt was judged and nothing about what any of them
found. Each row records the attempt number, the verdict, and the lesson, so the
planners and the inventor can see which attempt is worth continuing without
opening any of them. The loop writes both the file and the row — no agent is in
that path — which is why `refresh_index` and `describe_file` refuse the folder
outright (`folder_index::loop_owned`): a hand refresh would replace verdicts and
lessons with `_(undescribed)_`. The organizer's prompt said to leave it alone and
a live organizer refreshed it anyway, the usual lesson — a prompt instruction is
not a control. Writing the log is best effort: the lesson is already in the loop
state, and losing the archive copy must not cost the run the lesson.

## Reading what does not fit

`read_document` returned whole files, and for most of a workspace that is
right: a belief, a thread, an approach note is a few kilobytes and reading it
is one call. The library is the exception, and by the time it was measured it
was not a small one. The Gilbreath workspace holds **404 Markdown files
totalling 4.7 MB, of which 37 files hold 60% of the bytes.** The largest is
`research/sources/martin-annotated-bibliography-comparative-prime-number-theory.full.md`
at 427,889 bytes — about 107,000 tokens, more than a third of the 300,000-token
compression trigger, from one call.

A role facing that file had two options and both are bad: spend a third of its
window on one source, or never open it. The rule that was supposed to prevent
this is rule 13 of the shared method policy — *"open its `.full.md` companion
only when the summary does not answer the question, because the full text is
large enough to crowd out the work"* — which is a prompt instruction, and this
repository's own maxim says what that is worth. The same shape had already cost
a live run a 339,652-token model call from `trace.jsonl`, which is why
`ensure_visible` refuses that file by name. A research source cannot be answered
that way: it is exactly what the run is supposed to read.

So reading is now two steps, and four tools serve them.

| Tool | Answers |
|---|---|
| `outline_document` | what is in this file, and at which lines |
| `read_document` with `section` or `lines` | that part of it, and nothing else |
| `grep_workspace` | which file, and where in it, across the whole tree |
| `map_document` | a question about the whole file, without the file |

**The ceiling is the control.** An unselected `read_document` over 24 KiB does
not return the document — it returns the outline and says how to select. Every
byte stays reachable, one named range at a time, and a selected read is bounded
in turn at 48 KiB, cut at a line, with the line to resume from printed at the
end. The 24 KiB threshold is set at the size of a long note rather than a short
paper, so everything the run writes about itself reads exactly as it did before
and only the library is affected.

The outline is **derived, never stored**. `folder_index` already carries the
judgement half of cataloguing — what a file is *for*, which only the agent that
wrote it knows — and that has to be maintained. What a file *contains* needs no
judgement, so it is recomputed on each read from bytes already in memory, and
cannot disagree with the file the way a stored table of contents would after
the next edit. It also works in `research/`, where `INDEX.md` is refused
because Cognee owns that catalogue.

`map_document` is the recursive read, and it is the one that changes what is
possible rather than what is cheap. The region is split into 24 KiB chunks;
each chunk is read by its own model call that sees that chunk and nothing else;
the short findings are merged by one more call. Only the merged answer reaches
the caller — a 428 KB bibliography costs it a few hundred tokens of cited
answer instead of 107,000 of source. Three properties are deliberate:

- **The chunk precedes the question in the prompt.** Providers cache on a
  prefix, so a run that interrogates one survey five ways re-sends a prefix it
  has already paid for and is charged the cached rate for the expensive half.
  Question-first would move the varying part to the front and lose every hit.
- **A chunk with nothing to say must say `NOTHING`.** The output is an answer
  with citations, not a summary of the source; contributing a weak match is
  worse than contributing none, because the merge cannot tell them apart.
- **A failed or unread chunk is named in the output.** Fifty-nine chunks that
  answered beat one failure that discards them, but an answer with a hole in it
  that does not say so will be read as complete.

### Switching the recursion off

The ceiling and the recursion are different kinds of thing, and only one of
them switches off. The ceiling is a **control**: it costs nothing, stops one
call spending a context window, and is in force on every run — an operator who
wants more raises `MATH_AGENT_READ_CEILING` rather than removing it. The
recursion is a **spend**: one `map_document` over a 428 KB source is eighteen
provider calls the caller did not individually authorise, and there are runs
where that is the wrong trade — a cheap model where eighteen chunk reads cost
more than the answer is worth, or a calibration run being measured on what the
harness does without them.

So `MATH_AGENT_RLM=off`, or `--no-rlm` on `./agent`, withholds it — by **not
registering the tool**, the same enforcement as `MATH_AGENT_RESEARCH` and for
the same reason. The registry stops advertising the name in the same breath, so
a delegating role is never told about a capability the harness does not have. A
run without it keeps the outline, the selected read and the search, so a large
document stays readable; what it loses is the ability to ask one question of a
whole file.

Every bound is an override on the same rule the rest of the runtime follows —
missing, empty, unparsable or zero keeps the default, so a mistyped number
gets the runtime's judgement rather than a silent zero that would turn a bound
into a refusal of everything. They live together in `orchestrator::reading`
rather than as constants in the two modules that use them, because an operator
asking "how much of a file can a role see" should not have to read both.

| Variable | Default | What it sets |
|---|---|---|
| `MATH_AGENT_RLM` | `on` | whether `map_document` exists at all |
| `MATH_AGENT_READ_CEILING` | 24576 | unselected read before the outline answers instead |
| `MATH_AGENT_READ_SLICE` | 49152 | one `section` or `lines` read; held at or above the ceiling |
| `MATH_AGENT_RLM_CHUNK_BYTES` | 24576 | source one chunk read sees |
| `MATH_AGENT_RLM_MAX_CHUNKS` | 60 | chunks one call reads before it stops and says so |
| `MATH_AGENT_RLM_CONCURRENCY` | 6 | chunk reads in flight |

The slice bound is held at or above the ceiling deliberately. An operator who
raises one and forgets the other would otherwise get a runtime where naming a
section returns *less* than not naming one, which reads as the selection having
gone wrong rather than as a misconfiguration.

Its reply is evidence, not a claim — the same standing as a search result, and
the tool says so on every call: read the cited lines before relying on it. The
reader model is wrapped in accounting at construction, so chunk reads appear in
`model_accounting` under `chunk_reader` and a run can see what interrogating a
survey cost it.

## The directive queue

Three files under `config/` carry human direction into a live run, and which
side writes each one is the whole design.

| File | Written by | Holds |
| --- | --- | --- |
| `directives.jsonl` | the host, append-only | one JSON object per directive: `at`, `from`, `text` |
| `.directives-cursor` | the runtime only | how many lines it has consumed |
| `DIRECTIVES.md` | the runtime only | each directive and what the run did about it |

Splitting the writers removes the race rather than managing it. Neither side
writes what the other writes, so neither needs a lock, and the one number they
share — how far through the file the run has got — belongs to the side that
advances it. The cursor is staged and renamed rather than written in place: a
half-written cursor reads as zero, redelivering every directive already acted on.

A directive's identifier is its line number, not a stored field. That is what
makes delivery exactly-once without a counter anyone could disagree about, and it
is why a line the reader cannot parse is skipped *and still counted* — a torn
append costs that one directive rather than the alignment of every later one. A
host append can interleave with the checkpoint commit below, so this is worth
surviving rather than a hypothetical.

Directive text is capped at 2000 characters, keeping a rendered line inside the
size an append lands in one piece. Anything longer is a document, and the run can
be pointed at it instead.

The queue is committed like everything else in the workspace. What an operator
asked for, and when, is part of how an answer was reached — a run that changed
direction three attempts in reads as inexplicable without it.

## The task ledger, and ledgers a run declares

`TASKS.md` was free-form Markdown that the goals agent and the director rewrote
whole. On one workspace that was forty-eight rewrites, 1,647 lines written to
reach a net 165 — and every rewrite silently dropped the finished rows, so
nothing on disk said what the run had done or why anything had been ruled out.
The agents noticed before the runtime did: that file grew a hand-maintained
`## Do not do` section, which is the loss being worked around by the roles
suffering from it.

It is derived now, from the directive queue's design applied to a third problem.

| File | Written by | Holds |
| --- | --- | --- |
| `config/tasks.jsonl` | any role that keeps tasks, append-only | one JSON event per change: `at`, `from`, `id`, `fields` |
| `TASKS.md` | the runtime only | the derived list every planner reads |
| `config/ledgers/<slug>.json` | `define_ledger` only | a ledger this run declared for itself |

There is **one write operation** and adding, closing, dropping and blocking are
all it: an event names an entry and carries some fields, the fold applies them
in order, and absent keys are left alone. Closing a task is
`{status: done, reason: …}`. A vocabulary of operations would mean a vocabulary
of inverses to get wrong — what `unblock` does to a task that was never blocked
— and a merge has none. Nothing is lost by not naming them, because the event
log keeps the whole history either way.

A derived path is refused to `write_document` and `edit_document`, naming the
tool to use instead. That is not tidiness: the file is rewritten from its source
on the next write to it, so an edit is not a change but work queued for
deletion, and the agent believes otherwise until it reads the file back. It is
the `ROOT.md` versus `INDEX.md` contention above, caught before it costs three
rounds instead of after.

**A run may declare its own.** This section of `docs/ledgers.md` records a live
workspace that grew an undesigned `research/folds/` folder — `game-core.md`,
`passes.md`, `counting-arithmetic.md`, `deadends.md` — because it needed a topic
axis the runtime did not have; `threads` was written in response, later, by a
human. `define_ledger` is that answer without a release. What keeps it safe is
in `ledgers.md`; the two rules that show up in the tree are that a declared
ledger may not shadow a built-in slug and may not write a derived path another
ledger owns.

Migrating a workspace that still has a hand-written `TASKS.md`:

```sh
cargo run --example import_tasks -- workspace/conjectures/gilbreath
cargo run --example import_tasks -- workspace/conjectures/gilbreath --write
```

Without `--write` it prints what it would record and touches nothing, which is
the only safe default for something that reads prose and guesses. It imports
checklist items and the `Do not do` bullets, and deliberately imports neither
`## Background` nor the thread summaries — those are not tasks, they belong in
`CONTEXT.md` and the ledgers that already carry them, and deciding where is a
judgement about the mathematics that a parser has no business making. The old
file is renamed rather than deleted, with everything it did not import still in
it.

## The teams tree

Two or three [schools](schools.md) work one problem in one workspace. What each
does privately is its own; what it establishes is everyone's.

| Path | Written by | Holds |
| --- | --- | --- |
| `teams/<slug>/` | that school only | its own derivation, notes and working files |
| `teams/board.jsonl` | any school, append-only | one JSON object per post: `at`, `from`, `kind`, `body`, `refers` |
| `teams/BOARD.md` | the runtime only | the derived board every school reads |

Everything under `research/` and `code/` stays shared, and sharing it is the
point rather than an economy: a verified helper in `code/lib/` is worth most to
the school that did not write it, and a claim is evidence whoever established
it. That is safe without coordination because none of the nine ledgers is
*edited* — each is derived by walking a one-file-per-item directory and
re-rendered whole, so two schools writing distinct notes never conflict on
content. They would conflict on the render, and `orchestrator::worklock`
serialises that.

The board is the directive queue's design applied to a second problem, for the
same reason: one append-only file that many writers append whole lines to, and a
derived file only the runtime writes. Concurrent posters interleave lines and
never halves of one, so no lock is needed and none is taken. A post is
**asserted, not established** — `BOARD.md` is never an input to a derived ledger,
and the posting school is baked into the tool at registration rather than being
an argument it could fill in, so no school can post as another.

What the board carries that the ledgers cannot is the thing that is not a claim
yet: a dead end with its reason attached, a hunch worth interrupting somebody
for. `docs/methods-gap-analysis.md` records the absence of exactly that as
deliberate, and it is right for a claim and wrong for a hunch — a route one
school has already killed should be paid for once.

## What is committed, and how often

Workspace contents are committed: the derivation, the program and the per-run
notes are the record of how an answer was reached, which is the point of the
product.

They belong in history, not in every commit. A live run writes into `workspace/`
continuously, so a host-side auto-commit hook firing on each tool call turns
that into commit spam. One measured hour produced 97 commits on `main`, 87 of
them touching nothing but `workspace/`, with model-written subjects that did not
always match their diffs — one read *"remove outdated project euler problem 763
files"* for a change that removed nothing and added five lines to a prompt.
`.claude/settings.json` therefore sets `AUTO_COMMIT_EVERY=25` for this
repository. Everything is still committed and nothing is excluded; it is
batched, and the fine-grained record is not lost either, because the runtime
keeps its own per-write checkpoint in `.workspace-history`.

What is ignored is what a reader would never open. `.python-packages/` holds pip
installs, which land in the workspace only because the container root filesystem
is read-only. `raw/` and the bulky enumeration pools sit beside the counts that
cite them. `trace.jsonl` and `console.log` run to several megabytes per run,
while the derivation and the notes already carry the reasoning worth keeping —
read the trace locally or in Langfuse instead. The hidden `config/.*.json` is
the runtime's own cache of the frontier, the request ledger and the document
index, rewritten on nearly every tool call, and each already has a committed
human-readable counterpart beside it — `research/FRONTIER.md`,
`research/REQUESTS.md` — which is what the derivation cites.

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

### What the history never records, and the 71.6 GB that proved it needed saying

That history has its own `info/exclude`, and it is a **separate git directory
from the product repository** — so the repository's `.gitignore`, which has
carried a carefully argued list since the enumeration pools were purged, never
applied to it. For a long time the two disagreed and nothing compared them.
`AGENTS.md` said `trace.jsonl`, `console.log`, the bulky pools and the hidden
`config/.*.json` state were ignored "because a reader would never open one"; the
exclude file listed four paths and none of those, while its comment claimed it
covered "the event log".

An audit of thirteen live conjecture workspaces measured the cost. Of ~86 GB,
**71.6 GB was `.workspace-history` and 47 MB was `research/`** — the reasoning
artifacts, which are what the product is for, were 0.05% of the tree. One
workspace had committed `config/trace.jsonl` **137 times at roughly 600 MB a
commit**, and its five largest blobs were five copies of that one file. A live
run appends to the trace continuously, so it is dirty at every checkpoint and
lands in every batch — the same argument already recorded against the hidden
JSON caches, which do have a rule.

`checkpoint::NEVER_COMMITTED` is now that list in one place, and two details
about how it is applied are load-bearing:

- **The exclude is rewritten on every start, not only at init.** A workspace
  outlives the build that made it, and every workspace on the box predates the
  constant. A write guarded by "the history directory is missing" would have
  left all of them excluding four paths forever.
- **A file already committed must also be untracked.** An ignore rule applies
  only to *untracked* paths, so adding the trace to the exclude changes nothing
  where it was already committed — which is everywhere. `untrack_excluded` runs
  `git rm --cached`, which stages the removal and **leaves the file on disk**:
  a live run is still appending to it and `./euler-tui --replay` still reads it.
  Without this the exclude file would read correctly while the history kept
  growing, which is the failure mode this whole section is about.

This stops the growth and does not reclaim what is already committed. Rewriting
a workspace's published history is out of scope by the same rule that forbids it
anywhere else: that history is the record of how an answer was reached.

When a workspace is first used, the helper copies the template into it without
replacing existing files. The runtime appends `AGENTS.md`, `config.toml`,
`MEMORY.md`, and the relevant role prompt to each agent's built-in system
policy. `GOAL.md` and `TASKS.md` are also loaded. Workspace context must never
replace built-in tool or container restrictions.

The tool-builder also gets `apply_patch` (`src/orchestrator/patch.rs`), which
applies a Codex-format envelope — `*** Begin Patch`, `*** Add File:` /
`*** Update File:` / `*** Delete File:` sections, `@@` hunks with ` `/`-`/`+`
line prefixes — across several files at once. Two deviations from upstream are
deliberate and should stay. Context matching is **exact**, and an ambiguous hunk
is refused rather than resolved: Codex falls back to fuzzy matching, which suits
an interactive tool with a human watching and not a run where a patch landing in
the wrong place yields a program that computes something else. Application is
**atomic**: every operation is resolved against the current files before a byte
is written, so a bad hunk in the third file cannot leave the first two rewritten.
A context line missing its leading space is read as context anyway — that reading
is unambiguous, and the most common way a small model malforms the envelope.

The format is borrowed rather than invented because a documented one the model
may already have seen beats a private dialect it has to learn from a schema.

Every runtime agent receives the workspace document tools: bounded download,
read, write, exact edit, index, and search. The index is
`/workspace/config/.document-index.json` and contains only relative paths in
the selected workspace. Keep the 5 MiB per-document limit and reject non-HTTP
downloads, traversal, symlink escapes, non-UTF-8 content, and missing
exact-edit targets. Do not move generated artifacts into source directories
unless the user asks to promote a specific artifact into the product.
