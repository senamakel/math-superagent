# L2 fold: Counting arithmetic for A(n), B(n) and negative search results

Seven L1 notes cohere into one subject: **computing the board totals
A(n)=Σₖ₌₁ⁿ k·popcount(k) and B(n)=Σₖ₌₁ⁿ k·zerocount(k) in polylog time** — the
engine the (A,B) DP needs at n=10⁵ — plus the negative search result. Together
they establish:

- **A(n)** rests on the summatory 1-bit count A000788 (Σ popcount) with O(log n)
  divide-and-conquer recurrences ([[bitcount]]); the k·-weighting is the run's
  per-bit superimposition.
- **B(n)** rests on the summatory 0-bit count A059015 (Σ zerocount), computed as
  total bits − ones via the identity A059015 = A083652 − A000788 ([[zerocount]],
  [[a083652]]); [[a083652]] supplies the unweighted total-bit leg in exact O(1)
  closed form.
- **Trollope–Delange structure** (main term + 1-periodic fluctuation) is proven
  from a primary source ([[trollopedelange]], Girgensohn 2011) and gives the
  same O(log n) recurrences; [[verify_trollopedelange]] is the check-list that
  must be run before any of its formulas is quoted numerically.
- Weighted first-moments of digit-sum functions (our k·-weighted A,B) admit the
  same Delange-type closed form ([[weightedmom]], Larcher–Pillichshammer 2005;
  abstract-only, subscription-gated full text).
- **Negative result:** the sequence S(n) is **not in OEIS** ([[weightedsearch]]),
  so no closed-form lead there — S(n) must be derived, not looked up.

**Net result:** A(n) and B(n) are computable symbolically in O(poly log n), not
by iterating to n, so the (A,B) minimax DP can be run at n=10⁵.
