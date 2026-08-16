# Shared context

What this run knows, in its own words. The context curator writes this file and
is normally the only role that writes it; the director amends it on a directive
that changes what every role should know. Nearly every other role is sent it on
every model call. So what is here is what the run knows without going to look,
and what is missing is what each agent rediscovers separately.

It carries what an agent would otherwise rebuild from disk, from the note store,
or from a session it was not present for: established results with their basis,
approaches that died and why, what the computed numbers look like, what durable
memory relates this problem to, and where two accounts disagree. It is not a
catalogue of files — `research/INDEX.md` is that — and not a narration of what
agents did.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). The
file is re-sent on every model call in every role that reads it, so length here
is a bill the whole run pays many times over; a brief past its budget is cut
where it exceeds it on the way into a prompt, with a notice saying so. Link the
file that still holds any detail compressed away — source notes under
`research/summaries/`, untouched full texts under `research/sources/`,
reflections, threads. Durable findings belong in Cognee. A statement nobody can
trace to a source is worth less than no statement.

## Established

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it. Each belief names
what would falsify it.

- **Exact values ES(3..6) = 3, 5, 9, 17.** ES(3)=3 (any 3 non-collinear points);
  ES(4)=5 (Klein's 1930s proof from 5 points); ES(5)=9 (Makai/Turán; Bonnice and
  Lovász hand proofs via the (3,3,2)/(4,3,1)/(3,4,2) lemma); ES(6)=17
  (Peters–Szekeres 2006 computer proof, SAT/backtracking on signature functions).
  *Evidence:* proved (hand) for n≤5, verified-numerically for n=6.
  *Falsified by:* an exact orientation table of 9 points with no convex pentagon,
  or of 17 points with no convex hexagon. `research/ROOT.md` §3.

- **Lower bound and its realizability.** ES(n) ≥ 2^{n-2}+1: blocks T_0..T_{n-2}
  with |T_i| = C(n-2,i), each free of an (i+2)-cap and (n-i)-cup with slopes
  bounded by 1 in absolute value, placed near circle angles θ_i = π/4 − iπ/(2(n-2)).
  Largest convex subset has ≤ n-1 points. Realizable with integer coordinates in
  grid size O(n² log³ n) (Duque–Fabila-Monroy–Hidalgo-Toscano, arXiv:1602.03075).
  *Evidence:* proved. *Falsified by:* a convex n-subset found by an exact
  orientation table in any realization. `research/ROOT.md` §2.

- **Tóth–Valtr binomial bound.** ES(n) ≤ C(2n-5, n-3) + 2. *Evidence:* proved
  (1998). Exact-form, but far above the conjectured 2^{n-2}+1 — it does not
  resolve the constant. *Falsified by:* an n-avoiding set of size
  > C(2n-5,n-3)+2. `research/ROOT.md` §1.2.

- **Asymptotic upper bounds — NOT bearing on the exact conjecture.** Suk:
  ES(n) ≤ 2^{n + 6n^{2/3} log n} for n ≥ n₀ (n₀ a large absolute constant).
  Holmsen–Mojarrad–Pach–Tardos: ES(n) ≤ 2^{n + O(√(n log n))} (current best).
  Both are of the form 2^{n+o(n)}: **asymptotic**, so they cannot settle the exact
  constant ES(n)=2^{n-2}+1. *Evidence:* proved. *Falsified by:* a set violating
  the stated inequality — but as asymptotics they are recorded as context, not as
  tools for the exact conjecture. `research/ROOT.md` §1.4–1.5.

- **Baek–Balko split/decomposable result.** ES_split(k) = 2^{k-2}+1 proved
  exactly (tight threshold for split k-gons); the conjecture holds for
  decomposable sets; the ordered 3-uniform hypergraph generalization is false.
  *Evidence:* proved (SoCG 2025). *Falsified by:* a split-k-gon-free set of size
  2^{k-2}+1, or a decomposable set of 2^{k-2}+1 points with no convex k-gon.
  `research/ROOT.md` §5.1.

- **Cups-and-caps tightness.** f(k,l) = C(k+l-4, k-2) + 1 exactly, and
  ES(n) ≤ f(n,n) = C(2n-4, n-2) + 1. *Evidence:* proved (Erdős–Szekeres 1935;
  tightness per Morris–Soltan). *Falsified by:* a set of f(k,l) points with
  neither a k-cup nor an l-cap. `research/ROOT.md` §1.1.

- **4-point criterion (oracle backbone).** A finite set in general position is in
  convex position iff every one of its 4-subsets is. *Evidence:* proved
  (Erdős–Szekeres 1935). *Falsified by:* a convex set with a non-convex 4-subset,
  or the reverse. Underpins the phase-3 oracle. `research/ROOT.md` §6.

