# Librarian cycle — origin-paper citation graph closed; library confirmed complete

Cycle focus: verify the library still meets the phase-1 exit test, work the
top of `derived/FRONTIER.md` that is not already struck through, and close the
one canonical origin-tier item never held. Verdict: the library is complete;
the only origin-tier gap (the 2001 paper itself) is publisher-blocked and is
provably non-load-bearing.

## 1. The origin paper (Casas-Alvero 2001) — citation graph fully covered

Ran `citation_graph` on the origin DOI `10.1006/jabr.2000.8727` ("Higher order
polar germs", J. Algebra 240(1):326-337, 2001). Result: **every work that
cites it, and every work it cites, is either held or declared out of scope**:

- **Citing works (all held):** Castryck–Laterveer–Ounaïes 2012 (arXiv:1208.5404)
  and 2014 (Math. Comp.); Battiston 2015 (arXiv:1511.04932); Yakubovich 2014
  and 2016; de Frutos Marín 2013 thesis; Cima–Gasull–Mañosas 2020; Gasull 2021.
- **Cited background (all out of scope per GOAL.md):** Teissier 1977
  "Variétés polaires", Merle 1977 "Invariants polaires", Zariski 1968
  equisingularity, Walker 1950, Enriques–Chisini 1919, Fischer 2001,
  Husemöller — the plane-curve-germ/polar singularity theory that Motivated CA
  but is explicitly background.
- **The paper itself** remains bronze-OA but network-blocked from this host
  (OpenAlex content 401, ScienceDirect 403, recorded in ROOT.md and
  `librarian-cycle-hessian-anchored.md`). Its statement, motivation, history
  and status are fully carried by the held secondary tier (Wikipedia entry,
  Schaub–Spivakovsky 2023, Berger ENS course, every survey).

**Conclusion:** no primary-source gap is left unattended. A future run with
working publisher access should retry the 2001 PDF, but nothing this run needs
to reason about is absent.

## 2. 2026 sweep re-confirmed — nothing new

`exa_search` restricted to research papers confirms the fresh-2026 arXiv sweep
(`research/sources/arxiv_search_casasalvero_fresh.full.md`, dated 2026-08-17)
is still complete: only already-held works surface (Ghosh 2501.09272 v2,
Schaub–Spivakovsky 2411.13967 / s40687-024-00444-z / 2312.08742, Ghosh
2402.18717, Castryck 1208.5404, Graf-von-Bothmer math/0605090). No new
settled degree, no new disproof, no new refereed partial result through the
2026 record.

## 3. Phase-1 exit test — still met

`research/ROOT.md` states, from held primary sources:
- status (CA open; Ghosh 2501.09272 v2 unverified preprint);
- minimal-counterexample structure (≥5 distinct roots / N≥6, no multiplicity
  ≥N−2, shared-root set ≠ size 2);
- verification bound (d≤7, d=8, d=12; smallest open = 20);
- restricted classes settled with hypotheses (p^k, 2p^k, 3p^k, 4p^k, 5p^k /
  6p^k / 7p^k with bad-prime lists; ≤4 distinct roots ⇒ CA; Massri degree-20;
  Ghosh finiteness).

Requests ledger empty. All top FRONTIER rows held or documented-blocked.
No download can be made this cycle that would settle a stated gap.

## Recorded for later runs

- **memory outage**: `remember_memory` failed (memory server health check
  timed out). This note is the fallback storage. Verify the memory store
  recovers before relying on Cognee recall.
- If a later run gains publisher/wayback access, fetch: Casas-Alvero 2001 PDF,
  de Frutos Marín 2015 JTN2015 note, Chávez Martínez 2018 UCrea thesis
  (all documented-blocked, claims-level coverage already in library).
