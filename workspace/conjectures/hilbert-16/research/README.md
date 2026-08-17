# Research — what this run has read, and what it now believes

This folder exists from the first moment of a run rather than from the first
download, because every planning role is *told* about it before anything has
written here. On a workspace where it did not exist, a fresh run spent its
opening calls discovering that: `list_workspace research` and
`read_document derived/FRONTIER.md` both failed inside the first ten seconds
of PE620, on a librarian and a judge that had been handed those paths in their
own system prompts. A directory the prompts promise should be a directory.

## What goes where

| Path | What it holds |
| --- | --- |
| `sources/<name>.full.md` | A downloaded source's complete text. Nothing edits these. |
| `summaries/<name>.md` | What that source actually establishes — the note that replaces the excerpt. One file per source, under a thousand tokens. |
| `notes/<name>.md` | The run's own findings that are not tied to one source. |
| `threads/<name>.md` | One direction of attack: its question, what it rests on, what blocks it, what is next. |
| `approaches/<name>.md` | A proposed line of attack, and the reason it was taken up or dropped. |

Create a subfolder by writing the first file into it.

## The derived ledgers are not yours to write

`CLAIMS.md`, `THREADS.md`, `APPROACHES.md`, `FRONTIER.md`, and `REQUESTS.md`
appear here on their own and are rewritten from the files above whenever one of
those is written. Editing one by hand is work the next write throws away. To add
a claim, put a fenced `claim` block in the note that establishes it; to open a
thread, write the thread file.

A claim block belongs beside a program's output under `code/out/` too, not only
here. One run held a check value reproduced to ten digits and 38 points
cross-validated two ways, and its ledger said it had established nothing —
because the ledger read `research/` alone. If the run computed it and checked
it, write the claim down where it was computed.
