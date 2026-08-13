# Quartic reciprocity in Z[i] — Dummit lecture 31

Source: https://dummit.cos.northeastern.edu/teaching_sp21_4527/4527_lecture_31_quartic_reciprocity.pdf (Math 4527, Number Theory II, §8.3.4-8.3.5). Full text at `[[dummit-quartic-reciprocity-lecture.full]]`. Independent corroboration of the quartic reciprocity law and its supplementaries needed by the adopted `biquadratic-character-divisors` step 2.

## Definitions

**Quartic residue symbol**: for π a prime of Z[i] with Nπ ≠ 2, `[α/π]_4 ∈ {0, ±1, ±i}` is 0 if π|α, else the unique value with `[α/π]_4 ≡ α^{(Nπ−1)/4} (mod π)`. `[α/π]_4 = 1 ⟺ α ≡ β^4 (mod π)` (α a quartic residue). Multiplicative in numerator; invariant under associates and numerator congruence mod π.

**Primary prime** in Z[i]: `π ≡ 1 (mod 2+2i)`. Equivalently (this lecture): every prime except associates of 1+i has exactly one primary associate.

## Main law

If π, λ are distinct primary primes of Z[i], then
```
[π/λ]_4 = [λ/π]_4 · (-1)^{((Nπ−1)/4)((Nλ−1)/4)}
```
Same sign pattern as the Wikipedia statement: sign −1 iff both are ≡ 3+2i (mod 4).

## Properties used to test

Worked examples verify by direct computation ([3+2i/5-4i]=i, [5-4i/3+2i]=i with N=13,41 both ≡1 mod 4, no sign; [3+2i/7-2i]=1, [7-2i/3+2i]=-1 with N=13(13≡5 mod 8? no — (13-1)/4=3 odd),(53-1)/4=13 odd ⇒ sign −1). Confirms the main law, not the supplementaries (this lecture does not spell out [2/π] explicitly).

## What it contributes

A second, independent statement of the same law with a clean primary definition (`≡ 1 mod 2+2i`) and direct worked arithmetic for verification. Same restriction: applies to primary primes; the step-2 RHS over composite `2^p+i` needs the Jacobi extension and primaryization.

```claim
id: qr-main-law
statement: For distinct primary primes π, λ of Z[i],
  [π/λ]_4 = [λ/π]_4 · (-1)^{((Nπ-1)/4)((Nλ-1)/4)}.
hypotheses: π, λ primary (≡ 1 mod 2+2i), Nπ ≠ 2
holds-here: yes (all relevant r ≡ 1 mod 4, split into primary Gaussian primes)
status: sourced
bearing: the reciprocity engine the adopted product identity runs on;
  confirms the sign rule independently of Wikipedia
anchor: research/sources/dummit-quartic-reciprocity-lecture.full.md
```
