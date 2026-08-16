# Symmetric Pascal matrices modulo p — Bacher & Chapman (2003)

Source: https://arxiv.org/html/math/0212144
Full text: [[bacher-chapman-symmetric-pascal-matrices-modp.full]]

## What it establishes

Study the **symmetric Pascal matrix** `P(n)` with entries `p_{i,j} = C(i+j, i)`,
`0 ≤ i,j < n`, and its reduction mod p. (Note: `P(n)` is *symmetric* and *not* the
fold matrix `Φ_n` of this problem, which is `(n−2)×n` with rows `C(d, j−(n−1−d))`.)

- **Thm 1.1.** `det(P̄(n)_2) = ∏_{k=0}^{n-1} (−1)^{s_k}` where `s` is the Thue–Morse
  sequence (parity of binary digit sum). Determinant is ±1.
- **Prop 1.2 / Thm 1.3 / Thm 1.4.** For `q = p^l`, characteristic polynomial
  `χ_q(t) ≡ (t²+t+1)^{(q−ε(q))/3}(t−1)^{(q+2ε(q))/3} (mod p)`, `ε(q) ≡ q (mod 3)`.
  Over F₂ this gives `χ_n(t) ≡ (t+1)^{γ(n)}(t²+t+1)^{γ₂(n)} (mod 2)` with the γ
  recursion in the text.
- **Conjectures 1.6–1.8.** Formulas for the mod-p characteristic polynomials, open.
- **Thm 2.1.** P(n) is autosimilar: `P(2n) = [[P(n),P(n)],[P(n),0]]` block structure.

```claim
id: bacher-chapman-sym-pascal
statement: det(C(i+j,i) mod 2)_{0<=i,j<n} = prod_{k=0}^{n-1} (-1)^{s_k}, s_k = parity of
  binary digit sum of k (Thue-Morse); and char poly of the symmetric Pascal matrix mod 2
  factors as (t+1)^{gamma(n)}(t^2+t+1)^{gamma2(n)}.
hypotheses: p prime; P(n)=symmetric Pascal matrix C(i+j,i)
holds-here: no -- P(n) is a different matrix from Phi_n (this problem's fold matrix is
  not symmetric and is (n-2) x n)
status: proved (Thm 1.1, 1.4)
bearing: establishes the Thue-Morse sign structure and autosimilar block recursion for
  the *symmetric* Pascal matrix; a useful caution that row structure of Pascal-mod-2
  matrices is closely governed by Thue-Morse/down-set signs (parallels Callan), but the
  specific Phi_n multiset is not addressed
anchor: research/sources/bacher-chapman-symmetric-pascal-matrices-modp.full.md
```

## Contradiction / non-bearer note

`P(n) = (C(i+j,i))` is **not** this problem's `Φ_n`. Its `holds-here` is **no**. It is
kept as a warning that the literature's "Pascal matrices" are usually a different
object, and its Thue-Morse autosimilarity parallels Callan's down-set sign structure
but does not bear on the symmetric-difference multiset directly.
