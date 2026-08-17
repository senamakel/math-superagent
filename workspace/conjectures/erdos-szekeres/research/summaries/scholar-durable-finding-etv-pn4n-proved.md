# Durable finding (memory server down — workspace record for later Cognee store)

**Finding — Baek's ETV primary proves P(n,4,n) (status upgrade).**

Baek, "On the Erdős–Tuza–Valtr Conjecture", arXiv:2206.04260v2, full text on disk at
`research/sources/ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md`, **proves** P(n,4,n):
any (n−1 choose 2)+2 points in general position contain a 4-cap or an n-gon, via the
combinatorial generalization Theorem 2.7 (arbitrary order-colored 3-uniform hypergraph
configurations). Complete proofs are in the held text:

- Theorem 3.2: a slope labeling always exists (label(e) = cap-length starting at e − 1).
- Theorem 3.6: α-statistic p ↦ (α_1(p),…,α_{a−2}(p)) is injective into the grid simplex
  T_{a,b}, |T_{a,b}| = C(a+b−4, a−2); hence set-theoretic cups-caps |S| ≤ C(a+b−4,a−2).
  (Proof at lines 377–395 of the full text.)
- Lemma 5.2: a pair of interweaved laced (n−1)-cups forces a (3,n−1)-gon. (Proof lines 603–630.)
- Theorem 5.10: any 4-cap,n-cup-free configuration of size (n−1 choose 2)+2 contains a pair
  of interweaved laced (n−1)-cups, by induction on n via the (α,β)-plane rows R_i and the
  deletion set ∆ = {x_1,…,x_{n−2}}. (Proof lines 748–900.)
- Theorem 2.7 follows immediately (5.10 + 5.2).

Status upgrades applied to the ETV note: `baek-ETV-n4n`, `etv-alpha-statistic-injective`,
`baek-interweaved-laced-cups` → **proved**. `etv-equivalent-to-es` stays **asserted**
(cited to Erdős–Tuza–Valtr 1996; not proved in the held text).

Bearing: P(n,4,n) is the first new ETV case since the 1935 cups-caps theorem and the ETV
conjecture is equivalent to the ES conjecture (Theorem 1.5), so this is a genuine
restricted-class partial result on ES — but the bound (n−1 choose 2)+1 ≈ n²/2 is
polynomially far below 2^{n−2}, so it does not touch the ES(7) frontier at N=33.

Open generalization: Conjecture 5 (size (n−1 choose 2)+k forces k mutually interweaved
laced (n−1)-cups) is proved only for k = 1, 2, n.

Store to Cognee when the memory server recovers. Source: scholar digest cycle, this run.

To store verbatim into Cognee later:
```
remember_memory { text: "Baek's ETV primary (arXiv:2206.04260v2, full text on disk) PROVES P(n,4,n): ... ", source: "scholar digest cycle; ... ETV-on-the-Erdos-Tuza-Valtr-Conjecture.md" }
```