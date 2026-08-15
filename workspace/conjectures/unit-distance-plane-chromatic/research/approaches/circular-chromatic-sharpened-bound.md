# Approach: circular chromatic number as a sharper exact threshold invariant

```approach
idea: Replace the integer 4-colourability question with the rational invariant
  chi_c(G) — Vince's circular chromatic number — which satisfies chi(G) =
  ceil(chi_c(G)). Therefore chi_c(G) > 4 is *equivalent* to "G is not
  4-colourable": the threshold is crossed exactly where integer colouring is,
  but chi_c is a homomorphism-theoretic relaxation (a p/q-colouring is a
  homomorphism G -> C(p,q), the circulant on Z_p with steps q, p/q > 4) that can
  be certified with a finite object — either an explicit p/q-colouring witness, or
  a proof of non-existence of such a homomorphism via clique/independent-set
  integer arguments. chi_c sits between the fractional chromatic number and chi:
  chi_f(G) <= chi_c(G), and chi(G) = ceil(chi_c(G)).
mechanism: This is a change of invariant rather than of representation: from the
  integer chromatic number to the rational circular chromatic number of Vince
  (1988; Zhu's 2001 survey). Its value here is that it is a strictly finer scale
  than the run's existing Lovasz-theta / vector-chromatic relaxation (adopted in
  `lovasz-theta-vector-chromatic`): theta can sit at 4 while chi_c crosses 4, since
  chi_c is defined by homomorphisms to circulants and is not bounded by the theta
  SDP. Concretely, on the Eisenstein-integer triangular lattice Z[omega] — the
  run's rigidity lever — the distance-1 graph has chi_c = chi_f exactly (a
  vertex-transitive LP), a closed form; on arbitrary constructed unit-distance
  graphs a p/q-circular colouring is an exact, verifiable witness, and ruling out
  every p/q > 4 (a finite independent-set computation for candidate p,q) certifies
  non-4-colourability without the exponential 4-SAT search. Every certificate is
  in exact arithmetic: the arcs in a circular colouring are rational intervals,
  and adjacency-disjointness is a finite check.
status: refuted
killed-by: no shortcut and no crossing. (1) chi(G) = ceil(chi_c(G)) is an
  identity, so deciding chi_c > 4 is exactly as hard as the 4-colourability SAT
  the run already owns. (2) The only cheap closed form — the vertex-transitive
  Eisenstein (triangular) lattice — is 3-colourable, so chi_c = 3 there and never
  crosses 4. What remains is a tightness heuristic, not a certificate.
first-step: Implement exact chi_c lower/upper bounds: (1) calibrate on the Moser
  spindle (must return chi_c in (3,4], matching chi=4) and C5 (chi_c = 5/2);
  (2) compute chi_c on the first Eisenstein-integer triangular-lattice disks via
  the fractional/vertex-transitive LP; (3) scan the run's constructed graphs
  (Moser+Moser, next Minkowski tier) for chi_c > 4 — any crossing is a certified
  chi >= 5 with a p/q-colouring witness, otherwise a precise relaxation-gap datum.
falsifies: chi_c(G) <= 4 on every graph the run constructs (the invariant never
  crosses the threshold), establishing that circular colouring is no stronger than
  theta on this construction family — a precise negative result, not a theorem
  failure. The other failure mode is the relation chi(G)=ceil(chi_c(G)) being
  mis-stated; it is Vince's theorem and is here confirmed by three independent
  survey sources.
precedent:
  - Vince 1988, "Star chromatic number", J. Graph Theory 12(4):551–559 — the
    original definition; a (k,d)-colouring is f: V -> {0,...,k-1} with
    d <= |f(u)-f(v)| <= k-d for every edge uv; chi_c = min{ k/d }.
  - Zhu 2001, "Circular chromatic number: a survey" (Discrete Math 229:371–410) —
    the standard treatment; confirmed: chi(G)-1 < chi_c(G) <= chi(G), hence
    chi(G) = ceil(chi_c(G)) exactly.
  - Pêcher–Wagler 2020, "On circular-perfect graphs: A survey", Europ. J. Comb.
    https://doi.org/10.1016/j.ejc.2020.103224 — restates the (k,d)-circular
    colouring definition, chi_c = min{k/d}, chi_c <= chi, chi_f <= chi_c <= chi,
    and chi = ceil(chi_c).
  - "Circular colouring and algebraic no-homomorphism theorems" (Electron. J. Comb.)
    and the circular game-chromatic-number paper — both confirm
    chi(G)-1 < chi_c(G) <= chi(G) and chi(G) = ceil(chi_c(G)).
  - claim `einstein-lattice-unit-distance` — the vertex-transitive lattice where
    chi_f = chi_c is a closed-form exact LP (vertex-transitivity).
```

