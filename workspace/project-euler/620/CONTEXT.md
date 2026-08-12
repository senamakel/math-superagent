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
`g(c,s,p,q)` = number of valid arrangements (finite). `G(n)=Σ_{s+p+q≤n}
g(s+p+q,s,p,q)`, p<q, p,s≥5. Worked: g(16,5,5,6)=9, G(16)=9, G(20)=205;
target G(500).

**Residue form — settled.** The correct tooth-mesh residue per planet type t is
`Q_t(d) = (c-t)·β(d) + (s+t)·μ(d)` (the n_t/π form), with sign convention
(sigma,eta,theta)=(-1,-1,-1) — the only variant of eight giving g(16,5,5,6)=9
(claim `tangency_enum_oracle_match`, anchor `code/out/tangency_enum.txt`). β =
angle of planet centre about ring centre O; μ = angle about sun centre S; both
for the upper tangency position (two mirror positions exist per type at each d).

**Two implementations, one verified:**

1. `n_integer_count.py` (grid enumeration, O(N) d-scan): n_t = Q_t / π (not
   mod-1), conditions n_p∈ℤ, n_q∈ℤ, n_p−n_q≡p−q (mod 2), degenerate endpoints
   (y≈0) excluded. **Reproduces g=9, G(16)=9, G(20)=205** — all three oracle
   values. Output: `code/out/n_integer_model.txt` with per-tuple G(20) table.

2. `fast_g.py` (monotone f-crossing, no grid): f(d)=Q_p(d)−Q_q(d) strictly
   increasing; g = #{m∈ℤ : f(DL) < m < f(DU)}. **Reproduces g=9, G(16)=9 but
   G(20)=213 vs oracle 205** — overcount of 8 (claim `g20_overcount_by_eight`,
   anchor `code/out/G20_overcount.md`). Sign convention correct; admissibility
   rule wrong.

**Structural identity (computed).** At valid d, n_p + n_q = s+c exactly; n_p
increases monotonically with d and takes consecutive integer values 1..9 for the
flagship. g = number of valid integer levels of n_p in (d_min,d_max).

**Geometry (sourced).** All four planets share one ellipse (foci O,S, major
semiaxis (c+s)/4π) — planet radius cancels in sum of focal distances. For fixed
d and type t, exactly two tangency positions (mirror pair across line of
centres); the count is over d, never over angular positions.

## Ruled out

1. **Continuous single-d phase-elimination** (`lib/gears.py`): g=0 vs 9.
2. **Single-centre least-mesh-angle lattice** (`discrete_model_probe.py`): g=0.
3. **Idler-phase B-model** (`phase_model_probe.py`): g=0.
4. **W-invariant off-centre model** (`w_invariant_test.py`): max 5 vs 9.
5. **Other 7 sign variants of the tangency residue**: give g∈{6,7,10}, none 9.

All dead models return 0 or wrong count; all used phase-congruence systems that
didn't reduce to monotone integer-level counting in d. That shape — integer
levels of ONE monotone function of d — is the one that works.

## Numbers

Oracle values: g(16,5,5,6)=9, G(16)=9, G(20)=205.
`n_integer_count.py` reproduces all three; per-tuple G(20) table at
`code/out/n_integer_model.txt`.
`fast_g.py` reproduces g=9, G(16)=9, but G(20)=213 (+8 overcount).
G(500) uncomputed.

## Current task (directive 3)

**Diagnose the overcount.** Run `fast_g.py` per-tuple over G(20), compare
against `n_integer_count.py` table, find which tuples differ, print offending
d values and planet positions, fix the admissibility rule. The sign convention
and residue are NOT to be re-derived. See `TASKS.md`.
