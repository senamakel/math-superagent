# Shared context

Problem: Project Euler **761** — runner/swimmer pursuit-evasion on a regular
n-gon pool (swimmer at center speed ≤1, runner on boundary at edge-midpoint
speed ≤v). State of the run: **hexagon value computed to 8 dp via a validated
formula and reduced to an exact closed form; the one independent game-encoding
solver (`code/indep_game_encoding.py`) has been run and its output captured
(`code/indep_game_encoding_OUTPUT.txt`) — it FAILS to reproduce the oracles,
because it encodes the straight-dash red herring, so do NOT report the value as
independently verified.** Full statement: `/workspace/problem.md`.

## The answer

**V_hexagon = 5.05505046330389333772536479582… → 5.05505046** (8 dp;
full-precision value printed by `code/verify_hexagon.py`, mpmath/sympy default).
For n=6: K=2, α = ½(π/3 + arccos(−1/8)) ≈ 1.37166085458, V = 1/cos(α).

**Exact closed form (established, exact algebra):** V_hexagon = **2 + 2√21/3
= (40+8√21)/3 under the radical** (²/³·√21 ≈ 3.05505046, +2 = 5.05505046).
Derivation (exact radicals, `code/hexagon_closed_form.py` +
`code/confirm_hexagon_closedform.py`): inner = −1/8, cos(2α) = −(1+3√21)/16,
cos²α = (15−3√21)/32, V² = (40+8√21)/3, square of 2+2√21/3 = same. I
(curator) re-derived this by hand and it is exact; confirms the decimal to
*full* precision.

## Method (sourced, exact formula)

For a regular n-gon, the critical speed is V(n) = 1/cos(α) where, with θ=π/n
and t=tanθ:

```
K   = largest integer in [0,n] with  sin(Kθ) − (K+n)·t·cos(Kθ) < 0
      (== floor of the unique root of tan(xθ) − (x+n)t in [1, n/2))
α   = ½·( Kθ + acos( 2·sin(Kθ)/((K+n)·t) − cos(Kθ) ) )
```

Source: stewbasic, Math.SE q.1762665 (via Wayback); corroborated by Abel et
al., "Escaping a Polygon", arXiv:2007.08965. Mechanism = the same boundary-time
identity as the circle: equalize the swimmer's straight-line escape time to an
exit point against the runner's perimeter time to that point; the safe region
is the pool **scaled homothetically** (perimeter v× smaller) — on a polygon the
runner's angular speed is non-constant, so the safe region is a scaled copy,
not a circle.

## Validation — READ THE STATUS LABELS CAREFULLY

**Formula validated against the statement's own oracle anchors (sourced → real):**
- **n=3**: V=(3+√5)·√2 = 7.4049183473 — matches Abel et al. Thm 4.5 exact.
- **n=4**: V=√(5/2·(7+√41)) = 5.78859314459 — matches Abel 4.6, David K
  (a *genuinely distinct* geometric derivation), and the statement oracle
  5.78859314.
- **n→∞**: converges to circle constant 4.6033388 (V(10000)=4.60333900) —
  matches IBM Ponder This oracle 4.60333885.

These anchors make the *formula* trustworthy, but on their own they do not
verify the *n=6 value* by a second route.

