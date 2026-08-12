# Polygon generalization of the runner–swimmer (goblin-in-pool) critical speed

**Question.** The circle case has V ≈ 4.6033 from cos B = 1/V, sin B = (π+B)/V.
How does this generalize to a regular n-gon pool (square, hexagon) where the
runner starts at an edge midpoint and V_square ≈ 5.78859314? The subtlety is that
on a polygon edge the runner's angular speed about the pool center is NOT
constant, so the circle's "matching radius / safe region / keep-opposite" idea
needs a structural replacement.

## The one-line structural answer

The circle's safe radius, "angular speed 1/ρ = v matches the runner" idea is
replaced, on a polygon, by an **inner region homothetic (scaled copy) of the
pool** whose *perimeter is v times smaller*: the swimmer creeps along this inner
boundary to get diametrically/centrally opposite the runner, then dashes.  The
critical speed comes from **equalizing the swimmer's straight escape time against
the runner's polygon-perimeter time to the exit point** — exactly the circle's
boundary-time comparison, but with the boundary genuinely the polygon edges
(piecewise-linear perimeter), not arc length.

There is a **fully explicit general-n formula** (Math.SE user *stewbasic*,
2017) that reproduces the square and gives a method for the hexagon, and an
**independent closed form for the square** (Math.SE user *David K*) that
reproduces the oracle 5.78859314 to 8 digits exactly.

## Result 1 — general-n formula (stewbasic, Math.SE q.1762665)

Let the pool be a regular n-gon, θ = π/n. Let K be the largest integer in
[0, n] such that

    sin(Kθ) − (K+n)·tanθ·cos(Kθ) < 0

Equivalently, K = floor(r) where r is the unique root in [1, n/2) of

    tan(r·θ) − (r + n)·tanθ = 0

Then (as a consequence of placement)

    cos((K+2)θ) ≤  2 sin(Kθ)/((K+n)tanθ) − cos(Kθ)  <  cos(Kθ)

so we may define

    α = ½( Kθ + arccos( 2 sin(Kθ)/((K+n)tanθ) − cos(Kθ) ) )

and the **critical speed ratio is λ = 1/cos(α)**.

- The inner (safe) region is obtained from the outer n-gon P by rotating by
  Kθ and scaling about the center by s = cos α / cos(α − Kθ). The student can
  win for speed < λ; the teacher wins for speed > λ.
- Square: n=4, K=1, α ≈ 1.397, λ ≈ 5.789 → **matches V_square ≈ 5.78859314**.
- Large n: θ small, n·tanθ ≈ π, so α ≈ Kθ ≈ μ where **tan μ = μ + π**, giving
  λ → 1/cos μ ≈ 4.6033 — *recovers the circular pool* (the Ponder-This B is
  μ−π... precisely the circle identity). This is the continuity check between
  polygon and circle.

Source: https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon (answer by stewbasic, Oct 2017).
Direct SE blocks scraping; fetched via
https://web.archive.org/web/2021/https://math.stackexchange.com/questions/1762665/...

## Result 2 — independent square closed form (David K, same thread)

For the square (side 2), the limiting speed ratio is exactly

    V_square = √( 5/2 · (7 + √41) )

Check: 5/2·(7+√41) = 5/2·13.403124 = 33.50781; √33.50781 = **5.78859314...**
— reproduces the oracle to 8 decimals.  Two totally different derivations
(stewbasic's general-n formula and David K's geometric construction in the
square) give the same value, which is a strong cross-check.

## Result 3 — the "inner octagon"/safe-shape discussion (what the safe region is)

For the square, sub-optimal safe regions give these speeds (from the same
thread), showing how the *shape* of the safe region controls the bound:

  inner shape | edge-center speed | corner speed | min needed
  ------------|-------------------|--------------|-----------
  inner square| 5.00              | 5.51         | 5.00
  diamond     | 5.41              | 5.25         | 5.25
  circle      | 5.27              | 5.41         | 5.27
  octagon     | 5.38              | 5.38         | 5.38
  homothetic / optimal (stewbasic/DavidK) | ... | ... | **5.7886**

