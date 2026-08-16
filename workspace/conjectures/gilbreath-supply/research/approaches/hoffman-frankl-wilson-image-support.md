# Image support vs the disjointness graph (Hoffman / Frankl–Wilson)

```approach
idea: Reformulate SUPPLY's excess S(n) = Σ_{d=2}^{n−1} (−1)^{a_d} as an extremal
statement about the image support D = {d : a_d = 1} inside the "disjointness
graph" G_n on the rows, where d ~ d' iff d ∧ d' = 0. The fold's Gram matrix over
F₂ is exactly the disjointness matrix, so the structure of the row family is the
structure of the orthogonality/disjointness graph, and the bias of the image
column can be attacked by Hoffman's eigenvalue bound and by Frankl–Wilson /
Kleitman-type linear-algebra independence bounds.

mechanism: The load-bearing identity is (Φ_n Φ_n^T)[d,d'] = |R_d ∩ R_d'|
mod 2, where R_d = {n−1−d+o : o⊆d}. Hand-verification in this proposal round
(d,e = 2..7 and 9..10 pairs, over 10 cases) suggests the EXACT form
|R_d ∩ R_e| = 2^{popcount(d∧e)} (so the parity is 1 iff d∧d'=0): e.g. d=3,e=4
give intersection {n−1} of size 2^0=1; d=6,e=5 give {n−5,n−1} of size 2^1=2;
d=7,e=7 give size 2^3=8. If this exact identity holds (it is the "two Lucas
rows overlap in a translate of the down-set of their bitwise AND" fact,
machine-checkable for all n), the Gram matrix is EXACTLY the disjointness
matrix J[d,d'] = [d∧d'=0]. The excess is the bias of the
image column: S(n) = (n−2) − 2·wt(Φ_n h) = Σ_d (−1)^{a_d}. So SUPPLY is the
statement that the specific column of the Hadamard/character matrix realised by
the prime h is not "almost constant". The graph G_n = disjointness graph on
{2,...,n−1} has known spectral structure (it is the orthogonality graph of the
Boolean lattice: independence number and eigenvalues are classical, via
Frankl–Wilson / Kleitman / the Grassmann trick). Candidate theorem to seek: if h
has both kernel coordinates o(n) — ⟨h, even-alt⟩ = o(n) and ⟨h, odd-alt⟩ =
o(n), i.e. h is balanced on even and odd positions — then the image support D
cannot be a small subset, because a small D would force the column to concentrate
on a large independent-ish subfamily of the disjointness graph, contradicting the
known independence number. CORRECTION (made before research, this proposal round): the claim that
Siegel–Walfisz makes the kernel coordinates o(n) is FALSE, hand-verified here.
Since h_j = [q_j ≢ q_{j+1} mod 4] = (1 − χ(q_j)χ(q_{j+1}))/2, both kernel
coordinates ⟨h, even-alt⟩ = Σ_{even j} h_j and ⟨h, odd-alt⟩ = Σ_{odd j} h_j are
PAIR statistics (adjacent-index products χ(q_j)χ(q_{j+1}) restricted by parity),
not one-point statistics. So "balanced kernel coordinates" is a parity-split
switch density, and one-point Siegel–Walfisz does NOT control it. The honest
input is pair-level; the route must therefore do the work with the DISTRIBUTION
of the image column, not with the two kernel bits.

falsifier (already fired for the naive form): Thue–Morse is balanced on BOTH
parity classes (even and odd positions each carry a shifted Thue–Morse, so
kernel coordinates ≈ n/4 each) yet has sublinear ν₂. So any mechanism that only
uses "kernel coordinates far from {0, n/2}" is dead — Thue–Morse is the witness.
The route is live only if the Hoffman/Frankl–Wilson step uses the DISTRIBUTION of
the image column (not just the two kernel bits) — the first step checks exactly
this, and Thue–Morse is the negative control that must FAIL the certificate.

status: refuted
killed-by: >
  The direction of application to the disjointness graph is wrong. By Hoffman's
  bound the independence number of the disjointness graph on the row indices
  (edges d~e iff d∧e=0) is LARGE — an independent set is a pairwise-INTERSECTING
  family of subsets of the digit set, of maximum size 2^{n-1} (whole-set
  families), comparable to the total row count. So "a small image support D
  contradicts the independence number" fires the wrong way: even a countably
  small upper bound permits D as large as half the cube, and SUPPLY wants
  |D|=wt(Phi_n h)≥c·n to be LARGE. Frankl-Wilson's |F|≤n^s bound governs
  uniform k-subsets of an n-set with restricted intersection SIZES; the rows are
  not uniform-weight and the prime-k congruence hypotheses do not transpose. The
  falsifier already fired: Thue-Morse is balanced on both parity classes (kernel
  coordinates ~n/4 each) yet has sublinear nu2, so any kernel-bit mechanism is
  dead, and the "use the distribution of the image column" hedge is not supplied
  by any source. The load-bearing Gram identity |R_d∩R_e|=2^{popcount(d∧e)} is a
  real, ALREADY-PROVED in-workspace claim (downset-row-intersection-meet-formula,
  M_d∩M_d'=M_{d∧d'}), so Φ_nΦ_n^T is indeed the disjointness matrix — but it is
  inert: surjectivity (rank n−2) makes the image support unconstrained by that
  Gram matrix. Engines real; application direction wrong.
precedent:
  - "Ellis, Intersection Problems in Extremal Combinatorics, arXiv:2107.06371,
    Theorem 2.7 (Frankl-Wilson 1981): for p prime, k<=n, lambda_i in {0}∪[1,p-1]
    all ≡ k (mod p), if distinct S,T in F ⊆ [n]^k have |S∩T|≡lambda_i (mod p)
    for some i then |F|<=n^s."
  - "Frankl-Rödl, Forbidden intersections, Trans. AMS 1987, DOI
    10.1090/s0002-9947-1987-0871675-6."
  - "Albertson et al., Distinguishing orthogonality graphs, J. Graph Theory, DOI
    10.1002/jgt.22704 (orthogonality graph of the cube, spectrum via Krawtchouk)."
  - "Jenssen-Malekshahian-Park, On Dedekind's problem... and antichains of a
    given size, DOI 10.1112/jlms.70624 (Boolean-lattice independent/antichain
    structure)."
  - "In-workspace: excess-is-negative-character-sum (checked),
    fold-rank-n-minus-2-binomial-proved (proved)."
first-step: (a) tool_builder: compute the two kernel coordinates ⟨h, even-alt⟩,
⟨h, odd-alt⟩ for the prime h as functions of n ≤ 20000 and confirm both are o(n)
(measurement to fix constants, theorem is Siegel–Walfisz); (b) compute the
eigenvalues and independence number of the disjointness graph on rows {2..n−1}
for n ≤ 64, and check whether Hoffman's bound evaluated at the empirical |S(n)|
is informative (non-vacuous); (c) run the SAME certificate on the Thue–Morse and
balanced anti-dyadic controls — if they also satisfy it, the candidate is dead
before any theory is spent. Negative control: all-ones has kernel coordinate n
and must FAIL the certificate.
```
