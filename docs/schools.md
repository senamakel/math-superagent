# Schools: several mathematicians on one problem

The runtime attacked a problem exactly one way, and it never chose to. This
file is the argument for the schools, what each is a bet on, what they share,
and what is deliberately not built. The rule and the command are in
[`CLAUDE.md`](../CLAUDE.md); the evidence is here.

## The setting nobody knew they had chosen

[`research/mathematicians/12-cross-cutting.md`](../research/mathematicians/12-cross-cutting.md)
sets eleven mathematicians against each other and organises the result by
disagreement rather than by person. It states the rule this whole subsystem
applies:

> where all eleven agree, the runtime has a requirement; where they split, the
> runtime has a **setting it did not know it had chosen**.

It had chosen two, silently.

**Split 1 — trick against framework.** Tao, Erdős, Gowers, Wiles and Zeilberger
attack the problem where it stands. Grothendieck, Scholze, Arnold and Perelman
enlarge the surroundings until it dissolves. Grothendieck names the pair —
hammer and chisel against the rising sea — and explicitly refuses to rank them.
Every arm this runtime has built is chisel-side: `weakener` lowers the target,
`refuter` attacks the statement, `searcher` hits a score function, `reducer`
finds sufficient lemmas.

Why it was chosen is the part worth reading twice:

> The rising sea is unaffordable under `MAX_ATTEMPTS = 8` and
> `STUCK_THRESHOLD = 2` … So the runtime's thresholds *decided the
> methodology*, and no document says so.

A method whose whole shape is that the goal does not move for a long time while
the theory around it does is, to a counter that diversifies after two
unproductive attempts, indistinguishable from being stuck. The threshold was
set as a budget limit and functioned as a methodological commitment.

**Split 4 — where computation belongs.** `src/prompts/method_policy.md` opens by
requiring computation before prose. That is right for Project Euler, whose
problems have a number as an answer. It is inherited without argument by the
conjecture side, and the cross-cutting file records that **five of the ten
subjects' central results involved no computation at any stage** —
Grothendieck's four programmes, Fermat over eight years, geometrization for
Haken manifolds, the Liquid Tensor theorem, the Ricci flow papers.

## What a school is

Four things, and deliberately no more:

1. a method-policy overlay, layered after the shared policy and never replacing
   it;
2. optional per-role prompt overlays;
3. a bench — which specialists it leads with;
4. [`Thresholds`](../src/orchestrator/schools.rs) — when it changes course.

A school is **not** a second loop, a second graph, a second workspace or a
second set of roles. All of that is shared. The point is several
mathematicians in one workspace, not several runtimes in one container.

| Slug | The bet | Subjects |
| --- | --- | --- |
| `chisel` | Attack where it stands; compute first | Tao, Erdős, Gowers, Wiles |
| `rising-sea` | Enlarge the setting until the problem dissolves | Grothendieck, Scholze, Arnold |
| `adversarial` | Break it before proving it; price what is not proved | Erdős, Gowers, Zeilberger |

### `chisel` is the control, and its overlay is empty

`chisel` is today's runtime under a name. Its policy overlay is the empty
string, its thresholds are the existing constants, and `selected()` returns it
alone unless somebody asks for more.

That is not caution, it is what makes the rest measurable. A new school is only
evidence if the old one is running beside it on the same problem, and a change
that altered the control while adding alternatives could not be read at all.
`schools_test.rs` asserts the empty overlay rather than trusting it, and
`orchestrator_prompts` is tested for `load` and `for_school(.., chisel)` being
byte-identical.

### `rising-sea` has the only checkable firing rule in the corpus

Grothendieck describes the method and supplies no way to tell it from
procrastination. Scholze does: a change of ambient setting earns its place only
if it **covers the case where the old setting was working well**.

That is checkable against `research/CLAIMS.md` — name a result the run already
established and show the new setting reproduces it — and it is the whole reason
this school is affordable. Without it, "restate the problem in a better world"
has no failure condition and a school pursuing it cannot be told from one
achieving nothing.

Its thresholds are `Thresholds::patient()`: `stuck` raised by two,
`computational` by one, everything else the control's. Raising a threshold is
declined in [`methods-proposals.md`](methods-proposals.md) — *"it spends more
budget on the same measurement"* — and that decline stands for the single loop
it was written about. It does not reach here, because this is not the same
measurement run longer. `blocked` is deliberately **not** raised: a provider
failure is not a methodological question, and no school gets to reinterpret one.

