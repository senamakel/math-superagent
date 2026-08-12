# Grounding summary — exponent-signature-first is not a new direction

The full analysis and literature evidence are stored in durable memory and
condensed into the `precedent` / `verdict` fields of
`research/approaches/exponent-signature-first.md` itself.

**Bottom line:** the exponent-signature-first search is exactly Goto & Shibata's
§3 three-step algorithm (Math. Comp. 2004) for harmonic numbers — list ω(n),
list exponent types, list prime possibilities — using the same monotonicity and
the same sorting lemma (their §3.3 and Lemma 4.2). The sorting lemma also appears
independently in colossally/superabundant-number theory (Alaoglu–Erdős 1944).
For the hemiperfect/multiperfect σ-equation target family specifically, the
published standard is the interleaved tree-search over prime powers
(Flammenkamp; Alekseyev arXiv:2601.17832), which is what the run's
denominator-cancellation DFS already implements.

So the approach is **grounded as a real technique but not novel** and offers no
advantage over the run's existing method. The exact count of feasible signature
shapes at 10^18 is not in the literature and was not computed in this run
(unverified; finiteness is standard via e1 ≤ log2(10^18) ≈ 59 and the product
constraint).
