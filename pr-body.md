Rebuilds how the runtime gathers, files, compresses, and retrieves research, so
an agent can load the right pieces into its context rather than the right files.

## The diagnosis

The unit of `research/` was a **file**, and the organizing axis was **arrival
order** — `L0.n` batches of ten, sealed by an `L1.n` note named for the batch.
That is right for provenance and wrong for retrieval: a reader asking "what do
we know about the pass rule" gets a seal covering whichever ten things arrived
together.

The strongest evidence is that workspace 882 invented the missing axis by hand.
It grew a `research/folds/` folder nobody designed, holding `game-core.md`,
`passes.md`, `counting-arithmetic.md`, and `deadends.md`. The same workspace
records four unrelated arXiv downloads in `misfiled.md`, and keeps
`raw_mfl_pass.md` beside the proper note for the same paper — collection had no
dedup and no acceptance test.

## What this changes

**Structural digest** (`digest.rs`). `research_excerpt` took the leading 4,000
characters. For a paper that is the title, the abstract, and half the
introduction — precisely the part the scholar prompt says to throw away
("compress by dropping what the source says about itself"). So the run paid a
thousand tokens for the wrong thousand tokens and still had to open the full
text to decide whether it was worth opening. The digest is the heading outline,
the abstract, and every paragraph opening `Theorem`, `Lemma`, `Definition`,
`Proposition`, `Corollary`, `Algorithm`, `Conjecture`, `Claim`, `Fact`, `Axiom`
— all mechanically locatable, and the payload of a mathematical source. `Proof`
is excluded: it is the argument for a statement already captured and the longest
block on the page. A source with no headings and no labelled statements falls
back to leading characters, because for that shape the leading characters
genuinely are the document.

**Citation frontier** (`readable.rs`, `frontier.rs`). `readable` has always
parsed every anchor into a `LinkTable` and then discarded it — a citation graph
thrown away at the moment of maximum information. Records now carry the URL, the
anchor text, and *the sentence the citation appeared in*, which is what says why
the source thought the target mattered. Converted PDFs get a bare-URL / `arXiv:`
/ `doi:` scanner, since a paper's reference list names the primary literature as
identifiers rather than anchors. Ranking in `research/FRONTIER.md` is mechanical
and costs no model call: in-degree first, then goal-term overlap in the citing
sentence. In-degree is the signal no search can provide — a URL three of the
library's own sources cite is the standard reference, and no rephrasing of a
query surfaces that. It doubles as the fetch ledger, so a second download of a
URL already held is refused with the path of the file that holds it.

**Claim ledger** (`claims.rs`). An agent about to compute something needs one
statement with its hypotheses, not the note that happens to contain it. Notes
carry fenced `claim` blocks — `id`, `statement`, `hypotheses`, `holds-here`,
`status`, `bearing`, `anchor`, `contradicts`, `answers` — and `research/CLAIMS.md`
is derived from disk on every research write, the way `INDEX.md` is derived from
a directory. `search_claims` retrieves rows. Two checks that were prompt-only and
never verified are now mechanical: a `contradicts` edge surfaces a contradiction
(the scholar prompt calls finding one "the most valuable thing you can find"),
and `holds-here: yes` with `status: asserted` is flagged as load-bearing but
unverified. A malformed block is reported, never silently dropped.

**Threads** (`threads.rs`). `research/threads/<slug>.md` is one direction of
attack — `question`, `status`, `rests-on`, `blocked-by`, `next` — deriving
`research/THREADS.md`. Unlike a seal it is live; unlike the arrival tree it is
organised by what a reader wants. Dead threads are kept with their reason, since
a known dead end is a result. A blocked thread with no stated blocker is called
out (a blocker stated precisely is the next research request; one left blank is a
mood), and a thread resting on a claim id not on disk is surfaced.

**Request ledger** (`requests.rs`). Gathering was triggered by inference — a
`STUCK` verdict, a gap in `ROOT.md`, an attempt count — none of which can be
closed, so nothing could say whether a search answered what prompted it.
`request_research` states it: what is missing, what the asker would do with it,
and what would falsify the belief they are working from. It is checked against
the claim ledger *before* queueing, so the common case (the run knows this and
forgot) costs a lookup rather than a download — the runtime's reluctance made
mechanical rather than requested. Its id is derived from its text, so one wall
hit by two roles is one row. It closes when a note carries `answers: <id>`.

**OEIS adapter** (`oeis.rs`). The one lookup with no phrasing problem: terms
either match a catalogued sequence or they do not, and a match usually carries
the closed form that turns an enumeration into an evaluation. It was a sentence
in the research prompt, which is to say it happened when a model remembered; as a
tool it is something a run can be seen not to have done. A miss is a result —
882 recorded `S(n) ∉ OEIS` as a finding. Entries are filed under `research/`
(a formula quoted into a tool result and nowhere else is uncheckable later) and
`Cf.` cross-references go into the frontier. Gated with `exa_search` under
`MATH_AGENT_RESEARCH`, by not registering it rather than by asking the model to
abstain.

## Context routing

| File | Roles |
| --- | --- |
| `research/CLAIMS.md` | planners, tool_builder/coder, scholar, librarian/research, inventor |
| `research/THREADS.md` | planners, scholar, librarian/research, inventor |
| `research/FRONTIER.md` | librarian/research only |

tool_builder and coder get the claims but not the threads: a closed form changes
what they implement, while which direction the run is pursuing is the planners'
call. `holds-here` is the load-bearing column there — implementing a theorem
whose hypotheses fail here yields a program that runs and computes the wrong
thing. Only the fetch-deciding roles see the frontier; to everyone else it is a
list of things nobody has read.

Verified end-to-end by rendering `dump_prompts` against a synthetic workspace:
each file reaches exactly the roles above and no others.

## Design notes

- All four ledgers are written by code, never an agent, and re-derived from disk
  on every relevant write — the `INDEX.md` rule, one level down. Each is
  described via `record_description` so none sits as `_(undescribed)_`.
- `search_claims` and `request_research` travel with the document tools, like the
  index tools: the role that needs to know what the run establishes, or that
  walks into a gap, is whichever one is working.
- One block format (`claims::fenced` / `fields`) for both claims and threads, so
  an agent learns one syntax for the library.
- No new dependencies. JSON ledgers use `serde_json::Value` directly, matching
  `documents.rs` and `vector.rs`.

## Verification

- `cargo fmt --all -- --check`, `clippy --all-targets --all-features -D warnings`
- `cargo test --all-features` — 264 passed, 62 new
- `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps --all-features`
- `sh -n` on every script; `docker compose config --quiet`

## Two things to flag

`README.md` is at exactly 500 lines. Fitting the new material under the repo's
own cap meant tightening several pre-existing paragraphs, which is a wider edit
than the additions alone.

`AGENTS.md` is now 1,102 lines. It was already 966 and well past the same cap
before this branch, so this adds a focused section rather than restructuring —
worth a separate pass if that rule should be enforced.

This branch was developed in a worktree at the user's request; the repository
guidelines otherwise prefer committing to `main`. Commit count is high because
the `auto-commit` hook checkpointed throughout.
