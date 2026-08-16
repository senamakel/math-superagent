# Parity shadow of the switch set in the Boolean lattice

```approach
idea: nu2(n) is the PARITY SHADOW of the reflected switch-position set in the
Boolean lattice. Let S = {j : h[j]=1} be the switch positions, S' = {n-1-j : j in S}
their reflection. Then the fold cell is T(n,d) = |S' cap down(d)| mod 2, so
nu2(n) = #{ d in [2,n-1] : |S' cap down(d)| odd } = |odd-shadow of S'|.
The witness is exactly this: h=00000010 gives S'={1}, odd shadow {3,5,7} (nu2=3);
h'=00000100 gives S'={2}, odd shadow {2,3,6,7} (nu2=4). A single point u has
odd-shadow size 2^{m-pc(u)}, linear in n whenever pc(u)=O(1).
mechanism: Boolean-lattice isoperimetry (Kruskal-Katona minimal shadow at the
compressed/initial-segment extremal; Harper's vertex-isoperimetric theorem) is
proposed as a LOWER-BOUND tool for the size of the odd shadow. The target
theorem: |odd-shadow(S')| >= c·(max single-point shadow among S') unless S'
cancels into the kernel span(even-alt, odd-alt); kernel-avoidance is the one
arithmetic fact needed from the primes. THIS IS THE ENGINE'S LOAD-BEARING STEP,
and it is FALSE (see killed-by).
first-step: for n=2..64 compute parity-shadow size for subsets S' of the cube,
print dependence on (|S'|, popcount histogram); falsifier: if a SPREAD set S'
(full popcount histogram) has nu2 = o(n), the bound cannot work.
status: refuted
precedent:
  Kruskal-Katona / Harper / shadow-isoperimetry (the named engine, real and
  correctly stated, but cardinality-valued, not parity-valued):
  - "Keevash-Long, Stability for vertex isoperimetry in the cube,
    arXiv:1807.09618 — Harper vertex-isoperimetric theorem, stability,
    K-K via Lovasz form. Whole shadow-isoperimetric toolbox controls
    |ordinary shadow|."
  - "Harper, Optimal assignments of numbers to vertices, J. SIAM 12 (1964)
    — the vertex-isoperimetric theorem on the cube."
  - "Keevash, Shadows and intersections, Adv. Math. 2008,
    doi 10.1016/j.aim.2008.03.023 — Kruskal-Katona lower bounds on
    |ordinary shadow| and its Eulerian/Lovasz forms."
  The parity shadow as a mod-2 zeta / F2-image weight is exactly the fold:
  in-workspace claims fold-rank-is-n-2-nullity-2-alternating,
  excess-is-negative-character-sum (2·nu2 − (n−2) = −S(n)),
  downset-row-intersection-meet-formula (M_d ∩ M_d' = M_{d∧d'}).
  The only real part of the mechanism (a single low-popcount switch does force
  linear parity shadow): enminus2-linear-supply-switch-density-not-necessary,
  fixed-single-1-fold-weight-bounded-by-j.
  No source applies Kruskal-Katona / Harper to a mod-2 zeta (parity) shadow of
  a prime-gap switch set; searches return the shadow-isoperimetric and K-K
  stability literature, none touching a parity count or this problem. Say
  plainly: I found no theorem lower-bounding a parity (mod-2) shadow, because
  the parity shadow is the F2 zeta transform, not the ordinary shadow.
killed-by: >
  The engine's own falsifier fires, with an explicit spread-set witness, and no
  isoperimetric theorem reaches the quantity being bounded. Two independent
  defects, either alone fatal.

  (1) The proposed lower bound is FALSE: spread does NOT imply linear parity
  shadow. The kernel vectors even-alt and odd-alt (claim
  fold-rank-is-n-2-nullity-2-alternating, machine-verified n=2..20) have
  wt(Phi_n x) = 0 — they lie in ker Phi_n — hence parity shadow 0. But
  even-alt is a MAXIMALLY SPREAD set: its elements are all even indices, i.e.
  ~half of EVERY popcount layer of the m-cube (the low bit being 0 is
  independent of popcount, so for every p a positive fraction of the layer-p
  elements have it). So the candidate's own target — "a spread set S' (full
  popcount histogram) forces linear parity shadow" — has a direct
  counterexample with nu2 = 0, and the route's stated falsifier fires without
  any arithmetic. The escape "unless S' cancels into the kernel" names exactly
  the one fact the run cannot prove about the primes (full rank pins the kernel
  to 2 dimensions but cannot say the prime switch set avoids it; measured nu2 ~
  n/2 shows it does, but that is the CONCLUSION of SUPPLY, not an input
  available to the route).

  (2) Kruskal-Katona and Harper bound the CARDINALITY (ordinary) shadow, not a
  mod-2 PARITY count. K-K and Harper are statements about |∂F|/vertex
  boundary: they lower-bound the size of the ordinary shadow/upset of a family
  given its size, at the compressed/initial-segment extremal (Keevash-Long
  arXiv:1807.09618; Harper 1964). The parity (odd) shadow #{d : |S' ∩ down(d)|
  odd} is the mod-2 zeta transform of the indicator of S', the F2 image weight
  wt(Phi_n h) — a PARITY (sum-over-F2) count, which can cancel entirely (odd
  |S' ∩ down(d)| = 0 for every d) even when the ordinary shadow is a constant
  fraction of the cube. The mod-2 cancellation is exactly what isoperimetric
  theorems do NOT control: they never bound the number of ODD intersections of
  a family with a down-set, only the number of sets that contain some member.
  even-alt is again the witness: its ordinary upset is ~half of every layer,
  but its parity shadow is 0.

  Net: the route re-labels the fold weight as a shadow and then asks
  isoperimetry — which is cardinality-blind to parity — to lower-bound a parity
  count. The one case where the bound could hold is the kernel, and there it
  is 0. The claimed "strictly weaker one-point input" (distribution of S' over
  popcount classes) never delivers a lower bound, because a set spread over all
  classes (even-alt) already has zero shadow. This closes GOAL priority 2
  negatively for this candidate.
```

## Distinctness and honesty

Not an ANF/Reed-Muller relabeling and not read-cone-column-equivalence (those
run the zeta transform as the object or the converse direction); this route is
a forward isoperimetric lower bound on the odd shadow. Refuted on evidence:
even-alt is a spread set with zero parity shadow, and isoperimetric shadow
theorems are cardinality-valued. Both facts are structural, independent of any
arithmetic on the primes.
