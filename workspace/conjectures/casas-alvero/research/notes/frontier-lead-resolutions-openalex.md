# Frontier lead resolutions — OpenAlex works W1558046128, W2003962780, W2062454016, W1579326781

Status of four previously-unidentified frontier entries, resolved this cycle via the
OpenAlex API (`https://api.openalex.org/works/<id>`). These are **metadata records**, not
full texts; they exist to say what each frontier lead actually is.

## W2003962780 — the origin paper, paywalled (both mirrors now proven blocked)

**E. Casas-Alvero, "Higher Order Polar Germs", J. Algebra 240 (2001) 326–337,**
DOI 10.1006/jabr.2000.8727. This is the paper that states the conjecture.
OpenAlex marks it `oa_status: bronze` with `pdf_url:
https://www.sciencedirect.com/science/article/pii/S0021869300987271/pdf` and a mirrored
copy at `https://content.openalex.org/works/W2003962780.pdf`. **Both downloads were
attempted this cycle and both failed**: content.openalex.org → HTTP 401 Unauthorized;
sciencedirect.com → HTTP 403 Forbidden. This confirms, with fresh evidence, the prior
audit's record that the origin paper is not fetchable from this environment. It is
**not load-bearing**: the conjecture's statement, motivation (higher-order polars of
plane curve germs) and status are fully covered by held full texts (Draisma–de Jong
survey; Wikipedia; the Schaub–Spivakovsky notes; the Casas-Alvero 2012 "roots and
foci" EMS paper).

## W1579326781 — ALREADY HELD (duplicate lead)

OpenAlex title "Abel-Goncharov's polynomials and the Casas-Alvero conjecture" (2013-08-24,
arXiv PDF url: https://arxiv.org/pdf/1308.5320) is the **original title of S. Yakubovich's
arXiv:1308.5320**, which the library already holds in full under its later v5 title
"Polynomial problems of the Casas-Alvero type" (`research/sources/yakubovich2013_abel-goncharov.full.md`).
The record's own abstract confirms the match (Abel–Goncharov interpolation polynomials,
CA conjecture, real-roots cases). **No new download; the frontier entry points at a held
source.** Cited-by is 0, consistent with a preprint superseded by the survey version.

## W1558046128 — NOT a primary treatment (book review)

"Algebraic geometry and arithmetic curves" (2003), type `book-review` of Qing Liu's
book of the same name — a Choice Reviews Online review, `has_fulltext: false`,
`is_oa: false`. It entered the frontier from the citation graph of Lu 2017. **Discard as a
lead**: it is not a source of mathematics for this run. The underlying book (schemes,
arithmetic surfaces, reduction) is textbook background; the run's scheme-theoretic
instruments are already covered by the problem statement's own method section.

## W2062454016 — Barwise–Eklof 1969 "Lefschetz's principle", paywalled, background-only

**J. Barwise, P. Eklof, "Lefschetz's principle", J. Algebra 13 (1969) 554–570,**
DOI 10.1016/0021-8693(69)90117-3. `is_oa: false`, `has_fulltext: false`. This is the
model-theoretic precise form of "true over C ⟹ true over every algebraically closed
field of char 0" — the justification for the problem statement's free normalisation
"reduce to C". **Not fetched** (paywalled) and **not load-bearing**: the run works over
explicit ℤ-schemes by construction, and the char-0/char-p distinction the run actually
relies on is the model-theoretic one already documented in the held sources (the
counterexample family in char p). Eklof's own 1973 follow-up "Lefschetz's Principle and
Local Functors" (Proc. AMS, DOI 10.2307/2039433) is the standard citation for the
char-p-valid formulation and is cited by the MathOverflow discussion of the principle.

## Bookkeeping

- The four OpenAlex API responses were auto-filed as `research/sources/openalex_W*.full.md`
  (JSON metadata, with the source URL in the first line) and auto-digests as
  `research/summaries/openalex_W*.md`. They are resolution records, not full texts;
  the summaries above replace the auto-digests.
- OpenAlex citation-graph side effects (71 + 63 + 89 + 115 new frontier candidate rows,
  mostly junk citations of a book review and of Lefschetz's principle) should be treated
  as noise: the frontier derives new candidates from *every* citation, and a book
  review citing 595 things adds no mathematical lead.