**Hexagon: the independent route WAS run and CAPTURED, and it FAILS to
reproduce the oracles — it encodes the documented straight-dash red herring.**
`code/indep_game_encoding_OUTPUT.txt` (captured, 1254 bytes):
circle 4.14159265 (= π+1, the red herring, NOT 4.60333885), square 4.09372236,
hexagon 3.98230929; r=0 never-staging controls 3.1416/3.1623/3.0551 all sit
below the staged values, confirming the model does measure a staging gain. The
solver is genuinely independent of the K/α formula (no K/alpha/arctan anywhere;
bisects on v solving g(v)=v, g = max over boundary Q of runner-perim-dist(Q)/
swim-dist(Q) at stage radius 1/v), BUT it models the dash as a straight ray from
a diametrically-opposite staging point — exactly the dead-end that caps the
circle at π+1 (see Ruled out). So it is an independent *attempt* whose model is
wrong, not the missing verification. Honest status: **value = single (formula)
route, numerically + exact-closed-form confirmed; NO independent model has yet
reproduced any oracle, because the only independent game-encoding built encodes
the red-herring staging.** A correct independent route needs the tangent-chord
staging (circle's sin B=(π+B)/v, or a David-K-style n=6 construction), not a
straight radial dash. Thread
`research/threads/hexagon-critical-speed.md` and reflection memory flag this.
**Thread staleness:** that thread predates the exact closed form and the
independent-solver run; its status/"Next" lines (re-derive the exact value;
build option-(a) numeric check) are superseded — do not re-run
`code/indep_game_encoding.py` (dead end, output captured) or re-derive the
closed form. CONTEXT.md is authoritative over the thread.

**Two more solver scripts exist on disk but were NEVER run — no captured
output, not in `code/INDEX.md`, no scratch/memory record of results.** Scratch's
last entry ("direct-game solver agent-run-15 still running") matches these; the
session ended before any output. `code/hexagon_first_principles_explore.py` is
the *correct-framework* attempt: stage on the scale-1/v homothetic hexagon
boundary keeping the runner opposite, committed-CCW perimeter distance, bisect
on v, with built-in circle self-validation (must reproduce 4.60333885 before any
hexagon number is trusted). `code/hexagon_independent_solver.py` is another
straight-dash variant (stage at rho=P/2v then a chord) — the same red-herring
family as `indep_game_encoding.py`, NOT the circle-validated two-phase
mechanism. So the missing independent route is still missing as *verified
evidence*: whoever continues it may run `hexagon_first_principles_explore.py`
(its circle gate is the acceptance test), but nothing on disk now counts as
verification.

### Circle case (established, sourced, CLOSED — do not re-derive)
V_circle from cos B=1/V, sin B=(π+B)/V, i.e. tan B=π+B, V=1/cos B ≈ 4.60333885.
Source: IBM Ponder This May 2001, `research/summaries/ponder-this-goblin-pool-circle.md`.
Two-phase mechanism: stage on radius-1/v arc keeping diametrically opposite the
runner, then tangent chord to a shore point offset by B. This is the template
the n-gon generalizes.

## Ruled out / dead ends

- **Naive "stage at antipode + straight dash"** gives only π+1 ≈ 4.1416, NOT
  the circle oracle — the documented red herring. Correct model is the
  two-phase staging-arc + tangent-chord. Falsifying check kept in
  `code/explore_general_dash.py`. **A naive straight-dash polygon model is only
  a lower bound; do not trust it as a hexagon check.**
- **K(n) = floor(3n/7) for all n** is FALSE beyond n=85 (first deviation n=86,
  off by +1); the period-7 recurrence also breaks. Asymptotic truth:
  K(n)/n → c ≈ 0.4302966531 solving tan(cπ)=π(c+1), so K≈floor(c·n); c≠3/7.
  floor(c·n) is robust but non-exact (fails at n=165, n=3809, boundary effects
  when c·n lands just below an integer). K is an auxiliary index in V(n); V(n)
  changes smoothly, so none of this affects the 8-dp answer. OEIS small-term
  matches (A057357) are coincidences. Details: `code/k_*` files,
  `code/pattern_findings.md`.
- **A general closed form V(n)² = quadratic surd for all n is FALSE.** Exact
  minpolys (computed, sympy): n=3 x²−56x+64, n=4 x²−35x+50, n=6 9x²−240x+256
  (roots 28±12√5, 5/2(7±√41), (40±8√21)/3 — the last is exactly the hexagon
  V²); V(5)² and n≥7 are NOT quadratic (minimal-polynomial degree >2, and a
  PSLQ-style search finds no small integer quadratic for V(5)²). Clean surd
  closed forms exist only for n=3,4,6 — do not chase one for other n. Code:
  `code/v2_quadratic_test.py`, `code/v2_quad_independent2.py`.

## Numbers / anchors (cheap to restate, expensive to recompute)

| n | K | α | V |
|---|---|---|---|
| 3 | 1 | — | 7.4049183473 |
| 4 | 1 | 1.397 | 5.78859314459 |
| 6 | 2 | 1.3716608546 | **5.0550504633** = 2+2√21/3 |
| ∞ | — | — | 4.6033388 |

## Recalled (durable memory, cross-run)

Durable memory holds the circle identity, the stewbasic general-n formula, the
David K square closed form, the Abel et al. model (unique critical speed in
locally rectifiable regions; exact values for disk/triangle/square but NO
hexagon value; ~10.9-approximation too coarse), and V_hexagon=5.05505046 —
all consistent with this run's files. **A durable-memory reflection explicitly
warns: sympy-vs-mpmath is not an independent route; report the hexagon value as
single-route unless a game-encoding solver (max over dash-landing point P of
runner-perimeter-dist(P)/swim-dist(P) at stage 1/V, or a David-K-style n=6
construction) is actually built and **its output captured**. That solver now
exists on disk and its output IS captured (`code/indep_game_encoding.py` +
`code/indep_game_encoding_OUTPUT.txt`) — but the run **failed** to reproduce the
oracles (it encodes the straight-dash red herring), so it closes nothing; see
Validation/Gaps. Treat the stewbasic n-gon formula as a sourced result with
strong numeric agreement (square + circle limit reproduced two ways, and
self-consistent exact closed form for n=6), not a peer-reviewed theorem.

## Provenance of V_hexagon — literature leaves n>4 OPEN (librarian finding)

**Source-backed caveat, added by the librarian after reading the Abel et al.
full text in full:** the paper's own **Open Problems** (item 4) states the
exact critical speed ratio for regular n-gons with **n>4 is an open
problem** — "Our pursuer strategies for equilateral triangle and square
generalize naturally, but we have been unable to find matching escaper
strategies, suggesting these may not be tight." So **no held primary source
independently derives V_hexagon**; Abel et al. and Hesterberg give exact
values only for disk (4.603), triangle (7.405) and square (5.789). **V_hexagon
= 2+2√21/3 ≈ 5.0550504633 rests solely on the stewbasic Math.SE formula
(n=6)**, whose n=3/4/∞ anchors reproduce the paper-oracle values and whose n=6
value reduces to an exact quadratic-surd closed form. When reporting the
answer, state it as **formula-derived + exact-closed-form-confirmed,
single-route**, with the note that the peer-adjacent literature explicitly
flags n>4 as open. Note: `research/notes/hexagon-provenance-literature-open.md`,
claim `abel-open-ngon-ngt4`.

## Contradictions

No open contradiction on the value (5.05505046). Two caveats to record, not
reconcile: (1) the run's earlier GOAL.md claims "verified by a second
independent route" — that is an **overclaim** (see Validation/Gaps). (2) **All
three "oracles" agree the *formula* is right** (n=3/4/∞ anchors + exact closed
form), but the **only independent game-encoding solver built does NOT reproduce
the oracles** — it caps each shape at a lower straight-dash bound. That is not a
contradiction of the answer (the solver's model is the known-wrong red herring)
but it means "independently verified" is NOT yet true. (3) **The published
literature leaves regular n-gons with n>4 open** (Abel et al. Open Problems
item 4), so the hexagon value is not confirmed by any peer-adjacent source —
see the provenance note above. The research/CLAIMS.md
mirror lists the circle identity claim as "unchecked" in its one `claim` block;
the notes and programs override it authoritatively.

## Gaps

**Directive 1 status — librarian's primary-source pass COMPLETE; symbolic_math's
`hexagon-first-principles` derivation is the one remaining in-flight item.**
`research/sources/` holds 8 full texts: lion-and-man (Bollobás–Leader–Walters
arXiv:0909.2524; Alexander–Bishop–Ghrist capture-unbounded), Tao's square-pool 6×
boy/teacher (Math.SE q.1555855 — the problem's ancestry, plus a numeric anchor:
6 > V_square ⇒ capture), the circle two-phase staging-dash (Math Factor "Princess
and Beast": staged semicircular arc of radius R/2v keeping opposite, then tangent
dash; ODE dr=√(v′²−r²)dt — an independent confirmation of the circle mechanism),
and Abel et al. "Escaping a Polygon" (arXiv v3 + Hesterberg MIT thesis 2018). New
claim blocks from these are in `research/CLAIMS.md` (lion-man-metric-space-both-win,
tao-square-pool-6x-capture, princess-beast-stage-arc-dash-ode, abg-capture-
unbounded). What they establish for THIS run: (a) the pool is locally rectifiable,
so Abel et al.'s unique-critical-speed well-posedness applies and the lion-man
both-win pathologies are ruled out; (b) the homothetic scaled safe-region +
boundary-time equalization mechanism is confirmed by Tao's inner-square and the
princess-beast staged arc; (c) **none gives a hexagon exact value** — the paper's
exact list is disk/triangle/square only. `research/notes/` has only the circle and
polygon-generalization notes, so `hexagon-first-principles.md` is still missing
(`code/hexagon_first_principles_explore.py` is an un-run first-principles
*implementation* — see Validation); when it lands it is the missing independent
route, until then the value stays
single-route (see Validation). The thread's "Next" (librarian downloads) is
superseded.

The value is computed and exact-closed-form-confirmed; formula-route only. The
one independent game-encoding solver that was actually built (`code/indep_game_encoding.py`)
has now been RUN and its output captured — and it FAILS (encodes the
straight-dash red herring: circle π+1, square 4.09, hexagon 3.98), so it must
NOT be cited as verification. What is missing: an independent route that does
the tangent-chord staging (circle's sin B=(π+B)/v) or a David-K-style n=6
construction reproducing at least the square and hexagon oracles. Until such a
route exists and its output is captured, report the hexagon answer 5.05505046
as formula-derived + exact-closed-form-confirmed but NOT independently
game-encoded. Files: `code/solution.py` (exact formula), `code/hexagon_closed_form.py`
& `code/confirm_hexagon_closedform.py` (exact closed form),
`code/indep_game_encoding.py` + `code/indep_game_encoding_OUTPUT.txt`
(independent solver, RUN — fails, dead end), `code/indep_sanity_circle.py`
(analytic proof that failure = the π+1 naive bound), `code/brute.py circle`
(reproduces circle oracle), `solution_hexagon_pattern.md` (the run's derivation
write-up — stands in for the `/workspace/solution.md` the brief calls for),
`GOAL.md`, `research/threads/hexagon-critical-speed.md`. **Un-run on disk**:
`code/hexagon_first_principles_explore.py` (correct-framework solver, circle
self-validation built in — the natural completion of the missing route) and
`code/hexagon_independent_solver.py` (straight-dash variant, red-herring
family).
