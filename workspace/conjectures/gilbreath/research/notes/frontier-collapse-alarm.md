# Frontier collapse alarm

On 2026-08-13, the download of the Gatti 2020 preprints.org wrapper page through
web.archive.org replaced `research/FRONTIER.md` wholesale. The file went from
501 candidate leads to 15 rows — every one a social-media share button scraped
from the archived wrapper (Twitter intent/tweet, Facebook sharer.php, LinkedIn
shareArticle, Reddit submit, Delicious post, BibSonomy BibtexHandler, Mendeley
import, Publons follow). `config/.frontier.json` held the same 15 and is
gitignored, so the run's only recovery was the last committed frontier from
commit db36fc23 (42 rows, the operator saved it).

## Rule: a collapse in candidate count is a failure signal

When FRONTIER.md is rewritten, compare the row count before and after. A drop
of more than 30% means the download replaced the frontier instead of adding to
it, and the output is almost certainly garbage — one wrapper page with
navigation chrome is all it takes.

## Second incident (2026-08, this librarian cycle) — the documented filter did not run

Re-downloading the **Colonna 2026-08 record page** and the **DeepMind
Gilbreath.lean** raw file in one cycle again replaced FRONTIER.md wholesale:
the reseeded 42 shown + 418 further candidates collapsed to 21 rows, again
dominated by the same Gatti-wrapper share buttons (Twitter intent/tweet,
Facebook sharer, LinkedIn shareArticle, Delicious, BibSonomy, Mendeley,
Publons), plus a handful of new-but-few academic citations from the Colonna
page. Recovery: FRONTIER.md was rewritten from memory of this session's read of
the good state (the 42-row reseeded table verbatim), with the genuine new leads
(MR 93k:11119, MR 96e:11002, OEIS A000101 PDF, Wikipedia Prime_gap, arXiv
2510.06688) appended in a separate section.

**Lesson:** the header filter is documented but was NOT applied by the rewrite
machinery on these writes — the collapsed file contained the very URLs the
filter claims to drop, and the filter header itself was gone. Any
multi-page-download cycle must re-read FRONTIER.md afterwards and count rows; a
drop > 30% means the rewrite was garbage regardless of what the header claims.
The genuine content of the two downloads was preserved in sources/summaries;
nothing was lost but the candidate list, which is recoverable from the reseeded
table above.

## Filter (added same date, in FRONTIER.md header)

A URL matching any of these patterns is a share/bookmark endpoint, never a
citation, and is dropped before writing:

- `intent/tweet`
- `sharer.php`
- `shareArticle`
- `/submit?url=`
- `BibtexHandler`
- `/import/?url=`
- `follow/publon`
- `/follow/`

The FRONTIER header reports how many rows the filter dropped on each write.