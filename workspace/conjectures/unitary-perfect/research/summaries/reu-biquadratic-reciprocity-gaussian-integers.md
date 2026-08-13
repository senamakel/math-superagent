# Biquadratic reciprocity — REU survey (Xu), Gauss sums proof

Source: https://math.uchicago.edu/~may/REU2021/REUPapers/Xu,Nancy.pdf. Full text at `[[reu-biquadratic-reciprocity-gaussian-integers.full]]`. Proof-oriented companion to the Wikipedia/Dummit statements: gives the character, primary convention, the main law, and explicitly the supplementary `(i/π)_4` value.

## Quartic residue character (Def 5.2)

`(α/π)_4 ∈ {0, ±1, ±i}`, `(α/π)_4 = i^j` where `α^{(Nπ−1)/4} ≡ i^j (mod π)`, Nπ ≠ 2. `(α/π)_4 = 1 ⟺ α` is a perfect 4th power mod π. Extends to composite denominators (Def 5.3) by multiplicativity over irreducible factors.

**Primary** (Def 5.4): nonunit `α ≡ 1 (mod (1+i)^3)`. Proposition 5.5: α = a+bi primary iff `a ≡ 1 (mod 4), b ≡ 0 (mod 4)` or `a ≡ 3 (mod 4), b ≡ ?`. (Note: this REU gives the primary ≡ 1 mod (1+i)^3 form; a+bi primary iff a≡1 mod 4 & b≡0 mod 4, or a≡3 mod 4. See full text / Wikipedia for the exact b condition in the second case.)

## Biquadratic reciprocity (Theorem 5.8)

For relatively prime primary elements λ, π of Z[i]:
```
(λ/π)_4 = (π/λ)_4 · (-1)^{((Nλ−1)/4)((Nπ−1)/4)}
```

## Supplementary value of i (Prop 5.7)

For n ≡ 1 (mod 4): `(i/n)_4 = (-1)^{(n−1)/4}`. Proven from the prime cases p ≡ 1 (mod 4) and q ≡ 3 (mod 4).

## What it contributes

The proof mechanism (Gauss sum `g(χ_π)^4 = π^3·π` via Jacobi sums, Prop 5.9) and the primary convention `≡ 1 mod (1+i)^3`. Confirms the main law and the sign rule independently. Does NOT give the explicit `(2/π)_4` supplementary (Wikipedia does) — so for the actual step-2 evaluation the Wikipedia `[2/π]=i^{-b/2}` is the operative formula; this source supports the framework.

```claim
id: qr-char-def-and-primary
statement: The quartic character (α/π)_4 on Z[i] (Nπ≠2) detects 4th powers;
  primary means ≡ 1 mod (1+i)^3; biquadratic reciprocity
  (λ/π)_4 = (π/λ)_4·(-1)^{((Nλ-1)/4)((Nπ-1)/4)} for primary relatively
  prime elements; and (i/n)_4 = (-1)^{(n-1)/4} for n ≡ 1 (mod 4).
hypotheses: Z[i], Nπ≠2, primary elements relatively prime
holds-here: yes
status: sourced
bearing: establishes the character machinery and Jacobi-sum identity
  g(χ_π)^4 = π^3 π the reciprocity proof runs on; complements the
  Wikipedia supplementary [2/π]=i^{-b/2}
anchor: research/sources/reu-biquadratic-reciprocity-gaussian-integers.full.md
```
