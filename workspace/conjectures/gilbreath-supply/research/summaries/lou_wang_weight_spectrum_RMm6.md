# Lou & Wang — Weight spectrum of RM(m−6, m)

**Source:** Yueying Lou, Qichun Wang, "Determining the Weight Spectrum of the
Reed-Muller Codes RM(m-6,m)", arXiv:2406.03803 (2024). Full text:
`research/sources/lou_wang_weight_spectrum_RMm6.full.md`.

## What it is

The primary research paper determining the **weight spectrum** (the *set of
distinct* Hamming weights, not the counts) of the Reed-Muller codes
`RM(m−6, m)` for `m ≥ 12`. It stands in the line that the `anf-mobius-reed-muller`
refutation cites: Carlet & Solé did `c = 3,4`; Carlet did `c = 5`; this paper
does `c = 6`.

## What it establishes

- **The weight spectra of `RM(r,m)` were unknown for `r ∈ {3, …, m−5}`**
  (its opening line), and this paper settles `r = m−6` (equivalently `c=6`) for
  `m ≥ 12` — a positive answer to an explicit previously-open case. It proposes
  a conjecture (Conjecture 1) that would, if true, settle the whole `RM(m−c,m)`
  family for fixed `c` and large `m`.
- It gives the **low-weight structural theorem** (Theorem 1, from Kasami–Tokura):
  a weight `w` of `RM(r,m)` in `[2^(m−r), 2^(m−r+1))` has the form
  `2^(m−r+1) − 2^(m−r+1−i)`. This is exactly the kind of rigidity a lower-bound
  argument wants, but it is **only for low weights** near the minimum, not a
  global lower bound.
- McEliece divisibility: weights in `RM(r,m)` are multiples of `2^⌊(m−1)/r⌋`,
  minimum nonzero weight `2^(m−r)`.

## Bearing on SUPPLY

- **It is the primary-source proof that the middle-order RM weight-spectrum
  problem driving the `anf-mobius-reed-muller` refutation is genuinely open and
  only partially settled.** Every advance only chips away specific `c`; no
  general `r ∈ {3,…,m−5}` weight spectrum/weight distribution exists. This
  hardens the refutation: the "open RM weight-spectrum" it rests on is not a
  citation handed between summaries but now a real, citable, checkable fact.
- It does **not** provide a lower bound on `wt(Φ_n h)`: it concerns attainable
  weight *spectra* of whole codes, not the weight of one folded image, and the
  low-weight theorem covers only the `[2^(m−r), 2^(m−r+1))` window. The open
  request `walsh-spectral-subset-b904` stands.

## Would-be falsifier

A weight-spectrum or weight-distribution result for a general order `r` strictly
inside `(3, m−5)` — i.e. not of the `RM(m−c,m)` penny-packet type — would change
the "open middle orders" picture. This paper gives none beyond `c=6`.
