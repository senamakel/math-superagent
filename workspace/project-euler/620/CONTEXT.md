# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. It carries what an agent would otherwise rebuild from disk:
established results with their basis, approaches that died and why, computed
numbers, durable memory that bears on the problem, and where two accounts
disagree. It is not a catalogue of files — `research/INDEX.md` is that — and not
a narration of what agents did.

**Token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000). The file is re-sent on
every model call in every role that reads it; length here is a bill paid many
times over. Link the file holding any detail compressed away. Durable findings
belong in Cognee; a statement nobody can trace to a source is worth none.

## Established

**Problem (PE 620, `problem.md`, restatement `GOAL.md`).** C: internal ring gear,
circumference c. S: sun gear, circumference s, OFF-CENTRE inside C. Four planets
(two of circumference p, two of q; p<q), each tangent internally to C and
externally to S; planets MAY overlap (waives the neighbor condition); closest
S–C boundary gap ≥1cm ⇒ centre offset d ≤ R−r−1. c,s,p,q integers ≥5.
"Perfectly meshing" = constant angular-velocity ratio, teeth align with grooves.
`g(c,s,p,q)` = number of valid arrangements (finite; only discrete arrangements
mesh). `G(n)=Σ_{s+p+q≤n} g(s+p+q,s,p,q)`, p<q, p,s≥5. Worked: g(16,5,5,6)=9,
G(16)=9, G(20)=205; target G(500).

**THE WINNING DISCRETENESS — computed and checked (reproduces all three
oracles).** The n_t integer meshing model (`code/pattern/n_integer_count.py`,
checked; high-precision verification `code/pattern/winner_refine.py`, mpmath
60-digit). For planet type t define
`n_t(d) := [(c−t)·β(d) + (s+t)·μ(d)] / π`, where β = angle of the *upper*
tangency point about ring centre O, μ = its angle about sun centre S, at centre
separation d. A valid arrangement exactly iff:
(a) `n_p(d), n_q(d) ∈ ℤ`, and (b) `n_p − n_q ≡ p − q (mod 2)`.
Each valid d gives exactly **one** arrangement: two p-planets at their mirror
tangency points, two q at theirs (degenerate endpoints, where a pair coincides
y≈0 and planets are not distinct, are excluded). This reproduces g(16,5,5,6)=9,
G(16)=9, G(20)=205 (all 22 pairs, `code/out/n_integer_model.txt`).

