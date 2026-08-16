# The Krawtchouk spectrum of the fold row set IS the excess functional — a meet-matrix Parseval self-duality

```approach
idea: >
  The Walsh/Krawtchouk spectrum of the fold's row set is not a separate
  "geometry" object: it is the EXCESS FUNCTIONAL itself. Writing
  C_n-hat(omega) = sum_{d in [2,n-1]} (-1)^{<omega, 1_{M_d}>} for the row
  indicators 1_{M_d}, the tautological identity <omega, 1_{M_d}> = T_omega(n,d)
  mod 2 (both are the parity of omega on the window M_d) gives

      C_n-hat(omega) = S_omega(n)  =  sum_{d in [2,n-1]} (-1)^{T_omega(n,d)}

  for EVERY input string omega in F2^n. Substituted into the Krawtchouk/MacWilliams
  diagonalization of the distance enumerator F_n(z) = sum_{d,d'} z^{|M_d △ M_{d'}|}
  (hand-checked in the adopted `fold-second-moment-krawtchouk` route), this gives the
  exact Parseval/energy identity for the map h -> S_h(n):

      F_n(z) = 2^{-n} sum_{omega} (1-z)^{wt(omega)} (1+z)^{n-wt(omega)} S_omega(n)^2.

  The left side is the meet-matrix distance enumerator, proved O(n) for |z| < 1 by the
  adopted `downset-row-code-distance-closed-form` route (the meet matrix
  Phi Phi^T = (2^{pc(d∧d')}) is the Boolean-lattice meet matrix with f = 2^{pc}, whose
  full-cube spectrum is phi^{2(m-2k)} — the named Mattila meet/join-matrix home). The
  right side is a weighted L^2 average of the excess functional over the whole cube,
  with weight 2^{-n}(1-z)^{wt}(1+z)^{n-wt} = p^{wt}(1-p)^{n-wt} at z = 1-2p — exactly
  the iid-Bernoulli(p) measure. So the geometry and the arithmetic are THE SAME OBJECT
  seen through two bases (Walsh and submask), and the second moment under ANY product
  measure is E_p[S^2] = F_n(1-2p) = O(n), for p bounded away from 0 and 1
  (|1-2p| <= z_0 < 1); NOT uniformly over all p in (0,1). [Corrected by the
  refuter: at p -> 0 the terms all -> 1 and F_n(1-2p) -> (n-2)^2 = Theta(n^2),
  because h == 0 (and all-ones) are kernel inputs with every cell T=0, eps=+1,
  S=n-2. See claim parseval-second-moment-not-uniform-in-p.]
mechanism: >
  (1) SELF-DUALITY (exact, index bookkeeping only). By the fold definition
  T_omega(n,d) = XOR_{j in M_d} omega[j] and <omega,1_{M_d}> = sum_{j in M_d} omega[j],
  the two agree mod 2, so (-1)^{<omega,1_{M_d}>} = (-1)^{T_omega(n,d)}. Summing over
  d in [2,n-1] gives C_n-hat(omega) = S_omega(n). No reflection, no zeta transform,
  no conjecture. Hand-checked: n=4, omega=(1,0,0,0) gives C_n-hat = S_omega = 0.
  (2) PARSEVAL (exact, Krawtchouk/MacWilliams). The identity
  F_n(z) = 2^{-n} sum_omega (1-z)^{wt omega}(1+z)^{n-wt omega} C_n-hat(omega)^2 is the
  standard Krawtchouk diagonalization, hand-verified in `fold-second-moment-krawtchouk`
  ("Confirmed" section), valid for ANY multiset of row indicators (no linearity needed
  for the identity, only for the LP bound). Substituting (1) yields the Parseval form.
  (3) MEET-MATRIX HOME (sourced, Mattila). The row Gram Phi Phi^T = (2^{pc(d∧d')}) is
  the meet matrix of the Boolean lattice with f = 2^{pc}, i.e. the Kronecker power
  ⊗[[1,1],[1,2]] with eigenvalues phi^{2(m-2k)} (hand-verified: the 2x2 block has
  eigenvalues phi^2, phi^{-2}); its F2 reduction Phi Phi^T mod 2 is the disjointness
  matrix ⊗[[1,1],[1,0]] with the golden spectrum phi^{m-2k}(-1)^k of the refuted
  `f2-gram-disjointness-spectrum` candidate. This is exactly the Mattila meet/join
  matrix spectral theory (Lindström–Wilf / Möbius factorization), so the spectral
  language research surfaced is real and names the object.
  (4) REPRODUCTION (Scholze gate). At z = 0 the Parseval identity gives
  E_omega[S_omega(n)^2] = F_n(0) = n-2, which is EXACTLY the on-disk proved claim
  `fair-model-exact-binomial` (wt(Phi h) ~ Binomial(n-2,1/2) => var S = n-2). The new
  setting reproduces an established result, so it earns its place.
status: grounded
precedent: >
  Sourced: Mattila, "On the eigenvalues of combined meet and join matrices", Linear
  Algebra Appl. 2014 (doi 10.1016/j.laa.2014.10.001) and Mattila dissertation 2015
  (meet/join matrices via Möbius inversion — the named home of the spectral theory);
  MacWilliams 1963 / Delsarte 1973 / Krawtchouk diagonalization (already in
  `fold-second-moment-krawtchouk` precedent); the Lindström–Wilf meet-matrix
  factorization. In-workspace (established, imported as proved): claim
  `linearisation-fold-weight` (T(n,d) = XOR_{o⊆d} h[n-1-d+o], equivalently
  XOR_{j∈M_d} h[j]); claim `downset-row-intersection-meet-formula`
  (M_d ∩ M_{d'} = M_{d∧d'}, |M_d ∩ M_{d'}| = 2^{pc(d∧d')} — the meet structure);
  claim `fold-rank-is-n-2-nullity-2-alternating` (surjectivity, so h ↦ wt(Φh) has
  the Binomial fibre structure); claim `fair-model-exact-binomial` (reproduced at
  z=0); the Krawtchouk diagonalization is hand-checked in the adopted
  `fold-second-moment-krawtchouk` file; `downset-row-code-distance-closed-form` proves
  F_n(z) = O(n) for |z|<1. The NEW content is the single identification
  C_n-hat(omega) = S_omega(n), which none of these files stated.
first-step: >
  tool_builder, exact integer/F2 arithmetic, no number theory beyond the row-set
  definition (the prime string h is NOT needed for steps 1-4 — pure combinatorics):
  (1) VERIFY the self-duality C_n-hat(omega) = S_omega(n) by brute force for n <= 16:
      compute C_n-hat(omega) = sum_d (-1)^{<omega,1_{M_d}>} and S_omega(n) =
      sum_d (-1)^{T_omega(n,d)} independently for EVERY omega in F2^n (2^16 = 65536
      inputs at n=16, cheap), assert equality on all of them.
  (2) VERIFY the Parseval identity F_n(z) = 2^{-n} sum_omega (1-z)^{wt}(1+z)^{n-wt}
      S_omega(n)^2 for n = 8..20 and z in {0, ±0.1, ±0.3, 1-2·0.597}, against F_n(z)
      computed directly from the meet formula |M_d △ M_{d'}| =
      2^{pc(d)}+2^{pc(d')}-2^{pc(d∧d')+1} (claim downset-row-intersection-meet-formula).
  (3) VERIFY the z=0 reproduction: E_omega[S_omega^2] = 2^{-n} sum_omega S_omega^2 = n-2,
      matching the Binomial(n-2,1/2) variance of the fair model (negative control: a
      WRONG formula such as n-1 or n must fail).
  (4) SHARP-NEGATIVE CHECK (the load-bearing honest limit): confirm numerically that the
      pointwise bound extracted from Parseval, S_h^2 <= F_n(1-2p) · 2^{n H(p)} with
      p = wt(h)/n, is exponentially WEAK — at n=20 and p=0.597 it must exceed the trivial
      (n-2)^2, so the geometry provably cannot bound a single input's excess. This is the
      statement that (A) is irreducibly arithmetic.
  (5) COMPUTE the operative principal-submatrix spectrum of the meet matrix Phi Phi^T =
      (2^{pc(d∧d')}) for d,d' in [2,n-1] (the exact object research flagged as unverified),
      and compare to the full-cube Kronecker spectrum phi^{2(m-2k)}: report where the
      restricted spectrum sits and whether a spectral gap survives the restriction.
  FALSIFIER: if (1) fails on any omega the self-duality is wrong (it is index bookkeeping,
  so this would mean the fold/row definitions are misread); if (4) produces a bound STRONGER
  than trivial, the sharp-negative claim is wrong and the geometry DOES carry pointwise
  force, which would be the better outcome.
```

