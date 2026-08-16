# Proposals: what to build next, ranked

Read [`docs/tao-gap-analysis.md`](tao-gap-analysis.md) first; this file is what
follows from it. Every entry names the Tao evidence, the gap, what to build,
where it lives, and roughly what it costs. The eight at the top are **done on
this branch**; the rest are not, and the reasoning is kept here so that a later
decision starts from it rather than from nothing.

Ranking is by *value per unit of change*, not by importance. The single most
valuable change in this file is #9, and it is ninth because it is an operational
decision rather than a piece of code.

The pattern in what got built is worth stating up front: three of the eight —
the statement graph, the entailment closure, and the assumed-axiom check — add
no role, no tool, and no file an agent writes. They are relations that were
already on disk and that nothing had ever followed, and each existed only as
prose asking a role to check for it. The cheapest large gains here were not
missing capabilities.

---

## Done on this branch

### 1. `lean_check` — make the kernel a control, not an instruction

**Tao:** formal verification is what removes trust as a prerequisite, which is
what let ~25 strangers formalise PFR in three weeks with the author writing ~5%
of the Lean (`02`§6). His stated failure mode for AI mathematics is the
plausible-but-wrong argument that "no human would have actually made that
mistake" (`04`§I.3).

**Gap:** Lean and Mathlib were the largest thing in the image and nothing ran
them. `derived/CLAIMS.md` could not distinguish a kernel-checked lemma from a
sentence claiming one.

**Built:** `src/orchestrator/lean.rs` — a tool that runs `lean`, parses
compiled/`sorry`/`#print axioms`, and files a verdict under `code/out/lean/`.
`Status::Formalised` in `claims.rs`, settable only against a passing verdict,
downgraded to `asserted` with a stated reason otherwise. Granted to
`lean_prover` alone.

**Cost:** ~330 lines plus 12 tests, and one line in a Lean file per theorem.

### 2. `weakener` — the third direction

**Tao:** "find a version of the problem that turns off nine of the difficulties
… and solve that" (`01`§1). Four of eleven programmes in `02` were solved by
weakening the target along a named axis; a fifth by weakening the *hypothesis*.

**Gap:** `reducer` asks what would be enough, `inventor` asks what other route
reaches the goal. Both hold the goal fixed.

**Built:** `src/prompts/weakener.md`, the role in the registry, and
`src/orchestrator/weakened.rs` — the difficulty ladder as a seventh derived
ledger (`research/weakened/<slug>.md` → `derived/WEAKENED.md`). It runs
concurrently with the reducer inside the existing reduction arm, sharing its
cadence, fingerprint gate, and single-writer gate.

**Cost:** ~830 lines plus 22 tests, and one extra child run per reduction
cadence.

### 3. `BANKED` — a partial or no-go result is a result

**Tao:** Greenfeld–Tao's 2021 rigidity result proved their encoding could not
work and is what sent them to the one that did (`02`§9). Two of eleven
programmes were preceded by an explicit no-go; one *was* the no-go.

**Gap:** `solved` was binary.

**Built:** a fourth reflection verdict, honoured only when
`claims::collect(workspace).established()` grew — so it cannot be asserted into
existence, and cannot keep a stuck run out of `diversify`. `route` does not read
it, so the routing policy and its parity harness are untouched.

**Cost:** ~40 lines plus 3 tests.

### 4. `searcher` — scored program search

**Tao / FunSearch / AlphaEvolve:** FunSearch moved the cap-set lower bound past
twenty years of work; AlphaEvolve matched or beat the literature on 20 of 67
problems (`04b`). Both evolve *programs that build the object*, not the object.

**Gap:** nothing here searched over programs. A construction was reasoned toward
or not found.

**Built:** `src/orchestrator/search.rs` — the island population, best-shot
prompting, the score ledger and the derived board, in Rust because they are
bookkeeping. `src/prompts/searcher.md` and a role whose authority is a set of
absences: no file-write tool, no shell, so `submit_candidate` is its only route
to disk and it scores what it writes in the same call. `score.py` is
unreachable, which is the AlphaEvolve verifier-exploitation finding turned into
a tool boundary. Two tests assert the absences.

**Cost:** ~700 lines plus 25 tests. No new dependency, no image change.

**What is deliberately not built:** PatternBoost. Its own authors write "machine
learning is hard!", it trains a transformer per problem, and requirement R36
from the same research says off-the-shelf over bespoke ML. FunSearch trains
nothing, which is why it is here and PatternBoost is not.

### 5. Vampire and the `refuter` arm

