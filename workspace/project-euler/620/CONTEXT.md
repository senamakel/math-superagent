# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. It carries what an agent would otherwise rebuild from disk, from the
note store, or from a session it was not present for: established results with
their basis, approaches that died and why, computed numbers, durable memory that
bears on the problem, and where two accounts disagree. It is not a catalogue of
files — `research/INDEX.md` is that — and not a narration of what agents did.

**Token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000). The file is re-sent on
every model call in every role that reads it; length here is a bill paid many
times over. Link the file holding any detail compressed away. Durable findings
belong in Cognee; a statement nobody can trace to a source is worth none.

## Established

**Problem (PE 620, statement `problem.md`, restatement `GOAL.md`).** C: internal
ring gear, circumference c. S: sun gear, circumference s, off-centre inside C.
Four planets (two of circumference p, two of q; p<q), each tangent internally to
C and externally to S; planets MAY overlap each other (waives the standard
neighbour condition); closest S–C boundary gap ≥1cm ⇒ centre offset d ≤ R−r−1.
c,s,p,q integers ≥5 (teeth, pitch 1cm). "Perfectly meshing" = constant angular
velocity ratio, teeth align with grooves. `g(c,s,p,q)` = number of valid
arrangements (finite; only discrete positions mesh). `G(n)=Σ_{s+p+q≤n} g(s+p+q,
s,p,q)`, p<q, p,s ≥5. Worked: g(16,5,5,6)=9, G(16)=9, G(20)=205; target G(500).

**Governing structure — sourced and/or derived; holds-here unchecked except where marked:**

1. **Least-mesh-angle discretization (sourced, originally asserted).** Legal
   planet angular positions are integer multiples of β = 2π/(c+s) in a COAXIAL
   train. Three independent gear sources state it (Drivetrain Hub, UTS, Gear
   Solutions handbook; claims `least_mesh_angle*`) and Guo 2011 OSU thesis Ch.5
   derives it: (Z_ring+Z_sun)·ψ̂ = 2πn (eq. 5.21, ring tooth count negative for
   internal gears), with the step unchanged for d_i=1 independent trains, so
   p,q do not enter the step (eq. 5.25). **Caveat every solver must hear**: all
   sources derive it for a COAXIAL train; PE620's sun is OFF-CENTRE — planet
   centres lie on an ellipse, the angle about S is not the angle about C, and a
   single-center β-lattice is a conjecture. All three implemented models have
   now failed the oracle (Ruled out); the rule survives as the d→0 coaxial
   limit of the off-centre invariant (item 4).
2. **Ellipse locus (sourced).** The centre of a planet tangent internally to C
   and externally to S lies on the ellipse with foci at the centres O and S and
   sum of focal distances (R−ρ)+(r+ρ) = (c+s)/2π — the planet size **cancels**,
   so all four planets share one ellipse (major semiaxis (c+s)/4π, focal
   separation d = |OS|). Claim `tangent_circle_center_ellipse`; Pappus-chain
   rational parametrization known (durable memory).
3. **Teeth-matching conditions (sourced, partial).** Zou 2015: concentric /
   homogeneity-distribution / neighbour / gear-ratio conditions
   (`research/summaries/single-planetary-teeth-matching-zou-2015.md`); PE620
   permits planet overlap, so only the concentric geometry and assembly
   discreteness survive. Xue 2020 full derivation unobtainable (JS-rendered
   page, DOAJ 403) — abstract only.
4. **Off-centre dual-mesh phase invariant — THE live hypothesis (derived;
   holds-here UNCHECKED; not yet implemented).** Eliminating each planet's free
   spin from its two mesh congruences leaves W_j = s·φ_j + c·χ_j − t_j·γ_j,
   with φ=∠PSC, χ=∠PCS, γ=∠SPC (Guo pitch-point convention: sun phase
   +s·contact angle, internal ring −c·contact angle). Simultaneous meshing ⇔
   all four W_j pairwise congruent mod 2π — per mirror pair s·φ+c·χ ∈ πℤ,
   cross-type s(φ_p−φ_q)+c(χ_p−χ_q)−p·γ_p+q·γ_q ∈ 2πℤ — and g = #{d ∈
   (max_t|a_t−b_t|, (c−s)/2π−1] satisfying all three} × mirror factor κ∈{1,2}
   (oracle pins κ and endpoint rules). Full derivation, coaxial-limit
   consistency (recovers β-lattice as d→0), and the 4 sign variants to probe:
   `research/threads/offcentre-mesh-phase-model.md`, claim
   `offcentre_dual_mesh_phase_invariant`. **Trap to pin first**: with
   UNORIENTED triangle angles the mirror pair has identical angles, so W+ − W−
   ≡ 0 trivially — the per-type π-congruence is a signed-angle statement; read
   the signs off Guo Ch.5 Table 5.1 / eq 5.22, don't guess them.

## Ruled out — THREE implemented models FAILED (checked; each returns 0)

