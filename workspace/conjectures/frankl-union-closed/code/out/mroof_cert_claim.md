# M♮-certificate over/under-certification — exact claim block

<!-- regenerator-trigger -->
```claim
id: mroof-cert-vs-alb-both-directions
statement: For the support-restricted M♮-concave certificate class over
  union-closed families — Cert(F) = {x : ∃ M♮-concave w, w=0 outside F,
  w≥0, Σ_F w=1, Σ_{x∈A∈F} w(A) ≥ 1/2} — compared with Alb(F) = {x :
  density_x ≥ 1/2}, BOTH over-certification (Cert ⊋ Alb) and
  under-certification (Cert ⊊ Alb) occur at every n ≥ 2. Exact counts:
  n=2 over 2/13, under 2/13; n=3 over 24/121, under 46/121, rigid 51.
  n=4 COMPLETE sweep (all 4959 UC families, code/out/mroof_sweep.py, 20228
  exact solves): over 686/4959, under 2992/4959, totally-uncertifiable
  (Cert∩Alb=∅) 2789/4959 (2788 with nonempty Alb), Cert==Alb 1281/4959.
  (The earlier partial n=4 pass — 932 families in a 240s budget — gave over
  110, under 663; the complete sweep supersedes those figures.)
  Over-cert exemplar
  F={∅,{x},{x,y}} n=2 (y density 1/3 certifiable); under-cert exemplar
  F={x} n=2/3 and {5,7} n=3 (density-1 element not certifiable).
hypotheses: F finite union-closed subfamily of 2^[n]; M♮-concavity =
  gross-substitutes exchange (disjunction of linear inequalities per
  (X,Y,u)); w restricted to support F; exact real arithmetic (Z3 QF_LRA).
holds-here: yes — computed exactly over ALL UC families n≤4 (complete,
  20228 exact solves, parallel), enumeration counts match A102896
  3,13,121,4959; the M♮-encoding is the canonical code/out/mroof_z3.py
  reused verbatim and cross-checked against hand cases (z3 and cvc5
  agree) plus F={3,7} n=3 verified infeasible-for-all-elements by hand.
status: verified-computationally (exact, n≤4 COMPLETE).
bearing: NEGATIVE for the discrete-convex-weighting approach as a proof
  route. The support-restricted M♮-class neither proves UC (under-certifies
  abundant elements including density 1) nor characterises abundance
  (over-certifies non-abundant x), so Cert ≠ Alb is the norm, not a rigid
  stepping stone. NOT a UC result; UC is machine-verified to n=12
  (bosnjak-markovic-11) independently of this.
anchor: code/out/mroof_cert_vs_alb.captured.txt; program
  code/out/mroof_cert_vs_alb.py; encoding code/out/mroof_z3.py.
ceiling: n=4 partial (932/4959 families within 240s); exact over all
  families only for n≤3.
```

## What the capture settles

The open task `mroof-cert-probe-execute`'s decisive question — "find ANY
family with Cert != Alb (over-certify = approach negative; rigid Cert=Alb =
positive stepping stone)" — is answered: **both** directions occur, and
under-certification (the class too small, losing density-1 elements) already
kills the class as a UC proof route. `code/out/mroof_cert_vs_alb.captured.txt`
is non-empty and exits 0.
