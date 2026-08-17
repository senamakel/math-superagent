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

## The certificate arm: making a computation the strongest row rather than the weakest

A run enumerates, sieves and sweeps constantly, and until this existed every one
of those results reached the ledger as prose somebody typed — `asserted`, the
weakest status there is. That is backwards. An exact computation is the *most*
checkable thing a run produces, and the arrangement that makes it checkable is
read off a proof that used it at scale: nine tenths of the ProofAtlas Sendov
formalisation is certificate, 110,406 lines of it against a 10,527-line
argument, and it earns the same `verified` verdict as the argument does.
[`../research/proofatlas/01-sendov-bundle-anatomy.md`](../research/proofatlas/01-sendov-bundle-anatomy.md)
has the anatomy and the counts.

Four parts, and the order is the whole content:

```
code/lean/Lib/<Topic>/Generated/Data499.lean   def rows499 : … := [ … ]   ← untrusted
code/lean/Lib/<Topic>/Schema.lean              def check (r : Row) : Bool
                                               theorem check_spec : check r = true ↔ P r
code/lean/Lib/<Topic>/Replay499.lean           theorem ok : checkAll rows499 = true := by decide
```

**Generated data may not conclude anything, and that is enforced.** A `theorem`,
`lemma`, or `axiom` in a path containing a `Generated/` segment fails the
`lean_check` verdict and names the declaration — `lemmas::generated_conclusions`,
refused in `Verdict::objection`, and excluded from `states_something` so it
cannot even be kept as a partial statement to build on.

The failure that rule stops is the one that looks most like success. A generator
emitting both its data *and* the theorem about it produces a file that compiles,
carries no `sorry`, rests on Lean's three axioms, and proves whatever statement
the generator chose to make — so the kernel check is real and vouches for
nothing. Every one of the 559 generated modules in that bundle says so in its own
header: *"All declarations below are untrusted certificate data. Mathematical
conclusions must pass through the human-written replay and block checkers."* The
difference here is that it is a control rather than a header.

**A checker that reduces a Boolean over data is exactly the right thing to
write**, and is only wrong in the file the generator produced. The check is about
provenance, not shape: the identical theorem outside `Generated/` passes.

**Data nothing reads is a file, not evidence.** The other half cannot be checked
one file at a time, so it lives in the derivation: `derived/LEMMAS.md` renders
*Generated, and nothing reads it* listing every generated module whose declared
names appear in no hand-written module. Name containment rather than an import
graph, deliberately — a checker reaches its data by naming a declaration, and the
two tests fail in opposite directions. Name containment can be fooled by a file
that mentions a name idly, which is a false pass a reader can see; an import test
would report every module reached through a re-export, which is a false alarm on
correct work, and a check that cries wolf is one a run learns to ignore.

**`decide`, never `native_decide`.** Already enforced through the axiom list —
`Lean.ofReduceBool` fails a verdict — and worth restating here because the
certificate arm is where the temptation is strongest and the loss is largest.
The Sendov bundle uses `decide +kernel` 1,010 times and `native_decide` zero
times, which is the same line this runtime draws, drawn independently.

## Clearing the denominators

`lean_check` names any statement that divides by something the statement does not
say is nonzero. It is the one check here that **reports and never refuses**: it
cannot be made exact — `lemmas::uncleared_divisions` is a textual scan that skips
numerals and accepts `≠ 0`, `0 <`, `0 ≠`, `.Pos` and `.ne'` in the binders — and
a wrong refusal on a correct file costs more than a note a reader can dismiss.

It is carried anyway because Lean makes the mistake silent. `x / 0 = 0` is a
theorem, so an unguarded division compiles and the statement is quietly weaker
than the one intended; nothing else in a verdict would ever mention it.

The discipline behind it is one the Sendov proof follows everywhere and states
out loud at each step — *no division by `J`, a root, or a product occurs*, *only
the positive scalar `n²` is cancelled*, *`j = 0` is retained*. Keeping every
identity cleared is why that argument needs no nonvanishing side conditions, and
therefore why repeated roots, zeros on the boundary and nonmonic polynomials cost
it no case analysis at all. The advisory prefers the multiplied form over the
extra hypothesis for that reason: a cleared identity carries its degenerate cases
instead of excluding them one at a time.

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

### The collector stamp: collected against supplied

That rule says who *should* write a verdict. Nothing in a verdict said who
*did*. `code/out/lean/` is inside the workspace and the write path refuses only
`derived/`, so a record shaped like a verdict is a file like any other — and to
the join in `claims.rs`, a kernel run and a hand-typed JSON object were the same
bytes.

So a verdict now carries a `collector` block, stamped in the two code paths that
actually invoke the kernel and reachable from nowhere else — not the tool schema,
not a prompt, not the write path:

