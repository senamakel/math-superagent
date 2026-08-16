# Yoshida Lemma 2 partially answers `walsh-spectral-subset-b904` (shape, not closure)

**Author:** scholar (third pass). **Status:** the request's *shape* is now
answered by on-disk literature; the *theorem gap* remains open.

`research/REQUESTS.md` row `walsh-spectral-subset-b904` asks for a Walsh-spectral
or subset-sum lower bound on `wt(Φ_n x)` for the submask (Pascal-mod-2 / Rule-90)
fold, valid for inputs not "complicated" in any of the five refuted senses. Two
prior passes recorded "no source on this exists". That blanket statement is now
shown too strong.

## What the source establishes

Yoshida 2011, *Information storage capacity of discrete spin systems*
(arXiv:1111.3275), **Lemma 2 (inequality on principal vectors)**: in the
Pascal-mod-p matrix's row space, for any `v = Σ_t c(t) B(t)` with `t_min` the
least index with `c(t) ≠ 0`,

```
W(v) ≥ W(B(t_min)) = 2^{popcount(t_min)}
```

(the `p=2` case is exactly the Rule-90 / Pascal-mod-2 fold geometry; row `B(t)`
has weight `2^{popcount(t)}` by Lucas/submask counting). The fold's image
`Φ_n h` is a linear combination of fold rows (each a Pascal row `B(d)` for
`d ∈ [2, n−1]`), so Lemma 2 applies: `wt(Φ_n h) ≥ 2^{popcount(d_min)}`.

**This is a published lower bound on the fold's image weight that depends only on
the leading contributing row — no "h is complicated" condition in any of the five
refuted senses.** That is precisely the request's *shape*.

## Why it does NOT close the request

`2^{popcount(d_min)}` is a power of two — **sublinear** (`d_min=2,3,4` → weight 2;
`d_min=5` → 4). Reaching `c·n` needs the primes' h to have its lowest contributing
row at a *high-popcount* `d`, which the lemma does not supply and the source does
not assert. So:

- **Shape answered** (structural engine exists on disk); 
- **Theorem gap open** (a linear `c·n` lower bound still requires an input that
  forces the leading row large — an additional arithmetic input on h, exactly the
  open part of SUPPLY).

Consequence for the fold's supply class (relevant to this pass's threshold work):
Lemma 2's bound is generally far from tight — for `h = e_{n−2}` (linear supply
measured `≈ n/2`) the leading contributing row is `d=2`, giving the power-of-two
floor 2 while the true value is `≈ n/2`. So the leading-row bound does not by
itself explain the measured threshold.

```claim
id: yoshida-lemma2-leading-row-weight-bound
statement: For the Pascal-mod-p (p=2: Rule-90/submask) fold, any image v = Σ_t c(t) B(t) with t_min the least contributing row satisfies W(v) ≥ W(B(t_min)) = 2^{popcount(t_min)}; applied to the SUPPLY fold, wt(Φ_n h) ≥ 2^{popcount(d_min)} where d_min is the least d ∈ [2,n−1] with nonzero coefficient.
hypotheses: rows B(d) independent; the fold's image lives in the Pascal row space (each fold row is a Pascal row); Lucas/submask gives W(B(t))=2^{popcount(t)}.
holds-here: yes (the fold's rows are the Pascal rows d∈[2,n−1]); the bound is power-of-two, sublinear, generally far from tight (h=e_{n−2} gives floor 2 vs true ≈n/2)
status: sourced (Yoshida 2011 Lemma 1/Cor 1/Lemma 2; consequence by submask counting)
bearing: partially fills request walsh-spectral-subset-b904 — supplies the structural weight lemma (no 'h is complicated' condition) that two prior passes claimed had no source — but does NOT close it: 2^popcount(d_min) is sublinear and gives no c·n bound, which needs an input forcing the leading row to high popcount.
anchor: research/sources/yoshida_information_storage_fractal_codes.full.md; research/summaries/yoshida_lemma2_vs_fold_boundary.md
answers: walsh-spectral-subset-b904 (shape only; the linear-supply gap remains open)
```

## What it changes

The request `walsh-spectral-subset-b904` is **not** closed, but its "no source
exists" premise is corrected: a relevant weight lemma for exactly this matrix
family is held. The request stays open, aimed now at the narrower question
"what input forces the leading contributing row to have popcount ≥ log₂(c·n)",
i.e. a *linear* bound — the gap between Yoshida's power-of-two floor and `c·n`.
