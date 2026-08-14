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

## What is in the library

**Core claims (each has a `claim` block feeding `research/CLAIMS.md`):**
- `debruijn-erdos-1951` — chi(G) = sup chi(H) over finite subgraphs; the
  finite-to-infinite reduction behind the whole problem.
  `research/sources/debruijn-erdos-1951-chromatic-reduction.md`
- `unit-distance-upper-bound` — u_2(n) = O(n^{4/3}): density cannot be bought.
  `research/sources/spencer-szemeredi-trotter-unit-distance-bound.md`
- `szemeredi-trotter-incidence` — I(P,L) = O(m^{2/3} n^{2/3} + m + n): the
  theorem under the unit-distance bound. **Added this run.**
  `research/sources/szemeredi-trotter-incidence-theorem.md`
- `szemeredi-trotter-algebraic-extremal` — same bound's claim, plus that the
  extremal point-line configurations are built from algebraic number fields
  Q(sqrt k) (Guth–Silier sharp constructions). **Added this run; distinct id
  from `szemeredi-trotter-incidence` to avoid ledger collision.**
  `research/sources/szemeredi-trotter-incidence-algebraic-extremal.md`
- `maehara-algebraic-rigid-distances` — distances in rigid unit-distance graphs
  are exactly the algebraic numbers: the exact-arithmetic justification.
  `research/sources/maehara-1991-algebraic-rigid-distances.md`
- `kempe-universality` — the linkage construction technique behind Maehara's
  converse. **Added this run.**
  `research/sources/kempe-universality-linkages.md`
- `einstein-lattice-unit-distance` — Eisenstein integers / triangular lattice.
  `research/sources/eisenstein-integers-triangular-lattice.md`
- `minkowski-sum-unit-distance-condition` and `minkowski-sum-dense-graphs` — the
  Minkowski-sum construction engine.
  `research/sources/minkowski-sums-rotations-construction.md`
- `sat-k-colourability-encoding` — the complete colouring oracle encoding.
  `research/sources/sat-colourability-encoding.md`
- `critical-minimum-degree` — every k-critical graph has min degree >= k-1; the
  backbone of the size-bound rung. **Added this run.**
  `research/sources/colour-critical-graphs-structure.md`
- Also: `totally-unfaithful-unit-distance-graphs.md` and the
  `research/summaries/` index records (de Bruijn–Erdős 1951, Moser spindle 1961,
  SST 1984).

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
