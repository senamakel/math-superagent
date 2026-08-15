```approach
idea: affine-weyl-alcove-walk-crystal
mechanism: |
  Two established facts suggest the whole coupled system is a single object from
  the representation theory of the affine Weyl group of type A1 (the infinite
  dihedral group), and the run has never taken this reading.

  (1) INTRUDER = ALCOVE WALK. The proved descent/absorption lemma
      x_s = |x_{s-1} - c_s|, c_s in {0,2}, is a walk in the fundamental alcove of
      the affine Weyl group W_tilde(A1). The two simple reflections of W_tilde(A1)
      act on the line by s_0 : x -> -x and s_1 : x -> 2 - x; the map x -> |x - 2|
      on x >= 0 is exactly s_1 on [0,2] and a translate-by-2 for x >= 2, i.e. an
      affine reflection/fold. The step "c_s = 0 does nothing, c_s = 2 folds by 2"
      is a word in these affine reflections, and the absorbing set {0,2} is the
      orbit of the fundamental alcove's walls. Alcove-walk theory (Ram 2006,
      "Alcove walks, Hecke algebras, spherical functions, crystals and
      Macdonald polynomials") gives EXACT combinatorial formulas for walks and
      their endpoints in terms of affine Weyl group data.

  (2) BLOCK INTERIOR = BRANCHING/CRYSTAL. Inside the {0,2} block the halved
      entries evolve by XOR = Pascal mod 2 = Sierpinski (proved, rule90-interior-xor).
      Pascal's triangle mod 2 IS the branching multiplicity structure of sl(2)
      (Lucas' theorem / Kummer's theorem = the Clebsch-Gordan branching rules),
      which is exactly the crystal/lattice structure whose weight words are the
      binary edge readouts.

  The synthesis: couple (1) and (2). The intruder descends against the edge
  pattern c_s in {0,2}, and the edge pattern is the binary readout (weight word)
  of the block's sl(2)-crystal under branching. So "does the intruder reach the
  absorbing alcove {0,2}?" is the question "does the weight word of the block's
  crystal drive the intruder's alcove walk into the fundamental alcove?" — one
  statement about a single affine-crystal object, not two unrelated processes.
  The conjecture is then the statement that this alcove-walk/crystal pair never
  leaves the safe chamber.

  The named mathematics is real and untouched by this run: affine Weyl groups,
  alcove walks and their Hecke algebra, Kashiwara crystals, Lucas/Kummer as
  branching. It is distinct from vectorial-subtractive-euclidean (which needed a
  simplex/renormalisation that does not exist — here the folds are exact 1-D
  affine reflections, no normalisation is claimed) and from odometer-disjointness
  (which imported entropy/rigidity for a subshift — here the odometer-like folds
  act on the intruder value itself, directly from the proved descent lemma).
status: refuted
killed-by: |
  Refuted by the candidate's OWN falsifier (step b: "if nu2 has no named
  alcove-walk/crystal counterpart, the bijection is bookkeeping"). The probe fires
  decisively:
  (1) RANK-1 COLLAPSE. W_tilde(A1) is the infinite dihedral group; the descent
      lemma x_s = |x_{s-1} - c_s|, c_s in {0,2}, is a genuine 1-D alcove walk (fold
      against 2 = affine reflection s_1: x -> 2 - x; c_s = 0 is a no-op). But in
      rank 1 the alcove-walk algebra's only nontrivial statistic is the number of
      wall hits of each reflection type — here the single type s_1, applied nu2
      times — combined with the starting value v. That is LITERALLY the already-proved
      biconditional v <= 2*nu2 + 2 (lemma54-descent-lean-formalised, kernel-checked).
      The alcove-walk statistics that carry real content (Hall-Littlewood / weight-
      space support, spherical functions) are higher-rank / higher-weight objects;
      A1 has a single simple root and none of that.
  (2) RATE = OPEN CONTENT. The drain/regeneration rate — how often the c_s = 2 steps
      (wall hits) arrive — is exactly the open G-supply / regeneration question, the
      same content that refuted vectorial-subtractive-euclidean (return-rate question
      = open regeneration rate in new variables). Alcove-walk / crystal theory carries
      no handle on the rate. No source applies alcove walks, affine crystals, or Hecke
      combinatorics to the iterated absolute-difference / Ducci / Gilbreath problem
      (searched several angles; the Ducci literature is periodicity/cyclotomic —
      Breuer 2010, Lewis-TeFFT 2024 — and never representation-theoretic).
  (3) CRYSTAL HALF DOES NOT COUPLE. The block interior = Pascal mod 2 = sl2 branching
      (Lucas) is the STATIC Sierpinski interior; no source couples it to the intruder's
      drain. The dictionary is exact (affine reflection + Lucas) but reproduces a proved
      lemma in representation-theoretic costume; the open direction is untouched. Same
      re-description pattern as vectorial-subtractive-euclidean (exact dictionary, no
      new bound, open rate restated).
precedent: |
  Framework named and real: Ram, "Alcove walks, Hecke algebras, spherical functions,
  crystals and column strict tableaux", Pure Appl. Math. Q. 2(4):963-1013 (2006),
  https://doi.org/10.4310/pamq.2006.v2.n4.a4; Parkinson-Ram 2008; J-folded alcove
  walk / MV-intersection literature. NOT applied to this problem anywhere (searched).
  Run: lemma54-descent-lean-formalised (the proved biconditional the rank-1 alcove
  statistics reduce to); vectorial-subtractive-euclidean (refuted re-description
  pattern).
first-step: |
  CLOSED BY REFUTATION — do not spend compute on the dictionary (steps a-b are exact
  by construction and re-derive a proved lemma; step c has no rank-1 content beyond
  the already-proved nu2). Recorded so the next round does not re-propose the
  affine-Weyl / crystal reading.
named-mathematics: affine Weyl group W_tilde(A1), alcove walks (Ram), Hecke
  algebra, Kashiwara crystals, Lucas/Kummer branching
falsifier: >
  The dictionary (a)-(b) is exact and cannot fail (it re-derives a proved lemma
  in new coordinates). The approach dies if step (c) shows the edge pattern is
  NOT a genuine weight word of a known crystal — i.e., the two halves couple
  only superficially and the affine-crystal object does not bound nu2 or the
  drain rate. Step (b)'s statistic match is the decisive probe; if nu2 has no
  named alcove-walk/crystal counterpart, the bijection is bookkeeping.
side: general-class / dynamical, with representation theory as the certifying
  structure
```
