# Librarian cycle — state of the art confirmed complete; no new acquisition warranted

## Conclusion in one line

Re-verified from disk and from live web that the reference library meets the
phase-1 exit test, the standing REQUESTS rows are answered by genuine held
primary texts, and no on-topic primary gap surfaced — the single known gap
(JCTA 2026 Theorem 8 proof) remains unobtainable in open access.

## What this cycle verified (independently, from disk, not from recall)

1. **Standing REQUESTS rows are answered by genuine held full texts.**
   - `full-text-faithful-b96b` (Erdős–Szekeres 1961 lower-bound construction):
     read the first page of
     `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
     (source https://renyi.hu/~p_erdos/1960-09.pdf) — real scan content,
     constructs 2^{n-2} points with no convex n-gon.
   - `balko-valtr-attack-baa4` / `open-access-full-1e6e` (Balko–Valtr SAT
     encoding): held at
     `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
     (https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf); claims
     `balko-valtr-refutes-PS` and `balko-valtr-pseudolinear-verifies` anchor
     there.
   - The `derived/REQUESTS.md` rows still *render* open — a re-derivation
     artifact, not a library gap (the claims ledger carries the `answers:`
     anchors; the claims ledger is authoritative).

2. **The one genuine gap is still open and precisely scoped.**
   Baek–Balko SoCG 2025 Theorem 8 (every decomposable set of more than
   Σ_{i=k-a+2}^{u} C(k-2,i-2) points contains an a-cap, u-cup, or k in convex
   position — hence ES holds for all decomposable sets) is stated verbatim in
   the held full text
   (`research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md`
   lines 343-353) with "The proof of Theorem 8 is omitted", deferred to
   JCTA 2026 (DOI 10.1016/j.jcta.2026.106195). Re-confirmed: ScienceDirect
   still paywalled; no arXiv preprint of the journal-complete version exists;
   the frontier row for that DOI is the journal version of the held SoCG 2025
   paper, NOT a distinct work. Claim `baek-balko-decomposable` stays
   asserted-by-source and must not be used as a proved basis.

3. **State of the art has not moved since the last cycle.**
   - ES(7)=33 remains open. Newest direct attacks all held: Dumitru
     (arXiv:2512.24061, Dec 2025 — UNSAT only for anchored subfamilies),
     Koshelev–Koshka (arXiv:2604.20120, Apr 2026 — SAT/ASP + linear
     subreduction; proves the ADJACENT h_nc(4,0;4,0)=26),
     Krapivin–Przybocki–Heule PointSAT (arXiv:2607.02958, Jul 2026 — proves
     the ADJACENT h(6,7)=24; the 32-point no-7-gon search found no realizable
     order type among 200,000 abstract ones, evidence but NOT a proof).
   - No new upper bound on ES(n), no new exact value beyond ES(6)=17.
   - citation_graph on the two newest papers returns 0 connected works
     (OpenAlex records too new — no citation-derived leads available yet).

4. **Adjacent-problem drift rejected (per the drift guard).**
   - Furukawa 2025 "Big convex polytopes or rich hyperplanes"
     (arXiv:2501.03645) — higher-dimensional analogue ES_d(l,n); no reduction
     to the planar exact conjecture.
   - Chen–Pohoata 2026 "Above and below" (arXiv:2605.27061) — higher-order
     Erdős–Szekeres functions AB^{(d)}(k); adjacent, not ES(n).
   - The Parillo/Briggs 2026 JCTA entry surfaced by a misparsed query is a
     chemistry erratum, not mathematics — do not re-search the bare DOI name.

## Disposition

No new download is warranted: the canonical tier exists, the only standing
gap is confirmed unobtainable in open access, and no on-topic primary gap
surfaced in live search. The next valuable work is run-side, not
acquisition-side: the pending computations head-of-queue (con4-supersat,
layer-transfer-matrix, polar-dual verification per directive 23) and the
Lean formalisation loop.

Re-check for the JCTA 2026 Theorem 8 proof only when a subscription is
available or the authors post the journal version to arXiv.