1. **Continuous single-d model — DEAD.** `code/lib/gears.py` / `code/brute.py`
   (`code/oracle_test.py`): g(16,5,5,6)=0 vs 9; a 20k-point residual scan found
   no non-degenerate valid offset d (global minimum only at the degenerate
   endpoint d=1/2π, where the two p-planets coincide). Notes + claim
   `gears_model_fails_oracle` (checked): `code/out/oracle_test.md`,
   `code/out/oracle-model-broken.md`, `code/out/oracle_test.txt`.
2. **Single-d least-mesh-angle lattice model — DEAD.** `code/pattern/discrete_model_probe.py`
   → `code/out/lattice_test.txt`: slots k·2π/(s+c) about O or about S (four
   planets sharing one centre offset d from each slot's tangency quadratic),
   valid iff 2F_p, 2F_q, F_p−F_q ∈ ℤ (mod 1) (mpmath-60, T-sign ±1, all four
   {O,S}² anchor variants): **0 distinct valid d — g(16,5,5,6)=0 vs 9; G(16)=0;
   G(20)=0 (all 22 per-pair rows 0)**, 0.00 s per case. Kills the
   single-center-lattice transfer, not the coaxial theorem. No claim block
   documents this yet — write the checked claim before reuse. Unrun sibling:
   `code/pattern/phase_grid.py` (signed E = Rβ−rγ−ρψ re-derivation, 400k-point
   fine scan of d; no output on disk).
3. **Idler-phase B-model — PARTIALLY PROBED (2/4 sign variants, both 0).**
   `code/pattern/phase_model_probe.py` → `code/out/phase_model_test.txt`: NO
   position lattice; d free over (max_t|a_t−b_t|, R−r−1]; idler-spin elimination
   leaves B_t = (r+ε·t/2π)·γ + ε·(R−t/2π)·β, valid iff 2B_p, 2B_q, B_p−B_q ∈ ℤ
   (mod 1), ε=±1: **g(16,5,5,6)=0 for BOTH ε variants** (0.09 s). Two of four
   independent sign combinations tested — the remaining two (independent signs on
   gamma and beta coefficients) must be probed before declaring dead. Raw output
   only; write the checked claim before reuse.

Common structure of all three failures: they parametrise by d and test
phase-elimination congruences, never reproducing 9. The W-model differs in
that the per-type condition is a signed-π statement (mirror pair), which the
unoriented implementations above could not even formulate.

## Numbers

Oracle values — still reproduced by **no** program: g(16,5,5,6)=9, G(16)=9,
G(20)=205. Every computed g value on disk is 0 (the three dead models above).
No positive terms exist ⇒ sequence/OEIS analysis remains blocked.

## Recalled

Cognee holds: the gear-geometry source cards (Drivetrain Hub, UTS, Gear
Solutions, Cut-the-Knot); the teeth-matching / assembly-condition findings (Zou
2015, Xue 2020 abstract); the dead continuous-model verdict; graph edges
linking β-discretization ↔ ellipse locus ↔ mesh-phasing theory (Guo 2011,
Parker–Lin 2004, ISMA 2016); the W-model derivation card (this run's own).
No prior PE620 result is importable — the run's numbers must stand on its own
computation. **Memory vs. computation disagreement**: Cognee's older "discrete
counting model" card asserts an integer-lattice of 2π/(c+s) positions about
the SUN on the shared ellipse — CONTRADICTED by Ruled-out #2's checked zero
(both O-anchored and S-anchored lattices); its elliptical geometry (item 2) is
unaffected.

## Gaps

- **No oracle reproduces 9/9/205** — the top blocker (GOAL.md step 1). Every
  candidate model so far returns 0, so the reading of "perfectly meshing" or of
  the discreteness is still unvalidated.
- **Phase-model probe partial: only 2 of 4 chi/gamma sign variants tested** in
  `code/pattern/phase_model_probe.py` → `code/out/phase_model_test.txt` (eps
  tied to both gamma and beta coefficients together — only ±1 probed).
  Remaining 2 variants (independent signs) must be tested; if all 4 return 0,
  the directive is to stop deriving top-down and instead enumerate the 9
  arrangements for (16,5,5,6) directly by tangency, compute tooth phases
  numerically, and work backwards from what survives to the correct condition.
- **Implement and oracle-test the W-model congruences** (item 4: 4 signed-angle
  variants, κ factor, endpoint rules) — NOT the immediate next step per directive;
  `code/pattern/phase_grid.py` is the only other unrun artifact. First: finish
  probing all 4 sign variants in `phase_model_probe.py`. If all four return 0,
  fall back to direct enumeration of the 9 arrangements for (16,5,5,6).
- Exact count of g, and summing G(500) without enumerating s+p+q ≤ 500 (cost
  must not grow with the bound 500).
- d enters as the ellipse focal separation, bounded by d ≥ max_t|a_t−b_t| and
  d ≤ R−r−1 (the 1cm gap); endpoint/degeneracy counting detail open.