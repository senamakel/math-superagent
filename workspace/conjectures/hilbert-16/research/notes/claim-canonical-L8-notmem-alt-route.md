h16-2-local-cyclicity/L8-not-in-L4-L6

# L8 ∉ ⟨L4, L6⟩ — second independent route, and the general certificate

node: h16-2-h14-3-finite-cyclicity / G-lean-cert
kind: formalisation (kernel-checked), plus a second independent witness

## What closed

1. `code/lean/Lib/Certificate.lean` — **VERIFIED** (lean_check), no sorry, no
   cited axiom, axioms `[propext, Classical.choice, Quot.sound]`:
   - `eval_cert_nonmem (φ : R →+* S) : φ f1=0 → φ f2=0 → φ f3≠0 →
     f3 ∉ Ideal.span {f1,f2}`
   - `eval_point_cert_nonmem`: same with `φ = MvPolynomial.eval p`.
   This is the quotient-homomorphism / linear-functional certificate. It
   upgrades the Gröbner-only claim that L8∉⟨L4,L6⟩ to a route the kernel
   checks from evaluations. Status `formalised`.

2. `code/lean/Lib/L8NotInIdeal_alt.lean` — compiles; **Route A closed**,
   Route B is a gap:
   - `second_point_route` at `certPt2 = (-3,-3,2,0,1,-1)`, NON-proportional to
     `Bautin.lean.certPt = (-2,-2,1,-1,-1,1)` → kernel-closed (axioms
     `[propext, Classical.choice, Quot.sound]`).
   - `graded_membership_shape` (Route B, graded degree-6 reformulation) →
     `by sorry`, gap `graded-reformulation-L8`.

## Second witness evidence

`code/bautin/cofactor_certificate2.py` (exact sympy; full-box sweep {-3..3}^6
with proportionality check vs certPt), capture
`code/out/cofactor_certificate2.captured.txt`: at certPt2,
L4=0, L6=0, L8=-25/8≠0; cleared V1num=0, V2num=0, V3num=-57600 (denoms
8/192/18432). Non-proportional to certPt. This is a genuinely second proof
route to the same statement, so a single arithmetic coincidence in the
focal-value tables cannot be what both rest on.

## What is asserted, not established

- The `h1 h2 h3` evaluation hypotheses of `second_point_route` (and the three
  evals in `Bautin.lean`) are established by exact computation in captures,
  not by the kernel.
- Route B (graded membership) is stated but not proved; the homogeneous-degree
  decomposition of MvPolynomial is the missing machinery.

## status: formalised (for Certificate.lean)
formalisation: code/lean/Lib/Certificate.lean
