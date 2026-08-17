# Librarian cycle — JCTA 2026 Theorem 8 proof still unobtainable; library phase-1 complete

<!-- source: fresh recon this cycle via exa_search + citation_graph on 10.1016/j.jcta.2026.106195 -->

## What this cycle did

Re-confirmed that the Erdős–Szekeres reference library is complete against the
current state of the art, with the single known acquisition gap still open.

## The one genuine gap: JCTA 2026 Baek–Balko Theorem 8 proof

The held SoCG 2025 full text (`sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md`)
states Theorem 8 verbatim — every decomposable set of more than
Σ_{i=k-a+2}^{u} C(k-2, i-2) points contains an a-cap, a u-cup, or k points in
convex position — and then says "The proof of Theorem 8 is omitted", deferred to
the JCTA 2026 journal version. This is the strongest restricted-class result
(ES holds for all decomposable sets) and is load-bearing in the
extreme-structure thread.

Fresh recon this cycle:
- ScienceDirect JCTA 2026 (DOI 10.1016/j.jcta.2026.106195) — still paywalled
  (403 in prior cycle; no open copy surfaced now).
- No arXiv preprint of the journal-complete Baek–Balko joint paper exists.
- Martin Balko's KAM page (kam.mff.cuni.cz/~balko/) lists publications but hosts
  only presentation slides, no full-version PDF of the Baek–Balko paper.
- citation_graph on the DOI returns 0 connected works (OpenAlex record too new),
  so no citation-derived leads.
- Author portals (BGU, Starfos, MTMT) carry only the SoCG 2025 short version,
  which is already held.

**Status: claim `baek-balko-decomposable` stays asserted-by-source.** The
decomposable theorem must NOT be used as a proved basis for a structural step.
The run CAN still (a) test whether its own es_construct extremal sets are
decomposable (definition is on disk), and (b) verify the S(a,u,k) bound
computationally for small a,u,k.

## The three REQUESTS rows are answered by held full texts

- `full-text-faithful-b96b` (ES 1961 lower-bound construction): ANSWERED by
  `sources/erdos-szekeres-1961-...-renyi.pdf.full.md` (renyi.hu scan).
- `open-access-full-1e6e` and `balko-valtr-attack-baa4` (Balko–Valtr SAT
  encoding): ANSWERED by `sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
  (open-access EuroComb ENDM full text), which encodes ES via red-blue ordered
  3-uniform hypergraph monotone paths and refutes the Peters–Szekeres
  strengthened conjecture — the exact formulation the run's computational arm
  needs.
- The `research/requests/etv-rr-estimates.md` gap (exact rr(k) Ramsey-remainder
  values) is a refinement, not a live REQUESTS row; the EJC 1996 paper is
  paywalled but its abstract-level claim is held, and no run step currently needs
  the exact rr(k) values.

## Recent work is already held

- Dumitru, "Notes on the 33-point Erdős–Szekeres problem" (arXiv:2512.24061)
  — held.
- Koshelev–Koshka, "Combinatorial Geometry of ES-type Problems: SAT/ASP" 
  (arXiv:2604.20120) — held.

## Adjacent-problem drift (rejected, per the drift guard)

- Furukawa 2025 "Big convex polytopes or rich hyperplanes" — higher-dimensional
  analogue; no reduction to planar exact conjecture.
- Blake–Felsner–Hämäläinen–Witkowski "ES for convex permutations and
  orthogonally convex point sets" — a different function N_o(n), not ES(n).

## NOTHING FURTHER to acquire

Every angle — canonical tier, every published upper bound, lower-bound
realizability, exact values and their computations, SAT/order-type/chirotope
foundations, restricted classes, adjacent problems, formalisation arm — is
covered by a held primary or faithful digest. Further acquisition resumes only
against a stated gap, and the only such gap is the JCTA 2026 Theorem 8 proof,
which remains unobtainable in open access as of this cycle. Re-check only when a
subscription is available or the authors post the journal version to arXiv.
