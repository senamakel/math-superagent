# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

It carries what an agent would otherwise rebuild from disk, from the note store,
or from a session it was not present for: established results with their basis,
approaches that died and why, what the computed numbers look like, what durable
memory relates this problem to, and where two accounts disagree. It is not a
catalogue of files — `research/INDEX.md` is that — and not a narration of what
agents did.

**Token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). The file is
re-sent on every model call in every role that reads it; length here is a bill
the whole run pays many times over. Link the file that still holds any detail
compressed away.

## Established

Nothing yet. This is a fresh scaffold: no claims recorded (`derived/CLAIMS.md`
re-derived empty, `search_claims` finds none), no research notes, sources or
summaries under `research/`, no `code/lib` modules, no Lean files, no captured
output under `code/out/`, no durable memory or scratch (`recall_memory` and
`recall_scratch` both empty). All ledgers — tasks, attempts, reductions,
thesis, goals, threads, approaches, claims, requests — have 0 entries.

## Recalled (asserted but unverified — from `problem.md`, written from memory)

`problem.md` itself demands correction (GOAL.md rule). None of these has a
citation in the workspace; GOAL.md §1 exists to confirm or strike each:

- n ≤ 2: `ker D` finitely generated — classical, source not present.
- n = 3: finitely generated — attributed to Miyanishi, also via Zariski's
  finiteness in dimension ≤ 3; the argument is the run's most valuable import.
- n = 5: **not** always fg — Daigle–Freudenburg derivation with
  non-finitely-generated kernel. Unsettled here: whether the kernel is *proved*
  non-fg or only computed to be large.
- n = 6: Freudenburg; n = 7: Paul Roberts — counterexamples, historically
  earlier and larger than n = 5.
- n = 4 (H14.4): open — the run's target.
- Weitzenböck: *linear* `G_a`-actions have fg invariant rings in every
  dimension (Seshadri's proof); exact hypothesis (linear? triangularisable?)
  to be pinned. A dimension-4 argument that never uses non-linearity is void.

## Ruled out

Nothing. No attempt has been made, so no dead end exists yet.

## Numbers

None. No computation has been captured.

## Contradictions

None recorded.

## Gaps

The first unresolved thing is not mathematics but the frontier check (GOAL.md
§1), before any attempt is spent: (1) the smallest published n with a
non-fg `ker D`, the paper, and proved-vs-computed status; (2) the n = 3 proof
and which argument generalises; (3) Weitzenböck's exact hypothesis;
(4) the best variable count for Nagata-type counterexamples of other unipotent
groups (kept separate from the `G_a` record); (5) whether any dimension-4
claim exists anywhere — published, preprint, withdrawn. In parallel per the
phase plan: state H14.4 in `code/lean/Lib/Statement.lean` (ending `:= by
sorry`) and record what Mathlib cannot yet state; build the oracle in
`code/lib` with the three entry guards of GOAL.md §3, verified against the
published n = 5 generator degrees before any n = 4 use.
