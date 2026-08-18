# Wrong-fetch — Fishkin Mat. Zametki DOI guessed, unrelated paper stored (2026-08-19)

## What happened

To obtain A. Yu. Fishkin, "On the number of limit cycles of planar quadratic
vector fields with a perturbed center" (Mat. Zametki 85(1), 110-118, 2009), the
DOI `10.1134/S0001434609010118` was **guessed** from the Springer DOI pattern
(`10.1134/S...`), and the download resolved to an unrelated paper on network
matrix analysis (coreness measures, spectra of graphs, Horn–Johnson / Golub–Van
Loan / Barabási references).

## Neutralised

`research/sources/fishkin-2009-mat-zametki-85-1.full.md` now carries a
WRONG-PAPER header pointing to the correct paper and to this record. It must not
be cited as Fishkin.

## Lesson (second instance of the same failure mode)

The mathnet lesson (`research/findings/wrong-fetch-rozanova-mislabeled-ilyashenko-1990.md`)
was "never guess a mathnet paperid". This incident generalises it: **never guess
a Springer DOI either**. A DOI must come from a search result, a citation that
carries it, or a held source's reference list. The Fishkin Mat. Zametki 2009
paper's real DOI is not yet held anywhere; the Trans. Moscow Math. Soc. 2010
paper's DOI (10.1090/s0077-1554-2010-00181-1) and its OpenAlex record ARE held,
but its full text remains unobtained (AMS PDF redirects to the journal landing
page; OpenAlex content 429; CiteSeerX connection failed).

## Status of the Fishkin constants

The search-result abstract (Doklady 2009 Russian / OpenAlex 2010 English) states:
Thm 1: #δ-good cycles ≤ exp(exp(10^72 κ − 2δ − 33)) for fields σ-close to a
center and κ-far from the singular set; Thm 2: same shape with 10^77 for the
κ-distance case without the closeness assumption. **This is search-level recall,
not verified primary text** — the thread `restricted-h2-bounds` stays open until
the AMS full text or the real Mat. Zametki paper is held.
