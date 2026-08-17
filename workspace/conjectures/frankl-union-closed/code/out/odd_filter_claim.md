# Filed claim: odd-filter max-density extremal — value correct, uniqueness false

<!-- regenerator-trigger -->

Result of task `verify-odd-filter-minmax`, settled by running the three
already-written programs
(`code/out/odd_filter_min_maxdensity_verify.py`,
`code/out/odd_filter_minimizers_char.py`,
`code/out/odd_filter_minimizers_general.py`), all previously un-executed; the
combined run is captured in `code/out/odd_filter_minmax.captured.txt` (3 parts,
exit 0 each). The claim below is verified-computationally — the exhaustive
enumeration is a measurement, not a proof, and its ceiling is stated.

```claim
id: odd-filter-max-density-extremal-nonboolean
statement: Among NON-Boolean union-closed families F ⊆ 2^[n], the minimum over
F of max_x density_x equals 2^{n-1}/(2^n-1) — but this value is NOT attained
uniquely by the odd filter F = 2^[n]\{∅}: for every n ≥ 2 the minimizers are
exactly n+1 families, the odd filter plus, for each x ∈ [n], the power-set-
minus-singleton family F_x = 2^[n]\{{x}} (each non-Boolean, |F| = 2^n − 1,
max density 2^{n-1}/(2^n-1)). The claimed UNIQUENESS is False.
hypotheses: F finite union-closed over [n], non-Boolean (not a Boolean
subalgebra / not closed under symmetric difference); max_x density = max
integer count / |F|.
holds-here: yes
status: verified-computationally — value and minimizer set by exhaustive oracle
enumeration of ALL union-closed families for n = 2,3,4 (2^(2^n) subfamilies,
65536 at n=4; UC counts 12/120/4958 = A102896's 13/121/4959 minus the excluded
{{∅}} family), and the structural facts (each minimizer union-closed,
non-Boolean, same bound) confirmed for general n by exact arithmetic and direct
oracle checks n = 2..8. The VALUE being the true minimum over all non-Boolean
UC families for a general n depends on step-1's Frankl bound
(max density ≥ 1/2, strict > 1/2 for non-Boolean) and on the even-m bound
(max ≥ m/2+1) which the sympy step checks PASS; for n ≤ 11 UC is itself
machine-verified, so the value is unconditional there. The n+1-minimizers
counterexample to uniqueness is unconditional for every n ≥ 2.
bearing: corrects the extremal-counting claim in the abundance-profile front —
the odd filter is NOT the unique most-balanced non-Boolean UC family; the
power-set-minus-singleton families tie it. It also feeds the minimal-
counterexample profile search: at m = 2^n − 1 the max density cannot be pushed
below 2^{n-1}/(2^n-1) by going non-Boolean, and several families achieve it.
anchor: code/out/odd_filter_minmax.captured.txt (the run);
code/out/odd_filter_min_maxdensity_verify.py,
code/out/odd_filter_minimizers_char.py, code/out/odd_filter_minimizers_general.py
(programs); the step-by-step verdict matching this claim is also in
code/out/odd_filter_claim_verdict.md (written before the run, now carried by
the capture).
ceiling: exhaustive minimizer enumeration only for n ≤ 4 (2^(2^n) subfamilies —
the sanctioned oracle bound; n = 5 would be 2^32 and is not attempted).
Structural/closed-form facts verified by direct oracle only to n = 8. The
value-minimality for general n rests on the sourced Frankl/even-m bounds, not
on enumeration.
```