### `adversarial` moves refutation before the attempt

The runtime's `refuter` runs on a cadence *after* the run has committed to a
statement. Gowers's rule is a gate *before* proving: *"a sufficiently simple
general statement that is not obviously true is almost certainly false."*

Arnold supplies the second half — control by examples continuously, not once at
the end — with the warning case `1, 2, 4, 8, 16, 29`: five terms of a doubling
sequence are consistent with several closed forms and the sixth is where they
part. Zeilberger supplies the third: random specialisation buys almost-certainty
for an epsilon of the cost, prices compose along a deduction, and a conclusion
is only as certain as the least certain thing it rests on.

Its most valuable move is often attacking another school's fresh claim rather
than starting something of its own.

## What they share

Per-team subtrees, shared ledgers, one board.

```
workspace/<problem>/
  teams/
    board.jsonl              append-only; any school appends
    BOARD.md                 derived; routed into every school
    <slug>/                  private working files
  research/                  SHARED — the nine derived ledgers
  code/                      SHARED — a verified helper is worth most to
                             the school that did not write it
  CONTEXT.md                 SHARED, still single-writer (the curator team)
```

The ledgers are safe to share without coordination because none of them is
edited: each is **derived by walking a one-file-per-item directory** and
re-rendered whole. Two schools writing distinct note files never conflict on
content. They would conflict on the *render*, which is what
[`worklock`](../src/orchestrator/worklock.rs) serialises.

### The board

Everything a school *establishes* already reaches the others through the
ledgers. That covers finished work, which is the smaller half of what a
collaborator wants. The larger half is the thing that is not a claim yet.

Gowers designed a collaboration around exactly this — *"just give quick
reactions"*, the ideal outcome being a solution *"with no single individual
having to think all that hard"* — and this runtime is built to refuse it. Every
ledger demands a well-formed block, and the scratch is deliberately unreachable
from durable recall so nothing unchecked can come back looking established.
[`methods-gap-analysis.md`](methods-gap-analysis.md) records the consequence as
**absent, deliberately**: no role can see another's provisional work at all.

That separation is right for a claim and wrong for a hunch. "The
generating-function route is dead, and here is what killed it" is worth nothing
after the run and everything during it — and it is the one thing none of the
other schools will discover for themselves.

Three controls keep it honest:

- **A post is asserted, not established.** `BOARD.md` is never an input to any
  derived ledger, and `post_board` has no way to make one. This is the
  `director` rule applied to a second source of unevidenced text: the director
  acts on what a human asserts and is deliberately denied `research/CLAIMS.md`,
  because a role holding the evidence ledger while reading an instruction is one
  prompt away from filing the instruction as a finding.
- **The sender is not an argument.** The posting school is baked into the tool
  instance at registration. A school that could name its own sender could
  attribute a hunch to a sibling, and a dead end is evidence only because the
  school that walked into it is the one reporting it.
- **The queue is append-only.** One `write_all` of one complete line on an
  append handle — the same construction, for the same reason, as
  [`src/directives`](../src/directives/mod.rs). Concurrent posters interleave
  whole lines and never halves of one, so no lock is needed and none is taken.

#### The board was built, wired, and never used

The first live three-school run — Project Euler 1006, `chisel`, `rising-sea` and
`adversarial` for eighty minutes — called `post_board` **zero times**. Nothing
was broken. All three schools reached a verdict, all three ran the reflection,
which is one of the three roles holding the tool, and `teams/` was never created
because nothing ever wrote to it.

Everything structural was correct and the gap was one layer up. The grant was in
the registry, `teams/BOARD.md` was routed into six roles' context, the tool
validated and appended — and **no prompt in the crate mentioned the board**.
`grep -c board` over `reflection.md`, `inventor.md` and `goals.md` returned
`0, 0, 0`. So the only trace of the board a model ever saw was an unexplained
entry in a tool list, inside a call whose instructions run thirty lines of
output format and end *"Answer exactly these four things"*. It answered the four
things. Three times, in three schools, correctly.

The lesson is the one this repository keeps recording, pointed the other way. A
prompt instruction is not a control — and a control nobody is instructed about
is not a capability. Registering a tool and asking for it are two different
acts, and only one of them had been done.

