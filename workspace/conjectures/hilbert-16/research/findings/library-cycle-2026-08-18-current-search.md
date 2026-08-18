# Library cycle report — 2026-08-18

## Search and triage performed

Searched Exa for the canonical H16.2 status, DRR graphics, elementary-polycycle bounds, and special Abelian-integral bounds. Read/triaged canonical Encyclopedia of Mathematics, Ilyashenko Centennial History, Rousseau–Shan–Zhu 2015, Roussarie–Rousseau 2015, Kaloshin/Kaleda–Shchurov, Binyamini–Dor, and a 2025 arXiv preprint. The canonical encyclopedia and primary sources were already held; no duplicate downloads were made. The ScienceDirect exact degree-4 result was triaged but its download returned 403, so it is not evidence.

## Verified/held findings

- The Encyclopedia of Mathematics source (`research/sources/canonical-encyclopedia-limit-cycle.full.md`, URL in file) defines a limit cycle as an isolated closed trajectory / nonconstant periodic solution, and states that individual polynomial fields have finitely many limit cycles while no uniform degree bound is known, even for degree 2.
- Ilyashenko's held Centennial History gives the individual-field finiteness theorem, but this does not provide coefficient-uniform H(n).
- Rousseau–Shan–Zhu 2015 (held full source `primary-rousseau-shan-zhu-nilpotent-saddle-graphics-2015-v1.full.md`) proves full finite cyclicity of `I^1_12` and `I^1_13`.
- Roussarie–Rousseau 2015 (held full source `primary-roussarie-rousseau-2015-center-graphics.full.md`) proves full finite cyclicity of `I^1_14`; its theorem for `I^1_6b`, `H^3_13`, `DI_2b` is boundary-limit-periodic-set only, and `H^3_14` is explicitly exceptional. This distinction is load-bearing.
- Kaloshin's held source gives `E(k) <= 2^(25 k^2)` for elementary polycycles in generic finite-parameter families. Kaleda–Shchurov gives `E(n,k) <= (2^(5 n^2)+20 n) k^(3 n)` when the number of singular vertices is fixed. These restricted results do not cover nilpotent/degenerate graphics.
- Binyamini–Dor's held source gives an explicit Abelian-integral zero bound `exp+2(n^2)*m + exp+5(n^2)`, linear in form degree, under polynomial Hamiltonian and continuous nonsingular oval hypotheses.
- New held preprint `research/sources/mucino-rebollo-abelian-trivial-monodromy-2025.full.md` (arXiv:2508.15925; summary alongside it) states that for primitive polynomial H on C² with trivial global monodromy, Abelian integrals extend polynomially and have explicit sharp bounds depending on degrees and generic-fiber homology rank. It is a preprint, so status is asserted-by-source, not formalised.

## Search failures and limits

- `citation_graph` was attempted on arXiv:1502.00689 but OpenAlex returned HTTP 429; no claim relies on it.
- Download of the 2019 ScienceDirect exact degree-4 hyperelliptic Abelian-integral paper returned HTTP 403. Exa/read_sources reports a sharp bound 3, but this remains a lead only.
- Durable memory service was unavailable during this cycle; this file is the local fallback and must be ingested later.

## Remaining gap

No authoritative post-2015 source giving a complete graphic-by-graphic current DRR ledger was found. The workspace's ROOT and REQUESTS already state this unresolved gap; do not turn the 121/125 discrepancy or unrefereed 2026 claims into established closure.