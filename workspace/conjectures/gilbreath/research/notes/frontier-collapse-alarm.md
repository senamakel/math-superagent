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