## The ledgers, and how to reach them

This workspace keeps its state in **ledgers** — the task list, the sub-goals,
the claims, the approaches, the threads, and any axis this run has added for
itself. `list_ledgers` names every one and says what it holds.

**The rendered files in your context are shortened.** `derived/APPROACHES.md`
and the rest carry a bounded row per entry, because everything in this prompt is
re-sent on every call you make. The whole of a refutation, the full statement of
a claim, the complete detail of a task — those are on disk, and `read_ledger`
is how you get them:

```
read_ledger { ledger: "approaches", status: "refuted" }
read_ledger { ledger: "tasks", query: "sieve" }
```

Two habits worth having, because they are cheap and the alternative is not:

- **Read before you conclude a ledger holds nothing.** A section that says
  `12 more not shown here` means exactly that. Treating the bounded copy as the
  whole record is how a run re-proposes something it already closed.
- **Read one entry in full before acting on it.** A one-line summary is enough
  to decide an entry is relevant and never enough to decide what to do about it.

Never edit a derived file by hand. They are rewritten from their sources on the
next write, so an edit is not a change — it is work queued for deletion, and you
will not be told when it goes. The write tools are the only way in, and if you
do not hold them, whoever does is the role to hand it to.
