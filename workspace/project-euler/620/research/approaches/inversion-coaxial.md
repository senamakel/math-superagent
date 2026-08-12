```approach
idea: Coaxial reduction by circle inversion about a limiting point
mechanism: For any two non-intersecting nested circles C (radius R) and S (radius r, centre at distance d from O), the coaxal system they determine has two limiting points L₁, L₂ on the line of centres — the unique points whose power with respect to both circles is equal. Inversion in a circle centred at either limiting point maps C and S to concentric circles C′, S′. Because circle inversion preserves tangency (and the angle between curves), the off-centre PE620 configuration maps to a coaxial planetary gear train where the standard Guo least-mesh-angle theorem applies without caveat: legal planet positions are at multiples of β = 2π/(c+s) in the inverted angular coordinate. Inverting back gives a discrete set of planet centre positions on the original ellipse — one per valid lattice slot. The p and q planets, which have different radii in the original picture, map to circles of the same radius (R′−r′)/2 in the inverted picture (all circles tangent to both concentric circles are congruent), but they occupy different angular slots. The counting problem g(c,s,p,q) becomes: in Z/(c+s)Z, select two positions for type p and two for type q such that, when the inversion is undone, the original planet circumferences are p and q — the inversion radius-transformation formula ρ_original = k²ρ′ / |d_LP² − ρ′²| provides the constraint that picks out which slots are valid for each type. This turns a transcendental root-finding problem into a combinatorial assignment on a cyclic group of order c+s, with the constraint expressed as an algebraic equation in the slot index.
status: refuted
killed-by: inversion_does_not_preserve_tooth_mesh
precedent: https://en.wikipedia.org/wiki/Limiting_point_(geometry) ; https://mathworld.wolfram.com/LimitingPoint.html ; https://mathworld.wolfram.com/Inversion.html ; https://en.wikipedia.org/wiki/Steiner_chain ; https://www.cut-the-knot.org/Curriculum/Geometry/SteinerChain.shtml ; claim `tangent_circle_center_ellipse`, `pappus_center_ellipse_params` (ellipse locus, geometry only)
first-step: (not pursued — refuted at the tooth-count half) Compute the limiting points for C=(0,0,R=c/2π) and S=(d,0,r=s/2π); derive the inversion radius k and the image radii R′, r′ explicitly in terms of c, s, d.
```

## Research verdict (why this is refuted as a *counting* route)

**The geometric half is real and well-sourced.** Constants of classical
inversive geometry confirm every claim the candidate makes about the shapes:
two non-intersecting circles invert to concentric circles under an inversion
about either limiting point (Wikipedia "Limiting point"; MathWorld "Limiting
Point", citing Coxeter 1969), inversion maps circles to circles and preserves
tangency and angles (MathWorld "Inversion", citing Casey 1888), and the
Steiner-chain/porism literature uses exactly this inversion-to-concentric
device, in which chain circles become congruent and equally spaced by 2π/n. So
the transformation of the *geometry* is sound.

**What kills it as a way to count g.** Inversion is conformal, **not an
isometry** — it does not preserve arc length or tooth pitch. The premise of the
approach is that the inverted coaxial train's meshing condition is the standard
Guo least-mesh-angle rule (planet positions at multiples of 2π/(c+s)). But that
rule is a *tooth-count, pitch-1cm metric* statement about the original gears:
1cm of tooth pitch on C maps to a non-uniform pitch on the inverted circle C′,
and the integer tooth totals c, s of the original have no clean integer
commensurability in the inverted frame. The inverted picture gives you the
*continuous* positions (an ellipse before, concentric annulus after) but the
*which-slot-meshes* criterion — the very thing that makes g finite — is
expressed in metre/arc-length/teeth units that do not pass through the
inversion. So the counting problem is NOT reduced to a combinatorial assignment
on Z/(c+s)Z; that group's step does not correspond to the original tooth phases.

Concretely: the candidate's own step "the constraint that recovers the original
planet sizes becomes an algebraic equation in the slot index k ∈ Z/(c+s)Z" is
the crux, and nothing in the inversive literature supplies that equation —
because the inversive geometry that maps the picture cannot carry the metric
teeth data. This is a *structural* objection (conformality ≠ isometry), not a
search-failure. Recorded as claim `inversion_does_not_preserve_tooth_mesh`.

**Separately**, the candidate inherits the coaxial-assumption caveat: even
before inversion, the source rule β=2π/(c+s) is a coaxial-train statement (Guo
eq. 5.21, valid where planets share the axis); its off-centre transfer was the
unchecked step. The inversion was meant to cure that, and it does not, because
the metric tooth condition is not inversive-invariant.

Status: **refuted** (killed-by `inversion_does_not_preserve_tooth_mesh`).
Not a search-failure — the objection is a theorem-level fact about the map.

```claim
id: inversion_does_not_preserve_tooth_mesh
statement: Circle inversion preserves tangency and angles (conformality) but NOT arc length, tooth pitch, rolling contact, or integer tooth counts, so the inverted-coaxial picture of two nested non-concentric circles (which is real: inversion about a limiting point does map them to concentric circles) cannot carry the tooth-phase data that makes the PE620 meshing count g finite. The least-mesh-angle step beta=2pi/(c+s) is a metric tooth-count statement and does not pass through the inversion; hence inversion-coaxial does not reduce g to a combinatorial assignment on Z/(c+s)Z.
hypotheses: circle inversion in the plane; conformal (angle/tangency preserving) but not an isometry; gear meshing depends on pitch (1cm) and integer tooth counts.
holds-here: yes — PE620's gear meshing is a metric/tooth-count condition, exactly what inversion does not preserve.
status: refuted (structural: conformality != isometry).
bearing: closes the inversion-coaxial approach; counting g must stay in the original metric where tooth pitch/teeth are meaningful (or be done in a transform that preserves rolling/tooth structure, which none of the sources supplies).
anchor: research/approaches/inversion-coaxial.md
```

