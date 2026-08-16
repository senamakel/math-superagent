# Radon transform on Z_2^k and the K>1 functional

```approach
idea: Read the fold weight nu2(n) = wt(Phi_n h) as the Hamming weight of a
PARTIAL Radon transform on Z_2^k (k = ceil(log2 n)). Each fold cell
eps_d = (-1)^{T(n,d)} = prod_{j in M_d} s_j is the integral of s over the
translated subcube M_d (|M_d| = 2^{pc(d)}), so (eps_d)_d is the
X-ray/Ray-slice transform over a fixed family of subcubes of all dimensions.
The K>1-sensitive functional is the Walsh-degree localization of this transform:
correlation order K of h <-> Walsh modes omega with |omega| = K.
mechanism: Diaconis-Graham (Pacific J. Math 1985, "The Radon transform on
Z_2^k") give the complete spectral theory of the HYPERPLANE Radon transform on
Z_2^k: eigenvalues are Krawtchouk polynomials in the Walsh basis, the inverse
is explicit, and an uncertainty principle holds: |supp f|·|supp Rf| >= 2^k.
Our operator is the PARTIAL transform over the subcube family {M_d}, a proper
subfamily of all subcubes; its spectrum is a restriction of the Krawtchouk
spectral measure, and the order-K content lives in the restriction. Goal:
express wt(Phi h) through the spectral weights lambda_omega |s-hat(omega)|^2 and
price those degrees against one-point mod-2^m equidistribution of primes
(Chebotarev) — strictly weaker than pointwise mod-4 switch density.
first-step: diagonalize the energy operator R*R of the subcube family in the
Walsh basis, print eigenvalues grouped by Walsh degree, verify the n=8 witness
separates at degrees >= 2.
falsifier: if all spectral mass of R*R sits at degree <= 1, the route is dead.
status: refuted
precedent:
  Diaconis-Graham, "The Radon transform on Z_2^k", Pacific J. Math 118 (1985)
  323-345, doi 10.2140/pjm.1985.118.323 — the named full-hyperplane engine
  (Krawtchouk spectrum, inversion, uncertainty |supp f|·|supp Rf| >= 2^k).
  Diaconis-Graham "vanishing", Vance "Fourier transforms and the Radon transform
  on Z_2^k" (Scand. J. Stat. 1995) — the DG-uncertainty family.
  Krawtchouk spectral machinery (same Walsh/MacWilliams/Delsarte toolbox as the
  grounded fold-second-moment-krawtchouk and meet-join-parseval-self-duality
  routes): in-workspace claims delsarte-lp-holds-for-nonlinear-row-sets,
  fold-second-moment-krawtchouk, meet-join-parseval-self-duality,
  downset-row-intersection-meet-formula.
  Partial-subcube/witness structure: collapse-witness-n8-kstar-ge-2,
  REOPENED.md (K*(n)=floor(n/2)), fold-cell-degree-is-2^popcount.
  The proven negative it inherits: meet-join-parseval-self-duality (spectral
  geometry carries no pointwise force on a single input); request
  walsh-spectral-subset-b904 (an input-dependent weight lower bound remains
  open).
  No source applies the Radon/uncertainty machinery to the Pascal-mod-2 fold
  weight of the prime gap-parity string; searches return the DG/Radon-over
  Z_2^k and Krawtchouk-transform literature, none touching this object. Say
  plainly: I found no prior use of the Radon transform on Z_2^k for the fold
  weight, and the engine's theorems do not cover the partial subcube family
  this route needs.
killed-by: >
  The mechanism cannot deliver a pointwise weight lower bound for the fixed
  prime input, and this is a PROVEN failure of the spectral approach in this
  very workspace, not a speculative one. Three defects, the first alone fatal.

  (1) Spectral/uncertainty machinery bounds the Walsh-side support of an
  operator or a distribution, NOT the F2 image weight wt(Phi_n h) for a fixed
  input — and this workspace has already PROVED that the spectral geometry
  carries no pointwise force. The candidate proposes to express wt(Phi h)
  through spectral weights lambda_omega |s-hat(omega)|^2 and a Diaconis-Graham
  uncertainty principle |supp f|·|supp Rf| >= 2^k. But:
  - The DG uncertainty principle is a product/support bound about |supp f| and
    |supp Rf| in the Walsh basis — a constraint on WHERE a function is
    supported under the transform, not a lower bound on wt(Phi_n h) for a fixed
    prime string h. A low-Walsh-support statement is exactly the "structured
    low-weight input" family the five closed doors forbid relying on, and the
    equality cases of every uncertainty bound are subgroup/affine-subspace
    indicators (the collapse witnesses of the doors).
  - This workspace's grounded route meet-join-parseval-self-duality already
    proved the sharp negative: Parseval bounds a weighted average, and the
    spectral geometry provably carries no pointwise force on a single input
    (S_h^2 <= O(n)·2^{nH(p)} is strictly worse than trivial). The Radon
    candidate is another spectral route on the same object (the S_omega Walsh
    spectrum of the fold's row set), so it inherits that proven negative. It
    does not escape by calling the operator "partial" — the pointwise-no-force
    fact is about the DIAGONALIZATION being a distributional identity, not
    about which subfamily the rows form.

  (2) Diaconis-Graham's theory is for the FULL hyperplane Radon transform, and
  the candidate's "partial subcube family" is exactly where their theorems
  stop. DG 1985 give the complete Krawtchouk spectral theory and inversion for
  the transform Rf integrating f over ALL hyperplanes, plus the uncertainty
  principle. The candidate's {M_d : d in [2,n-1]} is a proper subfamily of all
  subcubes of all dimensions — the digital downsets down(d) reflected. The
  Krawtchouk eigenvalue theorem and uncertainty inequality are not stated for a
  partial subcube family, and the whole point of the restriction is that it is
  NOT the full (bijective, inert) zeta/Mobius transform the full-families
  theory covers. So the named engine gives a complete answer for an operator
  that is not ours, and leaves ours (the one whose K>1 content is claimed)
  without a single stated theorem. The "speculative" half — the restricted
  Krawtchouk measure has a clean closed form — is asserted, not sourced.

  (3) Correlation order K*(n) ~ floor(n/2) and Walsh degree are conflated in a
  way the witness does not support. REOPENED's witness (h=00000010 vs
  h'=00000100, equal C_1, S^2=0 vs 4) separates under S^2, and the candidate
  reads this as "separates at Walsh degrees >= 2". But correlation order K (how
  many layers of the C_K correlation vector determine S^2, the floor(n/2)
  budget) is a different index than Walsh degree of the Radon-transformed
  string. A single point-mass at position u has Walsh content spread over all
  degrees, but its C_K correlation truncation is what the K*(n) budget
  measures; identifying "sees structure at K>1" with "Walsh degree >= 2" is a
  dictionary the witness does not establish. Whatever the right dictionary is,
  the pointwise lower bound it would produce is still barred by (1).

  Net: the Radon candidate restates the known second-moment spectral object
  under a partial-transform name, invokes a full-family engine whose theorems
  do not apply to the partial family, and proposes to extract a pointwise weight
  lower bound from a spectral identity — which the run has already proven to
  carry no pointwise force. Refuted on evidence, not on absence.
```

## Distinctness and honesty

Not f2-gram-disjointness-spectrum (refuted: Gram spectrum h-independent) and
not spectral-gap-parseval-native-transfer (refuted: complex Parseval, DC mode);
the new claim was a partial-subcube restriction of the Radon transform. Refuted
on evidence: spectral geometry carries no pointwise force (the proven
meet-join-parseval-self-duality negative) and DG's theorems cover only the full
hyperplane transform.
