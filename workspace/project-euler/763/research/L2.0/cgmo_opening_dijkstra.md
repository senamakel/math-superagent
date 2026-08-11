# Pebbling a chessboard — Chung, Graham, Morrison, Odlyzko (opening, via Dijkstra EWD 1200)

<!-- source: https://www.cs.utexas.edu/~EWD/transcriptions/EWD12xx/EWD1200.html -->
<!-- original: Amer. Math. Monthly 102 (1995) 113-123.  The UCSD hosted PDF
     (fanchung.ucsd.edu/mypaps/fanpap/150chess.pdf) is a scan with no text
     layer, so the definitive transcription is Dijkstra's EWD 1200, which
     reproduces pp. 113-115 (Introduction + §2 opening) verbatim. -->

## The problem (verbatim from the paper)

Infinite "chessboard" B covering the first quadrant; cells labelled (i,j),
i,j ≥ 0. Initially a single pebble at (0,0). A **move** removes some pebble,
say in cell (i,j), and places two pebbles at (i+1,j) and (i,j+1), *provided
each of those positions is not already occupied*. After k steps the board has
k+1 pebbles. Such configurations of pebbles are **reachable configurations**.
R(k) = set of reachable configurations with k pebbles.

## Definitions

- **Level** L(k) = {(i,j): i+j = k}. The union L(1)∪L(2)∪L(3) (all cells with
  i+j ≤ 3; Dijkstra notes L(0) should be included) is *unavoidable*: any
  reachable configuration must have some pebble in it.
- An *unavoidable set* is one which intersects every reachable configuration.
- A *minimal unavoidable set* S is unavoidable with no proper subset also
  unavoidable; M(k) = family of minimal unavoidable sets with k cells.

## Key results (the paper's §2)

**Lemma 1** (Kontsevich). L(1)∪L(2)∪L(3) is unavoidable.
Proof (weight invariant): assign weight 2^{-(i+j)} to cell (i,j).
(i) total weight covered by pebbles in any reachable configuration is 1 (a
move preserves it: 2^{-(i+j)} = 2^{-(i+1+j)} + 2^{-(i+j+1)});
(ii) total weight of all cells = Σ_{i,j≥0} 2^{-(i+j)} = 4;
(iii) weight of L(1)∪L(2)∪L(3) is 13/4, so the complement has weight only 3/4
< 1 and cannot contain all pebbles of a reachable configuration. ∎

**Lemma 2** (Khodulev). L(1)∪L(2) is unavoidable. (Any reachable configuration
C has exactly one pebble on each of the two boundaries {(i,0)} and {(0,j)},
so the weight it can cover outside L(1)∪L(2) is too small; to avoid it would
have to cover all those cells, impossible since C is finite.) Neither set is
minimal.

**Uniqueness of the move set.** For any reachable configuration C, the *set* of
moves needed to reach C is unique; only the *order* of those moves can vary.

**Lemma 3** (stacking). If a configuration (≤1 pebble per cell) can be reached
by moves that *allow* accumulation of multiple pebbles in cells, then it can
also be reached by the standard non-accumulating moves. (Model: pebbles first
move onto an infinite binary tree rooted at (0,0); the 2^k vertices of level k
are identified with the k+1 cells of level L(k). Easy induction.)

**Theorem 1** (polynomial-time recognition). Given X ⊂ B, define the set of
moves M(X) recursively: starting at level 0 and going up one level at a time,
perform the moves required either to remove *all* pebbles from a cell in X, or
to remove *all but at most one* of the pebbles from a cell not in X, through
the last level L(h(X)) containing a cell of X. Then:
**X ⊂ B is unavoidable iff after executing M(X), some cell contains at least
3 pebbles.** (This is the paper's level-trimming criterion; it is the 2D case
of Eriksson's Propositions 4/13.)

Also noted: r(k) = |R(k)| and m(k)=|M(k)| asymptotically as k→∞ are new; the
analysis leads to asymptotic enumeration. Furthr generalisations to arbitrary
posets by Eriksson.

## Bearing on this run

This gives the exact 2D definitions, the weight-invariant, the unavoidable-set
/ level-trimming machinery, and Lemma 3 (stacking ⇔ non-stacking) — the facts
the 3D generalisation (Eriksson's folded polyominoids) builds on. The 3D PE763
process is exactly Vaderlind/Eriksson's n=3 pebbling game (a pebble at
(x,y,z) → three pebbles at the three positive-unit neighbours if all three are
empty), so Eriksson's n≥3 theory, not this 2D paper's crossings, governs the
3D D(N).

## Sources
- Chung, Graham, Morrison, Odlyzko, "Pebbling a chessboard", Amer. Math.
  Monthly 102 (1995) 113-123. DOI 10.2307/2975345.
- Transcription of the opening: Dijkstra EWD 1200,
  https://www.cs.utexas.edu/~EWD/transcriptions/EWD12xx/EWD1200.html
- Sci-scan of the full paper (no text layer):
  https://fanchung.ucsd.edu/mypaps/fanpap/150chess.pdf
