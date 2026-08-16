# Proposals from the ten-mathematician study, ranked

Read [`docs/methods-gap-analysis.md`](methods-gap-analysis.md) first; this file
is what follows from it, and it presupposes
[`docs/tao-proposals.md`](tao-proposals.md) rather than repeating it.

Ranking is by **evidence weight per unit of change**, not by importance. The
top of the list is where more than one subject converges on a change that is a
graph walk over a ledger the runtime already derives. Nothing here is built;
this round wrote research.

Each entry: **Evidence** (which subjects, with section references into
[`research/mathematicians/`](../research/mathematicians/)), **Gap** (with the
`file:line`), **Build**, **Cost**, and where it applies, **What is deliberately
not built**.

The surfaces a proposal may target, in order of leverage over effort:
`src/prompts/method_policy.md`, which leads every prompt in every role and must
stay first because the provider cache is keyed on the prefix; the per-workspace
`prompts/<role>.md` overrides, live today in
`workspace/conjectures/erdos-gyarfas/prompts/`; the role prompts themselves; and
the ledger block schemas in `claims.rs`, `approaches.rs` and `backward.rs`,
where adding a field is how a heuristic stops being requested and starts being
mechanically checkable.

---

## 1. The inherited-hypothesis check

**Evidence:** three subjects, three routes to the same walk. Grothendieck:
Serre thought the rings "should meet some conditions, at least be Noetherian",
and Grothendieck's originality "was that no one but him thought it could work in
all generality" (`01`§A3). Gowers ranks moves by what they *close off*, and
gives expanding a definition a low priority because it is irreversible
(`03`§A10). Scholze reports that the Liquid Tensor simplification came from
Commelin being forced to state exactly which properties the Breen–Deligne
resolution's use actually consumed (`08`§A7).

**Gap:** `research/BACKWARD.md` records `rests-on` per gap (`backward.rs`), so a
hypothesis that no step below cites is already detectable from data on disk.
Nothing looks.

**Build:** a derivation-time report over the existing skeleton/gap graph: for
each hypothesis on a goal or lemma, whether any node below it cites that
hypothesis. Rendered into `research/BLUEPRINT.md`, which already walks this
graph and already reports cycles above everything else.

**Cost:** small. One walk over a structure `blueprint.rs` builds, plus tests. No
new role, no new tool, no file an agent writes — the same shape as the three
cheapest things built on this branch.

**Why it is first.** It is the mechanism `docs/tao-proposals.md` #11 says it
lacks. That entry records simplification-as-a-mode as one of the highest-yield
moves in the Tao sample and concludes "unclear, and that is the finding".
Scholze supplies the answer: simplification is a *by-product of being forced to
name the hypotheses actually used*, not an act of taste.

## 2. Formalisation targeting off the blueprint's in-degree — **built**

**Evidence:** Scholze's stated criterion for what to formalise — "As it will be
used as a black box, a mistake in this proof could remain uncaught" — and his
own calibration evidence against himself: a proof of weight-monodromy that
"passed judgment of top mathematicians, but then it turned out to contain a
fatal mistake" (`08`§A2). Perelman is the cost estimate for the absence: five
years and three independent teams (`10`§A3).

**Gap:** `lean_check` is granted to `lean_prover` and what gets formalised is
whatever that role decides to formalise. There is no priority order.

**Build:** `blueprint.rs:44` already derives a node per goal, lemma and claim,
with standing as the minimum over what it rests on. In-degree over that graph
*is* Scholze's criterion. Render a "verify these first" section: high in-degree,
standing below `Formalised`.

**Cost:** very small — a sort over a graph already built, and a section in a
file already written.

**Built as `Blueprint::targets`, `orchestrator::verify`, and the `eval_verification`
arm.** The sort and the section came in as described. What the estimate missed
is that a priority order buys nothing while the tool it prioritises is only ever
*delegated to* — the gap above says "there is no priority order", and the larger
half of the gap was that there was no scheduled caller either. So the arm is the
build: one target per pass, ranked; a second pass on a node that failed asks for
a decomposition rather than another proof; two attempts and it moves on.
[`solution-loop.md`](solution-loop.md) has the three decisions and what each
costs. One pre-existing fault fell out of writing the tests: an entailed
`formalised` claim had its `Verified` standing overwritten with `Established`,
so the kernel would be sent back to re-check what it had already accepted.