- **Signotope / CC-system foundation (the SAT arm's axioms).** Rank-3 signotopes
  (triple-orientation sign maps with at most one sign change per 4-set) are in
  bijection with simple pseudoline arrangements with a fixed top cell (Felsner &
  Weil 2001); a triple orientation is such an arrangement exactly iff it obeys
  the generalized transitivity law; a realizable point set = a stretchable
  (straight-line) arrangement, and realizability is ∃ℝ-complete
  (Goodman–Pollack–Sturmfels). The CC-system axioms (Knuth: cyclic symmetry,
  antisymmetry, nondegeneracy, interiority, transitivity) are the exact axioms
  the orientation-variable SAT encoders (SMQH, Dumitru, Scheucher, Balko–Valtr)
  post. Abstract CC systems count ~exp(n²) vs ~exp(Θ(n log n)) realizable ones —
  the quantitative realizability trap. *Evidence:* proved (Felsner–Weil primary;
  the CC-system axiom/count statements are asserted-by-secondary-source, Knuth via
  Wikipedia). *Falsified by:* a rank-3 signotope with one sign change per 4-set
  whose marked arrangement is not simple; or a realizable order type failing a
  CC axiom. `research/summaries/felsner-weil-sweeps-arrangements-signotopes-2001.md`,
  `research/summaries/wikipedia-cc-system.md` (claims `fw-rank3-signotope-pseudoline`,
  `cc-system-axioms`).

## Ruled out

Approaches that failed, and the reason each failed — plus what is excluded from
counting as progress.

- **Empty-hexagon and higher-dimensional SAT results are adjacent problems, not
  progress.** H(6)=30 (Heule–Scheucher) and the higher-dimensional
  acyclic-chirotope SAT numbers concern different questions; they do not bear on
  ES(n) and are kept out of Established. Recorded as context only in
  `research/ROOT.md` §5.4–5.5.
- **The even/odd block bipartition is not a line-separability obstruction.**
  `gsplit_line.py` found the even- vs odd-index blocks of `es_construct` not
  strictly line-separable; that is a property of this one realization, not a
  refutation of G-split (a valid radial placement exists per the literature). The
  genuine question is the exhaustive any-line test, task
  `gsplit-exhaustive-line-test`.
- **Steering rule in force (steer 4): no new sources.** Phase 1's exit test is
  met; gathering is admissible only against a stated gap in
  `research/REQUESTS.md`. The pending computation must be run first.

## Numbers

- ES(3..6) = 3, 5, 9, 17.
- Lower-bound construction sizes at n=5,6,7: 8, 16, 32 points (2^{n-2}).
- **GOAL.md criterion 3 (oracle) is met**: `lib/es_geom` passed its self-test on
  hand-known sets and `lib/es_construct` is verified (largest convex = n−1 at
  n=4,5,6; no convex 7-gon at n=7) by two independent hull algorithms. Captures:
  `code/out/checker_vs_construction_resolution.md`, `code/out/verify_es_construct.py`,
  `code/out/verify_es_construct_indep.py` (see `build-oracle` close reason).
- `es_construct` convex-layer profiles (hull peeling, exact): n=4 [3,1],
  n=5 [4,4], n=6 [5,5,3,3], n=7 [6,6,6,5,6,3]. The n=6,7 profiles are the
  steering-named data for the layer-profile conjecture (steer 4 item 4).

## Recalled

Nothing promoted from durable memory yet. Fill this section from `recall_memory`
before relying on any cross-run finding.

## Contradictions

- **Resolved: the run's ES construction was defective, not the checker.** The
  checker `lib/es_geom` is correct (survives every hand-known set); the defective
  realizations were `es_construction.es_lower_set`, `es_lower.py`, and `esz.py`.
  `es_construct.py` is the verified 2^{n-2}-point no-convex-n-gon construction
  (largestConvex = n−1 at n=4,5,6; no convex 7-gon at n=7), checked by two
  independent hull algorithms. The three other construction modules are
  **quarantined — do not import them** (see `code/lib/INDEX.md`). Resolution:
  `code/out/checker_vs_construction_resolution.md`.

## Gaps

What the run still needs and has not found.

- **STEERING — scored program search is now the head of the queue (steer 6).**
  The work to do next is the scored search under `code/search/es-nogon`: tool_builder
  writes `PROBLEM.md` + `score.py` against the VERIFIED `lib.es_geom` orientation
  predicate (the searcher must NOT write the scorer); run the k=6 rung first and
  confirm it caps at exactly 16 before touching k=7; then run ≥50 k=7 candidates
  and report the score distribution, which constraint binds, and whether the top
  score is believed. 32 reproduces the known `es_construct` construction; 33+
  refutes ES(7)=33 and must be re-verified independently before being reported.
  The pending `gsplit_exhaustive.py` capture and the construction quarantine /
  layer-profile conjecture remain queued behind it, not abandoned.

- **Exhaustive line-split test of es_construct (task `gsplit-exhaustive-line-test`).**
  `gsplit_line.py` checked only the even/odd block bipartition (each half is
  2^{n-3} and (n-1)-avoiding at n=5,6,7, but NOT strictly line-separable) — a
  dead guess, not an obstruction. Open: does ANY line split the verified
  `es_construct` set into two (n−1)-avoiding halves at n=5,6,7? Starter
  `code/out/gsplit_exhaustive.py` is written but **its run is not yet captured**;
  verify its bipartition enumeration (C(N,2) pair-lines × on-line assignments)
  before trusting its output. An empty result would rule out the split reduction
  `f(n) <= 2f(n-1)` for THIS construction at THESE n — not for all extremal sets.
  State in `code/out/gsplit_state.md` (claims `gsplit-even-odd-not-line-separable`,
  `gsplit-exhaustive-pending`).
- **Balko–Valtr SAT encoding still only at DOI/abstract.** Needed to reproduce
  ES(5)=9 / ES(6)=17 with our own encoder. Filed as `balko-valtr-attack-baa4` in
  `research/REQUESTS.md`.

## The ledgers, and how to reach them

This workspace keeps its state in **ledgers** — the task list, the sub-goals,
the claims, the approaches, the threads, and any axis this run has added for
itself. `list_ledgers` names every one and says what it holds.

**The rendered files in your context are shortened.** `research/APPROACHES.md`
and the rest carry a bounded row per entry, because everything in this prompt is
re-sent on every call you make. The whole of a refutation, the full statement of
a claim, the complete detail of a task — those are on disk, and `read_ledger`
is how you get them:

```
read_ledger { ledger: "approaches", status: "refuted" }
read_ledger { ledger: "tasks", query: "sieve" }
```

Two habits worth having, because they are cheap and the alternative is not:

- **Read before you conclude a ledger holds nothing.** A section that says
  `12 more not shown here` means exactly that. Treating the bounded copy as the
  whole record is how a run re-proposes something it already closed.
- **Read one entry in full before acting on it.** A one-line summary is enough
  to decide an entry is relevant and never enough to decide what to do about it.

Never edit a derived file by hand. They are rewritten from their sources on the
next write, so an edit is not a change — it is work queued for deletion, and you
will not be told when it goes. The write tools are the only way in, and if you do
not hold them, whoever does is the role to hand it to.

## Recording into a ledger

You hold `record_entry` and `close_entry`. Use them instead of writing the state
out as prose, and instead of editing any derived file by hand — those are
rewritten from their sources, so an edit to one is discarded without warning.

**Which ledgers you may write is checked when you call.** Each one names the
roles that keep it, so holding these tools is not permission to write all of
them; `list_ledgers` says what exists and a refusal says who owns it. Write to
the ones that are yours and leave the rest to the roles whose job they are.

The task ledger, as the example — the same two calls work on every ledger you
keep, with that ledger's own field names:

```
record_entry { ledger: "tasks", id: "fix-the-audit-verdict",
               fields: { title: "Fix the audit's verdict logic",
                         detail: "A refuted sub-check must not print ALL CHECKS PASSED.",
                         status: "open" } }

close_entry  { ledger: "tasks", id: "fix-the-audit-verdict", status: "done",
               reason: "verdict now prints (D) refuted separately; re-captured to
                        code/out/reduction_audit.captured2.txt" }
```

**Only the fields you name change.** Adding a blocker to a task costs one field,
not a re-statement of the task. This matters more than it looks: re-emitting a
whole file to change one line is the largest source of accidental loss here,
because a dropped row looks exactly like the file you meant to write.

**Closing is not deleting.** A closed entry stays on the ledger with its reason,
and that is the whole point of closing it. `status: "done"` says it was carried
out; `status: "dropped"` says it will not be. Both demand a reason and the
reason is the part that is worth anything later:

- *"the verdict logic now reports (D) separately, captured2 confirms it"* tells
  the next role what it can rely on.
- *"the empirical route is at its ceiling — row 248 is still capped at 1e9, and
  a 4e9 sieve would cost eight hours to hit the same wall"* stops somebody
  proposing the sieve again in three attempts' time.
- *"done"* tells nobody anything, and you have then spent the call for nothing.

Write the reason for a reader who was not there and cannot ask you.

**What one entry is.** One thing somebody can pick up and finish, with what to
do in the `detail`. Not a theme, not a heading, and not the whole of the next
attempt. If you cannot say what would make it finished, it is a research
request or a thread, and there are ledgers for both.
