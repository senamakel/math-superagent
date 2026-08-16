# Chase & Lovett, "Approximate union closed conjecture" (arXiv:2211.11689)

**Full text:** [[chase-lovett-approximate-union-closed-2022.full]]

Verifies Gilmer's (3−√5)/2 conjecture; extends it to (1−ε)-approximate union-closed families (where nearly all pairs have union in F); and shows (3−√5)/2 is **optimal** for that relaxation.

```claim
id: chase-lovett-approximate
statement: For (1−ε)-approximate union-closed families (ε < 1/2, nearly all pixel- unions in F), some element is in at least ψ = (3−√5)/2 fraction of sets; ψ is optimal for this relaxation.
hypotheses: (1−ε)-approximate union-closed, ε < 1/2
holds-here: yes, as a statement about the iid entropy inequality
status: proved
bearing: Makes precise that (3−√5)/2 is a *real* barrier for the iid/approximate method, not slack in estimates — the extremal distributions achieve it. This is the cleanest "the method is capped at c₀<1/2" statement in the library.
anchor: research/sources/chase-lovett-approximate-union-closed-2022.html.full.md
follows-from: ahs-barrier-3-minus-rt5-over-2
```

**Bearing for this run:** the strongest available support for a "barrier theorem" — the iid entropy method is provably capped at (3−√5)/2 < 1/2. Any attempt to push the Gilmer-form entropy inequality past 1/2 must leave the iid/approximate class.
