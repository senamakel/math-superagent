# Frankl's conjecture for large semimodular and planar semimodular lattices

Gábor Czédli, E. Tamás Schmidt. _Acta Universitatis Palackianae Olomucensis.
Facultas Rerum Naturalium. Mathematica_ 47 (2008), no. 1, 47–53.
Persistent URL: http://dml.cz/dmlcz/133405
Full text (proof read): `research/sources/czedli-schmidt-full.pdf.full.md`

<!-- source: https://dml.cz/bitstream/handle/10338.dmlcz/133405/ActaOlom_47-2008-1_5.pdf -->

## What it establishes (primary source, full proof read)

Two broad classes of finite semimodular lattices satisfy Frankl's conjecture
(lattice form: some nonzero join-irreducible `f` with `|↑f| ≤ |L|/2`).

**Theorem 1 (large semimodular):** If `|L| > 5·2^(m−3)` where `m = |J(L)|` is
the number of nonzero join-irreducibles, then `L` satisfies Frankl's conjecture.
Proof: first show `|J(L)\A(L)| ≤ 1`; then construct an explicit injection
`↑a₁ → L\↑a₁` via `x ↦ y(x)` with `a₁ ∨ y = x` and `y ∉ ↑a₁`. Corollary 1
strengthens the size threshold to `|L| > 6·2^(m−3)` ⇒ `J(L)=A(L)`.

**Theorem 2 (planar semimodular):** Every finite semimodular planar lattice `L`
satisfies Frankl's conjecture; if `|L| ≥ 4` and its greatest element is
join-reducible, there are *two* distinct join-irreducible `f₁,f₂` with
`|↑fᵢ| ≤ |L|/2`. Proof uses the Grätzer–Knapp structure theorem for planar
semimodular lattices (slim case via a grid/congruence induction, then inserting
doubly irreducible elements into covering squares).

The paper explicitly states that whether *all* (upper) semimodular lattices
satisfy Frankl's conjecture is **open and much harder** than the lower
semimodular case (Reinhold).

## Why it matters for this run

Primary source confirming ROOT.md's class claims previously sourced only "by the
survey". It fixes exact hypotheses:
- large semimodular (size > 5·2^(m−3)): settled;
- planar semimodular: settled;
- upper semimodular general: open.

Also records (via citation list) the low-semimodular results: Abe–Nakano
(modular, 1998), Abe–Nakano (lower quasi-semimodular 2000), Reinhold (lower
semimodular 2000), Herrmann–Langsdorf (lower semimodular preprint).

```claim
id: czedli-schmidt-large-semimodular
statement: Every finite large semimodular lattice L (|L| > 5·2^(m−3),
  m=|J(L)|) satisfies Frankl's conjecture; if |L| > 6·2^(m−3) then J(L)=A(L).
hypotheses: L finite semimodular lattice of the stated size.
holds-here: true
status: proved
bearing: settles the large semimodular class from the primary source.
anchor: Czédli–Schmidt 2008, Theorem 1 & Corollary 1; full text in research/sources.
```

```claim
id: czedli-schmidt-planar
statement: Every finite semimodular planar lattice satisfies Frankl's
  conjecture; if |L| ≥ 4 and 1 is join-reducible then there are two distinct
  join-irreducible f₁,f₂ witnessing it.
hypotheses: L finite semimodular planar lattice.
holds-here: true
status: proved
bearing: settles the planar semimodular class from the primary source.
anchor: Czédli–Schmidt 2008, Theorem 2; full text in research/sources.
```

```claim
id: upper-semimodular-open
statement: Whether every finite upper semimodular lattice satisfies Frankl's
  conjecture is OPEN; this is the difficult lattice-theoretic case, in contrast
  to the settled lower semimodular case.
hypotheses: none (state of the art as of 2008; still open per Joshi–Waphare 2019).
holds-here: true
status: asserted
bearing: identifies the fault line for the lattice attack line: upper
  semimodular lattices are the open case.
anchor: Czédli–Schmidt 2008 (intro); Joshi–Waphare 2019 (intro).
```
