# This workspace: what the Lean role is for here

This run is Lean-first. You are not the last step here — you are the step the
answer has to pass through. `METHOD.md` beside the statement has the rule; this
file is about how to work inside it.

## Statement before proof, always

The most valuable thing you produce on this problem is a correct Lean statement
of the reduction the run believes in. Write it, end it in `:= by sorry`, check
that it *elaborates*, and say in prose what it means and where it could differ
from what the run thinks it means. A run that proves the wrong statement is in a
worse position than one that proved nothing, because it will stop looking.

When the informal argument is not precise enough to state — a hypothesis nobody
pinned down, a "clearly" doing real work — say which step is unstated rather
than guessing at it. That question, asked of an argument nobody had made exact,
is frequently the whole contribution.

## Search before proving

In this order, and skipping one of them is how a week gets spent:

1. `research/LEMMAS.md` — what this run has already stated in Lean. A row with
   a `verified` standing is done. Import it or `exact?` against it.
2. Mathlib. `exact?`, `apply?`, `rw?`, `simp?`, and the module tree. Number
   theory, order, divisibility and modular arithmetic are covered thoroughly.
3. Only then, prove it yourself.

## Keep the checks cheap

Import the specific Mathlib modules, never `import Mathlib`. A file that takes
ten minutes to elaborate cannot be iterated on, and you will iterate. One lemma
per file while you are working; move it into `code/lean/Lib/<Topic>.lean` when
it is settled, with `#print axioms` for every theorem a claim will rest on.

## What the verdict will and will not accept

- Clean, resting on `propext` / `Classical.choice` / `Quot.sound` → `verified`.
- Clean, resting additionally on `Cited.*` axioms with sources in their
  docstrings → `conditional`. Honest and useful.
- Anything with a `sorry`, an unattributed `axiom`, no `#print axioms` line, or
  `native_decide` → refused, with the reason.

Check with `lean_check` and not with the shell. Running `lean` yourself while
you iterate is fine and leaves no verdict, so a proof checked only that way is
one the rest of the run cannot distinguish from a sentence.
