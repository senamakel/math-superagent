# On the Scope of Averaging for Frankl's Conjecture

Gábor Czédli, Miklós Maróti, E. Tamás Schmidt. _Order_ 26 (2009), 31–48.
doi:10.1007/s11083-008-9105-5.
Full text (read, OCR'd): `research/sources/czedli-maroti-schmidt-scope-averaging-2009.full.md`

<!-- source: https://www.math.u-szeged.hu/~czedli/m/publ.pdf/czedli-maroti-schmidt_on-the-scope-of-averaging-Frankl's-conjecture.pdf -->

## What it establishes (primary source, read)

Let `F` be a union-closed family of subsets of an `m`-element set `A`, `n = |F|`,
`∅ ∈ F`. For `b ∈ A` set `w(b)` = (# sets in `F` containing `b`) − (# sets not
containing `b`). Frankl's conjecture is: some `b` has `w(b) ≥ 0`.

The **averaged Frankl property** is: the average of the `w(b)` over all `b ∈ A`
is nonnegative. This is much stronger than Frankl's conjecture and does *not*
hold for all union-closed families. The first author (Czédli, "On averaging
Frankl's conjecture for large union-closed sets", JCTA 116 (2009) 724–729) had
verified the averaged property whenever `n ≥ 2m − 2^(m/2)`, `m ≥ 3`.

**Main result of this paper:** for the threshold `2^(m/2)` in the averaged
property,
1. **one cannot replace** `2^(m/2)` with the *upper* integer part of `2^(m/3)`
   (a counterexample shows the bound `2^(m/2)` cannot be pushed that far);
2. **if Frankl's conjecture holds** at least for `m`-element base sets and
   `n ≥ 2m − ⌊2^(m/3)⌋`, then the averaged Frankl property holds — i.e. in
   that conditional range `2^(m/2)` can be replaced by the *lower* integer part
   of `2^(m/3)`.

Proof combines elementary combinatorics and lattice theory; self-contained.

## Why it matters for this run

This is a primary source on the **limitations of the averaging method** — it
proves the averaged property is conditional and shows a concrete obstruction to
improving the averaging threshold. It is directly relevant to the "what can a
method achieve" question in ROOT.md: averaging is bounded away from solving the
conjecture, precisely because the averaged Frankl property fails outright for
some families and the best unconditional threshold is `2^(m/2)`.

It also fixes the lattice-form framework citations (Stanley, Poonen for the
lattice version; Abe–Nakano, Herrmann–Langsdorf, Reinhold for lattice classes).

```claim
id: cms-averaged-frankl-wrong
statement: The averaged Frankl property (average over b of w(b) is nonnegative)
  does NOT hold for all union-closed families; the averaging method has
  intrinsic limits.
hypotheses: F union-closed, finite, m = |A|.
holds-here: true
status: proved
bearing: establishes that a pure-averaging proof cannot solve the conjecture;
  bounds what the averaging method can achieve.
anchor: Czédli–Maróti–Schmidt, Order 26 (2009), §1; full text in research/sources.
```

```claim
id: cms-averaged-threshold
statement: The first author verified the averaged Frankl property whenever
  n ≥ 2m − 2^(m/2) (m ≥ 3); one cannot replace 2^(m/2) with the upper integer
  part of 2^(m/3); and if Frankl's conjecture holds for m-element base sets,
  the averaged property holds for n ≥ 2m − ⌊2^(m/3)⌋.
hypotheses: F union-closed over m-element set, n=|F|.
holds-here: true
status: proved
bearing: quantifies exactly how far averaging can be pushed and the obstruction
  beyond it.
anchor: Czédli–Maróti–Schmidt, Order 26 (2009), main theorem; full text in sources.
```
