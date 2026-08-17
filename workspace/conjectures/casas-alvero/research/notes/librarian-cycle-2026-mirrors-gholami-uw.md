# Librarian cycle — second mirror check, Gholami closure, UW status documents

Cycle focus: attack the two documented fetch limits with fresh sources, close
the one unresolved loose end from the audit, and re-confirm the status claim
with the newest 2025–26 evidence. All conclusions below are asserted-by-source
with the held file named; nothing here is recalled.

## 1. de Frutos Marín 2015 JTN note — blocked from a SECOND mirror

The library's documented gap (JTN2015 contribution "Un problema sobre números
combinatorios", Valladolid) was re-attempted via a URL surfaced by `exa_search`
on a different uva.es path and host form:
`http(s)://singacom.uva.es/JTN2015/contribuciones/ordinarias/frutos.pdf`.
`download_document` failed at the network layer (socket error, not 404) on both
http and https — same failure class as every prior attempt on `uvadoc.uva.es`
and `hdl.handle.net/10902/15246`. Conclusion: the `uva.es` / `unican.es` host
block is network-wide from this environment, not path-specific. The abstract
(held, `research/summaries/defrutosmarin2015-combinatorios-corroborates-badprimes.md`)
remains the only held content; claim-level coverage of its content (bad/ineficaces
prime lists L(3)..L(7)) is already in the library via claim
`badprimes-lists-corroborated-by-defrutosmarin2015`. Fetch-limited, not unknown.

## 2. "Gholami 2025" loose end — CLOSED (no phantom author)

The audit flagged a single name "Gholami 2025" in an abstract as uncorroborated.
Resolved: the Exa summary text for arXiv:2501.09272 renders the reference to
Ghosh's own 2025 finiteness preprint as "[Gho25]"; the author's name in that
citation is **S. Ghosh**, arXiv:2402.18717, already held in full
(`research/sources/ghosh2024_finiteness_html.full.md`). Grep of the held Ghosh
proof text confirms its only "Gho" author reference is "[14] S. Ghosh (2025) A
finiteness result towards the casas-alvero conjecture … 2402.18717". The lead
is a rendering artifact, not a distinct source. No action needed; recorded so
nobody re-chases it.

## 3. Two UW documents added — institutional framing, not validation

Downloaded (filed by the tool in `research/summaries/`):

- `research/summaries/uw-news-ghosh-simons-award-2025.md` — UW Math news,
  20 Aug 2025: Ghosh named to the first class of Simons Dissertation Fellows;
  the announcement describes the award as recognizing "his recent resolution
  of the Casas-Alvero conjecture", linking to arXiv:2501.09272. This is the
  awarding department's framing of the author's own preprint — **not**
  peer review, not independent validation, not a publication record.
- `research/summaries/uw-seminar-ghosh-casas-alvero-2025.md` — UW student AG
  seminar, 17 Apr 2025: Ghosh's talk abstract ("we will … sketch a proof of the
  conjecture over characteristic 0", counterexamples finite in char p,
  corollary on rational normal curves as set-theoretic complete intersections),
  based on arXiv:2402.18717 and 2501.09272. Records that the claim was
  presented in a departmental seminar by its author.

These add to the status record two dated, sourced institutional data points and
the corollary claim (rational normal curves ⇒ set-theoretic complete
intersections in char 0) as a stated consequence of the preprint. They do not
change classification: the claim remains **unverified preprint** — no
independent confirmation, no retraction, no journal publication through the
2026 record.

## 4. Status re-confirmed against the newest held evidence

- Refereed Schaub–Spivakovsky, *On the Casas-Alvero conjecture*, J. Commut.
  Algebra 17(2):199–202 (Summer 2025), held in full via HAL
  (`research/sources/schaub_spivakovsky_jca-2025_hal-open.full.md`), carries
  "Added in press: In two recent preprints [6] and [7] Soham Ghosh gave a
  complete proof of the Casas-Alvero conjecture" — flags the claim, endorses
  nothing.
- 2023–2026 search sweep (three fresh phrasings, category research paper)
  returns only already-held works (Massri, Ghosh 2402/2501, Schaub–Spivakovsky
  2307/2312/2411/jca-2025, Castryck, Graf-von-Bothmer). No new settled degree,
  no new disproof, no refereed resolution.
- OpenAlex forward-citations on the three pillars (Castryck 1208.5404,
  Graf-von-Bothmer math/0605090, Laterveer–Ounaïes 1204.0450) add only
  already-held works (withdrawn Dobrowolski; de Frutos 2013 thesis).

## Verdict

Fetchable coverage is complete for every load-bearing question GOAL.md poses.
The two unfilled items are network-blocked, documented, and claim-covered. The
frontier's top is worked; the handful of new frontier rows from the UW pages
are navigation boilerplate and institutional links, none load-bearing. No open
request exists that a download could settle. Next cycles are mathematics, not
gathering.