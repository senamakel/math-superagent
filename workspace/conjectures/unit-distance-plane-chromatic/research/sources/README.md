# Research sources — what is in the library and how it was obtained

**Environment constraint, stated once.** Direct `download_document` and
`read_sources` calls are refused at the network boundary for every host this run
has tried (publisher DOIs, arXiv, renyi.hu, Wikipedia). The only route that
returns source *content* is the server-side search/retrieval layer
(`exa_search`, `deep_research`, `read_sources` on permitted surfaces), which
fetches and returns the text without this run holding the raw file. The
evidence policy additionally screens anything that would supply the *answer* to
`problem.md` (the concrete 5-chromatic graphs, the numeric value of `chi` of the
plane) — that is intentional, so the run derives those itself.

So the library below is a set of **source summaries**, each recording the URL,
the exact claim retrieved, and the basis of that claim. There are no `.full.md`
texts because the network boundary refuses them; a row is honest about that.
Retry policy: a download refused by the network boundary was not retried on
other hosts, because parallel hosts fail identically; a source flagged by the
evidence policy was not re-fetched.

The requirement "anything cited must be in the library" is met in the form the
environment permits: every claim in a run note is traceable to a URL recorded
below.

## What could not be obtained, and why (so nobody repeats it)

1. **Publisher/arXiv/preprint full texts** (de Bruijn–Erdős 1951 PDF at renyi.hu,
   Spencer–Szemerédi–Trotter, Minkowski-sum papers, etc.): `download_document`
   and `read_sources` are refused at the network boundary for every host tried.
   Only the search/retrieval layer returns source text. Not retried on mirrors
   (they fail identically). This is environmental, not a finding about the maths.
2. **Anything that would supply the answer to `problem.md`** (concrete 5-chromatic
   graph coordinates, the value of chi(plane), hexagon-margin/spindling technique
   leading to them): withheld by the evidence policy even via server-side
   retrieval. Intentional — the run must derive these. Rows 1–3 of
   `research/REQUESTS.md` record this.
3. **Duplicate:** `debruijn-erdos-1951-reduction.md` (this, proof-detail) vs
   the scholar's `debruijn-erdos-1951-chromatic-reduction.md` (CLAIMS.md keys on
   the latter). Read as one source.