**Tao / EQT:** "spend the first ten minutes looking for a counterexample"
(`01`§10). The Equational Theories Project put a number on it: 524 small finite
structures refuted 13.6 million of 22 million implications, 13.3 million at size
3 alone, for 165 CPU-hours, before any clever proof search ran.

**Gap:** four proving roles, every one *delegated to*, none scheduled *against*
the statement being pursued.

**Built:** Vampire 5.1.0 in the image, pinned and smoke-tested in both modes —
its `--saturation_algorithm fmb` searches for a finite model, which is what
`eprover` cannot do and what answers a *false* conjecture instead of timing out
on it. `src/orchestrator/refute.rs` parses the SZS status into four findings and
files a verdict; `refuter` runs as a sixth evaluation arm against the open gaps
and the current weakened rung. A claim citing a refutation is checked against
the verdict, as a formalised claim is checked against the kernel. The role
writes files but has no shell, so it cannot hand-roll the search.

**Cost:** ~700 lines plus 22 tests, and ~55 MB in the image.

**The verdict that justified it:** `ContradictoryAxioms`. Everything follows
from contradictory hypotheses, so a broken axiomatisation proves the goal — the
way a bad encoding looks like a triumph. It was a prompt instruction to check
for; it is now a status the runtime reads.

---

### 6. `blueprint.rs` — the statement graph, and the closure over claims

**Tao:** `04` R2/R3 — a statement DAG with a status per node is what let ~25
strangers take independent pieces of PFR. EQT's `04` R5b is the other half:
propagating each established fact through the entailment relation gave about 37×
more answers than direct proofs — 597,582 facts closing into all 22,028,942
implications.

**Gap:** two, and they turned out to be one shape. `derived/BACKWARD.md` held
every dependency edge and drew none of them, so nothing could say which lemma
was ready to be picked up, and a decomposition proving its own hypothesis read
as two sound files. And `search_claims` retrieved a claim while nothing derived
one: a ledger holding `A` and "`B` follows from `A`" did not hold `B`.

**Built:** `src/orchestrator/blueprint.rs` derives `derived/BLUEPRINT.md` — a
node per goal, lemma and claim, a standing that is the minimum over what it
rests on, a **ready** list, and a cycle report above everything else because a
cycle invalidates what is below it. `src/orchestrator/closure.rs` derives
`derived/ENTAILMENT.md` from one new `follows-from:` field, closed to a fixed
point rather than one hop — stopping at one hop discards every sound step above
the first, which is most of the 37×. It reports what is established for free,
what the library already entails (the Dalmatian filter), and contradictions no
single block states. The graph reads the closure, so a free upgrade reaches the
ready list rather than dying in a file.

Neither adds a role, a tool, or a file an agent writes. Both are relations that
were already on disk and that nothing had ever followed.

**Refused in the strict direction, deliberately.** `asserted` never propagates,
and a claim supporting itself settles nothing — the permissive reading would
manufacture establishment from a chain of guesses, which is worse than having no
closure at all, because the run would stop looking.

### 7. The `novelty` node — check the literature *after* a solve

**Tao:** `01`§19 — a proof that arrived surprisingly quickly is far more often
already known, or wrong, than it is new. Erdős #728 is the live case: an AI
solution matching Pomerance 2014 (`04` R33).

**Gap:** the exact inverse was implemented. `open_library` returns early on
`state.solved`, so the one moment the literature was most worth reading was the
one moment nothing read it.

**Built:** a node between the loop's exit and the final judge. It asks whether
the result is published, whether the method used is the standard one, and
whether the run reaching it in that many attempts on that many claims is
plausible for a result of this size. It runs before the judge because "this was
published in 1974" is the most important thing the judge could be told.

It cannot un-solve the run. What it produces is a finding filed beside the
answer; a runtime that retracted its own verdict on a web search would be
trusting a query over a verified program.

### 8. The assumed-axiom check in `lean_check`

**Tao:** `04` R1 — a proof is what the kernel accepted.

**Gap:** `lean_check` caught a file that did not compile, one with `sorry`, one
printing no axioms, and one resting on `sorryAx`. It accepted a file declaring
`axiom key_estimate : …` and using it: compiles, warns nothing, prints its
axioms honestly, proves the theorem *given* something nobody established.

**Built:** a verdict fails on any axiom outside `propext`, `Classical.choice`
and `Quot.sound`, and names it so the role knows what to prove.
`Lean.ofReduceBool` is refused with them — `native_decide` trusts the compiler
rather than the kernel, and the whole argument for ranking a Lean result first
is that the kernel checked it.

