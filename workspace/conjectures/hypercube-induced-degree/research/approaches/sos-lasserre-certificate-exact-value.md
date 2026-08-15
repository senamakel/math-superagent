# Sum-of-squares / Lasserre hierarchy: proof certificates for the exact value

```approach
idea: Treat f(n) as a polynomial optimisation and attack the exact value with
the sum-of-squares (Lasserre) hierarchy of convex relaxations. The decision
problem "∃ S, |S|=2^{n-1}+1, D(S) ≤ d" is a binary quadratic feasibility
problem: variables x_v ∈ {0,1}, the degree ceiling D(S) ≤ d is
∀v: Σ_{u~v} x_u x_v ≤ d, and |S| = Σ x_v. The SoS/Lasserre hierarchy produces,
for each level t, a stronger and stronger convex relaxation whose dual is a
*certificate* (sum of squares + polynomials vanishing on the Boolean cube)
proving infeasibility of D(S) ≤ d. A dual certificate at level t that succeeds
for d = ceil(√n) − 1 is a machine-checkable proof of f(n) ≥ ceil(√n).

mechanism: The crucial structural fact is that the cube is the Cayley graph of
Z_2^n, so the entire feasibility instance is invariant under the n-dimensional
character group, and the Lasserre relaxation can be block-diagonalised by the
characters χ_a(v) = (−1)^{⟨a,v⟩}. The moment matrix then decomposes over the
2^n irreducible representations (all 1-dimensional), turning an exponentially
large SDP into a finite computation in the group algebra — the same
representation-theoretic symmetrisation used in the spectral proof, but now
applied to a *hierarchy of certificates* rather than a single eigenvalue bound.

Where it is different from what is closed: the spectral route gives the single
inequality λ_max(B) ≤ D(S) and interlacing λ_max(B) ≥ √n — one certificate at
one level. The Lasserre hierarchy is a strictly richer family of proof objects;
its dual gives the same √n bound at low level (recovering Huang as a degree-2
SoS certificate) and, at higher levels, could *certify the exact value*
ceil(√n) or locate a genuine obstruction ("the hierarchy does not close before
level t"). The quantity is a maximum by construction — the objective is the
per-vertex degree ceiling, and the certificate is a sum-of-squares identity
over the Boolean ideal, not an average.

covers: reproduces the spectral lower bound as a level-2 SoS proof (the
λ_max ≤ D(S) + interlacing chain is exactly a quadratic-form certificate), so
Scholze's rule holds. The genuinely new content is the hierarchy above level 2,
targeting f(n) = ceil(√n) exactly and producing proof artifacts (dual
polynomials) a Lean formalisation can check.

status: adopted
synthesis: research grounded the machinery and surfaced what none of the three
candidates named — the LOWER bound f(n) >= ceil(sqrt n) is already a theorem
(Huang's spectral chain, plus the integrality of f(n)), so the only open content
is the UPPER bound, i.e. the exact value f(n) = ceil(sqrt n), which is a
CONSTRUCTION problem (exhibit S with |S| = 2^{n-1}+1 and D(S) <= ceil(sqrt n)),
not a lower-bound/certificate problem. All three candidates were aimed at
proving sqrt(n), which is redundant after Huang. This SoS/character-symmetry
framework is kept because it is the only grounded instrument, but it is
re-aimed: level 2 is Huang's proof (Scholze's rule holds, so the closed bound is
reproduced as a machine-checkable dual certificate), and the genuinely new
content is the FEASIBLE side at d = ceil(sqrt n) — either the character-block-
diagonalised relaxation exposes/rounds to an explicit witness (the missing upper
construction), or it fails to, locating exactly where the hierarchy is blind.
The direct falsifier is the exact-value oracle: if D(S) <= ceil(sqrt n) is
infeasible at some n then f(n) > ceil(sqrt n) and the exact-value conjecture
dies — settled by a computation, not by this proposal's opinion.
The SoS/Lasserre method on the Boolean cube is well developed: the certificate
world (Positivstellensatze of Putinar and Schmuegen on the hypercube; effective
degree bounds) and the symmetry reduction (reflect the whole instance under the
Z_2^n character group) are both standard. What the literature shows, and why the
grounding is honest: (a) degree bounds for hypercube certificates are known
(Schmuegen-type O(1/sqrt(eta)); Putinar O(fmax/fmin), Baldi-Slot 2023), so low
levels CAN be huge; (b) symmetric-quadratic hypercube functions recently got
O(sqrt(n k) log n) degree certificates (Kurpisz-Potechin-Wirth 2021, ICALP),
showing symmetry reductions are genuinely powerful here; (c) the level-2
certificate IS Huang's spectral chain (quadratic form λ_max ≤ D, interlacing), so
Scholze's rule holds — the route does reproduce huang-f-n-sqrt-n as a degree-2
SoS proof. The open question is not whether the framework works but at what level
it closes; that is precisely the computation the first-step proposes and the
literature does not answer for this quantity. Caveat: no published source applies
the Lasserre hierarchy to certify the exact f(n) = ceil(sqrt(n)) value of this
max-internal-degree problem; the proposal's "hierarchy does not close" failure
mode is also possible and would be a genuine located-obstruction result.
precedent:
  - Kurpisz-Potechin-Wirth, "SoS certification for symmetric quadratic functions
    and constrained Boolean hypercube optimization", ICALP 2021 —
    https://doi.org/10.4230/lipics.icalp.2021.90 (symmetry reduction + SQF
    degree certificates on the cube; the same character-block-diagonalisation
    the proposal names)
  - Kurpisz, "Sum-of-squares bounds via Boolean function analysis" (2019) —
    https://doi.org/10.3929/ethz-b-000355047 (dual-certificate perspective,
    degree lower bounds on the Boolean cube)
  - Baldi-Slot, "Degree bounds for Putinar's Positivstellensatz on the
    hypercube" — https://hal.science/hal-04003633/document (Putinar degree
    O(fmax/fmin) on the cube)
  - "An effective version of Schmuegen's Positivstellensatz for the hypercube",
    Optimization Letters 2022 — https://link.springer.com/article/10.1007/s11590-022-01922-5
    (degree O(1/sqrt(eta)) certificate on the cube)
  - Vandaele-Gijswijt (symmetry in SDP-relaxations for polynomial optimisation)
    — https://dl.acm.org/doi/10.1287/moor.1120.0558 (block-decomposition under
    group action; the exact mechanism for the character symmetrisation)
  - Lauria-Nordstroem, "Tight size-degree bounds for sums-of-squares proofs",
    CCC 2015 — https://doi.org/10.4230/lipics.ccc.2015.448 (SoS degree can be
    forced high; the "hierarchy does not close" failure mode is a real,
    studied phenomenon)
  - No source found applying the Lasserre/SoS hierarchy to certify the exact
    max-internal-degree value f(n) at |S|=2^{n-1}+1; the specific certificate
    (dual at fixed level for all n) is this proposal's own target.
first-step: (tool_builder, sat_solver) Two independent, immediately runnable
  computations, both feeding the same question (is f(n) = ceil(sqrt n)?):
  (1) Exact-value oracle extension: with code/lib/fmax.py decision_ilp, settle
  feasibility of {|S| = 2^{n-1}+1, D(S) <= ceil(sqrt n)} at n = 6 (|S|=33,
  d=3), 7 (|S|=65, d=3), 8 (|S|=129, d=3). Feasible => f(n) = ceil(sqrt n) at
  that n and keep an explicit witness S (the construction at that n);
  INFEASIBLE => f(n) > ceil(sqrt n), the exact-value conjecture dies, and the
  first counterexample is recorded. This is the highest-value next fact.
  (2) SoS instrument at the boundary: for n = 4,5 build the degree-2 moment-
  matrix relaxation of D(S) <= d, block-diagonalise over the Z_2^n characters,
  and confirm (i) infeasible at d = ceil(sqrt n)-1 (Huang's lower bound as a
  dual certificate — the machine-checkable artifact), (ii) feasible at
  d = ceil(sqrt n), comparing the relaxation's feasible set to the ILP witness.
  If (ii) rounds to an integer S, that is the construction route; if the
  relaxation is feasible while no integer witness exists at a larger n, that is
  the located "hierarchy gap".
```
