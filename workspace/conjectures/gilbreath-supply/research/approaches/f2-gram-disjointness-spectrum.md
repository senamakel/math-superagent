# F₂ Gram = disjointness matrix: involutive-slice spectrum of the fold

```approach
idea: Φ_n is a rectangular slice of the SELF-INVERSE F₂ zeta/Möbius matrix Z
(Z_{S,T}=[T⊆S], Z²=I over F₂), and the F₂ Gram matrix G_n = Φ_n Φ_n^T is the
DISJOINTNESS matrix G_{d,d'} = [d∧d'=0]. The ℂ spectrum of G is explicit —
G = ⊗_{i} [[1,1],[1,0]] has eigenvalues φ^{m−2k}(−1)^k with φ the golden ratio —
so G carries a spectral gap and a genuine self-duality the integer-Gram
(Krawtchouk) route does not see. Bound wt(Φ_n h) by an exact Parseval/energy
identity on this involutive basis, with the prime string entering through a
single golden-ratio-weighted spectral quantity.
mechanism: Two independent, checkable structure facts. (1) Involutive slice:
Z²=I over F₂ (the submask zeta transform equals its own inverse because −1=1), so
the fold is a window of an orthogonal (over F₂) self-adjoint map, and the quotient
F₂^n/ker → image is an isometry with respect to a *twisted* form whose Gram is G.
(2) Disjointness Gram: G_{d,d'} = (Z Z^T mod 2)_{d,d'} = 2^{pc(d∧d')} mod 2 =
[d∧d'=0], matching the already-proved meet formula |M_d ∩ M_{d'}| = 2^{pc(d∧d')}.
Because G = ⊗[[1,1],[1,0]] its ℂ eigenvalues are φ^{m−2k}(−1)^k (largest ≈ n^{log₂φ}
≈ n^{0.694}), a clean spectral gap — in contrast to the integer Gram Φ^TΦ (entries
2^{pc(d∧d')}, Krawtchouk eigenvalues) used by the adopted
`fold-second-moment-krawtchouk` route. The proposal is that wt(Φh)=‖Φh‖₁ admits an
exact decomposition through the G-eigenbasis whose dominant term is a single
golden-ratio-weighted energy of h, so a lower bound on wt reduces to a *spectral*
input on h strictly weaker than switch density.
status: refuted
killed-by: G = Φ_n Φ_n^T is h-INDEPENDENT (a property of the row set alone), so its golden spectrum cannot bound wt(Φ_n h) for a fixed input h; and weight != energy (over Z, wt(Φh) counts parity cells while h^T Φ^T Φ h = Σ_d (integer dot)^2 -- the all-ones string has wt(Φh)=0 but energy ~n, closed door 1). The h-coupling Gram is Φ^T Φ (Krawtchouk), already the adopted fold-second-moment-krawtchouk route. The disjointness/golden spectrum is a relabeling of row self-similarity, not a weight lower bound.
precedent: (machinery located and hypotheses verified — the transfer to a weight
bound is the unproven, open step; see "Grounded, and what is not" below)
- Zeta/Möbius invertibility on the subset lattice, and ζ=ζ^{-1} in characteristic 2:
  Björklund–Kaski–Williams, "Solving Systems of Polynomial Equations over GF(2) by a
  Parity-Counting Self-Reduction", ICALP 2019, https://doi.org/10.4230/lipics.icalp.2019.26
  (fast zeta transform; "in the field F₂ of two elements ζ = ζ^{-1}").
- Meet-matrix / lattice eigenvalue machinery (the disjointness matrix is the meet
  matrix of the Boolean lattice with the constant function): Mattila, "On the
  eigenvalues of combined meet and join matrices", Linear Algebra Appl. (2014),
  https://doi.org/10.1016/j.laa.2014.10.001 ; and Mattila, "On the invertibility and
  eigenvalue properties of some lattice-theoretic matrices: meet and join matrices via
  Möbius inversion" (dissertation, 2015), https://trepo.tuni.fi/handle/10024/97895 .
- In-workspace (established): claim `downset-row-intersection-meet-formula` (proved:
  M_d ∩ M_{d'} = M_{d∧d'}, |M_d∩M_{d'}| = 2^{pc(d∧d')}); claim `fold-rank-is-n-2-nullity-2-alternating`
  and `fold-rank-n-minus-2-binomial-proved` (rank n−2, nullity 2, F₂^n/ker ≅ image);
  claim `linearisation-fold-weight` (ν₂(n)=wt(Φ_n h)).
- The disjointness-matrix eigen-identity G = ⊗[[1,1],[1,0]] with eigenvalues
  φ^{m−2k}(−1)^k is elementary (Kronecker of the golden-ratio matrix); the largest
  eigenvalue φ^m = n^{log₂φ} ≈ n^{0.694}.
first-step: Machine-verify (a) Z²=I and (b) G_{d,d'}=[d∧d'=0] for n ≤ 64 by
explicit F₂ matrix multiplication; compute the ℂ spectrum of G and confirm the
golden-ratio eigenvalues φ^{m−2k}(−1)^k; then compute the proposed energy
decomposition of wt(Φ_n h) for the primes against all-ones and Thue–Morse
(negative controls). Falsifier: if the G-eigenbasis decomposition of wt(Φh) does
not exist or does not separate primes from the controls, the spectrum is inert.
```