## 3. Repair the refuted statement instead of filing it

**Evidence:** the one measured case in the directory. Berndt, Dixit, Roy and
Zaharescu, *New pathways and connections in Number Theory and Analysis motivated
by two incorrect claims of Ramanujan* — two identities on page 336 of the lost
notebook, both "vitiated by divergent series", which ninety-six years later
produced corrected convergent formulations, a generalisation of the Voronoi
summation formula, and a new class of integral transforms (`07`§B2). Wiles is
the second instance in a different key: the Iwasawa approach abandoned in 1991
was completed by what the Kolyvagin–Flach failure taught, and he called that
"the most important moment of my working life" (`04`§B1).

**Gap:** `refute.rs` parses an SZS status into four findings and files a verdict.
`research/APPROACHES.md`'s `refuted` and `spent` are absorbing states nothing
revisits.

**Build:** before the refuter writes its verdict, one further question — what is
the nearest statement the counterexample does *not* kill, and which hypothesis,
convergence condition or quantifier had to change. File that as a new claim at
`asserted`.

**Cost:** small — a prompt change on `refuter` plus one schema field.

**What is deliberately not built:** an automatic revival loop over *all* dead
approaches. Wiles's revival was driven by a specific diagnosis, and the
unconstrained version is a loop that retries old ideas forever. The guard on the
repair is likewise stated: the repaired statement must still entail something
the run wanted, or the loop weakens statements until they are vacuous.

## 4. Make orientation a scoreable outcome

**Evidence:** four subjects whose central work is invisible to a goal-reading
statistic. Wiles's dark mansion — "after six months or so, you find the light
switch" (`04`§A1). Grothendieck's rising sea, in which "nothing seems to happen,
nothing moves" (`01`§A1), and his own case ran sixteen years with Deligne
closing it (`01`§A10). Scholze's eighteen months of formalisation during which
the theorem did not change (`08`§B2). Thurston's foliations period.

**Gap:** `STUCK_THRESHOLD = 2` (`solutions_attempt.rs:8`) sends a run to
`diversify` after two unproductive attempts, and an attempt that built
definitions, worked examples and a map of the objects produces no claim,
discharges no gap, and reads as unproductive to every derived ledger.

**Build:** *not* a higher threshold — that spends more budget on the same
measurement. A distinct outcome: an attempt that added definitions or worked
examples without moving the goal is recorded as such, and `research/THREADS.md`
is where it shows. Whether it should reset `unproductive` is the real design
question and should be decided the way `BANKED` was: honoured only against
something read off disk, so it cannot be asserted into existence.

**Cost:** medium, and it touches the routing policy, so `orchestrator::parity`
must stay green.

**The risk, stated:** this is the proposal most likely to let a stuck run keep
itself out of `diversify` forever by claiming orientation every cycle. That is
exactly the failure `COMPUTATIONAL_THRESHOLD` exists to close for one verdict,
and the same discipline applies.

## 5. Derivation depth on a claim

**Evidence:** Arnold — "The longer and fancier is the chain of deductions
('proofs'), the less reliable is the final result" (`09`§A3). Zeilberger's
priced theorems are the constructive form of the same idea, and they compose:
"Whenever statement A, whose price is p, and statement B, whose price is q, are
used to deduce statement C, the latter becomes a priced theorem priced at p + q"
(`06`§A1).

**Gap:** `closure.rs:47` closes the ledger under `follows-from` to a fixed point
and reports standing. It walks depth and discards it, so a claim established at
depth twelve and one established at depth one render identically.

**Build:** carry a maximum depth along the same walk that already folds standing
as a minimum. Render it beside the claim in `research/ENTAILMENT.md`.

**Cost:** very small — one accumulator on an existing fixed-point walk.

**What is deliberately not built:** Zeilberger's full numeric price. What price
*means* for a runtime is a real question — model calls, kernel acceptance,
independent routes, unverified links in the chain — and it should not be
answered by analogy. Depth is the honest first version, and Zeilberger himself
predicts the decay: "Most likely we will wind up abandoning the task of keeping
track of price altogether" (`06`§A7). A price that is not visible at the point of
use decays into a licence.

