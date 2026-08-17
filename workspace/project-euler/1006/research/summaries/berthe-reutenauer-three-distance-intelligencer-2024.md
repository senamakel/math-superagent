# Berthé & Reutenauer — On the Three-Distance Theorem (Intelligencer 2024)

Source: Valérie Berthé, Christophe Reutenauer, "On the Three-Distance
Theorem", The Mathematical Intelligencer 46 (2024), 183–188, DOI
10.1007/s00283-023-10316-z. Full text:
`research/sources/berthe-reutenauer-three-distance-intelligencer-2024.full.md`
(author copy from https://reutenauer.math.uqam.ca/wp-content/uploads/2024/05/Three-distance.pdf).

## Statements it establishes

- **Three-distance theorem** (history): conjectured by Steinhaus; first proved
  in 1958 by Sós, Surányi, Świerczkowski; later Slater and Halton. If one
  picks α and n, the fractional parts 0, α, 2α, …, (n−1)α together with 1
  partition [0,1] into successive intervals of at most three different
  lengths; if three occur, the longest is the sum of the other two.
- **Theorem 1** (new): in the three-distance partition, the leftmost interval
  is not the longest. Encoding the successive interval lengths from left to
  right by letters (leftmost length → a, longest → b, other → c; two-length
  case: leftmost → a, other → c), the **distance-encoding word** is the word
  encoding of a circular symmetric exchange of three (resp. two) intervals.
- **Theorem 3**: a Lyndon word is *perfectly clustering* iff it is the word
  encoding of some circular symmetric discrete interval exchange (essentially
  Ferenczi–Zamboni; two-letter case Mantaci–Restivo–Sciortino). Hence the
  distance-encoding word is a perfectly clustering Lyndon word.
- Proof style: purely combinatorial, first for rational α then irrational by
  compactness/pigeonhole; running example α = 5/22, n = 7 with interval
  lengths 3,2,3,2,5,5,2 encoded as `acacbbc`.

## Relation to PE1006

- Primary recent source for the *structure of the arc partition* used by
  directive 2 (circle cut at k+1 points, arcs = the k+1 representatives) and
  directive 1 (rotation bookkeeping). In the PE1006 setting α = a = F(n−2)/F(n)
  is rational, and the theorem's rational-α branch (denominator > n) is the
  operative one.
- The "leftmost interval is not the longest" and the perfectly-clustering /
  Lyndon structure of the distance-encoding word is the same ordering rigidity
  that makes the k+1 arc-midpoint representatives line up in cyclic order —
  the fact the mechanical-word construction exploits when it iterates the
  k+1 intercepts by arc.

Not a method source: no algorithm; it fixes the statement, the history, and
the word-structure of the partition the solver computes over.