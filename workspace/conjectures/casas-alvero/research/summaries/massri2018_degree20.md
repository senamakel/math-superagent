# Massri, *The CA conjecture for three recycled roots in degree 20* (arXiv:1806.09561, v6 2023)

Full text: [[massri2018_degree20_html]] (arXiv HTML v6 2023, held in full since the 2026 librarian cycle; the older [[massri2018_degree20]] file is the landing page only and is superseded).

Targeted at the smallest open degree, 20 = 2²·5. The full text is now held: Theorem 7.10 (no CA-polynomial of degree 20 with three recycled roots, 3^17-case check), Theorem 7.9 (no degree-20 CA with root multiplicity ≥ 11; no degree-24 with ≥ 15), Remark 7.6 (a degree-20 CA polynomial has a common root of abs value > 19^−5), Proposition 7.7 (p-adic bound ruling out certain coincidences), Section 5-6 (finiteness and algebraic-coefficient results).

## Results claimed (from abstract)

```claim
id: massri-finiteness-psums
statement: The number of possible counterexamples in normal form of degree p^r + p^s or
  p^r + 2p^s (p prime, r,s positive integers) is finite.
hypotheses: degree of the form p^r+p^s or p^r+2p^s
holds-here: yes (a finiteness statement in the same family as Ghosh 2024's)
status: asserted-by-source (preprint)
bearing: Reinforces that counterexamples, when they exist at all in a family, are finite —
  consistent with Ghosh 2024's finiteness. Suggests finite-verification approaches for
  these degree shapes.
anchor: research/sources/massri2018_degree20.full.md (abstract)
falsifies: an infinite family of normal-form counterexamples at a fixed degree.
```

```claim
id: massri-prplus1-algebraic
statement: A possible counterexample in normal form of degree p^r + 1 has algebraic
  coefficients.
hypotheses: degree p^r+1, p prime
holds-here: yes
status: asserted-by-source (preprint)
bearing: for degree p^r+1 (e.g. 12+? = 2^2·3+1=13, or p+1 shapes) any counterexample is
  algebraic — bounds the base field the run would need for such a degree.
anchor: research/sources/massri2018_degree20.full.md (abstract)
falsifies: a held counterexample of degree p^r+1 with transcendental coefficients.
```

```claim
id: massri-degree20-no-3-recycled
statement: In degree 20 there are no counterexamples with three recycled roots.
hypotheses: degree 20, char 0
holds-here: yes
status: asserted-by-source (preprint)
bearing: Necessary-condition style result on the smallest open degree: a degree-20
  counterexample (if any) cannot use only 3 recycled roots. Compatible with (and weaker
  than) Laterveer–Ounaïes' ≥5-distinct-roots bound. A concrete partial result on degree 20.
anchor: research/sources/massri2018_degree20.full.md (abstract)
falsifies: a degree-20 counterexample using ≤3 recycled roots.
```

## What it does not settle
Degree 20 remains open (only "no 3-recycled-roots" counterexamples ruled out; a type-4+ counterexample remains possible). Massri is a preprint. The finiteness of `p^r+p^s`/`p^r+2p^s` counterexamples does not settle CA for those degrees (finite could still be nonempty).
