# Caldwell — Prime Glossary: Gilbreath's conjecture

**Full text:** `research/sources/caldwell-gilbreaths-conjecture-glossary.full.md` (if present) / source https://t5k.org/glossary/page.php?sort=GilbreathsConjecture
**Source:** Chris Caldwell's Prime Pages glossary.

## What it establishes (statement + record, no new maths)

- The conjecture statement with the worked triangle and the block-lemma check described plainly: "if the row starts with a 1 and then n entries which are either 0 or 2, then the next n rows must start with a one." So Odlyzko only needed 635 rows to exceed 10^13.
- Verification record table: smallest k with first π(x) entries of k-th row in {0,1,2}: k=5,15,35,65,95,135,175,248,329,417,481,635 for x=10^2..10^13. (This is Odlyzko's G-table, restated.)
- Guy's remark that primes are unremarkable, only slow-growing + reasonably distributed.

## **CONTRADICTION with the run's sourced claims (flag it)**

- Caldwell says: "Proth claimed to have proven this result in 1878, but his proof turned out to be faulty" — this is **the retracted myth**, contradicted by `proth-myth-retracted` (Chase 2024 §7; Arias de Reyna 2020; Williams' retraction).
- Caldwell's references list "Proth, Théorèmes sur les nombres premiers, C. R. Acad. Sci. Paris, **85** (1877) 329–331" — the **wrong** citation: those pages are Pépin's paper, and C.R. 85 is the very sub-error Chase/Arias correct. (Caldwell apparently preserves the very citation-tangle the run refuted.)
- Caldwell also gives "first 64,419 rows" for the two-students check — a number that differs from Killgrove–Ralston's "first 63,419 primes" in the library (63,419 vs 64,419). Minor inconsistency; the sourced K–R/Mathematical-Computations figure is 63,419.

## Bearing / status

Encyclopedic/glossary tier — statement, record, block lemma, Guy's heuristic. Its mathematical content matches the sourced primaries, but **its Proth history claim and citation are wrong and must not be cited for those**. Flag as a contradiction the scholar should record: an otherwise-respected glossary repeats the myth the library has refuted, plus the Pépin/Proth citation swap.

```claim
id: caldwell-proth-myth-repeats
statement: Caldwell's prime glossary repeats the retracted claim that "Proth (1878) claimed to prove Gilbreath's conjecture but his proof was faulty" and cites C.R. 85 (1877) 329–331 for it — contradicted by Chase 2024 §7 / Arias de Reyna 2020 (that citation is Pépin's paper; Proth gave no proof).
hypotheses: the two scholarly accounts of Proth's 1878 article.
holds-here: yes — an authoritative-adjacent source propagating the exact myth and citation tangle the run refuted.
status: contradicts proth-myth-retracted and proth-citation-correction
bearing: shows the myth persists in print; nothing in Caldwell supports treating Proth's "proof" as real.
anchor: research/sources/caldwell-gilbreaths-conjecture-glossary.full.md
contradicts: proth-myth-retracted, proth-citation-correction
```
