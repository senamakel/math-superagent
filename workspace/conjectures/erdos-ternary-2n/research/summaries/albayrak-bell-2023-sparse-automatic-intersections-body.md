# Albayrak & Bell, "Quantitative estimates for the size of an intersection of sparse automatic sets" — HELD IN FULL

Source: arXiv:2304.09223 (2023, cs.FL/math.NT). Full text:
`research/sources/albayrak-bell-2023-sparse-automatic-intersections-body.full.md`
(58 KB, ar5iv capture); abstract page in
`research/sources/albayrak-bell-2023-sparse-automatic-intersections.full.md`.

## What it proves

- **Theorem 1.1 (quantitative Cobham–Séné for sparse sets).** If `k, ℓ` are
  multiplicatively independent and `X ⊆ ℕ^d` is a sparse `k`-automatic set,
  `Y ⊆ ℕ^d` a sparse `ℓ`-automatic set, then `X ∩ Y` is **finite**, with an
  effectively computable upper bound on its size in terms of `d, k, ℓ` and the
  state counts of the minimal automata (explicit form in Theorem 4.1).
- **Sparse** means polylogarithmic counting: `|{w ∈ L : |w| ≤ n}| = O(n^d)`.
  Automatic sets satisfy a dichotomy (Prop 2.1 / Prop 5.2): either positive
  lower density, or `O(x^{1-ε})` for some `ε > 0`.
- **Conjecture 5.3** (their own, new): if `X` is a sparse `k`-automatic set and
  `Y` a **zero-density** `ℓ`-automatic set, then `X ∩ Y` is finite. They give a
  heuristic (summability of `Σ 1/i_j^ε` over the sparse set) and note this is
  **well beyond current methods**.

## The precise bearing on Erdős's conjecture — this is the honest answer

The paper *explicitly* frames the Erdős conjecture as the intersection of
`X = {2^i}` (2-automatic, sparse) with `Y = {numbers whose ternary expansion
avoids digit 2}` (3-automatic). Key facts:

- **Theorem 1.1 does NOT apply to the Erdős case.** The digit-avoiding set
  `Y` is **zero-density but NOT sparse**: it has `≈ x^(log_3 2)` elements up
  to `x`, i.e. `≈ 2^k` elements with `k` ternary digits — polynomial, not
  polylogarithmic in the input length. So the sparse-∩-sparse finiteness
  theorem is out of reach for this configuration.
- The Erdős conjecture is exactly the **sparse × zero-density** intersection
  question, which they pose as Conjecture 5.3 and call "well beyond what
  current methods in number theory can handle."
- On decidability (the question problem.md raises about Cobham/Büchi/Walnut):
  the paper cites Hieronymi–Schulz showing that Presburger arithmetic plus two
  multiplicatively-independent automatic predicates (neither Presburger
  definable) has **undecidable** first-order theory, so no clean decidability
  route applies. Deciding emptiness of such an intersection is "apparently
  very difficult and connected to highly non-trivial Diophantine questions
  that are not known to be decidable."

The paper quotes Erdős verbatim on p. 33 / [15, p. 67]: *"as far as I can see,
there is no method at our disposal to attack this conjecture."*

```claim
id: ALBAYRAK-BELL-ERDOS-AS-SPARSE-ZERODENSITY-INTERSECTION
statement: The Erdős ternary conjecture is exactly the special case (k=2, l=3)
  of Conjecture 5.3: a sparse k-automatic set (powers of 2) intersecting a
  zero-density l-automatic set (numbers omitting digit 2 in base 3) is finite.
  The sparse x sparse finiteness theorem (Thm 1.1) does NOT apply because the
  digit-avoiding set is zero-density but not sparse (~x^(log_3 2) elements).
hypotheses: k,l multiplicatively independent; X sparse automatic; Y zero-density
  automatic.
holds-here: yes -- places the conjecture inside the automatic-set intersection
  theory and states precisely that general sparse-∩-sparse machinery misses it.
status: proved-in-source for the framing; Conjecture 5.3 itself is a conjecture
  (open), and deciding such intersections is undecidable/very hard in general.
bearing: answers problem.md's flagged question whether Cobham/Buechi/Walnut
  decidability applies. It does not give finiteness; the case is genuinely the
  hard sparse x zero-density gap, and no decidability machinery reaches it.
anchor: research/sources/albayrak-bell-2023-sparse-automatic-intersections-body.full.md
```

## Status

Primary source, held in full. The most precise current statement that the
Erdős conjecture sits inside the automatic-set intersection problem and that
Cobham-type machinery is silent on it — this is the honest recorded answer to
the "automatic sequences and finite automata" lead in problem.md.
