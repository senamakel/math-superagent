# Tao, *Higher Order Fourier Analysis* (AMS GSM 142, 2012)

<!-- source: https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf | converted from PDF -->
<!-- full text: [[tao_higher_order_fourier_analysis.full]] -->

Author's preliminary version (book published by the AMS). The complete text is
at `research/sources/tao_higher_order_fourier_analysis.full.md`.

## Why it is in the library

The reopened question (GOAL priority 2) asks whether a **functional of the
fold sensitive to correlation order `K`, `1 < K ≲ n/2`**, is controllable by an
arithmetic input strictly weaker than pointwise mod-4 switch density. "Order"
is the vocabulary of higher-order Fourier analysis: Gowers uniformity norms,
their inverse theory, and polynomial equidistribution. This is the standard
reference, cited twice by the library's own Gowers-norm sources
(Byszewski–Konieczny–Müllner; Konieczny) but previously not held.

## What it establishes (verified against the text)

- **Gowers norms and the inverse conjecture (§1.5, lines 4411–4520).** For a
  finite-dimensional space `V/F` of characteristic p, a function with
  `‖f‖_{U^{d+1}(V)}` near 1 is close to a degree-≤d polynomial phase; the 1%
  inverse theorem (Thm 1.5.3, `char(F) > d`) says large `U^{d+1}` norm
  implies correlation with a degree-≤d polynomial phase. Over finite fields this
  is the inverse conjecture for the Gowers norm (d=2: Green–Tao; low
  characteristic d=2: Samorodnitsky; higher d: Tao–Ziegler et al.).
- **Classical vs non-classical polynomials, and the low-characteristic caveat
  (§1.4, lines 3560–3705).** A polynomial is **classical** if it takes values in
  the p-th roots of unity (identified with F). Corollary 1.4.2: if `p > d`
  (high characteristic), every degree-≤d polynomial is classical up to a
  constant. If `p ≤ d` (low characteristic, in particular **p = 2**), there are
  **non-classical** polynomials (e.g. `P(0)=0, P(1)=1/4` on F₂ is a quadratic
  but not a shifted classical polynomial, since its range is not a translate of
  the second roots); Tao then *restricts to the high-characteristic case* and
  notes the low-characteristic theory of non-classical polynomials is partly
  not in the literature.
- **Equidistribution of polynomial sequences (§1.1):** a degree-`s` polynomial
  with an irrational leading coefficient equidistributes; Weyl and van der
  Corput bounds quantify the error. The energy/regularity machinery (Roth, §1.2)
  and the linear-equations-in-primes framework (§1.7) are the higher-order
  analogues.

## Bearing on SUPPLY (honest)

**Structural and cautionary, not a key.** The book supplies the exact language
for "correlation order `K`": under the inverse conjecture, an order-K functional
being blind is equivalent to the input being orthogonal to K-th-order
(degree-(K−1)) polynomial phases. Door 3 (Thue–Morse, sublinear `ν₂` but
Gowers-uniform of all orders — Konieczny) is exactly an input invisible to
*every* finite-order correlation. So the book sharpens what any `1<K` control
input must look like, but **does not transfer** to the fixed finite-string fold
`wt(Φ_n h)` on the prime gap-parity string: the fold input is neither a
nilsequence nor one whose higher correlations are known.

**The low-characteristic caveat is the piece with the most direct bearing.**
SUPPLY's fold is over F₂, the paradigm low-characteristic case. Tao's classical
polynomial description and the clean inverse theory he states are for
`p > d`; the F₂ fold lives in the `p ≤ d` regime where non-classical polynomials
appear and where Tao himself says the theory is harder and partly unavailable.
So the "order-K functional blind ⇔ orthogonal to nilphases" inversion that this
pass's vocabulary leans on is **not established at characteristic 2 with
control on the constants** by this source — a caveat the run's inverse-theoretic
framing must not assume away.

## What it does NOT do

- No bound on `wt(Φ_n h)`: the book is about the *structure* of correlation.
- Does not touch consecutive-prime residue frequencies (the mod-4 switch side).
- Request `walsh-spectral-subset-b904` remains a gap in *theorems*, not in the
  library. Tao neither provides the requested lower bound nor the finite-prefix
  / index-domain transfer (the run's own open step).

## Claim blocks

```claim
id: tao-inverse-conjecture-blind-iff-nilphase-orthogonal
statement: Under the inverse conjecture for the Gowers U^{d+1} norm, an order-d+1 functional that sees no correlation is blind to Fourier at all orders iff the input is orthogonal to d-step nilphases (finite-field form: degree-≤d polynomial phases); large U^{d+1} norm forces correlation with such a phase.
hypotheses: char(F) > d (high characteristic); f bounded with L1 ≤ 1; inverse conjecture (proved over finite fields).
holds-here: unchecked — the identified obstruction is valid (door 3 Thue-Morse is all-order Gowers-uniform), but the rigorous transfer to the fixed F2 fold is absent and the characteristic-2 constants are not controlled by this source.
status: sourced (Tao GSM 142, Thm 1.5.3 / Cor 1.4.2)
bearing: Names the exact obstruction any 1<K functional must beat: a fully Gowers-uniform collapse witness (Thue-Morse) is invisible to every finite-order correlation, so the control input must come from outside finite-order correlations of h.
anchor: research/sources/tao_higher_order_fourier_analysis.full.md
```

```claim
id: tao-low-characteristic-nonclassical-polynomial-unavailable
statement: Over a finite field of characteristic p, every degree-≤d polynomial is classical (a phase over p-th roots) up to a constant iff p > d (Cor 1.4.2). If p ≤ d — in particular p = 2 — non-classical polynomials occur (e.g. P(0)=0, P(1)=1/4 on F2 is a quadratic but not a shifted classical polynomial), and Tao restricts to the high-characteristic case; a full low-characteristic theory of non-classical polynomials is not currently in the literature.
hypotheses: V = F_p^n; d ≥ 0; classical = values in p-th roots of unity identified with F_p.
holds-here: yes — SUPPLY's fold is over F2, the paradigm low-characteristic case, so this caveat applies directly.
status: sourced (Tao GSM 142, §1.4, Cor 1.4.2 and the passage after it)
bearing: The "order-K-functional-blind ⇔ orthogonal to nilphases" inversion that GOAL's K>1 vocabulary leans on is NOT cleanly available at characteristic 2 by this source. Any claim that a K>1 functional of the F2 fold is controllable by an input weaker than switch density must not silently import the high-characteristic inverse theory.
anchor: research/sources/tao_higher_order_fourier_analysis.full.md lines 3560-3705
```

## Not helpful here

For the *specific* gap (a Walsh/subset-sum lower bound, or a finite-prefix /
index-domain transfer for the prime gap-parity string) it does not help; it is
in the library because the reopened question is framed in its vocabulary and its
own sources cite it. Read once for the vocabulary and the char-2 caveat.
