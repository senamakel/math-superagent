# Pebody, "Extension of a method of Gilmer" (arXiv:2211.13139)

**Full text:** [[pebody-extension-2022.full]]

Achieves (3−√5)/2 by solving the sharp optimization: given a binary X possibly depending on an auxiliary S with given E(X) and H(X|S), minimize H(X₁∪X₂ | S₁,S₂) for independent (X₁,S₁),(X₂,S₂).

```claim
id: pebody-optimization
statement: The best constant obtainable by the iid-OR entropy inequality (with an auxiliary variable S) is (3−√5)/2, found as the optimum of a conditional-entropy problem.
hypotheses: iid coupling of (X,S), H(X|S) fixed, E(X) fixed
holds-here: yes (as the iid ceiling)
status: proved
bearing: states the barrier as an optimization: the value of min over distributions of E[H(X∪Y)]/E[H(X)]. Gives the precise object whose value a "barrier theorem" would compute for any coupling class it covers.
anchor: research/sources/pebody-extension-2022.html.full.md
follows-from: ahs-barrier-3-minus-rt5-over-2
```

**Bearing:** confirms and refines AHS's value. Together these four sources (AHS, Chase–Lovett, Sawin, Pebody) give (3−√5)/2, its optimality for iid and for the approximate relaxation, and the escape by dependent couplings.
