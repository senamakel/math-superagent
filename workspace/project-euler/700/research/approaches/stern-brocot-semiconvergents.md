# Approach: Eulercoins as semi-convergents of A/M via a Stern–Brocot walk

```approach
idea: Identify the Eulercoins with the semi-convergents (intermediate
       fractions) of A/M that lie just below A/M, enumerated by a Stern–
       Brocot tree mediant walk from 0/1 upward; a coin is a fraction p/q
       with q·A − p·M positive and record-small, and the coin value is
       exactly q·A − p·M.
mechanism: c_n = A·n mod M = A·n − p·M with p = floor(A·n/M), so
       c_n = q·(A/M − p/q)·M with q = n. A record-low coin is therefore a
       lower fraction p/q (p/q < A/M) whose signed gap q·A − p·M is a new
       minimum over all smaller denominators. The fractions realising these
       minima are precisely the best approximations of the second kind of
       A/M from below — convergents *and* their semi-convergents (intermediate
       fractions), i.e. exactly the nodes on the Stern–Brocot path from 0/1
       to A/M that are visited when approaching A/M from the left. Enumerating
       this path is a comparison-only mediant walk (an L/R string whose length
       is the sum of the continued-fraction partial quotients, O(log M) nodes),
       a different *object* (Farey/Stern–Brocot tree, semi-convergents) from
       the index recurrence. Long runs of repeated left-steps correspond to the
       observed 17 arithmetic-progression runs of coin values.
status: grounded
precedent: the identification is exactly this run's verified claim
       `eu700-record-lows-are-best-lower-approximations` (research/summaries/
       hancl-turek-one-sided-diophantine-approx.md): the Eulercoins are the
       best lower Diophantine approximations of the second kind of A/M, which
       by Hancl–Turek Theorem 4.5 are precisely the convergents and
       semiconvergents (p_n r + p_{n-1})/(q_n r + q_{n-1}) of A/M at odd n,
       0 ≤ r < a_{n+1}. The Stern–Brocot/semiconvergent correspondence is
       standard: Reutenauer, "On the Stern–Brocot expansion of real numbers",
       J. Theor. Nombres Bordeaux 32 (2020) (doi 10.5802/jtnb.1104) — the
       labels on the Stern–Brocot path are exactly the semiconvergents, the
       convergents being the path-turning nodes; Milinkovic–Malesevic–Banjac,
       "Continued fractions, intermediate fractions and their relation to the
       best approximations", J. Sci. Arts 20 (2020) (doi 10.46939/j.sci.arts-
       20.3-a05) — intermediate fractions (semiconvergents) and their role in
       best approximations of the second kind.
first-step: Run the Stern–Brocot mediant walk for A/M =
       1504170715041707 / 4503599627370517, collecting every left-side
       fraction p/q whose gap q·A − p·M is a new minimum; check that the
       list of gaps equals the brute oracle's coin values and that the
       denominators equal the coin indices (1, 3, 506, 2527, 4548, ...).
       By the grounded identification this is expected to reproduce all 102
       coins; the walk IS the recurrence's ceil-quotients at semi-convergent
       level.
```

## Notes

- GROUNDED (structural, not a new computation). The Eulercoins are exactly the
  best lower approximations of the second kind of A/M (claim
  eu700-record-lows-are-best-lower-approximations), and Hancl–Turek Thm 4.5
  classifies those as the convergents and semiconvergents at odd stages. The
  Stern–Brocot path labels are precisely the semiconvergents (Reutenauer), so
  the walk enumerates exactly the Eulercoin set. This is a genuinely different
  *object* (the Farey/Stern–Brocot tree, semi-convergents) from the two-term
  index recurrence, so it is a legitimate independent route.
- Caveat: it is not independent at the algorithmic level — the mediant walk and
  the index recurrence both descend the same Euclidean algorithm of A/M; the
  walk's L/R string is the partial-quotient string of A/M, which is exactly
  what the recurrence's ceil-quotients encode. So grounding does NOT certify a
  code path independent of eu700-record-low-recurrence; it certifies the
  identification.
- The "semi-convergent" part is what makes this complete where the naive
  two-sided lattice/Gauss view (lattice-gauss-reduction, refuted) is not: the
  coins include intermediate fractions, not just two-sided convergents.
