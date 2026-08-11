# Recursive Inversion Models for Permutations (Meek & Meilă, NIPS 2014)

Source: https://papers.neurips.cc/paper_files/paper/2014/file/d157fbe354aeead90fe6287cbc4a04ca-Paper.pdf

## What it establishes

A probabilistic model family over permutations of a set E built **recursively by merging
subsequences** (a stochastic *merge sort*), rather than by single-element insertions (the
insertion-sort / Mallows route). Key machinery, directly on-point for the tree recursion:

- **Discrepancy matrix** D_{ij}(π,π0) = 1 if i <_π j but j <_π0 i else 0. The **inversion distance**
  d(π,π0) = Σ_{ij} D_{ij} counts pairs whose relative order differs between test π and reference π0
  (Mallows, 1957). The problem's parity is exactly d mod 2.
- A **RIM** is given by a binary tree τ over E; each internal node i carries (i_L, i_R) plus a
  parameter θ_i. The generating process recursively builds the permutation: the permutation of a
  node = (merge of the left-subsequence and right-subsequence permutations), preserving relative
  order *within* each subsequence. **All inversions arise at the merge of the two child
  subsequences of a node; no inversions cross between unrelated nodes' subtrees.**
- **Vertex discrepancy** v_i(π,π0) = number of inversions created when merging i_L and i_R at node i.
  The total inversion distance is the **sum over all internal nodes** of v_i:
  d(π,π0) = Σ_i v_i(π,π0). Likelihood is exponential: P(π|τ,θ) ∝ Π_i exp(−θ_i v_i), with a
  **tractable closed-form normalization** (the partition function factors when the per-node terms
  decouple).
- Serializes the inversion count as an **additive functional over the recursion tree**: each
  internal node contributes exactly the pairs it shuffles between its left and right ranges, and
  the two child subproblems are otherwise independent.

## What it implies for this problem

In Torpids the parity of the new order is (# bump-chain pairs i→…→j, i<j) mod 2 — the inversion
count of the permutation produced by the recursive race structure. The RIM framework is the named
counterpart of the treap recursion in [[randomized_search_trees_treaps_seidel_aragon]]: when an
interior element r splits the range into left [a,r−1] and right [r+1,b], the parity splits into

    parity(π[a,b]) = parity(π[a,r−1]) · parity(π[r+1,b]) · (−1)^{cross_{a,b}(r)}

where cross_{a,b}(r) is the number of pairs (i in left, j in right) whose relative order is flipped
at this node. The cross term is the node's vertex discrepancy v_r. Because the two child subranges
decouple (independent sub-treaps / independent sub-races), the expectation of any multiplicative
parity functional is a **sum of products of per-range factors** — the exact-integration route
memory.md demands. This is the inversion-accumulation identity, alongside the distance-ratio
weights from [[inid_exponential_order_statistics_nagaraja]] and the subrange independence from the
treap note.
