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

**Newest addition (trollopedelange.md, + .full.md):** the arithmetic engine now has a
*primary, locally-held* source proving the Delange-type structure it had previously only
cited as a gated abstract. Girgensohn, "Digital sums and functional equations" (INTEGERS 11,
2011, #A54) gives an elementary proof of the exact Trollope–Delange representation for
both summatory functions —
  - ones: S(n) = (n/2)log₂p(n) + p(n)·F(x), p(n)=largest 2-power ≤ n, x=(n−p(n))/p(n),
    with F a continuous 1-periodic fluctuation; equivalently S(2n)=2S(n)+n and the
    S(n+p(n)), S(n+2p(n)) recurrences, so the whole sequence is fixed by its values at
    powers of two in O(log n) steps;
  - zeros: (1/n)S⁽⁰⁾₁(n) = (1/2)log₂n − 1 − (1/2)log₂(x+1) + F⁽⁰⁾₁(x)/(x+1), F⁽⁰⁾₁(x)=x+½T(x).
This independently corroborates the A000788/A059015 recurrences (bitcount.md, zerocount.md)
and, unlike the gated Larcher–Pillichshammer abstract (weightedmom.md), is fully readable
locally. It is the unweighted one-/zero-count summatory engine the run's k·-weighted A(n),B(n)
build on via its per-bit decomposition. Caveat recorded: the paper's formulas are unweighted,
and the zero-count side uses a s⁽⁰⁾(0):=−1 normalisation — both must be handled before quoting
numbers (see research/verify_trollopedelange.md for the tool_builder four-point numerical
check).

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

