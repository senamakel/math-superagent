# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `berthe_imbert_ostrowski.md` | **Digitized.** Berthe-Imbert (DMTCS 11:1, 2009): Ostrowski numeration of integers/reals, Algorithm 2 (inhomogeneous best-left approximations), Props 4-6 (correctness, O(log log x)), Prop 7 (two-sided greedy fails naive). Independent one-sided check on the run's Cabanillas method; corroborates both-signs-of-b correction and the "records not semiconvergents" finding. |
| `cabanillas_labbe_nearest.md` | arXiv landing metadata only; **no content**. Redundant with cabanillas_variant_pdf.*; kept for provenance, nobody should read it again. |
| `cabanillas_prop9_10_exact_statement.md` | Exact transcription of Cabanillas Algorithm 3(ii) and Props 9/10 (both rational & irrational cases) from the PDF, with hypothesis checks and the O(log L) candidate-union argument for PE591. |
| `cabanillas_variant_pdf.md` | **Primary source** (arXiv:1904.01874v2), read in full: the α-numeration algorithm (Alg 3(ii)) and Props 9/10 giving the exact O(log L) candidate set for the argmin of ||nα−β||_Z. This is the method solution.py uses for PE591. |
| `ostrowski_wikipedia.md` | **Digitized.** Background: classical Ostrowski integer & real numeration bases from convergent denominators; Zeckendorf case. No inhomogeneous result; context only. |
| `three_gap_wikipedia.md` | **Digitized.** Background: three-gap/Steinhaus theorem statement, history (Sós/Surányi/Świerczkowski), Liang proof. Homogeneous only; explains why inhomogeneous theory (Cabanillas) is needed. |

## Notes (research/notes)

| File | Purpose |
| --- | --- |
| `inhomogeneous_record_structure.md` | The run's consolidated theory report: reduction to min over b of ||bα−β||_Z, why semiconvergent hypothesis is false in the inhomogeneous case, exact O(log L) answer via Cabanillas Props 9/10 and the one-sided Berthe-Imbert Algorithm 2, full source list. Governing theory behind solution.py. |
| `pattern_analysis.md` | Pattern-finder report: record-b sequences (Cabanillas candidates, no linear/polynomial regularity); |I_d| laws (nint(b√d−π), m²d scaling); corrected S = 526007984625966. |