## 6. A refutation gate before a proof attempt

**Evidence:** Gowers's working assumption — "make the working assumption that a
sufficiently simple general statement that is not obviously true is almost
certainly false" (`03`§A7), motivated by Reiter's model-pruning: "before we
invest time in proving a statement, we like to feel that that statement has at
least some plausibility". Arnold places the counterexample hunt *between*
observation and formulation (`09`§A2), with `1, 2, 4, 8, 16` — "but then comes
29" as the case.

**Gap:** `refutation_arm` (`solutions_routing.rs:144`) runs on a cadence against
open gaps and the current weakened rung — that is, against statements the run is
already committed to proving. Separately, `analyze_sequence` and
`find_linear_recurrence` emit patterns with no refutation step at all.

**Build:** route a *newly proposed* gap to the refuter before any proof effort,
when it is simple, general and not already believed. Every new gap goes through
one place in `backward.rs`, so this is a routing change rather than a new
capability.

**Cost:** small for the gap gate; small for the pattern gate, which is the
higher-value half and is currently unguarded.

## 7. A move ladder ordered by safety

**Evidence:** Ganesalingam–Gowers, in full. "the program prefers safe moves to
dangerous moves … we have to make an assessment of how likely any given choice
is to form part of the argument one is looking for" (`03`§A1), applied greedily
over a fixed list of move types, chosen by introspection before the test
problems and not modified afterwards. This is also `../tao/04` R5's cheap-first
ladder, reached from a different tradition and with a better ordering principle:
probability of appearing in the final argument rather than cost.

**Gap:** `route()` (`solutions_attempt.rs:383`) routes on *state*. An attempt is
a model call that decides for itself what to try, so the ordering exists and is
made silently, per turn, by the model.

**Build:** large, and it should be instrumented before it is scheduled — which
is `docs/tao-proposals.md` #7's conclusion reached independently. `RunTracer`
already sees every delegation; recording (role, wall-clock, tokens, whether the
subgoal closed) would say whether the ladder is worth building for this
workload.

**Cost:** instrumentation small; the ladder large.

**What is deliberately not built, for now:** Gowers's ban on backtracking
(`03`§A2). It is the cleanest scoping move in the directory and it presupposes
the ladder — without an ordering there is nothing for the ban to protect.

## 8. Petkovšek beside the recurrence finder

**Evidence:** Zeilberger — if the recurrence a sum yields is of order above one,
"most likely the sum is not explicitly-evaluable (in closed form), and
Petkovsek's algorithm … can be used to find out for sure" (`06`§A5).

**Gap:** `find_linear_recurrence` finds the recurrence and stops. "There is no
closed form, stop looking" is a **no-go result**, which is precisely what
`BANKED` was added to score.

**Build:** a named, implementable algorithm on `pattern_finder`. Not a new
dependency — the symbolic stack is in the image.

**Cost:** small to medium, and it is the only proposal in this file that turns a
heuristic into a decision procedure.

## 9. Read an explanation out of the kernel, not only a verdict

**Evidence:** Scholze, asked whether he learned any mathematics during the
formalisation: "What actually makes the proof work! When I wrote the blog post
half a year ago, I did not understand why the argument worked" — and the thing
he learned was that "the key thing happening is a reduction from a non-convex
problem over the reals to a convex problem over the integers" (`08`§A6). He had
spent a year on the proof and it had not come.

**Gap:** `lean.rs` parses compiled / `sorry` / `#print axioms` and files a
verdict. A boolean. `research/ROOT.md` — "what the library means" — is the
nearest place for such a sentence and is not connected to the Lean verdict at
all.

**Build:** require the `lean_prover`, on a passing verdict, to state which step
the argument turns on and file it beside the verdict.

**Cost:** small.

**The honest caveat:** this rests on one first-person report, reached through a
summarising fetch. `lean_check` should not be re-justified on it. A *targeting*
rule (#2) has better support than this does.

## 10. A conjecture store, with a consumer

**Evidence:** Ramanujan — over six hundred formulas without proofs, and Berndt's
collaborators found that well over half were new (`07`§A1, §A2). Arnold, on
being taught Riemann-surface facts as a first-year student: "even given without
any proofs) they give a better and more correct idea of modern mathematics than
whole volumes of the Bourbaki treatise" (`09`§A7).

