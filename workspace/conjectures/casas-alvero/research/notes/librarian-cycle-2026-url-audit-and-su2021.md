# Librarian cycle — source-URL integrity audit, Su 2021 triaged, frontier top confirmed held

## What this cycle did

Re-verified, by mechanical inspection rather than memory, three properties the
library must have and that earlier cycles only asserted.

### 1. URL provenance audit (60/66 full texts carry their URL in the file header)

`grep 'source: https?://' research/sources` on all 66 `.full.md` files: 60
carry the source URL in their first line (the `<!-- source: ... -->` header).
The 6 without a first-line header are all documented failed fetches or
non-text records, each with its attempted URL recorded in the body:

- `diaz-toca-gonzalez-vega-2006.full.md` — "NOT OBTAINED" marker; the
  verification-bound claim it would support is double-corroborated by two held
  primaries (Draisma–de Jong survey; Castryck–Laterveer–Ounaïes 2012) and
  independently reproduced by the run's Gröbner oracle
  (`research/threads/computational-boundary.md`).
- `sudbery1973_distinct-roots.full.md` — header literally reads
  `| DOWNLOAD FAILED`; the ≥5-distinct-roots claim is proved directly in held
  Laterveer–Ounaïes.
- `levinson1944_gontcharoff-polynomials.full.md` — header carries the Project
  Euclid URL; body is the paywalled stub. The Abel–Gontcharoff material it
  would provide is covered by held Yakubovich + Dzhaparidze–Janssen.
- `openalex_W1558046128.full.md` / `openalex_W2003962780.full.md` /
  `openalex_W2062454016.full.md` — OpenAlex record stubs (bibliographic
  records, not papers; the papers they describe are covered by the held
  primary tier; `openalex_W2003962780` is the origin paper's record, whose
  full text is confirmed unobtainable).

The other 3 files under `research/sources/` are not `.full.md` texts:
`REMOVED-tmp-castryck-homepage.md` (marked removal), `tmp-castryck-homepage.full.md`
(fetch artifact of Castryck's homepage; superseded by the badprimes7.txt data
file held from the author), `rahman1971_distinct-zeros-product.cambridge.md`
(redundant landing page; genuine full text held as
`rahman1971_distinct-zeros-product.pdf.full.md`).

**Verdict: every file in the library is either a genuine full text with its URL
recorded, or a correctly-labelled failed-fetch with its attempted URL
documented. Nothing is a bare recall claiming a source that is absent.**

### 2. Top of the citation frontier is held

`derived/FRONTIER.md` top rows: arXiv:2312.08742 (Schaub–Spivakovsky note,
held as `schaub_spivakovsky_2023_note*`), arXiv:1705.01704 (Dobrowolski 2017
withdrawn claim, held), the origin paper DOI
(DOI:10.1006/jabr.2000.8727, recorded unobtainable — statement/motivation/
status fully covered by held sources per
`research/notes/librarian-cycle-2026-origin-polars.md`), arXiv:1208.5404v1
(Castryck et al. degree-12, held), Polstra convex-hulls (held), MathReviews
record pages (bibliographic only), arXiv:math/0605090 (Graf-von-Bothmer et
al., held).

The three OpenAlex leads linked from the Lu 2017 record resolve to: the origin
paper itself (W2003962780, covered), and two background texts relevant only to
the singularity-theory *motivation* (W1558046128 = Qing Liu's *Algebraic
geometry and arithmetic curves* — a standard textbook on exactly the
scheme-over-Z axis the run works in, but not a CA source; W2062454016 =
Lefschetz's principle 1969 — the model-theoretic principle behind "CA over ℂ ⇔
CA over any char-0 field", again background, not a CA result). Neither adds a
CA-specific claim the library lacks. **No fetchable, non-duplicate primary
treatment is outstanding from the frontier.**

### 3. Su 2021 triaged (was the only unclassified citing work of the origin paper)

Origin-paper citation graph (W2003962780, 19 citing works) was walked. All are
held except one: **Jiaxuan Su, "On the Casas-Alvero's Conjecture", J. Phys.
Conf. Ser. 1955 (2021) 012020** — a conference-proceedings paper by an author
affiliated with Suffield Academy (a high school). Triaged via
`read_sources` on the DOI landing page: from its abstract, it proves CA **only
for small n**, by "a different method", with no claim of a general resolution.

Assessment: the abstract's claim ("prove it when n is small") is strictly
weaker than what the library already holds (d≤7 by Gröbner over ℚ, d=12
settled by Castryck et al.), so the paper is not load-bearing. It is also not
one of the full-conjecture claimed proofs the run documents in
`research/notes/casas-alvero-status.md` (Battiston, Dobrowolski, de las Heras,
Lu, Ghosh), so it does not change the claimed-proof family record. **Not worth
a download; recorded here so no later cycle re-chases it.**

## Assessment

The reference library on the Casas-Alvero conjecture is complete for the
run's purposes, audited for provenance at the file level, current through
2026, and every load-bearing claim in `research/ROOT.md` traces to a held
full text with a recorded URL. The genuinely absent sources (origin paper
2001, Diaz-Toca–Gonzalez-Vega 2006, Levinson 1944, Sudbery 1973, de Frutos
Marín 2015, Chávez Martínez 2018) are each blocked by paywall or network
failure, and each is covered by a held primary or by the run's own verified
computation.

Per GOAL.md's phase-1 exit rule, the library meets ROOT.md's test
(status / minimal-counterexample structure / verification bound / restricted
classes). Further gathering should happen only against a stated gap in
REQUESTS.md, which is currently empty.

**NOTHING FURTHER — no fetchable, non-duplicate, CA-relevant source is
outstanding; the library is audited and current; the next cycle belongs to
the mathematics.**