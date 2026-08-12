# Shared context

Problem: Project Euler **761** — runner/swimmer pursuit-evasion on a regular
n-gon pool (swimmer at center speed ≤1, runner on boundary at edge-midpoint
speed ≤v). State of the run: **hexagon value computed to 8 dp via a validated
formula and reduced to an exact closed form; the independent game-encoding
solver is written (`code/indep_game_encoding.py`) but its run output is NOT
captured — do not report as independently verified.** Full
statement: `/workspace/problem.md`.

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

**Hexagon: the independent route EXISTS on disk but is NOT yet confirmed.**
`solution.py` (mpmath), `verify_hexagon.py` (sympy), `hex_check.py` (math) all
implement the SAME stewbasic formula at different precisions — one route; do
NOT call that independent verification. The genuinely independent geometry-first
solver exists at **`code/indep_game_encoding.py`** (bisects on v solving
g(v)=v, g = max over boundary point Q of runner-perimeter-dist(Q)/swim-dist(Q)
at stage radius 1/v, decoding the circle/square/hexagon oracles itself WITHOUT
the K/α formula). **Its run output is not captured anywhere — scratch stops at
"agent-run-15 still running"; no final value in memory or docs; not in
code/INDEX.md unless refreshed.** What tool_builder should do, and the only
thing that closes the gap: run `python code/indep_game_encoding.py` and confirm
it reproduces 4.60333885 (circle), 5.78859314 (square), and 5.05505046
(hexagon). What IS already independent of the decimal arithmetic is the exact
closed form V=2+2√21/3 above (full-precision confirmation), but that still
subsumes the formula's correctness. Honest status: **value = single (formula)
route, numerically + exact-closed-form confirmed; independent game-encoding
solver present but its result unconfirmed.** Thread
`research/threads/hexagon-critical-speed.md` and reflection memory flag this.

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
construction) is actually built.** Treat the stewbasic n-gon formula as a
sourced result with strong numeric agreement (square + circle limit reproduced
two ways, and self-consistent exact closed form for n=6), not a peer-reviewed
theorem.

## Contradictions

None on the value. But note: the run's earlier GOAL.md claims "verified by a
second independent route" — that is an **overclaim** (see Validation). The
mirror in research/CLAIMS.md lists the circle identity claim as "unchecked" in
its one `claim` block; the notes and programs override it authoritatively.

## Gaps

The value is computed and exact-closed-form-confirmed. The one honest gap: the
**independent game-encoding solver's result is not captured** — `code/indep_game_encoding.py`
exists (bisection fixed-point g(v)=v, decodes all three oracles, no K/α
formula) but the scratch record stops at "agent-run-15 still running" and no
output is in memory, docs, or a file. Next step: run it, record
circle/square/hexagon agreement, then mark the value independently verified.
If a final report is due before that, it should state 5.05505046, cite the
stewbasic formula + arXiv paper, give the exact closed form 2+2√21/3, and
report the hexagon as formula-derived + exact-closed-form-confirmed but NOT
yet cross-checked by the captured independent game-encoding run. Files:
`code/solution.py` (exact formula), `code/hexagon_closed_form.py` &
`code/confirm_hexagon_closedform.py` (exact closed form), `code/indep_game_encoding.py`
(independent solver, unrun), `code/brute.py circle` (reproduces circle oracle),
`GOAL.md`, `research/threads/hexagon-critical-speed.md`.