**Gap:** every ledger schema demands justification structure at write time, and
`note_scratch` is deliberately unreachable from durable recall. So the runtime
cannot answer "has this run produced any statements it believes and cannot yet
justify?" — the answer is always no, by construction.

**Build:** three parts, all mandatory or none. A store unreachable from anything
that derives an established ledger. The generator's promotion rate recorded from
the first run, which is derivable if a claim carries its origin. And a
*consumer*: the refuter arm, run against the store rather than only against the
current statement.

**Cost:** medium.

**Why it is tenth despite strong evidence.** Ramanujan's notebooks were useless
for ninety years except as a work queue, and Berndt's five volumes ran 2005–2018
(`07`§A5). A store without a consumer is a landfill, and the consumer is the
expensive half. `../tao/04b`'s Dalmatian heuristic — test whether a conjecture
is *informative* before testing whether it is true — is the filter this needs
and is still the cheapest unbuilt item in `docs/tao-proposals.md`. Build that
first.

## 11. Cross-workspace gaps

**Evidence:** Perelman took Hamilton's publicly stated gap and adopted the
programme's machinery wholesale rather than auditing it (`10`§A1). Thurston
argues for publishing the infrastructure *ahead of* the theorem, in terms that
do not mention the motivating problem (`05`§B2). Erdős's catalogue is the same
thing with status and price attached (`02`§A6).

**Gap:** `research/BACKWARD.md` gaps already carry `id`, `lemma`, `status` and a
first move a `tool_builder` could run today — a publishable work item, inside a
directory nothing outside the workspace reads.

**Build:** not a code change first. This is `docs/tao-proposals.md` #6 — the
shared technique library — arriving from a fourth direction, and #6's own
conclusion holds: the decision is operational, the cheapest honest experiment is
to measure recall latency under `COGNEE_NETWORK` for two concurrent runs, and
the code change only follows if that holds.

**Cost:** unknown, and gated on #6's measurement.

---

## Declined, with reasons from the research

Recorded so a later session does not re-litigate them.

**Raising `MAX_ATTEMPTS` or `STUCK_THRESHOLD`.** The obvious response to
Grothendieck, Wiles and Scholze, and it is wrong. It spends more budget on the
same measurement. The problem is that "the goal did not move" and "nothing
happened" are the same reading, which is #4.

**A `simplifier` role.** The obvious response to `../tao/02`'s sunflower cascade
and to Thurston. Scholze's evidence says the simplification did not come from
someone deciding to simplify; it came from being forced to state which
properties the argument uses (`08`§A7). That is #1, and it costs a graph walk
instead of a role.

**Withholding `execute_command` for the first `n` attempts.** Gowers's "extreme
human" constraint taken literally (`03`§A3), and it would be enforced the right
way, by not registering the tool. Declined because it contradicts the other
half of the evidence: Arnold wants computation *continuously* as the only
reliable control (`09`§A4), and Zeilberger's random specialisation is the same
mechanism (`06`§A2). The set is genuinely split and the runtime should not pick
a side on the strength of one subject. What survives is the *distinction* — the
runtime does not tell goal-directed reconnaissance apart from undirected
exploration, which is #10's territory.

**A numeric price on claims.** See #5. Depth first; price is a design question
about what a runtime's certainty costs, and Zeilberger's own prediction is that
an unenforced price decays into nothing.

**Anything resting on the "dark mansion" quotation alone.** It is the most-quoted
Wiles line in existence and this study reached it at two removes, via Oort
quoting a 1996 BBC documentary. #4 is supported by Grothendieck and Scholze
independently and does not need it.

**Deceiving the model about the mathematics.** `02`§B1 records that GPT-5.2
refused open problems it recognised and had to be told the problem was a
competition exercise. The framing change is worth considering — the runtime
volunteers "this is a hard open problem" in prompts, which has no bearing on the
argument and a measured effect on the effort — but any version that alters the
*statement* is out. This one is flagged rather than proposed, because it is a
one-participant anecdote and the runtime's own evidence for it is nil.
