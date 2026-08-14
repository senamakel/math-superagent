# Download failures — do not retry

Each of these was attempted and failed; retrying the same URL wastes a cycle. The
citation itself (where known) is kept so the source can be obtained by another route
if the run ever needs it.

| Target | URL tried | Why it failed | What was kept instead |
| --- | --- | --- | --- |
| Hening–Kelly, "On Polya's Orchard Problem" (RHUMJ 7(2), 2006), full article PDF | https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1244&context=rhumj | HTTP 403 Forbidden (Digital Commons blocks the direct download) | The abstract/landing page is on disk: `research/sources/hening-kelly-polya-orchard-problem.full.md` (records only the abstract: the compact-convex-domain generalisation and the rhombus/circle/3D examples; the minimal-radius result ρ = 1/d is **not** in the file on disk — it was mentioned in an earlier note but is unsupported by the landing page, which is abstract-only). The 403 was for the article body only. |
| Goodrich–Mbirika–Nielsen, "New methods to find patches of invisible integer lattice points" (preprint) | https://people.uwec.edu/mbirika/lattice_point_paper.pdf | HTTP 404 Not Found (author page moved) — **RESOLVED**: the author's current copy at https://people.uwec.edu/mbirika/paper_lattice_point_visibility.pdf was downloaded in full (Involve 14:2 (2021) 283–310) | Full text at `research/sources/goodrich-mbirika-nielsen-invisible-lattice-points.full.md`, summary at `research/summaries/goodrich-mbirika-nielsen-invisible-lattice-points.md` |
| Rearick, "Some Visibility Problems in Point Lattices" (Caltech PhD thesis, 1960), full text | https://thesis.caltech.edu/2705/1/Rearick_df_1960.pdf (also thesis.library.caltech.edu path) | **Scanned PDF with no OCR text layer** — the download tool refuses it ("no extractable text"); the alternate host failed at connection level. Do not retry. | Landing page/abstract at `research/summaries/rearick-1960-visibility-point-lattices.md`; the abstract's results (density 1/ζ(k), 2^k mutually-visible bound, arbitrarily large gaps) are captured there from search-extracted title-page text. |
| Laison–Schick, "Seeing dots: Visibility of lattice points," Math. Mag. 80(4) (2007) 274–282 | (DOI 10.1080/0025570X.2007.11953494) | Paywalled at Taylor & Francis; no open copy found in search | Its existence and content are recorded via the Goins et al. and Adhikari–Granville citations in FRONTIER.md. |
| Allen, "Pólya's Orchard Problem," Amer. Math. Monthly 93 (1986) 98–104 | (DOI 10.2307/2322700) | JSTOR paywall; no open PDF found | The result ρ = 1/d is carried by Hening–Kelly (on disk) and cited by Goins et al. |
| Nicholson–Rachan, "On weak lattice point visibility," Involve 9 (2016) 411–414 | (DOI 10.2140/involve.2016.9.411; Project Euclid PDF) | Incapsula access block on projecteuclid.org; no open copy found | The Goins et al. reference list carries the citation; the weak-visibility variant is not needed for the exact count. |

Note: Honsberger, "The Orchard Problem," Mathematical Gems I (MAA, 1973), ch. 4,
pp. 43–52 — the book is not open; the chapter's content is summarized in the
MathWorld Orchard Visibility Problem page already in the library.
