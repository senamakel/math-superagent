# Thread: hexagon critical speed (PE 761 answer)

## Question
What is V_hexagon, the critical runner speed for a *regular hexagon* pool, to
8 decimals? The circle (4.60333885) and square (5.78859314) oracle values are
established; the hexagon is the actual PE 761 answer.

## What it rests on
- `stewbasic-regular-ngon-cutoff`: the general-n formula λ = 1/cos(α). For n=6
  this evaluates to V_hexagon = 2 + 2√21/3 ≈ 5.05505046 — exact closed form
  confirmed by two programs (`code/hexagon_closed_form.py`,
  `code/confirm_hexagon_closedform.py`).
- `davidk-square-closed-form`: formula validated on square (5.78859314 two
  independent ways), giving confidence in the general-n formula's correctness.
- `escaping-polygon-wellposed-exact-square-disk` (+ `abel-open-ngon-ngt4`):
  rigorous model confirms the mechanism but has NO hexagon exact value, and
  explicitly leaves n>4 OPEN in the literature.

## Status — value settled, independence gap open

**V_hexagon = 5.05505046330389… = 2 + 2√21/3 — single route (formula).**
The exact closed form is confirmed and self-consistent; but no *independent,
correct* game model reproduces it yet.

### Workstream A: librarian — primary-source research pass: COMPLETE
`research/sources/` and the digested claims now cover lion-and-man (Bollobás–
Leader–Walters, ABG, Sgall, Abrahamsen), the swimmer-circle two-phase (Quanta,
Ponder-This, Hesterberg, Lady-in-the-Lake, princess-beast, spirograph,
OEIS A328227), the n-gon boy/teacher (Math.SE stewbasic/David K, Abel et al.,
Hesterberg thesis), and perimeter-differential-games (Shishika–Kumar, Mora).
Net: heavy corroboration of the circle MECHANISM and V_circle, and of the
model; **none gives a hexagon value** — the literature leaves n>4 open.

### Workstream B: symbolic_math — independent first-principles hexagon derivation
Still the missing route. `research/notes/hexagon-first-principles.md` does not
exist; `code/hexagon_first_principles_explore.py` was never run (empty
captured output). The `david-k-hexagon-construction` approach (synthetic
equal-time geometry, exact quadratic-surd target) is the planned execution.
The one independent game-encoding solver built (`code/indep_game_encoding.py`)
encodes the straight-dash red herring and FAILS the oracles — do not re-run.

## Next
- Build the David-K-style hexagon equal-time construction (exact target 2+2√21/3
  already known; verify 9V⁴−240V²+256's positive root) and CAPTURE its output —
  that is the missing second route.
- When it lands: curator confirms agreement with 5.05505046, updates CONTEXT.md,
  closes the thread.

```thread
question: What is V_hexagon to 8 decimals (PE 761 answer)?
status: candidate 5.05505046 from stewbasic n=6 formula, exact closed form 2+2sqrt21/3 confirmed; value single-route (no correct independent model yet reproduces the oracles)
rests-on: stewbasic-regular-ngon-cutoff, davidk-square-closed-form, escaping-polygon-wellposed-exact-square-disk, abel-open-ngon-ngt4
workstreams: (A) librarian pass COMPLETE — sources corroborate circle mechanism + literature leaves n>4 open; (B) David-K hexagon construction still the missing independent route
blocked-by: no independent correct game model; indep_game_encoding.py is the documented red-herring dead end
next: build + capture David-K hexagonal equal-time construction, then curator verifies and closes
```
