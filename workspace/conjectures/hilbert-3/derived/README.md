# Derived

Nothing in this folder is written by hand. The runtime walks the notes a run
writes — the claim blocks in `research/notes/`, the skeletons in
`research/backward/`, the approach files, the task queue — and renders each
ledger here.

That means two things, and both matter:

- **Editing a file here is not a change.** It is work queued for deletion, and
  the next write to the underlying note overwrites it. To change what a ledger
  says, change what it is derived from: write the note, or use `record_entry`.
  The write path refuses these paths and names the right route.
- **Agents do not read these files directly.** They are hidden from
  `read_document`, `grep_workspace` and the listings, and reached with
  `read_ledger` instead — which bounds what it returns and can select by `id`,
  `status` or `query`. `CLAIMS.md` was measured at 7,488 tokens and one live
  `APPROACHES.md` at 86 KB; returning all of that to answer a question about one
  row is the cost the tool exists to avoid. `list_ledgers` names them all.

They are committed and kept for people. This is the record of what an
investigation established and what it ruled out, which is the point of the
product — it is read in a pull request, in a diff, and by whoever picks the
problem up next.
