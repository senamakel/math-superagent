# Quartic (biquadratic) reciprocity — definition, main law, and the supplementary laws for 2

Source: https://en.wikipedia.org/wiki/Quartic_reciprocity. Full text at `[[wikipedia-quartic-reciprocity.full]]`. This is the exact source for the supplementary laws the adopted `biquadratic-character-divisors` route's step 2 needs to evaluate `(2/(2^p+i))_4` in closed form.

## Definitions (Gaussian integers, §Gaussian integers)

Z[i] is a UFD. Units {1,i,-1,-i}. A prime which is ±1 mod (1+i)^3 is **primary**; every odd Gaussian integer has exactly one primary associate. λ = a+bi is primary iff `a ≡ 1 (mod 4), b ≡ 0 (mod 4)` or `a ≡ 3 (mod 4), b ≡ 2 (mod 4)`. Norm N(a+bi)=a^2+b^2; for every prime except 1+i, Nπ ≡ 1 (mod 4).

**Quartic residue character** of α mod a prime π with Nπ ≠ 2: `[α/π] = i^k ≡ α^((Nπ−1)/4) (mod π)`, the unique k mod 4. `x^4 ≡ α (mod π)` solvable iff `[α/π] = 1`. Extends multiplicatively to composite denominators (Jacobi-style), where value can be 1 without solvability.

## Main law (biquadratic reciprocity)

Let π, θ be primary relatively prime nonunits of Z[i]. Then
```
[π/θ] [θ/π]^{-1} = (-1)^{((Nπ−1)/4)·((Nθ−1)/4)}
```
(Gauss's form: if either ≡ 1 (mod 4) then `[π/θ]=[θ/π]`; if both ≡ 3+2i (mod 4) then they differ by a sign.)

## Supplementary laws (the load-bearing facts for this problem)

Let π = a+bi be a **primary** Gaussian prime. Then
```
[i/π]   = i^{-(a-1)/2}
[1+i/π] = i^{(a-b-1-b^2)/4}
[-1/π]  = (-1)^{(a-1)/2}
[2/π]   = i^{-b/2}
```
These are THE formulas the adopted product identity must evaluate. Note they require π primary and pair (a,b) explicit.

Rational statements (Gauss/Dirichlet): for prime p ≡ 1 (mod 4), 2 is a biquadratic residue mod p iff p = a^2 + 64b^2 (Euler); and (2/p)_4 as a period-8 function of the Gaussian-coefficient parity: `2 belongs to class 1/2/3/4 iff b ≡ 0/2/4/6 (mod 8)`. Dirichlet: `(2/p)_4 ≡ i^{ab/2} (mod p)` with i ≡ b/a.

## What it lets this run compute

The step-2 formula of `biquadratic-character-divisors` is `Π_{π^e || 2^p+i} (2/π)_4^e = (2/(2^p+i))_4`. The left factors are each `[2/π] = i^{-b/2} ∈ {+1, i, -1, -i}`, and `[2/π] = +1 ⟺ Nπ ≡ 1 (mod 16)` (this equivalence is verified computationally on all 71 primitive divisors through p=61 — `code/out/heven_gauss_61.captured.txt`, check F2). To evaluate the right side in closed form one must make `2^p+i` primary and apply `[2/π]=i^{-b/2}` — the primaryization is the nontrivial step (multiply by a power of i, tracking how `[2/·]` transforms). **Nothing here guarantees a positive or negative product; it is the exact mechanism, not a conclusion.**

## What it does not settle

The supplementary laws give `[2/π]` from the coefficients of a SINGLE primary Gaussian prime. The step-2 RHS is `(2/(2^p+i))_4` over a COMPOSITE denominator — needs the Jacobi-style extension, and `2^p+i` must be made primary first. The laws alone do not tell us the sign of the product or that any factor is +1; they are the machine, not the answer.

```claim
id: qr-supplementary-2
statement: For a primary Gaussian prime π = a+bi, [2/π] = i^{-b/2};
  [-1/π] = (-1)^{(a-1)/2}; [1+i/π] = i^{(a-b-1-b^2)/4}. Also [2/π] = +1
  iff Nπ ≡ 1 (mod 16) when applied to a primitive divisor of Φ_{4p}(2).
hypotheses: π primary in Z[i] (Gauss normalization); Nπ ≠ 2
holds-here: yes (Nπ ≡ 1 mod 16 ⟺ π | Φ_{4p}(2) has v2(r−1) ≥ 4 — verified
  on all 71 primitive divisors through p=61, check F2)
status: sourced (Wikipedia/Gauss/Dirichlet); the mod-16 equivalence is
  computed-only below p=61
bearing: the exact law the adopted product identity evaluates; turns the
  mod-16 coin-flip (Conjecture 29) into a product of per-factor quartic
  characters computable from the Gaussian factorization of 2^p+i
anchor: research/sources/wikipedia-quartic-reciprocity.full.md
```
