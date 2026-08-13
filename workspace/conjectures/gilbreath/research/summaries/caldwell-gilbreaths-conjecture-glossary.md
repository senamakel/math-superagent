# Caldwell, The Prime Glossary — "Gilbreath's Conjecture" (t5k.org, Wayback capture)

**Full text:** `research/sources/caldwell-gilbreaths-conjecture-glossary.full.md` — wikilink: [[caldwell-gilbreaths-conjecture-glossary.full]]
**Source:** https://web.archive.org/web/2024/https://t5k.org/glossary/page.php?sort=GilbreathsConjecture (Chris Caldwell's Prime Pages, widely-read primer)

## What it establishes

Encyclopedic-tier glossary entry, notable mainly as a **vector of the retracted Proth myth** and as an independent restatement of the block lemma and of Odlyzko's G(π(x)) table.

- **The canonical statement and rows.** Displays the triangle A_0..A_11 (2,3,5,7,… → 1,2,2,4,2,4,2,4,6,2 → 1,0,2,2,2,2,2,2,4 → …) — exactly the run's oracle rows; Gilbreath's students verified the leading-1 claim for "the first 64,419 rows" (the K–R source figure is 63,419 primes — Caldwell's digit is a typo/rounding).
- **The block lemma, stated correctly (constant 1).** "If the row starts with a 1 and then n entries which are either 0 or 2, then the next n rows must start with a one." This is the run's proved `odlyzko-block-lemma-exact`: one row protected per {0,2} block entry — independent (encyclopedic) agreement with Odlyzko 1993 and Killgrove–Ralston 1959.
- **Odlyzko's computation method and G-table.** Explains why Odlyzko did not compute all 5×10^22 entries: he only needed the first 635 rows, using the block lemma to skip. Reproduces G(π(10^x)) = 5,15,35,65,95,135,175,248,329,417,481,635 (x=2..13) — matching Odlyzko Table 2 and the run's `odlyzko-verification-1993`.
- **Guy's "nothing special about primes" comment** (quoted): the primes are not special, only slow-growing and reasonably distributed; a proof might come from maximal-gap and gap-distribution knowledge — the same general-class framing the run's ROOT.md commits to.
- **The Proth myth, repeated uncritically.** "Proth claimed to have proven this result in 1878, but his proof turned out to be faulty," citing "Théorèmes sur les nombres premiers, *C. R. Acad. Sci. Paris* 85 (1877) 329–331". Both claims are wrong: Proth's only discussion is Nouv. Corresp. Math. 4 (1878) 236–240 with no proof, and C.R. 85:329–331 is Pépin's paper (documented in `proth-myth-retracted` / `proth-citation-correction`).

## Bearing on this run

- Corroborates (third independent source) the block lemma constant 1 and the G-table — both already proved/sourced; encyclopedic confirmation only.
- **Do not cite Caldwell for the Proth episode.** It is the myth's continuing public vector: the glossary repeats the retracted "faulty proof" claim and the wrong C.R. pages. It *contradicts* the run's sourced `proth-myth-retracted` and `proth-citation-correction`; record it as the counter-example of how the myth circulates, never as authority.

```claim
id: caldwell-proth-myth-repeats
statement: Caldwell's Prime Glossary (t5k.org) restates the block lemma correctly (a row of 1 then n entries in {0,2} protects the next n rows' leading 1) and reproduces Odlyzko's G(π(10^x)) table (5,15,35,65,95,135,175,248,329,417,481,635), but repeats the retracted myth "Proth claimed to have proven this result in 1878, but his proof turned out to be faulty" and cites C.R. 85 (1877) 329–331 for it — pages that are actually Pépin's paper.
hypotheses: the glossary's own text (Wayback capture, 2024).
holds-here: yes — the block-lemma/table corroboration matches the run's proved and sourced results; the Proth claim is the myth refuted by proth-myth-retracted and proth-citation-correction.
status: catalogued/corroborative for the block lemma and G-table; contradicted for the Proth episode.
bearing: third independent source for the constant-1 block lemma and G-table; the standing exhibit of the Proth-myth's circulation — cite as counter-source only.
anchor: research/sources/caldwell-gilbreaths-conjecture-glossary.full.md
contradicts: proth-myth-retracted, proth-citation-correction
```

## Source status

Wayback capture of the Prime Pages glossary (t5k.org, Chris Caldwell); encyclopedic tier, widely cited by OEIS entries. No theorem content beyond the block-lemma restatement.