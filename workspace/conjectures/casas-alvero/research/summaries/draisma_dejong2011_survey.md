# Draisma & de Jong, *On the Casas-Alvero conjecture* (EMS Newsletter 80 (2011) 29–33)

Full text: [[draisma_dejong2011_survey.full]]

The standard expository treatment; held as the whole EMS newsletter (OCR-degraded). Introduces the **p-adic valuation** reinterpretation of the Graf-von-Bothmer method and proves the **shared-root-set-not-two** fact. Most valuable to the run for: the p-adic valuation technique, and the statement of which degree families it settles.

## The p-adic valuation reinterpretation

```claim
id: pdic-valuation-method
statement: The Graf-von-Bothmer reduction-mod-p proof can be recast in terms of fields
  with a p-adic valuation. Let v_p extend the p-adic valuation on Q to C, R = {z : v_p(z)≥0},
  M its maximal ideal, K_p = R/M the residue field (char p). If n = n' p^e with n' < p and
  CA holds for all degree-n' polynomials in K_p[X], then CA holds for all degree-n
  polynomials in C[X]. (This is the "Proposition 9" of [5] quoted by Ghosh 2024.)
  From this, CA over char 0 follows in degrees 3p^k (p≠2) and 4p^k (p≠3,5,7); 3p^k,4p^k
  being the first extensions beyond [GvB]'s p^k,2p^k.
hypotheses: n = n' p^e, n'<p; CA holds in degree n' over the residue field
holds-here: yes
status: asserted-by-source (this is [5]'s method, exposited here and re-quoted in the held
  Ghosh/Castryck sources)
bearing: Gives the run a characteristic-honest lifting tool: settle the base degree n' if
  it divides n with quotient < p and is itself settled; fewer bad primes to worry about.
anchor: research/sources/draisma_dejong2011_survey.full.md (Section 7, OCR), also
  research/sources/ghosh2024_finiteness_html.full.md (Prop 9 of [5])
falsifies: a degree-3p^k or 4p^k char-0 counterexample (p≠ excluded primes).
```

## Shared-root-set-not-two (analytic)

```claim
id: ddj-not-two
statement: The set of common zeroes of a CA polynomial f with its derivatives cannot have
  cardinality two. (Section 6 of the survey; re-proved as Prop 1 in Laterveer–Ounaïes.)
hypotheses: char 0
holds-here: yes
status: proved (see also laterveer_ounaies §1 Prop 1)
bearing: First constraint on the shared-root set that any counterexample must violate if
  the run seeks one; a minimal counterexample has ≥5 distinct roots (Laterveer–Ounaïes).
anchor: research/sources/draisma_dejong2011_survey.full.md (Sec 6)
falsifies: a held counterexample with exactly two distinct common roots.
```

## Status statement (2011)
The four degrees left open by a slight enhancement of [GvB] are n = 12, 24, 28, 30 (this 2011 list predates the 2012 degree-12 verification; today degree 12 is settled and **20** is the smallest open). CA is open even for real-rooted polynomials, degree ≥5.

## What it does not settle / caveat
The held full text is an entire OCR-degraded newsletter; the CA article body is fragmentary. All specifics worth keeping were cross-checked against the cleaner Castryck and Ghosh sources. No machine-readable algorithm is given beyond the valuation method sketch.
