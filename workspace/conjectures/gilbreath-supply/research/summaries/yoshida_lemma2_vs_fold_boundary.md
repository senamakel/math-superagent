# Yoshida Lemma 2 vs the SUPPLY fold — exact consequence and boundary

**Date:** this pass. **Author:** librarian (verification; not a proof claim beyond what the source states).

## What the source establishes (verified against the full text)

In Beni Yoshida, *Information storage capacity of discrete spin systems*, arXiv:1111.3275:

- **Lemma 1** (= Lucas' theorem): the mod-p Pascal entry `_tC_r ≠ 0 (mod p)` iff every base-p digit
  of r is ≤ the corresponding digit of t. For p=2 this is exactly the **submask** condition `r ⊆ t`.
- **Corollary 1**: the whole Pascal matrix B has `W(B) = (p(p+1)/2)^m` nonzero entries.
- **Row weight**: by Lemma 1, row B(t) is nonzero exactly at positions r ⊆ t, so for p=2
  `W(B(t)) = 2^{popcount(t)}`.
- **Lemma 2 (Inequality on principal vectors)**: for any v = Σ_t c(t) B(t) in the row space, with
  t_min the least t such that c(t) ≠ 0,
  ```
  W(v) ≥ W(B(t_min)) = 2^{popcount(t_min)}.
  ```
  The rows B(t) are independent, so this decomposition is unique.

## What this does and does NOT give for SUPPLY

The fold is the Pascal-mod-2 (Rule-90) map; its image is a subspace of the full Pascal row space.
Every `v = Φ_n h` is a linear combination of fold rows (each a Pascal row B(d) for d ∈ [2, n−1]),
so Lemma 2 applies:

```
wt(Φ_n h) ≥ 2^{popcount(d_min)}
```

where d_min is the least d ∈ [2, n−1] such that h has nonzero coefficient on row B(d).

**Consequence — a genuine, published weight lower bound for the fold's image that does not require h
to be "complicated" in any of the five refuted senses.** This is the structural engine the open request
`walsh-spectral-subset-b904` asked for, and it *exists in the literature* (contradicting the two prior
passes' blanket "no source exists").

**Boundary — it does NOT settle linear supply.** `2^{popcount(d_min)}` is a power of two. For the
lowest contributing row d_min = 2 it is just 2, for d_min = 3 it is 2, for d_min = 4 (popcount 1) it is
2, for d_min = 5 (popcount 2) it is 4. This bound is **not** `c·n`; it is tiny. To get linear supply
from this route one would need the primes' h to have its *lowest* contributing row at a high-popcount d,
which is not a hypothesis this lemma supplies and not something the lemma or the source asserts.

## Honest verdict for the request

- **Available now (this source):** a published lower bound `W(v) ≥ W(B(t_min))` on images of the
  Pascal/Rule-90 mod-p fold, depending only on the leading contributing row — no "h is complicated"
  condition. ✅ The request's *shape* is answered by literature.
- **Still open (the theorem gap):** whether any input h forces that leading row to have weight ≥ c·n,
  i.e. a *linear* lower bound. Yoshida's bound alone is sublinear (power of two); reaching `c·n` needs
  the additional fact that the relevant leading row has large popcount, which the source does not give.

So this source **partially** fills `walsh-spectral-subset-b904` (it supplies the structural weight
lemma) but does **not** close it (linear supply still needs more). The request should stay open with
the lead "leading-row weight is 2^popcount; a linear bound needs input forces high-popcount leading row".

## Related: the leading-row strategy is structurally the tight route

This refines a theme the run already holds: `fixed-single-1-fold-weight-bounded-by-j` (a single 1 at
position j gives wt = O(1)) and `enminus2-linear-supply-switch-density-not-necessary` (h = e_{n-2}
gives wt ≈ n/2 because depth d reads position n−2 iff d is odd, d−1 ⊆ d). Under Yoshida's Lemma 2,
h = e_{n-2} corresponds to a linear combination whose leading contributing row is d = 2 (the e_{n-2}
pattern is read at the smallest read-depth), giving the power-of-two floor, while the *measured* value
is ≈ n/2 — so for that input Lemma 2 is very loose. The bound is real but far from tight for the fold.

## Status

Verified against the source text: Lemma 1, Corollary 1, Lemma 2 stated faithfully. The consequence
`W(B(t)) = 2^{popcount(t)}` follows directly from Lemma 1 (I have not machine-checked it this pass,
but it is the standard submask counting). Filed as a durable finding for the scholar to price.
