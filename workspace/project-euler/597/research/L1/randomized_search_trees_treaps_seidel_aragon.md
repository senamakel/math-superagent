# Randomized search trees (treaps) — Seidel & Aragon

<!-- source: https://faculty.washington.edu/aragon/pubs/rst96.pdf | Seidel & Aragon, "Randomized Search Trees", Algorithmica 16(4/5):464-497 (1996); extended from Aragon & Seidel FOCS 1989 -->
Full text: `research/L0/seidel_aragon_randomized_search_trees.full.full.md`

## What the source establishes

A **treap** (randomized search tree) on a set of items, each with a **key** (totally
ordered, here the boat coordinate/rank) and a **priority** (totally ordered), is a
binary tree that is in **in-order** by keys and in **heap-order** by priorities
(parent's priority = max/min of subtree). With distinct keys and priorities the treap
is **unique**: the item of extremal priority is the **root**, and the left/right
subtrees are the treaps of the key sets to its left/right. (Sec: unique for distinct
keys and priorities.)

**Random-priority treap (random BST):** if the priorities are i.i.d. continuous random
variables independent of the keys, then the root is the extremal-priority item at a
**uniform** rank, and the two subtrees are **independent** random treaps of their
sizes. That is, the treap's shape is a random binary search tree: the recursive
decomposition at the root (min-priority item) yields left and right subtrees that are
independent, identically distributed copies. This is the classic observation (also
Gabow et al. via the Cartesian tree) that underlies optimal expected operation time.

## Why this closes the PE 597 gap

The run's exact recursion conditions on the boat "slowest relative to a target t"
(relative speed Exp with rate = distance, per
[[inid_exponential_order_statistics_nagaraja]]) and recurses **independently on the
two subranges** left and right of that boat. That is precisely the treap/Cartesian-tree
decomposition: root = min-priority (slowest) boat, left/right subtrees independent.
Seidel & Aragon give the named, proven statement that such a recursive split into
independent subtrees is valid when priorities are i.i.d. — here the i.i.d. Exp(1)
speeds provide those priorities. It (a) names the structure the recursion builds, and
(b) confirms the subrange recursions are independent, so p(n,L) is a sum of products
over the two sides (no cross-range coupling). Combined with the exponential/
Laplace/order-statistics notes it supplies the independence justification the exact
integration needs.
