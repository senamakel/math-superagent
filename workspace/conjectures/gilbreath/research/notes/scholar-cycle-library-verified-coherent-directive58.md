# Scholar cycle — reference library verified coherent; one stale-state flag

**Role / source:** scholar, adversarial re-digest of the closed library
(Directive 46/47: do not re-fetch, do not re-sweep; verify the recorded closure
and the live threads).

The library is closed and almost fully internally consistent. This cycle did
not re-read the corpus (forbidden and unnecessary); it verified the load-bearing
claims against their summaries/sources, cross-checked claims against durable
memory, and hunted for contradictions. What it found:

## What holds up (verified)

- **Oracle foundation.** `code/lib/gilbreath.py` carries the `EXPECTED` worked
  rows of problem.md (A_1..A_5) and `code/out/witnesses.json` (sieve 400000,
  33,860 primes, depth 600) reproduces them exactly (`leading_entry_is_1`,
  `second_entry_always_0_or_2`, `min_leading_02_block`: 2). The block profiles
  rows 1..40 in witnesses.json match the ledger's published profile
  `2,7,13,13,24,23,...` exactly. Every claim the run makes sits on this
  generator, and it is what the ledger says it is.
- **Consumption constant = 1 (not n/2) is genuinely sourced.** `block_lemma.md`
  re-derives the block lemma with constant 1 (a {0,2} block of length n
  protects n+1 rows) and quotes Odlyzko 1993 §2 p. 374 verbatim agreeing
  (`d_k(1)=1 for K ≤ k ≤ N+K−1`, N=n+1), independently in Killgrove–Ralston
  1959. The `n/2` claim (`odlyzko-block-lemma-asserted`) is contradicted and
  correctly recorded as such. Verified this is not a misreading: the Odlyzko
  1993 summary says explicitly the n/2 figure appears nowhere in the paper.
- **The LOS overstatement is already corrected on disk.** `g-supply-two-point-
  crux-settled.md` flags that `los-2016-consecutive-pair-mod4-bias` was recorded
  with "main term unconditional from PNT-in-AP", which is an overstatement; the
  claim ledger now carries the CORRECTED-2026 note (the two-point leading term
  li(x)/φ(q)^2 is exactly the k-tuple prediction, conjectural). No live
  contradiction remains.
- **The two-point crux and G-supply conditional theorem are in durable memory**
  and agree with the on-disk `g-supply-two-point-crux-settled.md` and
  `abgs-2011-s9-mod4-switch-limit-open`. The switch count is a consecutive-pair
  statistic; one-point PNT-in-AP/GRH/Dirichlet are structurally blind
  (countermodel: list all 1-mod-4 then all 3-mod-4 primes); unconditional
  literature (Ruzsa/Shiu/Martin) bounds only the wrong, non-switch side. The
  deliverable is the CONDITIONAL theorem at Hardy–Littlewood / LOS two-point
  level.

## The one genuine stale-state flag (worth a board post)

**CONTEXT.md "Run state (Directive 56)" and TASKS.md "Do next" still present the
four-candidate gap-variety transfer-repair (`find-weakest-gap-variety-
hypothesis`) as the live open task — but that task is `status: dropped`, killed
by Directive 57, and the live successor is `research/threads/dyadic-periodicity-
collapse.md` (Directive 58).** A worker reading the brief would re-hunt H_f in a
dead list. The claims/threads/tasks ledgers themselves are coherent
(`g-supply-transfer-universal-refuted`, `transfer-matrix-kernel-allones`,
`nu2-transfer-not-restored-by-nondegeneracy` all present and mutually
consistent). The fix is not to edit the derived renders by hand but to let the
task-drop render catch up.

## The live frontier (Directive 58), stated exactly

The F2 transfer ν₂ ≥ c·w is **prime-specific and dead as a universal lemma**:
nu2 = O(1) exactly on power-of-2-periodic halved-gap bit strings (period 1 → 1,
period 2/4/8 → 2), while non-power-of-2 periods grow nu2 ~ c·n (period 3/5/6/7,
c ∈ [0.53, 0.67]); period 6 = 2·3 grows, so the *odd factor* matters. Proof
goals: (1) from Lucas, h eventually periodic with period 2^k forces nu2 = O_k(1);
(2) an odd factor in the period forces nu2 ≫ n. **This gives the primes only
aperiodicity, which is weaker than the quantitative anti-dyadic input the supply
bound ν₂ ≥ c·n needs — it does NOT close G-supply.** The honest deliverable
stays the conditional theorem.

## Files

- This note: `research/notes/scholar-cycle-library-verified-coherent-directive58.md`
- Durable findings stored to Cognee (dyadic dichotomy; stale-state flag).

## What the run still lacks (unchanged)

A proof or unconditional bound of `ν₂ ≥ c·n`. Everything else is proved,
machine-checked, or a recorded refutation.