```json
"collector": {
  "toolchain": "leanprover/lean4:v4.29.0",
  "elapsed_ms": 1234,
  "source_digest": "9f86d081884c7d65..."
}
```

The failure came from ProofAtlas, which blocks its largest result on exactly
this and on nothing mathematical — 1,176 Lean files, zero `sorry`, a clean axiom
list, and `buildTranscriptRecorded: false`, `collectorCommit: null`. Their
sentence for it is *the retained audit is a summary rather than the complete
build transcript required by the current evidence contract*.
[`research/proofatlas/06-trust-model.md`](../research/proofatlas/06-trust-model.md)
has the rest. A transcript you were given is a claim; a transcript you collected
is evidence.

The two halves are graded differently, and the asymmetry is the design:

- **`source_digest` mismatch downgrades.** The kernel ran and accepted
  something — text the file no longer contains. That is not a doubt about
  provenance, it is a fact about staleness, so the claim drops to `asserted`
  with the reason naming the file. This is also the common honest failure: a
  verdict earned fairly, and the statement edited underneath it afterwards.
- **A missing `collector` is reported, never downgraded.** Every verdict written
  before the stamp existed is unstamped through no fault of its own, and taking
  standing away from a run that earned it would be a worse error than the one
  being prevented. Those claims render under *Formalised on a verdict with no
  provenance*, which asks for one more `lean_check` over a file already checked
  and empties itself as that happens.

The honest limit: this is not a signature. A determined forger with file-write
could write a plausible `collector` block, and `elapsed_ms` is recorded but never
checked — a zero is the shape of a check nobody ran, and a reader notices it. The
control's value is that absence is *visible* and the normal path stamps it
without anyone remembering to, not that presence is unforgeable. Tightening a
missing stamp into a downgrade is the follow-up, once live workspaces have
re-checked.

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

## Two roles, and why the writing moved off the run's model

`lean_prover` was one role doing two jobs: deciding what to state, and getting
Lean to accept it. They want different things. The first is judgement — is this
statement faithful to the mathematics, does it earn a claim — and wants the
run's own model with the investigation in front of it. The second is mechanical,
repetitive, and mostly consists of arguing with the elaborator.

The measurement that split them, taken against this repository's own kernel on
2026-08-17:

| | Leanstral (`labs-leanstral-1-5`) | the run's default |
|---|---|---|
| routine Mathlib lemma | 1–4 s, kernel-`verified` 2/2 | 183 s, failed |
| output rate | 80–135 tok/s | ~50 tok/s including reasoning |
| cost per attempt | $0 (free preview) | ~$0.0017 |

Both models then failed the same harder statement — a degree-2 Casas-Alvero
identity over `ℂ` — and failed it *at the same step*, deriving `a*r*2 + b = 0`
and being unable to conclude `b = -(a*r*2)`. So the specialised model is not
smarter. It is roughly fifty times faster and free, which is what makes volume
affordable, and volume was the thing missing: 33 of 45 workspaces held no Lean
at all, and Conway-99's blueprint ranked 87 verification candidates of which
four had ever been attempted.

### The failure mode to design around

Leanstral reaches for `linarith`/`nlinarith` over fields with no order. Across
four independent samples and a four-round repair loop fed real kernel errors, it
used them in seven of eight attempts — including when the prompt said in as many
words that `ℂ` is not ordered and those tactics do not apply. Neither explicit
instruction nor tool feedback dislodged it.

`src/prompts/lean_scribe.md` therefore says what to reach for *instead*
(`linear_combination`, `ring_nf`, `field_simp`) rather than only what to avoid,
and `orchestrator_registry_test.rs` asserts the prompt still carries it. It is
not a fix — the model did this anyway — but a prompt that only forbids leaves
nothing in the gap.

### What the split buys, and what it costs

The scribe's assembled prompt is ~670 tokens against `lean_prover`'s ~20,000,
of which roughly two thirds was workspace state: `CONTEXT.md` at 6,380 tokens,
`CLAIMS.md` at 2,772, `LEMMAS.md` at 2,008. None of it helps a role that is
handed one statement and asked for one file, and all of it would be sent on
every call.

The boundary is that the scribe holds `lean_check` and holds no ledger write. It
can establish that a file compiles; it cannot file anything saying what that
means. `only_the_lean_prover_can_mint_a_formalised_claim` is the test.

It also holds no durable memory, which is the second exemption from a rule that
otherwise reaches every role. The argument is in
`every_agent_but_the_judge_and_the_scribe_can_write_durable_memory`: what the
scribe establishes is already durable without a note, because the `.lean` source
and the kernel verdict are on disk and `LEMMAS.md` re-derives from them.

### The provider, and two things it required

The tier runs on Mistral's own endpoint rather than through OpenRouter, reached
via the vendored `ProviderSpec` so the base URL and key name are not restated
here. Two constraints that are not obvious from the outside:

