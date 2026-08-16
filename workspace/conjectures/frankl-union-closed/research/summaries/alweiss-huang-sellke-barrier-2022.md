# Alweiss, Huang, Sellke, "Improved lower bound for Frankl's conjecture" (arXiv:2211.11731, v4 Jul 2024)

**Full text:** [[alweiss-huang-sellke-barrier-2022.full]]

Confirms Gilmer's conjectured inequality and proves the (3−√5)/2 ≈ 0.38197 bound. One case of the inequality is checked by computer.

```claim
id: ahs-barrier
statement: Every nonempty union-closed family has an element in at least (3−√5)/2 ≈ 0.38197 of its sets.
hypotheses: F union-closed, F ≠ {∅}, |F| finite
holds-here: yes
status: proved
bearing: (3−√5)/2 is the value of the tight iid-OR entropy inequality, i.e. the maximum of E[H(X∪Y)]/E[H(X)] over the min-densities. It is a barrier to the *iid-twin* form of Gilmer's method, not to the conjecture.
anchor: research/sources/alweiss-huang-sellke-barrier-2022.full.md
answers: exact-current-published-c8b8
```

```claim
id: ahs-gilmer-conj
statement: Verifies the explicit one-variable inequality conjectured by Gilmer that yields the constant.
hypotheses: the tight one-parameter entropy inequality h(x²) family
holds-here: yes
status: proved
bearing: pinpoints exactly where the iid method saturates; the associated extremal distributions are the object a "barrier theorem" must exhibit.
anchor: research/sources/alweiss-huang-sellke-barrier-2022.full.md
```

**Bearing:** this is what (3−√5)/2 is a barrier *for* — the iid-OR entropy inequality. Chase–Lovett later showed the same value is *optimal* for the (1−ε)-approximate relaxation, so the barrier is real for iid, but Sawin's dependent couplings escape it.
