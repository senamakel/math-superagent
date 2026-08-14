# Proposals: what to build next, ranked

Read [`docs/tao-gap-analysis.md`](tao-gap-analysis.md) first; this file is what
follows from it. Every entry names the Tao evidence, the gap, what to build,
where it lives, and roughly what it costs. The five at the top are **done on
this branch**; the rest are not, and the reasoning is kept here so that a later
decision starts from it rather than from nothing.

Ranking is by *value per unit of change*, not by importance. The single most
valuable change in this file is #6, and it is sixth because it is an
operational decision rather than a piece of code.

---

## Done on this branch

### 1. `lean_check` — make the kernel a control, not an instruction

**Tao:** formal verification is what removes trust as a prerequisite, which is
what let ~25 strangers formalise PFR in three weeks with the author writing ~5%
of the Lean (`02`§6). His stated failure mode for AI mathematics is the
plausible-but-wrong argument that "no human would have actually made that
mistake" (`04`§I.3).

**Gap:** Lean and Mathlib were the largest thing in the image and nothing ran
them. `research/CLAIMS.md` could not distinguish a kernel-checked lemma from a
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
ledger (`research/weakened/<slug>.md` → `research/WEAKENED.md`). It runs
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

## Not built

### 6. A shared technique library across problems

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

### 7. A cheap-first ladder with cost instrumentation

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

### 8. Closure of the claim set under implication

**EQT:** propagating each established fact through the entailment relation and
symmetry group gave ~37× more answers than direct proofs (`04` R5b).

**Gap:** `search_claims` retrieves a claim; nothing derives one. A claim ledger
that knows `A` and `A ⟹ B` does not know `B`.

**What to build:** the general version is a theorem prover over the ledger and is
too large. The narrow version is worth it on its own: a claim's `contradicts`
field is already parsed and rendered, so the same machinery could carry
`implies` edges and close over them transitively. That is a graph walk, not a
prover.

**Cost:** small for the transitive version, large for anything more.

### 9. Post-solve novelty check

**Tao:** `01`§19 — a short proof of a famous problem raises the prior that it is
already known. FunSearch's argument is that beating a numeric state of the art
is what distinguishes discovery from retrieval; its inverse is Erdős #728, where
an AI solution turned out to match Pomerance 2014 (`04` R33).

**Gap:** none of the three closing verdicts requires a literature check. A run
can close `SOLVED` having never asked whether the result is known.

**What to build:** a research delegation on the `Solved` and `Reported` routes,
before the outcome is written, recording what it searched and what it found. It
must not be able to *change* the verdict — a novelty check that can retract a
proof is a second judge — only to attach the record.

**Cost:** small, and it closes a real reporting risk.

### 10. Fund the orthogonal branch

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

### 11. Simplification as a mode

**Tao:** the sunflower cascade — ALWZ → Rao → Tao → Bell–Chueluecha–Warnke, four
rewrites in thirteen months against 59 years of near-stasis, and the extracted
spread lemma outlived the application (`02`§8 G1–G3).

**Gap:** the librarian acquires and the scholar digests. Nothing rewrites.

**What to build:** unclear, and that is the finding. This is the move in the set
that depends most on taste — "find the formalism in which the key inequality
becomes an identity" is not a schedulable action. Recorded because it is one of
the highest-yield moves in the sample and the runtime has no version of it, not
because a design follows.

### 12. Two fixes unrelated to Tao

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
what changed is that something now runs them. Three pieces of the PFR/EQT
infrastructure are *not* built and are worth knowing about: **Blueprint**, the
DAG of statements with a status per node that let strangers take independent
pieces (`research/BACKWARD.md` is flat by comparison); **`lean4checker` /
`lean4lean`** for kernel replay, a real concern at 22 million implications and
not one that bites at this scale; and **`gapt`**, Hetzl's machine-proof → sequent
calculus → Lean pipeline, which only pays off once ATP output is produced in
bulk.

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
- **The Dalmatian heuristic (Graffiti/TxGraffiti) — not yet.** Test whether a
  conjecture is *informative* before testing whether it is true; more than half
  of Graffiti was the triviality filter rather than the generator. An algorithm
  rather than a dependency, and it belongs on `pattern_finder`. This is the
  cheapest unbuilt item in this document.
- **Ramanujan Machine — declined.** Escalating numerical precision as the
  verifier. Worth borrowing its vocabulary rule — its authors tested to 2,000
  digits and still wrote that this "does not replace the need of a formal
  proof" — but not the machine.

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
