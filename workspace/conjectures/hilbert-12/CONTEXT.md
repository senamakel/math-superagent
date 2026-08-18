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

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). The
file is re-sent on every model call in every role that reads it, so length here
is a bill the whole run pays many times over; a brief past its budget is cut
where it exceeds it on the way into a prompt, with a notice saying so. Link the
file that still holds any detail compressed away — source notes under
`research/summaries/`, untouched full texts under `research/sources/`,
reflections, threads. Durable findings belong in Cognee. A statement nobody can
trace to a source is worth less than no statement.

## State of the workspace — cycle 1

**Substantively empty: scaffolding only.** Every ledger (`tasks`, `attempts`,
`reductions`, `thesis`, `goals`, `board`, `claims`, `threads`, `approaches`,
`weakened`, `blueprint`, `entailment`, `frontier`, `requests`) holds 0 entries;
`derived/` has never rendered. Cognee memory, scratch, the claims ledger and
the document index all return empty (checked via `recall_memory` ×3 phrasings,
`recall_scratch`, `relate_memory`, `search_claims`, `search_documents`,
`list_ledgers`). No source has been downloaded, no program run, no Lean file
written, no earlier run left anything. Present on disk: `GOAL.md`, `problem.md`,
`METHOD.md`, `AGENTS.md`, `README.md`, `config/config.toml`, this file, and
README/index scaffolding under `code/` and `research/` — every index lists zero
files (`code/INDEX.md`, `code/lib/INDEX.md`, `code/lean/INDEX.md`,
`code/lean/Lib/INDEX.md`, `code/out/README.md`, `research/*/README.md`).
`code/lean/Lib/` says its first file should be `Statement.lean`; `research/`
has no `sources/`, `summaries/` or `notes/` subfolders yet. The tasks ledger's
single open row is "Record the first concrete step toward the current goal."

## Established

Nothing. Zero claims in the ledger, zero sources, zero computations, zero Lean
statements. The template sections below are filled with the inventory of what
is *not* yet known, because naming the absence is what this run starts from.

## Asserted but unverified — the entire current content

Everything substantive lives in `problem.md` and `GOAL.md`, written from memory
and explicitly flagged "expects correction". None of it is sourced or checked.
The load-bearing items, in the order they matter:

- **Dasgupta–Kakde / Brumer–Stark** (problem.md, recalled): "Brumer–Stark
  proved (away from 2, then completely) by Dasgupta–Kakde, who also give a
  `p`-adic analytic construction of the Brumer–Stark units and, with it, an
  explicit `p`-adic answer to Hilbert's twelfth for totally real fields."
  GOAL.md §1 makes confirming *exactly* what they proved — which conjecture,
  over which fields, `p`-adic-only or not — task #1; it is the item most likely
  to be misremembered or overstated, and it decides what "remains open" means
  for this run.
- **Rank-one abelian Stark conjecture** over a totally real base (problem.md):
  "the sharpest and most tested form" — its precise statement, hypotheses, and
  the proved-vs-conjectural split are not established.
- **Existing Stark-unit tables** (problem.md, GOAL.md): "several published
  tables are small" — which fields and conductors, what software, how many
  entries: unknown. This is the run's baseline; nothing can go "past" it until
  it is enumerated.
- **`p`-adic real multiplication** (problem.md): Shintani, Hayes,
  Darmon–Dasgupta–Pollack–Vonk supply `p`-adic constructions whose
  complex-analytic counterparts are conjectural — asserted, uncited.
- **Kronecker–Weber and CM** settle `Q` and imaginary quadratic: standard
  background, but no source fetched; GOAL.md forbids re-proving either.
- **Mathlib's class field theory coverage**: "probably little" — the actual
  inventory of what today's Mathlib can state (ray class groups, ray class
  fields, Galois groups of number fields) is itself a reportable deliverable,
  unwritten.

## Ruled out

Nothing tried: `attempts`, `approaches`, `threads`, `reductions`, `thesis` all
empty; `research/approaches|backward|threads/` hold READMEs only. No dead end
to avoid yet.

## Numbers

None computed. No oracle exists (`code/lib/` empty); no captured output
(`code/out/` empty). There is no precision ceiling, no verification bound, no
reproduced control value.

## Recalled

Empty. Durable memory (Cognee), scratch, and the claims ledger hold nothing
about Hilbert 12, Stark units, or ray class groups — so no earlier run's
conclusions or hypotheses carry over. Nothing imported, because there is
nothing to import.

## Contradictions

None recorded — nothing is established, so nothing can conflict. Standing
hazard: `problem.md` itself warns its recalled items may be wrong; any of them
may be struck when a primary source lands.

## Gaps — the obvious next unresolved thing

Everything is open; the run's first moves, in order of dependency:

1. **Settle Dasgupta–Kakde from primary sources** (GOAL.md §1, first bullet):
   exact theorem, fields covered, `p`-adic-only or not. Falsifier for the
   current belief: the construction is not `p`-adic-only, or the theorem covers
   a proper subclass of totally real fields. This decides the target.
2. **State the conjecture in Lean**: `code/lean/Lib/Statement.lean` — a real
   quadratic `K`, a modulus, its ray class field, the assertion that a named
   special value generates it, ending `:= by sorry`. Where Mathlib cannot state
   it is a finding about the problem.
3. **Build the oracle in `code/lib`**: exact ray class groups and conductors
   (computed first, always), Stark units from partial zeta values with
   precision/height/margin reported, exact field verification (degree,
   discriminant, ramification, Galois group) returning verified/contradicted/
   inconclusive, guarded by the three controls (Hilbert class polynomial,
   cyclotomic, a published real-quadratic Stark unit).
4. **First attack**: extend the published verified Stark-unit table past its
   range — impossible until gap 1 and the table enumeration land.

Each of these is an unrecorded research request / task; nothing in this cycle
was written to any ledger (the curator holds no write tools for them).