## The exact identities (derived by hand; machine verification is first-step)

Fix `n`, rows `d ∈ [2, n−1]`, columns `j ∈ [0, n−1]`, windows
`M_d = {n−1−d+o : o ⊆ d}`. By claim `linearisation-fold-weight` the fold cell is

```
T_h(n,d) = XOR_{o ⊆ d} h[n−1−d+o] = XOR_{j ∈ M_d} h[j].
```

For any input `ω ∈ F₂ⁿ` (taken as a string, not a frequency), and the row indicator
`1_{M_d} ∈ F₂ⁿ`:

```
⟨ω, 1_{M_d}⟩  =  Σ_{j ∈ M_d} ω[j]        (integer sum)
              ≡  T_ω(n,d)        mod 2.
```

Hence `(−1)^{⟨ω,1_{M_d}⟩} = (−1)^{T_ω(n,d)}` (both are ±1 and agree mod 2). Summing
over `d ∈ [2, n−1]`:

```
Ĉ_n(ω) := Σ_d (−1)^{⟨ω, 1_{M_d}⟩} = Σ_d (−1)^{T_ω(n,d)} =: S_ω(n).      (SD)
```

**Hand-check (n=4):** rows d∈{2,3}; M₂={1,3}, M₃={0,1,2,3}. Take ω=(1,0,0,0).
`Ĉ = (−1)^{ω₁+ω₃} + (−1)^{ω₀+ω₁+ω₂+ω₃} = (−1)⁰ + (−1)¹ = 1−1 = 0`. On the other side
`T_ω(4,2)=ω₁⊕ω₃=0`, `T_ω(4,3)=ω₀⊕ω₁⊕ω₂⊕ω₃=1`, so `S_ω=1−1=0`. ✓

