# Scratchpad

## tool_builder oracle re-run (this session, fourth confirmation — current)

Re-ran the EXISTING `code/brute.py` (no second oracle written, per instruction).

Command: `cd /workspace && PYTHONPATH=/workspace/code python code/brute.py` → exit 0, exact stdout:
```
K4: min degree = 3, cycle lengths = [3, 4], power-of-two cycle lengths = [4]
K3,3: min degree = 3, cycle lengths = [4, 6], power-of-two cycle lengths = [4]
Petersen: min degree = 3, cycle lengths = [5, 6, 8, 9], power-of-two cycle lengths = [8]
cube Q3: min degree = 3, cycle lengths = [4, 6, 8], power-of-two cycle lengths = [4, 8]
K4[g6]: min degree = 3, cycle lengths = [3, 4], power-of-two cycle lengths = [4]
graph6 K4: (3, {3, 4}, frozenset({4}))
```
Every worked example MATCHED its hand-stated answer:
- K4 (n=4):   min deg 3, lengths {3,4}, powers {4} ✓
- K3,3 (n=6): min deg 3, lengths {4,6}, powers {4} ✓
- Petersen (n=10): min deg 3, lengths {5,6,8,9}, powers {8} ✓
- cube Q3 (n=8): min deg 3, lengths {4,6,8}, powers {4,8} ✓
- graph6 K4 "C~": agrees with hand-built K4 (independent from_graph6 path) ✓

All-nonnegative examples are consistent with the conjecture (each has a 2-power
cycle, k>=2). Nothing here disproves δ≥3 ⇒ some 2-power cycle; the Petersen graph
is just the first graph clearing the "no 4-cycle" barrier but still has an 8-cycle.
Runs in well under a minute at n<=10; not pointed at any larger bound (that would
defeat the method — deliberate).

## tool_builder oracle verification (this run)

Ran the EXISTING naive oracle rather than writing a second one, per instructions.
Compute core is `code/lib/cycles.py` (networkx-based exact cycle-length set +
min_degree), exercised through `code/brute.py` and independently through
`code/verify_cycles.py`.

Command: `cd /workspace && PYTHONPATH=/workspace/code python code/brute.py`
Output — every worked example MATCHED its hand-stated answer:
- K4:           min degree 3, lengths {3,4}, powers {4}
- K3,3:         min degree 3, lengths {4,6}, powers {4}
- Petersen:     min degree 3, lengths {5,6,8,9}, powers {8}
- cube Q3:      min degree 3, lengths {4,6,8}, powers {4,8}
- graph6 K4:    agrees with hand-built K4 (cross-check of from_graph6 path)

Command: `cd /workspace && PYTHONPATH=/workspace/code python code/verify_cycles.py`
Output: ALL CHECKS PASSED (expected vs got identical for all four graphs).

The oracle is verified at the exact size the statement's worked examples use
(n <= 10, cycle enumeration exponential but trivial here). Not pointed at any
larger bound — that is deliberately out of scope for this task.

## tool_builder oracle re-run (this session, confirming previous)

Re-ran the EXISTING harness rather than writing a second oracle, per instruction
"if the workspace already holds such a program, run that instead."

Command: `cd /workspace && PYTHONPATH=/workspace/code python code/brute.py` → exit 0:
- K4:           min degree 3, lengths {3,4}, powers {4}
- K3,3:         min degree 3, lengths {4,6}, powers {4}
- Petersen:     min degree 3, lengths {5,6,8,9}, powers {8}
- cube Q3:      min degree 3, lengths {4,6,8}, powers {4,8}
- graph6 K4 ("C~"): agrees with hand-built K4 (cross-check of from_graph6 path)

All match hand-stated answers. Independent second check:
`cd /workspace && PYTHONPATH=/workspace/code python code/verify_cycles.py` →
ALL CHECKS PASSED (expected vs got identical on K4, K3,3, Q3, Petersen).

Verified at the sizes the statement uses (n <= 10); not pointed at any larger bound.

## tool_builder oracle re-run (this session, third confirmation)

Re-ran the EXISTING `code/brute.py` (no second oracle written, per instruction).
Both entry points exercised; all worked examples of problem.md matched.

Command 1: `cd /workspace && PYTHONPATH=/workspace/code python code/brute.py` → exit 0:
- K4:           min degree 3, lengths {3,4}, powers {4}
- K3,3:         min degree 3, lengths {4,6}, powers {4}
- Petersen:     min degree 3, lengths {5,6,8,9}, powers {8}
- cube Q3:      min degree 3, lengths {4,6,8}, powers {4,8}
- graph6 K4 ("C~"): agrees with hand-built K4 (independent from_graph6 path)

