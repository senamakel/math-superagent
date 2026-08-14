# Research sources — what is in the library and how it was obtained

**Environment constraint, stated once.** Direct `download_document` and
`read_sources` on publisher/preprint hosts (renyi.hu, arxiv.org, springer,
sciencedirect, wikipedia, preprint PDF hosts) are refused at the network
boundary. The only route that returns source *content* is the server-side
search/retrieval layer (`exa_search`, `deep_research`, `read_sources` on
permitted surfaces), which fetches and returns text without this run holding
the raw file. The evidence policy additionally screens anything that would
supply the *answer* to `problem.md` (the concrete 5-chromatic graphs, the
numeric value of `chi` of the plane) — intentional, so the run derives those
itself. A source flagged by the evidence policy was not re-fetched.

So the library is a set of **source summaries**, each recording the URL, the
exact claim retrieved, and the basis of that claim, plus a few `.full.md`
bibliographic records where the text could not be fetched. The requirement
"anything cited must be in the library" is met in the form the environment
permits: every claim in a run note is traceable to a URL recorded below.

## The library by subject (as of when this README was last written)

**The finite-to-infinite reduction.**
- `debruijn-erdos-1951-chromatic-reduction.md` — De Bruijn–Erdős compactness:
  chi(G) = sup over finite subgraphs; needs BPIT/choice for uncountable graphs;
  applies verbatim to the plane graph. Claim `debruijn-erdos-1951`.
- `komjath-2010-infinite-chromatic-survey.md` — the survey fixing the metadata
  of the reduction and its AC-content caveats.

**Density cannot be bought (unit-distance extremal theory).**
- `spencer-szemeredi-trotter-unit-distance-bound.md` — u_2(n) = O(n^{4/3}).
  Claim `unit-distance-upper-bound`.
- `erdos-unit-distance-bound.md` — the same bound + Erdős lower bound and
  history (SST 1984 attribution).
- `matousek-unit-distance-problem.md` — course-note treatment; alternative
  proofs (Székely crossing-number, Clarkson et al., Aronov–Sharir). Claim
  `unit-distance-dense-upper-bound-tight`.
- `szemeredi-trotter-incidence-theorem.md` — the incidence theorem itself.
  Claim `szemeredi-trotter-incidence`.

**The construction engine (algebraic point sets / Minkowski sums).**
- `minkowski-sums-rotations-construction.md` — the exact distance-1 condition in
  A+B and that dense UDGs are sums. Claims `minkowski-sum-unit-distance-condition`,
  `minkowski-sum-dense-graphs`.
- `szemeredi-trotter-incidence-algebraic-extremal.md` — sharp ST constructions
  live on algebraic Q(√k) point sets. Claim `szemeredi-trotter-algebraic-extremal`.
- `szemeredi-trotter-arbitrary-number-fields.md` — sharp ST constructions over
  arbitrary number fields via nice (product-closed) bases. Claim
  `number-field-extremal-constructions`.
- `eisenstein-integers-triangular-lattice.md` — the Eisenstein lattice, its unit
  vectors and norm. Claim `einstein-lattice-unit-distance`.

**Exact-arithmetic verification backbone.**
- `maehara-1991-algebraic-rigid-distances.md` — rigid-UDG distances are exactly
  the algebraic numbers. Claim `maehara-algebraic-rigid-distances`.
- `kempe-universality-linkages.md` — the constructive converse via linkages.
  Claim `kempe-universality`.
- `exact-coordinate-certification-unit-distance.md` — O(n^2) exact certification
  procedure for UDG coordinate fields. Claim `exact-coordinate-certification`.
- `sat-colourability-encoding.md` — the complete k-colouring SAT oracle.
  Claim `sat-k-colourability-encoding`.

**Structural colouring theory (size-bound direction).**
- `colour-critical-hajos-construction.md` — k-critical min-degree >= k-1,
  Hajós construction. Claim `k-critical-minimum-degree`.
- `colour-critical-graphs-structure.md` — critical-graph structure (parallel
  scholar source). Claim `critical-minimum-degree`.
- `totally-unfaithful-unit-distance-graphs.md` — non-embeddability certificates
  (parallel).

**Calibration target.**
- `moser-spindle-7-vertex-chi4.full.md`, `summaries/moser-spindle-7-vertex-chi4.md`
  — the run's own verified 7-vertex chi=4 calibration (exact coordinates in
  Q(sqrt3,sqrt11,sqrt33), 11 edges, chi=4, k-counts 0,0,0,384,5040).

## What could not be obtained, and why (so nobody repeats it)

1. **Publisher/arXiv/preprint full texts** (de Bruijn–Erdős 1951 body,
   Spencer–Szemerédi–Trotter 1984 chapter, Moser & Moser 1961 note, and the
   Minkowski-sum papers): blocked at the network boundary. Only the
   search/retrieval layer returns source text. Not retried on mirrors (they
   fail identically). Environmental, not a finding about the maths.
2. **Anything that would supply the answer to `problem.md`** (concrete
   5-chromatic graph coordinates, chi(plane) value, hexagon-margin/spindling
   technique leading to them): withheld even via server-side retrieval.
   Intentional — the run must derive these. Rows 1–3 of `research/REQUESTS.md`
   record this.
3. **Duplicate** `debruijn-erdos-1951-reduction.md` (proof detail) vs the
   scholar's `debruijn-erdos-1951-chromatic-reduction.md` (CLAIMS.md keys on
   the latter). Read as one source.
