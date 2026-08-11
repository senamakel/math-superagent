# Index — research/notes

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

Run-produced derivations, theory reports, and pattern analysis (not downloaded sources - those live in research/ directly).

| File | Purpose |
| --- | --- |
| `inhomogeneous_record_structure.md` | The run's consolidated theory report. Restates the PE591 reduction to the inhomogeneous problem min over b in [0,L] of the distance of b*alpha-beta to nearest integer (alpha = fractional part of sqrt(d), beta = fractional part of pi); explains why the semiconvergent-denominator hypothesis is false in the inhomogeneous case; and gives the exact O(log L) answer via Cabanillas Prop 9/10 plus Berthe-Imbert, with a worked derivation and the full source list. The governing theory behind solution.py. |
| `pattern_analysis.md` | Pattern-finder report on the computed data: the record-b sequences for several d, the abs(I_d) values, and the b_d at n=1e13. States the verified structural facts (record-b sequences are Cabanillas candidates; abs(I_d) = nint(b_d*sqrt(d)-pi) = nint(b_d*sqrt(d))-3 at n=10^4; the m^2*d scaling rule) and the non-facts (no linear recurrence, no polynomial structure). |