Command 2: `cd /workspace && PYTHONPATH=/workspace/code python code/verify_cycles.py` → ALL CHECKS PASSED
(independent harness; MATCH on min_degree and cycle_lengths for all four).

Every worked example matched. Verified at the sizes the statement uses (n <= 10); not
pointed at any larger bound — that is deliberately out of scope for this task.

## pattern_finder note (this run)

At the time of this check the run has produced **no computed integers**:
`research/` holds nothing gathered, `code/` holds no checker or program output,
`reflections/` is empty, and `MEMORY.md`/`SCRATCHPAD.md` contain only the seeded
rows. There is no integer sequence on disk to run `analyze_sequence` or
`find_linear_recurrence` over, so no regularity can be reported as exact and no
conjecture can be stated from computed data.

Per guidance: reporting no pattern is valued above inventing one from too few
terms. Re-check after Phase 3 (the oracle) has produced numbers — e.g. the count
of connected minimum-degree-3 graphs by order, or cycle-length spectra of
generated small graphs. Those counts/spectra are the sequences this role should
be handed.

## pattern_finder note (second check — after Phase 3 numbers landed)

Findings over the sequences now on disk:

1. **Survivor/girth sequences too thin to mine.** `S5(n)` (connected min-degree-3,
   girth>=5) is `0,0,0,0,0,0,1` — a single nonzero term (Petersen at n=10).
   `analyze_sequence` confirms no polynomial/recurrence structure; there is nothing
   exact to conjecture. The n=10 survivor is Petersen, cycle lengths {5,6,8,9}
   (recomputed directly this run) — it has an 8-cycle, so it is NOT a counterexample,
   just the first graph clearing the "no 4-cycle" barrier. To clear the next barrier
   (no 8-cycle) needs girth>=9, Moore-min-n=46; the one after (no 16) needs n>=766.

2. **A007112 (count of connected min-degree>=3 graphs) has no exploitable low-order
   recurrence here.** `total`: 1,3,19,150,2589,84242,5203110,577076528 (matches OEIS
   A007112). `find_linear_recurrence` returned a 4th-order relation with huge rational
   coefficients that fits these 8 points — this is overfitting (a counting sequence has
   no such small constant-coefficient recurrence), and is DISCARDED, not reported as
   structure. Growth is super-polynomial (ratios 3, 6.3, 7.9, 17.3, 32.5…); this just
   reflects the combinatorial explosion of graph counts.

3. **The one exact structure: the Moore-bound threshold sequence.** The minimum number
   of vertices a min-degree-3 graph needs to avoid all 2-power cycle lengths up to 2^m
   is, by the Moore bound (BFS ball of radius floor((g-1)/2) around any vertex is a
   regular tree when min degree d, girth g):
     n_min(m) = 1 + 3·sum_{i=0}^{2^(m-1)-1} 2^i = **3·2^(2^(m-1)) − 2**.
   Terms (avoid 2,4,8,16,32): 10, 46, 766, 196606, 12884901886. This is a PROOF-level
   statement (Moore bound is a theorem), not a conjecture. Both `analyze_sequence` and
   `find_linear_recurrence` correctly find no low-order recurrence — it grows as
   exp(exp(m)), exactly as one expects for these exponentially-spaced barriers.

   **What this says for the run:** a counterexample avoiding the first k = m−1 power
   barriers must be enormous once girth is high — but low girth is exactly where
   small cycles (lengths 4,8) already appear, and the δ≥3 gap machinery
   (two admissible cycles, Consecutive-lengths, both in L1.1) is what must convert a
   sparse predominantly-cubic structure into a 2-power. The barrier sequence shows
   Moore-girth alone is NOT a usable obstruction at accessible n: you can clear 4 with
   n=10 but 8 needs 46 and 16 needs 766, so a genuine counterexample runs into the
   known ≥17/≥30 verification floor long before girth forces anything. The structural
   fight is in low-girth cubic-dominated graphs, not in the girth regime.

**Bottom line:** no new integer-sequence regularity beyond the Moore closed form; the
   survivor counting data (Phase 3) is still too sparse to extract a conjectured
   recurrence or closed form. Re-mine only after the oracle pushes survivor counts to
   larger n (past 30), or once a cycle-length-spectrum sequence for a near-counterexample
   family (e.g. Markström's 24-vertex only-16-cycle graphs) is produced.
