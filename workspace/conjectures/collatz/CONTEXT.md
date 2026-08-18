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

## State of the workspace

**Library established — phase 1 substantially complete.** The workspace holds:

- `research/ROOT.md` — meets the phase-1 exit test: counterexample structure
  (divergent orbit or non-trivial cycle), current verification bound
  (2^71.02, Barina) and its method, ≥3 restricted classes settled with
  hypotheses, Tao's theorem stated exactly (and what it does not claim),
  current non-trivial-cycle exclusion bound (m ≥ 92; length ≥ 355,504,839,929).
- `research/sources/` — 25 full texts (primary and encyclopedic): Lagarias
  overview + two bibliographies, Tao, Barina 2021+2025 + project page, Hercher,
  Simons–de Weger preprint, Crandall, Kurtz–Simon, Zudilin, Halbeisen–
  Hungerbühler, Eliahou–Fromentin–Simonetto, Chamberland, Kontorovich–Lagarias,
  Mol, Yolcu–Aaronson–Heule, Honda–Ito–Nakano, Roosendaal, Oliveira e Silva
  page, OEIS A006577, Wikipedia, and the Terras failure record.
- `research/summaries/` — one note per source with fenced `claim` blocks;
  `derived/CLAIMS.md` holds ~45 claims.
- `code/` — still empty of programs and Lean; `code/lean/Lib/Statement.lean`
  does not exist yet. The run's own mathematics has not started.
- Ledgers: `claims` populated; `threads`/`approaches`/`tasks`/`attempts`
  empty — no direction of attack has been opened yet.

## Established

The library now holds primary sources; every claim below traces to a file under
`research/sources/` and a claim id in `derived/CLAIMS.md`. Evidence classes:
proved (theorem in source), asserted-by-source, verified-numerically, conjectured.

- **Counterexample structure** (`lagarias-counterexample-structure`): a
  counterexample is either (a) an orbit diverging to infinity, or (b) an orbit
  entering a non-trivial cycle other than 1→4→2→1. Both open; no method
  approaches either (Lagarias overview §6.1, §7).
- **Verification record** (`barina-2075-2p60`): all n < 2075×2^60 ≈ 2^71.02
  verified to reach 1 (Barina project page, 2026-08-18 snapshot; 2^71 verified
  2025-01-15). Method: accelerated/Syracuse form, 3^k sieves, GPU/CPU, work
  unit 2^40 (`barina-method`, `barina-2021-method`: O(N) tables replace O(2^N);
  speeds 4.2e9 CPU / 2.2e11 GPU per sec). Supersedes Oliveira e Silva's
  20×2^58 (`lagarias-W1`).
- **Cycle-length consequence** (`barina-cycle-length-355b`): at verification
  limit 2^71, any non-trivial cycle has length ≥ 355,504,839,929 (Barina 2025
  line 253).
- **Tao's theorem** (`tao-almost-all`, proved): for any f(N)→∞,
  Col_min(N) < f(N) for almost all N in logarithmic-density sense. It does NOT
  rule out divergent orbits or non-trivial cycles (`tao-does-not-close`).
  Korec baseline: θ > log 3/log 4 ≈ 0.7924, Col_min(N) ≤ N^θ almost all N.
- **Cycle exclusion** (`hercher-m92`, proved): no Collatz m-cycle with m ≤ 91
  local minima; m ≥ 92 needed. (`hercher-K-1p375e11`, proved): if all n ≤
  3×2^69 verified, any non-trivial cycle has K > 1.375×10^11 odd members
  (hypothesis now satisfied by Barina). Eliahou via Lagarias (`lagarias-W2`):
  trivial cycle only one with period < 10,439,860,591 or < 6,586,818,670 odd
  integers (now superseded by `barina-cycle-length-355b` for length).
- **Diophantine lever** (`zudilin-mu-8616`, proved): μ(γ) < 8.616 for any
  nonzero γ ∈ Q log 2 + Q log 3, so |log 3/log 2 − p/q| > c/q^{8.616} — the
  effective irrationality measure that converts cycle shapes into cycle-length
  bounds. This corrects the earlier guess of 13.3.
