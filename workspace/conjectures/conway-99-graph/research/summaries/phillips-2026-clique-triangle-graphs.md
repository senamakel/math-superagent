# Phillips 2026 — A Comprehensive Study of Clique Graphs and Clique Regular Graphs

<!-- source: https://arxiv.org/pdf/2605.22867 | downloaded 2026 -->

## What it is
Connor Phillips, "A Comprehensive Study of Clique Graphs and Clique Regular Graphs",
arXiv:2605.22867 (2026). A general study of locally-linear graphs — graphs in which every
edge is in a unique triangle — the clique-regular property, and the 3-clique graph
(triangle graph) C3(Γ) that takes triangles as vertices and joins two triangles when they
share a vertex. This triangle-graph construction is directly the one the Conway-99
problem's partial-linear-space framing points to (231 triangles on 99 points).

## What it establishes, and its bearing on (99,14,1,2)

An srg(n,k,λ,μ) is **locally linear iff λ = 1**. The (99,14,1,2) candidate is therefore
locally linear, and every locally-linear SRG is 3-clique regular, i.e. a regular clique
assembly.

**Theorem 4.5 (the load-bearing result):** The only *non-boring* strongly regular
locally-linear graphs whose 3-clique graph C3(Γ) is ALSO strongly regular are the unique
graphs with parameters
  srg(9,4,1,2), srg(15,6,1,3), srg(27,10,1,5).

(99,14,1,2) is non-boring and locally-linear but is NOT one of those three. **Therefore,
if a Conway 99-graph exists, its triangle graph C3(Γ) is NOT strongly regular.** This is
a fresh, concrete structural constraint the library did not previously hold: the triangle
graph of a putative (99,14,1,2) is a 231-vertex, 18-regular "regular clique assembly"
(231 = nk/6 triangles; degree d = 3(k/2 − 1) = 18 since each triangle has 3 vertices and
each vertex lies in k/2 = 7 triangles; maximal clique size ω = 3 because λ=1 forbids K₄)
but it is forced to FAIL strong regularity. The failure criterion (Thm 4.2) is
`s = −k/2` OR `k = 6` (with ω=3, ω−1=2): (99,14,1,2) has s=−4 ≠ −7 and k=14 ≠ 6, so it
fails both. An SRG-parameter check on C3(Γ) is a candidate obstruction. (This is a lead
to test, not a proven 99-nonexistence.)

> **Correction:** earlier drafts of this note wrote the clique size as ω = k/2 = 7.
> That is wrong. `k/2 = 7` is the number of triangles through a vertex, used to compute
> the degree of C3 (d = 3(k/2−1) = 18); the clique size is ω = 3 for every λ=1 graph,
> because λ=1 (each edge in a unique triangle) forbids K₄. Thm 4.2's `ω−1` is therefore
> 2, and the criterion is `s == −k/2` or `k == 6`.

## The τ,ρ system does NOT help here (a dead end worth recording)

For the non-strongly-regular cases, the paper derives a rank-10, 13-variable τ,ρ linear
system that any such triangle graph must satisfy (from walk-regularity and counts of
triangles/quadrangles/5-walks around a vertex). It then used Z3 to check: **for every
feasible locally-linear SRG parameter set with k ≤ 5×10⁷, a non-negative integer solution
exists.** So the τ,ρ system fails to eliminate (99,14,1,2) and every other feasible set in
that range. This route is recorded as closed rather than re-attempted.

## Also establishes (general background, sourced)
- Spectrum of C3(Γ) from Γ (Remark 3.6 / Theorem 3.5 / formula 4.3 with ω=3):
  for an srg(n,k,1,μ) with spectrum k¹, rᶠ, sᵍ, the 3-clique graph has spectrum
  d¹, r̃ᶠ, s̃ᵍ, (−3)^(m−n) where m = nk/6, d = 3(k/2 − 1),
  r̃ = k/2 + r − 3, s̃ = k/2 + s − 3
  (all k/2 terms follow from k/(ω−1) with ω=3, the clique size).
- Critical-group connections between Γ and C3(Γ)/S3(Γ) (Theorem 5.1), generalising the
  line-graph/subdivision case.
- The four known locally-linear SRG constructions and their triangle-graph parameters
  (Table 4.1): (81,20,1,6), (243,22,1,2), (378,52,1,8), (729,112,1,4).

```claim
id: phillips-triangle-graph-not-srg
statement: The only non-boring strongly regular locally-linear graphs whose
  3-clique graph C3(Gamma) is also strongly regular are the unique graphs
  srg(9,4,1,2), srg(15,6,1,3), srg(27,10,1,5) (Phillips 2026, Thm 4.5). Hence
  for a putative srg(99,14,1,2) with triangle graph C3(Gamma) (231 vertices,
  18-regular regular clique assembly, clique size omega=3; m=nk/6=231,
  degree d=3(k/2-1)=18), C3(Gamma) is NOT strongly regular.
hypotheses: Gamma an srg(n,k,1,mu), lambda=1 (locally linear), non-boring;
  the 3-clique graph C3(Gamma) exists.
holds-here: yes — (99,14,1,2) is locally linear and non-boring but not among
  the three, so its triangle graph is forced NOT strongly regular.
status: sourced (verified in full text, lines 1960-1964; Thm 4.2 gives the
  criterion s = -k/2 or k = 6 with clique size omega=3, lambda-1 forbids K4,
  from which the three parameters are enumerated)
bearing: a candidate obstruction: a putative (99,14,1,2) must have a triangle
  graph that is an 18-regular 231-vertex regular clique assembly failing strong
  regularity; checking C3(Gamma) against srg parameter sets is a testable lead.
  CONSTRAINT NOT PROOF: (243,22,1,2) is also not among the three, so its
  triangle graph is also not strongly regular — the claim does not rule out 99
  and must obey the negative-control rule (does not kill 243).
anchor: research/sources/phillips-2026-clique-triangle-graphs.full.md
contradicts: none
answers: none
```

```claim
id: phillips-tau-rho-dead-end
statement: The rank-10, 13-variable tau/rho linear system that any locally-linear
  srg must satisfy (from walk-regularity and triangle/quadrangle/5-walk counts
  around a vertex) admits a non-negative integer solution for every feasible
  srg(n,k,1,mu) parameter set with k <= 5e7 (checked with the Z3 SMT solver,
  Phillips 2026 App. A). It therefore eliminates no parameter set in that range,
  including (99,14,1,2).
hypotheses: srg(n,k,1,mu) locally linear; the feasibility equations (4.1),(4.2).
holds-here: yes — the tau/rho system imposes no further restriction on (99,14,1,2)
  beyond ordinary feasibility.
status: sourced (read from full text lines 2485-2494; the Z3 computation is the
  paper's, not reproduced here)
bearing: closes the tau/rho linear-algebra route for 99 as a dead end — do not
  re-attempt it. It is a RULED-OUT direction, not a lead.
anchor: research/sources/phillips-2026-clique-triangle-graphs.full.md
contradicts: none
answers: none
```

## Library status
Full text: research/sources/phillips-2026-clique-triangle-graphs.full.md.
Note the (243,22,1,2) BvLS graph in Table 4.1 — it is not among the three in Theorem 4.5,
so its triangle graph is also not strongly regular; the constraint is genuinely one that
99 and 243 share, so it is a *constraint*, not a nonexistence proof, and any use must
respect the negative-control rule (it does NOT rule out 243, therefore cannot by itself
rule out 99).
