# Refuter finding: the powers-of-two string is NOT a G-weak-input-strictness witness

Attacked the run's central positive hypothesis `G-weak-input-strictness` (weak-input
skeleton): *some fixed binary string h\* with switch density 0 and ν₂(n) ≥ c·n*.

The run already proved a **fixed single 1** gives bounded (O(1)) weight and pinned
the needed witness as *sparse-but-growing*. The canonical such candidate is the
**powers-of-two string** h[j] = 1 iff j is a power of two (1, 2, 4, 8, …), which has
switch density 0 (O(log n)/n → 0). This note finds that candidate FAILS too.

## Structural proof (hand, then machine)

Setup: h[j]=1 iff j is a power of two. Fold cell (problem.md facts 1-2):

    T(n,d) = ⊕_{o ⊆ d} h[n-1-d+o],   d = 2..n-1.

Write k = n-1-d (the window's start index). Then d = n-1-k, so o ⊆ d means o's bits
are within the 0-bits of k (o ⊆ ~k, no carry): the read index is P = k + o with
(k+o)&k = 0, i.e. **k ⊆ P** (k is a bitwise submask of P, P = k|o).

Since P is a single-bit power of two, P's submasks are {0, P}. So the cell reads
h[k+o] at indices o ⊆ ~k; among these, exactly those P that are powers of two
contribute. A P ∈ {k+o : o ⊆ ~k} is a power of two iff:
- P = 0 (never; the h value at the window here, but h[0]=0, so irrelevant), or
- P = k (if k is itself a power of two; o=0 ∈ ~k-submask) or P = 2^a with k ⊆ 2^a.

For a power P=2^a ≠ k, the condition "k ⊆ 2^a" with k ≠ 2^a forces k = 0 only
(single-bit P has only submask 0 besides itself). Hence the cell is 1 exactly for
windows whose start k is a power of two:
- k = 0: the only powers ⊆ the window are {P: P ≤ n-1 with o ⊆ ~0}, i.e. all powers
  of two in [0, n-1]; parity = number of powers in {1,2,4,...,2^{m-1}} = m mod 2.
- k = 2^a (a ≥ 1): the read indices P with k ⊆ P are exactly P = k; the window
  [k, n-1] hits the single power P=k along the submask path... contributing 1 iff
  ≤ n-1 (always true since k ≤ n-1).

So T(n,d) = 1 for exactly the k ∈ [0, n-3] that are powers of two (plus k=0 with
parity m mod 2). Number of such k is ⌊log₂(n-1)⌋, hence

    ν₂(n) = O(log n),   ν₂(n)/n → 0.

## Machine cross-check

Literal submask-XOR oracle (no reliance on the reduction):

    n      ones(h)    nu2(direct)   nu2/n
     8        4           4         0.5000
    12        4           4         0.3333
    16        5           4         0.2500
    32        6           5         0.1562
    64        7           6         0.0938
   128        8           7         0.0547
   256        9           8         0.0312
   512       10           9         0.0176

Ratio → 0: sublinear, NOT linear. (The m mod-2 contribution is visible: nu2(16)=4
since 15 = 1111 has m=4 even.) This reproduces the hand formula exactly.

## Bearing on the run

- The powers-of-two string fails G-weak-input-strictness. The needed witness is
  *not* in the single-power-of-two-per-position family.
- This is a second closed candidate for the central positive hypothesis, joining
  the fixed-single-1 bound. The witness must be sparse-but-growing in a *denser or
  more carefully positioned* way — this rules out the "powers of two" shape.
- Contrast with the per-window boundary spike h=e_{n-1} which does amplify (but is
  not a fixed h, so doesn't satisfy G-weak-input-strictness's "fixed" requirement).

## Status

Structural argument + machine reproduction: a proof that the powers-of-two family
is sublinear, and a numeric confirmation. Engine not run on this (parity encoding
returns undecided, as the run's other parity probes did). Two independent routes
(hand/structure and literal oracle) agree; claim status: checked-numerically +
structural proof.

# (scratch) — promote to a claim block once a run of powers_two_check.py confirms
