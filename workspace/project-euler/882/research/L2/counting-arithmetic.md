# L2 fold: Counting arithmetic for A(n), B(n)

Seven L1 notes cohere into one subject: **computing the board totals
A(n)=Σₖ₌₁ⁿ k·popcount(k) and B(n)=Σₖ₌₁ⁿ k·zerocount(k) in polylog time** — the
engine the (A,B) DP needs at n=10⁵. They establish:

- **A(n)** rests on the summatory 1-bit count A000788 (Σ popcount) with O(log n)
  recurrences ([[bitcount]]); the k·-weighting is the run's per-bit
  superimposition.
- **B(n)** rests on the summatory 0-bit count A059015, via
  A059015 = A083652 − A000788 ([[zerocount]], [[a083652]]); [[a083652]] gives the
  unweighted total-bit leg in exact O(1) closed form.
- **Trollope–Delange structure** (main term + 1-periodic fluctuation) is proven
  from a primary source ([[trollopedelange]], Girgensohn 2011), which also
  supplies the O(log n) recurrences; [[verify_trollopedelange]] is the check-list
  to run before quoting it numerically.
- **Weighted digit sums keep that structure**: first-moment weighted digit-sum
  functions have closed-form main-term + periodic-fluctuation forms — now from
  two openly-hosted primary texts, **[[flajolet_weighted_digitalsums]]**
  (arXiv:1003.0150) and **[[minabutdinov_qweighted]]** (arXiv:1801.03120,
  Takagi–Landsberg limits), upgrading the earlier abstract-only [[weightedmom]].
- **Negative result:** S(n) is **not in OEIS** ([[weightedsearch]]), so no
  closed-form lead there — S(n) must be derived.

**Net result:** A(n), B(n) are computable symbolically in O(poly log n), not by
iterating to n, so the (A,B) minimax DP can run at n=10⁵.
