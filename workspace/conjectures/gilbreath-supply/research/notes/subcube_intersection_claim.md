# Downset-row intersection/distance formula established

```claim
id: downset-row-intersection-meet-formula
statement: >
  For d,d' in [2,n-1], the fold rows satisfy M_d ∩ M_d' = M_{d∧d'}, hence
  |M_d ∩ M_d'| = 2^{pc(d∧d')} and
  |M_d △ M_d'| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d∧d')+1}, where M_d =
  {n-1-d+o : o ⊆ d}.
hypotheses: Relection x ↦ n-1-x is a bijection M_d → ↓d (digital down-set),
  and ↓d ∩ ↓d' = ↓(d∧d') in the Boolean lattice.
holds-here: Yes for every n, d, d' — the identity is the meet-semilattice
  structure of downsets carried through the reflection; no hypothesis on the
  prime string h is used and none is needed.
status: proved-by-derivation (all-n bijection: reflection x ↦ n-1-x maps M_d onto
  the down-set ↓d; down-sets intersect by AND). Machine verification pending in
  code/librarian/verify_downset_intersection.py (n=8..256, brute submask
  enumeration + negative control). Scholar's independent machine route:
  code/scholar/downset_verify.py (n=4..199, all pairs; checks meet, intersection
  size, and symdiff size, plus a random same-size set-family negative control
  that proves the pass is not vacuous). Derivation to ALL n is in
  research/notes/scholar_intersection_formula.md. Not a proof of SUPPLY; it is
  the geometry lemma the adopted approach rests on.
bearing: Makes F_n(z) = Σ z^{|M_d△M_d'|} an exact n-local combinatorial count
  (popcount statistics of d,d',d∧d'), isolating the density-1 (averaged)
  form's arithmetic content as the single second-moment statement
  E[S(n)²]=O(n). A_2 = #dist-2 pairs reads the dyadic-lag autocorrelation of
  the switch sign u_j = s_j s_{j+1}.
anchor: research/notes/subcube_intersection_pricing.md
```

The formula is elementary and standard; the subcube-intersection literature
(Groenland, Melo–Winter, etc.) studies a different question (which cardinalities
generic affine flats can intersect), so the run already holds everything it
needs and no new source is licensed.
