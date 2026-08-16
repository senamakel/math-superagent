# Tensor/bit-splitting of the F2 zeta transform: a doubling identity for Phi_n

```approach
idea: >
  Replace the FALSE substitution/self-similarity rules that killed
  substitution-incidence-perron and pascal-cascade with the one self-similarity
  the F2 zeta transform genuinely HAS: block decomposition by the top bit. The
  submask map d -> 1_{M_d} is a slice of the zeta matrix Z over {0,1}^{m+1},
  and Z_{m+1} is the lower-triangular 2x2 block matrix [ Z_m, 0 ; Z_m, Z_m ]
  (the standard tensor structure of the subset lattice). This yields an EXACT
  identity expressing wt(Phi_{2n} h) as wt(Phi_n h_lo) + wt(Phi_n h_hi) plus
  explicit cross terms, where h_lo, h_hi are the two halves of the switch string.
  The cross terms are the only coupling, and they vanish in expectation whenever
  the two halves are "independent". The arithmetic input is then SHORT-MEMORY /
  local randomness of the prime switch sequence — measurable for the primes
  (gaps are locally random, density 0.585), violated by every closed-door
  witness (all of which are globally structured), and strictly weaker than
  proving the adjacent mod-4 switch density.
mechanism: >
  Named structure: the F2 zeta (submask) transform is self-inverse and splits
  under bit-append as the 2x2 block matrix above; the fold Phi_n is the slice of
  Z obtained by taking rows d in [2,n-1] of the reflected window. Doubling n
  appends one bit to the window coordinate, so Phi_{2n} decomposes into two
  copies of Phi_n acting on the two halves, plus cross rows d in [n, 2n-1] whose
  downsets straddle the halves. The cross term has an exact closed form in terms
  of the meet formula (claim downset-row-intersection-meet-formula), and its
  F2/character expectation factors over the halves. Thus wt(Phi_{2n} h) >=
  wt(Phi_n h_lo) + wt(Phi_n h_hi) - |cross|, with |cross| a deterministic count
  that is small under a stated independence hypothesis on the halves. This is NOT
  a renormalization group (no fixed point is claimed) and NOT a false 2x2 weight
  block recursion on the slice: it is the exact tensor decomposition of the full
  transform, verified cell-by-cell against the oracle first. The doors die here
  because all-ones, Thue-Morse, and the anti-dyadic witnesses have their two
  halves PERFECTLY correlated (the cross term is maximal), while the prime switch
  sequence has rapidly decaying window correlations (measured).
status: refuted
killed-by: >
  Refuted on evidence, not on absence. (1) THE HOME OF THE GENUINE SELF-SIMILARITY
  IS NOT THE SLICE Phi_n. The block identity Z_{m+1} = [ Z_m, 0 ; Z_m, Z_m ] is
  real, but it is a property of the FULL zeta matrix on the whole {0,1}^{m+1}
  cube of submasks — the same Pascal-mod-2 block self-similarity documented by
  Callan (Sierpinski's triangle and the Prouhet-Thue-Morse word,
  arXiv:math/0610932, Thm 1: S^{-1} is a (-1,0,1)-matrix with Thue-Morse sign
  pattern), Bacher-Chapman (Symmetric Pascal matrices modulo p, EJC 22 (2003),
  autosimilar LDU), and Kubelka (Self-similarity and symmetries of Pascal's
  triangles mod p, 2004). SUPPLY's object is the ANTI-DIAGONAL SLICE Phi_n
  (rows d in [2,n-1] of a reflected window), and the library has ALREADY closed
  this exact category error twice: pascal-cascade-block-recursion (refuted: "The
  Sierpinski self-similarity lives on rows/blocks/triangular regions, NOT on the
  anti-diagonal slice Phi_n that SUPPLY uses") and substitution-incidence-perron
  (refuted: the claimed slice recursion T(2n,2d)=T(n,d) fails because doubling
  reads even-offset vs consecutive-offset data of the same h). Doubling n does
  not map the fold's slice onto two copies of itself; the block identity
  describes the index-cube submask structure, which is a different object from
  the fold's row-window structure. The candidate's "verified cell-by-cell"
  would, when checked, reduce to the already-refuted substitution incidences.
  (2) THE DEMAND RE-PRICES SWITCH DENSITY. "Two halves independent => cross =
  o(n)" is a short-memory / local-randomness input on the switch string, i.e.
  exactly the object GOAL priority 2 prices; and the per-scale second-moment
  refinement shows any per-scale/local correlation input collapses back to the
  g=0 switch-density scale (per-scale-refinement-collapses-to-switch-density).
  So even where the identity were exact, the price does not weaken toward "see
  more, demand less" — it re-prices the known barrier. (3) NO SOURCE APPLIES
  THE TENSOR/BLOCK DECOMPOSITION TO A WEIGHT LOWER BOUND FOR THE SLICE;
  Callan/Bacher-Chapman/Kubelka are structural facts about the full matrix, none
  bearing on wt(Phi_n h) for a fixed prime gap-parity string.
precedent: >
  Block self-similarity of the full zeta / Pascal-mod-2 matrix (real, precisely
  stated, wrong object): Callan, arXiv:math/0610932, Thm 1 (S^{-1} has the same
  zero pattern, Thue-Morse sign pattern); Bacher-Chapman, "Symmetric Pascal
  matrices modulo p", Eur. J. Combin. 22 (2003) DOI 10.1016/e2003.06.001
  (autosimilar matrices, LDU factorization); Kubelka, "Self-similarity and
  symmetries of Pascal's triangles mod p", 2004 DOI 10.1080/00150517.2004.
  12428445. In-workspace (established): substitution-incidence-rules-false
  (the slice recursion fails); pascal-cascade-block-recursion (refuted, same
  object mismatch); per-scale-refinement-collapses-to-switch-density (the price);
  downset-row-intersection-meet-formula (the exact meet/cross machinery, which
  does NOT stay small under local randomness in the way the route needs).
falsifies: >
  Closed by the object-mismatch ground: an exact weight-doubling identity on the
  slice would contradict the already-verified substitution-incidence failure
  unless the two halves assumption carries content, which is the re-priced
  switch/local-randomness input. A reopening must first exhibit the slice
  doubling identity cell-by-cell against the oracle without assuming half-
  independence — none of the located tensor literature supplies it.
```

## Grounding note (research pass, this dossier)

The block decomposition Z_{m+1} = [ Z_m, 0 ; Z_m, Z_m ] is a genuine, correctly
stated identity for the full submask/zeta matrix (Callan, Bacher-Chapman,
Kubelka agree). But "the fold Phi_n is a slice of Z" does not make Phi_n block-
recursive in n — the block structure lives on the full index cube, not on the
anti-diagonal row-window slice, and this is the exact category error the
library already recorded twice (pascal-cascade, substitution-incidence). The
price (independent halves) is local randomness / switch density re-imported.
Verdict: refuted.
