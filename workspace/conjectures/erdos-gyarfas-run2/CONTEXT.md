# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. Carries established results with their basis, dead approaches and
why, the computed numbers, related durable memory, disagreements, and gaps —
not a file catalogue and not a narration of what agents did.

Token budget `MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default; the file is
re-sent on every model call in every role, so length is a bill paid many times.
Detail compressed away lives at the linked file.

## Starting state

Not a cold start. The workspace already holds a validated oracle
(`code/lib/erdos_gyarfas.py`), a digested library (`research/CLAIMS.md`), the
2-connected G-heart verification at N=8 (`code/out/g_heart_verify_n8.out`),
and a weakened ladder. Full reconciliation of the Established section is
tracked in task `reconcile-stale-context` (the curator owns it); Numbers and
Ruled out below are current as of the director's latest edits.

## Established

- **G-heart lemma holds for the 2-connected δ≥3 class up to N=8** (this run,
  checked): every 2-connected min-degree≥3 graph on n≤8 contains a 4- or
  8-cycle. Evidence: `code/out/g_heart_verify_n8.out` / `.md`.
- The digested library lives in `research/CLAIMS.md`; the curator's
  `reconcile-stale-context` task is what folds its load-bearing rows into this
  section.

## Ruled out

- Pairwise-VF2-isomorphism dedup in `code/lib/biconnected_gen.py`: it is what
  made all three 600s `execute_command` runs time out (verify_biconnected.py,
  check_biconnected_gen.py, check_generator_to8.py). Replaced by exact
  canonical dedup (`code/lib/canonical.py`); the corrected generator matches
  A002218. Closed as task `verify-2conn-class-oracle` (done, N=8).
- Ad-hoc regeneration of the 2-connected class (pattern_finder's inline
  `python3 -c` at [86:04]): it is the fifth 600s timeout. **Nobody regenerates
  that class ad-hoc.** Every role that needs it runs
  `code/out/pattern_gheart_corrected_fast.py` or reads the committed
  `code/out/g_heart_verify_n8.out` / `.md`. Any new enumeration states its N
  and expected runtime before it is run, and stays under 120s.
- Enumerating the girth-5 class past N=11 in `code/out/check_girth5_class_crosscheck.py`: it ran >4min (over the 120s rule) and the n=12,13 range verifies nothing about the girth-5 claim, which is on n=10,11. Cap that cross-check at N=11; state N and expected runtime before re-running. An n=13 run needs a stated reason first.

## Numbers

2-connected min-degree≥3 counts (this run's own sequence, checked):
**1, 3, 19, 149, 2581** at n = 4..8. Every such graph contains a 4- or 8-cycle:
149/149 at n=7 and 2581/2581 at n=8, the latter independently re-checked with
`nx.simple_cycles`. The generator's #2conn totals match A002218
(1,3,10,56,468,7123 at n=3..8). n=8 wall time 28.3s. Evidence:
`code/out/g_heart_verify_n8.out` + `code/out/g_heart_verify_n8.md`; regenerate
only via `code/out/pattern_gheart_corrected_fast.py` (see Ruled out).

## Recalled

*None.* `recall_memory` and `recall_scratch` return no prior-run notes for this
problem.

## Contradictions

*None recorded.* No sources exist in the run yet, so there is nothing to
disagree.

## Gaps

The whole problem is open and the run has it from source only as a statement,
not yet as a literature map. The first two concrete gaps, to be turned into
`research/REQUESTS.md` and `research/FRONTIER.md`:

- The exact partial results and their hypotheses/conclusions: conjectured
  settled classes (planar under connectivity/cubic, claw-free, bounded-degree,
  bounded-girth), and the current computational verification bound with its
  method. `problem.md` lists candidate leads (Bondy–Vince, Verstraëte,
  Sudakov–Verstraëte, Liu–Ma, Gao–Huo–Liu–Ma) but flags them all as
  *unverified leads, possibly mis-named*; nothing here is established.
- The obstruction to beat is that powers of two are sparse, so an interval
  result does not force one unless it exceeds the gap; the attack must produce
  a cycle at a *prescribed* length, not merely in a range. This is the frame
  from `problem.md`, not an established result.
