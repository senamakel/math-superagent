# Method: the answer is not accepted until the Lean kernel carries it

This run is a Lean-first run. The number is not the deliverable on its own — a
program that prints it is evidence, and this run is being asked for a proof.

## The rule

**A `.lean` file with a passing `lean_check` verdict must carry the final
answer before this run reports one.** Not a Python script that agrees with
another Python script. The last theorem in the chain should be the answer
itself, as an equality of naturals, and every rung it rests on should be a
theorem in the same tree.

You may and should still write Python. Use it exactly as a mathematician uses a
computer: to see what is true, to test a conjecture at small size, to find the
factorisation, to check a formula before you spend an hour proving it. What you
may not do is let it stand as the final justification.

## The one tactic that is not available

`native_decide` is refused. `lean_check` rejects `Lean.ofReduceBool`, so a goal
closed by compiling and running a decision procedure will not pass, and neither
will a kernel `decide` over a search space large enough to matter — it will not
terminate inside the tool timeout.

This is the point of the exercise rather than an obstacle to work around. It
removes the cheap route at the last step, and what is left is the structural
argument: prove the reduction, then evaluate something small enough that the
kernel can do it by unfolding. A run that finds itself needing `native_decide`
has found that it has an answer and not a reason, which is worth knowing.

## Where a hard computation goes: the certificate pattern

Some steps are expensive to *find* and cheap to *check*. A factorisation is the
model case: finding the factors of a large number is work, and verifying them is
one multiplication. Do the finding in Python and hand Lean the answer as a
literal, so the kernel checks the step it can check cheaply.

```lean
/-- src: found with `code/factor.py`; verified here by multiplication. -/
theorem factors_600851475143 : 600851475143 = 71 * 839 * 1471 * 6857 := by norm_num
```

That is a kernel-checked fact, and nothing about it trusts the Python. The same
shape works for a witness, a bound, or a finite case list: search outside, check
inside.

## Where the mathematics goes

Everything the run establishes goes under `code/lean/Lib/`, one namespace per
subject, one subject per file, importing only the Mathlib modules it needs.
`research/LEMMAS.md` is derived from that tree and is what the next role reads —
a signature carries its own hypotheses, so it cannot lose one the way a prose
summary can, and it costs a line where a summary costs a page.

A result you took from the literature and did not prove here goes in the same
tree as an `axiom` under `namespace Cited`, with the source in its docstring.
That gives the theorem depending on it a `conditional` verdict, which is honest
and is a real result. It is not `formalised`, and nothing about the namespace
makes it more likely to be true.

Markdown is still where the things Lean cannot say go: what you tried that did
not work, what the obstruction was, why a route was abandoned. Those are often
the most useful thing a run produces and they do not compress into a type.

## Order of work

1. Restate the problem in `GOAL.md` and reproduce every worked example in the
   statement with an obviously-correct brute-force program. If it disagrees,
   your reading is wrong and nothing else matters.
2. Find the structure — the theorem that turns the search into a computation.
   Write it as a Lean *statement* first, ending in `sorry`, and check that it
   elaborates. Getting the statement right is most of the work and a wrong
   formalisation is worse than none.
3. Prove the rungs, smallest first, each in its own file. Check each with
   `lean_check`, not with the shell: a proof checked in the shell leaves no
   verdict, and the rest of the run cannot tell it from a sentence.
4. Compute the answer, and prove it.
5. Report the answer, the theorem carrying it, the `lean_check` verdict
   verbatim, and every `sorry` and `Cited` axiom that remains.

If step 3 stalls, say precisely which goal is left after which tactic. A
formalisation that fails at a specific step has found something, and it is
usually the gap in the informal argument.
