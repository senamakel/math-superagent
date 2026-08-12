# Math.SE q.1762665 — Can the boy escape the teacher for a regular n-gon?

Source: https://math.stackexchange.com/questions/1762665 (via Wayback). Full text:
`research/sources/mathse-boy-escape-teacher-regular-ngon.full.md` → [[mathse-boy-escape-teacher-regular-ngon.full]]

Setup: boy at centre of regular n-gon (side 2), teacher on the edge at speed v
times the boy (teacher stays on the edge). Boy escapes by reaching an edge
point the teacher is not at. This is exactly PE 761's polygon model (swimmer
at centre, runner on boundary). Starting position here is a *vertex*; PE 761
uses an edge midpoint — both covered by the general formula below.

## stewbasic's general-n exact formula (answer, Oct 2017) — the load-bearing result

Let θ = π/n. Let K be the largest integer in [0,n] such that
    sin(Kθ) − (K+n)·tanθ·cos(Kθ) < 0.
Equivalently K = floor(r), r the unique root in [1, n/2) of tan(xθ) − (x+n)tanθ = 0.
Then define
    α = ½( Kθ + arccos( 2 sin(Kθ)/((K+n)tanθ) − cos(Kθ) ) ),
cutoff speed λ = 1/cos(α). For speeds < λ the boy wins; > λ the teacher wins.
The safe (inner) region Q is the outer n-gon rotated by Kθ and scaled by
s = cos α / cos(α − Kθ) about the centre.

- Square n=4: K=1, α≈1.397, λ≈5.789.
- Large-n consistency: θ→0, n·tanθ→π, α≈Kθ→μ with tan μ = μ+π, λ→1/cos μ ≈ 4.6033,
  recovering the circular pool's value (Ponder-This B). *Minor note slip:* the
  limiting μ is precisely the circle's B (=1.3518), not π−B as the run's note
  parenthetically wrote; the limiting value 4.6033 is unchanged and correct.

## David K's independent square closed form (Aug 2017)

    V_square = √( 5/2 · (7 + √41) ) = 5.78859314…
This is geometrically derived (teacher runs to edge centre, boy swims up the
axis, then both turn; τ=0 at the limit d2 = v·d1). Independent of stewbasic's
formula — a genuine second route to 5.78859314, matching the PE oracle to 8 dp.

## TMM / Jens — why naive safe regions are suboptimal (mechanism)

Safe-region choices give lower bounds on v (not the true value):
  inner square 5.00 | diamond 5.25 | circle 5.27 | octagon 5.38, versus the
  optimal homothetic (scaled-pool) value 5.7886. Mechanism: the boy can only
  keep the centre on the line to the teacher while creeping along the *inner
  region's boundary*; he cannot force the region's shape. The optimal safe
  region is the scaled pool, not a circle/diamond/octagon. This confirms the
  run's structural principle (stage opposite, then dash; equalize swimmer line
  time vs runner perimeter time).

```claim
id: stewbasic-regular-ngon-cutoff
statement: For a regular n-gon pool, the critical speed ratio is lambda = 1/cos(alpha) with theta=pi/n, K = largest integer with sin(K*theta) - (K+n)tan(theta)cos(K*theta) < 0, alpha = 1/2(K*theta + arccos(2 sin(K*theta)/((K+n)tan(theta)) - cos(K*theta))). For n=4 this gives 5.7886; n=6 gives lambda = 1/cos(1/2(pi/3 + arccos(-1/8))) = 2 + 2*sqrt21/3 ~ 5.05505046 (hexagon, the PE 761 answer) [earlier draft wrote 5.0549; that digit was a slip — the exact V^2 = (40+8sqrt21)/3, V = 5.0550504633].
hypotheses: regular n-gon, boy at centre, teacher constrained to boundary moving at speed v; escape = reach a boundary point the teacher is not at; theta=pi/n.
holds-here: yes — identical structure to PE 761 (swimmer centre, runner boundary); hexagon is n=6.
status: asserted (Math.SE answer, not peer-reviewed) but strong numeric agreement: reproduces square oracle 5.78859314 two independent ways, recovers circle limit 4.6033.
bearing: gives V_hexagon = 1/cos(1/2(pi/3+arccos(-1/8))) ~ 5.0549; the direct exact route to the answer. n=6 value is SINGLE-ROUTE (no independent hexagon source) so needs a second verification.
anchor: research/sources/mathse-boy-escape-teacher-regular-ngon.full.md
```

```claim
id: davidk-square-closed-form
statement: V_square = sqrt(5/2(7+sqrt(41))) = 5.78859314..., reproduced by an independent geometric construction (David K) and by stewbasic's general-n formula.
hypotheses: square pool side 2, boy at centre, teacher on boundary; limiting speed ratio where tau=0.
holds-here: yes — matches PE oracle V_square = 5.78859314 to 8 dp.
status: derived (two independent routes agree) — solid cross-check for the square.
bearing: validates the general-n formula by confirming the square case exactly, giving confidence the same formula for n=6 yields the hexagon answer.
anchor: research/sources/mathse-boy-escape-teacher-regular-ngon.full.md
```

## What it does NOT settle
- stewbasic's formula is not published in a peer-reviewed venue; treat the
  square agreement (two routes) as the evidence, and the hexagon value as
  needing its own independent check.
- The problem's statement has the runner start at an edge *midpoint* (PE 761);
  this thread mostly analyses vertex starts, but the general formula covers
  "regardless of starting position" per stewbasic.
