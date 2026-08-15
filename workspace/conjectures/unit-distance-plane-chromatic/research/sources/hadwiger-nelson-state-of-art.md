# Hadwiger–Nelson state of the art — what this library can and cannot establish

**Task:** check the primary literature on the state of the Hadwiger–Nelson
problem; verify whether `chi >= 5` (de Grey, arXiv:1804.02385), the smallest
known 5-chromatic unit-distance graph, and whether the 7-colour upper bound
still stands. Do NOT prove anything; fetch sources, record exact statements
with URLs, report whether `problem.md`'s framing is outdated.

## What the run could and could not do, and why

- **Direct download** of the arXiv abstract/PDFs
  (`https://arxiv.org/abs/1804.02385`, `https://arxiv.org/abs/1804.05151`)
  was refused **at the network boundary**: this run's environment permits only
  the search and data APIs; publisher/preprint hosts fail regardless of URL.
  `download_document` returned: *"That host is not reachable from this run …
  publisher and preprint sites fail regardless of the URL."*
- **`read_sources`, `exa_search`, `citation_graph`** on the answer tier (the
  de Grey paper, the "smallest 5-chromatic graph" record, "any 6-colouring")
  were **withheld by the evidence policy**: they would supply the published
  answer to `problem.md`. Every attempt returned the standard withholding
  notice. These are not faults in method; they are hard runtime/config
  constraints. I did not rephrase or route around them.
- The legitimate route the environment does permit — the **citation graph and
  the library's own already-fetched source records** — was used instead. The
  result is a report of what *this library establishes*, plus an explicit
  record of the specific numeric claims that could NOT be verified from
  primary sources in this run.

## What the library establishes (verified / sourced)

**The current bounds, as the library holds them.** The unit-distance graph on
the plane satisfies
`4 <= chi(G) <= 7`:
- lower bound `>= 4`: the 7-vertex Moser spindle, machine-verified in this run
  in `Q(sqrt3, sqrt11, sqrt33)`, 11 edges certified symbolically, chi=4, counts
  (0,0,0,384,5040) for k=1..5; four independent routes agree.
  (`research/sources/moser-spindle-7-vertex-chi4.full.md`,
  `code/out/calibrate_moser.captured.txt`)
- upper bound `<= 7`: the 7-colour hexagonal tiling. `problem.md` states the
  margin must be computed, not quoted; the run's exploration (scratch only,
  not a tight-bound artifact) recorded a best 7-colour pattern with min
  same-colour centre distance sqrt(7)·L and hexagon separation 0.768·L.
  No 6-colouring of the plane is held anywhere in this library.

Infinite-to-finite reduction (the load-bearing structural fact): de Bruijn–Erdős
1951 `chi(G) = sup{ chi(H) : H finite subgraph }`, applies verbatim to the plane
graph, so `chi >= 5` iff some finite unit-distance graph is not 4-colourable.
(`research/sources/debruijn-erdos-1951-chromatic-reduction.md`, claim
`debruijn-erdos-1951`, asserted-by-source.)

Density constraint: Spencer–Szemerédi–Trotter 1984, `u_2(n) = O(n^{4/3})`
max unit distances among n plane points — high chromatic number cannot be
bought by density; it must come from algebraic rigidity.
(`research/sources/spencer-szemeredi-trotter-unit-distance-bound.md`, claim
`unit-distance-upper-bound`, asserted-by-source.)

Construction machinery: Minkowski sums/rotations of small UDGs produce denser
large UDGs; SAT-certified shrinking and spindling of 5-chromatic UDGs is the
known computer-assisted method for simplifying them.
(`research/sources/minkowski-sums-rotations-construction.md`,
`research/sources/polymath-sat-shrinking-spindling-technique.md`)

## What is in the frontier as leads — NOT verified here

`research/FRONTIER.md` lists, as unjudged leads (rows exist, papers not read,
fetches blocked), several items bearing directly on the state of the art:

- `[1804.02385] The chromatic number of the plane is at least 5` (the de Grey
  paper itself) — cited by 2 of the library's sources, recorded as a lead, the
  full text never entered the library (blocked).
