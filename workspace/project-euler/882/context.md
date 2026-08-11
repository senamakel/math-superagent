# Context — what the library now establishes

The reference library previously covered the **game-theoretic/structural side**
of the problem end to end:

- The board is a **disjunctive sum** of one subgame per number, each number's
  game equals the integer (a−b) (surreal values; disjsum.md, surreal.md), so the
  no-skip value of the whole board is the single integer **A−B** where A = total
  1-bits, B = total 0-bits. Sprague–Grundy does not apply (strictly partisan;
  partisan.md); normal play is the win rule (normalplay.md); the skip is a
  zugzwang escape and a loopy self-loop in the DP (zugzwang.md, loopy.md).

That told **why** the game reduces to counting bits, but not **how** to compute
A and B at n=10^5 efficiently. The library now fills that arithmetic gap:

- **A(n) = Σ k·popcount(k)**: OEIS A000788 (bitcount.md) gives the summatory
  1-bit count with **O(log n)** divide-and-conquer recurrences (a(2n)=a(n)+a(n-1)+n,
  a(2n+1)=2a(n)+n+1; a(2^m−1)=m·2^(m-1)) and 2-regular / Trollope–Delangé
  structure.
- **B(n) = Σ k·zerocount(k)**: OEIS A059015 (zerocount.md) gives the summatory
  0-bit count with the complementary recurrences and the identity
  zeros = total-digits − ones (A059015 = A083652 − A000788).

Net new result: the two integers the (A,B) minimax DP runs on are computable in
**polylog time** rather than by iterating to n, which is exactly what the n=10^5
scale demands. (The required sums are the k·-weighted versions of these
unweighted summatory sequences; the run's own derivation applies the same
bit-position decomposition for the weighting.) Also now on record: a source
caveat that the leading-bit-deletion effect means the counting model is a
surrogate whose S(n)-agreement with the real game is being checked empirically.

**Newest addition (weightedmom.md):** the *weighted* side now has a named,
citable theory backing the k·-weighting instead of a bare derivation. Larcher &
Pillichshammer (2005), "Moments of the weighted sum-of-digits function", shows
that first-moment digit sums (Σ k·popcount(k), Σ k·zerocount(k) are exactly
first moments of digit-count functions) admit **Delange-type closed forms** —
a main term plus a fluctuation — rather than needing term-by-term summation. So
the k·-weighted A(n) and B(n) are not merely unweighted-with-a-patch: they are
instances of a class of functions known to have polylog-expressible moments.
Caveat recorded: only the abstract is locally available (PDF gated); the paper
is cited for the existence/structure of the weighted moment formulas, and the
specific O(log n) recurrences still come from A000788/A059015 plus the run's
bit-position decomposition.