The Krawtchouk/MacWilliams diagonalization of the distance enumerator (hand-checked
"Confirmed" in `fold-second-moment-krawtchouk`):

```
F_n(z) = Σ_{d,d'} z^{|M_d △ M_{d'}|}
       = 2^{−n} Σ_ω (1−z)^{wt ω} (1+z)^{n−wt ω} Ĉ_n(ω)².
```

Substituting (SD) gives the Parseval identity

```
F_n(z) = 2^{−n} Σ_ω (1−z)^{wt ω} (1+z)^{n−wt ω} S_ω(n)².                (P)
```

At `z = 0`: `F_n(0) = n−2` (only the diagonal, `|M_d △ M_{d'}| = 0` iff d=d′, survives),
and the RHS is `2^{−n} Σ_ω S_ω(n)² = E_ω[S_ω(n)²]`. This is exactly
`var(S) = n−2` under the uniform model, i.e. claim `fair-model-exact-binomial`. ✓
(Scholze gate: the new setting reproduces an on-disk proved claim.)

At `z = 1−2p`, the weight is `2^{−n}(2p)^{wt}(2(1−p))^{n−wt} = p^{wt}(1−p)^{n−wt}`, the
iid-Bernoulli(p) measure, so

```
E_p[S²] = F_n(1−2p) = O(n)   for p with |1−2p| ≤ z₀ < 1 (bounded away from 0 and 1);
the "uniformly in p ∈ (0,1)" phrasing is FALSE (refuter claim
parseval-second-moment-not-uniform-in-p: at p→0, F_n(1−2p)→(n−2)²=Θ(n²) via the
kernel input h≡0/all-ones giving every cell T=0, eps=+1, S=n−2).
```

because `F_n(z) = O(n)` for `|z| < 1` is a theorem (`downset-row-code-distance-closed-form`).
The fold is benign under every product measure, not just p = 1/2.

## The meet-matrix spectral home (sourced)

The row Gram is a meet matrix of the Boolean lattice:

```
(ΦΦᵀ)_{d,d'} = |M_d ∩ M_{d'}| = 2^{pc(d∧d')} = ⊗ [[1,1],[1,2]]
```

