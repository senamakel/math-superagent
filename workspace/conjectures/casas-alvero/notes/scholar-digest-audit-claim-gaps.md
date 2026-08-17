# Scholar digest — cycle: audit and close claim-block gaps

## What this cycle did

The reference library was already mature from prior cycles: every load-bearing
source is held as a `.full.md` under `research/sources/`, most carry a bounded
digest under `research/summaries/`, and the phase-1 test (ROOT.md: status,
minimal-counterexample structure, verification bound, settled classes) already
passes. My job this cycle, per the scholar role, was not to re-acquire
documents but to confirm each source is actually **converted into usable claim
blocks** — that is, that its statements reach `derived/CLAIMS.md` with
hypotheses, holds-here, status, bearing, and falsifier — and to store durable
findings.

### Claim-block gaps closed (4 digests upgraded with fenced claim blocks)

1. **`lu2017_casas-alvero-computational-ag.md`** → `lu-2017-charp-trap`.
   Lu 2017 (arXiv:1707.04754) reduces char-0 CA to an F_p-point count of size p
   (Prop 2.3) and proves those F_p statements. Since CA is false in char p, an
   argument whose core is a char-p count cannot prove CA: the size-p branch is
   the pure powers, and ruling out the counterexample branches is the missing
   char-0 content. Another entry in the claimed-proof family, with its char-p
   test stated (for n=p+1 the F_p count must NOT be p on counterexample
   branches).

2. **`chellali2012_degree-5p-hal.md`** → `5p-bad-primes-chellali`.
   CA holds for degrees 5p^e (p prime, p ∉ {2,3,7,11,131,193,599,3541,8009}).
   Independent of Castryck et al.'s computational 5p^k classification; the two
   agree on the bad-prime set.

3. **`cima_gasull_manosas_2020_extensions-casas-alvero.md`** → two claims:
   - `smallest-open-degree-20-vs-2020-survey`: the 2020 survey's passing status
     remark "first open cases n = 24,28,30" skips 20; resolved in favour of 20
     (20 = 4·5 not covered — 4p^e excludes p=5). **A cross-source discrepancy
     resolved, not silently picked.**
   - `charp-witness-xpp1-xp-xp-1-polynomial`: over F_5, x^2(x^2+1) is a second
     char-p counterexample family (shares root with each derivative, not a pure
     power), a second primary citation for the hard constraint.

4. **`polstra2012_convex-hulls-casas-alvero.md`** → `polstra-convex-hull-collapse`.
   Thm 3.1: a CA polynomial over C has all roots hull vertices iff it is a pure
   power; contrapositive: a genuine counterexample has a non-vertex root. This
   is the char-0-only geometric collapse step the live root-difference-coloring
   thread rests on, and it has no F_p analogue — consistent with char-p
   counterexamples surviving.

All four landed in `derived/CLAIMS.md` and are searchable via `search_claims`.

### What was already complete

The digests for Graf-von-Bothmer, Castryck, Laterveer–Ounaïes,
Schaub–Spivakovsky (2023, 2024), Ghosh (2024, 2025), Draisma–de Jong, Massri,
and Macintyre already carried proper claim blocks. Nothing needed re-adding.

### Durable memory

`remember_memory` failed all attempts (memory server down for the cycle, as the
run's own note already records). The durable record is nonetheless safe: every
claim block lives on disk in a digest under `research/summaries/` that renders
into `derived/CLAIMS.md`, which all planning roles read. The two findings meant
for Cognee (the 20-vs-24/28/30 discrepancy resolution; the second char-p
witness family) are recorded as claims, so nothing is lost — they are just not
yet in the graph store. A later cycle with a live memory server should call
`remember_memory` for these two to put them into Cognee proper.

### What the run still lacks

No new gap: `REQUESTS.md` is empty, every claim traces to a held source. The
open mathematics is unchanged — degree 20 is the smallest open degree; the
approach in the current direction is the scored degree-20 search, which has
collapsed onto one construction family (binomials) and needs diversification.
