# Summary — Krawtchouk (Kravchuk) polynomials

Source: Wikipedia, "Kravchuk polynomials" (redirect from Krawtchouk polynomials).
Source URL: https://en.wikipedia.org/wiki/Krawtchouk_polynomials
Full text: `research/sources/wikipedia_krawtchouk_polynomials.full.md`

## What this is

The encyclopedic entry for the discrete orthogonal polynomials that diagonalise
the Walsh/Hadamard (MacWilliams) transform over the Boolean cube. These are the
exact polynomials named by the live adopted approach
`fold-second-moment-krawtchouk` and by the properly-digested
`guruswami_macwilliams_lp_notes` and `macwilliams_1963`. It fixes the definition,
the explicit low-degree forms, the orthogonality relation, and the generating
function — the standard reference for the object, cheap and worth having as the
canonical tier.

## What it establishes

For q = 2 the first few Krawtchouk polynomials are K₀(x;n)=1, K₁(x;n)=−2x+n,
K₂(x;n)=2x²−2nx+C(n,2), K₃(x;n)=−(4/3)x³+2nx²−(n²−n+2/3)x+C(n,3).

**Definition** (q a prime power, n positive, k = 0..n):
K_k(x;n,q) = Σ_{j=0}^k (−1)^j (q−1)^{k−j} C(x,j) C(n−x, k−j).

**Alternative forms** (useful in coding theory)
= Σ_j (−q)^j (q−1)^{k−j} C(n−j, k−j) C(x,j)
= Σ_j (−1)^j q^{k−j} C(n−k+j, j) C(n−x, k−j).

**Symmetry:** (q−1)^i C(n,i) K_k(i) = (q−1)^k C(n,k) K_i(k).

**Orthogonality:** Σ_{i=0}^n C(n,i)(q−1)^i K_r(i) K_s(i) = q^n (q−1)^r C(n,r) δ_{r,s}.
For q=2 this is the orthogonality that makes Krawtchouk the eigenbasis of the
discrete Fourier transform on the Boolean cube — the coordinate system in which
the MacWilliams identity and the fold's distance distribution F_n(z) diagonalise.

**Generating function:** (1+(q−1)z)^{n−x} (1−z)^x = Σ_k K_k(x;n,q) z^k.
This is the exact generator behind the functional-equation form of the MacWilliams
identity in `guruswami_macwilliams_lp_notes` (Remark 12):
Σ_ℓ W^{C⊥}_ℓ z^ℓ = (1/|C|) Σ_i W^C_i (1−z)^i(1+z)^{n−i}.

**Three-term recurrence** in k (given in full text) — the recurrence used for
efficient numerical evaluation of Krawtchouk moments.

## Bearing on this problem

The fold route's central quantity F_n(z) = Σ_{d,d'} z^{|M_d XOR M_{d'}|} (the
distance enumerator of the row code) is diagonalised by exactly these
polynomials: the Krawtchouk diagonalization
F_n(z) = 2^{−n} Σ_ω (1−z)^{wt(ω)} (1+z)^{n−wt(ω)} Ĉ_n(ω)²
is the MacWilliams identity in the Krawtchouk basis (q=2). This entry supplies
the definition and orthogonality that give that basis its diagonalising power.
It is a secondary/encyclopedic reference relative to the primary
`macwilliams_1963` and the on-point derivation in `guruswami_macwilliams_lp_notes`;
it does not by itself bound A₂ or F_n(z) for the fold row set.

## What would falsify its bearing

Treating the Krawtchouk polynomials' existence as itself giving A₂ = O(n) for the
fold row code: it does not — orthogonality gives the transform, not the growth of
a specific distance distribution, which is the open combinatorial content of
condition (C) in the adopted approach.

```claim
id: krawtchouk-polynomials-encyclopedic
statement: >
  Krawtchouk polynomials K_k(x;n,q)=Σ_j(−1)^j(q−1)^{k−j}C(x,j)C(n−x,k−j) are the
  discrete orthogonal polynomials diagonalising the Walsh/MacWilliams transform
  on the Boolean cube, with generating function (1+(q−1)z)^{n−x}(1−z)^x=Σ_k K_k z^k,
  orthogonality Σ_i C(n,i)(q−1)^i K_r(i)K_s(i)=q^n(q−1)^r C(n,r)δ_{rs}, and the
  explicit low-degree forms K₀=1, K₁=n−2x, K₂=2x²−2nx+C(n,2) (q=2).
hypotheses: q a prime power, n positive, 0≤k≤n; standard.
holds-here: yes — the q=2 forms are exactly the eigenbasis in which the fold's
  distance enumerator F_n(z) and the MacWilliams functional equation
  (1/|C|)Σ_i W^C_i(1−z)^i(1+z)^{n−i} diagonalise.
status: asserted-by-source (encyclopedic/standard; matches the primary derivations
  in macwilliams_1963 and guruswami_macwilliams_lp_notes).
bearing: supplies the canonical definition and orthogonality for the Krawtchouk
  basis used by the live approach fold-second-moment-krawtchouk; does NOT itself
  bound A₂ or the growth of the fold's row-code distance distribution.
anchor: research/sources/wikipedia_krawtchouk_polynomials.full.md
```
