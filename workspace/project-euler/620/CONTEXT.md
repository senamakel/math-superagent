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

**Governing structure — sourced, but holds-here UNVERIFIED:**

1. **Least-mesh-angle discretization (DERIVED, not merely asserted).** Legal
   planet angular positions are integer multiples of β = 2π/(s+c). Now backed
   by a derived assembly condition, not just three design guides: Guo 2011 OSU
   thesis (Ch.5 eq. 5.21) — (Z_ring+Z_sun)·ψ̂ = 2πn, i.e. a planet meshing both
   internal ring and sun sits only at multiples of 2π/(Z_ring+Z_sun), where the
   sun–planet and ring–planet mesh phases coincide; Z_ring taken negative for
   internal gears, hence the (+). Corroborated by Zou 2015 homogeneity
   condition (Z_R+Z_S)/n_b = N and the Xue 2020 unified-assembly abstract.
   **Structural fact**: PE620's four planets are independent single-planet
   trains (d_i=1), so the step stays 2π/(c+s) and the planet tooth counts p,q
   do NOT enter the step (Guo eq. 5.25). Less-mesh-angle claims in
   `research/CLAIMS.md`; source
   `research/sources/compound-planetary-dynamics-mesh-phases-guo-2011.full.md`.
   **Caveat every solver must hear**: Guo (like the design guides) derives the
   rule for a COAXIAL train; PE620 has S OFF-CENTRE — planet centres lie on an
   ellipse, and the angle about S is not the angle about C. A single-center
   β-lattice is therefore a conjecture, and it is exactly the part both failed
   models bet on.
2. **Ellipse locus (sourced).** The centre of a planet tangent internally to C
   and externally to S lies on the ellipse with foci at the centres O and S and
   sum of focal distances (R−ρ)+(r+ρ) = (c+s)/2π — the planet size **cancels**,
   so all four planets share one ellipse (major semiaxis (c+s)/4π, focal
   separation d = |OS|). Claim `tangent_circle_center_ellipse`. A rational
   parametrization exists via the Pappus chain (durable memory): x_n =
   r(1+r)/(2[n²(1−r)²+r]), y_n = n·r(1−r)/(n²(1−r)²+r).
3. **Teeth-matching conditions (sourced, partial).** Zou 2015: concentric /
   homogeneity-distribution / neighbour / gear-ratio conditions
   (`research/summaries/single-planetary-teeth-matching-zou-2015.md`); PE620
   explicitly permits planet overlap, so only the concentric-type geometry and
   the assembly discreteness survive. Xue 2020 full derivation unobtainable
   (JS-rendered page, DOAJ 403) — abstract only.

## Ruled out — both implemented models FAILED (checked; return 0)

1. **Continuous single-d model — DEAD.** `code/lib/gears.py` / `code/brute.py`
   (`code/oracle_test.py`): g(16,5,5,6)=0 vs 9; a 20k-point residual scan found
   no non-degenerate valid offset d (global minimum only at the degenerate
   endpoint d=1/2π, where the two p-planets coincide); all 22 G(20) pairs give
   0. Notes + claim `gears_model_fails_oracle` (status: checked):
   `code/out/oracle_test.md`, `code/out/oracle-model-broken.md`,
   `code/out/oracle_test.txt`.
2. **Single-d discrete least-mesh-angle lattice model — NOW DEAD (new checked
   failure).** `code/pattern/discrete_model_probe.py`, run by a driver that
   wrote `code/out/lattice_test.txt`: slots k·2π/(s+c) about O or about S (all
   four planets sharing one centre offset d, d from each slot's tangency
   quadratic), valid iff 2F_p, 2F_q, F_p−F_q ∈ ℤ (mod 1) (mpmath-60, T-sign ±1,
   all four {O,S}² anchor variants). Result: **0 distinct valid d — g(16,5,5,6)=0
   vs 9; G(16)=0 vs 9; G(20)=0 vs 205**, 0.00 s per case (candidate d's never
   satisfy both planet types together, so the phase test is barely reached).
   What this does NOT kill: the least-mesh-angle theorem itself — only this
   implementation of it. Plausible diagnosis (conjecture): the single-center
   β-lattice is the wrong discretization for an off-centre sun. **No claim
   block/note yet documents this failure** — only raw output; whoever reuses it
   should write the checked claim. Unrun sibling: `code/pattern/phase_grid.py`
   (clean signed phase re-derivation E = Rβ − rγ − ρψ, mirror-signed β/γ, ψ =
   lamS−lamC, 400k-point fine scan of d; NO output on disk yet).
3. **Idler-phase B-model — NEW checked failure.** `code/pattern/phase_model_probe.py` →
   `code/out/phase_model_test.txt`: NO position lattice; d free over
   (max_t|a_t−b_t|, R−r−1]; idler-spin elimination leaves B_t =
   (r+ε·t/2π)·γ + ε·(R−t/2π)·β, valid iff 2B_p, 2B_q, B_p−B_q ∈ ℤ (mod 1),
   ε=±1: **g(16,5,5,6)=0 for BOTH ε variants** (0.09 s). This is pattern_finder's
   derivation — a DIFFERENT congruence system from the W-model (Established #2;
   (s±t),(c∓t) vs s,c,t), so it does not settle the live hypothesis. Two
   phase-elimination systems now dead with the same shape of conditions — any
   NEW one is a hypothesis to pin against g=9 first, not the oracle. Raw output
   only; write the checked claim before reuse.

## Numbers

Oracle values — still reproduced by **no** program: g(16,5,5,6)=9, G(16)=9,
G(20)=205. Every computed g value on disk is 0 (the two dead models above). No
positive terms exist ⇒ sequence/OEIS analysis remains blocked.

## Recalled

Cognee holds: the four gear-geometry source cards (Drivetrain Hub, UTS, Gear
Solutions, Cut-the-Knot); the teeth-matching / assembly-condition findings (Zou
2015, Xue 2020 abstract); the dead continuous-model verdict (pattern_finder);
graph edges linking β-discretization ↔ ellipse locus ↔ mesh-phasing theory
(Guo 2011, Parker–Lin 2004, ISMA 2016 in `research/sources/`). Scratch agrees:
no computed g/G sequence. No prior PE620 result is importable — the run's
numbers must stand on its own computation.

## Gaps

- **No oracle reproduces 9/9/205** — the top blocker (GOAL.md step 1). Every
  candidate model so far returns 0, so the reading of "perfectly meshing" or of
  the discreteness is still unvalidated.
- The correct discreteness for the off-centre geometry: how tooth-phase
  congruences discretize planet positions on the shared ellipse (open; likely
  the crux of the whole problem).
- Exact count of g, and summing G(500) without enumerating s+p+q ≤ 500 (cost
  must not grow with the bound 500).
- d enters as the ellipse focal separation, bounded by d ≥ max|(R−ρ)−(r+ρ)| and
  d ≤ R−r−1 (the 1cm gap); counting detail open.