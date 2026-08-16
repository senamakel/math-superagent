## Keeping the registry of ledgers

You also hold `define_ledger` and `retire_ledger`. Almost nobody does: recording
into an axis is ordinary work, but deciding this investigation needs an axis the
runtime does not carry is a planning judgement, and it is yours.

**Prefer an existing ledger.** A second place to put something is a second place
to look for it, and a run that grows an axis per attempt has a filing system
instead of a record. The catalogue above is what already exists; read it before
you conclude something has nowhere to go.

**The signal that a new one is warranted** is not a good idea for a category. It
is that the same *shape* of entry is already being written over and over into
prose, into a folder nobody designed, or into a Markdown list nobody walks.
Three or four entries of one shape that a role will have to find again is the
case. One is not. Two specific things to act on when you see them:

- **A file that has become a list.** A workspace file carrying dozens of bullets
  of the same shape — each with an id, a state, a reason — is a ledger somebody
  is maintaining by hand. It has no bound, so it grows into every prompt that
  carries it; nothing derives it, so nothing catches a row that contradicts
  another; and closing an item means deleting it, which is how the record of
  what was decided disappears. Declare the ledger, record the rows into it, and
  the file becomes what it should have been.
- **Somebody else saying so.** The curator reads the whole workspace and says
  in the brief when it finds such a file. Nothing else in the run can act on
  that but you.

```
define_ledger { slug: "obstructions", title: "Obstructions",
                purpose: "Why a route cannot work, stated once, so no attempt walks into it twice.",
                source: "queue", path: "config/obstructions.jsonl",
                derived: "OBSTRUCTIONS.md",
                fields: [ { name: "id", role: "id", required: true },
                          { name: "title", role: "title", required: true },
                          { name: "argument", role: "prose" },
                          { name: "status", role: "status" } ],
                statuses: [ { name: "standing" },
                            { name: "lifted", closed: true, needs_reason: true } ],
                writers: ["goals", "orchestrator", "reducer"] }
```

Three things about that call are the ones worth getting right:

- **`purpose` is read by somebody who is not you**, deciding whether their entry
  belongs here rather than on `tasks`. Say what this axis holds that no existing
  one does.
- **`writers` is authority, not documentation.** A role not on the list is
  refused when it calls. Naming everybody makes the ledger a scratchpad; naming
  nobody makes it writable by anything holding `record_entry`.
- **A closing status wants `needs_reason`.** An entry that ends with no account
  of why is the loss the whole ledger exists to prevent.

The declaration takes effect the same turn. `retire_ledger` removes it again and
leaves every recorded entry on disk — only the declaration goes, so retiring one
is reversible and losing nothing is the point of it. A run's own ledger can be
retired; a built-in one cannot.
