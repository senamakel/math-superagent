# Fox–Pach–Sudakov–Suk, "Erdős–Szekeres-type theorems for monotone paths and convex bodies"

<!-- source: https://arxiv.org/abs/1105.2097 (arXiv 1105.2097; PLMS (3) 105 (2012) 953–982, DOI 10.1112/plms/pds018) | full text at
     research/sources/fox-pach-sudakov-suk - ES-type theorems for monotone paths and convex bodies - PLMS 2012.full.md -->

**Publication.** J. Fox, J. Pach, B. Sudakov, A. Suk, *Proc. London Math. Soc.* (3) 105 (2012)
953–982. arXiv:1105.2097.

## The ordered-3-uniform-hypergraph reformulation (the backbone of the SAT route)

Define $N_k(q,n)$ = the least $N$ such that every $q$-coloring of the $k$-element subsets of
$[N] = \{1,\dots,N\}$ contains a **monochromatic monotone path of length $n$** — a chain of
$k$-tuples $(j_i, j_{i+1}, \dots, j_{i+k-1})$ for $i = 1,\dots, n-k+1$.

**The two classical values (from Erdős–Szekeres 1935):**
- $N_2(q,n) = (n-1)^q + 1$ (monotone subsequence theorem);
- $N_3(2,n) = \binom{2n-4}{n-2} + 1$ — **this is exactly the ES cups-and-caps bound**
  $\mathrm{ES}(n) \le f(n,n) = \binom{2n-4}{n-2}+1$.

So the cups-and-caps upper bound is precisely a statement about red/blue colorings of the
ordered complete 3-uniform hypergraph, where red = cap and blue = cup (equivalently
clockwise/counterclockwise orientation of each triple). This is the reformulation that
Balko–Valtr, Scheucher, and Dumitru encode with triple-orientation variables.

## What the paper proves

- $2^{(n/q)^{q-1}} \le N_3(q,n) \le 2^{n^{q-1}\log n}$, for $q\ge 2$, $n\ge q+2$.
- Stepping-up (Erdős–Hajnal) gives analogous bounds for $N_k(q,n)$, $k>3$, which are towers of
  height $k-1$ in $n^{q-1}$.
- Geometric application: an extension of the Happy Ending theorem to **plane convex bodies in
  general position** — every family of at least $M(n) = 2^{n^2\log n}$ noncrossing convex bodies
  contains $n$ members in convex position.

## Why it matters for this problem

This is the primary statement of the reformulation the run's computational arm depends on:
the cups-and-caps theorem — the very theorem the conjecture sharpens — is literally
$N_3(2,n) = \binom{2n-4}{n-2}+1$ for monotone paths in an ordered 3-uniform hypergraph. It fixes
the vocabulary (monotone path, cap/cup = red/blue) and confirms that a SAT encoding must work
over orientation variables, exactly as GOAL.md/context prescribe. It does NOT by itself bear on
the exact constant of the conjecture (it gives the $4^{n}/\sqrt n$-order bound, not $2^{n}$).

## claim block

```claim
id: cups-caps-is-N3-monotone-path
statement: ES(n) ≤ f(n,n) = C(2n-4,n-2)+1 is exactly N_3(2,n) = C(2n-4,n-2)+1, the ordered-3-uniform-hypergraph monotone-path Ramsey value; the Erdős–Szekeres cups-and-caps theorem is the statement that every red/blue coloring of the 3-subsets of [N], N ≥ C(2n-4,n-2)+1, contains a monochromatic monotone path of length n (cap=red, cup=blue by orientation).
hypotheses: planar point sets in general position, ordered by x-coordinate; red/blue on triples by orientation.
holds-here: true — this is the exact encoding the run's SAT/CP-SAT arm must reproduce and is the existing best exact-form upper bound.
status: proved (Erdős–Szekeres 1935; reformulation in Fox–Pach–Sudakov–Suk 2012).
bearing: fixes the SAT formulation (orientation variables = red/blue), provides the theoretical framing for the computational route, and supplies the upper-bound bound being sharpened.
anchor: research/sources/fox-pach-sudakov-suk - ES-type theorems for monotone paths and convex bodies - PLMS 2012.full.md
```
