# Literature grounding of the three proposed reformulations (PE 700)

Question: do the inventor's three reformulations (lattice/Gauss reduction,
Stern–Brocot semiconvergents, Euclidean sum recursion) correspond to named,
sourced theory, does that theory's hypothesis hold here, and has it been
applied to this problem — i.e. is each a grounded reformulation or a dead end?

Central fact (already in the library, claim
`eu700-record-lows-are-best-lower-approximations`): the Eulercoins are the
record lows of c_n = A·n mod M, which are exactly the **best lower Diophantine
approximations of the second kind** of α = A/M, and Hančl–Turek, *One-sided
Diophantine approximations*, J. Phys. A 52 (2019) 045205, arXiv:1809.01013,
Theorem 4.5 (+ Remark 4.7) classifies those as the convergents and
**semiconvergents** (intermediate fractions) (p_n r + p_{n-1})/(q_n r + q_{n-1})
of A/M at **odd** n, 0 ≤ r < a_{n+1}. The count is small (102), not O(M).

That single fact decides two of the three candidates.

## Candidate 1 — lattice-gauss-reduction: REFUTED

- The 2D lattice / Gauss-reduction literature is real and the correspondence
  "continued fraction ⟷ Gauss reduction of the closest-vector chain to the line
  y=(A/M)x" is standard (low-dimensional lattice basis reduction:
  https://dl.acm.org/doi/10.1145/1597036.1597050, 2D Gauss reaches successive
  minima; reduced cells / 2D-lattice reduction:
  https://link.springer.com/article/10.1007/s10208-022-09601-8; nearest-integer
  Euclidean algorithm with centred quotients:
  http://www.numbertheory.org/php/neuclid.html).
- BUT those successive minima are the **two-sided** convergents of A/M — a
  proper subset of the Eulercoin set. The coins include the one-sided
  **intermediate fractions** (the long AP runs), which the plain centred-
  quotient Gauss chain skips. So the naive Gauss reduction cannot yield all 102
  coins, and matching the coins would need an *asymmetric* one-sided norm,
  outside the classical two-sided theory.
- Also, even where the lattice view is legitimate, it is the same Euclidean
  descent as the already-verified record-low index recurrence — not an
  independent computation.
- Verdict: refuted as a route to the full coin set; kept as vocabulary.

## Candidate 2 — stern-brocot-semiconvergents: GROUNDED

- The identification is exactly the one-sided best-lower-approximation claim
  above (Hančl–Turek Thm 4.5).
- The Stern–Brocot semiconvergent correspondence is standard: Reutenauer,
  *On the Stern–Brocot expansion of real numbers*, J. Théor. Nombres Bordeaux
  32 (2020), doi 10.5802/jtnb.1104 (the path labels of the Stern–Brocot tree are
  exactly the semiconvergents; the convergents are the path-turning nodes);
  Milinković–Malešević–Banjac, *Continued fractions, intermediate fractions and
  their relation to the best approximations*, J. Sci. Arts 20 (2020)
  doi 10.46939/j.sci.arts-20.3-a05 (semiconvergents/intermediate fractions and
  best approximations of the second kind).
- Verdict: grounded as a legitimately different *object* (Farey/Stern–Brocot
  tree, semiconvergents). Caveat: the mediant walk and the index recurrence both
  descend the same Euclidean algorithm, so it is not an algorithmically
  independent route.

## Candidate 3 — euclidean-sum-recursion: GROUNDED (with independence caveat)

- The "division-transform" self-similarity it proposes is exactly floor_sum, the
  AtCoder Library Euclidean recursion — claimed eu700-floor-sum-tool,
  validated at full size (research/summaries/floor-sum-editorial.md).
- The run-by-run telescoping over quotient-2 steps is the checked AP-run
  decomposition of research/approaches/pe700-ap-runs.md (17 runs; V recomputed
  from it exactly).
- The Dedekind-sum sawtooth circle is real (Hall–Huxley Acta Arith 63 (1993)
  doi 10.4064/aa-63-1-79-90; Girstmair Int. J. Number Th. 13 (2017)
  doi 10.1142/s1793042117500889; Minelli–Sourmelidis–Technau arXiv:2301.00441)
  but is **vocabulary only**: the sum of record lows is not a Dedekind/floor-
  power sum (those sum the whole residue orbit, not the sparse record-low
  subsequence), so no off-the-shelf Dedekind closed form applies.
- Verdict: grounded as an O(log M) exact route that never materialises the
  coins. Independence caveat: a values-only recursion is the value-form of the
  same quotient descent as the index recurrence, so it is a distinct code path
  but not a mathematically distinct derivation.
