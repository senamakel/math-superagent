# Pattern-finder consolidated report — regularity and non-structure in the run's integer data

Author: pattern_finder (adversarial; every number below re-derived this run or
read from a captured artifact). Structural conclusions are **conjectures**
unless flagged `verified` (symbolically proven) or `sourced` (OEIS catalogue).

## What survived independent re-derivation this run

### 1. The Mycielski family is the ONLY clean sequence structure — and it is proven, not fit

The Groetzsch chain (Mycielski iterates of C5), k = 1..8:

- **Vertex counts** `V_k`: `5, 11, 23, 47, 95, 191, 383, 767, 1535, 3071`
  = **`3*2^k - 1`** (A083329/A055010/A153893/A052940; `sourced`).
  Satisfies `V_{k+1} = 2 V_k + 1` and the order-2 recurrence `a(n)=3a(n-1)-2a(n-2)`
  (the `find_linear_recurrence` tool verified this exactly over all 10 terms).
- **Edge counts** `E_k`: `5, 20, 71, 236, 755, 2360, 7271, 22196, 67355, 203600`
  = **`(1 - 6*2^k + 7*3^k)/2`** (A122695, "edges in n-th Mycielski graph"; `sourced`).
  `analyze_sequence` shows non-polynomial; `find_linear_recurrence` verified the
  **exact order-3 recurrence `E_k = 6E_{k-1} - 11E_{k-2} + 6E_{k-3}`** (roots 1,2,3)
  over all 10 terms.

This run re-proved both closed forms symbolically with sympy from the
construction recurrences `V_{k+1}=2V_k+1`, `E_{k+1}=3E_k+V_k`:
both forms give identically 0 when substituted into the recurrences, and match
the OEIS forms. So these are **`verified`** by two independent routes
(construction-recurrence derivation + OEIS catalogue), not merely fit.

**But the family is a confirmed dead end for the plane-bound goal.** Mycielski
2-iterates onward contain an explicit K2,3, and the certified lemma
`sharp-nbhd-local` proves every unit-distance graph is K2,3-free. So
`M^k(C5)`, k>=2, are abstract 5-chromatic graphs that carry no plane colouring
information. (Independent re-check this run: M^2 has V=11 E=20, M^3 has V=23
E=71; M^2, M^3, M^4 all K2,3-free=False.)

### 2. The kernel-census counts have NO exploitable sequence structure (confirmed)

The class any 5-chromatic unit-distance graph must lie in:
graph on N vertices with min-degree>=4, K4-free, K2,3-free, nbhd-maxdeg<=2.

| n | kernel members | 4-chromatic | 3-colourable |
|---|----------------|-------------|--------------|
| 8 | 1 | 1 | 0 |
| 9 | 4 | 1 | 3 |
| 10 | 16 | 16 | 0 |
| 11 | 228 | 198 | 30 |

- kernel `[1,4,16,228]`: geometric head 4^0,4^1,4^2, then break at 228 (ratio
  14.25); not polynomial, **no** constant-coefficient recurrence of order<=3;
  `[1,4,16,228]` **not catalogued**.
- 4-chromatic `[1,1,16,198]`: no structure; an order-2 fit over 4 terms is an
  overfit, not a regularity.
- 3-colourable `[0,3,0,30]`: only trivial divisibility-by-3.

Only the n=12 count could decide a recurrence, and that enumeration is
infeasible (~100M+ graphs). **No defensible formula route exists.** This matches
three prior agent reports; all five times the tools have been exact over the
terms supplied and deleted no real regularity.

### 3. Structural (non-numeric) regularities that ARE load-bearing

- **The size-bound theorem** (verified, `checked`): every unit-distance graph on
  <= 11 vertices is 4-colourable; every 5-chromatic UDG has >= 12 vertices.
  Three machine-checked steps: sharp-critical-degree, sharp-nbhd-local
  (geometric kernel: K4-free, K2,3-free, nbhd-maxdeg<=2), and the complete C_11
  census (all 228 members 4-colourable by two independent oracles). This is the
  run's strongest result and it is already durable memory.
- **Moser-core dominance** (conjecture from data, complete over ALL existing
  terms but with no out-of-sample term): 67 of 198 n=11 4-chromatic kernel
  members (33.8%) have a minimal 4-critical core isomorphic to the 7-vertex
  11-edge Moser spindle; 118/198 contain a Moser subgraph somewhere. All terms
  that exist are used, so this cannot be tested further without the (infeasible)
  n=12 census. Keep it a conjecture.

### 4. Negative enumerations that stay negative (confirmed)

- Forced-pair under 4 colours: none in Moser (10 pairs) or Moser+Moser (256
  pairs); diamond tips forced equal only under 3 colours.
- Hoffman spectral bound on the constructible family peaks at 2.995 on the
  triangular disk radius-3 (37 pts), below 4: the spectral relaxation cannot
  certify chi>=5 on any built graph.
- Edge-count distribution of the 198 n=11 4-chromatic members:
  edges 22:15, 23:112, 24:62, 25:9 — matches the load-bearing minimum (a
  5-critical graph on 11 vertices with min-deg>=4 has >=22 edges), no further
  pattern.

## Verdict

**The only exact, proven regularity in the run's integer data is the Mycielski
closed-form pair V_k = 3·2^k − 1, E_k = (1 − 6·2^k + 7·3^k)/2 — and it drives a
family that is provably not plane-realizable.** The census counts that actually
govern the size-bound theorem contain no exploitable sequence structure; the
tools delete every candidate. The load-bearing content is not a number sequence
but the verified structural facts: the geometric kernel (K2,3-free etc.) and the
size-bound through N=11. Anyone hunting a formula in 1,4,16,228 should stop; the
next move is structural (forced-pair over richer bases), not numerical.
