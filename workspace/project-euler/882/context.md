# Context — what the library now establishes

The bit-deletion game reduces to counting: the board is a **disjunctive sum** of
one subgame per number ([[disjsum]], [[cgt]]), each number's game equals the integer
(a−b) ([[surreal]]), so the no-skip value of the whole board is the single integer
**A−B** (A = total 1-bits, B = total 0-bits). Sprague–Grundy does not apply —
strictly partisan ([[partisan]]); normal play is the win rule ([[normalplay]]); the
skip is a zugzwang escape and a loopy self-loop resolved as a fixpoint, finite S(n)
since the game is a stopper ([[zugzwang]], [[loopy]]).

The arithmetic engine computes A(n) and B(n) in **polylog time** (not iterating to
n), which the n=10⁵ scale demands:
- **A(n)=Σk·popcount(k)** via A000788 ([[bitcount]]) and **B(n)=Σk·zerocount(k)**
  via A059015 ([[zerocount]]), both with O(log n) divide-and-conquer recurrences.
- **Trollope–Delange** structure (main term + continuous 1-periodic fluctuation)
  is now proven from a primary, locally-held source — Girgensohn ([[trollopedelange]],
  unweighted; see [[verify_trollopedelange]] for the numeric check). Weighted
  first-moments like our k·-weighted A,B admit the same Delange-type closed forms
  per Larcher & Pillichshammer ([[weightedmom]]); the specific O(log n) recurrences
  come from the A000788/A059015 plus the run's per-bit weighting.
- **Newest: [[pass_waiting]]** (Larsson–Nowakowski–Santos 2015, arXiv:1505.01907) — a
  primary, math-rigorous treatment of passes/waiting moves: when extra passes "do no
  harm" (= order-embedding into Conway normal-play) and the pass as the
  zugzwang/tempo tool. It turns the earlier Wikipedia-level skip picture ([[zugzwang]],
  [[loopy]]) into a citable primary source; it is a structural analogue, not a recipe —
  our skip costs budget, so S(n) still comes from the (A,B) minimax DP.
- **Enrichment this cycle — [[a083652]] (OEIS A083652)** (summatory binary
  length, `Σₖ₌₀ⁿ bitlen(k)`), exact O(1) closed form `(n+1)·bitlen(n+1) − 2^{bitlen(n+1)} + 2`. This is the third leg of `total_bits = ones + zeros`
  (the identity [[zerocount]] uses to get B from A083652 − A000788). It makes
  the unweighted total-bit count available in closed form, tightening the
  A(n),B(n) counting-arithmetic toolchain for n=10^5.

**Demotion this cycle — the two raw arXiv-page notes are folded away.**
`raw_mfl_pass.md` and `raw_pass_waiting_check.md` were the unprocessed arXiv
abstract pages for papers already analysed in [[mfl_pass]] and [[pass_waiting]];
each was over the 1000-token cap and re-sent on every model call. Each is now a
~50-token stub stating the paper's one consequence and wikilinking its proper L1
analysis and the L0 full text — the tree still reaches every detail, but the
per-call context load drops by ~1400 tokens. No new mathematical content was
added this cycle; the run's pass-theory picture was already complete.

**Caveat (open):** the counting model is a *surrogate* — its (A,B) transitions
(One →(A−1,B), Zero →(A,B−1)) ignore that deleting a leading 1 can also drop 0-bits
(e.g. "100"→0). Given S(2)=2, S(5)=17, S(10)=64 are reproduced, but real-vs-counting
S(n) equality for all n is checked empirically by brute.py vs counting.py
([[disjsum]] records the caveat).
