# Approach: Eulercoins as successive minima of a rank-2 lattice (Gauss reduction)

```approach
idea: Cast the Eulercoins as the successive minima of the rank-2 lattice
       L = {(x, y) in Z^2 : y ≡ A·x (mod M)}, spanned by (M, 0) and (A, 1),
       and recover the record lows (n_k, c_k) with c_k = A·n_k mod M as the
       reduced-basis chain produced by Gauss's algorithm for 2D lattice
       basis reduction (equivalently, Lagrange–Gauss reduction of the binary
       quadratic form attached to L). The sum of Eulercoins is then the sum
       of the second coordinates along the reduction chain.
mechanism: gcd(A,M)=1 makes n ↦ A·n mod M a permutation, and the points
       (n, A·n mod M), n = 1,2,3,... are exactly the lattice points of L in
       the first quadrant ordered by x. A record-low coin is a lattice point
       whose second coordinate is minimal among all points with smaller
       first coordinate — the defining property of a successive minimum in a
       norm adapted to the slope A/M. Gauss reduction (nearest-integer /
       centred quotients q = ⌈r_{k-1}/r_k⌉, taking the least absolute
       remainder) produces exactly the chain of "closest vectors to the line
       y = (A/M)x", which is the classical lattice reformulation of the
       continued fraction of A/M. This is a different *object* (the lattice
       and its successive minima) and a different *algorithm* (centred
       reduction) from the smsxgz/brob26 index recurrence, even though the
       two descents are morally equivalent; it terminates in O(log M)
       Euclidean steps, not O(M).
status: refuted
killed-by: The 2D Gauss/lattice-reduction chain recovers the closest vectors to
       the line y=(A/M)x in the Euclidean norm — the (two-sided) convergents
       of A/M. That is a PROPER SUBSET of the Eulercoin set: the record lows
       are the one-sided BEST LOWER approximations of the second kind, which
       by Hancl–Turek Theorem 4.5 are the convergents AND semiconvergents at
       odd stages (see eu700-record-lows-are-best-lower-approximations). The
       plain centred-quotient Gauss chain skips the intermediate fractions
       (the long AP runs), so it cannot yield all 102 coins, and it is the
       same Euclidean descent as the already-established record-low index
       recurrence — not an independent computation. Refuted as a route to the
       full coin set, not as vocabulary: the second-kind/lattice and nearest-
       integer-Euclidean theory is genuine (see precedent).
precedent: https://arxiv.org/abs/1809.01013 (Hancl–Turek, Thm 4.5 + Remark 4.7);
       https://dl.acm.org/doi/10.1145/1597036.1597050 (low-dim lattice basis
       reduction: 2D Gauss reaches successive minima in l2); 
       https://link.springer.com/article/10.1007/s10208-022-09601-8 (2D-lattice
       reduction, reduced cells);
       http://www.numbertheory.org/php/neuclid.html (nearest-integer Euclidean
       algorithm, centred quotients). Claim eu700-record-lows-are-best-lower-
       approximations already in this library.
first-step (would-be oracle): build [(A,1),(M,0)], run nearest-integer Gauss
       reduction, compare second coordinates against the coin list — expected
       to give only the two-sided convergents (a subset), confirming the kill.
```

## Notes

- KILLED. The lattice/second-kind correspondence is classical and real (Gauss
  reduction, nearest-integer / centred Euclidean algorithm — the run's
  `nearest-integer-euclidean` source), and 2D Gauss reduction does reach the
  successive minima of L in the Euclidean norm. But those are the *two-sided*
  convergents of A/M — a proper subset of the Eulercoins. The Eulercoins are
  the one-sided best-lower-approximations of the second kind, which include
  semiconvergents/intermediate fractions (Hancl–Turek Thm 4.5), and the plain
  centred-quotient Gauss chain skips exactly those intermediate fractions (the
  long AP runs).
- Even where the lattice view is legitimate, it is the same Euclidean descent
  as the already-verified record-low index recurrence, so it is not an
  independent verification — it reproduces the index recurrence in different
  clothing.
- The success of any "successive minima" version hinges on an *asymmetric*
  (one-sided) norm, which is precisely outside the classical two-sided Gauss
  reduction theory; that is the reason the naive Gauss chain cannot reach all
  102 coins.
