# Frankl's Conjecture for a subclass of semimodular lattices

Vinayak Joshi, B.N. Waphare. _Categories and General Algebraic Structures with
Applications_ 11, Special Issue (2019), 197–206. doi:10.29252/cgasa.11.1.197
Full text: `research/sources/joshi-waphare-semimodular-2019-pdf.full.md`

<!-- source: https://doi.org/10.29252/cgasa.11.1.197 ; PDF:
https://cgasa.sbu.ac.ir/article_85730_9c926c8729189f4e871a4fed07a012e5.pdf -->

## What it establishes (primary source, full proof read)

The lattice (Poonen/Stanley) form of Frankl's conjecture: every finite lattice
`L` with `|L| ≥ 2` has a nonzero join-irreducible `j` with
`|{x ∈ L : j ≤ x}| ≤ |L|/2`. The paper proves it for two concrete classes.

**Theorem 1.3(A):** If the greatest element `1` of `L` is join-irreducible, or
is the join of two join-irreducibles, then `L` satisfies Frankl's conjecture.
Corollary: **every lattice of breadth at most two satisfies Frankl's conjecture.**
Proof is short and elementary (an injection `[j) → L\[j)`).

**Theorem 1.3(B):** If `L` is upper semimodular and `|J(L) \ A(L)| ≤ 3` (all
join-irreducibles except at most three are atoms), then `L` satisfies Frankl's
conjecture. Uses Stern's lemma (`x+ ≤ x′` in upper semimodular lattices) to build
the injection.

**Lemma 2.3 / Corollary 2.4 (re-proves Czédli–Schmidt):** If `L` is a *large*
semimodular lattice (`|L| > 5·2^(m−3)`, `m = |J(L)|`), then `|J(L)\A(L)| ≤ 1`,
and consequently `L` satisfies Frankl's conjecture.

Also: adjunct-operation and linear-sum preservation lemmas (Thm 2.7, 2.8,
Cor 2.9), extending the class of lattices known to satisfy the conjecture.

## Why it matters for this run

This is a **primary source confirming the lattice-class claims** that ROOT.md
had previously sourced only "asserted by the survey". It pins down:
- breadth ≤ 2 lattices: settled;
- upper semimodular in general: **open** (explicitly stated as the difficult
  lattice case) — this is the fault line worth attacking;
- upper semimodular with `|J(L)\A(L)| ≤ 3`: settled.

The breadth-two proof is elementary enough to be the model for a structural
attack on a minimal counterexample.

```claim
id: joshiwaphare-breadth2
answers: lattice-settled-classes
statement: Every finite lattice of breadth at most two satisfies Frankl's
  conjecture (lattice form): a nonzero join-irreducible j has |[j)| ≤ |L|/2.
hypotheses: L finite lattice, |L| ≥ 2, breadth(L) ≤ 2.
holds-here: true
status: proved
bearing: settles breadth ≤ 2 (hence dismantlable, hence planar) from a primary
  source; the elementary injection proof is a model for attacking a minimal
  counterexample.
anchor: Joshi–Waphare 2019, Theorem 1.3(A); full text in research/sources.
```

```claim
id: joshiwaphare-upper-semimodular-3
statement: If L is finite upper semimodular with |J(L) \ A(L)| ≤ 3, then L
  satisfies Frankl's conjecture.
hypotheses: L finite upper semimodular lattice, |J(L)\A(L)| ≤ 3.
holds-here: true
status: proved
bearing: settles a subclass of the (open) upper semimodular case; the general
  upper semimodular case remains open and is stated as the difficult lattice case.
anchor: Joshi–Waphare 2019, Theorem 1.3(B).
```

```claim
id: joshiwaphare-large-semimodular
answers: czedli-schmidt-planar
statement: If L is a large semimodular lattice (|L| > 5·2^(m−3), m=|J(L)|), then
  |J(L)\A(L)| ≤ 1 and L satisfies Frankl's conjecture.
hypotheses: L finite semimodular lattice, |L| > 5·2^(m−3).
holds-here: true
status: proved
bearing: independent primary-source confirmation of the Czédli–Schmidt large
  semimodular result.
anchor: Joshi–Waphare 2019, Lemma 2.3 / Corollary 2.4.
```
