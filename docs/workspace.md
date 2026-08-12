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
| reflections | `reflections/L0.<n>/` |
| what other programs import | `code/lib/<subject>.py` |
| programs attacking one question | `code/<question>/` |
| plumbing: `config.toml`, `problem.url`, `trace.jsonl`, the document index, the frontier and request ledgers | `config/` |
| operator direction: the queue, its cursor, and the receipt | `config/` |
| untouched download bytes | `raw/` |

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
came to 1,417 bytes against 7,800 bytes of notes, and what survived was one
line per source. That is a catalogue, and `INDEX.md` already is one. A seal is
what a reader opens *instead of* the ten notes below it, so it carries every
distinct result with its hypotheses, not their titles. Sealing once is the point: a flat level
is re-summarised every time anything is added, so the same sources are
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

## The five derived ledgers

Five files beside the library are written by code, never by an agent, and
re-derived from disk on every relevant write. All five follow the rule `INDEX.md`
already established: what a source establishes is a judgement and stays with the
agent that made it; whether the summary agrees with the files is not, so it is
measured. Each is described through `record_description` when written, so no
derived file sits in `research/INDEX.md` as `_(undescribed)_` for a whole run.

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
seal it is live and rewritten as the direction changes. Dead threads are kept:
a known dead end is a result, and the reason is what stops the next attempt
paying for it again. A thread resting on a claim id that is not on disk is
reported, and so is a blocked thread with no blocker stated, because a blocker
stated precisely is the next research request and one left blank is a mood.

`research/APPROACHES.md` (`approaches.rs`) is what the run has tried to
*think* of, beside what it has tried to compute. A thread is already anchored
to the library, so nothing held the step before it: a candidate reformulation.
That went into one prose field on the solution state and was gone by the next
attempt, so an idea proposed at attempt three could be proposed again at
attempt six and the literature check that would have killed it never happened.
An approach is `research/approaches/<slug>.md` with a fenced `approach` block
— `idea`, `mechanism`, `status`, `precedent`, `first-step`, `killed-by` —
whose stances are a life cycle rather than a flag: `proposed`, `grounded`,
`refuted`, `adopted`, `spent`. Empty `precedent` means nobody checked, which
is not the same as nothing having been found; refuted and spent approaches are
kept with their reasons, on the dead-thread argument.

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
same reason the index tools do: whichever role is working is the one that needs
to know what the run establishes, or that walks into a gap.

## The scratch

`SCRATCHPAD.md` was the third store and the only one still a file, and it was
the wrong shape for what it held. Being in `role_context` meant every model call
in every role holding it paid for every number anyone had jotted down, whether
or not the turn was about them, and appending a line meant reading the file
whole. `note_scratch` and `recall_scratch` (`vector.rs`) make it the same trade
`remember_memory` and `recall_memory` already make: written once, read back by
wording.

It is a third store rather than a flag on the durable one, and the separation
is the point. `visible_datasets` excludes `math_agent_scratch__*` outright and
`durable_node_sets` omits `scratch:<project>`, the second being the one the
server actually honours, so neither `recall_memory` nor `relate_memory` can
return provisional work: a half-finished calculation cannot come back looking
like something the run established, which is the distinction the method policy
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

Every reflection is archived to `reflections/L0.<n>/<epoch_ms>_<outcome>.md`,
where the outcome is `nothing` or `<n>_learnings` — so a directory listing
alone shows which attempts taught the run something — and indexed in
`reflections/INDEX.md` in the same step. The folder carries an index for the
same reason `research/` and `code/lib/` do: a directory of epoch-stamped
filenames says when each attempt was judged and nothing about what any of them
found. Each row records the attempt number, the verdict, and the lesson, so
the planners and the inventor can see which attempt is worth continuing
without opening any of them. The loop writes both the file and the row itself
— no agent is in that path — which is why `refresh_index` and `describe_file`
refuse the folder outright (`folder_index::loop_owned`): a hand refresh would
replace verdicts and lessons with `_(undescribed)_`. The organizer's prompt
said to leave it alone and a live organizer refreshed it anyway, which is the
usual lesson — a prompt instruction is not a control. Writing the log is best
effort: the lesson is already in the loop state, and losing the archive copy
must not cost the run the lesson.

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
half-written cursor reads as zero, which would redeliver every directive the run
had already acted on.

A directive's identifier is its line number, not a stored field. That is what
makes delivery exactly-once without a counter anyone could disagree about, and
it is why a line the reader cannot parse is skipped *and still counted* — a torn
append costs that one directive rather than the alignment of every later one. A
host append can interleave with the checkpoint commit below, so this is a case
worth surviving rather than a hypothetical.

Directive text is capped at 2000 characters, which keeps a rendered line inside
the size an append lands in one piece. Anything longer is a document, and the
run can be pointed at it instead.

The queue is committed like everything else in the workspace. What an operator
asked for, and when, is part of how an answer was reached — a run that changed
direction three attempts in reads as inexplicable without it.

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

When a workspace is first used, the helper copies the template into it without
replacing existing files. The runtime appends `AGENTS.md`, `config.toml`,
`MEMORY.md`, and the relevant role prompt to each agent's built-in system
policy. `GOAL.md` and `TASKS.md` are also loaded. Workspace context must never
replace built-in tool or container restrictions.

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
`/workspace/config/.document-index.json` and contains only relative paths in
the selected workspace. Keep the 5 MiB per-document limit and reject non-HTTP
downloads, traversal, symlink escapes, non-UTF-8 content, and missing
exact-edit targets. Do not move generated artifacts into source directories
unless the user asks to promote a specific artifact into the product.
