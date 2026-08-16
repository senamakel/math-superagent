# Prove Gamma-hat(1/2) = phi/2 — the quantitative ceiling of the Yu/Sawin coupling

```thread
id: yugamma-half-collapse
question: Does the Yu/Sawin two-atom conditionally-iid coupling certificate
  Gamma-hat(1/2) equal phi/2 = (1+sqrt5)/4 = cos(36 deg) exactly, and does that
  give the sharp quantitative ceiling of the Prop-1 relaxation (certification
  needs >= 1, and Gamma-hat(1/2) < 1)?
status: open
rests-on: yu-gamma-half-is-phi-over-2, yu-optimization-objective, iid-barrier-exact
blocked-by: none
next: |
  DONE: the collapsed alpha=0 value Gamma-hat(1/2)=phi/2 is proved by exact
  algebra (claim yu-gamma-half-is-phi-over-2, code/out/yugamma_phi2_claim.md).
  REMAINING: prove (or refute) that phi/2 is the GLOBAL sup Gamma-hat(1/2),
  i.e. no alpha>0 or 4-param two-atom coupling gives g/Eh > phi/2 at t=1/2.
  Currently this is numeric corroboration only (full-4-param SLSQP inf
  0.80901699 at alpha=0; alpha>0 gives smaller infs), not a theorem. Until it
  is proved, the "certificate value AT 1/2 is phi/2" barrier statement must be
  stated as: collapsed value proved, global sup corroborated numerically.
```

## Why this direction

`code/out/yugamma_highprec.py` reports the collapsed Gamma-hat at t=1/2 equals
phi/2 to 60 digits (diff exactly 0.0). That magnitude of agreement is not a
coincidence; it is the exact ceiling of the Yu/Sawin Prop-1 two-atom relaxation.
The certificate is a ratio of binary entropies (log terms), so an exact algebraic
value is non-trivial to prove, but at t=1/2 the h(1/2)=1 collapse should reduce
the ratio to an algebraic expression in Q(sqrt5).

This continues the now-closed `coupling-half` thread: there the push to c=1/2
was resolved as outcome (b) — the optimization is blocked below 1/2, with the
extremal mu exhibited. The collapsed certificate's exact value at 1/2 (= φ/2)
is now proved; the still-open question is whether it is the global sup over the
whole two-atom family, which is what would make "the certificate value AT 1/2
is φ/2" a theorem rather than a numerical corroboration.

## What would falsify it

A coupling at t=1/2 — either α>0 or a different two-atom pair (a1,a2,b1,b2) —
with g/Eh > φ/2 would refute the "global sup" part. The numeric search found
none (α=0.05→0.801, α=0.1→0.770, α=0.2→0.688, all < φ/2), but that is search,
not proof. The collapsed α=0 value itself is already proved (= φ/2) and cannot
be falsified; only the global-sup strengthening is open.

## Outstanding: external novelty

Whether Γ̂(1/2)=φ/2 as the Yu/Sawin certificate value is already stated in the
*external* literature (not this run's own library) is **unchecked**. Two
`request_research` calls declined to queue (the tool answers from the run's own
claim store, which already holds `yu-gamma-half-is-phi-over-2`). Do not claim
novelty in the write-up without this check.
