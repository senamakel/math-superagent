# PE 597 (Torpids) — Structure report: worked-example verification + bump-graph taxonomy

Companion program: `code/structure_taxonomy.py`. The reference engine is
`code/brute.py` (full-reachability `above`), wrapped by
`code/toolkits/race_events.py` and `code/toolkits/race_outcome.py`.

---

## 1. Worked-example reproduction (n = 3, L = 160)

Using one Exp(1)-distributed speed vector per row that produces that exact
chronological edge set, the brute engine reproduces all five rows:

| Bumps (edges) | New order | Parity | Listed probability | Engine |
|---|---|---|---|---|
| none `[]` | A,B,C | **even** | 4/15 | even ✔ |
| B bumps C `[(1,2)]` | A,C,B | **odd** | 8/45 | odd ✔ |
| A bumps B `[(0,1)]` | B,A,C | **odd** | 1/3 | odd ✔ |
| B bumps C then A bumps C `[(1,2),(0,2)]` | C,A,B | **even** | 4/27 | even ✔ |
| A bumps B then B bumps C `[(0,1),(1,2)]` | C,B,A | **odd** | 2/27 | odd ✔ |

Exact rational checks:
- Sum of **all five** row probabilities = `4/15 + 8/45 + 1/3 + 4/27 + 2/27 = 1`
  (verified exactly — the rows form a proper partition of the sample space).
- Sum of the two **even** rows = `4/15 + 4/27 = 56/135 = 0.4148148148…`, exactly
  the stated `p(3,160)`. ✔

## 2. p(4,400) Monte-Carlo check

`MC p(4,400) = 0.511487 ± 0.000790` (400,000 trials). Given value is
`0.5107843137`; the estimate agrees within ~0.9 SE. Consistent with the
verified engine.

---

## 3. Bump-graph taxonomy (MC, 60,000 trials per (n,L), n=3,4,5, L∈{160,1800})

The bump directed graph has vertices = boats, edges = `(bumper, bumped)` for
every chronological bump; a bumped boat keeps rowing and can be re-bumped, so
a boat may be the **target** of several edges — but each boat **bumps at most
once** (it stops) and the edge always points to a strictly higher index.

### 3.1 The bump graph is ALWAYS a forest (the central finding)
Across **all 360,000 trials** (every n,L config):
- **Out-degree ≤ 1 for every boat** (out-degree>1 observed count = 0/360k).
- **Every edge is strictly index-increasing** (non-increasing edges = 0).
- **Zero cycles** detected.
Therefore every bump graph is a **directed forest whose edges point to higher
indices**. Deterministic consequences (proved, not just observed):
- Boat `0` is **never** a target (nothing behind it) and boat `n−1` **never
  bumps** anyone (nothing ahead); both confirmed P = 0 over 100k trials.
- A forest on n nodes has `n − (#edges)` components; each component is an
  **in-arborescence** rooted at a boat that never bumps (a "finisher").
- Max bump-chain length reaches `n−1` (the chain `0→1→…→n−1`), confirmed.

### 3.2 Degree statistics
- **Out-degree:** essentially always exactly 1 for the n−1 lower boats that
  bump; the histogram is concentrated at 1 (only boats that never bump have
  out-degree 0). `outdeg>1` never occurs.
- **In-degree:** a boat can be bumped many times (in-degree up to 3–4 at n=5).
  At n=5, L=1800 the max in-degree histogram shows values {1,2,3,4} — the
  highest (least downstream) boats are the most-bumped targets, since every
  upstream chain eventually lands on whoever is ahead. Boat `n−1` is bumped
  with prob ≈ 0.45–0.49.

### 3.3 Geometry
- **Chain reachability** (`above`) is *not* simply consecutive-index: the set
  of boats bumping a given target need **not** be a consecutive lower-index
  block (≈1–3% of node-rows at n=5/6), and the set of non-bumping roots is
  frequently non-consecutive. `above[i]` can skip intermediate boats (a boat
  may pass a boat that has already stopped/OUT).
- The number of **distinct edge structures** reached grows with n: 5 (n=3),
  14 (n=4), 14–42 (n=5). The edge-set and `above`-reachability representations
  give the **same count** (bijective on the observed data).
- All observable structures are **forests** (matching §3.1).

### 3.4 Typical structures & that parity ≠ treap-ancestry
The dominant structures at n=5,L=1800 include `[(0,2),(1,2),(3,4)]`,
`[(0,3),(1,3),(2,3)]`, `[(0,1),(1,3),(2,3)]`, `[(0,1),(2,4),(3,4)]`,
`[(0,1),(1,4),(2,4),(3,4)]`. Note the independent forest components: a single
race can have several disjoint bump trees (e.g. `[(0,1)]` and `[(2,3)]`
simultaneously). These components reduce to independent index sub-ranges — the
parity then factors as a product over components, matching the `#chain-pairs
mod 2` identity. This is the structural reason the treap/one-scalar-priority
hypotheses FAIL (see MEMORY.md): bumping is a chronological, forest-of-chains
process, not a single-root Cartesian-tree ancestor relation.

---

## 4. Key structural conclusions (for the exact solver)

1. **Every bump graph is a directed forest with edges strictly index-increasing**
   (out-degree ≤ 1, no cycles) — so the object under study is always a forest
   of in-arborescences, never a general DAG with shared/downstream edges.
2. Parity = `#(chain-pairs i→…→j, i<j) mod 2` = inversion count of the new
   order, verified on every observed pattern via the forest reachability.
3. A bumped boat keeps rowing and may be re-bumped by several boats, so
   in-degree is unbounded (≤ n−1) while out-degree is ≤ 1; targets concentrate
   on the highest boats.
4. Forest components act on **disjoint index intervals** and are structurally
   independent — a productive route to decompose `p(n,L)` into per-component
   probabilities if the chronological race within a component has a closed
   form.
5. Reservoir finding: the race parity depends on **speed magnitudes and the
   chronological bump/finish interleaving**, not on a single scalar rank
   (w-order hypothesis refuted; see MEMORY.md).

## 5. Verification status
- n=3,L=160 five-row table: **PASS** (parities + exact rational sums 1 and 56/135).
- p(4,400): **PASS** within MC error (0.5115 ± 0.0008 vs 0.5108).
- Forest/degree/cycle invariants: confirmed exact (zero violations) over 360k trials.
