# MathWorld — Totient summatory function

Source: https://mathworld.wolfram.com/TotientSummatoryFunction.html — full text
at `research/sources/mathworld-totient-summatory-function.full.md`
[[mathworld-totient-summatory-function.full]]

## What this source establishes

Definition. Φ(n) = Σ_{k=1..n} φ(k) (eq. 1).

**Möbius-inversion identities (eqs. 2–4).**

    Φ(n) = Σ_{m=1..n} m Σ_{d|m} μ(d)/d
         = Σ_{d=1..n} μ(d) Σ_{d'=1..⌊n/d⌋} d'
         = (1/2) Σ_{d=1..n} μ(d) ⌊n/d⌋ (1 + ⌊n/d⌋)

(Hardy and Wright 1979, p. 268). The last form is exactly the formula
`code/verify_mobius.py` implements to independently recompute Φ(10⁸).

**Asymptotics.** Φ(x) ~ 3x²/π² + O(x log x) (Perrot 1881; Nagell 1951; Hardy
and Wright 1979, p. 268); Walfisz (1963) gives
Φ(x) = 3x²/π² + O(x (log x)^{2/3} (log log x)^{4/3}).

First values 1, 2, 4, 6, 10, 12, 18, 22, 28, … (OEIS A002088).

## Hypotheses

n ≥ 1 integer for the exact identities; the asymptotic is for real x. All
hold here.

## What it lets this run do

- Independent sourcing of the Möbius-inversion route to Φ(10⁸) (the exact
  formula used by verify_mobius.py).
- Magnitude anchor: Φ(10⁸) ≈ 3·10¹⁶/π² ≈ 3.0396×10¹⁵, confirming that the
  run's Φ(10⁸)=3039635516365908 has the correct size (and that the erroneous
  "303963552391" — Φ(10⁶) — does not).

## What it does not settle

- No algorithm with complexity bound; that is Brown's paper.
- No specific value of Φ(10⁸).

## Claims

```claim
id: summatory-totient-mobius-identity
statement: Φ(n) = (1/2) Σ_{d=1..n} μ(d)⌊n/d⌋(1+⌊n/d⌋).
hypotheses: n ≥ 1 integer.
holds-here: yes — implemented in verify_mobius.py, exact agreement with the
totient sieve at n = 10^8.
status: checked — verify_mobius.py implements this identity with an int8 μ
sieve and agrees exactly with the totient sieve at N = 10^8
(Φ(10^8) = 3039635516365908); identity sourced from Wikipedia and MathWorld.
bearing: the independent second computation of Φ(10^8)=3039635516365908.
anchor: research/summaries/mathworld-totient-summatory-function.md
```

```claim
id: totient-magnitude-anchor
statement: Φ(x) = 3x²/π² + O(x log x); hence Φ(10^8) ≈ 3.0396×10^15.
hypotheses: none beyond the asymptotic.
holds-here: yes — computed ratio Φ(10^8)/10^16 = 0.303964 vs 3/π² = 0.303964.
status: sourced (MathWorld TotientSummatoryFunction eq. (6); Walfisz 1963)
bearing: rules out any four-orders-of-magnitude error in Φ(10^8); the correct
value must be ≈ 3.04×10^15, which 3039635516365908 is and 303963552391 is not.
anchor: research/summaries/mathworld-totient-summatory-function.md
```
