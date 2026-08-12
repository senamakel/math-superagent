# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. It carries what an agent would otherwise rebuild from disk:
established results with their basis, approaches that died and why, computed
numbers, durable memory that bears on the problem, and where accounts disagree.
It is not a catalogue of files — `research/INDEX.md` is that — and not a
narration of what agents did.

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
arrangements (finite; only discrete positions mesh). `G(n)=Σ_{s+p+q≤n}
g(s+p+q,s,p,q)`, p<q, p,s ≥5. Worked: g(16,5,5,6)=9, G(16)=9, G(20)=205; target
G(500).

**Tangency forces positions — the count is over d, not over a beta-lattice
(asserted geometry; holds-here: yes; claim `offcentre_two_positions_per_type`).**
For planet size t (radius ρ_t=t/2π): exact tangency to both gears forces
|SP|=(s+t)/2π AND |CP|=(c−t)/2π simultaneously. With the two centres d apart
this is the intersection of two circles = exactly **two** points, mirror images
across the line of centres. So an arrangement (2 p-planets + 2 q-planets) is
fixed by d alone. d ∈ (d_min, d_max): d_min = max(|a_p−b_p|, |a_q−b_q|) with
a_t=(s+t)/2π, b_t=(c−t)/2π; d_max = (c−s)/2π − 1 (the 1 cm gap). This is WHY
both single-centre beta-lattice models returned 0 (below): they enumerated
angular positions on a lattice that tangency had already ruled out. The centres
all lie on one shared ellipse (foci O,S, sum of focal distances (c+s)/2π; planet
size cancels) — consistent with, and looser than, the two-positions fact.

**Leading hypothesis — off-centre dual-mesh phase model (derived in full;
holds-here UNCHECKED, oracle pending; claims `offcentre_dual_mesh_phase_invariant`,
`coaxial_limit_reproduces_lattice`).** The thread
`research/threads/offcentre-mesh-phase-model.md` derives from tooth-phase
congruences (Guo 5.21–5.22 pitch-point convention; internal-ring phase −c·contact
angle) that simultaneous meshing of all four planets is equivalent to the
per-planet invariants W_j = s·φ_j + c·χ_j − t_j·γ_j being pairwise congruent
mod 2π, where (φ,χ,γ) are the triangle angles at S, C, P from the law of cosines
(φ+χ+γ=π; γ=π only coaxially). This reduces to three explicit one-variable
congruences in d:
- mirror pair of one type: s·φ_t + c·χ_t ∈ π·ℤ
- cross-type: s(φ_p−φ_q) + c(χ_p−χ_q) − p·γ_p + q·γ_q ∈ 2π·ℤ
g = #{d ∈ (d_min,d_max) satisfying all three} × κ, with κ = mirror-identification
factor ∈ {1,2} to be fixed by the oracle (also decide whether the degenerate
single-contact endpoint d=d_min counts — there the two planets of a type
coincide). Coaxial limit d→0 reduces to W=(s+c)ψ − t·π and gives ψ ∈
(2π/(s+c))·ℤ — reproducing the least-mesh-angle rule of all three design guides
and Guo 5.21–5.22, so this model contains the sourced rule as a special case.
Cost per g is O(#solutions), independent of any bound. **This is the current
direction; only its setup is shown consistent — it has NOT yet been checked
against 9/9/205.**

## Ruled out — three implemented models FAILED (all checked; all return 0)

1. **Continuous single-d model — DEAD.** `code/lib/gears.py` / `code/brute.py`
   (`code/oracle_test.py`): g(16,5,5,6)=0 vs 9; 20k-point residual scan found no
   non-degenerate valid d (global minimum only at degenerate endpoint d=1/2π);
   all 22 G(20) pairs 0. Claims `gears_model_fails_oracle`,
   `oracle_model_reproduces_zero` (status: checked); notes
   `code/out/oracle_test.md`, `code/out/oracle-model-broken.md`,
   `code/out/oracle_test.txt`.
2. **Single-d least-mesh-angle lattice model — DEAD.** `code/pattern/discrete_model_probe.py`
   → `code/out/lattice_test.txt`: planets at slots k·2π/(s+c) about O or about S
   (all four sharing one d), valid iff 2F_p, 2F_q, F_p−F_q ∈ ℤ (mpmath-60, all
   four {O,S}² anchor variants). Result: g(16,5,5,6)=0, G(16)=0, G(20)=0. Killed
   by the geometry fact above — the search space did not contain the tangency
   positions. Does NOT kill the least-mesh-angle theorem itself. No claim note
   yet documents this failure (raw output only).
3. **Idler-phase model — DEAD (third checked failure).** `code/pattern/phase_model_probe.py`
   → `code/out/phase_model_test.txt`: planet treated as free idler, its spin
   eliminated per planet, conditions 2B_p, 2B_q, B_p−B_q ∈ ℤ with
   B_k(ε)=(r+ε·ρ_k)γ_k + ε(R−ρ_k)β_k (β ang of P about O, γ ang about S). Both
   ε=+1 and ε=−1 give g(16,5,5,6)=0. **Note: this is NOT the W-invariant model** —
   the thread's `blocked-by` says only the idler-phase model (2 of its 4
   χ/γ-sign variants) was probed; the W-invariant model has not been run. No
   claim/note documents this failure yet.

Unrun sibling: `code/pattern/phase_grid.py` (clean signed phase re-derivation
E = Rβ − rγ − ρψ; no output on disk).

## Numbers

Oracle values — still reproduced by **no** program: g(16,5,5,6)=9, G(16)=9,
G(20)=205. Every computed g value on disk is 0 (three dead models above). No
positive terms exist ⇒ sequence/OEIS analysis remains blocked.

## Recalled

Cognee holds: four gear-geometry source cards (Drivetrain Hub, UTS, Gear
Solutions, Cut-the-Knot); teeth-matching / assembly-condition findings (Zou
2015, Xue 2020 abstract); dead continuous-model verdict; graph edges linking
least-mesh-angle β ↔ ellipse locus ↔ mesh-phasing theory (Guo 2011, Parker–Lin
2004, ISMA 2016 in `research/sources/`). Scratch agrees: no computed g/G
sequence. No prior PE620 result is importable — the run's numbers must stand on
its own computation.

## Gaps

- **No oracle reproduces 9/9/205** — the top blocker (GOAL.md step 1). Every
  model so far returns 0, so the reading of "perfectly meshing" / discreteness
  is still unvalidated.
- Immediate next step (from the thread): probe the W-invariant model — all 4
  independent sign combinations of the χ- and γ-coefficient terms; if all return
  0, fall back to enumerating the 9 (16,5,5,6) configurations directly by
  tangency, computing tooth phases numerically, and reading the meshing
  condition off what survives. Also pin κ and the endpoint convention.
- Exact count of g, then summing G(500) without enumerating s+p+q ≤ 500 (cost
  must not grow with the bound 500). The W-model's O(#solutions) per g is the
  intended route.
