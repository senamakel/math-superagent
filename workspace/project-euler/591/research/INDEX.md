# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

Ordered by usefulness to the goal. Each summary `<name>.md` has a full-text companion `<name>.full.md`; read the summary first, open the full text only when the summary does not answer the question.

| File | Purpose |
| --- | --- |
| `cabanillas_variant_pdf.md` | **Primary source** (arXiv:1904.01874), read in full: the alpha-numeration algorithm (Algorithm 3(ii)) and Propositions 9/10 giving the exact O(log L) candidate set for the argmin of the distance of n*alpha-beta to nearest integer. This is the method solution.py uses for PE591. |
| `cabanillas_variant_pdf.full.md` | Complete converted text of the Cabanillas paper (arXiv:1904.01874v2, 90KB). Fallback for anyone who has read the summary and needs the actual Propositions and algorithm. |
| `berthe_imbert_ostrowski.md` | Summary of Berthe-Imbert, Diophantine Approximation, Ostrowski Numeration and the Double-Base Number System (DMTCS 11:1, 2009, pp.153-172): their one-sided inhomogeneous best-left approximation algorithm built on the three-gap theorem. **Excerpt only - not yet replaced with a real summary by the scholar.** |
| `berthe_imbert_ostrowski.full.md` | Complete converted text of the Berthe-Imbert paper (42KB). Read only via the summary above. |
| `ostrowski_wikipedia.md` | Summary of the Wikipedia Ostrowski numeration article: integer and real Ostrowski numeration bases derived from continued-fraction convergents. **Excerpt only - not yet replaced with a real summary by the scholar.** |
| `ostrowski_wikipedia.full.md` | Complete converted text of the Ostrowski numeration Wikipedia article (7KB). |
| `three_gap_wikipedia.md` | Summary of the Wikipedia Three-gap theorem article: statement and history of the Steinhaus conjecture - the orbit points {n*alpha} divide the circle into at most three distinct arc lengths. **Excerpt only - not yet replaced with a real summary by the scholar.** |
| `three_gap_wikipedia.full.md` | Complete converted text of the Three-gap theorem Wikipedia article (50KB). |
| `cabanillas_labbe_nearest.md` | arXiv landing page (metadata only) for Cabanillas' paper; kept for provenance, no mathematical content. Redundant with cabanillas_variant_pdf.* |
| `cabanillas_labbe_nearest.full.md` | Full converted text of the same arXiv landing page (metadata only, no mathematical content). Redundant - open neither. |

## research/notes

The run's own derivations and reports live in `notes/`, indexed by `notes/INDEX.md` (see below), not in this table.

## Why the sources are here
Berthe-Imbert (one-sided) and the Wikipedia three-gap / Ostrowski pages give the classical context; Cabanillas' Prop 9/10 is the exact both-sided algorithm that actually solves the problem. See `notes/inhomogeneous_record_structure.md` for the consolidated theory and why the semiconvergent-denominator hypothesis fails here.
