# linear-supply-threshold-limit-g-krawtchouk-parity

```skeleton
lemma: For h uniform among the C(n,w) weight-w strings and any M ⊆ {0,…,n−1} with |M| = m, Pr[⊕_{j∈M} h[j] = 1] = ½(1 − K_m(w;n)/C(n,m)) with K_m(x;n) the Krawtchouk polynomial, so E[(−1)^{T_M}] = K_m(w;n)/C(n,m). Anchors: w=0 gives 1, w=1 gives 1−2m/n, w=n gives (−1)^m.
next: symbolic_math: verify for all n ≤ 30, all w ∈ [0,n], all m ∈ [0,n] against the exact hypergeometric parity expectation, and reproduce the three anchors. theorem_prover: classical ₂F₁(−m,−w;n−w−m+1;t) at t=−1 identity (library carries krawtchouk-polynomials-encyclopedic and essential-coding-theory-machinery, both asserted-not-checked; this upgrades the parity form to checked).
reason: Duplicate of the per-cell Krawtchouk evaluation already stated as gap G-sphere-mean inside research/backward/linear-supply-threshold-limit.md. Recorded via record_entry with a `lemma` field instead of a `goal` field, which made the derivation read it as a skeleton with no goal. The live version is G-sphere-mean in that file.
status: spent
```
