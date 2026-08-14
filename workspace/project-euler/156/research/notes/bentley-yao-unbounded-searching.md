# Bentley–Yao, "An Almost Optimal Algorithm for Unbounded Searching"

On disk: `research/sources/bentley-yao-unbounded-searching.full.md`, hosted PDF of Information Processing Letters 5(3) (1976) 82-87, DOI 10.1016/0020-0190(76)90071-5. Downloaded from the Oxford-hosted copy surfaced by search: http://spivey.oriel.ox.ac.uk/wiki/images/0/05/Expsearch.pdf

## Why this run needs it

Khovanova & Marton's §7 search for the "greater-or-equal" sequences uses "a variation of unbounded binary search [Bentley-Yao]" with a "safeleft range" whose size doubles when the right end still satisfies f_d(x+p) < x and halves otherwise. Bentley–Yao is the classical analysis that such a strategy is near-optimal in the number of function evaluations when the target position is unbounded. In PE156 the target set is bounded by d·10^10, but the same doubling/halving iterator is the efficient engine; this source justifies its near-optimality.

## What it establishes

For a function F known to change behavior at a unique point in an unbounded ordered domain, the paper:
- formalizes unbounded searching as searching an ordered table of infinite size;
- gives Algorithm B (bounded binary search): double a probe until it passes the target, then binary-search between the last two probes; cost ≈ 2·lg n + 1 evaluations of F;
- gives Algorithm R: refine the first (doubling) stage so the total is closer to the lower bound;
- proves a lower bound showing the algorithm is very nearly optimal in the number of comparisons (the decision-tree phase interpretation: each evaluation is a node, outcomes are branches).

The gap-lemma the run uses — "if a≥(d) > x and f_d(y) < x then a≥(d) > y" (Khovanova–Marton Lemma 7.1, on disk) — is exactly the monotonicity fact that lets such a search skip the interval [x, y] safely; Bentley–Yao supplies the framework in which the skip schedule is near-optimal.

```claim
id: bentley-yao-unbounded-search
statement: Unbounded searching (locating the unique change-point of a monotone predicate on an unbounded ordered domain) can be done with about 2·lg n + 1 predicate evaluations via a doubling probe followed by binary search, and this is within a small constant of optimal (lower bound proved in the paper).
hypotheses: predicate is monotone; one change-point; cost = number of evaluations.
holds-here: holds. f(n,d) − n is not monotone in n (it dips), so the run does not use plain binary search on the whole range; instead the Khovanova–Marton safeleft-range iterator (Lemma 7.1 on disk) uses doubling/halving with the same near-optimality rationale.
status: sourced (Bentley & Yao, IPL 5(3) 1976, full text on disk)
bearing: justifies the efficiency of the skip-search engine that enumerates fixed points; complementary to the bound (Prop 9.1) that makes the search finite.
anchor: research/sources/bentley-yao-unbounded-searching.full.md
```