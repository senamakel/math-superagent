# Lean bench — can the model this runtime runs on actually write Lean?

The runtime has run on DeepSeek since it was built, grants `lean_check` to the
`lean_prover` role, and had produced 78 `.lean` files across four workspaces
before anyone measured whether the model can write Lean at all. That question
has two halves and this directory answers the second.

**Retrospectively** — `evals/lean-baseline/`, written by `scripts/lean-replay`.
It re-checks every `.lean` file past runs left behind. It measures what the model
produced under real conditions, which is what a run actually gets, and it is
confounded by everything real conditions include: budget, context, and whichever
prompt that role was carrying that day.

**Prospectively** — this directory, written by `scripts/lean-bench`. A fixed task
set, one call per task, the same `src/prompts/lean_prover.md` the role gets, and
a kernel verdict as the score. Nothing is retried and nothing is negotiated: the
model gets one attempt, exactly as it does inside a run.

```sh
set -a; . ./.env; set +a          # never print it
scripts/lean-bench --model deepseek/deepseek-v4-flash-0731 --provider deepinfra
scripts/lean-bench --model deepseek/deepseek-v4-pro --provider deepseek
```

Reports land in `reports/<model-slug>.md`; the Lean the model actually wrote
lands in `workspace/lean-bench/code/lean/<model-slug>/` and is committed, because
a pass rate with no artifacts behind it is a number nobody can check.

## The three kinds, and why the pass bar differs

| Kind | Task | Passes when |
| --- | --- | --- |
| `statement` | Write the Lean statement of an informal claim, ending in `sorry`. | The file **compiles**. |
| `proof` | Prove a small self-contained lemma. | The verdict is `verified` or `conditional`. |
| `repair` | Fix a file that genuinely failed, given Lean's actual errors. | The file **compiles**. |

A `statement` task ends in `sorry` by construction, so scoring it on the verdict
would fail every correct answer. Compiling is the right bar and is not a weak
one: it means every name resolved and every type checked, which is most of what
"is this the right formalisation" asks. `lean_prover.md` calls getting the
statement right "frequently the whole deliverable", and this is the number for
that claim.

A `proof` task is scored on the verdict, so a `sorry` fails. `p3-proof-cited`
is deliberately a task where the *right* answer is `conditional`: it asks the
model to record a theorem it is not proving as a `Cited.` axiom and derive a
corollary from it. A model that instead proves the corollary outright has not
understood the task, and one that leaves a `sorry` has not done it.

The `repair` tasks are the real ones. Each is a file from `workspace/` that a
past run wrote and that does not compile, with the errors the kernel emits
today. Nothing is constructed and nothing is simplified.

## What this does not measure

Whether the statement is *right*. A file that compiles can be a correct
formalisation of the wrong claim, and no kernel catches that — it is why
`lean_prover.md` asks the role to say in prose what its statement means and
where it could differ from the informal one, and why `CLAIMS.md` carries a
`holds-here` column. Reading the committed `.lean` files is the only check on
that, and it is a human one.

It also does not measure a run. A run has a budget, a research library, other
roles to ask, and many turns to iterate. This is one shot with no library. It is
a floor rather than an estimate.

## Adding a task

One markdown file in `tasks/`, with a `---` header carrying `id` and `kind`, and
the instruction as the body. Keep the id in the filename so a report row can be
traced to the file that produced it. Prefer a task drawn from real workspace
material over an invented one: this bench is meant to measure this runtime's
actual job.
