# Refuter: "uniformly in p" in the Parseval second-moment claim is false

A quick correction to the grounded approach
`research/approaches/meet-join-parseval-self-duality.md`, which asserts:

> E_p[S(n)²] = F_n(1−2p) = O(n), **uniformly in p ∈ (0,1)**.

**This is false.** As p → 0⁺ every term (1−2p)^{|M_d △ M_{d'}|} → 1, so

> F_n(1−2p) → (n−2)² = Θ(n²), not O(n).

The mechanism is the near-constant (kernel) input: h ≡ 0 (and h ≡ all-ones,
closed door 1) make every fold cell T(n,d)=0, every ε_d = +1, S(n)=n−2,
E[S²]=(n−2)². Concrete n=6 witness, all rows d=2,3,4,5 checked by hand and
confirmed by the engine (`code/refute/second_moment_p0_witness.p` —
find_counterexample: **proved**, i.e. all-zero h forces every ε_d = +1).

The correct statement is the already-proved `fold-distance-enumerator-On`: for
each **fixed** |z|<1 (p with |1−2p| ≤ z₀ < 1), F_n(z) = O(n), constant depending
on z. **The route's real working instance is unaffected** — the prime string sits
at p ≈ 0.585 (interior, |1−2p| ≈ 0.17) where the uniform-in-n bound holds. This
fixes wording only; it does not touch the Parseval identity, the Z=0 fair-model
reproduction, or the E[S²]=O(n) arithmetic input.

Claim: `parseval-second-moment-not-uniform-in-p` (code/out/refuter_parseval_uniform_p.md).
The two stale lines in the approach file are corrected.

One honest caution for whoever reads that file next: the phrase "under ANY
product measure … uniformly in p" would predict **no** fold collapse on
near-constant inputs, which is contradicted by the kernel collapse itself. It is
worth never quoting that clause again, since it is the exact false edge.
