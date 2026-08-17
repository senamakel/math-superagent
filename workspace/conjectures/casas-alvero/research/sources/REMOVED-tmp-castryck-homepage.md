Removed as a library source: the Castryck homepage full text
(`research/sources/tmp-castryck-homepage.full.md`) was a pointer-only fetch,
served only to resolve the relative URLs of the arXiv-listed companion files.
Its one load-bearing fact — the URL of the author's own `badprimes7.txt`
companion file — is recorded in the digest
`research/summaries/tmp-castryck-homepage.md`, and the companion file itself
is now held at `research/sources/castryck2012_badprimes7.txt.full.md`.
Keeping the 20 KB publication-list page would add no mathematical content.
(Deletion note: the digest remains; if a later run needs the full list of
computation scripts named on the page, the URLs are all `~/wcastryc/code/*`
per the digest.)