# Output — what a program produced, kept where it was produced

Run a program and capture what it printed into this folder. `code/` holds what a
person wrote; this holds what something computed. The split is what lets a
reader — and the judge scoring an attempt — tell a run that writes programs from
a run that runs them.

Capture the output rather than describing it. A report saying a program agreed
with the oracle is the first thing lost when an attempt is cut off at the run
cap; the file it wrote is not.

Write a Markdown note beside an output when the output settles something, and
put a fenced `claim` block in that note with `status: checked`. That is what a
verified computation earns, and it is how a computed result reaches
`research/CLAIMS.md` — which is otherwise a record of what the run has *read*
rather than what it has established.

An output that records a check against a known value must say so in words a
reader can find: whether it agreed, and with what. PE761's only independent
solver printed `agree? False` on every line, against published values it was
supposed to reproduce, and the run carried on reporting an answer supported by
one route while that file sat unread beside it.

Never leave a zero-byte `.captured.txt` in this folder. The `tee` in the
standard capture pattern creates the file the instant it starts, so a command
that dies before printing leaves an empty file that the judge reads as a failed
experiment. Before moving on, check every capture an attempt wrote is
non-empty; if a run printed nothing, put one line in the file saying what
happened (e.g. `not run: tool call rejected, superseded by the --lo/--hi
interface`).
