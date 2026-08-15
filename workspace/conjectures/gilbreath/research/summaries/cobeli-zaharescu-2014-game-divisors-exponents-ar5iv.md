# Cobeli & Zaharescu 2014 — "A game with divisors and absolute differences of exponents"

**Full text:** `research/sources/cobeli-zaharescu-2014-game-divisors-exponents-ar5iv.full.md`
**Source:** https://ar5iv.labs.arxiv.org/html/1411.1334 (arXiv:1411.1334 [math.NT]); journal version J. Difference Equ. Appl. 20(11):1489–1501, doi 10.1080/10236198.2014.940337.

## What it is

A **completely solved** absolute-difference game that is the closest proved sibling to Gilbreath's conjecture in the literature. The "atomic" rule is `Z(a,b) = ab/gcd(a,b)²`, applied to neighbors to form the next row, starting from the primes. Per-prime, `Z` is exactly an exponent absolute-difference: `Z(p^s,p^t) = p^{|s-t|}`. Because the game starts from **squarefree** numbers (the primes), a prime's exponent in every later entry is 0 or 1, and the per-prime exponent evolution is exactly the mod-2 difference game `φ(w)(n)=|w(n+1)−w(n)|` on `𝔽₂` sequences.

## The theorem (proved twice, §4 and §5) — a closed-form analogue of GC

Starting from the primes on row 0, every entry has an exact Sierpinski closed form:

```
a_{m,n} = ∏_{r ∈ S_m} p_{n+r},   where S_m = { r : binom(m,r) odd }
```

So `ν_{p_k}(d_m) = 1 iff binom(m,k) odd`, and the number of prime factors of the left-edge element `d_m` is `ω(d_m) = #{k : binom(m,k) odd}` = the number of odd binomial coefficients in row `m` = a **power of 2** (Glaisher). This is Theorem 1. Theorem 2: `ω(d_m) = ω(a_{m,n})` — the number of prime factors is the same all across row `m`.

Key facts behind it (all standard, all proofs shown):
- Per-prime exponents evolve by the mod-2 difference operator `φ`, whose generating series obeys `Q_{φ⁽ᵐ⁾} = ((1+X)/X)ᵐ Q_w (mod negative powers)`.
- The mod-2 difference operator is the Pascal/Rule-90 law: `ψ⁽ᵐ⁾(w_k)(n) = 1 iff binom(m, n−k) odd`.
- The left diagonal (`d_m`) is controlled by `φ⁽ᵐ⁾` at position 0, i.e. by `binom(m,k)`.
- The exponent sequence `log₂ ω(d_m) = δ_m` is fractal: `δ_{t·2^s} = δ_t`, `δ_{2^s+j} = δ_j + 1`; it equals the Sierpinski digit-sum / OEIS A000120 (number of 1s in binary).
- Cycle structure: the mod-2 difference game on a single monomial is **periodic with cycle length `L_k = smallest power of 2 > k`** (Theorem 3, Corollary 2): `φ⁽²ˢ⁾(w_k) = w_k` whenever `2^s > k`.

## Verified against the paper (this run)

The closed form `a_{m,1} = ∏_{r∈S_m} p_{1+r}` reproduces the paper's Table 1 exactly for m=0..7: 2, 6, 10, 210, 22, 858, 1870, 9699690. (S_m from odd binomials, primes p_1=2,p_2=3,p_3=5,p_4=7,p_5=11,p_6=13,p_7=17,p_8=19.)

## Why it matters for this run (bearings)

1. **A proved analogue, and the reason it is provable while GC is not.** This game is solvable exactly because the *exponent level* is what iterates: `Z` reduces every prime's exponent to a `{0,1}` mod-2 game, where `|a−b| ≡ a+b (mod 2)` is *linear*, so the whole evolution is Pascal/Rule-90 and admits a closed form. In Gilbreath the integer values do NOT reduce per-prime; the mod-4 linearization is the ceiling (the run has already established mod 8+ fails). This is a clean, citable illustration of exactly why the {0,2} regime in Gilbreath is hard: there is no per-prime reduction to a linear law.
2. **Confirms the "not about primes" structural framing.** The same Sierpinski/Pascal machinery the run proved for the {0,2} interior (rule90-interior-xor) governs this whole game, and here it *completes*; the difference is that the exponents form a linear mod-2 system while Gilbreath's integer entries do not. Reinforces Odlyzko's remark (quoted in the paper) that the left-edge taming is a general phenomenon for sequences with small random gaps.
3. **Rule-90 machinery in a four-prime-source setting.** The binomial-parity facts (binom(2^s−1,k) odd, binom(2^s,k) even in 𝔽₂; Glaisher power-of-2 count; Sierpinski) are the same ones underlying the run's proved rule90-interior-xor and the CHT mod-2 linearization — now anchored in the primary Cobeli–Zaharescu and Glaisher references.
4. **The cycle length `L_k = smallest power of 2 > k`** for the mod-2 single-monomial game is a concrete, proved periodicity the run's rule90/interior work can cross-check against.

**Status:** sourced (full text held), closed form machine-verified against the paper's Table 1 this run. Peer-reviewed (J. Difference Equ. Appl. 2014); two independent proof routes given in the paper itself.
