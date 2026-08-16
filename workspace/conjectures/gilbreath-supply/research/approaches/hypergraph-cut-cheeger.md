# Hypergraph cut / isoperimetric reformulation: Φ as the parity coboundary of a connected hypergraph

```approach
idea: Read Φ_n as the mod-2 incidence matrix of a concrete hypergraph on n vertices
      (vertex j = window position), with hyperedge d = {n−1−d+o : o ⊆ d} (a translated
      digital down-set), for d ∈ [0,n−1]. Then T(n,d) = ⊕_{v ∈ hyperedge d} h_v is the
      parity of the prime gap-parity labels across that hyperedge, and ν₂(n) = the number
      of hyperedges of odd label-parity — the *cut size* of the labelling h in the fixed
      hypergraph. SUPPLY becomes: the prime labelling cuts a linear fraction of the
      hyperedges of this one fixed, number-theory-free hypergraph.
mechanism: (REFUTED — premise false, see killed-by.) This mechanism read the fold as a
      hypergraph coboundary and claimed ker Φ_n = span(all-ones), nullity 1, ⟺ connectivity.
      Both the claimed kernel and the connectivity interpretation are false (d=0 singleton
      edge; operative kernel span(even-alt, odd-alt)). The cut-size reading of ν₂(n) is
      still literally true (T(n,d) is the parity of h over hyperedge d), but the
      isoperimetric route it was meant to open is closed.
      For the record, the original text was: "The known fact 'ker Φ_n = span(all-ones),
      nullity 1' has a new meaning here: it is exactly hypergraph connectivity (the only
      labellings h with every hyperedge even are h ≡ 0 and h ≡ 1)."
status: refuted

killed-by: >
  hypergraph-coboundary-false-premise (this note, below). The approach's mechanism
  builds on "ker Φ_n = span(all-ones), nullity 1 ⟺ the fold's hypergraph is
  connected (the only labellings h with every hyperedge even are h ≡ 0 and h ≡ 1)".
  That premise is false on two independent counts:

  (1) On the approach's OWN row range d ∈ [0, n−1], the hyperedge d=0 is the
      singleton {n−1} (its down-set is {0}, giving T(n,0) = h[n−1] alone), so row
      d=0 forces h_{n−1} = 0. The all-ones vector is therefore NOT in the kernel
      of the d∈[0,n−1] matrix. Hand-checked for n=4: rows [0,0,0,1], [0,0,1,1],
      [0,1,0,1], [1,1,1,1]; only h≡0 has every row even, so the kernel is {0},
      nullity 0, not span(all-ones). The approach asserts both "d ∈ [0,n−1]" and
      "ker = span(all-ones)", which are mutually contradictory.

  (2) Even on the operative rows d ∈ [2, n−1] (where all-ones IS in the kernel),
      the kernel is 2-dimensional, ker = span(even-alt, odd-alt), NOT span(all-ones)
      (fold-rank-is-n-2-nullity-2-alternating, machine-verified). So "connectivity
      ⟹ only 0 and all-ones cut evenly" is false for this hypergraph: the even-cut
      labellings are the parity-class-constant ones (a on even indices, b on odd),
      a richer family than graph connectivity predicts. This is because hyperedges
      of size > 2 (e.g. d=3 gives the 4-edge {0,1,2,3}) impose ONE sum-parity
      constraint, not the pairwise-equal constraints a 2-uniform graph would require.

  The mechanism's central reinterpretation ("the one structural fact is connectivity,
  so the even-cut labellings are only 0 and all-ones") collapses under the corrected
  rank. No isoperimetric/Cheeger conclusion that global non-constant even cuts are
  forbidden survives.

first-step: (closed by the above) the explicit d=0 singleton edge, hand-computed;
  and the operative-range kernel span(even-alt, odd-alt), machine-verified n=2..20.
```

## Provenance