This is the hole `lean4checker` is reached for, closed without a second binary;
see the toolchain survey for why the binary was the wrong answer.

## Not built

### 9. A shared technique library across problems

**Tao:** `01`§27 (archive everything); `04` R13. Mathlib is the mechanised form
of the argument, and the two fastest results in `02` — the sunflower rewrite and
PFR — both consisted of picking up existing output rather than starting cold.

**Gap:** `scripts/run-agent:110-126` gives each problem its own Cognee stack.

**What to build:** not a code change first. The decision is whether to run one
shared store, and the comment at that line records why the previous shared
arrangement was abandoned — four concurrent runs, a ten-minute `recall_memory`
hang, `409 Conflict`. `COGNEE_NETWORK` already opts back in, so the cheapest
honest experiment is to set it for two concurrent runs and measure recall
latency before writing anything. If it holds, the code change that follows is a
`remember_research` discipline: a claim worth carrying across problems is stated
without the problem's own notation.

**Cost:** an afternoon to measure; unknown to fix if it does not hold.

### 10. A cheap-first ladder with cost instrumentation

**Tao / EQT:** 22,028,942 implications went to ~1,000 by running finite model
builders and ATPs first, because they are "far cheaper to run and already
handled the overwhelming majority" (`04` R5).

**Gap:** an attempt is a model call that may delegate to a solver. Nothing
schedules the cheap rungs first, and nothing measures cost per resolved subgoal.

**What to build:** instrument first, schedule second. `RunTracer` already sees
every delegation; recording (role, wall-clock, tokens, whether the subgoal
closed) would say whether the ladder is worth building for this workload at all.
Building the scheduler before the measurement is the mistake `02`'s reading
warns about — reaching for computation before the problem is parameterised.

**Cost:** instrumentation small; the scheduler large, and only justified by what
the instrumentation says.

### 11. Fund the orthogonal branch

**Tao:** Polymath8's real lesson. Thirteen months drove 70,000,000 → 4,680;
Maynard reached 600 independently while discarding the machinery the effort had
gone into (`02`§7 F4).

**Gap:** the loop runs one line of attack and reaches `diversify` only after two
consecutive unproductive attempts. A run making thin but genuine progress every
cycle never diversifies at all — which the runtime already half-knows, since
`COMPUTATIONAL_THRESHOLD` exists precisely to catch a run scaling one method.

**What to build:** this one is genuinely hard and should not be attempted
casually. The honest small version is a report, not a mechanism: record how many
distinct approaches a run actually pursued, and surface a run that spent its
whole budget on one. Deciding to fund a losing branch is a judgement, and the
runtime has no way to make it well.

**Cost:** the report is small. The mechanism is a redesign of the loop.

### 12. Simplification as a mode

**Tao:** the sunflower cascade — ALWZ → Rao → Tao → Bell–Chueluecha–Warnke, four
rewrites in thirteen months against 59 years of near-stasis, and the extracted
spread lemma outlived the application (`02`§8 G1–G3).

**Gap:** the librarian acquires and the scholar digests. Nothing rewrites.

**What to build:** unclear, and that is the finding. This is the move in the set
that depends most on taste — "find the formalism in which the key inequality
becomes an identity" is not a schedulable action. Recorded because it is one of
the highest-yield moves in the sample and the runtime has no version of it, not
because a design follows.

### 13. Two fixes unrelated to Tao

Both are described in the gap analysis and neither is folded into this work.

- **`--no-research` does not withhold `download_document`**
  (`orchestrator_registry.rs:46`). A one-line move into the gated set, plus a
  test. Small, and it restores a control that reads as complete and is not.
- **The judge's score is written and never read** (`solutions_judging.rs:49`),
  and the judge runs once after the loop (`workflow.rs:56`). Recent and
  apparently deliberate; if it stays, the run has no monotone progress statistic
  anything acts on, which `01`§35 argues a long programme needs.

---

## The toolchain surveyed, including what was declined

Recorded so a later session does not re-litigate it. Every decline below has a
reason from the research rather than from taste, and two of them are the
projects' own calls.

**Provers and model builders.** The Equational Theories Project's roster is the
best-evidenced list available, since it is what took 22 million questions to
about a thousand: Vampire, E, Z3, Prover9/Mace4, and SAT inside the greedy
closure. We already had E, Z3, cvc5, MiniSat, CryptoMiniSat, CP-SAT, PySAT,
PuLP, CBC and GLPK. **Vampire was added** — its `--saturation_algorithm fmb`
does finite model building, which nothing else here could do and which is what
answers a false conjecture instead of timing out on it.

