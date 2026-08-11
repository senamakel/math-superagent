# Fold: counting arithmetic (A,B in polylog)

The engine that supplies the board totals `A(n)=Σk·popcount(k)` and
`B(n)=Σk·zerocount(k)` in O(poly log n) time — the scale n=10^5 needs this,
not iteration.

- [[bitcount]] — OEIS A000788, summatory 1-bit count with O(log n)
  divide-and-conquer recurrences → the per-bit-weighted A(n).
- [[zerocount]] — OEIS A059015, summatory 0-bit count, O(log n); identity
  A059015 = A083652 − A000788 → the per-bit-weighted B(n). (A083652 added as
  [[a083652]], the total-bit third leg.)
- [[trollopedelange]] — Girgensohn 2011 INTEGERS #A54, primary proof of the
  explicit Trollope–Delange closed forms (main term + 1-periodic fluctuation),
  O(log n) recurrences.
- [[weightedmom]] — Larcher & Pillichshammer 2005: weighted sum-of-digits
  first moments (our k·-weighted A,B) admit the same Delange-type closed form.
- [[verify_trollopedelange]] — concrete numeric check-list that must be run
  before any Girgensohn result is quoted.

What this yields: A(n), B(n) computable symbolically, so the (A,B) minimax DP
runs at n=10^5.
