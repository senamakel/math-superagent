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
  one ≥ 30. Markström found four 24-vertex graphs whose only 2-power cycle has length 16,
  one planar — the closest known near-counterexamples. → [[L2.0/L1.0]]
- **Restricted classes closed (never re-derive):** P13/P10/P8-free, 3-connected cubic
  planar, claw-free planar, K_{1,m}-free (with stated degree constraints), diameter-2,
  large average degree. → [[L2.0/L1.0]]
- **Density bound:** a counterexample is *sparse* — avg degree ≤ exp(O(log* n)) (powers
  of two are an exponentially-bounded even sequence; Sudakov–Verstraëte). With δ≥3,
  density sits between 3 and exp(O(log* n)). → [[L2.0/L1.0]]

## The obstruction every attack must beat

An interval of cycle lengths forces a power of two only when the interval spans a factor of
two (b ≥ 2a). Liu–Montgomery's large even-length interval settles only large-average-degree
for exactly this reason. → [[L2.0/L1.0]]

## Neighbouring machinery (arriving next)

The admissible-cycle / mod-k / consecutive-length toolkit from Dean, Gao–Huo–Liu–Ma, and
the trigonal–tetragonal framework (batch `L1.1`, not yet sealed). These are the tools that
could turn the sparse, predominantly-cubic structure above into a power-of-two cycle.

## Originals and seals

- `L0.0/` ↔ `L0.1/` are the full texts.
- `L1.0/` digest batch, sealed by `[[L2.0/L1.0]]`.
- `L1.1/` digest batch, not yet sealed.
- `L1.2/` holds the seal of `L0.0` and a single OEIS note.
