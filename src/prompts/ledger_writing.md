## Recording into a ledger

You hold `record_entry` and `close_entry`. Use them instead of writing the state
out as prose, and in particular instead of rewriting `TASKS.md` — that file is
derived now and an edit to it is discarded.

```
record_entry { ledger: "tasks", id: "fix-the-audit-verdict",
               fields: { title: "Fix the audit's verdict logic",
                         detail: "A refuted sub-check must not print ALL CHECKS PASSED.",
                         status: "open" } }

close_entry  { ledger: "tasks", id: "fix-the-audit-verdict", status: "done",
               reason: "verdict now prints (D) refuted separately; re-captured to
                        code/out/reduction_audit.captured2.txt" }
```

**Only the fields you name change.** Adding a blocker to a task costs one field,
not a re-statement of the task. This matters more than it looks: re-emitting a
whole file to change one line is the largest source of accidental loss here,
because a dropped row looks exactly like the file you meant to write.

**Closing is not deleting.** A closed entry stays on the ledger with its reason,
and that is the whole point of closing it. `status: "done"` says it was carried
out; `status: "dropped"` says it will not be. Both demand a reason and the
reason is the part that is worth anything later:

- *"the verdict logic now reports (D) separately, captured2 confirms it"* tells
  the next role what it can rely on.
- *"the empirical route is at its ceiling — row 248 is still capped at 1e9, and
  a 4e9 sieve would cost eight hours to hit the same wall"* stops somebody
  proposing the sieve again in three attempts' time.
- *"done"* tells nobody anything, and you have then spent the call for nothing.

Write the reason for a reader who was not there and cannot ask you.

**What a task is.** One thing somebody can pick up and finish, with what to do
in the `detail`. Not a theme, not a heading, and not the whole of the next
attempt. If you cannot say what would make it finished, it is a research
request or a thread, and there are ledgers for both.
