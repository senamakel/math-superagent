# "Complete Solution of the Lady in the Lake Scenario" — AFRL/SciTech 2024 (arXiv:2401.14994)

Source: https://arxiv.org/pdf/2401.14994 (arXiv:2401.14994), also https://doi.org/10.2514/6.2024-2158.
Full text: `research/sources/lady-in-the-lake-complete-solution.full.md`.

## What the source establishes

This is a modern (2024, AFRL) **zero-sum differential-games** treatment of the classic "Lady in the Lake" escape problem — the exact circle-pool ancestor of PE 761. Setup: an agent L (the "lady"/swimmer) starts inside the unit circle at the center and wishes to reach the perimeter with finite angular separation from M (a "monster"/runner) constrained to move along the perimeter. Same structure as PE 761's circle case.

- **Prior art (canonical solution).** The game under the "keep diametrically opposite, then dash to the shore" strategy was previously known; but for a large portion of the state space the canonical solution does not yield a unique equilibrium strategy (L vs M heading ambiguities).
- **New contribution.** The paper solves an **auxiliary zero-sum differential game**: L seeks the *antipodal point* (the radius at which L's and M's maximum angular speeds are equal, i.e. radius r = 1/v for M's speed v), minimizing time to reach it while M maximizes that time. The solution's equilibrium is composed of a **Focal Line (FL)**, a **Universal Line (UL)**, and their tributaries — explicit equilibrium headings for L and controls for M at every state (Lemmas 1–8, Theorem 1 with the Value function).
- **Result.** The equilibrium Value is the game's unique solution; along the FL tributaries L's optimal path is a **straight line in the global frame** that enters the FL tangentially (Lemmas 3–4) — the same straight-dash-to-opposite-point structure the two-phase circle strategy uses, now rigorously derived as the differential game's saddle point rather than taken as a heuristic.
- **Connection to the circle critical speed.** The critical threshold is the speed ratio at which the antipodal-staging radius equals the radius at which angular speeds match: v\* satisfies the known identity (the same tan B = π + B / cos B = 1/v\* form as V_circle ≈ 4.60333885 in the Ponder-This, Hesterberg and stewbasic treatments). The paper's differential-game derivation independently confirms this is the **equilibrium** of the continuous game, not just a symmetric-strategy artifact.

## Why it matters for this run

It is a **rigorous, modern, peer-venue differential-games confirmation** of the circle two-phase mechanism that the run's polygon treatment generalizes. It corroborates:
- the existence and uniqueness of the critical threshold (matching Abel et al.'s well-posedness and Hesterberg's circle theorem from a totally different method — Isaacs-type HJI rather than combinatorial/geometric);
- the "stage at the antipodal radius, then straight dash" structure as the actual saddle-point equilibrium, which is the template behind the polygon's homothetic inner region and the stewbasic formula.

**Caveats:**
- It treats the **circle only** — no square/hexagon/general-n value, so like Abel et al. and Hesterberg it is corroborating theory for the *model* and the *circle anchor*, not a source of V_hexagon.
- Its "radius at which angular speeds are equal" staging is the circle analogue of the polygon's homothetic inner region; the polygon case's nonconstant runner angular speed (edges vs vertices) is the reason the safe region there is a scaled copy, not a disk — a distinction this circle paper does not address.

```claim
id: lady-in-the-lake-differential-game-equilibrium
statement: The Lady-in-the-Lake escape game (swimmer L at center of unit circle speed 1, boundary runner M speed v, escape = reach perimeter with finite angular separation) has as its unique zero-sum differential-game equilibrium the two-phase strategy: L first minimizes time to the antipodal staging radius (where angular speeds match, r = 1/v), then dashes on a straight line; the equilibrium is composed of a Focal Line and a Universal Line and their tributaries; the critical speed ratio v* satisfies the standard circle identity (cos B = 1/v*, sin B = (pi+B)/v*) giving v* ~ 4.60333885.
hypotheses: unit circle, L starts at center, M constrained to the perimeter, zero-sum separable objective (terminal angular separation maximized/minimized), full information, optimal play.
holds-here: yes for the circle case - this is the differential-game derivation of V_circle = 4.60333885, the run's circle anchor and the n→∞ limit of the polygon formula; does NOT treat polygons, so no hexagon value.
status: proved (arXiv:2401.14994, Theorem 1 + Lemmas; AFRL SciTech 2024 paper).
bearing: independent modern differential-game corroboration of the circle critical speed and the keep-opposite-then-dash equilibrium structure that the polygon formula generalizes; no hexagon value.
anchor: research/sources/lady-in-the-lake-complete-solution.full.md
```

## What it does not settle
- No polygon / regular n-gon / hexagon value (circle only).
- The HJI derivation is for the circular perimeter; the polygon's edge/vertex angular-speed variation is outside its model.