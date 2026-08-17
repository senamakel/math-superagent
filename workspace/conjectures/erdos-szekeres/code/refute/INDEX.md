# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `es4-equals-5-fragment.p` | Diagnostic TPTP: weak CC fragment (axioms 1-3 only, no interiority/transitivity, no at-most-one-interior axiom) for ES(4)=5. Verdict: refuted with a non-realizable abstract chirotope (two points mutually inside each other's triangles) — concrete witness of the abstract-vs-realizable trap. Shows axioms 4-5 are necessary. |
| `pattern_triangular_n8_attack.py` | Refuter heavy-sampling attack on the n=8 realized-terminal-pattern-count claim (es-construct-realized-pattern-classes-triangular): hunt a 22nd convex-7 block pattern beyond the claimed 21. Exact integer arithmetic, 28-core parallel. |
| `r-extremal-structure-n4.p` | TPTP refutation attempt for R-extremal-structure's fixed hull-size part at the smallest case n=4: 4 points, no convex quadrilateral => some point interior (hull <= 3). Fresh target not covered by prior refuter sessions on the interior rungs. |
| `r-k-interior-n4-k2.p` | TPTP refutation attempt for weakened rung R-k-interior, worst small case n=4,k=2 (5 points, triangle hull, need convex quadrilateral). Verdict: proved (SZS Theorem) from the CC fragment axioms — exactly ES(4)=5 in its most hostile subclass. |
| `r-k-interior-refutation.md` | Refuter verdict on R-k-interior: R-k-interior(n,k) <=> ES(n) <= 2^(n-2)+1, so it is logically equivalent to the conjecture, not a genuine weakening; all small instances are settled values ES(4..6); new machine check at n=4,k=2 returns SZS Theorem. Redirects refutation to the run's own sampled structural claims (n=8 triangular patterns). |
| `r-one-interior-n4-fullcc.p` | TPTP refutation attempt for R-one-interior n=4 over the full Knuth CC-system axiom set, convexity axiom-native via hull edges (all-points-extreme). Verdict: proved (SZS Theorem) — abstract CC analogue of ES(4)=5 true; also the run's first encoder-validation rung. Earlier buggy version (vacuous hull_edge guards) returned spurious refuted; fixed. |
| `r-one-interior-n4.p` | TPTP refutation attempt for the R-one-interior weakened rung, tightest case n=4 (5 points): general-position CC fragment + interior/triangle + at-most-one-interior + convex4 via 4-point criterion. Verdict: proved (SZS Theorem) — the statement holds already at n=4 in this faithful abstract fragment. |
| `r-one-interior-refutation.md` | Refuter verdict on the current weakened rung R-one-interior: proved (hand one-line hull-count for all n + machine SZS Theorem at the tightest case n=4 in both the weak-fragment and full-CC encodings). Records that the weak-fragment es4-equals-5 diagnostic 'refuted' is the abstract-vs-realizable trap, not a counterexample, and that the rung's merge text belongs to R-k-interior k>=2. |
| `r-one-interior-refutation2.md` | Refuter report on the current weakened rung R-one-interior: proved (trivially true by hull-count argument, all n; two fresh find_counterexample runs return SZS Theorem). Redirects future refutation to R-k-interior k>=2 (first target n=5,k=5) and the n=8 sampled triangular-pattern claim as the most-likely-false finding. |
| `refuter-report.md` | Refuter verdict on the current rung R-one-interior (proved, hand+machine), the tool calibration (proved/refuted/proved), and the staged-but-unrun n=8 pattern attack pointing at the run's own sampled claims. |
| `rk_interior_probe.py` | _(undescribed)_ |
| `run_probe.py` | _(undescribed)_ |
