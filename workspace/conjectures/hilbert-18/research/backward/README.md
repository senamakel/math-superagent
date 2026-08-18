# Backward — what would suffice to prove the goal

One file per decomposition, `<slug>.md`, each carrying a fenced `skeleton` block
and one fenced `gap` block per missing lemma. `derived/BACKWARD.md` beside this
folder is derived from them and is not yours to edit.

This folder exists from the first second of a run for the reason
`research/approaches/` does: the reducer is told to write here before it
reports, and a directory the prompt names must be a directory. A first
`write_document` that comes back `is not a directory in the workspace` spends
the turn on the filesystem instead of on the mathematics.

A skeleton is not an approach. An approach is a *route* — a reformulation that
might get the run there, and `research/approaches/` holds those. A skeleton is a
*decomposition* — the goal itself, broken into propositions that can each be
attacked on their own. One answers what else could get us there; the other
answers what would be enough.

Every open gap is a task, so write it as one: a `next` that a tool_builder could
run today or a theorem_prover could be handed today. A lemma with no first move
is a research request, not a gap.

Record a discharged gap as carefully as an open one, with the claim id that
closed it. The single failure this folder exists to prevent is a later turn
restating a lemma the run already has, and the id beside it is the only thing
that prevents it.
