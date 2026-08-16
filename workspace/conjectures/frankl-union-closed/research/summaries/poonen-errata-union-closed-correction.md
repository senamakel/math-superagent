# Poonen, "Remarks and errata" — correction to Theorem 1 of "Union-closed families" (1992)

**Source:** https://math.mit.edu/~poonen/papers/errata.pdf (Poonen's own errata list, dated
August 14, 2025). Full text at `research/sources/poonen-errata-union-closed-correction.full.md`.

The 1992 JCTA paper "Union-closed families" is not openly available (ScienceDirect
403s; Poonen's site hosts CV/errata but not the paper). This errata page is the closest
primary-source statement obtainable of the paper's Theorem 1, and it fixes the exact
hypothesis of Poonen's FC-family characterization, which the run's claim ledger
currently carries on a survey's word alone.

## What it establishes

Section 3 ("Typos and minor misstatements"), entry "Union-closed families":

> p. 256, Theorem 1, in condition 2: Change `F ⊎ G = G` to `F ⊎ G ⊆ G`. A similar
> change should be made to the beginning of lines −5 and −3 on p. 257, and to the
> beginning of line 6 on p. 260. (Thanks to Theresa Vaughan.)

So the printed 1992 statement of Theorem 1's condition 2 uses an **equality**
`F ⊎ G = G`, and the correct hypothesis is a **containment** `F ⊎ G ⊆ G`
(where `⊎` is the disjoint union of the two families). Vaughan flagged the error;
Poonen confirms it.

```claim
id: poonen-theorem1-errata
statement: Poonen's own errata (Aug 2025) corrects Theorem 1 of his 1992
  "Union-closed families" paper: condition 2 should read F ⊎ G ⊆ G (containment),
  not F ⊎ G = G (equality), with the same change at the stated lines of pp. 257 and 260.
hypotheses: statement of a correction, not a new theorem; applies to the paper as printed.
holds-here: true
status: sourced (primary — author's own errata page)
bearing: sharpens the exact hypothesis of Poonen's FC-family characterization
  (Theorem 1); the ledger's `poonen-fc-characterisation` claim, asserted from the
  Bruhn–Schaudt survey, must be checked against this: if it quotes "K = L" (equality)
  it is quoting the printed (erroneous) form, not the corrected one.
anchor: https://math.mit.edu/~poonen/papers/errata.pdf, section 3, entry "Union-closed families"
```

## What this means for the run

- Any use of Poonen's Theorem 1 (FC-family characterization, the engine behind
  Poonen-weight / cutting-plane work) should cite the **corrected** containment form.
- The Pulaj and Morris papers in the library quote Theorem 1; if either relies on
  condition 2 as equality, it is relying on the pre-errata statement. (Vaughan's
  later "Families Implying the Frankl Conjecture" EJC 2002 likely uses the corrected
  form — that paper is on the frontier and not yet held.)
- The 1992 full text itself remains unobtainable so far; recorded as a gap, not a dead end.