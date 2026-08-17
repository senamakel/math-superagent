# Prove Gamma-hat(1/2) = phi/2 — the quantitative ceiling of the Yu/Sawin coupling

```thread
id: yugamma-half-collapse
question: Does the Yu/Sawin two-atom conditionally-iid coupling certificate
  Gamma-hat(1/2) equal phi/2 = (1+sqrt5)/4 = cos(36 deg) exactly, and does that
  give the sharp quantitative ceiling of the Prop-1 relaxation (certification
  needs >= 1, and Gamma-hat(1/2) < 1)?
status: open (partly advanced this pass)
rests-on: yu-gamma-half-is-phi-over-2, yu-optimization-objective,
  iid-barrier-exact, yu-collapsed-alpha0-inf-is-phiover2-via-boppana
blocked-by: none
next: |
  (1) DONE: collapsed alpha=0 value Gamma-hat(1/2)=phi/2 proved by exact algebra
      (yu-gamma-half-is-phi-over-2).
  (2) DONE (this pass): the collapsed alpha=0 INF over the whole collapsed
      two-atom family at t=1/2 is proved = phi/2, as a corollary of Boppana's
      inequality via the binary-entropy symmetry h(1-s^2)=h(s^2). Claim:
      yu-collapsed-alpha0-inf-is-phiover2-via-boppana (status proved).
      Reduction: u(a)=w*h(2a-a^2)/h(a), w=1/(2(1-a)); with s=1-a this is
      (1/2s)*h(1-s^2)/h(s) = (1/2s)*h(s^2)/h(s), so u>=phi/2 iff Boppana.
      Equality at s*=1/phi (1-s*^2 = s*), i.e. a=(3-sqrt5)/2.
  (3) STILL OPEN (numeric-only): the GLOBAL alpha=0 inf over ALL admissible
      two-atom marginals (not just the collapsed sub-family) at t=1/2; and all
      alpha>0. The collapsed boundary is the numeric minimizer, but that the
      general family cannot go below the collapsed one is not a theorem here.
  (4) The full global Gamma-hat(1/2)=phi/2 (sup over alpha of the inf) is not
      proved. The surviving open gap for the entropy-coupling reduction is in
      the strictly larger conditionally-iid class C3 of Liu (arXiv:2306.08824),
      per durable memory -- do not restate the gap at the two-atom ceiling.
```

## Why this direction

`code/out/yugamma_highprec.py` reports the collapsed Gamma-hat at t=1/2 equals
phi/2 to 60 digits (diff exactly 0.0). At t=1/2 the h(1/2)=1 collapse reduces
the ratio to an algebraic expression in Q(sqrt5). This pass proved not just the
collapsed *value* at the extremal but the collapsed *infimum* over the whole
collapsed family: the algebraic reason is that at s*=1/phi, `1-s*^2 = s*`, so
h(1-s*^2)=h(s*), and Boppana pins the ratio at phi/2.

## What would falsify it

- A coupling at t=1/2 — either α>0 or a different two-atom pair (a1,a2,b1,b2) —
  with g/Eh > φ/2 would refute the "global sup" part. Numeric search found none
  (α=0.05→0.801, α=0.1→0.770, α=0.2→0.688, all < φ/2), but that is search, not
  proof.
- The collapsed sub-family result (inf=phi/2) is proved and cannot be falsified.
- The collapsed α=0 value (= φ/2) is proved and cannot be falsified.
- What remains falsifiable: whether the general admissible (non-collapsed) class
  or alpha>0 can beat phi/2 — open, numeric-only.

## Outstanding: external novelty

Whether Γ̂(1/2)=φ/2 as the Yu/Sawin certificate value is already stated in the
*external* literature is **unchecked**. Do not claim novelty in the write-up
without this check. The global-sup part remains the genuine open target.
