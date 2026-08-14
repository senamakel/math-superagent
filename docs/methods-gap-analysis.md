# What ten more mathematicians do that this runtime cannot

Ten mathematicians read the way [`docs/tao-gap-analysis.md`](tao-gap-analysis.md)
read Tao, set against what this runtime actually does — with the `file:line`
that shows it. The research is in
[`research/mathematicians/`](../research/mathematicians/): the conventions and
the schema (`00`), one file per subject (`01`–`10`), the runtime's capabilities
at branch HEAD (`11`), and the disagreements between them (`12`).

Read the Tao pair first. This is a second round against the same runtime and it
does not restate what that one found.

**Why ten more.** Five things were built out of reading Tao — `lean_check`,
`weakener`, `BANKED`, `searcher`, and Vampire with the `refuter` arm — and every
one is *chisel-side*: lower the target, attack the statement, hit the score
function again. Grothendieck's method would have produced none of them. The risk
in a one-subject study is that the runtime acquires that subject's taste along
with their method and has no way to tell which is which. The value here is the
disagreements.

**This round builds nothing.** There are no `[closed]` rows. The status
vocabulary is otherwise the Tao file's:

- **Absent** — nothing in the runtime does this.
- **Unenforced** — a prompt asks for it. A prompt instruction is not a control,
  so an unenforced rule is a rule the code stopped guaranteeing.
- **Unused** — the code produces it and nothing reads it.
- **Partly**, **Present** — as they read.

## The table

| The move | Source | What this runtime does | Status |
|---|---|---|---|
| Restate the goal in a different ambient category, keeping the goal fixed | `01`§A4, `06`§A4, `08`§A1, `09`§A6 | `inventor` re-routes to the goal, `reducer` finds sufficient lemmas, `weakener` lowers it. None moves the ground under it | **Absent** |
| Drop a hypothesis that no step below actually cites | `01`§A3, `03`§A10, `08`§A7 | `research/BACKWARD.md` records `rests-on` per gap (`backward.rs`), so an inherited hypothesis is detectable. Nothing looks | **Absent**, and computable today |
| Rank the *applicable moves* by how likely each is to appear in the final argument, and take the safest | `03`§A1 | `route()` (`solutions_attempt.rs:383`) routes on state — attempt count, verdicts. Nothing enumerates moves | **Absent** |
| Ban backtracking, and define the tractable class as what needs none | `03`§A2 | `Route::Retry` and `MAX_RESTARTS = 2` (`solutions_attempt.rs:91`). No notion of a subgoal that should need neither | **Absent** |
| Classify the subgoal *before* attempting: does a progress measure exist on partial arguments? | `03`§A5 | `reflection` answers `KIND: MATHEMATICAL \| COMPUTATIONAL` after the fact (`solutions_judging.rs:551`). Solvers and reasoners both present, no classifier | **Partly, backwards** |
| Gate a simple, general, not-obviously-true lemma to refutation *before* spending on a proof | `03`§A7, `09`§A2 | `refutation_arm` (`solutions_routing.rs:144`) runs on a cadence against gaps already committed to | **Partly** |
| Measure overshoot — did the run's output exceed its goal? | `01`§A2, `02`§A2 | `research/CLAIMS.md` scores a run discharging its goal identically to one discharging it plus four unasked questions | **Absent** |
| A place to record a believed statement with no justification | `07`§A1, `03`§A11 | Every ledger schema demands justification structure at write time; `note_scratch` is unreachable from durable recall by design | **Absent** |
| Extract the corrected statement from a refutation instead of filing it | `07`§B2, `04`§B1 | `refute.rs` files a verdict; `research/APPROACHES.md`'s `refuted` and `spent` are absorbing | **Absent** |
| Revive an abandoned approach when a *later* failure supplies what it lacked | `04`§B1 | Same absorbing states. Immunity is recorded per-approach and never re-examined | **Absent** |
| Estimate difficulty — of the goal, of a gap, of an approach | `02`§A3 | Nothing anywhere. Erdős's own thirty-year pricing was noise below \$500, which is the bar to beat | **Absent** |
| Target formal verification at what will be used as a black box | `08`§A2 | `blueprint.rs:44` derives the statement graph with standing as a minimum over `rests-on`. In-degree is the criterion and nothing reads it | **Unused** |
| Read an *explanation* out of a formalisation, not only a verdict | `08`§A6 | `lean.rs` (507 lines) parses compiled / `sorry` / `#print axioms` into a verdict. A boolean | **Absent** |
| Check that the formal statement encodes the intended mathematics | `09`§A5, `02`§B1 | `Status::Formalised` is gated on a passing kernel verdict (`claims.rs:132`). Whether the statement is the right one is unchecked — the runtime knows this failure only as `ContradictoryAxioms` in `refute.rs` | **Partly** |
| Carry derivation depth, or a composing price, on a claim | `06`§A1, `09`§A3 | `closure.rs:47` closes to a fixed point and reports standing. Depth is walked and discarded | **Absent**, one accumulator away |
| Record a claim's quantifier structure | `08`§A3 | `hypotheses` is a free-text field in a claim block | **Absent** |
| Control the derivation against instances *continuously* | `09`§A4, `06`§A2 | `SOLVED` requires a program on disk (`solutions_judging.rs:979`) — the check applied once, at the end | **Partly** |
| Bound a pattern before promoting it to a conjecture | `09`§B1 | `analyze_sequence` and `find_linear_recurrence` emit patterns with no refutation step | **Absent** |
| Decide that no closed form exists — Petkovšek beside the recurrence finder | `06`§A5 | `find_linear_recurrence` finds the recurrence and stops. A no-go is what `BANKED` was built to score | **Absent** |
| Score orientation — an attempt that mapped the objects and moved no goal | `04`§A1, `01`§A10 | `STUCK_THRESHOLD = 2` (`solutions_attempt.rs:8`) diversifies after two such attempts | **Absent** |
| Score legibility — can another role act on this derivation? | `05`§A1, `05`§B1 | `research/ROOT.md` is agent-written and read by no verdict. `CLAUDE.md` states this as the product standard | **Unenforced** |
| Publish the infrastructure separately from the theorem it was built for | `05`§B2, `10`§A1 | Workspace-local. Nothing writes a technique in terms that omit the motivating problem | **Absent** |
| Take a *named gap* from another run's decomposition as a goal | `10`§A1 | `research/BACKWARD.md` gaps carry `id`, `lemma`, `status` and a first move — already publishable, and readable only inside their own workspace | **Absent** |
| Post a half-formed contribution another role can see | `03`§A11 | `note_scratch`/`recall_scratch` is a separate vector dataset, unreachable from durable recall. That separation is correct and it is also why no role sees another's provisional work | **Absent, deliberately** |
| Distinguish a lookup from a derivation | `09`§A8 | `Status::Catalogued` exists and its doc comment carries the Project Euler 241 incident that motivated it | **Present** |
| Withhold the answer-lookup routes under research gating | — | `search_tools()` returns nothing when research is off, by not registering (`orchestrator_registry.rs:13`). **Except `download_document`**, still `document_tools[0]` at `:45-46` | **Partly** |
| Check the literature after a solve, on the reported answer and not the derivation | `01`§A9, `02`§A6 | `novelty_arm` (`solutions_routing.rs:201`) runs before the run is scored and cannot change the verdict | **Present** |
| One monotone statistic, about the mathematics | `10`§A2 | `state.scores` is pushed at `solutions_judging.rs:49` and read by serialisation only | **Unused**, unchanged since `../tao/03` |

