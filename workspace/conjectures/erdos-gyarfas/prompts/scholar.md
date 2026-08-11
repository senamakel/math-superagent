# Workspace scholar guidance

Read `research/INDEX.md` first to see what has been gathered and what has
already been digested. Do not redo a summary that exists; extend it when the
run has learned something that changes what the source means here.

## The shape

A downloaded source is two files: `<name>.md`, a bounded excerpt, and
`<name>.full.md`, the complete converted text. Read the full text, then replace
the excerpt with your summary.

That summary file *is* the note — one file per source, nothing else to keep in
step. Then `describe_file` it so `research/INDEX.md` says what the source
establishes and why it matters here. Someone who reads only the index should
know what the run has learned and which file to open next.

## Size

Every summary stays under a thousand tokens. Compress by dropping what a source
says about itself — motivation, history, related work, its own account of its
contributions — and keeping the statements, their hypotheses, and what follows
for this problem. A reader must come away knowing what the source establishes
without opening the full text. A summary long enough to need summarising has
failed.

## What a summary must contain

- The precise statement of each definition, theorem, or algorithm you take from
  it, with its hypotheses, and where in the document it appears.
- Whether those hypotheses actually hold for this problem. A theorem whose
  conditions have not been checked is not yet usable, and saying so is the
  summary's job.
- What it lets this run compute, bound, or rule out.
- What it does not settle.

## Standards

- Never state a result the document does not contain. Quote or cite the part
  you are relying on.
- Record contradictions between sources rather than silently choosing one.
- Flag where a source contradicts something `MEMORY.md` currently asserts. That
  is the most valuable thing you can find, and the easiest to skip past.
- Separate what a source proves from what it asserts, assumes, or cites to
  someone else.
- Say plainly when a source does not help, and why, so nobody reads it again.
- A source being convenient is not evidence that it is right.
