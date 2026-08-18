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

**Phase 1 (library) complete; computation and Lean started; the run's central
thesis is refuted and must not be re-proposed as a live bet.**

- `research/ROOT.md` meets the phase-1 exit test: counterexample structure,
  verification bound, ≥3 restricted classes, Tao's theorem stated exactly,
  cycle-exclusion bound. 25+ sources under `research/sources/`, ~105 claims in
  `derived/CLAIMS.md`, summaries in `research/summaries/`.
- `code/lean/Lib/Statement.lean` states the conjecture (compiles, deliberate
  sorries, `#print axioms [sorryAx]`).
- **Code now holds executed programs and captured output** (the brief below was
  written before this): the oracle `code/brute.py` +
  `code/r-small-n-direct/verify_small.py` (verified n ≤ 2^20 reach 1, exact,
  cross-checked against the naive oracle on n=1..1000), `code/collatz_oracle.py`
  (naive, checked 1..10000), `code/cf-log23/` (continued fraction of log2 3,
  terms checked against Crandall), `code/cycles/` (Böhm–Sontacchi formula
  oracle), `code/no-cycle-diophantine/collision_table.py` (Hercher/Diophantine
  table). Captured outputs in `code/out/` with fenced claim blocks.
- **Ledgers populated**: `attempts` (1: `diophantine-collision-first-attack`,
  adopted — the run's only attempt), `tasks` (1 done), `reductions` (1 broken),
  `thesis` (1 **abandoned**), `goals` (1: no-nontrivial-cycle, sketched),
  `approaches` (3: one refuted, one **adopted** = lte-divisibility-obstruction,
  one narrowed), `threads` (reference-digestion, active, but rests on 4 claim
  ids of which only 2 exist on disk), `weakened` (collatz ladder, 7 rungs).
- `research/backward/no-nontrivial-cycle.md` — the proof skeleton for sub-claim
  (b); one gap open (`G-min-element-lower`), two discharged by literature.
- Open requests: Simons–de Weger published PDF (HTTP 502), Simons 2008 text
  layer; four answered (best effective μ, best cycle exclusion, verification
  record, Tao exact statement).

## Established

The library holds primary sources; each claim below traces to a file under
`research/sources/` and a claim id in `derived/CLAIMS.md`. Evidence classes:
proved (theorem in source), asserted-by-source, verified-numerically, checked
(computed here), conjectured, conditional (Lean, resting on a Cited axiom).

**The two live obstructions** (`lagarias-counterexample-structure`): a
counterexample is (a) a divergent orbit or (b) an orbit entering a non-trivial
cycle. Sub-claims (a) and (b) are independent; this run works on (b), and
closing (b) alone does NOT close the conjecture.

- **Verification record** (`barina-2075-2p60`, `barina-2p71-library-update`,
  asserted-by-source): all n < 2075×2^60 ≈ 2^71.02 reach 1 (Barina project
  page 2026-08-18 snapshot; 2^71 verified 2025-01-15). Method
  (`barina-2021-method`, `barina-method`): accelerated/Syracuse form, 3^k
  sieves, GPU/CPU; O(N) lookup tables replace O(2^N).
- **Cycle-length consequence** (`barina-cycle-length-355b`): at verification
  limit 2^71, any non-trivial cycle has length ≥ 355,504,839,929 (Barina 2025,
  citing the Eliahou-type formula).
- **Cycle exclusions, strongest to weakest**:
  - `hercher-m92` (conditional, Lean-checked): no m-cycle with m ≤ 91 local
    minima; any non-trivial cycle has m ≥ 92. Formalised in
    `code/lean/hercher_m92-97b13fb9.lean` (cited axiom `Cited.no_m_cycle_le_91`).
  - `hercher-K-7p76e19` (proved): m ≤ 98 ⇒ K ≥ 7.76×10^19 odd members.
    `hercher-table-K-bounds-m-92-200` (checked here): exact published table
    rows, m=92..200, source lines 1190-1210.
  - `hercher-K-1p375e11` (proved, conditional Lean): if all n ≤ 3×2^69
    verified (hypothesis now satisfied), any non-trivial cycle has K >
    1.375×10^11 odd members.
  - `lagarias-W2` (asserted, Eliahou 1993): trivial cycle is the only one with
    period < 10,439,860,591 or < 6,586,818,670 odd integers. Cross-checked by
    `ghosh-beta-loop-bound` (same number, independent derivation).
- **Diophantine lever** (`zudilin-mu-8616`): μ(γ) < 8.616 for nonzero γ ∈
  Q log 2 + Q log 3; the effective constant c₀ is source-effective but has NOT
  been extracted here. **Notation trap**: the cycle gives |log 3/log 2 −
  (K+L)/K| with K odd, L even — the approximating fraction's numerator is the
  EVEN-step count; getting this backwards turns a lower bound into an upper one
  (this exact error killed the run's first attempt, see Ruled out).
- **Bridge** (Hercher Thm 16 / Simons–de Weger Lemma 1, discharged in
  `G-cycle-diophantine-bridge`): 2^(K+L) = ∏(3 + 1/n) over odd members; upper
  bound (K+L)/K < log_2 3 + (3 log 2/K)·Σ T(n_i). Formalised abstractly in
  `code/lean/no_nontrivial_cycle_G_cycle_diophantine_bridge-33fd98af.lean`
  (verified, no sorry).
- **Tao's theorem** (`tao-almost-all`, proved): for every f(N)→∞,
  Col_min(N) < f(N) for almost all N (logarithmic density). Does NOT rule out
  divergent orbits or non-trivial cycles (`tao-does-not-close`). Korec
  baseline: θ > log 3/log 4 ≈ 0.7924, Col_min(N) ≤ N^θ almost all N.
- **Restricted classes / reductions**: Monks 2006 (`monks-ap-sufficient`,
  proved): every nonconstant arithmetic progression is sufficient for the
  accelerated map, and separately for the divergence and non-trivial-cycle
  sub-conjectures. Everett (`everett-density-1-finite-stopping-time`, proved):
  density-one finite stopping time. `efs-falling-time-14`,
  `efs-sft-9` (asserted): falling-time bounds for n ≡ 3 mod 4, n < 2^35.
  Knight 2025: excludes only the Christoffel-word extremal parity class (via
  Böhm–Sontacchi + divisibility) — a restricted class, does not touch general
  cycles or divergence.
- **Böhm–Sontacchi / Halbeisen–Hungerbühler** (`bohmsontacchi-cycle-formula`,
  `halbeisen-rational-cycle-formula`, proved): a cycle with L steps, m odd, has
  x = S(L,m,gaps)/(2^L − 3^m); a rational cycle exists iff 2^L > 3^m.
  **This is the load-bearing reformulation of the adopted approach.**
  `halbeisen-optimal-criterion`: the staircase parity pattern is extremal for
  cycle-length bounds.
- **Undecidability / failure context**: Kurtz–Simon Π^0_2-completeness of the
  generalized problem (`kurtz-simon-pi02`, proved — does NOT apply to 3x+1);
  Mol's tag-system encoding (`mol-collatz-tag-system`); Zantema SRS rewriting
  + natural matrix interpretations closed (`yah-no-natural-matrix-interp`);
  stochastic models are heuristic (`kl-stochastic-heuristic`);
  `kl-kontorovich-sinai-gbm` (rigorous, typical only); 2-adic ergodicity
  (`lagarias-2adic-ergodic`) explains why average-case control misses the
  conjecture.
- **Crandall** (`crandall-finite-cycles`, proved): finitely many cycles per
  period k. Brox 2000 (`brox-finite-cycles-few-descents`, proved): finitely
  many cycles with few descents.
- **Lean**: `Statement.lean` (3 sorries, `[sorryAx]`); `hercher_m92` and
  `hercher_K_1p375e11` (conditional, no sorries); `lagarias_W2` (conditional);
  `zudilin_mu_8616` file currently FAILS (span-membership `sorry` +
  `Cited.zudilin_theorem_3`); `cycle_collision.lean` (blueprint, theorem open
  `:= by sorry`, three Cited axioms — **the theorem it states is FALSE over
  the cited hypotheses**, see Ruled out; do not build on it).

## Ruled out — do not re-propose

1. **The Diophantine collision (x_min lower bound from K)** — the run's first
   and only attempt, REFUTED two independent ways (`attempts`
   `diophantine-collision-first-attack`; `thesis` `diophantine-cycle-collision`
   **abandoned**; `reductions` `cycle-xmin-vs-mu-threshold` broken;
   `research/approaches/diophantine-collision-refuted.md`):
   - Hercher's Corollary 24 Table 1 bounds **K (number of odd members), not
     x_min**. `research/ROOT.md`'s line 48 "min element ≥ 7.76e19" is a
     conflation — ROOT.md still carries this error and must be repaired.
   - Lean arithmetic (`code/lean/Lib/cycle_collision.lean`): the cited
     estimates imply S > c₀·m^(μ−1)/(3 log 2) and hence x_min < (3 log
     2/c₀)·m^(2−μ) — the **reverse** of the claimed lower bound. The proposed
     collision cannot be inferred and is algebraically false over the cited
     hypotheses. Consequence: **a lower bound on x_min is NOT available from
     Hercher's K-bounds + Zudilin's measure**; the "deficit" table
     (`collision-deficit-grows-with-m`) compares K against a threshold and is
     evidence about the WRONG quantity.
2. **backward-transducer-covering** (`approaches`, refuted): the stabilization
   hypothesis (composed transducers converge to a finite covering language) is
   not a theorem in the cited literature (Stérin 2019/2020) and is contradicted
   by published k-dependent growth bounds.
3. **parity-rationality-conjugacy** (`approaches`, narrowed): the 2-adic
   conjugacy survives as a TOOL; the divergence-via-three-distance bridge is
   closed — no lemma links v₂(T^k(n)+1) to an irrational rotation.
4. **yah-no-natural-matrix-interp**: natural matrix interpretations cannot
   prove termination of Zantema's system.
5. **Statistical/density approaches as progress**: Tao, Everett, Korec,
   Kontorovich–Sinai, stochastic models — do NOT touch the open case; do not
   report them as narrowing it.
6. **Unverified source claims that must not be used as established** (digest
   `2026-08-18-digest.md`): Laurore's claimed σ=ω for all positive integers
   (uncorroborated, must be independently certified before reliance);
   Angeltveit 2026 (method proposal, tested only to 2^60 — no new record);
   Ansari 2025 (recursive-sufficiency arithmetic NOT formally checked here;
   claimed frontier 4·3^44+2 ≈ 3.939e21 ≈ 2^71.74 is conditional on exact
   arithmetic + source theorem).

## Numbers

- **Verified here (exact)**: every 1 ≤ n ≤ 2^20 reaches 1
  (`r-small-n-direct-2^20`, checked; cross-check vs naive oracle on 1..1000
  AGREE; worked example 1→4→2→1 reproduced; no cycle, no divergence observed).
  Naive oracle `code/collatz_oracle.py` checked 1..10000.
- **Hercher K-table (exact, checked here)**: m≤98: K>7.76e19; m≤117: K>2.74e19;
  m≤276: K>4.68e18; m≤3079: K>3.97e17; m≤12055: K>1.30e17; m≤948987: K>4.30e15;
  m≤1.14e6: K>3.81e15; m≤1.33e9: K>1.64e12; m≤1.54e9: K>8.90e11; m≤9.46e9:
  K>1.37e11; all m: K>7.20e10. (Source lines 1190-1210, published JIS version
  — differs from arXiv v1; use published.)
- **Böhm–Sontacchi formula hand-verified here** against four real
  accelerated-map cycles on Z: (L,m,gaps)=(2,1,(2))→x=1; (1,1,(1))→x=−1;
  (3,2,(1,2))→x=−5; (11,7,(1,1,1,2,1,1,4))→x=2363/(−139)=−17
  (`research/approaches/lte-divisibility-obstruction.md` step 0).
  Hand-computed UNSAT for shape (5,2): D=23, S∈{5,7,11,19}, none divisible.
- **cf-log23**: continued fraction of log2 3 — first 50 terms match Crandall
  1978; exact convergent numerators/denominators match published cycle bounds
  (`code/cf-log23/continued_fraction_log2_3.py`).
- **Lean check verdicts** (json in `code/out/lean/` and `code/out/verify/`):
  Statement.lean outcome failed (3 sorries); hercher_m92 conditional; zudilin
  file failed (1 sorry). `hercher_ladder.txt` is EMPTY — the
  `verify_hercher_ladder.py` run timed out; its ladder comparison is
  unverified and must not support a claim.

## Recalled

Cognee holds the phase-1 library summary, the `Statement.lean` formalisation
record, and the Hercher table extraction (K-not-x_min). `research/LOCAL_MEMORY.md`
and `MEMORY.md` are the local fallback copies from the period when the memory
service was down — check them only for what Cognee lacks.

## Contradictions

- **`derived/THREADS.md`** lists `reference-digestion` as resting on
  `ansari-verification-extension-4p3p44`, `knight-no-integer-high-cycles`,
  `zudilin-mu-8616` — none of these ids exists as a claim block on disk (grep
  finds them only as prose mentions). `zudilin-mu-8616` and
  `knight-no-integer-high-cycles` are load-bearing in the brief but unrecorded
  as claims; the thread's `rests-on` must be repaired to real ids.
- `research/ROOT.md` line 48 conflates K with x_min ("min element ≥ 7.76e19") —
  refuted by `hercher-table-K-bounds-m-92-200`; ROOT.md needs the repair the
  closed task `first-executed-partial-result` demanded.
- `derived/CLAIMS.md` flags `lagarias-W2` and `lagarias-W2-formal` as "called
  formalised, not backed by the kernel": `code/lean/lagarias_W2-eb4a08bf.lean`
  has changed since the kernel checked it — re-check before relying on it.
- `code/lean/Lib/Statement.lean` on disk (accelerated map T) differs from the
  version Cognee's memory describes (plain map, `collatzStep`): the memory is
  of an earlier session; the disk file is current.

## Gaps — the obvious next unresolved things

1. **The adopted approach is not yet executed**: `lte-divisibility-obstruction`
   (status adopted) — exclude cycle shapes by testing the necessary
   divisibility (2^L−3^m) | S directly, prime by prime. Its own first step
   (run `code/cycles/run_oracle.py` to validate the formula against trivial
   and negative cycles, then enumerate shapes) is recorded but NOT done — the
   file exists but was never executed. This is the natural next task.
   The load-bearing completeness lemma to state in Lean first: for p prime,
   e = v_p(2^L−3^m), the map gaps → S mod p^e factors through
   (V_1,…,V_{m−1}) mod ord_{p^e}(2). Blind spot already identified: shapes
   with |2^L−3^m| = 1 (the trivial cycle's (2,1)) impose no constraint.
2. **G-min-element-lower is open and must be reformulated**: the old target
   (x_min lower bound colliding with the Diophantine arm) is dead; a correct
   statement relating K to x_min or S, or a genuinely independent x_min bound,
   is required before any new collision attempt (`reductions`, `goals`).
3. **c₀ not extracted**: the effective constant of Zudilin's μ<8.616 has not
   been read off the construction; every numerical threshold is currently
   computed at c₀=1.
4. **zudilin_mu_8616 Lean file fails**: span-membership proof gap + sorry;
   the brief and skeleton treat μ<8.616 as discharged by literature, which is
   true as a claim but not as a Lean artifact.
5. **Open source requests**: Simons–de Weger 2005 published PDF (HTTP 502,
   preprint v1.44 held), Simons 2008 text layer.