- Established here: `T(n,d) = ⊕_{o⊆d} h[n−1−d+o]` is by definition the parity of h over
  the translated down-set `{n−1−d+o : o⊆d}`, so Φ_n is literally that hypergraph's
  incidence matrix. **Correction (kills the approach).** The claim "ker = span(all-ones)
  ⟺ connected, i.e. the only even-cut labellings are 0 and all-ones" is false for this
  fold: (1) on the d∈[0,n−1] row range the d=0 singleton edge {n−1} forces h_{n−1}=0, so
  all-ones is NOT in the kernel there; (2) on the operative d∈[2,n−1] range the kernel is
  2-dimensional, span(even-alt, odd-alt) (fold-rank-is-n-2-nullity-2-alternating), not
  span(all-ones). Hyperedges of size > 2 impose one sum-parity constraint per edge, not
  the pairwise-equality constraints that make "connected ⟹ only global constants cut
  evenly" true for graphs. The approach is therefore refuted; recorded with this note's
  killed-by block.
- Named mathematics actually used: hypergraph incidence matrix, hypergraph cut function
  (odd-intersection), hypergraph connectivity, Cheeger / isoperimetric inequalities.
- **Speculative part:** that a Cheeger-type lower bound holds for this specific,
  wildly inhomogeneous hypergraph (edge sizes range from 1 to n), and that the prime
  switch-set A has the needed volume balance. Unchecked — and now moot for the mechanism
  as stated, since the connectivity premise it rested on is false.

## Research verdict (literature side)

The refutation above is correct, and the topology literature reinforces it from
an independent direction — a Cheeger-type lower bound was never going to fire
here even had the kernel premise held:

- Hypergraph Cheeger inequalities exist but are **k-uniform**: Mulas *A Cheeger
  Cut for Uniform Hypergraphs* (DOI 10.1007/s00373-021-02348-z), Banerjee, Xu–Zhou
  all state their bounds for k-uniform hypergraphs. The fold's hypergraph has
  edge sizes 1, 2, 4, … (one edge of each size up to a power of 2 — wildly
  non-uniform), so none of their hypotheses holds. The strongest non-uniform
  results (Lau–Tung–Wang, arXiv:2211.09776, reweighted eigenvalues) pay a
  `log r` factor in the maximum hyperedge size r — and here r ≈ 2^{log n} = n,
  so `log r ≈ log n` swallows the linear target. That is precisely the
  mechanism the approach would need, and it is degenerate in this range.
- Any Cheeger lower bound on cut size requires a volume/balance input on the
  labelling — and the fixed hypergraph is violently volume-imbalanced (vertices
  near the window centre sit on Θ(n) hyperedges, the ends on O(log n)), so the
  Cheeger constant h(Γ) is of order ~1/n and `min{vol(A), vol(V∖A)}` can be made
  tiny for any A concentrated in the low-degree ends — precisely where the
  switch-set concentrates. A Cheeger-type bound could not exceed the trivial
  w/… scaling the closed doors already forbid.
- The fold is the *parity* (mod-2 incidence) operator, where the "cut" counts
  odd-intersection hyperedges; the spectral-cut literature is written for real
  Laplacians and symmetric positive operators, not an F₂ coboundary. The mod-2
  transfer is not in any source found.

So the false kernel premise is not merely a defect in the wording — even
corrected, the hypergraph is exactly the case (non-uniform, volume-imbalanced,
F₂-parity) where the loaded machinery provably degenerates. Refutation stands on
both independent grounds.

Sources: Mulas (10.1007/s00373-021-02348-z); Banerjee; Xu–Zhou note
(S0166218X25004329); Lau–Tung–Wang arXiv:2211.09776; Ikeda–Miyauchi–Takai–
Yoshida arXiv:1809.04396; CIT06 (Laplacian eigenvalues, partition/coboundary
bounds, DOI 10.1016/j.laa.2008.06.034).

## Why it is distinct

This was the *topological / isoperimetric* route: it read Φ as a hypergraph coboundary
and converted the goal into a cut size in a fixed hypergraph. The cut-size reading of
ν₂(n) is literally correct, but the approach is **refuted**: its load-bearing premise
(ker = span(all-ones), nullity 1, ⟺ hypergraph connectivity) is false under the corrected
rank, both on the d∈[0,n−1] row range (d=0 singleton edge) and on the operative d∈[2,n−1]
range (kernel = span(even-alt, odd-alt)). It is kept here as a recorded dead end so the
next attempt does not re-derive it.

The full claim block for this refutation lives in `research/notes/hypergraph_cut_refutation.md` (`hypergraph-coboundary-false-premise`), so it reaches CLAIMS.md once.

