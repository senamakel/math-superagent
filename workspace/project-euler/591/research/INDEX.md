# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

NOTE: the automated `refresh_index` tool truncates this folder's index (it treats `*.full.md` companions, the section headers, and the `notes/` table as stale and drops them). Maintain this file by hand: list every `.md` and `.full.md` below, plus the `notes/` subsection.

## Primary source (the method)

| File | Purpose |
| --- | --- |
| `cabanillas_variant_pdf.md` | **Primary source summary** (arXiv:1904.01874v2, 12 Sep 2019, E. Cabanillas, "A variant of Ostrowski numeration", https://arxiv.org/pdf/1904.01874): the α-numeration algorithm (Alg 3(ii)), Def. 6, and Propositions 9/10 giving the exact O(log L) candidate set for the argmin of the distance of n*alpha-beta to nearest integer — the method solution_bothsides.py uses for PE591. Sections, hypotheses checks, and what it does not settle. |
| `cabanillas_variant_pdf.full.md` | The complete converted PDF text of arXiv:1904.01874v2 (~90 KB). Fallback for questions the summary does not answer. |
| `cabanillas_prop9_10_exact_statement.md` | Verbatim-transcribed precise statements (with section numbers and hypotheses) of Algorithm 3(ii), Definition 6, and Propositions 9/10 (irrational-alpha Case 2) — the citable theorem underlying the O(log L) candidate method for PE591, plus the correctness argument tying the candidate set to the PE591 minimum. Cross-checked against the summary. |
| `cabanillas_labbe_nearest.md` | arXiv landing page (metadata only) for the same paper; no mathematical content. **Redundant with cabanillas_variant_pdf.*; kept for provenance only.** |
| `cabanillas_labbe_nearest.full.md` | Raw arXiv HTML landing page for arXiv:1904.01874. Fallback; contains only bibliographic metadata, no content. Nobody should read it again. |

## Independent corroboration

| File | Purpose |
| --- | --- |
| `berthe_imbert_ostrowski.md` | **Digitized.** Summary of Berthé & Imbert, "Diophantine Approximation, Ostrowski Numeration and the Double-Base Number System" (DMTCS 11:1 (2009) 153-172, https://dmtcs.episciences.org/450/pdf): their one-sided (best-left) inhomogeneous approximation algorithm (Alg 2, Props 4-6, O(log log x)), the three-gap basis, and Prop 7 showing naive two-sided greedy fails. Independent corroboration of the run's Cabanillas method and of the both-signs-of-b correction; not the primary method (it is one-sided). |
| `berthe_imbert_ostrowski.full.md` | The complete converted PDF text of the Berthé–Imbert DMTCS paper (~42 KB). Fallback for the summary. |

## Background (setup only)

| File | Purpose |
| --- | --- |
| `ostrowski_wikipedia.md` | **Digitized.** Background summary of the Wikipedia Ostrowski numeration article: classical integer and real Ostrowski numeration bases from CF convergent denominators, Zeckendorf case. No inhomogeneous result; context only. |
| `ostrowski_wikipedia.full.md` | The full Wikipedia Ostrowski numeration article text (~7 KB). Fallback for the summary. |
| `three_gap_wikipedia.md` | **Digitized.** Background summary of the Wikipedia Three-gap theorem article: statement and history of the Steinhaus conjecture, and why the three-gap theorem (homogeneous) cannot by itself solve the fixed-target (inhomogeneous) PE591 problem. |
| `three_gap_wikipedia.full.md` | The full Wikipedia Three-gap theorem article text (~50 KB). Fallback for the summary. |

## The run's own notes (in `notes/`)

| File | Purpose |
| --- | --- |
| `notes/inhomogeneous_record_structure.md` | The run's consolidated theory report: restates the PE591 reduction to min over b in [0,L] of the distance of b*alpha-beta to nearest integer, explains why the semiconvergent-denominator hypothesis is false in the inhomogeneous case, and gives the exact O(log L) answer via Cabanillas Prop 9/10 plus Berthé–Imbert, with a worked derivation and the full source list. The governing theory (with the both-signs-of-b handling) behind solution.py / solution_bothsides.py. |
| `notes/pattern_analysis.md` | Earlier pattern-finder report on the computed data: record-b sequences per d, and the verified structural facts (record-b sequences are Cabanillas candidates; |I_d| = nint(b_d*sqrt(d)-pi); the m^2*d scaling rule) and non-facts (no linear/polynomial regularity). NOTE: its single-form |a| identity is superseded by notes/pattern_verify.md's sign-split master identity. |
| `notes/pattern_findings.md` | Pattern-finder report on the n=1e13 both-sign data (results_full_bothsides.txt, S=526007984625966): verified exact laws over all 90 d (sign-opposition; master |a| identity; m^2-scaling 36/36; equal-|a| groups with common squarefree part) and non-structure (no polynomial or low-order linear recurrence in d; b_d not semiconvergents). |
| `notes/pattern_verify.md` | **Current** pattern-finder independent verification from results_full_bothsides.txt: re-confirms no in-d recurrence, re-verifies sign-opposition 90/90 and the m^2-scaling law 36/36 and 18/18, and CORRECTS the master identity to the sign-split form. Supersedes the single-form identity in pattern_analysis.md / pattern_findings.md. |

See `notes/INDEX.md` for the same four files described from inside that folder.
