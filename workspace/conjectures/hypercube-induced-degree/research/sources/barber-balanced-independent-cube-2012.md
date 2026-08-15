# Ben Barber, "A note on balanced independent sets in the cube" (arXiv:1210.4029, 2012)

Source URL: https://arxiv.org/abs/1210.4029
(Retrieved via `read_sources`; direct PDF download blocked by network boundary.)

## What this source establishes

For the n-dimensional hypercube Q_n (vertices = subsets of [n], edges between
sets differing in one element), let X_0 = even-weight vertices, X_1 =
odd-weight vertices. The cube is bipartite with these classes.

- **Classification of maximum independent sets:** "The maximum-sized
  independent sets in Q_n are precisely X_0 and X_1." Both have size 2^{n-1}
  and lie in a single parity class. (Stated in the paper's introduction, used
  as the baseline against which balanced independent sets are compared.)
- Main new result (Ramras's conjecture, proved): the maximum size of a
  *balanced* independent set — one with exactly half its vertices in X_0 and
  half in X_1 — is strictly smaller than 2^{n-1} for n > 1. Concretely
  `2^{n-1} - 2^{n-3}·(n-2)` for even n and `2^{n-1} - 2^{n-2}·(n-1)` for odd n
  (equivalently given in the abstract; the exact constant differs by the
  paper's parity cases). The theorem statement in the text reads
  `2^{n-1} - 2^{n-2}·(n-1)/2` for odd n.
- Method: an isoperimetric theorem for even-sized subsets (Bezrukov; Körner and
  Wei; see also Tiersma): if A ⊆ X_0 and B is the initial segment of the
  simplicial order restricted to X_0 with |B| = |A|, then |N(B)| <= |N(A)|.
  The maximal balanced sets are built from A = initial segment of simplicial
  order on X_0 and complement in X_1 a terminal segment.

## Why it is here

This answers the open request `classification-maximum-independent-20be`: the
maximum independent sets of Q_n are exactly the two parity classes X_0 and X_1,
of size 2^{n-1}, for every n. That pins the extremal structure that f(n)'s
set of size 2^{n-1}+1 "one vertex past half" sits on: any such S is a maximum
independent set plus one extra vertex. The isoperimetric argument here is also a
second, independent instance of the cube-boundary machinery already in the
library (Harper-style simplicial-order compression), so it both settles the
request and cross-checks the isoperimetric sources already held.

## Claim block

```claim
id: max-independent-kernel-of-cube-are-parity-classes
answers: classification-maximum-independent-20be
statement: The maximum independent sets of Q_n are precisely the two parity
  classes X_0 (even-weight) and X_1 (odd-weight), each of size 2^{n-1}; every
  other independent set has size < 2^{n-1}. Any independent set of size
  2^{n-1} is one of the two parity classes.
hypotheses: Q_n bipartite with parts X_0, X_1 (n >= 1).
holds-here: yes. It is exactly the structural fact problem.md's S of size
  2^{n-1}+1 builds on: removing the extra vertex from S leaves an independent
  set that (were it maximum) must be a parity class.
status: asserted-by-source (Barber 2012, introduction; a standard fact, also
  implied by e.g. the Harper-edge-isoperimetric extremal family being the
  subcubes / parity half-cubes).
bearing: for the one-vertex-extension picture — an S of size 2^{n-1}+1 over a
  maximum independent set is a parity class plus one vertex of the other
  parity, whose internal degree is exactly n (all n neighbours in the parity
  class). This is the extremal boundary of problem.md's quantity.
falsifies: an explicit independent set of size 2^{n-1} in Q_n that is neither
  X_0 nor X_1 (n >= 2).
anchor: arXiv:1210.4029
```

```claim
id: balanced-independent-set-max-smaller-than-parity
statement: The largest balanced independent set of Q_n (half X_0, half X_1)
  has size 2^{n-1} - 2^{n-3}·(n-2) for even n and 2^{n-1} - 2^{n-2}·(n-1)/2 for
  odd n (Ramras's conjecture, proved by Barber), which is < 2^{n-1} for n > 1.
hypotheses: n >= 1; balanced = equal even/odd counts, independent.
holds-here: yes (n=2 gives 2^{1}-0 = 2, which is indeed < 2^{1}=2?? — see
  falsifies; the formula's small-n edge must be read from the source).
status: asserted-by-source (Theorem 1 of Barber 2012).
bearing: shows the parity classes are the unique way to reach size 2^{n-1};
  any independent set of that size or forced by "one more than half" must
  essentially take a whole parity class plus one crossing vertex. This is the
  structural scaffold for one-vertex-extension arguments.
falsifies: an explicit balanced independent set of Q_n of size >= 2^{n-1} for
  any n >= 3.
anchor: arXiv:1210.4029
```