**Structural identity (computed, high-precision checked).** At every valid d,
`n_p + n_q = s+c` EXACTLY (21 for the flagship); at non-valid d this fails, so
it is a genuine constraint, not trivial. `n_p(d)` is increasing in d over the
open interval (d_min, d_max) and takes consecutive integer values (1..9 for the
flagship). **So g = the number of valid integer levels of n_p in the interval** —
an O(#integer levels) count, independent of the bound 500. The intended G(500)
method is therefore a root-location/bisection over integer levels of n_p, NOT a
grid scan (the d-grid in n_integer_count.py is a small-case probe of the model
only). Nine d for the flagship: 0.16096, 0.16657, 0.17670, 0.19273, 0.21733,
0.25572, 0.31940, 0.43890, 0.73162.

**Geometry (sourced).** Planet centre tangent internally to C and externally to
S lies on the ellipse with foci O,S and sum of focal distances
(R−ρ)+(r+ρ) = (c+s)/2π — planet size **cancels**, so all four planets share one
ellipse (focal separation d; major semiaxis (c+s)/4π). Rational parametrization
via Pappus chain (durable memory). For fixed d and type t, tangency forces
exactly TWO planet centres, mirror images across the line of centres — the count
is over d, never over angular positions (claim `offcentre_two_positions_per_type`).

## Ruled out — every candidate that returns 0 or the wrong count (checked)

1. **Continuous single-d phase-elimination model** (`lib/gears.py`, `brute.py`):
   g=0 vs 9; residual minimum only at degenerate d=1/(2π). Claims
   `gears_model_fails_oracle`, `oracle_model_reproduces_zero`.
2. **Single-centre least-mesh-angle lattice** (`discrete_model_probe.py`): planets
   at slots k·2π/(s+c) about O or S sharing one d; g=G16=G20=0. Kills only the
   implementation, not the coaxial lattice theorem; for an OFF-CENTRE sun a
   single-centre β-lattice is the wrong discretization (tangency forces positions;
   there is no free angular choice).
3. **Idler-phase "B-model"** (`phase_model_probe.py`): B_k=(r+ε·ρ_k)γ_k+ε(R−ρ_k)β_k,
   conditions 2B_p,2B_q,B_p−B_q∈ℤ; g=0 for both ε=±1.
4. **W-invariant off-centre model** (`w_invariant_test.py`) — previously the live
   hypothesis, now **checked dead**: thread `offcentre-mesh-phase-model.md`
   derives per-planet invariant W_j = s·φ_j + c·χ_j − t·γ_j pairwise congruent
   mod 2π, but NONE of the four tested congruence formulations (A=s·φ+c·χ∈πℤ both
   types AND cross; B=cross only=5; C=t·γ−c·χ∈πℤ both AND cross=0; D=A with W') 
   gives g=9 (best B=5, stable to 1e6/4e6/12e6 with independent cluster check).
   Set C's "identically satisfied" suspicion is falsified (residues to 0.5).
5. **Tangency-enumeration residue scan** (`tangency_enum.py`): claims a specific
   (σ,η,θ)=(−1,−1,−1) sign variant gives g=9, but other variants give 6–10 and it
   was never extended to G(16)/G(20); superseded by the cleaner n_t model.

General lesson (confirmed by four dead families): monotone-integer-level counting
in a single parameter d is the shape that works; any "both planet types must
satisfy a congruence at the same d" phase system that cannot be reduced to
integer levels of ONE monotone function of d has returned 0.

## Numbers

All three oracle values are now reproduced by `n_integer_count.py`: g(16,5,5,6)=9,
G(16)=9, G(20)=205 (`code/out/n_integer_model.txt`, per-pair table present;
high-precision check `code/out/winner_refine.txt` confirms the n_p+n_q=s+c identity
to 60 digits). The 22 per-pair g values for G(20) are listed in n_integer_model.txt.
G(500) remains UNCOMPUTED (n_integer_count's d-grid scans are O(N); the real
method must count integer levels of n_p without scanning — TASKS.md step 3/4 open).

## Recalled

Cognee holds the gear-geometry cards (Drivetrain Hub, UTS, Gear Solutions,
Cut-the-Knot), the teeth-matching/assembly findings (Zou 2015, Xue 2020
abstract), the four dead-model verdicts above, and — newly promoted — the n_t
winner with its structural identity (this run's computation). Scratch had
overstated the tangency-enum "oracle match" as if G(16)/G(20) were done; they
were not until n_integer_count ran. Earlier runs carry no usable PE620 numeric
result; the run's numbers must stand on its own computation.

## Gaps / open

- **G(500) by theory, not scanning** (the real method): count valid integer
  levels of n_p over (d_min,d_max) for each (c,s,p,q) with s+p+q ≤ 500, cost not
  growing with 500 — root-location/bisection per integer level, plus the parity
  and degenerate-exclusion filters. `solution.py` must agree with
  n_integer_count on every reachable case, then compute G(500).
- **Independent second route** (GOAL step 5): e.g. a different derivation (the
  pitch-difference/whole-number formulation of the Split-Torque / Zhao-Li /
  White-Patil sources as a cross-check), or brute agreement at maximum feasible
  (c,s,p,q). Not yet done.
- d bounds: d_min = max(|a_p−b_p|,|a_q−b_q|), d_max = min(a_p+b_p, a_q+b_q,
  R−r−1); parity filter n_p−n_q ≡ p−q (mod 2); degenerate y≈0 endpoints
  excluded. Counting details for the closed form still open.