Key mechanistic insight (TMM): the swimmer cannot force the *shape* of the safe
region to be a circle; it can only keep the center between itself and the
teacher while moving along the safe region's boundary.  When it leaves the safe
region to dash, the teacher is at maximum distance; the pool-side to run to is
the *mirrored* point, and the race is swimmer-line-time vs teacher-perimeter-
time. The optimal safe region is the *scaled pool*, not a circle, diamond, or
octagon.

## Result 4 — formal game-theoretic treatment (Abel, Akitaya, Demaine, Demaine, Hesterberg, Ku, Lynch)

"Escaping a Polygon", arXiv:2007.08965. This is the rigorous model: human
(swimmer) at speed 1 inside; zombie (runner) at speed r outside (or on a
"moat"); human escapes by reaching a boundary point a positive distance from
the zombie.  It proves:
- There is a **unique winner / unique critical speed ratio r\*** in any locally
  rectifiable region (the model is well-posed).
- **Exact r\* for the disk, equilateral triangle, and square** (the same square
  value as above).  It uses the APLO ("axially progressing laterally opposing")
  escaper strategy, which is exactly the staged "keep-opposite then dash"
  strategy, rigorously justified.
- For general simple polygons: 10.89898-approximation to r\* in polynomial time
  (formula r\* ≈ max over boundary pairs of d_z/d_h, the zombie-geodesic over
  human-geodesic distance), and a pseudopolynomial PTAS.  NP-hard in 3D.

Important caveat: the *runner as pursuer on the boundary* in the PE/statement
model matches the paper's **"moat model"** (pursuer constrained to the exterior),
not the free-plane model.  The exact square/disk thresholds in the paper agree
with both the naive and moat models' critical speeds for these symmetric
shapes.

Source: https://arxiv.org/abs/2007.08965 ; full text
https://arxiv.org/html/2007.08965

## Synthesis for this project (PE 761)

- The circle value 4.6033 and the polygon values are **all the same mechanism**:
  stage on the inner (scaled) safe region to get centrally opposite the runner,
  then dash, and equalize
      swimmer straight-line time to the exit  =  runner perimeter time to exit.
  For the n-gon, "perimeter time" means running *along the polygon edges*
  (piecewise-linear), which is why the runner's angular speed is non-constant:
  the agent keeps the *center on the line to the runner* while on the inner
  copy, where the perimeter-ratio (not angular-speed-ratio) is the right
  invariant.
- **Wanted: V_hexagon.** The general-n formula (Result 1) with n=6 is the
  direct route; it should be evaluated exactly (root-finding, not search).
  David K's square derivation gives an independent method for the hexagon, also
  to be cross-checked.

## Sources
- Math.SE q.1762665 "Can the boy escape the teacher for a regular n-gon?"
  (stewbasic general-n formula; David K square closed form; TMM, Jens safe-region
  analysis). Via Wayback: https://web.archive.org/web/20210506134248/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon
- Abel, Akitaya, E.Demaine, M.Demaine, Hesterberg, Ku, Lynch, "Escaping a
  Polygon", arXiv:2007.08965. https://arxiv.org/abs/2007.08965
- IBM Ponder This May 2001 (circle identity, already in library):
  https://research.ibm.com/blog/ponder-this-may-2001

## Caveats / thin spots
- stewbasic's final formula is stated on Math.SE without a full published
  proof in a peer-reviewed venue; treat it as a sourced result with strong
  numeric agreement (square 5.78859314 reproduced two independent ways, circle
  limit recovered) but not a peer-reviewed theorem.
- "Escaping a Polygon" proves exact square/disk but its *hexagon* value, if any,
  is not highlighted in the abstract; the stewbasic formula is the direct way
  to get V_hexagon.
