# Approach: Lovász theta / vector chromatic number as an exact lower-bound certificate

```approach
idea: Lovász theta of the complement — the "vector chromatic number" χ_v(G) = ϑ(Ḡ),
  which sits in the sandwich ω(G) ≤ ϑ(Ḡ) ≤ χ(G) — as a semidefinite-programming
  lower bound on χ that is certified by an exact PSD dual matrix. Its cheap special
  case is the Hoffman bound χ(G) ≥ 1 − λ_max/λ_min. The point is that ϑ(Ḡ) > 4
  is a machine-verifiable proof that χ(G) ≥ 5, and it costs a polynomial-time SDP,
  not an exponential colouring search.
mechanism: The run's only lower-bound oracle today is complete SAT 4-colourability,
  which is exponential and already limits what can be tested. The chromatic problem
  has a relaxation hierarchy (fractional χ_f ≤ vector χ_v ≤ χ), and χ_v = ϑ(Ḡ) is
  exactly a semidefinite program. For every finite unit-distance graph the run
  constructs — including large Minkowski sums and spindles far beyond SAT reach —
  computing ϑ(Ḡ) gives a *lower* bound on χ: if it exceeds 4, non-4-colourability
  is certified. The certificate is a Gram matrix / PSD dual satisfying the SDP
  optimality conditions, checkable in exact arithmetic over the coordinate field
  (principal-minor or exact-Cholesky PSD check, plus a Lagrange-multiplier identity),
  so it obeys the run's no-floats discipline. Even short of 5, the sequence of
  ϑ values across constructions is a new progress metric that the SAT oracle cannot
  provide, and Hoffman's bound is the one-line eigenvalue version to build first.
  Calibration is immediate: the Moser spindle (χ=4) must have ϑ(Ḡ) ∈ [3,4], and
  C5 must give ϑ = √5, both checkable in exact arithmetic.
status: adopted
first-step: implement exact ϑ(Ḡ) for small graphs (sympy SDP / dual-certificate
  verification) and the Hoffman eigenvalue bound, calibrate on C5 (ϑ=√5) and the
  Moser spindle, then evaluate both on Moser+Moser and the next construction tier;
  store the exact certificate matrix per graph.
falsifies: a finite unit-distance graph with ϑ(Ḡ) > 4 that is nonetheless
  4-colourable — impossible by the sandwich theorem, so a *correct* implementation
  has no such case; the real failure mode is that every constructed graph stays
  ϑ(Ḡ) ≤ 4 (the relaxation is too weak to reach 5 on the constructions the run can
  make), which is a precise negative result, not an error.
cost: polynomial (SDP, ~O(n^{3.5}) interior point; Hoffman is a single exact
  eigenvalue computation). Certificate verification is polynomial in n. This is
  the whole appeal: it scales where SAT does not.
precedent:
  - Lovász 1979 sandwich + Knuth "sandwich theorem" statement
  - https://www.sciencedirect.com/science/article/pii/S1572528617300737 (theta SDP variants, sandwich)
  - https://link.springer.com/article/10.1007/s00453-013-9756-5 (theta computable in polynomial time)
  - https://doi.org/10.1023/b:joco.0000038911.67280.3f (theta(Gbar) <= chi(G) unifying bound)
  - Hoffman bound + Moser-spindle/unit-distance treatment: https://doi.org/10.48550/arxiv.2512.13187 (Abiad–Meeus), https://doi.org/10.1016/j.laa.2025.01.036
```

## Verification status on the theorem

The mathematics this approach *relies on* is standard and I confirmed its precise
statement against the literature:

- **Lovász sandwich theorem.** For a graph G, `ω(G) ≤ ϑ(Ḡ) ≤ χ(G)`, where ϑ is
  Lovász's theta function. The concrete SDP definition (max sum of entries of a
  PSD matrix X with tr X = 1 and X_ij = 0 on edges) is confirmed; ϑ(Ḡ) is a
  polynomial-time computable lower bound on χ. (`On the Lovász theta function and
  some variants`, ScienceDirect; the sandwich is Knuth's "sandwich theorem", EJC
  1994.) The vector-chromatic form χ_v = ϑ(Ḡ) is the Karger–Motwani–Sudan naming.
- **Hoffman eigenvalue bound.** χ(G) ≥ 1 − λ_max/λ_min, for graphs with at least
  one edge (Hoffman 1970; confirmed in the 2025 Abiad–Bosma–van Veluw "Hoffman
  colorings" paper and Abiad–Meeus arXiv:2512.13187, which *explicitly* treat the
  Moser spindle and unit-distance graphs as target examples of the eigenvalue /
  vector-chromatic bounds). So the suggested warm-up is genuinely the right one,
  and the machinery has already been pointed at unit-distance graphs in the
  literature — it did not produce a new public bound there, which is a soft signal
  about value, not a refutation of correctness.

