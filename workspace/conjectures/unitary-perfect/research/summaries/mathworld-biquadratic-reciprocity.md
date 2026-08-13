# Biquadratic reciprocity — MathWorld

Source: https://mathworld.wolfram.com/BiquadraticReciprocityTheorem.html. NOTE (librarian 2026): no separate `research/sources/mathworld-biquadratic-reciprocity.full.md` exists; the download manager keys this URL to this summary file and refuses a second fetch, so THIS summary is the library's held record for the page. All content below was read from the live page at the URL above. The operative formulas are also in the Wikipedia digest (held) and Williams 1976 (primary, held).

## Statements

For distinct Gaussian primes π, σ:
```
(π/σ)_4 (σ/π)_4 = (-1)^{((Nπ−1)/4)((Nσ−1)/4)}
```
`(α/π)_4 = 1` iff `x^4 ≡ α (mod π)` solvable in Z[i].

**Quartic character of 2** (Euler's conjecture, Gauss's proof): for prime p ≡ 1 (mod 8),
```
2 is a quartic residue (mod p)  ⟺  p = x^2 + 64y^2  for integers x,y.
```
If p ≡ 7 (mod 8) then 2 is ALWAYS a quartic residue: `p = 8k+7`, `(2^(k+1))^4 ≡ 2 (mod p)`; e.g. `2^4 ≡ 2 (mod 7)`.

## What it contributes

The `p = x^2+64y^2` criterion (Euler's conjecture, Gauss's theorem) — a pure-integer description of `(2/p)_4 = 1` matching the `r ≡ 1 (mod 16)` test for primitive divisors r of Φ_{4p}(2). Corroborates that `(2/r)_4 = +1 ⟺ r = a^2+64b^2`, consistent with the verified check F2.

**Caveat:** the p ≡ 7 (mod 8) ⇒ 2 always a quartic residue fact applies to a RATIONAL prime equal to the full modulus; it does NOT force a quartic residue among the *divisors* of a fixed composite `Φ_{4p}(2)`. The adopted per-class shortcut (for fixed p mod 8, some divisor ≡ 1 mod 16) was already REFUTED computationally (approach `biquadratic-character-divisors` correction M4) — this MathWorld fact is about a single prime, not about divisor support, so it is not in tension with that refutation.

```claim
id: qr-2-quartic-criterion
statement: For a rational prime p ≡ 1 (mod 8), 2 is a quartic residue mod p iff
  p = x^2 + 64y^2; and for p ≡ 7 (mod 8), 2 is always a quartic residue mod p.
hypotheses: p odd prime, p ≡ 1 or 7 (mod 8)
holds-here: yes as a statement about a single modulus; NOT a divisor-support fact
status: sourced (Euler's conjecture, Gauss's theorem)
bearing: gives the pure-integer form of (2/r)_4 = +1 ⟺ r = a^2+64b^2 used in the
  adopted route; but cannot be applied divisor-by-divisor to force a head in
  Φ_{4p}(2)
anchor: research/sources/mathworld-biquadratic-reciprocity.full.md
```
