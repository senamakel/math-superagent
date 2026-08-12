# Shared context

Problem: Project Euler **761** — runner/swimmer pursuit-evasion on a regular
n-gon pool (swimmer at center speed ≤1, runner on boundary at edge-midpoint
speed ≤v). State of the run: **hexagon value computed to 8 dp via a validated
formula and reduced to an exact closed form; an independent game-encoding check
is still NOT built — do not report it as independently verified.** Full
statement: `/workspace/problem.md`.

## The answer

**V_hexagon = 5.05505046330389… → 5.05505046** (8 dp). For n=6: K=2,
α = ½(π/3 + arccos(−1/8)) ≈ 1.3716609546, V = 1/cos(α).

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

**Hexagon: NO independent game-encoding route exists yet.** `solution.py`
(mpmath), `verify_hexagon.py` (sympy), and `hex_check.py` (math) all implement
the SAME stewbasic formula at different precisions — same derivation, one
route. Do NOT call that independent verification. What IS independent of the
decimal arithmetic is the exact closed form V=2+2√21/3 above (full-precision
confirmation), but it still subsumes the formula's correctness. Honest status:
**value = single (formula) route, numerically confirmed, exact-closed-form
confirmed; not yet checked by an independent game-encoding solver.** The
thread `research/threads/hexagon-critical-speed.md` and the reflection memory
both flag this.

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

## Numbers / anchors (cheap to restate, expensive to recompute)

| n | K | α | V |
|---|---|---|---|
| 3 | 1 | — | 7.4049183473 |
| 4 | 1 | 1.397 | 5.78859314459 |
| 6 | 2 | 1.3716609546 | **5.0550504633** = 2+2√21/3 |
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

The value is computed and exact-closed-form-confirmed. The one honest gap: an
**independent game-encoding solver** for the hexagon (the thread's listed
"blocked by"). If a final report is still due it should state 5.05505046, cite
the stewbasic formula + arXiv paper, give the exact closed form 2+2√21/3, and
report the hexagon as formula-derived + exact-closed-form-confirmed but NOT
yet cross-checked by an independent game-encoding route. Files: `code/solution.py`
(exact formula), `code/hexagon_closed_form.py` & `code/confirm_hexagon_closedform.py`
(exact closed form), `code/brute.py circle` (reproduces circle oracle),
`GOAL.md`, `research/threads/hexagon-critical-speed.md`.
