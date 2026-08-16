# Thread: forced non-strong-regularity of the triangle graph C3(Gamma)

```thread
id: thread-triangle-graph
question: A putative Conway 99-graph Gamma = srg(99,14,1,2) has 231 triangles
  (the 3-cliques; 231 = nk/6). Phillips 2026 (Thm 4.5) forces the 3-clique
  (triangle) graph C3(Gamma) to be NOT strongly regular. Is the shortfall from
  strong regularity on this 231-vertex 18-regular regular clique assembly
  (degree d = 3(k/2 - 1) = 18) a usable 99-structural constraint, i.e. can a
  counting identity force a contradiction that 9 and 243 escape?
status: open
rests-on: phillips-triangle-graph-not-srg, integrality-five-members, c5
blocked-by: none (the structural claim is sourced; a concrete counting
  identity on C3(Gamma) is not yet stated)
next: state the exact sense in which C3(Gamma) fails strong regularity for a
  lambda=1 graph (which eigenvalue multiplicities / eigenvector structure are
  forced), then ask whether the 231-vertex 18-regular constraint plus the
  underlying srg parameters admits any 99-specific obstruction that the
  (243,22,1,2) BvLS triangle graph — which is ALSO not strongly regular — does
  not. The negative-control rule applies: any argument here must be run against
  C3 of rook(9) and C3 of bvls(243) through code/lib before it can rule out 99.
```

## What the thread rests on

- **Phillips 2026, Thm 4.5** (claim `phillips-triangle-graph-not-srg`): the only
  non-boring srg locally-linear graphs with strongly-regular 3-clique graphs are
  srg(9,4,1,2), srg(15,6,1,3), srg(27,10,1,5). (99,14,1,2) is not among them, so
  **if a Conway 99-graph exists its triangle graph is not strongly regular.**
- **Philips 2026, Thm 4.2** gives the criterion: with clique size ω=3 (λ=1
  forbids K₄), C3(Γ) is srg iff `s = −k/2` OR `k = 6`. (99,14,1,2): s=−4 ≠ −7,
  k=14 ≠ 6 → fails both. (243,22,1,2) BvLS: s=−5 ≠ −11, k=22 ≠ 6 → fails both too.
  So 99 and 243 share the "C3 not strongly regular" fact — a constraint, NOT a
  nonexistence proof.
- **τ,ρ system is a closed dead end** (claim `phillips-tau-rho-dead-end`): the
  rank-10, 13-variable linear system any such triangle graph must satisfy has a
  non-negative integer solution for every feasible locally-linear srg parameter
  set with k ≤ 5×10⁷ (Z3), so it eliminates nothing including 99.

## The ω correction (do not repeat the earlier error)

For a λ=1 graph the **clique size is ω = 3**, not k/2. λ=1 (each edge in a unique
triangle) forbids K₄, so the largest clique is a triangle. The quantity k/2 = 7
is the number of triangles through a vertex, used only to compute the triangle
graph's degree d = 3(k/2−1) = 18. In Phillips the ω of the ω-clique graph is the
clique size, so ω−1 = 2 and the criterion is `s == −k/2` or `k == 6`.

## Why this might matter for 99

The triangle graph C3(Γ) is a 231-vertex, 18-regular graph with a very restricted
spectrum forced from Γ (formula 4.3): d¹, (k/2+r−3)^f, (k/2+s−3)^g, (−3)^(m−n).
For (99,14,1,2): m−n = 231−99 = 132 vertices carry eigenvalue −3; r̃ = 7+3−3 = 7,
s̃ = 7−4−3 = 0. So C3(Γ), if it exists, is an 18-regular graph on 231 vertices
with spectrum 18^1, 7^54, 0^44, (−3)^132. Whether such a graph exists (as the
"triangle graph" of a putative Conway graph) is the question — and whether a
regular graph with exactly this spectrum can fail to be strongly regular in the
precise way the triangle-graph would have to is a checkable lead.

## COMPUTED (tool_builder): C3 of both controls built and spectrum confirmed

`code/out/check_triangle_graph.py` (exact via `lib.triangles.triangle_graph`,
spectrum numerical) settled the thread's next step:

- **rook(3)=srg(9,4,1,2):** C3 = K_{3,3} = **srg(6,3,0,3)** exactly (is_srg
  True). This is the degenerate Thm-4.5 member; the eq-4.3 prediction does not
  apply because nT−v = 6−9 < 0.
- **BvLS=srg(243,22,1,2):** C3 is **30-regular on 891 vertices**, 13365 edges,
  triangle count nk/6=891, degree 3(11−1)=30 all exact. **NOT strongly
  regular**, decided exactly by common-neighbour counts: all 26730 adjacent
  pairs share exactly **9** common neighbours (constant λ-sector), non-adjacent
  pairs vary **{1:481140, 0:267300, 3:17820}** (non-constant μ-sector).
- **Spectrum matches Phillips eq 4.3 exactly:** 30^1, 12^132, 3^110, (−3)^648;
  trace 0 and sum-of-squares 26730 both match prediction exactly. Numerical
  eigvalsh gives the same multiset.

Bearing: the C3-not-strongly-regular claim is **shared by 99 and 243** (both
fail the `s==−k/2 or k==6` criterion), so it is a constraint, not a rule-out —
consistent with the negative-control rule. New observation: at BvLS the failure
of strong regularity of C3 is confined to the **non-adjacent (μ) sector**; the
adjacent (λ) sector is constant at 9. Whether a 99-graph's C3 would have to
avoid the two non-constant μ-values (0 and 3) or, like BvLS, necessarily hit
them is the next question; a per-triangle counting identity there is not yet
stated.

## Status

The structural constraint (C3 not strongly regular) is **sourced and verified**
against the full text; the ω correction is verified by hand arithmetic. The
checks above confirm both controls (rook's C3 = K_3,3; BvLS's C3 30-regular
891-vertex, non-srg, exact spectrum match). No 99-specific counting identity
on C3(Γ) has been stated yet, so the thread is a live lead rather than a
settled or refuted direction.
