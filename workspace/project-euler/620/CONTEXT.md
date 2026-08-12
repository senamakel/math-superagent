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

**Tangency enumeration — FIRST ORACLE MATCH: g(16,5,5,6)=9** (`code/out/tangency_enum.txt`,
`code/pattern/tangency_enum.py`). Residue model: each planet's tooth-mesh residue
Q = sigma*rho*(beta-gamma) - eta*R*beta + theta*r*gamma (mod 1), where beta=angle
about O, gamma=angle about S, rho planet radius. Mirror identity Q(L) = -Q(U)
(mod 1). Variant (sigma=-1, eta=-1, theta=-1): **9 valid d values, all from
pp=UU qq=UU (9) and pp=LL qq=LL (9) — no mixed (UL) combos survive.** The
other 7 sign variants give 6-10 but only (sigma=-1, eta=-1, theta=-1) yields
exactly 9. **G(20)=205 NOT YET CHECKED** — the enumerator is hardwired to
(16,5,5,6); generalizing it to all 22 G(20) tuples is the immediate next task
(TASKS.md STEP 1). Grid: 2^20+1 points over d in [d_min, d_max] (spacing ~5.6e-7),
COARSE_TOL=1e-4 (grid clustering), TIGHT_TOL=1e-9 (mpmath refinement).

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

Oracle values: g(16,5,5,6)=9 **NOW REPRODUCED** by tangency enumeration
`code/pattern/tangency_enum.py` → `code/out/tangency_enum.txt` (variant
sigma=-1, eta=-1, theta=-1; grid 2^20+1 points). G(16)=9 follows (only pair).
G(20)=205 **NOT YET CHECKED** — the enumerator must be generalized to accept
arbitrary (c,s,p,q) arguments and run over all 22 tuples.

## Recalled

Cognee holds: four gear-geometry source cards (Drivetrain Hub, UTS, Gear
Solutions, Cut-the-Knot); teeth-matching / assembly-condition findings (Zou
2015, Xue 2020 abstract); dead continuous-model verdict; graph edges linking
least-mesh-angle β ↔ ellipse locus ↔ mesh-phasing theory (Guo 2011, Parker–Lin
2004, ISMA 2016 in `research/sources/`). Scratch agrees: no computed g/G
sequence. No prior PE620 result is importable — the run's numbers must stand on
its own computation.

## Gaps

- **G(20) not yet verified** — the top blocker. One matched value (g(16,5,5,6)=9)
  is a coincidence until all 22 G(20) tuples sum to 205. Generalize the
  tangency enumerator and run it.
- **No claim written** for the tangency enumeration result — the claim must go
  beside the output in code/out/, with status=checked, the exact sign convention,
  grid/tolerance params, and the mirror structure (only UU/LL survive).
- **No bound-independent formula** for g(c,s,p,q). The enumerator uses a 1M-point
  grid scan — fine for oracle verification, wrong for G(500). Need the algebraic
  equation that Q_p(d) == Q_q(d) (mod 1) reduces to.
- Exact count of g, then summing G(500) without enumerating s+p+q ≤ 500.
