# Van Ravenstein — The Three Gap Theorem (Steinhaus conjecture), 1988 (HAL copy)

Source: Tony van Ravenstein, "The Three Gap Theorem (Steinhaus Conjecture)",
J. Austral. Math. Soc. (Series A) 45 (1988), 360–370. Full text on disk:
`research/sources/van-ravenstein-three-gap-theorem-1988-hal.full.md`
(converted from the HAL-hosted copy of M. Mayero's detailed working of
van Ravenstein's proof, https://hal.science/hal-00090031/PDF/three-gap.pdf;
DOI 10.1017/S1446788700031062).

## Statements it establishes

- **Theorem (Three Gap / Steinhaus)**: for all irrational α and all N, the N
  consecutive points {iα} mod 1, i = 0..N−1, partition the circle into arcs
  (gaps) of at least two and at most three different lengths.
- **Constructive content** (the reason this paper is worth holding): the proof
  identifies the *first(N)* and *last(N)* indices — the points giving the
  minimal and maximal fractional part among {0, α, …, (N−1)α} — and proves a
  recurrence: as N grows, the gap structure evolves by steps controlled by the
  simple continued fraction expansion of α; the gap lengths and their
  multiplicities at each N are read off the continued fraction. For the
  rational case α = p/q with N < q the same recurrences apply.
- The HAL copy is Mayero's carefully-axiomatised reworking (lemmas: existence
  of first and last, the after() relation, N ≤ M, first(N)=first(M),
  last(N)=last(M)), i.e. a formalisable proof of the gap structure.

## Relation to PE1006

- This is the constructive *counting* result behind directive 1's
  autocorrelation formula. PE1006's slope is the rational approximant
  a = F(n−2)/F(n) of 1/φ² (denominator F(n) ≫ k), and the k+1 points
  {−ma} mod 1, m = 0..k, are the arc cuts. For this continued fraction
  (partial quotients all 1 — the golden-ratio/Fibonacci case) the gap-length
  structure at N = k+1 points is exactly the Fibonacci-ratio bookkeeping:
  at every stage only two or three gap lengths occur, with counts given by
  the Euclidean/Fibonacci recursion; this is what makes
  A(d) = max(0,m−t)+max(0,m−(N−t)) with t = (dm) mod N a *three-term* formula
  rather than a distribution over many lengths.
- Combined with Alessandri–Berthé (factor frequencies ≤ 3 values) and
  Berthé–Reutenauer (distance-encoding word structure), it anchors the "why
  at most three lengths, and which" part of the pair-correlation route.

Not a method source: no algorithm for PE1006 itself; it is the classical proof
that the gap structure is continued-fraction-controlled, which is the reason
an O(log) evaluation of the lag-sums is possible at all.