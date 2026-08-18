# Library build report — 2026-08-18

## Restatement and scope
The target is Hilbert 16.2: for a planar polynomial field
\(\dot x=P(x,y),\dot y=Q(x,y)\), with \(P,Q\in\mathbb R[x,y]\) and degree at most \(n\), define \(H(n)\) as the supremum of the number of isolated periodic orbits (limit cycles). The conjecture asks whether \(H(n)<\infty\) for every \(n\ge2\), and asks for configurations. This run is building a source-backed library, not claiming a solution.

## Search and source work
I first inspected `problem.md`, `GOAL.md`, `research/ROOT.md`, and the derived frontier. I searched broadly in four directions: canonical definitions/status, DRR quadratic graphics, Abelian-integral bounds, and elementary-polycycle/analytic obstructions. Search results identified the Encyclopedia of Mathematics, MathWorld, Scholarpedia, Ilyashenko, Kaloshin, Kaleda–Shchurov, Binyamini–Dor, Rousseau–Shan–Zhu, Roussarie–Rousseau, Yeung, and Marín–Villadelprat.

Canonical encyclopedia records were already in the library (so duplicate downloads were refused):
- `research/summaries/canonical-encyclopedia-limit-cycle.md` with full text `research/sources/canonical-encyclopedia-limit-cycle.full.md`.
- `research/summaries/canonical-mathworld-hilbert-problems.md` with full text `research/sources/canonical-mathworld-hilbert-problems.full.md`.

Newly fetched/confirmed this cycle:
- `research/sources/scholarpedia-limit-cycles.full.md`, digest `research/summaries/scholarpedia-limit-cycles.md`.
- `research/sources/kaloshin-elementary-polycycle-2000.full.md`, digest `research/summaries/kaloshin-elementary-polycycle-2000.md`.
- `research/sources/marin-villadelprat-dulac-map-local-setting-2020-full.full.md` was already held; a DOI fetch yielded only a 110-byte landing capture, so the full held source is the evidence.
- The RSZ and RR 2015 sources already existed under their held filenames; I read the actual RR full text and RSZ full abstract rather than duplicating them.

## Source-backed findings
- The Encyclopedia of Mathematics says individual polynomial fields have finitely many limit cycles, while no degree-uniform bound is known even for degree 2; it also emphasizes the Poincaré return map as the object controlling limit-cycle properties. This is orientation, not primary proof evidence.
- Kaloshin’s source formulates the Hilbert–Arnold local problem for a generic \(k\)-parameter family near a polycycle and seeks a uniform cyclicity bound. This is restricted-family context, not H16.2 itself.
- Rousseau–Shan–Zhu (arXiv:1502.00689) state finite cyclicity for the two triple-nilpotent saddle graphics \((I^1_{12})\) and \((I^1_{13})\) in quadratic systems.
- Roussarie–Rousseau (arXiv:1506.07104), read at lines 1–120 of the held full source, state that DRR reduces quadratic finiteness to 121 graphics. They prove full finite cyclicity for \((I^1_{14})\), and boundary limit-periodic-set cyclicity for \((I^1_{6b})\), \((H^3_{13})\), and \((DI_{2b})\). They explicitly identify \((H^3_{14})\) as the one exception among those boundary cases and explain why boundary-set control does not by itself prove full graphic cyclicity.
- The same RR source records the structural method: blow up the family; write displacement functions as finite sums of center-ideal generators times generalized monomials and controlled factors; use Dulac maps and a generalized derivation–division algorithm. This is precisely the displacement-function route required by the problem.
- Existing held sources establish the restricted classes in `research/ROOT.md`: elementary polycycles in generic finite-parameter families (Kaloshin/Kaleda–Shchurov), Abelian integrals for polynomial Hamiltonian perturbations (BNY/Binyamini–Dor), and several named quadratic graphics (DRR/RR/RSZ).

## Evidence labels and falsifiers
All literature findings above are `asserted-by-source`, not independently formalised. They would be falsified by a primary source with a different theorem hypothesis, a corrigendum withdrawing the result, or a direct contradiction in the full paper. No claim here proves the global conjecture. The RR count and DRR inventory remain historically inconsistent (121 in the RR/DRR framework versus 125 in Shan's thesis), so the exact complete current ledger remains an open library request.

## What is now available locally
The relevant source corpus is under `research/sources/`, with short digests in `research/summaries/`; the root synthesis is `research/ROOT.md`. Durable memory was updated with the RR/RSZ findings and the source locations. The workspace's existing Lean and oracle work remains the formal/computational layer; this cycle added no unverified numerical conclusion.
