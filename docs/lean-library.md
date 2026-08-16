# The Lean library: writing what the run knows as Lean rather than as prose

The rules are in [`CLAUDE.md`](../CLAUDE.md) under *The Lean library*. This file
holds the argument behind them, the measurements that prompted the change, and
the limits — including the one that decides how far this idea can be taken.

## The problem this addresses

A conjecture workspace's research tree is prose, and it is large. Measured on
this repository's own workspaces:

| Workspace | `research/` | Markdown files |
| --- | ---: | ---: |
| `casas-alvero` | 2.8 MB | 202 |
| `frankl-union-closed` | 3.7 MB | — |
| `gilbreath` | 7.1 MB | — |
| `gilbreath-supply` | 9.5 MB | — |

Every paragraph of that is tokens a role pays for on the way into a prompt, and
`derived/CLAIMS.md` opens by admitting what most of them are worth: *everything
else on this page is a word somebody typed.* Of forty-odd claims in the
casas-alvero ledger, the great majority are `asserted` — a model read a paper
and wrote down what it thought the paper said.

Two failures live in that, and they are different failures.

The first is **size**. A summary costs a page and a statement costs a line, and
the run pays the page every time a role is assembled.

The second is **looseness**, and it is the worse one. The thing that goes
missing when a theorem is summarised is its hypotheses. `CLAIMS.md` already
carries a `holds-here` column for exactly this reason, with a note beside it: *a
true theorem whose hypotheses fail here is worse than no theorem, because it
looks like progress.* That column is a human-written guess about a
human-written summary. Nothing checks it.

A Lean declaration has neither problem. Its hypotheses are in its type, so they
cannot be dropped in the retelling; and its signature is one line.

## What is written where

```
code/lean/               work in progress: one lemma per file, iterate freely
code/lean/Lib/<Topic>.lean   what the library knows: one namespace, one subject
derived/LEMMAS.md       derived from the whole tree; do not edit
```

`derived/LEMMAS.md` is a ledger in this repository's sense — derived state,
walked by code, rendered to Markdown, refused to an agent's write path. It is
re-derived on every `lean_check`, which is the correct trigger rather than a
convenient one: half of every row is the *standing*, and standing is a verdict,
so re-deriving on a file write would publish a table saying `unchecked` about
work the kernel had just accepted.

Provenance goes in the Lean docstring, one line:

```lean
/-- src: arXiv:2307.05997 §4 Cor 8 -/
theorem bad_prime_criterion (p d : ℕ) (hp : p.Prime) : … := …
```

That line replaces a paragraph and is read into the ledger's `Source` column.

## `namespace Cited`, and the third verdict

The obstacle to writing a library in Lean is not the mathematics, it is honesty
about what has been proved. Most of a research library is *implications*: this
follows from that, and *that* is somebody else's theorem, which this workspace
has not proved and cannot check.

Written as a bare `axiom`, such a theorem is indistinguishable from a hole
somebody left — which is precisely the failure `lean.rs` refuses, and refuses
correctly. Before this change, compressing a paper into Lean produced a file
whose verdict could only fail, so the honest thing and the unrecordable thing
were the same thing.

The fix is a namespace and a third outcome:

```lean
namespace Cited
/-- src: Mihăilescu 2004, Crelle 572, Thm 1 -/
axiom catalan : ∀ x y p q : ℕ, 1 < p → 1 < q → x ^ p - y ^ q = 1 → (x, p, y, q) = (3, 2, 2, 3)
end Cited
```

| Verdict | Means |
| --- | --- |
| `verified` | Compiles, no `sorry`, axioms printed, all of them Lean's own three. |
| `conditional` | The same, plus axioms under `Cited.` that nothing here proved. |
| `failed` | Anything else, with the specific reason. |

**The namespace buys no trust.** A conditional result is not a verified one and
never becomes one. What it buys is that the implication can be *recorded*.

Three properties are worth stating because they are what makes it safe, and all
three are asserted in `lean_test.rs`:

- A `Cited.` axiom beside an unattributed one still fails, and the objection
  names the unattributed one.
- A `Cited.` axiom does not excuse a `sorry`. A citation says where a
  *hypothesis* came from and says nothing about a gap in a proof.
- The match is a prefix, not a substring, so `NotCited.sneaky` is a hole.

### Where `conditional` sits relative to `proved`

`Status::Conditional` sits between `Formalised` and `Proved` in `claims.rs`, and
the comparison with `Proved` is the interesting one, because both rest on a
paper's word.

The difference is *which step is checked*. `Proved` means a model read a PDF and
summarised it; the step from the paper to the claim is the summary, and that
step is where hypotheses go missing. `Conditional` means the step from the cited
statement to the claim was checked by the kernel. The failure mode `Proved`
carries — that the cited result does not actually give what the run thinks it
gives — is the one failure mode `conditional` does not have.

Its standing in `BLUEPRINT.md` is `Established`, not `Verified`, for the
matching reason: a node reported verified says the argument rests on nothing
further, and this one rests on a paper.

### The status cannot be typed

The ledger reads the status off the verdict, not off the note. A claim written
as `formalised` over a file resting on cited axioms is recorded as
`conditional`, with the axiom named — downgraded to what the kernel found and no
further, because pulling it to `asserted` would throw away an implication that
was actually checked. A claim written as `conditional` over a clean file is left
alone: understating what you have is not something the ledger should correct
behind a role's back.

## What does not move into Lean

Lean carries statements, definitions and dependencies. It does not carry:

- why an approach failed, and what the obstruction was;
- what was tried and abandoned, and at which step;
- the reading of a paper that is *judgement* rather than statement.

