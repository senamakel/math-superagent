# Montgomery — Cycles and expansion in graphs (EMS Magazine survey)

Source: R. Montgomery, "Cycles and expansion in graphs", Eur. Math. Soc. Mag. 138
(2025) 5–12, doi:10.4171/MAG/287 (open access, CC BY 4.0).
Full text: `research/sources/montgomery-cycles-and-expansion-survey.full.md` (41 KB).

## What it establishes (survey of recent expansion-based progress on three cycle problems)

The article surveys three cycle problems whose recent progress uses *graph expansion*
(Komlós–Szemerédi sublinear expansion), and reports the Liu–Montgomery results.

### 1. Erdős–Gallai cycle decomposition
- Conjecture 1.1 (Erdős–Gallai): every n-vertex graph decomposes into O(n) cycles and edges.
- Theorem 1.2 (Bucić–Montgomery): any n-vertex graph decomposes into O(n log\* n) cycles and edges.
- Method: find a sublinear expander subgraph of near-same average degree, remove O(n) cycles to leave a graph with average degree log^{O(1)} d, iterate O(log\* n) times.

### 2. Cycle lengths and the Erdős–Hajnal odd cycle problem — **the section relevant to E–G**
- Verstraëte 2005 (non-constructive): some increasing even-length sequence of limiting density 0 is unavoidable for average degree ≥ 10.
- Erdős asked specifically whether the *powers of 2* could be such a sequence. Sudakov–Verstraëte 2008: any n-vertex graph with no 2-power cycle has average degree ≤ e^{O(log\* n)}; proof works for *any* even sequence with k_{i+1} ≤ C·k_i.
- **Theorem 2.1 (Liu–Montgomery):** There is d > 0 such that *every graph with average degree at least d has a cycle whose length is a power of 2.* This answers Erdős's question affirmatively.
- The method works for a far wider class: any even sequence with k_{i+1} ≤ exp(k_i^{1/10}).
- **Conjecture 2.2 = the Erdős–Gyárfás conjecture (stated verbatim):** any graph with minimum degree at least 3 has a cycle whose length is a power of 2. Noted as likely to hold with a much smaller constant than the methods give.
- Theorem 2.3 (Liu–Montgomery): every graph with avg degree d satisfies Σ_{ℓ∈𝒞(G)} 1/ℓ ≥ (1/2 − o_d(1)) log d (confirms Gyárfás–Komlós–Szemerédi bound is tight).
- Theorem 2.4 (Liu–Montgomery): every graph with chromatic number ≥ k satisfies Σ_{ℓ∈𝒞_odd(G)} 1/ℓ ≥ (1/2 − o(1)) log k (resolves Erdős–Hajnal odd-cycle question, tight).
- Method: a sublinear expander H with large constant average degree has an interval in which 𝒞(H) contains *every even number*, long enough relative to its start to catch a power of 2.

### 3. Hamilton cycles (Chvátal toughness, Thomassen vertex-transitive, expansion-based Hamiltonian conjecture)
- Background, not relevant to E–G.

## Why it matters for this run

- Confirms in a 2025 peer-reviewed survey the exact status of the obstruction:
  the *average-degree* route (Liu–Montgomery Thm 2.1) forces a 2-power cycle as an
  interval of even lengths crosses a power of two, but only with an absolute *constant*
  average degree d ≫ 3. The Erdős–Gyárfás conjecture (Conjecture 2.2, min degree 3)
  remains open and is specifically called out as likely needing a much smaller constant.
- The phrase "interval of even lengths catches a power of 2" is the precise mechanism
  that beats the sparseness obstruction at huge average degree — the run's structural
  thread must find an analogous prescribed-length mechanism that works at min degree 3.

## Claim block

```claim
id: lm-large-avgdeg-forces-2power
statement: There is an absolute constant d > 0 such that every graph with average degree at least d contains a cycle whose length is a power of two. The proof works for any even sequence k_1<k_2<... with k_{i+1} <= exp(k_i^{1/10}).
hypotheses: finite simple graph, average degree >= d (d an absolute constant)
holds-here: yes — this is the average-degree 2-power result; does NOT apply at min degree 3 (the conjecture's hypothesis)
status: sourced (Liu–Montgomery, reported in Montgomery's 2025 EMS survey)
bearing: the strongest 2-power-specific positive result; confirms the obstruction is that d >> 3
anchor: research/sources/montgomery-cycles-and-expansion-survey.full.md
```
