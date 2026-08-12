# Quanta — "Math Can, in Theory, Help You Escape a Hungry Bear" (Aug 2021)

Source: https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/
Full text: `research/sources/quanta-escape-hungry-bear-pond.full.md` → [[quanta-escape-hungry-bear-pond.full]]
(Pradeep Mutalik, Quanta Insights; a Martin-Gardner-1965-derived popular treatment.)

## What it establishes (the circle two-phase mechanism, independently worked)

Setup = exactly PE 761's circle case (swimmer at centre speed 1, bear on
circumference at speed ratio v; here radius R and v set equal, R = v = 3.5).
Salient, source-stated results:

- **Naive straight dash to the opposite shore caps at v = π+1 ≈ 4.14**: "the
  simple strategy ... fails for the case where the lake's radius and the speed
  ratio ... exceed π + 1 (~4.14)" (Bonus 1). This is exactly the run's
  documented **straight-dash red herring** — corroborated from a popular
  source.
- **Squirrel strategy (keep diametrically opposite) is optimal on the staging
  leg.** The swimmer traces a **semicircle** of radius R/2v (here 0.5), centre
  (0,−0.5), keeping opposite the bear, "impervious to a reversal of direction"
  — i.e. it maximizes angular separation for free. It ends at the **safe circle
  of radius R/v = 1/v** (here 1), where the swimmer's and bear's *angular*
  speeds match (segment OP = 1 in the diagram). This is precisely the
  `stage at radius 1/v diametrically opposite` structure of the circle identity
  (cos B = 1/V) held in memory.
- **Final dash** is a straight line from the safe circle, at an offset angle
  B; the critical condition "final distance between bear and swimmer set to
  zero" solved numerically gives **v = 4.6033** (Bonus 2), with
  √(4.6033²−1) = 4.4934 (= A115365 root of tan x = x), cos⁻¹(1/4.6033)=1.3518
  (= B), and π + 1.3518 = 4.4934 — the exact tan B = π + B / sin B = (π+B)/V
  relation. Confirms V_circle ≈ 4.60333885.
- The **arc-tangent** optimal-dash detail (escape *fastest*, not at critical
  ratio) is not relevant to the critical-speed value but confirms the
  tangent-chord (not radial) dash is the right escape geometry.

%% == NOTE == %%
This is a popular exposition, not a proof venue; treat as corroboration of the
circle mechanism and the π+1 bound, not as the primary derivation.

```claim
id: quanta-circle-two-phase-red-herring
statement: In the circular-pool run/swim game (swimmer at centre speed 1, runner on the rim at speed ratio v), the naive straight dash to the diametrically-opposite shore point caps at v = pi+1 ~ 4.14 (fails above it); the optimal escape is to stage on a semicircle of radius R/2v keeping diametrically opposite (swimmer traces a semicircle, ending on the safe circle of radius 1/v where swimmer and runner angular speeds match), then make a straight dash at offset angle B; setting the swimmer's final lead to zero yields v = 4.6033 with cos(B)=1/v, sin(B)=(pi+B)/v, i.e. tan B = pi+B.
hypotheses: unit-circle pool, swimmer at centre speed 1, runner on the circumference at speed factor v, optimal play, escape = reach a shore point before the runner.
holds-here: yes — this is the run's circle anchor V_circle = 4.60333885, the n->infinity limit of the polygon formula; corroborates the two-phase staging-dash mechanism and independently reproduces the pi+1 red-herring bound already documented in CONTEXT.md.
status: asserted (popular Quanta exposition; the identities match the held Ponder-This/Hesterberg/lady-in-the-lake/OEIS-A328227 derivations).
bearing: popular-source independent corroboration of the circle mechanism, the red-herring bound, and V_circle; does not give a hexagon value.
anchor: research/sources/quanta-escape-hungry-bear-pond.full.md
contradicts: nothing held (agrees with the run's circle model and red-herring note)
```