`src/prompts/board.md` is the brief that was missing. It is layered into the
three posting roles by `school_layer`, and **only when the run has siblings**:
a school running alone has nobody to tell, so paying for the brief in every one
of its prompts would buy an audience of one — and it would move the control off
the prompts this runtime sent before schools existed, which
`the_control_school_changes_no_prompt_by_one_byte` exists to prevent.

Two tests now hold the seam that was empty. One asserts that a role is told
about the board **exactly when** it holds `post_board` — both directions, since
a role instructed to post that cannot and a role that can post and was never
asked fail equally silently. The other asserts a lone school is never told.
Neither list can be derived from the other: the grants live in per-role
`&'static str` benches, so the agreement is asserted rather than read off an
authority.

What none of this proves is that a school now *does* post. That needs another
live run.

## Concurrency: the part that had to come first

Nothing in this runtime locked the workspace, and for a single loop that was
very nearly true enough. It was never quite true — fifty sub-agents may run at
once and every one carries the checkpoint middleware — and the evidence that it
was not is on disk: a live Erdős–Gyárfás workspace holds a stranded zero-byte
`.workspace-history/index.lock`, which is what two concurrent `git add` on one
index leaves behind. The commit that lost is reported nowhere, because the
checkpoint deliberately swallows its own failures rather than failing the tool
whose work succeeded.

Several schools turn that from a rare loss into the normal case, so
[`worklock`](../src/orchestrator/worklock.rs) came first. Two locks:

- `writes()` — held across a whole write-and-re-derive, so a second writer
  cannot interleave with the ledger cascade.
- `commits()` — held across the git checkpoint.

**The rule that keeps them from deadlocking: a lock is taken at a tool-call
boundary and never below one.** `tokio::sync::Mutex` is not reentrant, and a
note write re-derives six ledgers, each of which reads a directory and writes
through the same store. A lock taken at the leaf would be taken again by
everything above it and the run would stop. Per-file atomicity is a separate
mechanism and does not depend on the lock: writes go through a temporary file
and a rename, so a reader sees the old bytes or the new ones and never half of
each.

## How a run ends

First verified solve wins, and there is no scheduler.

- Each school runs its own loop to its own terminal condition.
- The first to reach a genuine `solved` cancels the others.
- `unverified` does **not** win — an answer with one route behind it is not a
  solve, which is what `UNVERIFIED_THRESHOLD` already exists to say.
- Otherwise every school runs to the shared wall clock and the outcome names
  what each reached.

## Deliberately not built

Recorded so it is not re-litigated.

**A cross-school budget scheduler.** The obvious next step, and
[`tao-gap-analysis.md`](tao-gap-analysis.md) is right about why not: funding the
branch that is not currently winning *"means running two lines of attack
concurrently and splitting budget between them, which changes what a run is
rather than adding an arm to it"* — and deciding which losing branch to fund is
a judgement the runtime has no way to make well. Equal fixed split.
[`tao-proposals.md`](tao-proposals.md) asks for the honest small version, a
*report* on how many distinct approaches a run pursued; that report is now a
by-product of the run having actually pursued them.

**Per-school workspaces or containers.** `workspace_from_env` asserts the
workspace resolves to exactly `/workspace`, and cross-process safety would need
real advisory locking, of which there is none anywhere in this repository.
Schools are in-process by construction. Two containers on one workspace remains
the silent failure it always was.

**Withholding `execute_command` from `rising-sea`.** Taking Gowers's
*"deliberately not allowing ourselves to exploit the speed of computers"*
literally, and it would be enforced the right way — by not registering the tool.
Declined on this repository's own evidence: Arnold wants computation
continuously as the only reliable control and Zeilberger's random specialisation
is the same mechanism, so the set is genuinely split and the runtime should not
pick a side on the strength of one subject.

**More than three schools.** Each costs a share of a shared model budget against
the same wall clock.

**Letting the board feed the claim ledger.** See the board's three controls
above.

**Per-school Cognee scoping.** Recall is per *workspace* today, so the schools
share it. That is consistent with sharing the ledgers, and separating it would
mean a school could not recall what a sibling verified — which is the opposite
of the point. `vector_store.rs`'s node-set scoping is the knob if that ever
turns out wrong.
