# Lu (2026) bundle script — verify_h14_center_global_domains.py

<!-- src: arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/certificates/verify_h14_center_global_domains.py | plain text. Full text: [[lu-h14-3-verify-center-global-domains.py.full]]. -->

```claim
id: lu-h14-3-global-center-domains-checked-statements
statement: For the H14^3 reversible centre component x'=-y+Bx^2+my^2, y'=x(1+y)
  (z=1+y), H=(1/2)z^(-2B)x^2+V(z) with V_z=z^(-2B-1)((z-1)-m(z-1)^2) is a first
  integral (zero Lie derivative), the extra critical point is (0,1/m), and the
  source-minus-saddle potential barrier equals
  2(B+m)/((-2B)(1-2B)(2-2B))*((1+m)/m)^(1-2B). For the quadratic centre
  component x'=-y+Bx^2-By^2+ax, y'=(1+y)(x-ay), (1+y)k/(a^2-1) (with the given
  invariant conic k) is an inverse integrating factor, the gate point
  (-a/B,-1/B) is critical with Jacobian determinant (B-1)(a-1)(a+1)/B, and the
  conic restricts to (a-1)(a+1)(By+1)^2 on x=ay.
hypotheses: H14^3 two global centre components as in Lu arXiv:2607.13785v2;
  exact symbolic polynomial identities.
holds-here: yes
status: asserted
bearing: the domain/barrier half of Lu's Theorem-1 remainder that is at least
  machine-checkable; closes CONTEXT gap-2 at the holding level; a clean-room
  re-run would upgrade to checked.
anchor: research/sources/lu-h14-3-verify-center-global-domains.py.full.md
follows-from: lu-h14-3-bundle-scripts-now-held
answers: the Lu-2026-bundle-scripts gap (gap-2 in CONTEXT)
```

## What this script establishes (exact checks on the two global H14 centre components)

Symbolic-identity checks for both known centre components of the H14³ protein
field, i.e. the **domain-completeness / barrier half** of the claim (the part of
Lu's Theorem-1 human-proof remainder that is at least machine-checkable):

**Reversible component** — `ẋ = −y + Bx² + my², ẏ = x(1+y)` (z=1+y):
- First integral `H = ½ z^{−2B}x² + V(z)` with `V_z = z^{−2B−1}((z−1) − m(z−1)²)`
  has **zero Lie derivative** (assert `X(H)=0`).
- Extra critical point `(x,y)=(0,1/m)`; the potential's second derivative at the
  gate `z_s=1+1/m` is `−(m+1)/(m(1+1/m)^{2B})`.
- **Source-minus-saddle barrier identity**: the potential difference
  `V(−∞)−V(z_s)` equals
  `2(B+m)/((−2B)(1−2B)(2−2B)) · ((1+m)/m)^{1−2B}`.

**Quadratic component** — `ẋ = −y + Bx² − By² + ax, ẏ = (1+y)(x−ay)`:
- **Inverse integrating factor** `(1+y)·k/(a²−1)` with the invariant conic `k`
  (degree-2 polynomial given in full) satisfies the inverse-factor PDE
  `p·k_x + q·k_y = div(p,q)·k`.
- Gate (extra) critical point `(x,y)=(−a/B, −1/B)`: p, q, k all vanish there;
  gate Jacobian determinant `= (B−1)(a−1)(a+1)/B`.
- Invariant-conic restriction to the axis `x=ay` factors as
  `(a−1)(a+1)(By+1)²`.

## Hypotheses / holds here

Quadratic H14³ reversible and quadratic centre components. **Holds here: yes as
asserted-by-source** — the script is HELD (closes the second missing-bundle row),
and the statements it checks are exact algebraic identities. **Not yet
re-executed in this workspace**; unlike the focal-value half it overlaps only
partially with this run's clean-room verify_lu_core.py (which covered the
Darboux cofactors, not these global domain/barrier identities), so these remain
asserted-by-source until a clean-room run is captured.

**Evidence class: asserted-by-source** (original bundle script held; not yet
re-executed here).

## Bearing / implication

- Together with verify_h14_center_bautin.py, closes CONTEXT gap‑2 (both bundle
  scripts now held) at the level of *holding*, not verification.
- This is the domain/barrier input that Lu's existential-cyclicity conclusion
  needs; a clean-room re-run in code/ (capture to code/out/) is the honest next
  verification step and would upgrade this row to `checked`.
- Does NOT establish the analytic root-uniqueness / domain completeness of Lu's
  Theorem 1 in full — only that these exact algebraic checks pass.
