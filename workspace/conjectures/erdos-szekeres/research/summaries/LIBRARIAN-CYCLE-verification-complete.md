# Librarian cycle — verification pass; library confirmed complete and genuine

## What this cycle did

A verification pass rather than an acquisition pass: the steering rule says
gathering proceeds only against a stated gap in the requests ledger, and there
is no open gap. So this cycle's job was to confirm the library is (a) still
complete against the current state of the art and (b) free of invented or
wrong-paper contamination, and to report the only thin spots found.

## Verified genuine (against live search, not recall)

1. **The three open requests are answered by genuine held full texts.**
   - `balko-valtr-attack-baa4` / `open-access-full-1e6e` — the ENDM 2015
     Balko–Valtr full text is held at
     `sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
     (https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf); claim blocks
     carry `answers:` for both ids.
   - `full-text-faithful-b96b` — the 1961 Erdős–Szekeres primary is held at
     `sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
     (https://renyi.hu/~p_erdos/1960-09.pdf).
   The derived `derived/REQUESTS.md` render is stale (a re-derivation-state
   quirk noted by three prior librarian reports) — the content is on disk.

2. **The newest held arXiv entries are genuine live papers.** Live search
   resolves each to exactly its held title/abstract:
   - Dumitru, arXiv:2512.24061 (Dec 2025), ES(7)=33 still open; UNSAT only for
     anchored convex-layer subfamilies.
   - Koshelev–Koshka, arXiv:2604.20120 (Apr 2026), SAT/ASP + linear subreduction;
     hnc(4,0;4,0)=26 (bicolored empty monochromatic quadrilateral), h(6,≥2)=17,
     h(6,1)=18 — adjacent-problem values, not ES(7).
   - Krapivin–Przybocki–Heule, arXiv:2607.02958 (Jul 2026), PointSAT / SMR;
     largest set avoiding empty convex hexagons AND convex heptagons is 23 —
     adjacent-problem result.
   None is an invented or mis-assigned citation.

3. **Current state of the art on ES(7) is held.** The most recent direct ES(7)
   attack remains Dumitru (Dec 2025). No newer direct ES(7) result surfaced in
   live search. The computational landscape (SMQH, PointSAT, Koshelev–Koshka,
   Scheucher, Balko–Valtr) is all held.

## Thin spots found (all acceptable, none a live gap)

- **ES(5)=9 and ES(4)=5 primary proofs** (Bonnice 1974 AMM; Kalbfleisch–
  Kalbfleisch–Stanton 1970 conference) are paywalled and not held in full as
  primaries. They ARE covered at sufficient fidelity second-hand: the held
  Morris–Soltan survey carries the full Bonnice proof outline (Theorem 2.7 /
  Lemma 2.8, the (4,4,1)/(4,3,2)/(3,4,2)/(3,3,3) classification of 9-point
  no-pentagon sets). ROOT.md criterion 1's "method that settled each of
  ES(3..6)" is met by that outline; a paywalled fetch is not worth forcing.
- **Pach–Solymosi k-convex chapter** (DOI 10.1007/978-3-030-25005-8_4) is cited
  by 3 held sources but held only as a MIS-DOWNLOAD stub. It is a drift-guarded
  adjacent problem (k-convex polygonization, not convex-position ES), and the
  IWOCA 2019 version of the same Balko–Bhore–Martínez-Sandoval–Valtr paper IS
  held (abstract level). Not worth a Springer paywall fetch.
- **Bonnice 1974 bibliography record** exists but not the primary; recorded as
  documented-but-not-held.

## New source located this cycle (adjacent, not acquired)

"Garment numbers of bi-colored point sets in the plane", Aichholzer, Bergold,
Fink, Löffler, Schnider, Tkadlec, arXiv:2603.05339 (Mar 2026) — bicolored
4-point structures; engages the same empty-monochromatic-quadrilateral open
problem Koshelev–Koshka's hnc(4,0;4,0)=26 addresses. Adjacent to ES(7); holds
no new information for the convex-position conjecture. Not acquired.

## Decision

NOTHING FURTHER to acquire. Every angle is covered — canonical tier, upper
bounds, exact values, lower-bound construction, order types / signotopes / SAT,
restricted classes, computational attacks through Jul 2026, counterexample
constructions, and the empty-side Horton analogue. All requests answered. The
next valuable work is run-side (the gsplit Phase-2 re-capture already queued in
the Gaps head-of-queue), not librarian acquisition.
