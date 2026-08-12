# Math Factor Podcast — "Follow Up: Escaping the Beast" (optimal escape path derivation)

Source: The Math Factor Podcast (Chaim Goodman-Strauss / Kyle), "Follow Up: Escaping the
Beast", 2007-10. URL:
`https://strauss.hosted.uark.edu/mathfactor_site/mathfactor.uark.edu/2007/10/follow-up-escaping-the-beast/`.
Full text: `research/sources/mathfactor-princess-beast-optimal-escape.full.md`.

## What it establishes

A rigorous analytic derivation of the *optimal* escape strategy for the circular lake
("princess and beast") problem — the same two-phase structure PE 761's circle case uses.

**Key derivation (scale lake radius = 1, beast speed = 1, princess speed = 1/4).**
- If the princess stays at radius r from center keeping the beast diametrically opposite,
  over a small interval Δt the beast travels Δt along the shore while she must cover only
  r·Δt tangentially to stay opposite; the remaining motion can increase her radius.
- Pythagorean relation in the limit gives the radial ODE:
  **dr = √( (1/4)² − r² ) dt**, integrating with r(0)=0 to **r(t) = (1/4)·sin(t)**.
- The optimal strategy is: swim a **half-circle of radius 1/8 the lake** keeping opposite
  the beast, then **dash straight to the edge**. This is a "string-taught" path from the
  center to the shore — a curved (staging) segment followed by a straight tangent dash.
- Transition from the staged arc to the straight dash, and the landing point, are chosen by
  the geometric equalization of the beast's shore-arc time vs the princess's dash time.

## Why it matters for this run

- It is the **circle analogue** of exactly the two-phase "stage opposite, then tangent
  dash" mechanism that PE 761's circle oracle and the general n-gon (stewbasic formula)
  rest on: the stage region is a *homothetic* scaled copy (a semicircular arc of radius
  R/2v here), and the escape is a straight chord dash to a shore point offset by angle B.
- It independently confirms the staging-arc radius R/2v and the tangent-dash geometry that
  the run's `code/explore_general_dash.py` and the Ponder-This circle solution use.
- The ODE dr = √(v'²−r²)dt is precisely the radial-speed relation for a swimmer emerging
  outward while keeping the pursuer opposite — the same relation that fixes the polygon
  safe-region boundary.

## What it does NOT settle
- Only the circular case; no n-gon / hexagon value.
- A fixed speed ratio (1/4 in this telling); the *critical* ratio V ≈ 4.6033 and the
  general B-offset conditions (cos B = 1/V, sin B = (π+B)/V) are not derived here, though
  the geometry is the same.

## Claims

```claim
id: princess-beast-stage-arc-dash-ode
statement: For the circular lake pursuit, an optimal escape is to swim a semicircular arc of radius R/2v keeping diametrically opposite the pursuer (radial ODE dr = sqrt((R/2v)^2 - r^2) dt, r(t) = (R/2v) sin(vt)), then dash straight to the shore — a string-taught curved-to-straight path.
hypotheses: circle of radius R, pursuer on boundary at speed v, escapee starts at center at speed 1/2v in the fixed-ratio telling.
holds-here: yes as the circle mechanism — the same two-phase staging-then-dash structure that generalizes to the regular n-gon (stewbasic) and underpins PE 761's circle oracle V≈4.6033.
status: derived (analytic/geometric argument in a podcast exposition, not peer-reviewed).
bearing: confirms the structural principle (stager arc opposite the runner, then straight dash) that fixes the critical speed ratio; validates the run's reading of the circle geometry.
anchor: research/sources/mathfactor-princess-beast-optimal-escape.full.md
```
