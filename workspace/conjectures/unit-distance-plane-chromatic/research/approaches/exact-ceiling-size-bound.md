# Exact-ceiling size bound — the analytical N=11 theorem and the precise N=12 condition

```approach
idea: Prove the size bound "every 5-chromatic unit-distance graph has at least 12 vertices" analytically, by crossing the Kostochka–Yancey 5-critical edge lower bound against the EXACT unit-distance ceiling u(n) = A186705 (known exactly for n ≤ 21), instead of the asymptotic Spencer–Szemerédi–Trotter bound. This is an independent theorem route to the run's already-verified census N=11, and it pins the exact condition N=12 would require.
mechanism: >
  (1) A 5-chromatic UDG H on n vertices contains a 5-critical subgraph H′ which
      is again a UDG (induced subgraphs of a UDG are UDGs), on n′ ≤ n vertices.
  (2) Kostochka–Yancey (2014): every 5-critical graph satisfies
      |E(H′)| ≥ (9n′−5)/4.
  (3) H′ is a UDG on n′ points, so |E(H′)| ≤ u(n′), where u(n) is the exact
      maximum number of unit distances (A186705: exact for n ≤ 14 by Schade,
      for n ≤ 21 by Alexeev–Mixon–Parshall 2024).
  (4) So (9n′−5)/4 ≤ u(n′) is necessary. The exact crossing is
      (9n−5)/4 > u(n) ⟺ n ≤ 11, since u(11) = 23 < 47/2 = 23.5 while
      u(12) = 27 > 103/4 = 25.75. Hence no 5-critical UDG has ≤ 11 vertices,
      so no 5-chromatic UDG has ≤ 11 vertices: N = 11, analytically and
      independently of the census.
  (5) The N=12 barrier is exact. A 5-critical edge bound |E| ≥ c·n − 5/4
      contradicts u(12) = 27 iff c·12 − 5/4 > 27, i.e. c > 113/48 ≈ 2.3542.
      Kostochka–Yancey's slope 9/4 = 2.25 falls short by ε* = 5/48 ≈ 0.1042.
      The known triangle-free (K4-free) refinement
      |E| ≥ (9/4+ε)n − 5/4 − δ·T(G) has ε an asymptotic existence constant,
      not explicit, so it cannot be asserted to beat 5/48. N=12 is therefore
      out of analytical reach today.
  (6) The concrete route to N=12 is the census extended with a sound degree cap
      the current kernel does not use: kissing number in the plane is 6, so
      every UDG has maximum degree ≤ 6, and a 5-critical UDG has all degrees in
      {4,5,6}. This shrinks the enumeration from `geng 12 -d4` (all
      min-degree-4 graphs) to `geng 12 -d4 -D6` — a necessary-condition
      tightening that is free and provably sound.
status: adopted
first-step: >
  Write code/lib/exact_ceiling_cross.py: (i) read the exact A186705 terms for
  n = 1..21; (ii) evaluate the crossing (9n−5)/4 > u(n) in exact rationals and
  report the largest N with a contradiction (expected N = 11); (iii) compute the
  exact slope threshold c*(n) = (u(n) + 5/4)/n and the gap ε*(n) = c*(n) − 9/4
  for n = 12..21 (expected ε*(12) = 5/48); (iv) capture output to
  code/out/exact_ceiling_cross.captured.txt. This closes the analytical N=11 as a
  checked claim and hands tool_builder the exact ε table for the N=12 census
  decision.
precedent: grounded — Kostochka–Yancey (2014) and the A186705 exact values were
  checked against sources this pass; the triangle-free 5-critical ε-refinement
  was surfaced by search (authors/venue to pin before citing it verbatim).
speculation: none about the N=11 bound itself — the crossing is exact arithmetic
  on published values. The only open empirical point is whether the n=12 census
  with the -D6 cap is feasible; that is a scaling question, not a conjecture.
```

## Why this is not a closed line

- Not `discharging-minimal-counterexample` (refuted): that crossed the general
  Kostochka–Yancey bound against the **asymptotic** SST ceiling C·n^{4/3},
  which first stops contradicting at n=10 even with the impossible C=1, giving
  N=9. This crosses against the **exact** ceiling A186705, which pushes the same
  bound to N=11 — the exact value the census independently proved — and thereby
  locates the real barrier (ε* = 5/48 at n=12), not the asymptotic artifact.
- Not `census-kernel` / the N=11 size-bound result (in `research/backward/`):
  that proves N=11 **computationally** by enumerating 187M graphs. This is the
  **analytical** independent route to the same theorem, plus the free degree-cap
  (max degree ≤ 6) tightening that the census can adopt to attempt N=12.
- It is a theorem route (an inequality), not a search and not a certificate, and
  it is exact at every step — no asymptotic constant left unspecified.

Named mathematics: Kostochka–Yancey 5-critical edge bound (2014), the Erdős
unit-distance problem and its exact small values u(n) (OEIS A186705; Schade
n ≤ 14, Alexeev–Mixon–Parshall 2024 n ≤ 21), the plane kissing number 6.

## What would falsify it

- A misread of A186705 (if u(11) ≥ 24 or u(12) ≤ 25 the crossing differs) —
  verifiable directly against `research/summaries/oeis_a186705.md`, where the
  terms are recorded.
- A 5-chromatic unit-distance graph on ≤ 11 vertices — this would contradict
  both this theorem and the already-verified census, and is the one fact that
  would kill the line outright.
- A source establishing an *explicit* ε > 5/48 in the triangle-free 5-critical
  refinement — this would falsify claim (5) that N=12 is analytically out of
  reach and would immediately upgrade the bound to N=12.
