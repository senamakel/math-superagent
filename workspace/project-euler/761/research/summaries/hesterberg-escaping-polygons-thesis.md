# Hesterberg, Adam Classen — "Closed quasigeodesics, escaping from polygons, and conflict-free graph coloring" (MIT Ph.D. thesis, 2018)

Source: https://erikdemaine.org/theses/ahesterberg.pdf (also hdl.handle.net/1721.1/117875).
Full text: `research/sources/hesterberg-escaping-polygons-thesis.full.md`.
This is the **primary original source** behind Abel et al., "Escaping a Polygon" (arXiv:2007.08965); Chapter 2 of the thesis is that paper's ancestor. The thesis is under copyright (MIT); local copy is for this run's reading only.

## What the source establishes — the part relevant to PE 761 (Chapter 2, "Escaping from Polygons")

Setup as in PE 761 / Abel et al.: a human (escaper) moves continuously at speed 1 inside a polygon P trying to reach the boundary; a zombie (pursuer) moves at speed r outside P trying to be at the boundary when the human arrives. For what r can the human escape vs. the zombie catch?

- **Theorem 2.2.1 (circle).** Let φ ≈ 0.43π be the angle with tan φ = π + φ. Then the critical speed ratio for a **circle** is r\* = sec φ ≈ 4.60 (≈ 4.60333885). While the human is within distance cos φ of the center they can keep diametrically opposite the zombie; then they dash on a tangent chord. **This is exactly the PE 761 circle oracle V_circle** and an independent primary derivation of it (the same tan φ = π + φ identity as the Ponder-This / stewbasic circle limit).
- **Theorem 2.2.2 (wedge).** If P is an unbounded intersection of halfplanes with extreme angle 2θ ∈ (0, π], the critical ratio is r\* = csc θ.
- **Theorem 2.3.1 (lower bound).** For any polygon P, r\* ≥ max_{p,q ∈ ∂P} dz(p,q)/dh(p,q), where dz, dh are geodesic distances in the zombie and human play areas.
- **Theorem 2.3.2 (upper bound).** r\* ≤ 9.2504 · max_{p,q ∈ ∂P} dz(p,q)/dh(p,q) (the thesis's constant; the later Abel et al. paper tightens to 2(3+√6) ≈ 10.89898 in a slightly different model). For a center-started human / edge-midpoint runner, the boundary-time equalization at the optimal exit pair reduces exactly to the stewbasic n-gon formula's max-over-boundary-points structure.
- **Theorem 2.3.3 + (PTAS).** A pseudopolynomial-time approximation scheme exists (r\* to within 1+ε).

## Why it matters for this run

It is a **third independent, primary derivation of the circle constant** (tan φ = π + φ, r\* = sec φ), standing alongside IBM Ponder This May 2001 and stewbasic's n-∞ limit. It confirms the two-phase mechanism rigorously (keep-opposite stage radius cos φ of center, then tangent chord) — the same template the n-gon formula generalizes. It does **not** give a regular n-gon (hexagon) exact value: the thesis's exact list is circle and wedge only, and its 9.2504 bound is far too coarse for an 8-decimal answer. So like Abel et al., this source **supports the model and the circle/square anchors but is not a route to V_hexagon**.

```claim
id: hesterberg-circle-critical-speed-primary
statement: The critical speed ratio for escape from a circle (human speed 1 inside, zombie speed r outside) is r* = sec φ ≈ 4.60333885 where φ satisfies tan φ = π + φ (φ ≈ 1.3518168 rad); the human stages within radius cos φ keeping diametrically opposite the zombie, then dashes on a tangent chord.
hypotheses: circular lake of radius 1, human starts at center, zombie on boundary, continuous play, optimal strategies, escape = reach boundary before the zombie; re-derivation in the (P, ε, z, h) continuous-game model.
holds-here: yes - this is precisely the PE 761 circle case and reproduces V_circle = 4.60333885 from a primary thesis derivation.
status: proved (MIT Ph.D. thesis Theorem 2.2.1).
bearing: independently corroborates the circle anchor and the keep-opposite-then-dash mechanism; does not give V_hexagon.
anchor: research/sources/hesterberg-escaping-polygons-thesis.full.md
```

## What it does not settle
- No hexagon (or general regular n-gon) exact value — the exact-list is circle + wedge; regular n-gon and hexagon come from the stewbasic formula (n=6), which neither the thesis nor Abel et al. independently covers.
- The 9.2504 approximation is unusable for an 8-decimal answer.
