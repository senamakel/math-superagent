# Librarian provenance audit — the high-value and suspicious identifiers

Cycle finding: the library is complete (per ROOT.md / CONTEXT.md, gathering closed
by operator). The librarian's remaining duty is provenance, because the two
failure modes this role exists to prevent are (a) citing something not on disk
and (b) inventing a plausible identifier and filing an unrelated paper under a
wanted name. This note records a spot-audit of exactly the entries most
vulnerable to (b): recent / future-dated / newly-added identifiers.

Method: every suspicious or load-bearing identifier below was resolved against
the live web via DOI/arXiv lookup (`10.48550/arxiv.<id>` or the DOI or the
publisher URL), not taken from the summary's word.

## Verified real (no fabrication found)

| Claim / source | Identifier | Resolution |
| --- | --- | --- |
| Ho, generalization of Boppana's inequality | arXiv:2601.19327 (2026-01) | doi:10.48550/arxiv.2601.19327 resolves; title/author/abstract match; Lean 4 formalisation at github.com/boonsuan/entropy-inequality. NOT fabricated despite the future date. |
| Bhasin, cubical perspective on complements | arXiv:2409.17050 | doi resolves; title/abstract match. |
| Nived, graph formulation study | arXiv:2409.02221 | doi resolves; title/abstract match. |
| Bouchard, lattice formulation | arXiv:2503.00277 | bibsonomy + full text; resolves. |
| Moghaddas Mehr, isomorphism in UC | arXiv:2501.02637 | full text held; resolves. |
| Bošnjak–Marković, 11-element case | EJC 15(1)#R88, doi:10.37236/812 | held; DOI-tagged header. |
| Vučković–Živković, 12-element case | ipsitransactions.org/journals/papers/tir/2017jan/p9.pdf | held; header carries the URL; abstract confirms computer-assisted proof "true if |X| ≤ 12". |

## Enciclopedic / canonical tier confirmed on disk

- Wikipedia union-closed entry (research/sources/wikipedia-union-closed-sets-conjecture.full.md)
- Knill, "Graph generated union-closed families of sets", arXiv:math/9409215 (held)
- Balla–Bollobás–Eccles, "Union-closed families of sets", doi:10.1016/j.jcta.2012.10.005 (held)
- Lozin–Zamaraev, "Union-closed sets and Horn Boolean functions", doi:10.1016/j.jcta.2023.105818 (held)
- Reimer, "An average set size theorem", doi:10.1017/S0963548302005230 (quoted in full in Bruhn–Schaudt survey; the primary paper is not separately downloaded but its statement is quoted verbatim in multiple held sources)

## Conclusion — corrected (librarian, this cycle)

**The original conclusion was wrong.** A later spot-audit found that the
Marić–Živković–Vučković FC-families body was exactly the failure the audit
claimed not to exist: the file was downloaded under the mistyped arXiv ID
1209.5628 and held Oberdieck's "A Serre derivative for even weight Jacobi
forms" (number theory), not the FC-families paper. The genuine paper is
arXiv:1207.3604 and is now on disk (repair record in
`research/summaries/maric-zivkovic-vuckovic-fc-families-2012.md`). The audit's
resolution check covered identifiers that *resolved*; it did not catch an
identifier that resolved to the *wrong paper*. The two other known mislabeled
bodies (Vaughan math/0208012 → algebroids; Eccles 1210.2044 → Clifford analysis)
were already flagged DEFECTIVE with correct attribution, and their genuine
content is carried by genuine bodies on disk (Morris/Pulaj/survey for Vaughan;
arXiv:1311.2298 bodies for Eccles). The claim store is safe to rely on —
no load-bearing claim anchored to any of the three mislabeled bodies — but the
"no unrelated paper filed under a wanted name" statement is false as written.
Lesson: verify a downloaded body's actual first-page content against the
requested title, not only that a URL resolves.
