# Eccles, "A Stability Result for the Union-Closed Size Problem" (2015)

**Source URL:** https://arxiv.org/pdf/1210.2044 (downloaded; full text at
`research/sources/eccles-stability-result-2015.full.md`)

## What it is
Tom Eccles (Combinatorics, Probability & Computing 24(5), 2015; arXiv Dec 2012).
A stability result for the union-closed **size problem**: determine the maximum
average set size f(m) of a union-closed family of m subsets of [n], a problem
Balla–Bollobás–Eccles solved exactly.

## What it establishes
- The three-line source (Karpas 2017, already in library) pins the large-family
  progression precisely:
  - **Czédli**: UC holds if |F| ≥ 2^n − 2^{n/2}
  - **Balla–Bollobás–Eccles (2012)**: UC holds if |F| ≥ 2^{(3/2)n}
  - **Eccles (2015)**: improved to |F| ≥ (2/3 − 1/104)·2^n
  - **Karpas (2017)**: |F| ≥ 2^{n−1} (Boolean analysis)
- Eccles Corollary 1.4: UC holds for all UC families A ⊆ P([n]) with
  |A| ≥ 2^{n(2/3 − c₂)} for some c₂ > 0.
- Near-extremal union-closed families cluster around an extremal form
  (stability), which is the structural content.

## Why it matters to this run
- It is the **large-family regime** canon: the exact threshold progression for
  when UC holds by counting/compression. This is one of the restricted classes
  "already settled" that phase 1 must pin with hypotheses.
- The stability structure of near-extremal families feeds the minimal-
  counterexample programme: a counterexample must be *far* from these extremal
  shapes.

## Status
Sourced (arXiv 2012 / CP&C 2015). Claims are theorems in the source; not
re-verified computationally here.

```claim
id: eccles-stability
statement: Stability result for the union-closed size problem: near-extremal union-closed families (max average size) cluster around an explicit extremal form (Eccles Cor 1.4: UC holds for any UC A⊆P([n]) with |A| ≥ 2^{n(2/3−c₂)} for some c₂>0). Part of the large-family threshold progression Czédli 2^n−2^{n/2} → BBE 2^{3n/2} → Eccles (2/3−1/104)2^n → Karpas 2^{n−1}.
hypotheses: union-closed A⊆P([n]); |A| above the stated threshold
holds-here: yes (large-family settled class; Karpas 2^{n−1} is the best threshold in this progression)
status: asserted (theorems in the source; not re-checked here)
bearing: a counterexample must be FAR from these extremal shapes; the stability structure feeds the minimal-counterexample programme.
anchor: research/sources/eccles-stability-result-2015.full.md
```

## Bearing
The large-family regime is fully settled up to Karpas's |F| ≥ 2^{n−1}; this note
records the threshold progression so the run does not re-derive it.
