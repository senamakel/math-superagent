# Di Braccio–Katsamaktsis–Ma–Malekshahian–Zhao, "Leaf-to-leaf paths and cycles in degree-critical graphs"

**Source:** Francesco Di Braccio, Kyriakos Katsamaktsis, Jie Ma, Alexandru Malekshahian, Ziyuan Zhao, *Leaf-to-leaf paths and cycles in degree-critical graphs*, arXiv:2504.11656v2 (also published in Combinatorica 46 (2026) art. 11, open access). Full text on disk: `research/sources/dibraccio-katsamaktsis-ma-degree-critical.full.md` (from the arXiv HTML).

## What the source establishes

Follow-up to Narins–Pokrovskiy–Szabó (NPS). Degree-3-critical = $n$ vertices,
$2n-2$ edges, no proper induced subgraph with minimum degree 3. NPS's tree
correspondence reduced cycle-length questions in the graphs $G(T)$ (built from
even 1-3 trees $T$) to leaf-to-leaf path lengths in $T$; they posed
Conjectures 6.2–6.4 about how many distinct leaf-to-leaf path lengths a 1-3
tree must have. This paper resolves those conjectures up to constant factors:

**Theorem 1.** Every $n$-vertex degree-3-critical graph has $\Omega(\log n)$
distinct cycle lengths. (Resolves NPS Conjecture 6.2 up to constant factor —
NPS's Bollobás–Brightwell construction gives $O(\log n)$, so the bound is
tight in order of magnitude.)

**Theorem 2.** Every tree with maximum degree $\Delta \ge 3$ and $\ell$ leaves
has at least $\log_{\Delta-1}((\Delta-2)\ell)$ distinct leaf-to-leaf path
lengths. For $\Delta = 3$ and a 1-3 tree with $n$ vertices ($\ell =
(n+2)/2$ leaves): at least $\log_2(n/2)$ distinct path lengths — resolves NPS
Conjecture 6.3 in order of magnitude.

**Theorem 3/4.** There exist arbitrarily large 1-3 trees with only
$O(N^{0.91})$ distinct leaf-to-leaf path lengths below $N$, and conversely
every 1-3 tree with at least $2^N$ vertices has $\Omega(N^{2/3})$ distinct
leaf-to-leaf path lengths below $N$. (Resolves NPS Conjecture 6.4 in both
directions up to constants.)

**Theorem 5.** Generalizes Theorem 1 to $k$-critical graphs ($m = (1 +
\tfrac1{k-1})n - O(1)$-ish edge counts; the $k=3$ case is Theorem 1).

## Why it matters for this problem

- The power-of-two question over the $G(T)$ family is exactly a question
  about *short* leaf-to-leaf path lengths: cycles of length $2^k$ in $G(T)$
  correspond to leaf-to-leaf paths of length $2^k - 2$ (odd $2^k$) or two
  disjoint paths summing to $2^k - 4$ (even $2^k$). In 1-3 trees the *small*
  leaf-to-leaf lengths are what determines whether small 2-power cycles
  (4, 8, 16) exist. This paper pins the frontier of what is known about how
  many distinct *small* leaf-to-leaf lengths a 1-3 tree must have:
  - below $N$: $O(N^{0.91})$ achievable, and every large 1-3 tree has many
    small ones ($\Omega(N^{2/3})$ up to $2^N$ vertices). These are
    order-of-magnitude statements; the *specific* lengths (is 4, 8, 16, 32
    present?) are not decided by them.
- Theorems 1–2 give the state of the art for "how many cycle lengths" in the
  degree-3-critical class; the EG conjecture's obstruction (a *specific* sparse
  length) is one step past what any of these results pin down.
- The methods (additive structure, Erdős–Szekeres, Dilworth) are the modern
  toolkit for the leaf-to-leaf path question that any 1-3-tree-based
  construction of an EG near-counterexample must go through.

## Caveats

- Same as NPS: the class is "no proper induced δ≥3 subgraph with exactly
  $2n-2$ edges"; a minimal EG counterexample is not known to have $2n-2$
  edges. All four theorems are about the degree-3-critical class, not about
  the EG-minimal-counterexample class directly.

```claim
id: EG-DKMZ-critical-log-distinct-lengths
statement: Every n-vertex degree-3-critical graph has Ω(log n) distinct cycle lengths (best possible in order: Bollobás–Brightwell's construction has O(log n)); and every tree with max degree Δ≥3 and ℓ leaves has at least log_{Δ−1}((Δ−2)ℓ) distinct leaf-to-leaf path lengths.
hypotheses: degree-3-critical = n vertices, 2n−2 edges, no proper induced δ≥3 subgraph; trees with Δ≥3, ℓ leaves
holds-here: no — class mismatch (edge count 2n−2 not implied for a minimal EG counterexample); the leaf-to-leaf tree theorems hold for all such trees and would apply to any 1-3-tree-based construction
status: proved
bearing: sets the current quantitative frontier for "many cycle lengths" in the near-minimal class; the EG obstruction (a specific sparse length) is strictly finer than a count lower bound
anchor: research/summaries/dibraccio-katsamaktsis-ma-degree-critical.md
```

```claim
id: EG-DKMZ-short-leaf-lengths
statement: There exist arbitrarily large 1-3 trees with O(N^{0.91}) distinct leaf-to-leaf path lengths below N, and every 1-3 tree on at least 2^N vertices has Ω(N^{2/3}) distinct leaf-to-leaf path lengths below N (NPS Conjecture 6.4 resolved both directions).
hypotheses: 1-3 trees (degrees 1 and 3 only)
holds-here: yes — any tree-based EG construction lives in this class; the bounds quantify what "few short leaf-to-leaf lengths" can mean
status: proved
bearing: a would-be EG counterexample built as G(T) with T a 1-3 tree must have T avoid the specific leaf-to-leaf lengths 2^k−2; these results say the *number* of short lengths is large in every sufficiently big tree, but do not decide individual lengths — that is the open core the run would attack
anchor: research/summaries/dibraccio-katsamaktsis-ma-degree-critical.md
```