# Thread: hexagon critical speed (PE 761 answer)

## Question
What is V_hexagon, the critical runner speed for a *regular hexagon* pool, to
8 decimals? The circle (4.60333885) and square (5.78859314) oracle values are
established; the hexagon is the actual PE 761 answer.

## What it rests on
- `stewbasic-regular-ngon-cutoff`: the general-n formula λ = 1/cos(α). For n=6
  this evaluates to an exact closed form:
    K=2, θ=π/6,  α = ½(π/3 + arccos(−1/8)) ≈ 1.3716609 rad,
    λ = 1/cos(α) ≈ 5.0551 (hand-derived; between circle 4.6033 and square 5.7886).
- `davidk-square-closed-form`: formula validated on square (5.78859314 two
  independent ways), giving confidence in the general-n formula's correctness.
- `escaping-polygon-wellposed-exact-square-disk`: rigorous model confirms the
  mechanism but has NO hexagon exact value.

## Status
Candidate V_hexagon ≈ 5.0551 from the stewbasic formula — **single route, not
yet verified**. Abelian paper offers no hexagon value; the ~10.9-approximation
is too coarse for 8 decimals.

## Blocked by
- Need a SECOND independent route to V_hexagon (GOAL completion criterion 3).
  Options: (a) a numerical solver directly encoding the polygon boundary-time
  equalization (brute-force over dash landings, not over the bound), (b)
  David-K-style geometric construction specialized to the hexagon. Must agree
  with the stewbasic n=6 value to 8 dp.

## Next
- Get exact high-precision λ_hexagon from `code/polygon_critical.py`/`solution.py`
  (n=6, K=2, α=½(π/3+arccos(−1/8))).
- Build an independent numeric check (option a) and compare to 8 dp.
- Confirm the PE 761 start condition (edge midpoint) is covered by the formula
  ("regardless of starting position" per stewbasic).

```thread
question: What is V_hexagon to 8 decimals (PE 761 answer)?
status: candidate 5.0551 from stewbasic n=6 formula; single-route, unverified
rests-on: stewbasic-regular-ngon-cutoff, davidk-square-closed-form, escaping-polygon-wellposed-exact-square-disk
blocked-by: no independent route to V_hexagon yet
next: exact high-precision value, then independent numerical cross-check
```
