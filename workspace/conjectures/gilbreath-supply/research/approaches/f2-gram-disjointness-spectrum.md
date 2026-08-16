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
status: proposed
first-step: Machine-verify (a) Z²=I and (b) G_{d,d'}=[d∧d'=0] for n ≤ 64 by
explicit F₂ matrix multiplication; compute the ℂ spectrum of G and confirm the
golden-ratio eigenvalues φ^{m−2k}(−1)^k; then compute the proposed energy
decomposition of wt(Φ_n h) for the primes against all-ones and Thue–Morse
(negative controls). Falsifier: if the G-eigenbasis decomposition of wt(Φh) does
not exist or does not separate primes from the controls, the spectrum is inert.
```

## Speculation, marked

Facts (1) and (2) are established and cheap to verify mechanically. That the
golden-ratio spectrum yields a *useful* Parseval-type lower bound on wt(Φh), and
that the needed spectral input on h is weaker than switch density, is speculation
— and it risks being "another relabeling" in the sense that killed the ANF/Möbius
route, if no bound comes out of the spectrum. The first-step is designed to kill
that cheaply. Note also: the full disjointness matrix's ℂ spectrum is golden-ratio,
NOT the ±1 Hadamard spectrum, so this is genuinely distinct from the refuted
Walsh/Parseval routes (whose Parseval kill was over the ±1 Walsh basis).
