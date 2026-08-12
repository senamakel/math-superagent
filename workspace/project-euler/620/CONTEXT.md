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
Four distinct planets, circumferences p,p,q,q (p<q), each tangent internally to C
and externally to S; planets may overlap each other; closest gap between S and C
boundaries ≥1cm. c,s,p,q integers ≥5. "Perfectly meshing" = constant angular
velocity ratio, teeth align with grooves. `g(c,s,p,q)` = number of valid
arrangements (finite; only discrete positions mesh). `G(n)=Σ_{s+p+q≤n} g(s+p+q,
s,p,q)`, p<q, p,s ≥5. Worked: g(16,5,5,6)=9, G(16)=9, G(20)=205; target G(500).

**The continuous centre-distance model is DEAD** (see Ruled out). The run's
working hypothesis is now the **discrete least-mesh-angle lattice model**, not
yet implemented: each planet meshes with both S and C only at angular positions
about S's centre that are integer multiples of β = 2π/(s+c) (`least_mesh_angle*`
claims, three independent sources). A planet of circumference m tangent to C
internally and S externally has its centre on the ellipse with foci at C's and
S's centres, major semiaxis (c+s)/4π (m cancels) (`tangent_circle_center_ellipse`).
So each legal arrangement should be a lattice point (multiple of β) lying on that
ellipse; g(c,s,p,q) is then a discrete count over such points. **Not verified —
but a probe exists and is the next step**: `code/pattern/discrete_model_probe.py`
enumerates every candidate centre-offset d for four model variants (lattice
anchored at ring centre O vs at sun centre S, × T-sign ±1) and checks the phase
congruences (2Fp,2Fq,Fp−Fq ∈ ℤ) at mpmath-60 precision, then reports which
variant reproduces g(16,5,5,6)=9. **It has never been run** — no output in
`code/out/`. tool_builder should run it first.

## Ruled out

**The continuous centre-distance model (code/lib/gears.py) — FAILED, checked.**
It parametrizes each planet centre as circle(O, R−ρ) ∩ circle(S, r+ρ) with a
single free centre-offset d (R=c/2π, r=s/2π), and derives the meshing condition
as three phase-eliminated congruences `2F_p, 2F_q, H ∈ ℤ (mod 1)` holding at
valid d. Running it gives **g(16,5,5,6)=0 vs stated 9**; a 20k-point scan found
no non-degenerate valid d (global residual min only at the degenerate endpoint
d=1/2π where the two same-size planets coincide). `oracle_test.py` reports all
three oracle values DISAGREE (G(16): 0 vs 9 over 1 pair; G(20): 0 vs 205 over 22
pairs). The parameterization itself misses all 9 arrangements — the intended
models are NOT a single continuous d. Detail + claim `oracle_model_reproduces_zero`
in `code/out/oracle-model-broken.md`; full test log `code/out/oracle_test.txt`.
`code/brute.py` exists but implements the same dead continuous-d model (with the
corrected T-sign and an independent phase-solve verifier); it corroborates the
failure but is **not** the needed oracle and has not reproduced 9/9/205. The
discrete-model probe `code/pattern/discrete_model_probe.py` is written but
unrun.

## Numbers

Oracle values from the statement — reproduced by **no** program yet (the discrete
oracle does not exist):
- g(16,5,5,6) = 9,  G(16) = 9,  G(20) = 205,  target G(500).
The only computed numbers on disk are the *failures*: gears.py returns 0 for all
values it touches. Each (c,s,p,q) pair with s+p+q≤20, s,p≥5, p<q has g=0 under
the dead model (listed in `code/out/oracle_test.txt`).

## Recalled

Durable Cognee memory holds the four gear-geometry source cards (Drivetrain Hub,
UTS, Gear Solutions, Cut-the-Knot) backing the `least_mesh_angle*` and
`tangent_circle_center_ellipse` claims, and the dead-model claim
`oracle_model_reproduces_zero`. Scratch confirms no computed g/G sequence exists —
pattern/sequence analysis stays blocked until the discrete model emits real terms.
No prior PE620 result is importable; the run's numbers must stand on its own.

## Gaps

- **No working oracle**: the discrete lattice model must be run and reproduce
  9/9/205 before anything is trusted (completion criteria in `GOAL.md`, step 1).
  First move: run `code/pattern/discrete_model_probe.py` as-is.
- **Exact method**: how the ellipse ∩ β-lattice intersection is counted exactly,
  and how G(500) is summed without enumerating all s+p+q ≤ 500 — cost must not
  grow with the bound 500.
- Whether/how d (S↔C offset) and the ≥1cm gap enter the count is pinned by the
  geometry (ellipse-focus separation = d), but the discrete counting detail is
  open until the model runs.
