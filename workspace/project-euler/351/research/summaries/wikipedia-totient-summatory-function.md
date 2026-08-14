# Wikipedia — Totient summatory function

Source: https://en.wikipedia.org/wiki/Totient_summatory_function — full text at
`research/sources/wikipedia-totient-summatory-function.full.md` [[wikipedia-totient-summatory-function.full]]

## What this source establishes

Definition. Φ(n) := Σ_{k=1..n} φ(k), the summatory totient. It counts the
ordered coprime pairs (p,q) with 1 ≤ p ≤ q ≤ n.

**Implicit recurrence (the property this run uses).** For all real n ≥ 0:

    Σ_{d=1..n} Φ(⌊n/d⌋) = ⌊n⌋⌊n+1⌋/2 = n(n+1)/2 for integer n.

This is a direct consequence of Gauss's identity Σ_{d|m} φ(d) = m, summed over
m ≤ n and regrouping by d. Rearranging gives the floor-grouped recursion

    Φ(n) = n(n+1)/2 − Σ_{d=2..n} Φ(⌊n/d⌋),

which is the sublinear (O(√n) distinct values, O(n^{2/3}) with memoisation)
route to Φ(10^8). Note the claim in research/notes anchors the Gauss identity to
MathWorld TotientFunction eq. (15), Σ_{d|n}φ(d)=n, which the MathWorld full text
confirms verbatim.

**Möbius-inversion identity (independent verification route).**

    Φ(n) = Σ_{k=1..n} k Σ_{d|k} μ(d)/d = (1/2) Σ_{k=1..n} μ(k)⌊n/k⌋(1+⌊n/k⌋).

This is exactly the identity `code/verify_mobius.py` implements.

**Asymptotic.** Φ(n) ~ 3n²/π² + O(n log n) (Walfisz improves the error to
O(n (log n)^{2/3}(log log n)^{4/3})).

**Catalogued values.** Φ(10^k) = 1, 32, 3044, 304192, 30397486, 3039650754, …
(OEIS A064018), consistent with the run's check values up to Φ(10⁸)=3039635516365908.

## Hypotheses

All identities hold for integer n ≥ 1; no further hypotheses. The recurrence and
Möbius formula both hold-here.

## What it lets this run do

- Justifies the sublinear recursion (route (b) of the thread) as a third
  independent way to reach Φ(10⁸).
- Justifies verify_mobius.py's formula, the second verification route that
  agrees exactly with the totient sieve.

## What it does not settle

- Does not give Φ(10⁸) itself; that comes from OEIS A064018 and the run's own
  two-sieve computation.

## Claims

```claim
id: gauss-divisor-sum-of-totient
statement: Σ_{d|n} φ(d) = n for every positive integer n (Gauss); hence
Σ_{d=1..n} Φ(⌊n/d⌋) = n(n+1)/2, which rearranges to the summatory recursion
Φ(n) = n(n+1)/2 − Σ_{d=2..n} Φ(⌊n/d⌋), evaluated in O(√n) distinct floor
values with memoisation.
hypotheses: n ≥ 1 integer.
holds-here: yes — all hypotheses hold; recursion verified against the sieve
values at n = 10, 10^3, …, 10^8 by patterns.py (A063985 recursion probe).
status: sourced (MathWorld TotientFunction eq. (15); Wikipedia Totient
summatory function "Properties")
bearing: sublinear route to Φ(10^8); second independent verification path.
anchor: research/summaries/wikipedia-totient-summatory-function.md
```

```claim
id: summatory-totient-mobius-identity
statement: Φ(n) = (1/2) Σ_{k=1..n} μ(k)⌊n/k⌋(1+⌊n/k⌋), μ the Möbius function.
hypotheses: n ≥ 1 integer.
holds-here: yes — implemented in verify_mobius.py and agreeing exactly with the
totient sieve at n = 10^8.
status: checked — verify_mobius.py implements this identity and agrees
exactly with the totient sieve at N = 10^8; identity sourced from Wikipedia
and MathWorld.
bearing: independent computation of Φ(10^8) = 3039635516365908, the second
verification route.
anchor: research/summaries/wikipedia-totient-summatory-function.md
```