- **`temperature: 0` is rejected unless `top_p: 1` is sent with it** — HTTP 400,
  `code 3054`. The vendored request builder cannot express this, because both
  names sit in the `RESERVED` list that the provider-options escape hatch filters
  out. `agent::sampling` is the decorator that completes the pair.
- **The account admits ~0.63 requests/second** (5M tokens/min is slack by
  comparison). `agent::pace` spaces departures rather than bucketing them,
  because an idle bucket lets a fan-out leave together and 429 together.

`StickyProviderModel` and `ReroutingModel` are withheld from this tier: both
speak OpenRouter's dialect — one writes a `provider` object into the request
body, the other matches OpenRouter's error text — and against a direct endpoint
they produce a malformed request rather than a degraded pin.

An unset `MISTRAL_API_KEY` puts the scribe on the run's default model and says
so at startup. The workflow document then publishes `default` for that role,
because it is a record of what ran and not a statement of intent.

**Leanstral is in public preview and free, and enabling Labs models is an
organisation setting on Mistral's *privacy* page** — prompts sent there may be
used as training data. That is a reason not to point the mill at an argument the
run has not published.

## `./lean-mill`: from the reading to the library

The verification arm asks what the most rests on, and needs a statement graph to
answer. Most workspaces do not have one, and that is exactly where the Lean is
missing — Conway-99 carries 246 research files against 16 Lean ones, a ratio of
roughly forty to one by line count.

The mill walks the other way: prose the workspace already holds, to candidate
statements, to files, to verdicts.

```sh
./lean-mill conjectures/casas-alvero research/summaries --budget 25
```

It takes no blueprint and writes no attempt records, so it works on a workspace
that has never been decomposed. Only what the kernel accepts is kept: a `.lean`
file that does not compile sitting in the library is worse than an absent one,
because `LEMMAS.md` re-derives from the sources and a failed file becomes a row
that reads like work. What was found and not attempted is reported rather than
dropped, under the same rule every ledger section follows.

A statement the source *proves* becomes a theorem this run must prove. One the
source merely quotes becomes an `axiom` under `namespace Cited` and earns
`conditional`. The extractor is asked for that distinction explicitly, because a
model that marks everything cited produces a library of assumptions and one that
marks nothing cited produces a library of unprovable obligations.

Fetching a paper by URL or arXiv id is parsed and then refused with a message
saying so: the download is the librarian's tool and is not wired to this entry
point. That is deliberate — milling nothing and reporting a clean pass is the
failure worth avoiding.

### What a mill run keeps, after the first Casas-Alvero pass

The first version kept only kernel-`verified` files, on the argument that a
`.lean` file which does not compile is worse in the library than an absent one.
That argument is right and unchanged. What it got wrong is the middle case.

A live pass over `workspace/conjectures/casas-alvero/research/summaries`
produced this, and then deleted it:

```lean
theorem ca_at_least_five_distinct_roots (f : Polynomial ℂ) (hmonic : f.Monic)
    (hdeg : f.natDegree ≥ 5)
    (hderiv : ∀ i, 1 ≤ i → i ≤ f.natDegree - 1 → ¬ IsCoprime f (derivative^[i] f))
    (hnot_pure_power : ¬ ∃ (g : Polynomial ℂ) (k : ℕ), 2 ≤ k ∧ f = g ^ k) : …
```

It compiles. Its binders are Mathlib's own vocabulary. Its only defect is the
`sorry` underneath, which nobody on earth can currently remove, because the
statement is an open conjecture. `verify.rs` already makes the argument for its
own decomposition stage — *"a `sorry` here is the point rather than a failure,
because it says exactly where the argument is missing"* — and the mill was
throwing exactly that away.

So a run now reports three classes, and `Verdict::states_something` is the
predicate for the middle one: compiled, at least one declaration, nothing
vacuous, no retired binder. A `sorry` is explicitly allowed.

| class | kept | may back a claim |
|---|---|---|
| verified | yes | yes, `formalised` |
| stated with gaps | yes | **no** |
| rejected | no, removed | no |

The middle row is the one to be careful about. It is not a passing outcome and
`outcome()` does not admit it; it says only that the file is worth leaving on
disk for something else to work on. A report that merged it with the first row
would let a reader take a `sorry` for a proof, which is why the rendering names
the two separately and says in words that a stated file backs no claim.

### Probes have a directory

The scribe holds no search tool, so `#check` inside a file is its only way to
find out whether a Mathlib name exists. On the same Casas-Alvero pass, **17 of
26 kernel verdicts were `test_*` files** it had written into `code/lean/Lib/`
for exactly that purpose — `test_resultant`, `test_mvpoly`, `test_check9`.

