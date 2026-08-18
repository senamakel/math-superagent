# Eliahou 2011 — non-trivial cycles, part III

<!-- src: Shalom Eliahou, "Le problème 3n+1 : y a-t-il des cycles non triviaux ? (III)", Images des mathématiques (CNRS), 20 Dec 2011, DOI 10.60868/dmt0-jf29. Full text: research/sources/eliahou-cnrs-cycles-non-triviaux-2011.full.md -->

## What the source establishes

For a hypothetical non-trivial cycle C of the standard Collatz map, write p for the number of even terms and q for the number of odd terms. Combining the product identity with the current verification bound (the article uses 5×10^18) puts p/q in

    I = (1.58496250072115618145, 1.58496250072115618155).

Using two contiguous Farey intervals containing I, Eliahou identifies the most economical rational in I as

    10,439,860,591 / 6,586,818,670.

Therefore p ≥ 10,439,860,591, q ≥ 6,586,818,670, and the total period N=p+q satisfies

    N ≥ 17,026,679,261.

The same Farey construction excludes N=18,000,000,000: for N strictly above 17,026,679,261, the next economical rational has numerator+denominator 18,054,391,537, so N ≥ 18,054,391,537.

The article explains the generic method: start with a Farey interval containing I, bisect at its mediant until the mediant lies in I; the two resulting contiguous Farey intervals yield the exact lower bounds.

## Correction to a later citation

Laurore 2025 calls the 17,026,679,261 bound “Eliahou (2021)”; its bibliography actually points to this 2011 CNRS article. The library should cite the 2011 primary, not invent a 2021 paper.

## Claims

```claim
id: eliahou-cnrs-17026679261
statement: If a non-trivial positive-integer Collatz cycle has p even and q odd members, then p ≥ 10,439,860,591, q ≥ 6,586,818,670, and its total period N=p+q satisfies N ≥ 17,026,679,261, under the verification interval used in Eliahou's Farey argument (Eliahou 2011, Images des mathématiques, DOI 10.60868/dmt0-jf29).
hypotheses: positive-integer non-trivial cycle; verification bound sufficient to put p/q in the stated interval I
holds-here: the numerical verification hypothesis is superseded by Barina 2^71, but the resulting bound remains a valid weaker consequence
status: proved in source (expository article; exact Farey proof in held full text)
bearing: independent primary cross-check of the cycle-length lower-bound arm; corrects the Laurore date
anchor: research/summaries/eliahou-cnrs-cycles-non-triviaux-2011.md
```

```claim
id: eliahou-cnrs-exclude-18b
statement: Under the same interval/Farey setup, a non-trivial Collatz cycle cannot have total length exactly 18,000,000,000; any length strictly above 17,026,679,261 is at least 18,054,391,537 (Eliahou 2011).
hypotheses: same verification interval and p/q Farey interval as above
holds-here: yes as a weaker exclusion; Barina's stronger current verification may change the next gap
status: proved in source
bearing: demonstrates the rigidity of the rational-approximation ladder
anchor: research/summaries/eliahou-cnrs-cycles-non-triviaux-2011.md
```
