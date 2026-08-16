# Summary — Chebotarev density theorem in short intervals for extensions of F_q(T)

Source: Lior Bary-Soroker, Ofir Gorodetsky, Taelin Karidi, Will Sawin,
Trans. Amer. Math. Soc. 373 (2020) 597–628. arXiv:1810.06201 (verified).
Full text: `barysoroker_gorodetsky_karidi_sawin_chebotarev_short_intervals.full.md`.

## What this establishes

A function-field analogue of the short-interval Chebotarev density theorem, in
the large-finite-field limit `q → ∞`, for **any ε > 0** — the number-field
version is only reachable under GRH for `ε > 1/2`.

- **Theorem 1.2 / 5.1.** For a geometric `G`-extension `E/F_q(T)` (genus(E),
  n, |G| ≤ B; tame at infinity), the count `π_{C;q}(I(f,m); E)` of monic
  degree-n irreducibles in the short interval `I(f,m)` with Frobenius class
  `C ⊆ G` satisfies
  `| (1/q^{m+1}) π_{C;q}(I(f,m); E) − (|C|/|G|)(1/n) | ≤ M_B q^{−1/2}`.
- **G-factorization arithmetic functions (Thm 4.3).** Extends the count to any
  arithmetic function built from Frobenius/class-function data
  `⟨ψ_{E/F_q(T)}(f)⟩` over short intervals, again uniform with error `M_B q^{−1/2}`.
- **Class functions on G ≀ S_n are G-factorization (Lemma 4.2).** In particular
  the machinery covers factorization-type statistics.

## Why it matters here

This is one of the four grounding sources of the adopted `function-field-fqt-model`
approach. It grants the **one-point / value-domain / short-interval Chebotarev**
input the model's arithmetic side rests on: irreducibles with a given Frobenius
class are equidistributed in short intervals, effectively and in the large-q
limit, uniformly over the extension and interval.

**Transfer gap (load-bearing):** it is a *one-point* statement (a single
irreducible's Frobenius class in a short value-interval of degree). It does NOT
control the *degree-ordered lex-consecutive* switch statistic — two irreducibles
adjacent in the degree-then-lex order whose difference is non-zero mod T² — which
is the fold's actual two-point input. The G-factorization machinery (Thm 4.3)
handles correlations of class functions over value-shifts but not the
lex-consecutive adjacency. So the model's promised "switch-density analogue is a
provable Chebotarev statement" remains NOT granted by this source; only the
one-point side is.

```claim
id: b-g-k-s-chebotarev-short-interval
statement: Short-interval Chebotarev over F_q(T): for geometric G-extensions tame at
  infinity, the count of degree-n irreducibles in a short interval with Frobenius
  class C (and any G-factorization arithmetic function) has main term (|C|/|G|)(1/n)
  per q^{m+1} with uniform error O(q^{−1/2}), for every ε>0 in the large-q limit.
hypotheses: large finite field q → ∞; geometric G-extension, tameness at the
  infinite prime, genus(E),n,|G| ≤ B bounded.
holds-here: yes for the one-point/value-domain short-interval Chebotarev input the
  function-field model relies on; NO for the degree-ordered lex-consecutive two-point
  switch object the fold reads (never controlled here).
status: proved (Bary-Soroker–Gorodetsky–Karidi–Sawin 2020, arXiv:1810.06201).
bearing: grounds the one-point side of the adopted function-field model; the
  consecutive-switch transfer is open and is the model's own step to price.
anchor: research/sources/barysoroker_gorodetsky_karidi_sawin_chebotarev_short_intervals.full.md
```

## Keyword map
Chebotarev; short intervals; function field; Frobenius conjugacy class;
G-factorization arithmetic functions; large finite field; tame ramification.