- **Prover9/Mace4 — declined.** The tool this job usually names, and the obvious
  reach. Debian dropped it, and Vampire's `fmb` covers what Mace4 was wanted
  for. Building it from a 2009 tarball to duplicate a capability we now have is
  not worth the build surface.
- **`egg` and `duper` — declined.** E-graph rewriting and a Lean superposition
  tactic. EQT confined both to forks and kept them out of its base repo; their
  judgement on this is better evidenced than ours and following it costs
  nothing.

**Formalisation.** Lean and Mathlib were already the largest thing in the image;
what changed is that something now runs them.

- **Blueprint — adopted as an idea, not as a tool.** Massot's DAG of statements
  with a status per node is what let ~25 strangers take independent pieces of
  PFR in three weeks. The tool itself is a LaTeX/Lean build pipeline and would
  be the wrong shape here, where the statements live in Markdown blocks that
  code already parses. `derived/BLUEPRINT.md` is the same idea derived from the
  ledgers that already held the edges, and it adds no file for an agent to write.
- **`lean4checker` / `lean4lean` — declined, and the hole closed another way.**
  Kernel replay needs a build against the exact toolchain, which makes it an
  *optionally present* control, and an optional control is not one. The failure
  it is usually reached for here is simpler and far likelier anyway: a file
  declaring its own `axiom` compiles, warns nothing, prints its axioms honestly,
  and proves the theorem given something nobody established. `lean_check` now
  fails any verdict resting on an axiom outside Lean's own three, and names it.
- **`gapt` — declined for now.** Hetzl's machine-proof → sequent calculus → Lean
  pipeline. It needs a JVM in the image and substantial glue, and it only pays
  off once ATP output is produced in bulk. The *connection* it represents — an
  ATP result should land as checked Lean rather than as a claim — is worth
  building before the tool is.

**Search and discovery.** Here the transferable thing is almost never the code.

- **FunSearch — architecture adopted, code unused.** It trains nothing, which is
  the distinction that matters; see #4.
- **AlphaEvolve — unavailable, finding adopted.** Its verifier-exploitation
  result is what makes the searcher's write boundary a tool boundary.
- **PatternBoost — declined.** It trains a transformer per problem. Its own
  authors write "machine learning is hard!", and R36 from the same research says
  off-the-shelf over bespoke ML, so wiring it would contradict the finding that
  surfaced it.
- **AlphaProof, AlphaGeometry — declined.** Not released usably.
- **The Dalmatian heuristic (Graffiti/TxGraffiti) — adopted.** Test whether a
  conjecture is *informative* before testing whether it is true; more than half
  of Graffiti was the triviality filter rather than the generator. An algorithm
  rather than a dependency, and it turned out to belong in `closure.rs` rather
  than on `pattern_finder`: "already entailed by the library" is the same
  computation as "established for free", read in the other direction.
- **Ramanujan Machine — declined, vocabulary already enforced.** Escalating
  numerical precision as the verifier; its authors tested to 2,000 digits and
  still wrote that this "does not replace the need of a formal proof". The rule
  was worth borrowing and the claim ledger already carries it: `checked` means
  this run verified it numerically and is a different status from `proved`,
  which is a statement about a source, and from `formalised`, which is the only
  one the ledger does not take on trust.

**The pattern.** Of everything surveyed, exactly one binary was missing. Tao's
own slide title for modern ML's contribution to EQT was *the dog that did not
bark*: the work was done by automated theorem provers, which "were far cheaper
to run and already handled the overwhelming majority". A runtime reaching for a
new dependency should check first that it is not reaching past one it has.

## What the research says about all of this

Two readings from `02`'s ladder statistics are worth keeping in front of anyone
picking from this list.

**Programme length is unrelated to problem age.** An 83-year-old problem took
5.5 years; a 59-year-old one took a month of rewriting. What predicts a solve is
not effort on the frontier but *the arrival of an external tool* —
Matomäki–Radziwiłł for the discrepancy problem, ALWZ for sunflowers. For this
runtime that argues for #4 and #5 over #9: being able to pick up a new tool
cheaply beats being able to grind harder.

**Computation was decisive in exactly one of eleven cases and decorative in most
of the rest.** Where it mattered it was the endgame of an already-parameterised
problem. The 13 GB SAT certificate for the Erdős discrepancy problem settled one
value of `C` and generalised to nothing. A runtime whose instinct is to compute
should read that as a warning about its own default.
