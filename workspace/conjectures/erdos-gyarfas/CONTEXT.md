# Shared context

What the run's reference library and its own work establish, in the run's own
words. Research team writes; everyone reads. **~1000 tokens is the working
target.** Link down to the file holding the cut detail; full claim-by-claim
ledger is `research/CLAIMS.md`, sealed digests `research/L2.0/`, structure
`research/ROOT.md`.

Task: Erdős–Gyárfás — every finite simple graph with δ≥3 has a simple cycle of
length 2^k, k≥2 (so in {4,8,16,…}). Open. Deliverable is a partial result,
never a claim of the whole.

## Established (all in MEMORY.md unless noted)

- **Conjecture open** as of the library. Primary source Er96: "…min degree ≥3
  contains a cycle of length 2^k, k≥2." [[L1.0/erdosproblems-open-Er96]]
- **δ=2 insufficient** (a long non-2-power cycle has δ=2). Trivial.
- **A minimal counterexample is predominantly cubic**: every proper subgraph
  has a min-degree-2 vertex; regular ⇒ cubic; ≥4/7 of vertices have degree
  exactly 3; every vertex adjacent to a degree-3 vertex. [[L2.0/L1.0]]
  (Carr; asserted, not this run's oracle).
- **Sparse**: avg deg ≤ exp(O(log* n)) (Sudakov–Verstraëte; powers of two are
  an exponentially-bounded even sequence). With δ≥3, density ∈ [3, that].
- **Verification bound**: any counterexample needs ≥17 vertices, any cubic one
  ≥30. Markström found four 24-vertex graphs whose only 2-power cycle is
  length 16, one planar — closest known near-counterexamples. **Computed this
  run**: by the run's own oracle + nauty-geng, NO4-survivor counts (connected
  min-degree≥3, C4-free: 5,9,57,503,6059,91433,1655659 for n=10..16) — each and
  every C4-free δ≥3 graph on n≤16 contains an exact 8-cycle, so **no
  counterexample exists on n≤16**, computationally re-verifying the ≥17 floor.
  [[code/eg/survivor_sequences.md]]
- **Restricted classes closed** (never re-derive): P13/P10/P8-free,
  3-connected cubic planar, diameter-2, claw-free planar, K_{1,m}-free, Cayley
  families, large average degree. [[L1.1 digests]]
- **Only unconditional δ≥3 length guarantee**: two cycles of length 1-or-2
  apart (Gao–Huo–Liu–Ma, k=2) and two of consecutive length (Gao–Ma
  Bondy–Vince k=0). Non-density; still lands between consecutive 2-powers.
- **Moore-bound girth barrier (this run, proof-level)**: n_min to avoid all
  2-powers up to 2^m is 3·2^(2^(m-1))−2 → no 4 needs n=10, no 8 needs 46, no 16
  needs 766. Girth alone unusable as obstruction at accessible n. [[code/eg/moore_barrier_threshold.py]]
- **Oracle verified**: min_degree + exact cycle-length set via lib/cycles.py
  (networkx), cross-checked by two independent paths (verify_cycles.py, hand
  DFS in hand_dfs_check.py) on K4, K3,3, Petersen, cube Q3. Exact enumeration is
  exponential → small graphs only; egcheck.py is the polynomial bounded-DFS
  predicate that pushes the bound. [[code/lib/INDEX.md]]

## The obstruction every attack must beat

An interval [a,b] of guaranteed cycle lengths forces a 2-power only when b≥2a;
below 2^(k+1) the gap is 2^k. Liu–Montgomery's large-average-degree result
settles only enormous density for exactly this reason. So: the δ≥3 length
machinery gives at most consecutive cycles, which never spans a 2-power by
itself. The structural fight is in **low-girth predominantly-cubic graphs**,
where C4/C8 already appear — not in the girth regime.

## Failed approaches (dead ends; record, don't re-propose)

- **Interval-of-lengths**: gap below 2^(k+1) is 2^k; δ≥3 buys only consecutive
  / 1-or-2-apart cycles. THE obstruction.
- **Liu–Montgomery large avg deg**: guaranteed even interval [log^8 ℓ, ℓ] is
  wide only at enormous average degree; at δ=3 (sparse) gives nothing.
- **Girth/Moore-barrier** route: real counterexample hits the ≥17/≥30 floor
  long before high girth rules anything out (no-8 needs n=46).

## Lean

`lean/erdos_gyarfas.lean` elaborates the formal statement (SimpleGraph V,
minDegree≥3 ⇒ ∃ cycle p with p.length = 2^k ∧ 2≤k). No lemmas proved; body is
one intentional `sorry`. `#print axioms`: [propext, sorryAx,
Classical.choice, Quot.sound] — sorryAx the only non-standard axiom. Add
`#print axioms` to the file. [[lean/STATUS.md]]

## Durable memory / reflections

- `reflections/` holds NO findings: 8 attempts returned "judged unsolved" and
  reflection died on OpenRouter HTTP 403. No self-critique trail exists; trust
  none of those notes. Re-run reflection if the service recovers.
- Scratch (recall_scratch) on this run: no survivor-count / cycle-length
  sequences beyond the ones listed; the Moore closed form is the only exact
  sequence structure the pattern-finder found. OEIS A007112 (count of connected
  δ≥3 graphs per order) has no exploitable low-order recurrence.
- `research/THREADS.md`: no threads open yet; `FRONTIER.md` holds cited leads.

## Gaps / next

Phase 3 (oracle) essentially complete and bound re-verified on n≤16. Open Phase
2/4 items: keep MEMORY.md's structural facts honest; pursue one precise
structural claim about a minimal counterexample (the predominant-cubic /
sparse structure is the lever); formalise a lemma in Lean as one stabilises.
NOTHING from this run has established a new attack on the interval obstruction
itself — that is the open core.

## Live (this run, partly settled)

- **S5 vs A366224** (S5 = connected min-degree≥3 girth≥5 graphs; A366224 =
  3-connected girth≥5). **Verified equal through n=14** (S5 = A366224 =
  1,0,2,4,23). But the identity is **provably NOT a theorem**: joining two
  girth≥5 min-degree≥3 graphs at a cut vertex (e.g. Petersen+Petersen at one
  vertex, n=19) gives a connected min-degree≥3 girth-5 graph with a cut vertex
  that is not 3-connected ⇒ S5(n) > A366224(n) at n=19. So the question the
  probe answers is **at what first n it breaks** — finding the smallest
  non-3-connected girth≥5 min-degree≥3 graph. That breakdown n is structural
  (a 1-/2-separator in a low-girth cubic graph) and is exactly where a
  non-3-connected survivor could hide. No confirmed count beyond n=14 recorded
  yet (`code/out/` has none; scripts `code/eg/s5_*.py` stop at the un-run
  frontier). [[code/eg/INDEX.md]]
- **NO4(17) sanity range** (prediction, unconfirmed): pattern_finder's law
  `NO4(n)≈K·3^n·(n−10)!` (locked from n=12) predicts NO4(17) ∈ 30–41M,
  nominal ≈35M. Outside 25–45M flags an enumeration bug. Detail:
  [[code/eg/survivor_sequences.md]].
- Scratch/durable memory hold nothing further on this problem (earlier
  `recall_memory` surface hit an unrelated permutations paper; the graph has no
  other EG entries).
