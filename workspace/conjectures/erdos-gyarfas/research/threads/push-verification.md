# Thread: pushing past the verification bound with the degree dichotomy

```thread
question: Can the documented verification bound (n≤15 general, n≤29 cubic) be raised by exploiting the independent-set + ≥4/7-cubic structure as a SAT/SMS propagator, and can the P12-free ⇒ C4-or-C8 computer proof be reproduced/beaten?
status: open; sources digested, no computation run on this yet
rests-on: EG-markstrom-dichotomy, EG-predominantly-cubic, EG-verification-bound, EG-markstrom-24-graphs, EG-P12-free-C4C8
blocked-by: the mixed (V1≠∅) case has only the ≤15 general bound; the ≤29 cubic bound is unconditional but not structural
next: build a SAT/degree-sequence program that forces V1 independent + ≥4/7 cubic + δ≥3 and searches for absence of C4,C8,C16; if UNSAT past n=29 it is a genuine strengthening. Use the four Markström 24-vertex graphs as a test oracle. Run the Hegde public code path for P12 to confirm the reported times reproduce.
```

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