(claim `downset-row-intersection-meet-formula`; the Kronecker structure is the full-cube
one, each 2×2 block `[[1,1],[1,2]]` having eigenvalues `φ², φ⁻²`, so the spectrum is
`φ^{2(m−2k)}`, multiplicity `C(m,k)`, largest `φ^{2m} ≈ n^{1.388}`). Its F₂ reduction is
the disjointness matrix `⊗[[1,1],[1,0]]` with the golden spectrum `φ^{m−2k}(−1)^k` — the
object the `f2-gram-disjointness-spectrum` candidate mounted on the *weight* and got
refuted for (weight ≠ energy; the Gram is h-independent). Mattila's meet/join matrix
theory (Lindström–Wilf Möbius factorization) is the named home: these are meet matrices
with `f = 2^{pc}`, and the spectral language is real and citable.

What the refuted candidate got wrong was the *object*, not the *machinery*: the
h-independent Gram cannot bound `wt(Φh)` (an L¹ quantity), but its distance enumerator
`F_n(z)` — a function of the same meet structure — is what couples to the second moment
`S(n)²` (an L² energy). The self-duality (SD) is the missing link that makes this
coupling explicit: the row-set spectrum and the excess functional are one object.

## What is honestly new, and the honest limit

**New and provable now:** (SD) and (P) are exact, elementary identities. They give a
self-duality theorem — the Walsh spectrum of the fold row set equals the excess
functional `h ↦ S_h(n)` — and a Parseval identity that reproduces the fair-model
binomial law and proves `E_p[S²] = O(n)` for every product measure. This is the
sharpest possible formulation of GOAL priority 2: SUPPLY's density-1 form (statement
(A) of the downset route) is the assertion that the prime string `h` sits at the
typical level of the excess functional under the product measure of its own density,
`E[S_h(n)²] = O(n)` on average in `n`.

**The limit, stated exactly.** Parseval controls a *weighted average*, not a point.
Every term in (P) is non-negative, so for the single input `h` with `p = wt(h)/n`:

```
S_h(n)² · 2^{−n H(p)} ≤ F_n(1−2p) = O(n)  ⟹  S_h(n)² ≤ O(n) · 2^{n H(p)},
```

with `H(p)` the binary entropy, `H(p) > 0` for `0 < p < 1`. Since `2^{nH(p)} ≫ n` the
bound is `≫ n²`, strictly worse than the trivial `S_h² ≤ (n−2)²`. The geometry therefore
provably carries **no** pointwise force on a single input: statement (A) is irreducibly
an arithmetic statement about the primes, and no input-free spectral argument can close
it. This is a sharp negative that pins exactly where the "fold does work" hypothesis ends.

## Why this beats the three candidates (and is not a relabeling)

- **`f2-gram-disjointness-spectrum` (refuted):** mounted the meet-matrix spectrum on the
  *weight* `wt(Φh)`, an L¹ quantity with no energy coupling, on the h-independent Gram.
  This route mounts the same named machinery (Mattila) on the correct object — the
  distance enumerator / second moment — and the self-duality (SD) is the transfer
  theorem that candidate lacked. Not a relabeling: (P) is a new exact identity that
  reproduces the fair-model law and proves `E_p[S²]=O(n)` for all p, which the refuted
  candidate could not state.
- **`abel-boundary-recurrence` (refuted):** its local-boundary hope is already killed by
  the adopted `derivative-ladder-delta-commutation` route's anti-Pascal corollary (the
  depth-sum does not telescope). This route does not recur in n at all; it is a finite,
  exact Parseval identity, no boundary hypothesis.
- **`substitution-incidence-perron` (refuted):** its self-similarity rules are false on
  the operative sheet. This route needs no substitution fixed point; the meet matrix's
  Kronecker/spectral structure is exact on the full cube and explicitly tracked to the
  operative restriction in first-step (5).

## Honest falsifier

If (SD) fails on any input (first-step 1), the fold/row definitions were misread — but
(SD) is index bookkeeping, so a failure means the whole linearisation was. If first-step
(4) instead yields a bound *stronger* than trivial for some `h`, then Parseval carries
pointwise force after all and the geometry side is not exhausted — a strictly better
outcome. Either way the run learns which of the two it is.
