# research — what this now establishes

The top of this tree. Everything below is reached from here; sealed batches of originals
in `L0.<n>/`, one note per sealed batch a level up, and so on. Full claim-by-claim ledger:
`CLAIMS.md`; direction of attack: `THREADS.md`.

## The target (sealed)

The Erdős–Gyárfás conjecture: every *finite* simple graph with min degree ≥ 3 has a simple
cycle of length 2^k, k ≥ 2 — i.e. length in {4, 8, 16, …}. Finiteness is essential (an
infinite min-degree-3 tree is a trivial counterexample). Mid-1990s conjecture (sources say
1993–96); Erdős offered $100 / $50. The proposers themselves believed it *false*; that
stronger belief (a counterexample at every min degree) was disproved by Liu–Montgomery.
→ [[L2.0/L1.0]]

## Structure of a minimal counterexample (sealed)

A minimal counterexample G (min order *and* size, δ≥3, no 2-power cycle) is
**predominantly cubic**: every proper subgraph has a vertex of degree ≤2; regular ⇒ cubic;
at least 4/7 of vertices have degree exactly 3; every vertex is adjacent to a degree-3
vertex. → [[L2.0/L1.0]]

## What the run can rely on (sourced, sealed)

- **Verification bound / oracle anchor:** any counterexample has ≥ 17 vertices; any cubic
  one ≥ 30. Markström's exhaustive search found four 24-vertex graphs whose only 2-power
  cycle is length 16, one planar — the closest known near-counterexamples. → [[L2.0/L1.0]]
- **Restricted classes closed (never re-derive):** P13/P10/P8-free, 3-connected cubic
  planar, diameter-2, claw-free planar, K_{1,m}-free, Cayley families (quaternion,
  dihedral, semidihedral, order-p^3; abstract only), large average degree. → [[L2.0/L1.1]]
- **Density bound:** a counterexample is *sparse* — avg degree ≤ exp(O(log* n)) (powers
  of two are an exponentially-bounded even sequence; Sudakov–Verstraëte). With δ≥3,
  density sits between 3 and exp(O(log* n)). → [[L2.0/L1.0]]

## The obstruction every attack must beat

An interval of cycle lengths forces a power of two only when the interval spans a factor of
two (b ≥ 2a). Liu–Montgomery's large even-length interval settles only large-average-degree
for exactly this reason — the guaranteed even interval [log⁸ℓ, ℓ] is wide only at enormous
average degree. → [[L2.0/L1.0|L1.0]] [[L2.0/L1.1|L1.1]]

## The only unconditional guarantee at δ=3 (sealed)

Every δ≥3 graph has **two admissible cycles** — lengths 1 or 2 apart (min degree k+1 ⇒ k
admissible cycles at k=2, Gao–Huo–Liu–Ma) and **two cycles of consecutive length** (Gao–Ma
Bondy–Vince k=0 case). This is the *only* non-density length guarantee at the conjecture's
degree; it is a gap, still between consecutive 2-powers, so it does not close EG on its own.
The regimes that do close classes (diameter-2, P10-free) do so by forcing C4/C8 outright.
→ [[L2.0/L1.1]]

## Originals and seals

- `L0.0/` ↔ `L0.1/` are the full texts.
- `L1.0/` digest batch, sealed by `[[L2.0/L1.0]]`.
- `L1.1/` digest batch, sealed by `[[L2.0/L1.1]]`.
- `L1.2/` holds the seal of `L0.0` and a single OEIS note.
