```approach
id: hecke-character-product-l
idea: The four elliptic curves E_d: y² = x³ − d²x for d ∈ {u, v, u+v, u−v}
  are CM curves with CM by Z[i] (j = 1728).  Each corresponds to a Hecke
  Grössencharakter ψ_d of Q(i) of weight 1, whose L-function L(s, ψ_d) =
  L(E_d, s).  The additive relations u + v = (u+v) and u − v = (u−v)
  imply multiplicative relations among the Hecke characters, giving
  L(s, ψ_u) L(s, ψ_v) = L(s, ψ_{u+v}) × (local correction factors).
  Using Gross–Zagier (L'(E,1) ∝ height of a Heegner point, unconditional
  for CM curves of analytic rank 1), the requirement that all four curves
  have rank ≥ 1 forces a linear relation among Heegner-point heights that
  may be impossible.  It is claimed genuinely different from the refuted
  root-number-parity approach because it uses the full first derivative.
mechanism: For the congruent-number curve E_n, L(E_n, s) = L(s, ψ_n) with
  ψ_n a Hecke character of Q(i) attached to n.  The additive relations
  n₁ + n₂ = n₃ are hoped to induce a multiplicative identity among the
  four L-functions at s = 1 and, via the logarithmic derivative and
  Gross–Zagier, a linear identity among the four rank/heights.
status: refuted
killed-by: There is NO identity L(s,ψ_u)L(s,ψ_v) = L(s,ψ_{u+v})×(corrections).
  L-functions of successive quadratic twists of a CM curve do NOT multiply
  into the twist L-function of a sum of the twist parameters.  The product
  of two elliptic L-functions is not an L-function of a third twist; the
  only product object that exists is the Rankin–Selberg convolution
  L(E_u × E_v), a genuinely different L-function of degree 4 with its own
  functional equation, which is NOT equal to L(E_{u+v}) at s=1.  Additive
  relations among u,v,u+v,u−v therefore transfer to NO multiplicative
  constraint on the L-functions.  Gross–Zagier gives a PER-CURVE height of
  the Heegner point equal to c·L'(E,1) only when that single curve has
  analytic rank exactly 1; it never produces a cross-curve linear relation
  among L'(E_u,1), L'(E_v,1), L'(E_{u+v},1).  The whole mechanism rests on
  an identity that does not exist (the first step "derive the identity"
  is impossible), so the local-correction speculation never engages.
first-step: (moot.)  The candidate's own Step 1 — "derive the identity
  L(s,ψ·χ_u)·L(s,ψ·χ_v) = L(s,ψ·χ_{uv})×(corrections)" — is the step that
  is mathematically false: there is no such formula for quadratic twists of
  an elliptic (CM) curve.  The correct object, L(E_u)×L(E_v) as a
  Rankin–Selberg convolution, does not reduce at s=1 to L(E_{u+v}); there
  is no additivity-to-multiplicativity transfer.
precedent: The four-curve framing (E_d:y²=x³−d²x, d=u,v,u+v,u−v) is the
  exact object of the REFUTED root-number-parity-four-curves and
  simultaneous-congruent-numbers-2selmer approaches (closed: root numbers
  give parity only; the four-curve Selmer data is already fully encoded in
  Bremner II's K3 NS — mare k3-ns-rank-12-not-maximal, bremner-on-squares-of-
  squares-II-2001).  Gross–Zagier (Ann. Math. 124, 1986) is a real theorem:
  for an elliptic curve E/Q of analytic rank 1, a Heegner point has
  canonical height = c·L'(E,1)/Ω, c>0 — per curve, no sum identity.
  Coates–Wiles (Invent. Math. 39, 1977): ord L(E,1)=0 ⇒ E(Q) finite for CM.
  None of these provides the cross-curve linear relation the approach needs.
speculation: (superseded.)  The premise "rank ≥ 1 on all four curves forces
  an impossible height relation" is not only unproved, it is structurally
  empty: the four curves are not independent (Bremner II already computed
  their common geometric data through the K3 elliptic fibration), and an
  MSS exists over Q(√3,√133) (extension-field-mss-exist) where the
  corresponding four-curve situation with all rank ≥ 1 is real — so any
  "impossible relation" that fired would also be forbidden over the
  extension, where it is not, proving too much.
```

