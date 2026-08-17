# Cioabă & Mim — "On the homology groups of clique complexes of strongly regular graphs" (arXiv:2606.27328)

**Source:** https://arxiv.org/html/2606.27328v2 (v2, 16 Jul 2026; also viewed as
`cioaba-mim-clique-homology-srg.full.md`). Full text:
`research/sources/cioaba-mim-clique-homology-srg-html.full.md`.
Companion/foundation paper: Cioabă–Guo–Ji–Mim, *Clique complexes of strongly
regular graphs, their eigenvalues, and cohomology groups*, LAA 730 (2026),
152–197 (arXiv:2508.05871) — cited here as [6]; only its landing page is in the
library, its content is carried by this paper which cites it. [[cioaba-mim-clique-homology-srg-html.full]]

## What it establishes

**Definition.** H₁(Cl(G), F) = 0 ⟺ the cycle space of G over the field F equals
the span of the signed boundaries of the triangles of G (kernel of δ₀ᵀ equals
image of δ₁ᵀ in the edge space of the clique complex).

**Vanishing criterion, characteristic-free (Thm 2.10).** If G is a graph in
which every induced cycle of length ≥ 4 has four consecutive vertices with a
common neighbor, then H₁(Cl(G), F) = 0 over every field F. Proof is elementary
cycle surgery (induction on cycle length); no inner product, valid in any
characteristic.

**SRG reduction (Thm 2.11).** For a strongly regular graph it is enough that
every induced cycle of **length 4 or 5** has four vertices with a common
neighbor. (Uses μ>0: for an induced C=(v₁..v_ℓ), v₁≁v₄ so the μ=2-type
common-neighbor argument supplies the surgery vertex.)

**Classification theorem (Thm 8.4).** If G is a strongly regular graph and
H₁(Cl(G), F) ≠ 0 over *some* field F, then G is one of:
1. the **Petersen graph** (10,3,0,1);
2. the **Shrikhande graph** (16,6,2,2);
3. an element of the **exceptional family E_m**, m ≥ 3, in Neumaier's
   classification (Theorem 8.1: any SRG with smallest eigenvalue −m is complete
   multipartite, or an OA(m,n) Latin-square graph LS_m(n), or a block graph of a
   Steiner system S(2,m,n), or the finite exceptional family E_m);
4. a **conference graph** (v,(v−1)/2,(v−5)/4,(v−1)/4) with **v ≤ 255**;
5. a **complete bipartite** K_{n,n} (2n,n,0,n);
6. a **lattice graph** L₂(n) = K_n □ K_n, (n²,2(n−1),n−2,2), n ≥ 3.

**Infinite-family dichotomy (Thm 8.5).** If (G_n) are pairwise-distinct SRGs and
H₁ ≠ 0 for each over some field, then either G_n is a lattice graph (n≥9)
infinitely often, or λ_min(G_n) → −∞.

**Conference graphs (Thm 6.7).** Every conference graph on v ≥ 256 = C₀′
vertices has H₁ = 0 over every field. (So only v ≤ 255 can have H₁ ≠ 0.)

