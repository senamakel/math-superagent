# Verstraëte, "On Arithmetic Progressions of Cycle Lengths in Graphs" (2000)

**Source:** Jacques Verstraëte, *On Arithmetic Progressions of Cycle Lengths in Graphs*, Combinatorics, Probability and Computing 9 (2000) 369–373 (Cambridge). arXiv:math/0204222 (2002 posting of a 1999 manuscript). Full text on disk: `research/sources/verstraete-arithmetic-progressions-cycle-lengths.full.md`.

## What the source establishes

The tight degree threshold for forcing an *arithmetic progression* of cycle
lengths — the "progressions, not prescribed lengths" boundary of the cycle
machinery, directly relevant to the obstruction paragraph in problem.md.

- **Theorem 1.** Let $k \ge 2$ and $G$ a bipartite graph of average degree at
  least $4k$ and girth $g$. Then $G$ contains cycles of $(g/2 - 1)k$
  consecutive even lengths; the shortest has length at most twice the radius
  of $G$.
- **Corollary 4.** General graphs: average degree at least $8k$ and even girth
  $g$ gives $(g/2 - 1)k$ consecutive even cycle lengths.
- **Theorem 5.** Average degree at least $6k$ and girth $g$: for some odd
  $r \ge 3$, cycles of *all even or all odd* lengths in the interval
  $[r, r + (g-2)k]$.
- **Corollary 6.** Chromatic number at least $2k+2$ and girth $g$ gives
  $k(g-2)$ consecutive cycle lengths.
- Answers the Häggkvist–Scott question: minimum degree linear in $k$ suffices
  (they had $\ge 300k^2$).
- **Theorem 9 / Corollary 10.** Bipartite graphs of size at least
  $4\lceil 2(k-1)/(g-2)\rceil n^{1+1/k}$ contain a cycle of length $2k$, and
  size at least $8(k-1)n^{1+1/k}$ forces a cycle of length $2k$ — slight
  improvements over Bondy–Simonovits.

**The core lemma (Lemma 2).** If $H$ is a cycle with a chord and $(A,B)$ a
nontrivial vertex partition, then $H$ contains $A$–$B$ paths of every length
$< |H|$, unless $H$ is bipartite with bipartition $(A,B)$. This is the
"many lengths from one cycled-with-chord structure" engine: one chorded cycle
in the right place generates every intermediate path length, and each even
path length closes to a distinct cycle length. This is *exactly* the 
progressions machinery that problem.md says cannot force a prescribed sparse
length: the lengths produced are all in an interval of size $(g-2)k$, and to
force a power of two the interval must span a gap between consecutive powers,
which needs $(g-2)k \ge 2^j$ for the largest power below — impossible at
bounded degree/girth.

## Why it matters for this problem

- Together with Bondy–Vince (also on disk), this fixes the state of the art on
  "δ≥3 or large average degree forces *which* cycle lengths": at most
  *consecutive/progression* lengths in an interval, never a prescribed sparse
  length. The EG conjecture is the one case where the target set (powers of
  two) is sparse, which is why none of these theorems touch it.
- The chorded-cycle lemma (Lemma 2) is genuinely usable in the run's own
  attack: if a minimal counterexample contains a chorded cycle, the lemma
  forces many cycle lengths from one structure — possibly a route to show a
  minimal counterexample must be chordless in a strong sense (every cycle is
  induced), a structural statement the library does not yet hold.
- The parity/even-girth machinery explains why 2-power cycles (even lengths)
  are the natural target: even cycle lengths are what the interval results can
  deliver in bulk; the failure is only that the interval is too short.

```claim
id: EG-verstraete-AP-cycle-lengths
statement: A bipartite graph of average degree ≥4k and girth g has cycles of (g/2−1)k consecutive even lengths (shortest ≤ 2·radius); general graphs with average degree ≥8k and even girth g have (g/2−1)k consecutive even lengths. (Verstraëte 2000, answering Häggkvist–Scott)
hypotheses: finite simple graph; average degree (not minimum); girth g; k≥2
holds-here: no — average degree ≫ 3 and the conclusion is an interval of lengths, not a prescribed power of two
status: proved
bearing: makes precise why the EG conjecture is hard: the strongest cycle-length theorems give progressions/intervals whose length scales with degree×girth, and forcing a power of two needs an interval spanning the gap between consecutive powers, unavailable at bounded degree
anchor: research/summaries/verstraete-arithmetic-progressions-cycle-lengths.md
```

```claim
id: EG-verstraete-chorded-cycle-lemma
statement: If H is a cycle with one chord and (A,B) a nontrivial partition, then H has A–B paths of every length < |H|, unless H is bipartite with bipartition (A,B). (Verstraëte Lemma 2; implicit in Bondy–Simonovits)
hypotheses: H = cycle + chord; (A,B) nontrivial partition
holds-here: yes — a self-contained structural tool; applies to any subgraph of a minimal counterexample that happens to contain a chorded cycle
status: proved
bearing: candidate engine for the run's structural argument: a chorded cycle in a minimal counterexample would generate an entire interval of cycle lengths, so a counterexample must be strongly chordless (every cycle induced) — a testable structural claim
anchor: research/summaries/verstraete-arithmetic-progressions-cycle-lengths.md
```