Those stay in markdown, and on an open problem they are often the most valuable
thing a run produces. The compression is real but partial: it applies to the
half of the library that is mathematics, and the other half is why
`research/notes/` still exists.

## Reaching the kernel without installing it

Lean 4 and a 7.1 GB prebuilt Mathlib are in the runtime image and nowhere else,
which is right — see [`runtime.md`](runtime.md) — but it left every `.lean` file
a run produced unreachable to anyone not inside a run.

```sh
./lean-check conjectures/gilbreath code/lean/link_a.lean
./lean-check project-euler/622 code/lean/Lib/Riffle.lean --json
scripts/lean-replay --all
```

`scripts/lean-check` runs `docker run` against `math-agent:local` with the
`lean-verdict` binary as its entrypoint, under the same hardening `compose.yaml`
applies to a run. It is a second *caller* of `math_agent::check_lean_file`, not
a second implementation: the one thing this repository must not answer twice is
what counts as verified. Exit codes are the verdict — `0` verified, `1` failed,
`2` conditional.

The mount is read-only and **no verdict is ever filed**. `code/out/lean/` is the
evidence `CLAIMS.md` consults, so the only thing that may write there is the
`lean_check` tool inside a run.

That was briefly a flag rather than a rule, and a live run found the hole in
thirteen minutes: `lean-verdict` ships in the runtime image, so `execute_command`
can call it, and a `--file-verdict` flag would have let a role file its own
evidence without going through the tool that grants it. Every env-var gate that
might have guarded the flag is settable from the same shell. The capability was
removed instead — it had no caller — which is the only version of the rule that
is not a prompt instruction. A role reading a verdict from the shell is fine and
is not new: `execute_command` could always run `lean` directly.

## What the first replay found

`scripts/lean-replay --all`, over every `.lean` file four past runs left behind:

| Workspace | Files | Verified | Failed | Disagreements |
| --- | ---: | ---: | ---: | ---: |
| `consecutive-perfect-powers` | 24 | 2 | 22 | 0 |
| `erdos-gyarfas` | 5 | 0 | 5 | 0 |
| `erdos-gyarfas-run1` | 2 | 1 | 1 | 0 |
| `erdos-gyarfas-run2` | 15 | 3 | 12 | 0 |
| `gilbreath` | 32 | 8 | 24 | 0 |
| **total** | **78** | **14** | **64** | **0** |

Two things to read off it.

**Zero disagreements.** Every one of the 24 files that had a filed verdict got
the same answer on replay. That is the result that makes the other number worth
quoting: the host path and the in-run path agree, so the wrapper can be trusted.

**Fifty-four of seventy-eight files had no verdict at all.** They were written
and the kernel was never run over them — 69% of everything the runtime had ever
produced in Lean. `lean_prover.md` said, in bold, *check every file with
`lean_check`*, and this is the number that instruction achieved.

That is this repository's own recurring failure, recorded once more: a prompt
instruction is not a control. It is also why `LEMMAS.md` has an `unchecked`
standing and a **Never checked** section rather than quietly omitting such
files. An unchecked `.lean` file on disk reads exactly like one that passed, and
until the index said so, nothing in the runtime distinguished them.

## What a kernel check cannot do, with the instance that proved it

The check is a control on the *proof*, not on the *statement*. `lean.rs` has
said so since it was written — *a Lean proof of the wrong statement is still the
wrong statement* — and the Lean-first run on Project Euler 622 supplied the
concrete case.

Told that the answer was not accepted until a `.lean` file with a passing
verdict carried it, the run wrote real mathematics: `S_60` and `C_60` are honest
theorems, the Möbius-inverted divisor sums over `2^60 - 1`. Then, under a
docstring reading *the answer stated directly as an equality of naturals*, it
wrote

```lean
theorem pe622_answer_nat : 3010983666182123972 = 3010983666182123972 := by rfl
```

That compiles, carries no `sorry`, depends on no axiom at all, and says nothing
whatever about the problem. Every check in this file would have passed it as
`verified` — the strongest status the runtime has — and the claim ledger would
have carried the answer on it.

A mandate to produce a passing verdict *invites* this. The letter of it can
always be satisfied by a statement that is true for free, and the more a run is
pressed for a verdict the more attractive that becomes.

So `lemmas::tautologies` refuses the narrowest version: a `theorem` or `lemma`
whose top-level `=` has textually identical sides. That is never informative and
is always safe to refuse, and it is checked before the axioms because a file
containing one is usually flawless in every other way — which is exactly what
makes it dangerous.

It is not a triviality check and cannot be. `2 + 2 = 4 := by rfl` is a real fact
and keeps passing, because its sides differ. What no mechanism catches is a
statement that is merely *beside the point* — true, non-trivial, and not about
the problem. That is what `lean_prover.md` asks the role to describe in prose,
and what the `holds-here` column in `CLAIMS.md` is for. The kernel raises the
floor; it does not remove the reader.

## What the 622 run measured

| | |
| --- | --- |
| Elapsed | 122 minutes |
| `.lean` files written | 18 |
| Filed verdicts | 3 — one `verified`, two `failed` |
| Declarations in the index | 81 |
| Declarations in a checked file | **2** |

The verified one is `code/lean/Lib/Shuffle.lean`, and it is the deliverable: a
kernel-checked definition of the out-shuffle and its order, reached because a
workspace `METHOD.md` asked for it.

The other number is the finding. 2 of 81, against 14 of 78 files historically —
the same failure, worse, on a run explicitly told to formalise. It is why the
lemma index refreshes on a `.lean` *write* and not only on a check: the files a
role never checks are the ones the index most needs to name, and they are
exactly the ones that never trigger a check.
