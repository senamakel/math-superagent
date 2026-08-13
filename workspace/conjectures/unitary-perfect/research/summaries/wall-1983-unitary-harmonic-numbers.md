# Wall (1983), *Unitary Harmonic Numbers*, Fibonacci Quarterly 21(1):18–25

Full text: [[wall-1983-unitary-harmonic-numbers.full]]
Source: https://www.fq.math.ca/Scanned/21-1/wall.pdf

## What it establishes

`n` is **unitary harmonic** when its unitary-divisor harmonic mean
`H*(n) = n·τ*(n)/σ*(n) = Π_{p^e||n} 2p^e/(1+p^e)` is an integer.

- **Theorem 1.** Exactly **23** unitary harmonic numbers have `ω(n) < 4`
  (Table 1).
- **Theorem 2.** Exactly **43** unitary harmonic numbers are `< 10^6`
  (Table 2). These include all but one of the `ω < 4` list.
- The `n < 10^6` machinery: `2^a||n` forces `a ≤ 10`, and `2^a||n` forces
  divisibility by the largest prime factor of `1+2^a`; iterated divisibility
  constraints enumerate the candidates (a "sharp" B-search where `ω(n)>4`
  after Theorem 1 forces further size cuts).
- **Conjecture:** infinitely many unitary harmonic numbers (including
  infinitely many odd ones), but only finitely many with `ω(n)` fixed.

## Bearing on this problem

Adjacent-class background. Unitary perfect numbers are unitary harmonic
(σ*(n)=2n gives H*(n)=1). The paper is one of the references for the
bibliographic chain (Wall 1983) and for the 2-adic budget technique: the
observation "any odd prime dividing σ*(n) must divide n" and `2^a||n ⟹ a ≤ 10`
mirror the budget identity. It does not bound a sixth UPN; it classifies
unitary harmonic numbers in a range, which strictly contains the unitary
perfect ones. **Not load-bearing for H_even.**

Relevant cross-reference: the fifth UPN's exact factorization is restated here
(`2^183·5^47…` OCR-garbled; correct `2^18·3·5^4·…`) with `H*(n)=2048` for it.

```claim
id: wall1983-unitary-harmonic-classified
statement: There are exactly 23 unitary harmonic numbers with omega(n) < 4
  and exactly 43 unitary harmonic numbers n < 10^6 (Theorems 1, 2). Wall
  conjectures infinitely many unitary harmonic numbers but only finitely
  many with any fixed omega(n).
hypotheses: n unitary harmonic (H*(n) integral); ranges n < 10^6, omega < 4
holds-here: yes as adjacent-class background; does not bound a sixth UPN
status: asserted
bearing: bibliographic-chain and 2-adic-budget-technique background for the
  unitary harmonic adjacent class; not used by the active divisor-level thread
anchor: research/sources/wall-1983-unitary-harmonic-numbers.full.md
```
