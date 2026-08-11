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
