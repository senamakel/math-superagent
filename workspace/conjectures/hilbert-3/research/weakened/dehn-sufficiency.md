# Ladder — Dehn invariant sufficiency, weakened rung by rung

The full-strength target is two open conjectures (H3.n and H3.hyp in
`problem.md`). This file does not restate the goal as a target to prove; it
weakens it, switching off one named obstruction at a time, weakest first. A
rung that is `settled` is a real result the run has banked — never the goal
itself. Nothing here is established yet: the workspace is fresh, every ledger is
empty, and every rung is `open` until the forward loop attacks it.

```ladder
goal: (H3.n) For n >= 5, two Euclidean polytopes of equal volume and equal Dehn invariant are scissors congruent; AND (H3.hyp) in H^3 and S^3 the Dehn invariant together with volume is a complete invariant of scissors congruence.
difficulties: universal-over-all-pairs, sydler-no-lift-to-n5, no-known-third-invariant, vanishing-is-Q-linear-independence, no-scaling-in-curved-space, surjectivity-and-kernel-both
status: open
```

The six obstructions, named precisely so the rungs can be told apart:

- `universal-over-all-pairs` — the conjecture quantifies over every pair of
  polytopes; a proof must handle arbitrary polytopes, not a family or one pair.
- `sydler-no-lift-to-n5` — Sydler's cohomological proof that the Dehn-invariant
  map is surjective is specific to n=3 (Jessen reduces n=4 to n=3); the
  homological groups controlling the kernel change in n>=5 and the
  surjectivity argument does not lift. This is why n>=5 is open.
- `no-known-third-invariant` — a negative resolution needs a new invariant
  proved invariant under cutting and reassembly; no candidate exists, which is
  exactly why the conjecture is believed and why nobody can prove it.
- `vanishing-is-Q-linear-independence` — D(P)=0 is a Q-linear-independence
  statement about the angles theta_i/pi in R/piQ; deciding it needs
  transcendence theory (Niven, Baker), and a high-precision zero is not a proof.
- `no-scaling-in-curved-space` — in H^3/S^3 volume is rigid (Mostow) and of
  Dehn type, so the Euclidean scaling argument that separates volume from Dehn
  is unavailable. An argument transported from R^3 must name where scaling
  entered; this is the single most common way a claim here is wrong.
- `surjectivity-and-kernel-both` — completeness is the conjunction "the
  invariant map P(X) -> R (+) (R (x) R/piQ) is surjective" AND "its kernel is
  zero"; both halves are open in the target geometries/dimensions.

```rung
id: R-euclid-rational-dissection
statement: A published Euclidean 3-dimensional scissors congruence between two named polytopes whose dihedral angles are rational multiples of pi (e.g. a cube-to-rectangular-box dissection, or Sydler's prism dissection) verifies exactly: the listed pieces tile the source, their images tile the target, each map is an isometry of R^3, and volume and Dehn invariant match. The cube returns Dehn invariant 0 (trivial, since pi/2 in piQ) and a published prism dissection verifies.
off: universal-over-all-pairs, sydler-no-lift-to-n5, no-known-third-invariant, vanishing-is-Q-linear-independence, no-scaling-in-curved-space, surjectivity-and-kernel-both
stance: open
merge: Turning vanishing-is-Q-linear-independence back on means handling a polytope whose dihedral angle is an irrational multiple of pi — the regular tetrahedron, angle arccos(1/3) — and proving arccos(1/3)/pi irrational (Niven's theorem: 1/3 not in {0, +-1/2, +-1}) rather than observing D != 0 numerically. This is the oracle guardrail the run must build anyway, so it is the first thing to attack.
```

```rung
id: R-euclid-tetrahedron-independence
statement: The Dehn invariant of the regular tetrahedron is provably nonzero: compute D exactly as a sum over its six edges (each length a, dihedral angle arccos(1/3)) and prove arccos(1/3)/pi is irrational by Niven's theorem, so 6a (x) arccos(1/3) != 0 in R (x) R/piQ. The verdict is proved, not numerical. This is the nonzero control the oracle is measured against.
off: universal-over-all-pairs, sydler-no-lift-to-n5, no-known-third-invariant, no-scaling-in-curved-space, surjectivity-and-kernel-both
stance: open
merge: Turning no-scaling-in-curved-space back on means leaving Euclidean geometry for H^3, where volume is rigid and of Dehn type and the scaling engine is gone. The first move is to set up exact hyperbolic Dehn-invariant computation (dilogarithm / Bloch group) for one named hyperbolic polytope, since the Euclidean edge-sum formula no longer separates volume from Dehn.
```