**Verification claim:** SANDWICH THEOREM CONFIRMED (asserted by primary sources);
Hoffman bound CONFIRMED (asserted by primary sources); the "ϑ(Ḡ) is a polynomial
lower bound with an exact PSD certificate" mechanism is standard SDP duality. None
of this is a proof that ϑ(Ḡ) > 4 on anything the run can build.

## Value risk — stated honestly

The theorem is safe; the **value is genuinely unknown and the question is
censored at this run's evidence boundary.** Whether any plane unit-distance graph
— or the plane graph itself — has ϑ(Ḡ) ≥ 5 (or just > 4) is precisely the
published-answer tier this run's evidence policy refuses to let me look up
(screens on "vector chromatic number of the plane / Hadwiger-Nelson SDP lower
bound"). So I cannot say from the literature whether this relaxation reaches the
threshold. What I *can* say from general theory:

- The sandwich only forces ϑ(Ḡ) ≥ ω(G) ≤ 3 for finite plane UDGs (no K4 in the
  plane), so ϑ(Ḡ) ∈ [3, ...] — the relaxation gives no bound above 3 for free.
- It is entirely possible that every constructible UDG has ϑ(Ḡ) ≤ 4 while some
  has χ = 5 (relaxation gap). That would be a precise, reportable negative result
  and would *establish* that the SAT route is the only one reaching 5 among these
  constructions.

**Verdict: grounded** (the technique is standard, safe, polynomial-time, and a
legitimately cheap progress metric and pre-filter), with the honest caveat that
whether it ever certifies χ ≥ 5 is unanswered — and the evidence boundary prevents
me from checking the published answer. This is cheap enough to attempt: it is a
polynomial computation where SAT is exponential.

## What would refute it (killed-by)

A *correct* ϑ(Ḡ) implementation cannot exceed χ (sandwich), so the only genuine
failure is value-shaped: every constructed graph has ϑ(Ḡ) ≤ 4 (relaxation gap or
plainly below 5). That is a negative result, recorded as such, and it would
retire the SDP as a *certifier* while leaving it useful as a metric. The Hoffman
warm-up fails for the same structural reason (spectral bound on the spindle /
Moser+Moser will be ≤ 4; below the 5 threshold almost certainly).

## Adoption decision (converging)

**Adopted** — the only candidate that is simultaneously correct, polynomial-time, and a
real lower-bound certificate: ϑ(Ḡ) > 4 is a machine-checkable proof of χ ≥ 5, and
ϑ(Ḡ) ≤ 4 everywhere is a precise relaxation-gap datum. Its value question is decided
cheaply by this run's own oracle, not by a censored lookup.

**Why it beat the others.** The neighbourhood-complex route is refuted outright (its
cost estimate is wrong — N(G) is high-dimensional — and its certifying step is hard
where it matters); the P¹(K) route is a relabelling, not a new line. Theta/Hoffman is
the surviving residue.

**Synthesis (the third option, produced by the two rounds).** Candidate 3's correction
meets candidate 1 here: the *ring of integers* Z[ω] (not field K-points) is the rigidity
lever, and it is exactly for lattice-derived, vertex-transitive unit-distance graphs
that the Hoffman/theta bound becomes a closed-form exact computation — adjacency
eigenvalues are DFT sums over cyclotomic fields, Hoffman is 1 − λmax/λmin, and theta
has its vertex-transitive eigenvalue formula (source before use). So the cheap entry
point is an exact eigenvalue computation on Eisenstein-integer disks/tori, giving the
run a polynomial, exact, optimisable objective over its construction space; any
construction clearing 4 converts immediately into a certified lower bound.

**Sharpened first-step (supersedes the block's).** (1) Exact 0/1 adjacency matrices for
C5, the Moser spindle (7v/11e, from CONTEXT.md) and Moser+Moser (26v/69e). (2) Hoffman
bound 1 − λmax/λmin exactly (sympy characteristic-polynomial roots): confirm C5 = √5,
Moser and Moser+Moser in [3,4]. (3) Exact ϑ(Ḡ) with a dual PSD certificate, calibrated
on C5 (ϑ = √5). (4) Evaluate ϑ(Ḡ) and Hoffman on a first Eisenstein-integer
triangular-lattice disk or torus (vertex-transitive ⇒ DFT eigenvalues), where the
ring-of-integers rigidity lever lives; record every value — anything > 4 is a certified
χ ≥ 5, otherwise a precise relaxation-gap datum.
