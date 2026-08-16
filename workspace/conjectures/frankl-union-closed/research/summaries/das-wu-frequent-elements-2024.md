# Das & Wu, "Frequent elements in union-closed set families" (arXiv:2412.03862, v3 Jul 2025)

**Source URL:** https://arxiv.org/pdf/2412.03862 (downloaded; full text at
`research/sources/das-wu-frequent-elements-2024.full.md`)

## What it is
A recent (2024/2025) paper combining the entropic method of Gilmer with the combinatorial arguments of Knill. It attacks Nagel's generalisation (Conj 1.2): in a union-closed family with |∪F| ≥ k, the kth-most frequent element lies in at least |F|/(2^{k−1}+1) sets.

```claim
id: daswu-nagel
statement: For k ≥ 2 and |∪F| ≥ k, the kth-most frequent element lies in at least |F|/(2^{k−1}+1) sets, with equality iff F is a near-k-cube (= Boolean lattice 2^[k−1] plus one extra set).
hypotheses: F union-closed, |∪F| ≥ k ≥ 2
holds-here: yes
status: proved (Theorem 1.4; uses both entropy and Knill methods)
bearing: proves Nagel's conjecture exactly; the near-k-cube equality witnesses the sharpness.
anchor: research/sources/das-wu-frequent-elements-2024.full.md
```

```claim
id: daswu-record-0-3823455
statement: The current best constant for Frankl's conjecture is ≈ 0.3823455 = 0.38234 (355), obtained by Sawin's dependent-coupling method as evaluated by Yu and Cambie; no source in this library exceeds it unconditionally. This is where things stand as of 2025.
hypotheses: F union-closed, finite, nonempty
holds-here: yes
status: asserted-by-source (survey statement; primary values are Yu arXiv:2212.00658 ≈0.38234 and Cambie arXiv:2212.12500)
bearing: THE current-record claim this run may rely on: 0.3823455. Distinguish from Liu's conditionally-IID value ~0.38271 which is conditional (see liu-conditionally-iid).
anchor: research/sources/das-wu-frequent-elements-2024.full.md
answers: exact-current-published-c8b8
follows-from: yu-record-0-38234, cambie-question2-exact-0-3823455
```

```claim
id: daswu-large-kth
statement: For 0 ≤ α < (3−√5)/2 there is c_α≥0 such that if |F| ≥ 2^{c_α(k−1)} then at least k elements each appear in ≥ α|F| sets.
hypotheses: F union-closed, k ≥ 2, α < (3−√5)/2
holds-here: yes
status: proved (Theorem 1.5)
bearing: the Gilmer bound transfers to the kth-most-frequent element on large families.
anchor: research/sources/das-wu-frequent-elements-2024.full.md
```

## Why it matters to this run
- Confirms (2025) the current record at **≈0.3823455** unconditional, reconciling Yu (0.38234) and Cambie, and explicitly stating Liu's further value is conditional.
- The **near-k-cube** equality characterisation is relevant to the "barrier/extremal object" programme: the (3−√5)/2-zone families approach a specific structural shape.
- Confirms the verified range lineage: Vučković–Živković n≤12, Roberts–Simpson |F|≥4n−1, Balla–Bollobás–Eccles |F|≥2^{3n/2}, Knill |F|−1/log₂|F|, Reimer log₂|F|/(2n)|F|.

## Status of the claims
Sourced (theorems in a 2025 preprint). Conjectures 1.1 (Frankl) and 4.2 (f_k → 1/2) remain open.
