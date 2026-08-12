<!-- source: https://oeis.org/A120011 | converted from HTML -->

# A120011 — decimal expansion of sqrt(3)/4 = 0.4330127…

**This entry is NOT related to the runner/swimmer critical speed.** The previous
title ("critical speed constant") was a mislabel: A120011 is the *area of an
equilateral triangle of side 1*, sqrt(3)/4 ≈ 0.43301270, with minimal polynomial
16x²−3. It entered this run's frontier only as a cross-reference from A057357
(floor(3n/7)), which itself matched the K(n) sequence of the stewbasic formula
for small n by coincidence (see `code/pattern_findings.md` and CONTEXT.md:
"OEIS small-term matches (A057357) are coincidences" — the match breaks at
n=86, and floor(3n/7) ≠ K(n) exactly).

## Why this record exists
Kept on disk so nobody re-downloads it or re-derives the (false) connection.
The genuinely critical constants are the decimal expansions of the critical
speeds themselves:

- V_circle ≈ 4.60333884875170035 (root of cos B = 1/V, sin B = (π+B)/V, i.e.
  tan B = π+B; see `research/notes/circle-critical-speed-identity.md`).
- V_square ≈ 5.788593144591252 (independent David K construction and
  stewbasic's formula; `research/summaries/mathse-boy-escape-teacher-regular-ngon.md`).
- V_hexagon ≈ 5.055050463303893 = 2 + 2√21/3 (PE 761 target; run's own
  derivation, `code/hexagon_closed_form.py`).

Whether OEIS catalogues these decimal expansions is checked separately
(oeis.org/search by decimal prefix); if found, those records fix the standard
names and cross-references for the constants themselves.