# Sgall — "Solution of David Gale's Lion and Man Problem"

Source: author's homepage, https://iuuk.mff.cuni.cz/~sgall/ps/lion.ps
(PostScript of the Dec 5, 2000 preprint). Published as J. Sgall,
*Theoretical Computer Science* 259(1-2):663–670, 2001,
DOI 10.1016/S0304-3975(00)00411-4. Full text:
`research/sources/sgall-solution-david-gales-lion-and-man.full.md`
(the .ps is raw PostScript; the paper's text is embedded and readable —
headers/font bitmaps dominate the byte count, not the prose).

## What the paper establishes (the discrete-time lion-and-man game)

**Setup (Gale's version, Problem 31 in Guy's "Unsolved problems in
combinatorial games", AMS Proc. Symp. Appl. Math. 43, 1991).** Time is
*discrete*, space continuous: man and lion move in the non-negative quadrant
of the plane. Each round the man moves ≤ 1 (Euclidean), then the lion moves
≤ 1. Lion wins if he moves to the man's current position; man wins if he can
keep escaping forever. If initially x'_0 ≥ x_0 or y'_0 ≥ y_0 (man coordinate
not strictly below lion's in both axes), the man escapes trivially by moving
away from the origin.

**Main theorem.** If x'_0 < x_0 and y'_0 < y_0 (both the man's coordinates
strictly smaller), then the lion **catches the man in a finite number of
moves**, bounded by

max{ (x_0 + y_0(α₀ + √(1+α₀²)))², (y_0 + x_0(α₀⁻¹ + √(1+α₀⁻²)))² } = O(x₀² + y₀² + x₀²α₀⁻² + y₀²α₀²),

where α₀ = (y₀ − y'_0)/(x₀ − x'_0) is the initial slope of the lion–man line.

**Lion's strategy (Fixed Center Lion Strategy, FCLS).** Choose once, at the
start, a point C on the line M₀L₀ beyond L₀ such that the circle centred at
C through L₀ intersects both coordinate axes (choose the closest such point
to the origin). Invariants per move: (i) M has both coordinates < L's;
(ii) L lies on segment MC; (iii) |CL|² grows by ≥ 1 each move (Lemma 1:
r'² ≥ r² + 1 unless the lion catches immediately). Since |CL|² grows by ≥ 1
per move and |CL₀|² is bounded by the initial data, the number of moves is
bounded (Theorem 2). Proof: with Y = foot of perpendicular from L to M'C
(and X chosen so |L'Y| = |XY|), triangle inequalities + Pythagoras give
r'² ≥ |XC|² = |XL|² + |LC|² ≥ r² + 1.

**Man's strategy / tightness.** The man keeps the product x'y' (area under
his position) large by moving perpendicular to the lion–man line; this gives
a survival time ≥ 2x'_0y'_0 for the naive strategy (loss ≤ α/(1+α²) ≤ 1/2 per
move), i.e. Θ(x²) on the diagonal. A refined multi-phase strategy (move to a
slope-α point x = αy, then the simple strategy, restarting phases as α
decays) shows the man can survive for Ω((x₀² + y₀² + x₀²α₀⁻² + y₀²α₀²)/α₀^ε)
moves for any ε > 0 — so the lion's upper bound is **almost optimal**
(Theorem 6). On the diagonal the gap is < 3+2√2 < 6; in the extreme case
(man at origin, lion at (x₀,1)) the capture time is Θ(x₀⁴) — matching
bounds. The exact optimal strategy remains open.

**Generalizations.** The strategy works in any wedge (angle < π) and in
higher dimensions (any convex cone): lion wins iff the halfplane of points
closer to M₀ than to L₀ has bounded intersection with the playing area;
otherwise the man escapes. Exponent of the capture bound does not increase
with dimension.

## Relation to this run

This is the **discrete-time** lion-and-man game, the primary source that the
run's other documents cite for "Sgall's solution to Gale's problem" (cited
by Klein–Suri AAai'11, Casini–Garulli, Bollobás–Leader–Walters, the MaRDI
entry). It does **not** bear on the continuous-time *critical speed* of the
runner/swimmer pool (PE 761): different model (equal speeds, alternating
turns, quadrant) and different question (number of moves to capture, not
speed threshold). It is background coverage of the subject's canon: it fixes
the exact statement and technique of a named result several of our sources
reference, and its "wedge/convex cone" generalization is the same
halfplane/geodesic comparison idea that underlies the boundary-time
equalization in the Abel et al. escape model.

```claim
id: sgall-discrete-lion-man-fixed-center-capture
statement: In Gale's discrete-time lion-and-man game on the non-negative quadrant (man and lion alternate moves of distance at most 1), if both coordinates of the man are strictly smaller than the lion's initially, the lion catches the man in finitely many moves by the Fixed Center strategy: fix C on line M0L0 beyond L0 with the circle through L0 centred at C intersecting both axes, maintain L on segment MC and |CL|^2 increasing by >= 1 per move; the capture time is O(x0^2 + y0^2 + x0^2/alpha0^2 + y0^2*alpha0^2) with alpha0 the initial slope, and this is almost optimal (man survives Omega(time/alpha0^eps) for any eps>0). The same strategy works in any wedge (< pi) and in any convex cone in higher dimensions.
hypotheses: discrete time, space continuous, equal maximum speed 1, man moves first, quadrant (or wedge/convex cone) playing area, lion captures by moving to the man's position.
holds-here: no - this is the discrete equal-speed game, not the continuous runner-with-speed-v vs swimmer-speed-1 boundary-escape game PE 761 models (Abel et al. well-posedness is the relevant result there). It fixes a named result our sources cite.
status: proved (peer-reviewed TCS 2001; author's preprint on disk).
bearing: canonical background; identifies the FCLS strategy later improved by Casini-Garulli's Moving Center Lion Strategy; not a route to V_hexagon.
anchor: research/sources/sgall-solution-david-gales-lion-and-man.full.md
```