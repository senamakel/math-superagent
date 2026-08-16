# Bošnjak & Marković, "The 11-element case of Frankl's conjecture" (EJC 15(1)#R88, 2008)

**Full text:** [[bosnjak-markovic-eleven-element-case-2008.full]]

The machine-verified bound on the ground set.

```claim
id: bosnjak-markovic-11
statement: Frankl's (union-closed sets) conjecture holds for every union-closed family whose ground set |∪F| ≤ 11.
hypotheses: union-closed, |∪F| ≤ 11
holds-here: yes
status: proved (computer-assisted)
bearing: the exact verified range on the universe size n for this run.
anchor: research/sources/bosnjak-markovic-eleven-element-case-2008.full.md
```

```claim
id: faro-roberts-simpson-40
statement: A counterexample on an m-element ground set has at least 4m−1 member sets (Lo Faro / Roberts–Simpson); hence UC holds for all union-closed families with |F| ≤ 40.
hypotheses: union-closed, finite
holds-here: yes
status: proved (sourced, in the library's survey; the ≤40 inference combines n≤11 bound with the 4m−1 lemma)
bearing: the verified range on |F| for this run is ≤40 by this route; the survey separately cites |F|≤46/50.
anchor: research/sources/bosnjak-markovic-eleven-element-case-2008.full.md
follows-from: bosnjak-markovic-11
```

**Bearing for this run:** the numbers the oracle must reproduce (phase 3 of GOAL): all families with n≤11 or |F|≤40 are UC. A counterexample must have n≥12 and |F|≥41 (stronger than the 4m−1 minimal bound gives: with n≥12, |F|≥47).
