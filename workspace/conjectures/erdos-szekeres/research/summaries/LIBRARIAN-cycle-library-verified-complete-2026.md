# Librarian cycle — library independently re-verified complete; state of play unchanged

## Conclusion in one line
The reference library meets the phase-1 exit test and no on-topic download is
warranted this cycle. The adopted-first-step computations (directive 23) are the
next valuable work, not further gathering.

## What this cycle independently re-verified (from disk + live search, not recall)

1. **Every REQUESTS row is answered by a genuine primary held on disk.**
   - `full-text-faithful-b96b` (Erdős–Szekeres 1961 lower-bound construction):
     `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`,
     URL https://renyi.hu/~p_erdos/1960-09.pdf. Concrete construction:
     `summaries/erdos-szekeres-1961-construction-concrete.md`.
   - `balko-valtr-attack-baa4` / `open-access-full-1e6e` (Balko–Valtr SAT attack):
     `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`,
     URL https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf.
   - The claim blocks carry `answers: <id>` anchors; the claims ledger is authoritative.
     The rows still *render* open in `derived/REQUESTS.md` — a re-derivation artifact.

2. **Canonical tier, SAT arm, order-type foundations all present**, with URLs
   recorded in-file (see LIBRARY-STATUS.md and LIBRARY_LEDGER.md).

3. **State of play has NOT moved (live search, targeted queries + citation walks).**
   - Newest direct ES(7) attack: Dumitru, "Notes on the 33-point Erdős–Szekeres
     problem", arXiv:2512.24061 (Dec 2025), HELD. ES(7)=33 still open.
   - Baek–Balko SoCG 2025 (split k-gons = 2^{k-2}+1 tight, tight for a
     relaxation; decomposable sets; ordered-3-uniform-hypergraph generalization
     fails), HELD. The frontier's JCTA `10.1016/j.jcta.2026.106195` row is the
     journal version of this same mathematics.
   - Damásdi–Dong–Scheucher–Zeng saturation (7/8)·2^{n-2}, HELD.
   - Suk 2016 (2^{n+o(n)}) and HMPT (2^{n+O(√(n log n))}) remain the best
     asymptotic upper bounds; Tóth–Valtr binomial form still best of that form.
   - Citation walks on the newest held papers (Baek–Balko 2025, Heule–Scheucher
     2024, Dumitru 2025) return no new citations — papers too recent — so the
     frontier's top rows are all encumbrances of held content.

## The one standing "gap 0" is computational, not acquirable
SMQH ("Automated Symmetric Constructions in Discrete Geometry") proves there is
NO realizable 4-fold-symmetric 32-point no-7-gon set: of 310,187,713
non-isomorphic satisfying assignments, all share one of 6 inner-12
configurations, none realizable. The held full text states this result (see
`subercaseaux-mackey-qian-heule - Automated Symmetric Constructions - HTML.full.md`
§6.2) but does NOT list the six configurations explicitly, and no separate
artifact publishing them exists. Reproducing them via this run's own SAT arm is
a computation, not an acquisition — no download can fill it. The run-side
reproduction of ES(5)=9 / ES(6)=17 with an orientation-variable encoder is the
line that would eventually re-derive these six as a byproduct.

## Disposition
NOTHING FURTHER to gather. The next valuable work is run-side: the adopted
first steps (con4-supersat NNC count, layer-transfer-matrix cone capacities,
polar-dual verification) against es_construct and a second family, per
directive 23. Sources remain as held; no new download made this cycle.