## Research verdict — GROUNDED, with a scoping caveat

The mathematics the candidate rests on is **correct and well-sourced**. Three
independent treatments (Pêcher–Wagler 2020 survey; the circular game-chromatic
paper; the algebraic no-homomorphism paper) all state the exact theorem:

> **Theorem (Vince 1988; Zhu 2001).** For every finite graph G, with chi_c(G)
> the circular chromatic number,
>     chi(G) - 1 < chi_c(G) <= chi(G),
> hence **chi(G) = ceil(chi_c(G))**. A (k,d)-circular colouring is a map
> f: V -> {0,...,k-1} with d <= |f(u)-f(v)| <= k-d on every edge, and
> chi_c(G) = min{ k/d : G is (k,d)-colourable }.

So the candidate's central equivalence is **exactly right**: chi_c(G) > 4 iff
chi(G) >= 5 iff G is not 4-colourable; and chi_c(G) <= 4 iff G is 4-colourable.
Chi_c is genuinely finer than chi (it takes non-integer values, e.g. chi_c(C5)
= 5/2, chi_c(C_{2k+1}) = 2 + 1/k) and sits between the fractional chromatic
number and chi: chi_f <= chi_c <= chi = ceil(chi_c).

### What would be true — the correct relation and its limits

- The relation chi = ceil(chi_c) is **not** false; it holds for *every* graph.
  This refutes the candidate's own listed "failure mode" — that wording risk.
- The claim that chi_c can cross 4 where theta sits at 4 is plausible and
  consistent with the invariant being strictly finer, but **no graph in the run's
  construction family has yet been tested**, so "whether chi_c ever exceeds 4 on
  these" is genuinely open and is exactly what the first-step decides.

### The scoping caveat — where the candidate overstates value

Deciding chi_c(G) > 4 is **equivalent in difficulty to deciding 4-colourability**:
the threshold crossing *is* the 4-colourability question (by the theorem above),
and computing chi_c exactly is NP-hard in general. So the candidate's promise
"certifies non-4-colourability without the exponential 4-SAT search" is not
available in general: for an arbitrary constructed graph, certifying chi_c > 4
needs exactly the 4-SAT/independent-set work the run already has. The invariant's
real value is on the *structured* graphs where it is cheap:

1. **Vertex-transitive graphs (Eisenstein lattice distance graphs):** there
   chi_c = chi_f = (vertex count / independence number), an exact LP value with a
   closed form — no SAT at all. This is the one place the candidate genuinely
   buys something the run's theta could not.
2. **A grading of tightness:** for 4-colourable graphs, chi_c = 4 is "tight"
   (colouring uses the full circle), chi_c < 4 is "loose." A 4-colourable UDG
   with chi_c very close to 4 is structurally the most promising seed for a
   spindling/join that pushes across into chi_c > 4 — a *guide to construction*,
   not a certificate.

So: `status: grounded` — the invariant is real, correct, and strictly finer;
the equivalence chi_c > 4 <=> non-4-colourability is proved and sourced. The
advertised computational shortcut does not hold for arbitrary graphs, only the
vertex-transitive/Eisenstein subclass and the tightness-grading heuristic.

## Binding to the run's object

- The Moser spindle: must return chi_c in (3,4] to match chi=4 (first-step
  calibration). Not yet computed this run.
- The plane over the Eisenstein lattice: chi_c = chi_f because the distance
  graph is vertex-transitive — the only exact closed-form route. Whether chi_f
  of the lattice distance graph crosses 4 is unknown and open.
- Whether chi_c crosses 4 on any constructed UDG is exactly the relaxation-gap
  datum the lower-bound direction needs.

## Why this is not a restatement of a closed idea

- Not the theta/Hoffman line (adopted, not closed): chi_c is a homomorphism-to-
  circulant invariant, strictly finer (non-integer), not bounded by the theta
  SDP; theta is an upper/lower-bound certificate, chi_c a refinement.
- Not the P^1(K) line (refuted as a coordinate relabelling): chi_c is a
  *graph invariant*, independent of geometry.
- Not the neighbourhood-complex line (refuted): no topology, rational arcs only.

## Decision (convergence pass) — REFUTED

Adopted instead: `rigidity-matroid-henneberg-construction`. Two facts close this
as a lower-bound line. (1) chi(G) = ceil(chi_c(G)) is an identity, so deciding
chi_c > 4 is exactly as hard as the 4-colourability SAT the run already owns —
there is no shortcut. (2) The only cheap closed form (the vertex-transitive
Eisenstein lattice) has chi_c = chi = 3, because the triangular lattice is
3-colourable, so it never crosses 4. The invariant itself is real and strictly
finer than theta, but its remaining use — grading how "tight" a 4-colourable graph
is — is a construction heuristic, not a certificate, and produces no result on its
own.
