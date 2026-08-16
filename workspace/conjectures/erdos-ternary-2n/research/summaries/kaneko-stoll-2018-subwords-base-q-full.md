<!-- source: https://arxiv.org/pdf/1707.01440 | Kaneko & Stoll, "On subwords in the base-q expansion of polynomial and exponential functions", Integers 18A (2018) -->

# Kaneko & Stoll, "On subwords in the base-q expansion of polynomial and exponential functions"

Source: arXiv:1707.01440 (2017); published Integers: Electron. J. Combin. Number Theory 18A (2018). Full text: `research/sources/kaneko-stoll-2018-subwords-base-q-full.full.md`.

## Setting

For `h` either a polynomial of degree `d ≥ 1` or an exponential `h: n ↦ m^n` (m fixed), and `w` a word of length `l` over the base-q alphabet, let `e_q(w; h(n))` = number of occurrences of `w` as a subword in the base-q expansion of `h(n)`.

## What it establishes

**Theorem 1.2 (exponential case).** Let `p` be prime, `m ≥ 2` not a power of `p`, and `w` a finite word over the base-p alphabet of length `l ≥ 1`. Then

```
limsup_{n→∞}  e_p(w; m^n) / log n  ≥  γ(w) / (l · log p),
```

where `γ(w) ≥ 1` depends on a property of the *circular shifts* of `w`. So along infinitely many (rarefied) `n`, the number of occurrences of any fixed block `w` in the expansion of `m^n` is `≥ C(w) · log n`.

Applied to this problem: `m = 2`, `p = 3`. For **any** fixed ternary word `w` — in particular the digit `2`, or blocks like `02`, `12` — there are infinitely many `n` whose base-3 expansion of `2^n` contains `≥ γ(w)/(l log 3) · log n` copies of `w`.

## Method (3-adic)

The exponential statement is proved as a statement about the map `n ↦ m^n` extended 3-adically. The proof uses how the function `g(u) = m^u` on `Z_3` behaves modulo `p^e` — its differentiability properties as `e` grows (Proposition 3.1–3.2, Lemma 3.3) — to force prescribed blocks to repeat. It is a **3-adic p-adic-function** argument.

## Relevance to this run

- Confirms and quantifies: **no fixed ternary word ever stops appearing** in `2^n`; blocks of any length recur along a subsequence with multiplicity `≳ log n`. This is the structural reason the digit-`{0,1}` restriction is the hard one — it is a restriction on *absence* of the block `2`, and this theorem only guarantees *presence* of blocks along subsequences, not that the digit-2-free subsequence is empty.
- Directly bears on the density/block-frequency framing: the low digits are controlled by the sieve, the high digits by size arguments, and this shows **middle-digit blocks are abundant along subsequences** — so a "middle digits are too dense in 2" argument must contend with `≳ log n` occurrences of arbitrary blocks.
- Puts a quantitative floor under the naive heuristic: blocks genuinely do appear roughly log-density often along thin subsequences, so any invariant that forbids `2` in the middle has to beat a genuine recurrence of that block.

## Status

Sourced, peer-reviewed (Integers, 2018). Statements quotable with the constant `γ(w)/(l log p)` made explicit. The theorem is about *presence* of blocks along subsequences, not about the *absence* that Erdős's conjecture needs — record it as the latter's blind spot, never as progress toward it.

```claim
id: KANEKO-STOLL-BLOCK-ABUNDANCE
statement: For m=2, p=3, any fixed ternary word w of length l occurs in the
  base-3 expansion of 2^n at least gamma(w)/(l·log 3) · log n times along
  infinitely many n, where gamma(w) >= 1 (Theorem 1.2).
hypotheses: p prime, m>=2 not a power of p. Here p=3, m=2 (holds).
holds-here: yes — directly constrains how often any ternary block (in
  particular the digit 2, or middle-digit blocks) recurs in 2^n.
status: sourced (peer-reviewed, Integers 18A 2018)
bearing: blocks are abundant along subsequences (multiplicity ~ log n); so a
  middle-digit obstruction must beat genuine recurrence, and this does not
  prove the absence Erdős needs.
anchor: research/summaries/kaneko-stoll-2018-subwords-base-q-full.md
```