## The four things all eleven agree on

Where the set does not split, the runtime has a requirement rather than a
choice. Four, from [`research/mathematicians/12-cross-cutting.md`](../research/mathematicians/12-cross-cutting.md):

1. **Enumerate the difficulties by name before choosing a method.** Nobody in
   the set starts by attempting the full statement. `attempt_step` does, and
   `weakener` runs on a cadence beside it rather than before it.
2. **A failed attempt carries information that must be extracted.** Four
   subjects, four mechanisms. `killed-by` may be empty and the refuted states
   absorb.
3. **The artefact worth optimising is the one a later worker can pick up.**
   Thurston has the negative result attached: he emptied his own field by
   writing for readers who shared his background.
4. **Scrutiny should scale with what rests on a claim.** `blueprint.rs` computes
   the in-degree that would supply the rule.

## The one thing this reading says about the thresholds

`MAX_ATTEMPTS = 8` and `STUCK_THRESHOLD = 2` are not only budget limits. They
are a *methodological commitment*, and nothing records that they are.

Grothendieck's rising sea requires many consecutive attempts that do not move
the goal — sixteen years, in his own case, with Deligne closing it (`01`§A10).
Wiles describes six months of bumping into furniture before the light switch
(`04`§A1). Scholze's Liquid Tensor theorem took eighteen months of formalisation
during which the theorem did not change (`08`§B2). Every one of those reads as
`STUCK` to this runtime after two attempts.

That is a defensible choice. It is not a recorded one, and the whole argument of
this repository is that an unrecorded decision defended by nothing is the
failure mode worth naming. Raising the thresholds is *not* the proposal — it
would only spend more budget on the same measurement. The proposal is in
[`docs/methods-proposals.md`](methods-proposals.md) #4: make orientation a
scoreable outcome, so that "the goal did not move" and "nothing happened" stop
being the same reading.

## Two documentation findings

Both verified against the working tree while writing
[`research/mathematicians/11-harness-inventory.md`](../research/mathematicians/11-harness-inventory.md),
which is §11 of that file.

- **`organizer` is residue.** It is not in `orchestrator_prompts.rs:116-141` and
  is not registered, yet `docs/roles.md` still gives it a tool-boundary
  paragraph (`:322`) and a routing row (`:349`), and `docs/workspace.md` makes it
  the actor in four arguments — including `:99-103`, where a live run's lesson
  is attributed to a role that no longer exists.
- **Neither Tao document is reachable from `AGENTS.md`.** The *Where the rest of
  this lives* list runs `roles`, `solution-loop`, `routing`, `runtime`,
  `workspace`, `ledgers`. `docs/tao-gap-analysis.md` and `docs/tao-proposals.md`
  do not appear, and by that file's own rule a document with no rule above it is
  a document nobody has a reason to open. This pair is added to the list in the
  same change that adds these two files.

The counts are *not* a finding: `AGENTS.md:23` and `docs/roles.md:3,52` already
say twenty-two roles, and `AGENTS.md:33` already says nine ledgers, both
matching the code. `research/tao/03-harness-inventory.md` is stale on both,
which is why `11` replaces it.
