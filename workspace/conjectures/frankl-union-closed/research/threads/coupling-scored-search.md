# Scored program search on the coupling constant

```thread
id: coupling-scored-search
question: What does a scored program search over Yu's finite-dimensional
  coupling optimization (the two-atom symmetric P_pq, params α,a1,a2,b1,b2)
  find — where do candidates plateau, and which constraint binds? Does any
  candidate exceed the proved ceiling t̂_max ≈ 0.38235 (which would falsify the
  Γ̂ monotonicity proof), and what richer coupling class would be needed to
  improve the published 0.38234 frontier?
status: open
rests-on: yu-record-0-38234, yu-gamma-hat-nonincreasing, yu-gamma-half-is-phi-over-2
blocked-by: none
next: |
  (1) tool_builder writes code/search/uc-coupling/PROBLEM.md + score.py; the
      searcher must NOT write the scorer (a scored search learns to exploit its
      verifier first). The scorer independently VERIFIES every constraint and
      prints `SCORE: c` or `INVALID: <constraint, violating value>`; exact
      rationals where possible, interval-arithmetic certified LOWER endpoint
      for reals, <10s per candidate, bounded memory (8 GiB).
  (2) Calibrate first: reproduce 0.38234 on Yu's witness (α=0.035, a=0.3300622,
      b2=1, β=0.1560676; Γ̂=1.000008892) before any candidate.
  (3) Spawn searcher, slug uc-coupling, ≥50 candidates.
  (4) Fill SEARCH.md with scored rows + plateau + binding constraint; say
      plainly whether the top score is believed.
```

## Why this direction

The prior `coupling-half` thread resolved the *push to c = 1/2* as outcome (b):
Yu's Prop-1 two-atom relaxation reproduces 0.38234 but its certificate Γ̂(t) is
proved non-increasing in t, so it certifies nothing above t̂_max ≈ 0.38235. That
was a hand-implemented single-parameter push along the certified subfamily
(a1=a2, b2=1). The full 5-parameter space (α, a1, a2, b1, b2) has never been
mapped, and the operator's directive is that this is exactly the shape for a
scored program search: a constant nobody derives in closed form, improved by
constructing a better witness and scoring it. The deliverable is not "beat the
paper" but the *map* — where candidates plateau and which constraint binds —
plus the honest answer whether the top score is believed.

## What would falsify it

A candidate inside Yu's two-atom class scoring strictly above t̂_max ≈ 0.38235
would falsify the proved Γ̂ non-increase (F_t ⊆ F_t′) — that is extraordinary and
must be re-checked against both the proof and the scorer before it is believed.
A score of 0.5 would prove Frankl only if the witness survives independent
re-verification; it is far more likely a scorer exploit. A score above 0.38234
that escapes the two-atom class (a richer coupling object) is the genuine way to
improve the frontier, and is a different, still-open question.

## Reconciliation with established results

- Γ̂(t) non-increasing (proved): within the two-atom class the plateau is
  t̂_max ≈ 0.3823455333667 (Cambie). The binding constraint is expected to be
  `t` itself (the ceiling a ≤ t), not a slack constraint inside the coupling.
- Γ̂(1/2) = φ/2 = 0.8090169943… at the α=0 collapse (proved exact); the global
  sup over α>0 is numerical-only (open in `yugamma-half-collapse`).
- The scorer's calibration target 0.38234 is hand-verified
  (`code/out/yu_optimization_verbatim.md`, Γ̂ = 1.000008892 vs paper 1.00000889).
