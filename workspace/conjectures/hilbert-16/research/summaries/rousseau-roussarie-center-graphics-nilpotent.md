# Roussarie–Rousseau 2015 — finite cyclicity of (I¹₁₄) and boundary sets

Full text: [[rousseau-roussarie-center-graphics-nilpotent.full]]. arXiv:1506.07104.

## What the source establishes

Methods to prove finite cyclicity of graphics through a **triple nilpotent point
of saddle or elliptic type surrounding a center**, in quadratic systems. The
general method is the **Bautin trick**: writing the displacement map as a finite
sum of "generalized monomials" times nonvanishing functions,
V(z) = Σᵢ aᵢ mᵢ(1 + hᵢ(z)), where the aᵢ lie in the **center ideal** in parameter
space. This is possible because in quadratic systems the center conditions are
known: all such graphics surrounding a center occur in the stratum of **reversible
systems** (symmetric about an axis, Darboux integrable with an invariant line and
invariant conic). Blow-up of the family yields a singular 3-dimensional foliation.

**Theorems.** After blow-up, finite cyclicity of the graphic reduces to finite
cyclicity of a finite collection of limit periodic sets; the hardest is the
*boundary* limit periodic set (a 2-dimensional displacement map whose zeros are
studied along an invariant foliation, with a generalized derivation operator).

- **Theorem 1.1** (partial): the *boundary* limit periodic set of each of
  (I¹₁₄), (I¹₆b), (H³₁₃), (DI₂b) has finite cyclicity.
- **Theorem 1.2** (complete): the graphic **(I¹₁₄) has finite cyclicity** inside
  the family of quadratic vector fields.
- **It does NOT close (I¹₆b), (H³₁₃), (DI₂b) fully:** for these only the boundary
  set is done (Theorem 1.1); finite cyclicity of the full graphics is left for
  future work, with the specific obstructions named: (I¹₆b) involves four Dulac
  maps of the second type and cannot be reduced to a single equation; (DI₂b) has
  four second-type Dulac maps through semi-hyperbolic points.

This **corrects** the librarian's earlier suggestion that RR 2015 closed all four
graphics. Only (I¹₁₄) is fully closed.

## Where the analyticity enters (test 1)

- The division in the center ideal and the "behaves well under derivation" property
  (hᵢ(z) = o(1)) is the analytic profile; the derivation-division (Rolle) procedure
  bounds the number of zeros of the displacement, and it genuinely uses the
  structure of the Dulac maps and the center ideal — a C^∞ argument would not close.

## What it lets this run do

This is the model for attacking a **remaining open** graphic: the machinery for
center graphics through a nilpotent point exists and is partly published. The
remaining candidates with full cyclicity unproved are (I¹₆b), (H³₁₃), (DI₂b)
(center-type, boundary done) — the natural targets for G-drr-status. A reproducible
computation: reproduce the Dulac-map 2nd-type expansion and the boundary-set
derivation-division for one named graphic symbolically, matching the published
result as a check.

```claim
id: drr-rr-closes-i14
statement: The DRR graphic (I^1_14), through a triple nilpotent point of saddle
  or elliptic type at infinity surrounding a center, has finite cyclicity inside
  the family of quadratic vector fields.
hypotheses: n=2; graphic surrounds a center (reversible stratum); family
  compactified in S^2 × K.
holds-here: yes
status: asserted
bearing: closes (I^1_14) fully, bringing the count to 89 of 121 after RSZ's 88;
  demonstrates the Bautin-trick + blow-up-to-3D-foliation method for center
  graphics through a nilpotent point.
anchor: research/sources/rousseau-roussarie-center-graphics-nilpotent.full.md
follows-from: h16-drr-121-graphics
```

```claim
id: drr-rr-boundary-only-for-3-graphics
statement: For the DRR graphics (I^1_6b), (H^3_13) and (DI_2b) through a triple
  nilpotent point at infinity surrounding a center, only the boundary limit
  periodic set obtained in the blow-up has proved finite cyclicity (Theorem 1.1);
  the full finite cyclicity of these three graphics is not established by this
  source.
hypotheses: n=2; center-type graphics; boundary set done, remaining limit
  periodic sets open.
holds-here: yes
status: asserted
bearing: THE target set: these three graphics (plus other not-listed rows) are
  the remaining open center-type cases; the run's finite-cyclicity attack should
  target one of them.
anchor: research/sources/rousseau-roussarie-center-graphics-nilpotent.full.md
contradicts: drr-88-then-closed-all-four (the librarian overclaim)
follows-from: h16-drr-121-graphics
```
