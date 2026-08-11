# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `berthe_imbert_ostrowski.md` | **Digitized.** Summary of Berthé & Imbert, "Diophantine Approximation, Ostrowski Numeration and the Double-Base Number System" (DMTCS 11:1 (2009) 153-172, https://dmtcs.episciences.org/450/pdf): their one-sided (best-left) inhomogeneous approximation algorithm (Alg 2, Props 4-6, O(log log x)), the three-gap basis, and Prop 7 showing naive two-sided greedy fails. Independent corroboration of the run's Cabanillas method and of the both-signs-of-b correction; not the primary method (it is one-sided). |
| `cabanillas_labbe_nearest.md` | arXiv landing page (metadata only) for the same paper; no mathematical content. **Redundant with cabanillas_variant_pdf.*; kept for provenance only.** |
| `cabanillas_prop9_10_exact_statement.md` | Verbatim-transcribed precise statements (with section numbers and hypotheses) of Algorithm 3(ii), Definition 6, and Propositions 9/10 (irrational-alpha Case 2) — the citable theorem underlying the O(log L) candidate method for PE591, plus the correctness argument tying the candidate set to the PE591 minimum. Cross-checked against the summary. |
| `cabanillas_variant_pdf.md` | **Primary source summary** (arXiv:1904.01874v2, 12 Sep 2019, E. Cabanillas, "A variant of Ostrowski numeration", https://arxiv.org/pdf/1904.01874): the α-numeration algorithm (Alg 3(ii)), Def. 6, and Propositions 9/10 giving the exact O(log L) candidate set for the argmin of the distance of n*alpha-beta to nearest integer — the method solution_bothsides.py uses for PE591. Sections, hypotheses checks, and what it does not settle. |
| `ostrowski_wikipedia.md` | **Digitized.** Background summary of the Wikipedia Ostrowski numeration article: classical integer and real Ostrowski numeration bases from CF convergent denominators, Zeckendorf case. No inhomogeneous result; context only. |
| `three_gap_wikipedia.md` | **Digitized.** Background summary of the Wikipedia Three-gap theorem article: statement and history of the Steinhaus conjecture, and why the three-gap theorem (homogeneous) cannot by itself solve the fixed-target (inhomogeneous) PE591 problem. |