## Grounded, and what is not

**The named structure facts are real, standard, and their hypotheses hold here.**

1. **Z²=I over F₂.** The submask-zeta matrix Z_{S,T}=[T⊆S] has inverse given by the
   Möbius function of the subset lattice; in characteristic 2, zeta = Möbius, so Z²=I.
   This is classical (Rota; see the Björklund–Kaski–Williams source and the
   Moore–Penrose/incidence-matrix literature). It reproduces the in-workspace claim
   `supply-fold-submask-zeta-involution`. Verified in-spirit by
   `code/out/verify_approach_premises.py` (Z²=I for n=4,8,16; Gram=disjointness for
   n=4,8,16,32), which is written but not yet executed — tool_builder must run it.

2. **Gram = disjointness.** (Z Z^T mod 2)_{d,d'} = |{s: s⊆d, s⊆d'}| mod 2 = 2^{pc(d∧d')}
   mod 2 = [d∧d'=0]. This is exactly the proved meet formula
   `downset-row-intersection-meet-formula`. So the F₂ Gram of the fold's rows is the
   disjointness matrix, as claimed. The stated identities are confirmed.

3. **Golden spectrum (full cube).** The disjointness matrix on *all* subsets of an
   m-set decomposes as ⊗[[1,1],[1,0]], whose eigenvalues are φ^{m−2k}(−1)^k with φ the
   golden ratio, max φ^m = n^{log₂φ} ≈ n^{0.694}. Verified by direct hand-check of the
   Kron structure.

**But — a precision caveat that matters, and that the literature does not resolve.**
The golden-ratio Kron spectrum is literally that of the disjointness matrix indexed by
the *full cube* [0, 2^m − 1]. The operative fold Gram is a *principal submatrix*
indexed by d ∈ [2, n−1] — of size n−2 (not 2^m), and with the rows 0,1 removed. A
principal submatrix of the golden Kron-power does not automatically retain that clean
spectral gap; whether it does is exactly what the first-step's eigenvalue computation
must settle. So the statement "G carries a spectral gap with eigenvalues φ^{m−2k}(−1)^k"
is fully grounded only for the full-cube matrix; for the operative restricted sheet it
is a claim to test, not a fact.

**What the literature does NOT supply (this is the open, load-bearing step).** No
source applies the disjointness/meet-matrix spectrum, or the golden-ratio Kron
decomposition, to bound the Hamming weight of the image of a linear map against a
fixed (prime) coefficient string. The mechanism's speculative half — that wt(Φh)=‖Φh‖₁,
an L¹/weight quantity, admits a useful lower bound through a spectral quantity of the
F₂ Gram — is new work with no published precedent for or against it. It is not the
refuted Walsh/Parseval route (that Parseval kill is over the ±1 Hadamard basis; here
the basis is the disjointness/Golden eigenbasis), but it shares the ANF/Möbius route's
risk of being "a relabeling" if no bound comes out. None of the five closed doors is
implied: the input is a spectral condition on h in the submask coordinates (the
`submask-read` difficulty), not a complexity hypothesis, and the negative controls
(all-ones, Thue–Morse) are exactly the test.

**Verdict.** Grounded as machinery: the reformulation is real, named, citable, and its
stated algebraic identities check out. Not grounded as a theorem: nobody has made the
spectrum produce a weight bound, and the operative (principal-submatrix) spectrum is
unverified. Status `grounded` here means "the reformulation and its named facts are
real and sourced; the transfer to a bound is open and is the first-step's falsifier."
Run the first-step before spending number theory.
