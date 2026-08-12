# Thread: pushing past the verification bound with the degree dichotomy

```thread
question: Can the documented verification bound (n≤15 general, n≤29 cubic) be raised by exploiting the independent-set + ≥4/7-cubic structure as a SAT/SMS propagator, and can the P12-free ⇒ C4-or-C8 computer proof be reproduced/beaten?
status: open; n=6-9 UNSAT (base clauses alone unsatisfiable below n=10); n=10 CEGAR NOT converging — needs structural propagators
rests-on: EG-markstrom-dichotomy, EG-predominantly-cubic, EG-verification-bound, EG-markstrom-24-graphs, EG-P12-free-C4C8
blocked-by: the mixed (V1≠∅) case has only the ≤15 general bound; the ≤29 cubic bound is unconditional but not structural; the raw CEGAR loop (solve/block cycles/repeat) does not converge on n=10 — 2865 iterations, 36,459 clauses, 138s, every model has C8 as the sole power-of-two cycle with cycle set {3,5,6,7,8,9,10}
next: add Carr's ≥4/7-cubic + degree-≥4-independent-set propagators as base CNF constraints (not merely cycle-blocking), then re-run n=10 as a test; the 2865-iteration stall is quantitative evidence that pure cycle-blocking enumerates models without structural guidance
```

## Results so far

| n | base_clauses | result | iterations | time | cumulative clauses |
|---|-------------|--------|------------|------|-------------------|
| 6 | 123 | UNSAT iter=1 | 1 | 0.0s | — |
| 7 | 231 | UNSAT iter=1 | 1 | 0.0s | — |
| 8 | 394 | UNSAT iter=1 | 1 | 0.0s | — |
| 9 | 630 | UNSAT iter=1 | 1 | 0.7s | — |
| 10 | 960 | **no decision** | 2865 | 138s | 36,459 |

**n=10 analysis**: Every model has min-degree 3, no C4, and cycle set {3,5,6,7,8,9,10} — the Petersen-like profile with C8 as the sole power-of-two cycle. The CEGAR loop blocks each discovered C8 cycle with a negative clause, but the SAT solver keeps producing new graphs with different C8 cycles. After 2865 iterations, there is no sign of convergence: the per-iteration solve time is increasing (reaching 0.1s toward the end), and the clause accumulation rate is ~13 clauses per iteration. This is effectively enumerating C8-containing graphs one at a time — a brute-force search through the SAT solver. The C8-free cubic space is known to be nonempty at n=10 (Petersen is girth-5), and the no-C4 constraint is automatically satisfied for girth≥5 graphs. The solver is finding C8 cycles in graphs that have girth 3 (triangles present) and blocking them, but the combinatorial space of how triangles and 8-cycles interact on 10 vertices is large.

**Decision**: pure CEGAR with cycle blocking does not converge on n=10. The next step must encode structural constraints (Carr's degree dichotomy) into the base CNF to prune the search space before the solver starts. This is not a tweak — it is a different encoding.

## Resting claims (source-anchored)

- **EG-markstrom-dichotomy** (Markström §4): $G$ splits into an independent set $V_1$ of degree-$\ge4$ vertices plus a nonempty $V_2$ of degree-3 vertices. *Proved.*
- **EG-predominantly-cubic** (Carr Thm 0.1): $\ge4/7$ of vertices are cubic; $4|V_{\ge4}|\le3|V_3|$. *Proved.*
- **EG-verification-bound** (Markström §4 / Royle): no counterexample on $n\le15$ general, $n\le29$ cubic. *Computed & checked (primary).*
- **EG-markstrom-24-graphs** (Markström §4): four cubic $C_4,C_8$-free graphs on 24 vertices, all with a $C_{16}$, one planar. *Computed & checked.*
- **EG-P12-free-C4C8** (Hegde et al. Thm 0.2): every $P_{12}$-free $\delta\ge3$ graph has a $C_4$ or $C_8$; code public. *Computer-assisted proof.*

## Status notes

- The independent-set + degree dichotomy is now **source-anchored to primary literature** (Markström §4), no longer a hearsay citation — this closed ROOT's exact-citation gap for the 17/30 figures (Royle raw 15, Markström raw 29 cubic).
- Method risk for the SAT direction: forcing $V_1$ independent + $\ge4/7$ cubic is a *necessary* condition on a would-be counterexample only if $G$ is minimal — a graph satisfying the conditions need not be a counterexample, so UNSAT would be a real claim but the propagator must be stated as a *filter* that any minimal counterexample passes, not as the full counterexample search.
- Dead-end to record if pursued: Hegde et al. explicitly show the $P_k$-free backtracking method is **not** generalizable to $H$-free for cyclic $H$ (infinite min-deg-3 tree is $H$-free, no power-of-two cycle) or non-path trees (clique-substitution claw-free example). So that technique cannot touch the full conjecture; it only certifies the $P_k$-free class.
