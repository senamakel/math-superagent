# Ellis, Ivan, Leader, "Small sets in union-closed families" (arXiv:2201.11484, v3 Jan 2023)

**Full text:** [[ellis-ivan-leader-small-sets-2022.full]]

Resolves the "3-set fault line" in problem.md: a union-closed family *containing a 3-element set* does **not** force an abundant element from that set.

```claim
id: eil-small-sets
statement: For any ε>0 there is a union-closed family F whose (unique) smallest set S has no element in more than a fraction ε of F; explicitly, with |S|=k, no element of S is in more than (1+o(1))·log₂k/(2k) of F.
hypotheses: union-closed; k = |S| can be as small as 3
holds-here: yes (this is why "contains a 3-set" is NOT sufficient for UC)
status: proved
bearing: proves the negative control "3-sets do not force an abundant element from that set" — the single-3-set case is Non-FC (Poonen); the threshold where 3-sets start to force it is FC(3,n)=⌊n/2⌋+1 (Pulaj).
anchor: research/sources/ellis-ivan-leader-small-sets-2022.full.md
```

**Note on a folklore tension (not a claim-to-claim contradiction):** this refutes the folklore belief that "a union-closed family containing a 3-set has an element from that set abundant." That belief is not a written claim in this library; it is refuted as *belief*, not as a claim.

**Bearing for this run:** directly relevant to the "families containing a specified small set" line. For k=3 the bound log₂3/(6) ≈ 0.264 < 1/2, so a family with a smallest 3-set can have all its elements below half — the smallest-set-size direction of a structural theorem about a minimal counterexample must be handled with this in mind (a minimal counterexample's smallest set can plausibly be size 3 or larger).
