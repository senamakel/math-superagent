# Barber, "A note on balanced independent sets in the cube" (arXiv:1210.4029, 2012)

URL: https://arxiv.org/abs/1210.4029

## What it establishes

Q_n = {0,1}^n, X_0 = even-weight, X_1 = odd-weight vertices (|X_0|=|X_1|=2^{n-1}).

- **Classification of maximum independent sets:** the only independent sets of
  size 2^{n-1} are the two parity classes X_0, X_1; every other independent set
  has size < 2^{n-1}. (Paper's introduction; a standard cube fact.)
- Main new result (proves a conjecture of Ramras): a *balanced* independent set
  (exactly half of its vertices in X_0, half in X_1) has maximum size
  2^{n-1} − 2^{n-3}·(n−2) for even n and 2^{n-1} − 2^{n-2}·(n−1)/2 for odd n —
  strictly smaller than 2^{n-1} for n > 1 (the text states the odd case as
  2^{n-1} − 2^{n-2}(n−1)/2). Proven via a simplicial-order isoperimetric theorem
  for even-sized sets (Bezrukov; Körner–Wei; Tiersma).
- Method: if A ⊆ X_0 and B is the initial segment of the simplicial order
  restricted to X_0 with |B|=|A|, then |N(B)| ≤ |N(A)|. Maximal balanced sets
  are an initial segment of X_0 and a terminal segment of X_1.

## Why it is here

Closes request `classification-maximum-independent-20be`: the parity classes are
the *unique* maximum independent sets. This pins the structure problem.md's S of
size 2^{n-1}+1 sits on: removing one vertex from S leaves an independent set of
size 2^{n-1} (were it maximum) that must be a parity class, so the extremal S
is "a parity class plus one vertex of the other parity", whose added vertex has
internal degree exactly n. This is the extremal boundary of f(n).

## claim block

```claim
id: max-independent-kernel-of-cube-are-parity-classes
answers: classification-maximum-independent-20be
statement: The maximum independent sets of Q_n are precisely the two parity
  classes X_0, X_1, each of size 2^{n-1}; any independent set of size 2^{n-1}
  is one of them.
hypotheses: Q_n bipartite, parts X_0, X_1, n >= 1.
holds-here: yes — it is the structural base of the "one vertex past half"
  picture of problem.md.
status: asserted-by-source (standard cube fact, stated in introduction)
bearing: the extremal S near 2^{n-1}+1 is a parity class plus one crossing
  vertex (internal degree n of that vertex); the isoperimetric argument is a
  second instance of the simplicial-order machinery already in the library.
falsifies: an explicit independent set of Q_n (n >= 2) of size 2^{n-1} that is
  neither parity class.
anchor: research/sources/barber-balanced-independent-cube-2012.md
```

```claim
id: balanced-independent-set-max-smaller-than-parity
statement: The largest balanced independent set of Q_n has size
  2^{n-1} − 2^{n-3}(n−2) (even n) / 2^{n-1} − 2^{n-2}(n−1)/2 (odd n), < 2^{n-1}
  for n > 1.
hypotheses: n >= 1, balanced (equal even/odd counts), independent.
holds-here: yes (small-n parity of the formula must be read from the source).
status: asserted-by-source (Theorem 1)
bearing: the parity classes are the unique way to reach size 2^{n-1}; a
  balanced set of that size or more is impossible, so "one more than half" must
  essentially take a full parity class plus a crossing vertex.
falsifies: a balanced independent set of Q_n of size >= 2^{n-1} for n >= 3.
anchor: research/sources/barber-balanced-independent-cube-2012.md
```

**Does not help directly:** it is an independent-set (D=0) result, the d=0 line
of f(n), not a bound on D(S) at the +1 excess. Useful as the extremal-scaffold
fact and as a cross-check of the isoperimetric machinery.
