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
C and externally to S; planets MAY overlap (waives the neighbour condition);
closest S–C boundary gap ≥1cm ⇒ centre offset d ≤ R−r−1. c,s,p,q integers ≥5
(teeth, pitch 1cm). "Perfectly meshing" = constant angular-velocity ratio, teeth
align with grooves. `g(c,s,p,q)` = number of valid arrangements (finite; only
discrete positions mesh). `G(n)=Σ_{s+p+q≤n} g(s+p+q,s,p,q)`, p<q, p,s ≥5.
Worked oracle: g(16,5,5,6)=9, G(16)=9, G(20)=205; target G(500).

**WINNING MODEL — FULL ORACLE MATCH (computed, checked).** `code/pattern/n_integer_count.py`
→ `code/out/n_integer_model.txt`. For planet type t at centre separation d, put
`beta` = angle of the planet centre about the ring centre O, `mu` = angle about
the sun centre S (upper tangency point), and define
`n_t(d) = [(c−t)·beta + (s+t)·mu]/π`. A d is a valid arrangement iff
`n_p(d), n_q(d) ∈ ℤ` AND `n_p − n_q ≡ p − q (mod 2)`; degenerate d (where either
type's two tangency points coincide, y≈0) excluded — the four planets must be
distinct. Reproduces **g(16,5,5,6)=9, G(16)=9, G(20)=205** (all 22 per-pair g
values in the txt). Each valid d is ONE arrangement: the two p-planets at their
mirror tangency points, the two q-planets at theirs.

**Structural identity (computed, 60-digit):** `n_p(d) + n_q(d) = s + c` holds at
*every* d (probed at arbitrary non-valid d too), not just at valid ones —
`code/out/winner_refine.txt` (`code/pattern/winner_refine.py`, mpmath-60 bisection),
which independently re-derives g=9 for (16,5,5,6). Because n_q = (s+c) − n_p, the
parity condition reduces to `(s+c) ≡ q−p (mod 2)`, independent of k — so for a
given (c,s,p,q) EITHER every integer level of n_p is valid OR none. With n_p
monotone increasing in d, g is essentially the count of integer levels n_p
crosses on (d_min,d_max) — the seed of the bound-independent formula for G(500).
**The closed-form reduction is NOT yet derived** (see Gaps).

**Two earlier models independently give g=9 as well** (rule-11 corroboration of
the count for (16,5,5,6), though both were superseded on G): (i) tangency Q-residue
enumeration `code/pattern/tangency_enum.py` → `code/out/tangency_enum.txt` (claim
`tangency_enum_oracle_match`, status checked) with residue
`Q = σρ(β−γ) − ηRβ + θrγ (mod 1)`, mirror identity Q(L)=−Q(U), exactly 9 only
under (σ,η,θ)=(−1,−1,−1); (ii) the two mirror/`UL`-side structure (all 9 valid d
are UU/LL pairs, no mixed UL). The n_integer model is the complete one: it also
delivers G(16)/G(20).

**Sourced, holds-here-corroborated governing theory** (`research/threads/offcentre-mesh-phase-model.md`):
for planet type t, |SP|=(s+t)/2π and |CP|=(c−t)/2π force each planet's centre to
one of exactly TWO points per type (intersection of two circles = mirror pair
across line SC), so an arrangement is fixed by d alone — no free angular choice;
the count is over isolated d-solutions of tooth-phase congruences, i.e. integer
levels of a monotone signed angle×tooth-count sum (`split_torque_curvilinear_quadrilateral_condition`
Segade-Robleda 2012, `zhao_li_2018_duplex_idler_meshing_condition`, `idler_double_mesh_integer_index_condition`
White–Patil 2020 — the strongest published analogues). The coaxial least-mesh-angle
lattice β=2π/(s+c) (Drivetrain Hub, UTS, Gear Solutions, Guo) is the d→0 limit and
do NOT transfer off-centre. Claim `offcentre_dual_mesh_phase_invariant` (asserted,
not the counting rule that survived — W-form failed, below).

## Ruled out — five models FAILED (all checked; all return 0 except W-B)
1. **Continuous single-d** (`code/lib/gears.py` = `code/brute.py`, `code/out/oracle_test.txt`):
   g=0; only degenerate endpoint d=1/2π. Claims `gears_model_fails_oracle`,
   `oracle_model_reproduces_zero` (checked).
2. **Single-d least-mesh-angle lattice** (`code/pattern/discrete_model_probe.py` →
   `code/out/lattice_test.txt`): planets on grid k·2π/(s+c) about O or S; g=0. The
   search space never contained the tangency positions (two points per type).
3. **Idler-phase model** (`code/pattern/phase_model_probe.py` → `code/out/phase_model_test.txt`):
   idler-freed planet, both ε=±1 give g=0.
4. **W-invariant model** (`code/pattern/w_invariant_test.py` → `code/out/w_invariant_test.txt`,
   note `code/out/w_invariant_test.md`): condition sets A/B/C/D from the thread all FAIL —
   A=0, B=5, C=0, D=0; none gives 9. C ("identically satisfied") is FALSIFIED (residues
   up to 0.5). B's 5 roots stable across N=1e6/4e6/12e6 (not a resolution artifact).
   **This corrects the previous CONTEXT note that "the W-invariant model has not been run."**
5. **Tangency Q-residue / n_integer are NOT dead** — they are the live winners; the two
   earlier lattice models (1,2) and phase models (3,4) are the dead ones.

## Numbers
Oracle now FULLY reproduced: g(16,5,5,6)=9, G(16)=9 (=same pair), G(20)=205 —
`code/out/n_integer_model.txt` (22 pairs; e.g. g(16,5,5,6)=9, g(20,9,5,6)=12, ...).
n_p integer levels 1..9 for (16,5,5,6); n_p+n_q=21=(s+c) at every solution and at
every probed d. Three independent routes agree on g=9 (n_integer, tangency-Q,
winner_refine). G(20) matched by n_integer only.

## Recalled
Cognee holds the gear-geometry source cards, teeth-matching/assembly findings
(Zou 2015, Xue 2020 abstract), the dead continuous-model verdict, and graph edges
linking least-mesh-angle β ↔ ellipse locus ↔ mesh-phasing theory (Guo 2011,
Parker–Lin 2004, ISMA 2016 in `research/sources/`). No prior PE620 numeric result
is importable — the run's numbers stand on its own computation (n_integer_model).

## Gaps
- **G(500): the efficient, bound-independent method is not written.** `n_integer_count.py`
  is an O(N) d-grid scan — correct as the counting MODEL but wrong cost for G(500).
  The route to close it: n_p is monotone in d, n_p+n_q=s+c (identity), parity is a
  fixed (c,s,p,q)-dependent check — so g is plausibly the count of integer levels of
  n_p on the open interval, i.e. a near-closed-form in (c,s,p,q). Derive the
  interval endpoints in closed form and sum without enumerating s+p+q≤500.
- **No `solution.md` / `code/solution.py` yet** (GOAL steps 3–4 open).
- **No claim note yet documents the n_integer full-oracle match** — the value most
  needing one (status=checked, sign convention, grid params, identity).
- A second independent route to G(20)=205 beyond n_integer is desirable (rule 11);
  tangency-Q covers g=9 only.
