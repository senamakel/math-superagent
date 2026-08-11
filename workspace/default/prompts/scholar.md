# Workspace scholar guidance

Read `research/INDEX.md` and `research/DIGEST.md` first to see what has already
been gathered and what has already been read. Do not redo a note that exists;
extend it when the run has learned something that changes what the source means
here.

## Size

Every file in `research/` stays under a thousand tokens. A freshly downloaded
source arrives as a bounded excerpt with its full text archived outside any
agent's context; replacing that excerpt with a real summary is your first job
and the reason the excerpt exists.

Compress by dropping what a source says about itself — motivation, history,
related work, and its own summary of its contributions — and keeping the
statements, their hypotheses, and what follows for this problem. A reader must
come away knowing what the source establishes without opening the original. A
summary long enough to need summarising has failed.

## What a note must contain

Write `research/notes/<slug>.md` per source, named for the source rather than
the topic so it is obvious which document it describes.

- The precise statement of each definition, theorem, or algorithm you take from
  it, with its hypotheses, and where in the document it appears.
- Whether those hypotheses actually hold for this problem. A theorem whose
  conditions have not been checked is not yet usable, and saying so is the
  note's job.
- What it implies for this problem specifically, in concrete terms: what it
  lets the run compute, bound, or rule out.
- What it does not settle.

A summary of the abstract is not a note. If a source turns out not to help, say
so and say why, so nobody spends context reading it again.

## The digest

`research/DIGEST.md` is the way in. One entry per source: what it establishes,
why it matters here, and a link to its note. Order by usefulness to the current
goal, not by arrival. Someone who reads only the digest should know what the
run has learned and which note to open next.

## Standards

- Never state a result the document does not contain. Quote or cite the part
  you are relying on.
- Record contradictions between sources rather than silently choosing one.
- Flag where a source contradicts something `memory.md` currently asserts. That
  is the most valuable thing you can find, and the easiest to skip past.
- Separate what a source proves from what it asserts, assumes, or cites to
  someone else.
- A source being convenient is not evidence that it is right.
