# Lu (2026) bundle script — verify_h14_center_bautin.py

<!-- src: arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/certificates/verify_h14_center_bautin.py | plain text. Full text: [[lu-h14-3-verify-center-bautin.py.full]]. -->

```claim
id: lu-h14-3-bautin-focal-values-u0
statement: In the H14^3 chart, the Bautin/Lyapunov recurrence gives L1=(AC+CD+2DF-EF)/8.
  Under the H14 omega-parametrization A=B/w, C=a(2B-1)/w^2, D=(a^2(B-1)+m-ad)/w^3,
  E=1/w, F=(a+d)/w^2 with w^2=1-a^2, the reduced L1 numerator (mod w^2=1-a^2) is
  ell1=2B^2a+2Bam-Ba-2a^2d+am-2ad^2-a+2md-d with denominator 8w^5. Both exact centre
  components (a=0,d=0) and (m=-B,d=-a) annihilate the second focal value L2, and
  along the L1=0 branch L2|ell1=0 = (a(B+m)/48)*eps^2 + O(eps^3), i.e. the
  coefficient U(0)=1/48.
hypotheses: H14^3 five-coefficient chart; the rotation recurrence of
  verify_bautin_recurrence/verify_lu_core with radial gauge c_{k,0}=0.
holds-here: yes
status: asserted
bearing: supplies the second focal value's structure on each centre component —
  the content behind Lu's Bautin-trick division of the displacement; a clean-room
  re-run (capture to code/out/) would upgrade to checked.
anchor: research/sources/lu-h14-3-verify-center-bautin.py.full.md
follows-from: lu-finite-core-identity-half-checked, lu-h14-3-bundle-scripts-now-held
```

## What this script establishes (reproducibility certificate for blueprint (B9)–(B10))

Exact sympy recomputation of the focal values of the H14³ center-ideal machinery:

1. **Focal-value recurrence.** With V₂=(u²+v²)/2 and the rotation
   `R = −v∂_u + u∂_v`, iterates the degree-3..6 system
   `R(V_k) + Q₁∂V_{k−1}/∂u + Q₂∂V_{k−1}/∂v = L_{k/2}·(u²+v²)^{k/2}`
   (Q₁=Au²+Cuv+Dv², Q₂=Euv+Fv²), radial-gauge c_{k,0}=0, recovering
   `L₁ = (AC+CD+2DF−EF)/8` (degree 4) and the degree-6 focal value L₂.

2. **H14 ω-parametrization** of the five coefficients:
   `A=B/w, C=a(2B−1)/w², D=(a²(B−1)+m−ad)/w³, E=1/w, F=(a+d)/w², w²=1−a²`.
   Substituting reduces L₁ (mod w²=1−a²) to the numerator
   `ℓ₁ = 2B²a+2Bam−Ba−2a²d+am−2ad²−a+2md−d` with denominator 8w⁵.

3. **Both exact center components annihilate L₂**: `L₂|(a=0,d=0)=0` and
   `L₂|(m=−B,d=−a)=0`.

4. **Along the L₁=0 branch** (ℓ₁ solved to 2nd order in the radial ε-scaling,
   d=−εa+…) the reduced second focal value is
   `L₂|ℓ₁=0 = (a(B+m)/48)·ε² + O(ε³)`, i.e. **U(0)=1/48** — the coefficient
   that measures how the second focal value opens away from the centre
   components.

## Hypotheses / holds here

Quadratic H14³ source-normalized family; the Bautin/Lyapunov recurrence and the
two known centre components. **Holds here: yes as asserted-by-source** — the
script is now HELD (the long-missing bundle row is closed), and the algebraic
content it checks (focal-value recurrence, L₁ numerator, both-components
vanishing, U(0)=1/48) is consistent with this run's clean-room verification of
the same recurrence (`code/bautin/verify_lu_core.py`, capture
`code/out/lu_core.captured.txt`). But this specific script's output has **not**
been re-executed byte-for-byte in this workspace yet — the identity half
(`192·L₆+P30=0`, Darboux cofactors, `8L₄=AC+CD+2DF−EF`) was independently
verified; the two-center-components-vanishing and U(0)=1/48 statements remain
asserted-by-source until run.

**Evidence class: asserted-by-source** (original bundle script held; not yet
re-executed here).

## Bearing / implication

- Closes CONTEXT gap‑2's "two bundle scripts still not held" for this script.
- Supplies the second focal value's structure on each centre component — the
  concrete content behind Lu's Bautin-trick division of the displacement; a
  clean-room re-run (capture to code/out/) is the next verification step and
  would upgrade this row to `checked`.
- Does NOT establish Lu's Theorem 1 (the analytic/domain remainder; existential
  bound); it verifies only the finite algebraic core behind (B9)–(B10).