Forbidding the probes would be wrong, because the need is real. They have
`code/lean/probe/` instead, the prompt names it, and a mill run sweeps it at the
end: it is scratch by construction, and a probe nobody deleted reads to the next
run exactly like a statement.

### The mill inside a run

`./lean-mill` is a person deciding a workspace has read too much and formalised
too little. That decision should not have to be made by hand, so the library arm
makes it every diversify: after the librarian gathers and the scholar reads,
`mill::gather_fresh` takes the notes written since the newest file in
`code/lean/Lib/` and `mill::run` turns up to `mill::LOOP_BUDGET` of them into
checked statements.

Two numbers differ from the command's, and both for the same reason — this runs
beside five other arms on every pass of a run that may make hundreds, where the
command is a job somebody is waiting for. The budget is five rather than
twenty-five, and the read bound is 64 KB of notes rather than the prompt-context
ceiling.

The file clock is what stops the arm re-milling its own output. It is a
heuristic and is allowed to be: its failure modes are milling a note twice — the
kernel rejects the duplicate, or the library gains a second name for one
statement — and waiting a pass. Neither loses anything the run had.

## What the loop requires of an attempt

An attempt must end with a `.lean` file the kernel has seen *and* with an
executed program. The program requirement is the older one and stays — it is
what stopped attempts that ended in notes — but the order is now stated: a
program is evidence *for* a statement, and the attempt is asked to say which
statement each one bears on. What that changes is what a run can be while
looking productive. It was possible for the whole output of a run to be programs
and prose, every piece of it a reason to believe something and none of it the
thing itself.

Beside the opening oracle run, the first attempt also opens a formalisation:
the problem itself, into `code/lean/Lib/Statement.lean`, `:= by sorry` under it.
Nobody is asking for a proof there. The point is that a Lean statement cannot be
written at all without every hypothesis being named, and that the run's two
scheduled paths to the kernel both need something to rank — `verify` needs a
statement graph and the mill needs digested notes, and an early run has neither.
So without this, the opening passes of a run reach the kernel not at all, which
is exactly when a mis-stated problem is cheapest to catch.

## Known gaps, with what measured them

Five live mill runs across two workspaces produced these. Each is recorded with
the number that would tell you it had been fixed, because the thing this
repository keeps getting wrong is a plausible improvement nobody measured.

### The scribe cannot search Mathlib

It holds `write_tool_file` and `lean_check` and nothing else, which is
deliberate — given the document tools it spent 180 of 191 tool calls re-issuing
one identical `grep_workspace` and never wrote a file. But `#check` inside a
file is then its only way to learn whether a name exists, so on a Casas-Alvero
pass **17 of 26 kernel verdicts were probe files**, and files like this were
submitted as the deliverable:

```lean
import Mathlib
open Polynomial
#check Polynomial.hasseDerivative
```

The budget went to the search and left nothing for the statement. A narrow
`search_mathlib` against the image's prebuilt `.olean` tree would make a name
cost one cheap call instead of a write/check round trip.

It is not obviously right: a search tool is somewhere to browse, and this role
browsed the moment it had anywhere to go. Any attempt should bound the result
count, refuse follow-up navigation, and be judged on **probe files per milled
statement**. Today's baseline is 1 of 8 `stated with gaps` on
`./lean-mill conjectures/casas-alvero research/summaries --budget 8`.

### A paper cannot be milled directly

`Source::parse` recognises a URL and an arXiv id and `OrchestratorAgent::mill`
then refuses both, because fetching is the librarian's tool and is not wired to
that entry point. The refusal is deliberate — milling nothing and reporting a
clean pass is the worse failure — but `--paper` is advertised by the parser and
does not work. Either wire it to the librarian or stop parsing what cannot run.

### One pass cannot read a large directory

`gather` stops at `MAX_WORKSPACE_CONTEXT_BYTES` and reports what it skipped, so
nothing is silent. But Casas-Alvero's summaries are 584 KB across 121 files and
a run reads roughly a fifth of them: **19 source files unread** on the last
pass. Milling a narrower path is the workaround. Chunked passes over one
directory, with the statements deduplicated across them, is the fix.

### Nothing has been proved yet

Across five runs the mill has produced **zero** `verified` files and one
`stated with gaps`. That is the honest headline and it should not be read past.
The statements it produces are blueprint material for `lean_prover` to
decompose, which is worth something given 33 of 45 workspaces held no Lean at
all — but it is not what "formalised" means, and the report says so in words for
that reason.

Conway-99 is close to a worst case and is worth avoiding as a benchmark: its
statements are about strongly regular graph parameter sets, which Mathlib has no
vocabulary for, so the scribe must either invent a scaffold or fail. Casas-Alvero
is the fairer measure because Mathlib covers polynomials over `ℂ` properly.
