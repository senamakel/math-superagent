# Shared context

Problem: consecutive perfect powers — all integer solutions of
`x^p - y^q = 1`, x,y>0, p,q>1. Believed to have exactly `(3,2,2,3)` = `3^2-2^3=1`.
Not proved (as stated in problem.md). Objective (GOAL.md): a genuine partial
result stated exactly; the one outright failure is claiming the whole on an
argument that has not survived attack.

## Workspace character — read this first

- **Calibration workspace.** `config/screen.jsonl` labels this as such:
  problem.md is stated as open, and sources that would hand the run a published
  solution are withheld. The actual mathematical fact (Mihailescu 2002) is that
  this is a *proved theorem*. REQUESTS request `exact-statement-primary-1ad5`
  flags exactly this contradiction. Keep re-deriving in-workspace; the framing
  is part of the sandbox.
- **No external sourcing.** All 4 download attempts failed: `arxiv.org` not on
  the egress allowlist, `en.wikipedia.org` denied. Every skeleton `next` that
  says "librarian fetches Cassels 1960 / Mihailescu 2002" is dead at the
  network layer — those lemmas must be re-derived here, not fetched. This
  constrains every role; do not plan on downloads.

## State of the run

PLANNED, NOT VERIFIED. A substantial research tree exists (`research/BACKWARD.md`
5 skeletons / 20+ open gaps, `BLUEPRINT.md` statement graph, `WEAKENED.md` two
ladders, `REQUESTS.md` 4 posted requests) but every lemma is marked open and
`research/CLAIMS.md` is empty ("No claims recorded yet"). `search_claims`,
`recall_memory`, `recall_scratch` all return nothing. No source downloaded, no
claim block, no captured program output (`code/out/` has only its README).

## Established (verified in this run)

None. Nothing below is this run's verification; it is the task-stated / plan
content (problem.md + research tree), asserted not verified, each needing its
own in-workspace proof or claim block.

- Every lemma in `research/BACKWARD.md` sits where the known solution
  `3^2-2^3=1` is: the exponent-2 case `G-exp2-a`/`G-full-case-p2` must *return*
  `(3,2,2,3)` (it is the positive case); `G-exp2-b`/`G-full-case-q2` and the
  odd-odd lemmas are excluded by hypothesis (p or q = 2), silent about it.
  A lemma implying no solution at all is refuted, not weakened.

## Ruled out

- **External literature (as the route to Cassels/Mihailescu):** blocked by
  egress — arxiv not on allowlist, wikipedia denied. See Workspace character.
- **Closing the gap by computation:** the effective bound from linear forms in
  logarithms is astronomically large (problem.md); never propose exhausting it.
- The plan (odd-prime-case.md) already records one dead direction as *dead-end
  shaped*: the double-Wieferich congruences alone do NOT exclude all odd-prime
  pairs — G-exclude must also use the equation (q|x, p|y) and cyclotomic
  structure; the congruence pair alone is insufficient. A known conditional
  theorem already identified: Cassels + double-Wieferich give *if (p,q) is not
  a double-Wieferich pair then x^p-y^q=1 has no solution* — the shape of
  GOAL.md's second deliverable.

## Numbers

None computed. The oracle exists but **has never been run**:
`code/scholar_oracle/oracle.py` implements `solutions(N)` (exact integer, must
return exactly `(3,2,2,3)` for N>=9). `code/out/` empty — no N, no runtime.
First job: run and capture it.

## Recalled

None (both stores empty of prior findings).

## Contradictions

1. problem.md says "not proved"; Mihailescu 2002 proved it (REQUESTS
   `exact-statement-primary-1ad5`). Calibration artifact; see Workspace character.
2. problem.md hint `p^2 | y^{p-1}-1` contradicts Cassels's `p|y` (would force
   y^{p-1}=0 mod p). Both REQUESTS `exact-statement-citable-f890` and
   `backward/both-odd-primes.md` flag it. Re-derive the true form
   (`p^{q-1} ≡ 1 mod q^2`, `q^{p-1} ≡ 1 mod p^2`) rather than copying the hint.

## Gaps / next moves (in order)

1. **Run the oracle** `code/scholar_oracle/oracle.py`; capture output in
   `code/out/`; report N reached and runtime. Confirms exactly `(3,2,2,3)`.
2. **Close `R-trivial-bases`** (x,y >= 2: x=1→y^q=0 excluded, y=1→x^p=2
   impossible) — current weakest rung in `research/WEAKENED.md`, one line.
3. Redo the two exponent-2 cases (Z and Z[i]) and the prime-exponent reduction
   in-workspace — the foundation everything is calibrated against.
4. Re-derive Cassels (p|y, q|x) by in-workspace valuation computation (cannot
   be fetched); then the double-Wieferich conditions.
5. Open content: both-odd-primes class-group descent (G-exclude / G-odd-descent)
   in `Q(zeta_p)` — the only step without a cheap move and the real research
   requests live here.