# Literature check: Hecke-character / L-function product (REFUTED)

Author: research specialist. Date: this round.

## What the reformulation is actually called

The four curves `E_d: y² = x³ − d²x` are the **congruent-number curves**, the quadratic
twiats of `E_1: y² = x³ − x` (j = 1728, CM by Z[i]). Their L-functions are Hecke
L-functions `L(s, ψ_d)` of Q(i). The proposed engine is a **multiplicative relation
among the four twist L-functions** driven by the additive relations on the twist
parameters, evaluated at s = 1 via **Gross–Zagier**.

## The precise theorem the approach invokes, and why it fails here

**Gross–Zagier (1986).** For E/Q an elliptic curve of analytic rank 1, if K is an
imaginary quadratic field satisfying the Heegner hypothesis and P_K is the Heegner
point, then `ĥ(P_K) = c · L'(E,1)/Ω` for an explicit positive constant c.

- This is one-curve-at-a-time. It relates the height of THE Heegner point on a
  SINGLE curve to that curve's L'(E,1). It says nothing about a relation among
  L'(E_u,1), L'(E_v,1), L'(E_{u+v},1).
- The approach's mechanism (`L'(E_u,1)/L(E_u,1) + ... = L'(E_{u+v},1)/L(E_{u+v},1)`)
  requires the product identity `L(s,ψ_u)L(s,ψ_v) = L(s,ψ_{u+v})×corrections` to take
  a logarithmic derivative. **That identity does not exist.**

## Is there any published product identity for quadratic twists that adds the twist parameter?

No. The literature on L-functions of quadratic twists (this round's searches: moments of
quadratic twists of modular L-functions, ratios conjecture for quadratic twists, p-adic
properties of central L-values of twists, nonvanishing of central values over class-group
characters via Rankin–Selberg / Waldspurger) concerns **individual twists** and their
**Rankin–Selberg convolutions**; none establishes that the L-function of the twist by a
*squarefree class that is a sum of two others* factors as a product of the two constituents.
The correct product object is the Rankin–Selberg convolution `L(E_u × E_v)` (degree 4),
which is not `L(E_{u+v})` at s = 1. So the "identity" the candidate names as its first
step is the false step.

## Who has applied it to this problem?

Nobody, and the four-curve framing is itself already-closed ground in this run: the
refuted `root-number-parity-four-curves` and `simultaneous-congruent-numbers-2selmer`
approaches used the same four congruent-number curves. Root numbers gave parity only
(Birch–Stephens); 2-Selmer relations were subsumed by Bremner II's K3 Néron–Severi data.
The L-function product approach is a third attempt at the same four curves with a new
claimed lever (the full derivative instead of parity), but the lever's existence is the
very thing that fails: there is no product identity.

## What it would buy

Nothing obtainable. Even if some relation among the four L-values existed, the MSS
exists over Q(√3,√133) — where the analogous four AP differences are all realised with
all ranks ≥ 1 — so any "impossible cross-curve relation" would also be impossible over
that field, contradicting the extension-field existence. A correct relation among the
four twist L-functions at s=1 would be compatible with the extension-field MSS, and
therefore could not be the Q-vs-extension separator it is being asked to be.

## Verdict

**Refuted.** The mechanism rests on a product identity for quadratic-twist L-functions
that does not exist (only the Rankin–Selberg convolution exists), Gross–Zagier is
per-curve and never gives the needed cross-curve linear relation, and the four-curve
framework is already the object of two refuted approaches plus a live witness
(extension-field MSS, Bremner's rank-2 witness curve) that any firing relation would
have to survive — and by extension-field existence it cannot.
