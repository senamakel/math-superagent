# Librarian cycle — library verified complete and current against live state of the art

<!-- This is the librarian's durable record for this cycle. No new download was made. -->

## Conclusion in one line

The Erdős–Szekeres reference library is **phase-1 complete and current**: every
standing `REQUESTS` row is answered by a genuine primary full text on disk, the
full canonical tier is present with URLs recorded, the full texts are indexed and
searchable, and a live check confirms **no on-topic primary has appeared since the
last acquisition** (Dumitru Dec 2025 remains the latest ES(7) attack; ES(7)=33 is
still open). Nothing was downloaded because no gap exists — re-fetching held
material is refused by the steering rule.

## What was verified this cycle (each check against disk / live, not recall)

1. **All three standing REQUESTS rows are answered on disk** (grep-confirmed
   `answers:` anchors in claim blocks):
   - `full-text-faithful-b96b` (ES 1961 lower-bound construction):
     `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
     (https://renyi.hu/~p_erdos/1960-09.pdf), claims `es61-lower-bound`,
     `es1961-construction-held`.
   - `balko-valtr-attack-baa4` and `open-access-full-1e6e` (Balko–Valtr SAT
     attack): `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
     (https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf), claims
     `balko-valtr-refutes-PS`, `balko-valtr-pseudolinear-verifies`. The rows
     still *render* open in `derived/REQUESTS.md` — a re-derivation artifact,
     not a library gap; the claims ledger is authoritative.
   - No new open gap was posted this cycle.

2. **The canonical reference tier is present**, each full text carrying its URL:
   ES 1935 (numdam), ES 1961 (renyi.hu), Peters–Szekeres 2006 (Cambridge,
   ES(6)=17), Suk 2017 (arXiv:1604.08657), Holmsen–Mojarrad–Pach–Tardos
   (arXiv:1710.11415), Baek–Balko SoCG 2025 (split/decomposable), the 1998
   improvement chain (Chung–Graham, Kleitman–Pachter, Tóth–Valtr), Norin–Yuditsky,
   Vlachos, Mojarrad–Vlachos, Morris–Soltan survey, Balko–Valtr ENDM 2015,
   Heule–Scheucher (empty hexagon 30), Subercaseaux ITP 2024, Scheucher,
   Aichholzer 2002 (order types), Duque et al. (small integer realization),
   Károlyi–Tóth (forbidden subconfigurations), Pór–Valtr, Bárány–Valtr, Damásdi
   et al. (saturation), Horton 1983, Felsner–Weil signotopes, Felsner
   (chirotope NP-complete), Bergold–Felsner–Scheucher, Goodman–Pollack–Sturmfels,
   Moshkovitz–Shapira, Fox–Pach–Sudakov–Suk, Goaoc–Welzl, Kaibel/Welzl geometric-
   algorithmics convex-hull chapter, the Lean/Mathlib records, and the
   Wikipedia/MathWorld encyclopedic tier.

3. **The newest holdings are indexed and searchable** — search_documents returned
   the July-2026 PointSAT (`krapivin-przybocki-heule ... PointSAT HTML.full.md`,
   arXiv:2607.02958), the April-2026 Koshelev–Koshka SAT/ASP linear subreduction
   (arXiv:2604.20120), and the Dec-2025 Dumitru 33-point ES(7)
   (arXiv:2512.24061) from the local index. `search_documents` on the cups-caps
   bound and the lower-bound construction returns the correct primaries (Morris–
   Soltan survey, Felsner–Weil, Peters–Szekeres) — indexing is sound.

4. **State of the art has not moved** (live `exa_search`, category research paper,
   on ES(7) / new upper bounds): no paper surfacing a new exact value beyond
   ES(6)=17 or a new general upper bound beyond the held Holmsen–Mojarrad–Pach–
   Tardos 2^{n+O(√(n log n))}. Dumitru arXiv:2512.24061 (Dec 2025) is still the
   latest direct ES(7) attack — triple-orientation SAT + 4-set convexity criterion
   + convex-layer anchoring, yielding UNSAT for anchored subfamilies only; the
   full 33-point case remains open (no full UNSAT; heavy-tailed runtime). This
   matches the held summary. Every surfaced paper is already in the library.

## Documented-but-not-held (re-confirmed; not worth a re-search)

- **Erdős–Tuza–Valtr 1996, "Ramsey-remainder"** (EJC 17(6) 519–532,
  DOI 10.1006/eujc.1996.0045) — canonical primary of the ETV enumeration
  conjecture; open-access unobtainable (ScienceDirect 403). Faithfully restated in
  held Baek arXiv:2206.04260 (Thm 1.5) and Balko–Valtr. Recorded; not a live block.
- **Bonnice 1974** and **Kalbfleisch–Kalbfleisch–Stanton 1970** — primary
  ES(5)=9 proofs are paywalled; the Bonnice proof outline is in the held
  Morris–Soltan survey (Thm 2.7/2.8). Sufficient fidelity second-hand.
- **Knuth "Axioms and Hulls"** book — paywalled; CC-system axioms covered via the
  held Wikipedia CC-system + Felsner. Not worth a fetch.

## Disposition

The library meets the phase-1 exit test and GOAL.md criterion 1 (ROOT.md states
the structure of a minimal counterexample, the verification bound, and ≥3
restricted classes with hypotheses). The next valuable work is **run-side** — the
steer-11 gsplit Phase-2 provenance re-capture and the layer-profile conjecture —
which is a computation, not an acquisition. No new download was made because no
gap existed; this verification note is the cycle's durable record.