- **Undecidability** (`kurtz-simon-pi02`, proved): generalized Collatz problem
  is Π^0_2-complete; does NOT apply to the specific 3x+1 function.
  (`conway-1972-unsolvable`): Conway's unsolvable iteration problem.
  (`mol-collatz-tag-system`): Collatz reduces to halting of TS(3,2) — rules
  a0→a1a2, a1→a0, a2→a0a0a0; explains why generic machinery is unavailable.
- **Automated-deduction flank** (`yah-rewriting-equivalence`, proved): Collatz
  ⇔ termination of an SRS over mixed binary-ternary strings.
  (`yah-no-natural-matrix-interp`, proved): natural matrix interpretations
  cannot prove termination of Zantema's unary system — a closed route.
  (`yah-weakenings-automated`): arctic interpretations prove weakenings only.
- **Stochastic shadow** (`kl-stochastic-heuristic`): MRP and negative-drift
  BRW models predict bounded orbits and σ∞(n) ~ c log n, but are heuristic —
  the unproved independence assumption; any result built on them does not touch
  the conjecture. (`kl-kontorovich-sinai-gbm`): scaled initial trajectories
  converge to geometric Brownian motion (rigorous, typical only).
- **2-adic ergodicity** (`lagarias-2adic-ergodic`): the 3x+1 map extends to Z_2
  ergodically (conjugate to shift); the difficulty is Z ⊂ Z_2, a dense
  measure-zero subset — why average-case control misses the conjecture.
- **Counts** (`lagarias-W5`): ≥ X^0.84 integers ≤ X iterate to 1
  (Krasikov–Lagarias). (`lagarias-W3`): infinitely many n take ≥ 6.143 log n
  steps (Applegate–Lagarias).
- **Crandall** (`crandall-finite-cycles`, proved): finitely many cycles per
  period k; (`crandall-conjecture-H`, conjectured): H(x) ~ 2 log x / log(16/9).

Open requests still unfilled: the full texts of Eliahou 1993 and Simons–de Weger
2005 (paywalled/502), Steiner 1977 (conference proceedings, no free PDF), Korec
1994 (DML scanned no text layer), **Terras 1976** (scanned, no text layer — the
file once filed under this name was the wrong paper, Morton 1992, and has been
removed; its density-1 finite-stopping-time result is asserted-by-source via
Garner 1981, Gluck–Taylor 2001, Hercher 2022), Oliveira e Silva's chapter
(paywalled). The numbers from each are captured in the claims above via
secondary sources; the primary texts remain gaps.

## Ruled out

Nothing has been tried in this workspace — no approaches, no attempts, no
refuted claims on file. The standing obstruction any approach must beat
(problem.md): the parity-independence heuristic is unproved, and a worst-case
argument is required — average-case control does not narrow the open case.

## Numbers

None. No computation has been run; `code/out/` is empty.

## Recalled

Cognee holds nothing for this problem — no prior runs, no library, no memory.

## Contradictions

None on file. (The known tension between Tao's density result and the
conjecture itself is a fact about the literature, not a finding of this run.)

## Gaps — the obvious next unresolved things

1. **Primary texts still missing** — the full texts of Eliahou 1993
   (paywalled), Simons–de Weger 2005 published PDF (IMPAN 502 / no text layer;
   preprint v1.44 held), Steiner 1977, Korec 1994, **Terras 1976** (scanned;
   the file once filed under this name was the wrong paper — Morton 1992 — and
   has been removed), Oliveira e Silva's verification chapter. All captured via
   secondary sources; the primaries remain open requests.
2. **No Lean statement** — `code/lean/Lib/Statement.lean` (the conjecture as a
   type, ending `:= by sorry`) does not exist. This is the next deliverable
   after the library; the phase-1 library criterion (ROOT.md with counterexample
   structure, verification bound, ≥3 restricted classes, Tao exactly, cycle
   exclusion bound) is met.
3. **Cycle-length bound not in Lean** — the Eliahou-type formula and the
   Barina 355,504,839,929 consequence deserve Lean `Cited` statements so the
   cycle-exclusion arm builds on kernel-checked statements.
4. **No oracle** — no exact Collatz checker exists yet to reproduce the
   literature's verification bound before anything is computed past it. The
   oracle should reproduce the O(N)-table idea from `barina-2021-method`.