**Least eigenvalue −2 (Thm 7.8).** Among SRGs with smallest eigenvalue −2
(Seidel's classification), the only ones with H₁ ≠ 0 over some field are C₄,
the Petersen graph, the Shrikhande graph, and the lattice graphs.

**Latin square graphs (Thm 3.12).** For L = LS(M), M a Latin square of order
n ≥ 5, over any field: H_i = 0 for i=1 and i≥3; dim H₂ = (n−1)³ − I(M), where
I(M) is the number of intercalates (2×2 Latin subsquares).

## Bearing on the run — an exact correction to a recorded claim

The gap note `research/backward/n3-positive-global.md` and pattern-finder round
33 state that the classification "already forces H₁ = 0 at 99". **That is
stronger than the source justifies.** Theorem 8.4 lists the exceptional family
E_m — *with smallest eigenvalue −m* — as an *allowed* position of nonvanishing
H₁. A putative (99,14,1,2) has λ_min = −4 = −m with m=4, so it falls in the
exception bucket of Theorem 8.1 (or is OA(4,n)/S(2,4,n)), NOT in a position the
theorem forces to have H₁ = 0. The classification does **not** rule out
H₁(Γ) ≠ 0 at 99: it says that if H₁ ≠ 0 then Γ ∈ E₄ (or the OA/Steiner family
for m=4). Since 99's existence is open, so is its H₁.

What *is* ruled out by the classification for (99,14,1,2):
- not the Petersen or Shrikhande graph (parameters);
- not complete bipartite (μ = 2 ≠ 0);
- not a lattice graph: the lattice-graph member with λ = 1 is L₂(3) = the
  9-vertex rook's graph (9,4,1,2), a *control*, not 99 (n² = 99 impossible);
- not a conference graph: 99 ≡ 3 (mod 4), so (v−5)/4 ∉ ℤ.

**The gate verdict rests on the controls, not the classification.** H₁ is
nonzero on BOTH controls — dim H₁ = 4 for rook(3) = L₂(3) (which is *on* the
classification list, item 6, so this is CONSISTENT with the theorem), and
dim H₁ = 1540 for bvls (243,22,1,2) (λ_min = −5, so the theorem's exception
bucket for m=5 also leaves this open). A homology *separator* needs 99 and 243
on opposite sides of "H₁ = 0"; both are nonzero. Refuted-on-arrival **as a
separator** — by the computed controls, per pattern-finder round 33
(`code/out/homology_controls.py`, `pf_h1_closed_form.py`) — not by the
classification forcing H₁(99) = 0.

**Independent consequence of the classification worth keeping.** The closed form
dim H₁ = 2T − v + 1 (= vk/3 − v + 1, from rho=1) predicted for 99 gives 364 ≠ 0.
That is *consistent* with Theorem 8.4 (E₄ is an allowed nonzero position), so it
contradicts nothing — but equally the theorem gives no obstruction. Both the
invariant's predicted value and the theorem's allowed-position list are
silent on whether a (99,14,1,2) exists.

## Contradiction / agreement with recalled memory

- **Agrees** with the pattern-finder round-33 verdict that the homology line is
  refuted as a 99-vs-243 separator (control computation).
- **Disagrees** with the recorded phrasing "the classification already forces
  H₁ = 0 at 99" (in `n3-positive-global.md`). The classification only lists the
  *allowed* nonzero positions; 99 falls in the unresolved E₄/exception bucket.
  This is a wording correction, not a change to the gate's conclusion (which
  already rests on the controls).

```claim
id: cioaba-mim-h1-classification
statement: For an SRG G, H1(Cl(G),F) != 0 over some field F implies G is the
  Petersen graph, the Shrikhande graph, a complete bipartite K_{n,n}, a lattice
  graph L2(n), a conference graph on <= 255 vertices, or an element of the
  finite exceptional family E_m (m >= 3) in Neumaier's classification. For
  srg(99,14,1,2) (lambda_min=-4) this leaves only the E_4 / OA(4,.) / S(2,4,.)
  exception bucket open; the classification does NOT force H1=0 at 99.
hypotheses: G strongly regular; H1(Cl(G),F) != 0 for some field F
holds-here: yes
status: asserted (sourced theorem, not re-proved)
bearing: the clique-complex homology line is refuted as a separator by the
  CONTROLS (H1 nonzero on both rook(3) and bvls), not by the classification;
  the exception bucket cannot be used to claim H1(99)=0
anchor: research/sources/cioaba-mim-clique-homology-srg-html.full.md
contradicts: n3-positive-global's claim "classification forces H1(99)=0"
answers: (the directive-39 FIRST gate's classification input)
```

```claim
id: cioaba-mim-lattice-lambda1-is-rook
statement: Among lattice graphs L2(n) (n^2, 2(n-1), n-2, 2), the member with
  lambda=1 is exactly L2(3) = the 3x3 rook's graph (9,4,1,2), the 9-vertex
  control; no lattice graph has parameters (99,14,1,2).
hypotheses: lattice graph L2(n), lambda = n-2 = 1
holds-here: yes
status: asserted (direct from parameters)
bearing: rules the lattice-graph bucket out of (99,14,1,2) in the H1
  classification; the sole lambda=1 lattice member is the control rook(3)
anchor: research/sources/cioaba-mim-clique-homology-srg-html.full.md
follows-from: cioaba-mim-h1-classification
```