```rung
id: R-hyp-one-certificate
statement: An explicit, certified scissors congruence between two named hyperbolic 3-polytopes of equal volume and equal Dehn invariant, found by search: a finite list of pieces and isometries of H^3, verified exactly to tile the source and (after the isometries) the target, with volume and Dehn invariant matching — the Dehn match proved by Q-linear independence of the angles/pi, not observed. Even a single such certificate is unrecorded in the literature and is direct evidence for H3.hyp.
off: universal-over-all-pairs, sydler-no-lift-to-n5, no-known-third-invariant, surjectivity-and-kernel-both
stance: open
merge: Turning surjectivity-and-kernel-both back on means going from one certificate to a completeness statement for a restricted family — which requires showing the invariant map is surjective AND kernel-trivial on that family, not merely producing one pair that matches.
```

```rung
id: R-hyp-family-completeness
statement: Completeness of volume + Dehn for a named restricted family of hyperbolic 3-polytopes (e.g. ideal tetrahedra, or hyperbolic orthoschemes), with the obstruction to removing the family restriction named exactly: which step of the surjectivity-or-kernel argument fails to extend from the family to all polytopes.
off: sydler-no-lift-to-n5, no-known-third-invariant
stance: open
merge: Two branches open from here. (Affirmative, Euclidean high-dim) Turning sydler-no-lift-to-n5 back on means moving from H^3 to Euclidean n>=5, where Sydler's surjectivity proof does not lift; the first move is to identify precisely which step of Sydler's cohomological argument fails in n=5. (Negative) Turning no-known-third-invariant back on means searching for a new invariant, beyond volume and Dehn, that is provably invariant under cutting and separates two polytopes of equal volume and Dehn.
```

```rung
id: R-dim5-subclass-completeness
statement: Completeness of volume + Dehn for a named restricted subclass of 5-dimensional Euclidean polytopes (orthoschemes, or products of lower-dimensional pieces), with the precise step of Sydler's argument that fails to lift to n=5 identified, and the obstruction to removing the subclass restriction named. This is the honest deliverable GOAL.md names for the n>=5 line: a smaller result than the conjecture and a genuinely useful one.
off: no-known-third-invariant, no-scaling-in-curved-space
stance: open
merge: Turning no-known-third-invariant back on means the negative direction in dimension 5: search for a new invariant (beyond volume and Dehn) that is provably invariant under cutting and separates two 5D polytopes of equal volume and Dehn — the outcome nobody expects, and the most valuable available.
```

```rung
id: R-negative-separating-invariant
statement: A new invariant of polytopes, distinct from volume and Dehn, proved invariant under cutting and reassembly, that separates two named polytopes (in H^3, S^3, or R^n, n>=5) of equal volume and equal Dehn invariant. The invariance under cutting is proved; the separation is exact. This is a negative resolution for a restricted class — a rung, not the full conjecture.
off: universal-over-all-pairs
stance: open
merge: Turning universal-over-all-pairs back on means the separating invariant works on all polytopes, not a restricted class — i.e. a full negative resolution of H3.n or H3.hyp. This is the top of the ladder; reaching it is the goal, and the ladder is exhausted only if it is reached.
```

## What the run should attack next

`R-euclid-rational-dissection` — the bottom rung. It is the oracle guardrail
the run must build regardless (GOAL.md phase 3 requires the dissection checker
and the cube-returns-0 / prism-verifies controls), so attacking it costs
nothing the run was not going to spend, and settling it banks the first real
result: a machine-checked Euclidean dissection. `R-euclid-tetrahedron-independence`
rides along for free, since the regular-tetrahedron nonzero control is the
other guardrail and its proof is Niven's theorem — a one-line transcendence
argument, not a computation.

## Which difficulty I expect to bite

`no-scaling-in-curved-space`. The bottom two rungs are Euclidean and settle by
building the oracle; the obstruction that actually stops the run is the one that
kills every argument transported from R^3 into H^3, and it first bites at
`R-hyp-one-certificate`. There the Euclidean edge-sum formula for the Dehn
invariant no longer separates volume from Dehn (volume is itself of Dehn type,
via the dilogarithm), and even a single certified hyperbolic dissection requires
exact Bloch-group arithmetic and a proved Q-linear-independence of the
angles/pi. That is the rung where the run either produces genuine evidence for
H3.hyp or learns exactly where the curved-space obstruction lives — and either
is a real partial result.
