# OEIS lookup: the Paley(9)-pattern configuration-count sequence is not catalogued

The per-vertex Paley(9)-pattern configuration count over the five feasible
srg(v,k,1,2) members — the number of pairs of matching edges in a
neighbourhood, `C(k/2, 2) = k(k−2)/8`:

`[1, 21, 55, 1540, 123256]`  (k = 4, 14, 22, 112, 994)

was looked up in OEIS (round 27 pattern-finder) and returned **no match**.

The list is closed-form (`k(k−2)/8`), cross-checked against the measured
value on BvLS (243 × 55 = 13365 configurations, all verified to be induced
Paley(9), `code/out/paley9_pattern_check_fixed.captured.txt`) and against the
hypothetical 99 member (99 × 21 = 2079). No OEIS match confirms no external
closed form will surface. Recorded so nobody looks it up again.

Distinct from the two misses already recorded in
`oeis-miss-n3cap-and-triangle-counts.md` and `oeis-miss-family-vertex-counts.md`.