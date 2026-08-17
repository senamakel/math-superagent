# Alessandri & Berthé — Three distance theorems and combinatorics on words

Source: Pascal Alessandri, Valérie Berthé, "Three distance theorems and
combinatorics on words", L'Enseignement Mathématique (2) 44 (1998), 103–132.
Full text: `research/sources/alessandri-berthe-three-distance-theorems.full.md`
(converted from https://www.irif.fr/~berthe/Articles/3d.pdf). Survey + new
results; 85 citations (citation graph: `research/summaries/citations_w62113036.md`).

## Statements it establishes

- **Three distance theorem**: for 0 < α < 1 and n ≥ 1, the points
  {0}, {α}, …, {nα} mod 1 partition the unit circle into n+1 intervals of at
  most three different lengths, and if three occur, one is the sum of the
  other two. Diophantine content: it expresses the approximation properties
  of the Farey partial convergents of α (p. 1).
- **Three gap theorem** (equivalent dual form, p. 2): given α, β ∈ ]0,1[, the
  gaps between successive n with {αn} < β take at most three values, one the
  sum of the other two. If β = 1−α or β = α, the coding of the rotation by α
  with respect to [0,β[, [β,1[ is a **Sturmian sequence** — the binary word
  PE1006's S is one such coding (α = 1/φ²). The lengths of the 0-runs and
  1-runs are exactly the three gaps.
- **Factor frequencies** (Theorem 8): the frequencies of factors of a given
  length of a Sturmian sequence take at most three values; the three-distance
  theorem is equivalent to this fact.
- **Lemma 3** (the bridge used by directive 2): for a coding u of a rotation
  by angle α w.r.t. an interval partition, the frequencies of factors of u of
  length n equal the lengths of the intervals bounded by the points
  {iα} (i = 0..n−1) cut by the partition boundary — i.e. the *measure-theoretic*
  side of the arc/rotation construction.
- **Theorem 6**: for a recurrent sequence of complexity p(n), factor
  frequencies of length n take at most 3(p(n+1) − p(n)) values; for Sturmian
  p(n)=n+1 this gives the ≤ 3 bound.

## Relation to PE1006

- Anchors the *geometry* behind directive 2: the k+1 distinct length-k factors
  of a Sturmian word correspond to the k+1 arcs obtained by cutting the circle
  at {−mα} mod 1, m = 0..k (the arc-midpoint construction in claim
  `mechanical-word-digit-rule`). This survey proves the underlying fact that
  the *frequencies*, i.e. the counting multiplicities, of these factors are
  controlled by interval lengths — the same three-distance bookkeeping that
  underlies directive 1's cyclic-autocorrelation formula
  A(d) = max(0,m−t)+max(0,m−(N−t)).
- The "at most three" structure is why the autocorrelation counts in
  directive 1 have a closed form at all: at each lag d, the pairs (j, j+d)
  split into at most three gap classes.

Not a method source — a structural/survey source. The exact closed form of
A(d) itself is still a verify-in-container identity (it appears in no single
paper; this survey is the closest authoritative treatment of its rotation
bookkeeping).