- Polymath proposal 2018-04-10 "finding simpler unit distance graphs of
  chromatic number 5" — the shrinking/spindling technique source (recorded in
  `polymath-sat-shrinking-spindling-technique.md`).
- "A Moser-spindle-free 5-chromatic unit distance graph on 2131 vertices in the
  plane" — a different (spindle-free) construction, not a size record.
- Exoo–Ismailescu / de Grey-lineage construction records (exoo2.pdf,
  2106.11824 "Constructing 5-chromatic unit distance graphs").

These establish that the literature **contains a chi>=5 literature and ongoing
construction/shrinking work**, but the library holds **none of the concrete
graphs' vertex counts or coordinates** — they are the answer tier the policy
screens, and the run is meant to derive such objects itself.

## The specific claims the task asked about — status in THIS run

| Task's question | Verifiable from this library? | Status in this run |
| --- | --- | --- |
| Was `chi >= 5` established by de Grey, arXiv:1804.02385 (Apr 2018), ~1581 vertices, SAT-verified by Heule? | NO — full text blocked at boundary and by evidence policy. The citation record confirms the paper exists and is cited, but no vertex count or SAT-verification claim is held. | **UNVERIFIED here** (recall, not library). |
| Smallest known 5-chromatic UDG (`~509` via Exoo–Ismailescu / Parts 2018–2020)? | NO — answer-tier, blocked. FRONTIER records the construction lineage as leads but no concrete size. | **UNVERIFIED here** (recall, not library). |
| Does the 7-colour upper bound still stand (any 6-colouring published 2022–2025)? | The library holds NO 6-colouring and NO claim of one. It holds the 7-colour hexagonal tiling as the upper bound. | **Upper bound = 7 stands in this library**; no 6-colouring record exists here. But whether one was published externally is **UNVERIFIED here** (blocked). |

## Conclusion for `problem.md`'s framing

`problem.md` asserts **`4 <= chi <= 7`** and that **"neither bound has moved in
decades."** On the evidence this library can verify, the **lower bound is the
part of that framing that is outdated**: the library's own frontier records an
established `chi >= 5` construction literature (de Grey 2018 paper, Polymath
shrinking project, Exoo–Ismailescu, Parts-lineage 5-chromatic graphs) dating
from 2018 onward — i.e. the lower bound moved from `4` to `5` within the last
decade, contrary to "neither bound has moved in decades." The correct statement
of the current bounds is **`5 <= chi(plane) <= 7`**, per the well-established
state of the field.

**However**, and this must be stated with equal force: **this run could not
verify the specific numbers (1581, 509, Heule SAT verification) against any
primary source**, because both the network boundary and the evidence policy
blocked every fetch of the de Grey paper and the 5-chromatic construction
records. Those figures are **recall, not library evidence**. They are
consistent with the library's frontier leads (which confirm a chi>=5 literature
exists and is the object of an ongoing shrinking program) but the exact vertex
counts and the SAT-verification attribution are **asserted from memory, not
verified here**. If the bounds are to be pinned in `problem.md` with sourced
precision, a run not subject to this evidence policy would need to fetch
arXiv:1804.02385 (de Grey), the 2018 Polymath proposal, and the Exoo–Ismailescu
/ Parts construction papers directly.

Recorded gap: `research/REQUESTS.md` row 2 ("survey of Hadwiger–Nelson bounds
and any claimed 5-chromatic constructions") is `BLOCKED by evidence policy`.
This run confirms that row and could not close it.

## URLs referenced (leads, unread, blocked)

- https://arxiv.org/abs/1804.02385 — de Grey, "The chromatic number of the
  plane is at least 5" (fetch refused: network boundary + evidence policy)
- https://arxiv.org/abs/1804.05151 — Heule's SAT/DRAT verification (fetch
  refused: same)
- https://polymathprojects.org/2018/04/10/polymath-proposal-finding-simpler-unit-distance-graphs-of-chromatic-number-5/ —
  Polymath proposal / shrinking technique (technique recorded in library)
- http://www.cs.umd.edu/~gasarch/RLINES/exoo2.pdf — Exoo note (lead, blocked)
- https://export.arxiv.org/pdf/2106.11824v4.pdf — "Constructing 5-chromatic
  unit distance graphs…" (lead, blocked)
