# Memory

Durable beliefs this run holds. Every row states its evidence class. Nothing
enters here as a fact because it sounded right. Source-backed structural facts
live in `research/ROOT.md` + `CLAIMS.md`; this file records the run's own
settled belief about what a minimal counterexample must look like and which
obstructions closed which previous attempts.

## Established

| Belief | Evidence | Would be falsified by |
| --- | --- | --- |
| The conjecture is open as of the library's evidence. | Primary-source statement Er96 (Erdős problems): "Every finite simple graph with min degree ≥ 3 contains a simple cycle of length 2^k, k ≥ 2." | A published proof or counterexample the library turns up. |
| Minimum degree 2 is not enough. | A cycle C_n for n not a power of two has δ = 2 and exactly one cycle. | Nothing; immediate. |
| Any counterexample to EG needs ≥ 17 vertices; any cubic one needs ≥ 30. | Asserted by Wikipedia/EG sources; NOT yet reproduced by this run's own oracle (this is the open Phase-3 step). | This run's nauty-geng enumeration turning up a counterexample below the bound, or failing to match the count A007112. |
| A counterexample is **predominantly cubic**: every proper subgraph has a min-degree-2 vertex; regular ⇒ cubic; at least 4/7 of vertices have degree exactly 3; every vertex is adjacent to a degree-3 vertex. | ROOT.md, sealed L2.0/L1.0 (min-order/min-size minimality argument). | A minimal counterexample with a vertex all of whose neighbours have degree ≥ 4. |
| A counterexample is **sparse**: avg degree ≤ exp(O(log* n)) (Sudakov–Verstraëte, powers-of-two = exponentially-bounded even sequence). With δ≥3, avg degree ∈ [3, exp(O(log* n))]. | ROOT.md, sourced. | A dense counterexample with avg degree super-log*-exponential. |
| Restricted classes are closed (never re-derive): P13/P10/P8-free, 3-connected cubic planar, diameter-2, claw-free planar, K_{1,m}-free, Cayley families, large average degree. | ROOT.md list; full refining statements in L1.1 digests. | A counterexample within a closed class. |
| Every δ≥3 graph has two cycles of length 1 or 2 apart (Gao–Huo–Liu–Ma, k=2) and two cycles of consecutive length (Gao–Ma Bondy–Vince k=0). This is the ONLY non-density length guarantee at δ=3. | ROOT.md, sourced. | A δ≥3 graph violating it — would refute the source. |
| Moore-bound girth barrier: min order to clear the first m power barriers (2,4,…,2^m) is 3·2^(2^(m-1)) − 2 (terms 10,46,766,…). Girth alone is NOT a usable obstruction at accessible n (a survivor with girth≥9 needs n≥46, girth≥17 needs n≥766). | Derived this run (Moore bound is a theorem). | A graph beating the Moore bound — impossible by the theorem. |
| The interval obstruction: an interval [a,b] of guaranteed cycle lengths forces a power of two only when b ≥ 2a; below 2^(k+1) the gap is 2^k. | Arithmetic. | Nothing. |

## Under investigation

- Reproducing the n≥17 / cubic n≥30 verification bound with the run's own
  checked oracle (nauty-geng + lib.cycles/egcheck), and catalogs of
  near-counterexamples (Markström's 24-vertex only-16-cycle graphs, one planar).
  Tool_builder run agent-run-5.
- Lean formal statement (lean/erdos_gyarfas.lean) elaborates with `sorry`;
  no lemma yet proved. agent-run-6.

## Failed approaches (including dead ends the literature closed)

| Approach | How it closed / obstruction |
| --- | --- |
| Interval-of-cycle-lengths results ([a,b] or consecutive lengths at δ≥3). | The gap below 2^(k+1) is 2^k, so an interval forces a 2-power only when it spans a factor of two. δ≥3 buys only two consecutive / length-1-or-2-apart cycles (Gao–Huo–Liu–Ma, Gao–Ma), still landing between consecutive 2-powers. This is THE obstruction every attack must beat. |
| Liu–Montgomery large-average-degree result settling "for every r". | Settles only *large average degree*: the guaranteed even interval [log^8 ℓ, ℓ] is wide only at enormous average degree; at δ=3 (sparse) it gives nothing. | 
| Girth/Moore-barrier route to rule out 2-powers. | To clear 4 needs n=10, 8 needs n=46, 16 needs n=766 — a genuine counterexample runs into the ≥17/≥30 floor long before high girth rules anything out. The structural fight is in LOW-girth predominantly-cubic graphs, where small 2-power cycles already appear. |
