<!-- source: https://people.dmi.uns.ac.rs/~markovicp/papers/2007-Frankl10.pdf -->

# Marković, "An Attempt at Frankl's Conjecture" (2007) — summary

**Source URL:** https://people.dmi.uns.ac.rs/~markovicp/papers/2007-Frankl10.pdf
**Full text:** `research/sources/markovic-attempt-frankl-2007.full.md`
**Bibliographic:** Publications de l'Institut Mathématique, Nouvelle série 81(95) (2007), 29–43. DOI 10.2298/PIM0795029M.

## What this paper is

The author's qualifying paper (Vanderbilt, 2000), published 2007. It proves
Frankl's conjecture for families whose **universe (ground set) has at most 10
elements**: |⋃F| ≤ 10 ⇒ an element is in ≥ |F|/2 sets. This is one rung of the
small-universe verification ladder: Poonen (n ≤ 7), Marković (n ≤ 10),
Bošnjak–Marković (n ≤ 11), Vučković–Živković (n ≤ 12).

## Key method

- Rephrases Poonen's weight-assigning technique; the new idea is to use
  **several weight functions simultaneously** rather than one.
- Assigns weights to elements and to sets; a weight w is *successful* if some
  element has total weight ≥ half the total weight of the universe. Multiple
  weights are combined to cover the family.
- The technique is explicitly not claimed to prove the whole conjecture: the
  author says it "will most probably not prove the whole conjecture," but
  handles small cases efficiently and is amenable to algorithmic extension.
- Makes the FC-family machinery explicit: finds small union-closed families G
  such that any union-closed F ⊇ G satisfies Frankl's conjecture with the
  abundant element from G. Several such results are included as self-contained
  lemmas (credit assigned to Vaughan et al. and Morris where due).

## Claim blocks

```claim
id: markovic-uc-holds-n10
statement: Frankl's union-closed sets conjecture holds for every union-closed
  family F with |⋃F| ≤ 10: there is x with |{A∈F: x∈A}| ≥ |F|/2.
hypotheses: F finite union-closed, F ≠ {∅}, |⋃F| ≤ 10.
holds-here: yes
status: asserted-by-source (published 2007, PIM 81(95):29–43)
bearing: One rung of the small-universe verification ladder (Poonen n≤7,
  Marković n≤10, Bošnjak–Marković n≤11, Vučković–Živković n≤12). Independent
  primary confirmation that |F|-only verification (Roberts–Simpson |F|≤40/50)
  and universe-only verification are different axes.
anchor: research/sources/markovic-attempt-frankl-2007.full.md
falsifies: A union-closed F with |⋃F|≤10 and no abundant element.
```

```claim
id: markovic-multi-weight-technique
statement: Marković's method combines several Poonen-type weight functions
  simultaneously; the author states the technique "will most probably not prove
  the whole conjecture."
hypotheses: none (methodological statement)
holds-here: yes
status: asserted-by-source
bearing: Documents that the pre-entropy weight method was understood by its own
  inventor to be insufficient for the full conjecture; the entropy line (2022-)
  is what moved the absolute constant.
anchor: research/sources/markovic-attempt-frankl-2007.full.md
falsifies: A proof that multi-weight assignments do prove the full conjecture.
```