# Librarian audit — library phase-1 complete; REQUESTS rows are a derivation artifact

This cycle's work: an audit of the reference library, two on-point web probes
(citation_graph on the Balko–Valtr SAT-attack primary; find_similar_sources on
the Baek ETV arXiv page), and a durable record of the disposition. No new
download was made, because nothing on-topic and primary is missing.

## Conclusion

The Erdős–Szekeres reference library is **phase-1 complete**. ROOT.md states
the structure of a minimal counterexample, the verification bound, and multiple
restricted classes with their hypotheses (GOAL.md criterion 1). Nothing on-topic
and primary is absent from `research/sources/`.

## The three REQUESTS rows render open but are answered on disk

`balko-valtr-attack-baa4`, `open-access-full-1e6e`, `full-text-faithful-b96b`
still appear open in `derived/REQUESTS.md`, yet each is answered by a full text
already held:

- `balko-valtr-attack-baa4` and `open-access-full-1e6e`: answered by
  `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
  (eurocomb2015.w.uib.no PDF), digest
  `research/summaries/balko-valtr-A-SAT-attack-on-ES-ENDM2015.md`. The claim
  block there carries `answers: balko-valtr-attack-baa4` and
  `answers: open-access-full-1e6e`.
- `full-text-faithful-b96b`: answered by
  `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
  (renyi.hu/~p_erdos/1960-09.pdf), digest
  `research/summaries/erdos-szekeres-1961 lower-bound-construction.md` (claim
  `es61-lower-bound`, `answers: full-text-faithful-b96b`).

The re-derived REQUESTS.md opens a row only when no note carries `answers: <id>`;
here the answering claim blocks live in the held summaries but the request rows
were never formally closed in the ledger. **Derivation artifact, not a gap.**
Do not re-open or re-download. If REQUESTS.md must agree, the claims-ledger
`answers:` fields are authoritative.

## What the on-point probes surfaced — all already covered

- citation_graph on the Balko–Valtr primary (DOI 10.1016/j.ejc.2017.06.010,
  6 citing works) added to FRONTIER: Baek EJC 2024 = held arXiv 2206.04260;
  Baek–Balko JCTA 2026 = held SoCG 2025; the rest (orthogonal symmetric chain
  decompositions, two disjoint 5-holes, CC-system enumeration, Faradžev–Read)
  are adjacent or already-covered topics, none bearing a new primary on ES(n).
- find_similar_sources on arXiv 2206.04260: the jcpaik Lean 4 formalisation of
  the ETV paper shares its CapCup.lean with the already-held LeanPool file
  (LeanPool.ErdosTuzaValtr.Main.CapCup), so nothing new there; Strunk 2012
  (two conditional upper bounds) and Bárány–Roldán-Pensado–Tóth (ES for lines)
  are held or adjacent.
- GP80 (JCTA 29:220–235) and GP93 survey remain paywalled, but the definitional
  need is served faithfully by the held SLMath ch22
  (`slmath-goodman-pollack-allowable-sequences-chapter22.full.md`) and the
  Dumitrescu arXiv:2204.06101 restatement. The staircase-convexity claim those
  originals were wanted for has been machine-refuted; not load-bearing.

## What was NOT obtained and why

- **Goodman–Pollack 1980**, JCTA 29:220–235 — paywalled (ScienceDirect JCTA),
  no open copy found. Content faithfully held second-hand.
- **Goodman–Pollack 1993 survey**, Springer (Pach, ed.) — paywalled, no open
  copy. Definitional content held in SLMath ch22.
- **Abello–Eğecioğlu–Kumar 1995**, DCG 14 — staircase-convexity source; branch
  machine-refuted, no longer needed.

## NOTHING FURTHER to acquire this cycle

Every angle is covered — canonical tier (Erdős–Szekeres 1935 + 1961 primaries),
surveys (Morris–Soltan, Tóth–Valtr), all exact/upper bounds, SAT attacks
(Balko–Valtr, Scheucher, Dumitru, SMQH, PointSAT), order-type enumeration
(Aichholzer), CC systems / signotopes (Felsner–Weil), empty-hexagon, higher
dimensions, restricted classes (split/decomposable Baek–Balko, saturation,
forbidden-order-type, positive-fraction, partitioned), realizability, and the
Lean/Mathlib formalisation arm. Further acquisition resumes only against a
stated gap in RESEARCH_REQUEST and opening a new REQUESTS row.
