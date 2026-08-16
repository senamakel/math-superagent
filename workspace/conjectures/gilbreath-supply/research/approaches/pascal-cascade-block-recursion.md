# Self-similar block recursion (dyadic cascade) for the fold weight

```approach
idea: Exploit the Sierpinski self-similarity of the Pascal matrix mod 2 to decompose
      Φ_{2n} and Φ_{2n+1} into copies of Φ_n plus explicit shift/cross terms, and turn
      ν₂(n) = wt(Φ_n h) into a dyadic recursion whose cross term is a lower-order
      correlation. SUPPLY then reduces to controlling that cross term on average over
      dyadic scales — a cascade / renewal argument rather than a per-n bound.
mechanism: Pascal mod 2 is the Kronecker power of [[1,1],[1,0]] (the Sierpinski
      triangle; Hofer's Lemma 1 and Bacher's LU/determinant results on disk already
      record the full-matrix self-similarity). Φ_n is an anti-diagonal slice with entries
      C(k−1, j−(n−k)) mod 2, so it inherits a 2×2 block recursion in n. Writing
      wt(Φ_{2n} h) and wt(Φ_{2n+1} h) in terms of wt(Φ_n h') for shifted/truncated h
      isolates a single "boundary overlap" term. If that term is O(n^{1−ε}) on average
      (a variance/autocorrelation statement on h, the exact kind GOAL.md priority 2 wants
      to price), the recursion propagates a linear lower bound from every dyadic scale to
      the next, giving SUPPLY on a density-1 set of n by Chebyshev. This is a different
      object from the 2-regular automaton route: here we track the scalar ν₂(n) through a
      dilation recurrence, not a finite-state linear representation of the generating
      function.
status: refuted

killed-by: >
  The Sierpinski self-similarity lives on rows/blocks/triangular regions, NOT on
  the anti-diagonal slice Phi_n that SUPPLY uses (Cardell–Fuster-Sabater: the
  diagonals are binomial sequences, 2-regular generators; the correct home is the
  already-refuted diagonal-2regular-automaton route). No source supports a 2x2
  weight-block recursion on the slice, and the literature gives no reason to
  expect a small cross term. Refuted as a distinct route; the dyadic structure it
  sought is already housed in the 2-regular formulation on disk.

precedent: >
  Cardell–Fúster-Sabater, *Binomial Representation of Cryptographic Binary
  Sequences*, 10.1155/2019/2108014 (Sierpinski diagonals = binomial sequences,
  2-regular generators); Rowland arXiv:1001.1783 (Fine a2(n)=2^popcount(n));
  Northshield hdl.handle.net/1951/69939; Kubelka 10.1080/00150517.2004.12428445;
  Barbé 10.1016/s0166-218x(00)00211-0; Gamelin–Mnatsakanian 10.5565/publmat_49205_04.
  Reproduces hofer-mod2-pascal-thue-morse-structure, bacher-pascal-det-mod2
  (full-matrix block/LU self-similarity only).

## Research verdict (grounding check)

**The crux — "Φ_n is an anti-diagonal slice, so it inherits a 2×2 block
recursion in n" — is exactly wrong, and grounded in the literature.** P1 is an
anti-diagonal *slice* of the Pascal-mod-2 infinite matrix, and the Sierpinski
self-similarity lives on *blocks*, not slices. Precedent naming this precisely:
- Cardell–Fúster-Sabater *Binomial Representation of Cryptographic Binary
  Sequences* (10.1155/2019/2108014): the diagonal sequences of the Sierpinski
  triangle are exactly the **binomial sequences**, and every period-2^m binary
  sequence is an XOR of binomial sequences. The diagonals are *generators of a
  2-regular family*, not self-similar blocks — the natural recursion they carry
  is the **2-regular** (dilation) one, which is precisely the
  `diagonal-2regular-automaton` route this candidate claims to be distinct from.
- Northshield *Sums across Pascal's triangle modulo 2*: the (1,1)-diagonal sum
  b_n counts hyperbinary representations and satisfies `B(x) = (1+x)…` type
  functional equations — again the correct structural home is 2-regular /
  generating-function, not a weight-block recursion.
- Fine's theorem (`a₂(n) = 2^{popcount(n)}`) and Rowland's generalization
  (arXiv:1001.1783) give the *row-weight* self-similarity — the row is a 2×2
  Kronecker block, the anti-diagonal is not.
- Kubelka / Barbé / Gamelin–Mnatsakanian: the mod-2 Pascal self-similarity is a
  block-replacement (substitution/IFS) recursion on *triangular regions*; an
  anti-diagonal cut of the whole triangle is a self-intersecting line through
  these regions, so a clean 2×2 block recursion in n would require the slice to
  respect the fractal boundary, which it does not.

**Consequence for the cascade.** There is a well-founded *dyadic/cascade*
literature — but it is the 2-regular / substitution / binomial-sequence
structure that already exists on disk as `hofer-mod2-pascal-thue-morse-structure`,
`bacher-pascal-det-mod2`, and the `diagonal-2regular-automaton` candidate. The
specific claim here — that `wt(Φ_{2n} h)` and `wt(Φ_{2n+1} h)` admit a recursion
in terms of `wt(Φ_n h')` with a single small cross term — is not supported by any
source found; anti-diagonal slices do not carry 2 uniformly scaled copies of
Φ_n. The recursion would have to be *derived from scratch* (its speculative
half), and the literature gives no reason to expect the cross term to be
o(n^{-ε}).

Sources / precedent: Cardell–Fúster-Sabater, *Binomial Representation of
Cryptographic Binary Sequences*, 10.1155/2019/2108014 (Sierpinski diagonals =
binomial sequences, 2-regular generators); Rowland arXiv:1001.1783 (Fine
a₂(n)=2^popcount(n), row-weight); Northshield hdl.handle.net/1951/69939;
Kubelka 10.1080/00150517.2004.12428445; Barbé 10.1016/s0166-218x(00)00211-0;
Gamelin–Mnatsakanian 10.5565/publmat_49205_04. On-disk claims reproduced:
hofer-mod2-pascal-thue-morse-structure, bacher-pascal-det-mod2 (full-matrix
block/LU self-similarity only).

**Verdict.** Block recursion is *grounded* for the full Pascal matrix (rows),
reproducing `hofer-mod2-pascal-thue-morse-structure`; it is *ungrounded* for the
anti-diagonal slice Φ_n that SUPPLY actually uses. The dyadic hope is better
housed in the 2-regular/binomial-sequence formulation already on disk than as a
new weight-block recursion. If pursued, the first step must derive the block
recursion of Φ_n itself (the file's own first-step) before any averaging — that
derivation, not the literature, is the gate.

first-step: Compute Φ_n over F₂ for n = 2..64 and derive (or fit) the exact block
      decomposition Φ_{2n} and Φ_{2n+1} in terms of Φ_n, a shift operator, and a rank-2
      cross block; write down the resulting recurrence for ν₂(2n), ν₂(2n+1), and verify
      it against the oracle's ν₂(n) for the prime h on n ≤ 200.
```

## Provenance

- Grounded in the self-similarity of Pascal mod 2 (Sierpinski gasket / Kronecker-power
  structure), which the library already holds in `hofer-mod2-pascal-thue-morse-structure`
  and `bacher-pascal-det-mod2` — but those concern the full square matrix's determinant
  and LU, not the fold slice Φ_n's block recursion for the *weight*.
- **Speculative part:** that the anti-diagonal slice Φ_n has a clean block recursion
  (unchecked), and that its cross term is provably small from a second-moment/autocorrelation
  input on h. Unchecked; the block recursion itself is the first thing to establish.

## Why it is distinct

This is the *fractal / dyadic-cascade* route: a recurrence on the single scalar ν₂(n)
under n ↦ 2n, 2n+1. It differs from `diagonal-2regular-automaton` (which builds a
finite automaton for the bivariate generating function) and from `walsh-subset-sum-fold-structure`
(which Fourier-analyses Φ). It directly targets GOAL.md priority 1 (the averaged/density-1
form), because a dyadic recursion with a small cross term is precisely what a Chebyshev
averaging can consume.
