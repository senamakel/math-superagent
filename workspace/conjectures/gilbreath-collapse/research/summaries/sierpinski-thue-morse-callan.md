# Sierpinski's triangle and the Prouhet–Thue–Morse word — David Callan (2006)

Source: https://arxiv.org/pdf/math/0610932 (arXiv:math/0610932); full text at
`research/sources/sierpinski-thue-morse-callan.full.md` → [[sierpinski-thue-morse-callan.full]]

## What it establishes

Pascal's triangle mod 2, left-justified, is the infinite lower-triangular (0,1)-matrix
`S` with `S[i][j] = C(i,j) mod 2 = 1` iff `j` is a binary submask of `i`; the rows of
`S` are the indicator functions of the principal down-sets `M_i = ↓i` of the Boolean
lattice — exactly the sets `M_d` that are the rows of this problem's fold matrix `Φ_n`
(shifted to absolute positions `n−1−d+o`).

- **Theorem 1.** `S^{-1} = S(-1)` is a `(-1,0,1)`-matrix sharing the zero pattern of
  `S`; the nonzero entries in each column form the Prouhet–Thue–Morse word
  `((−1)^{popcount(j)})`. The inverse of the down-set incidence matrix is the Moebius
  function of the boolean down-set semilattice.
- **Theorem 2.** `S(x)S(y) = S(x+y)`; `S(x)^q = S(qx)`; `S(1) = S`. Where
  `S(x)_{ij} = x^{popcount(i−j)}` when `i−j` is free of `j` (binary subtraction has no
  borrows), else 0. Equivalently (Added in Proof, Bacher): the `2^k × 2^k` top-left
  corner of `S(x)` is the `k`-fold Kronecker product of `[[1,0],[x,1]]`.

The carry-free ("free of", no borrow) condition is exactly the rule governing the run
partition in problem item 5: `j ⊆ i` iff `i−j` has no carries.

## Bearing on this problem

Canonical reference for the matrix whose rows are `M_d`. Theorem 1 gives Moebius
inversion on the down-set semilattice — the cancellation structure that decides which
symmetric differences `M_d △ M_{d'}` survive as Walsh characters. Theorem 2 is the
self-similar fact behind the O(n) distance enumerator (imported result 4) and the run
structure (result 5).

## Claim blocks

```claim
id: callan-downset-inverse
statement: The down-set incidence matrix S (row d = indicator of the principal down-set
  M_d of the Boolean lattice) satisfies S^{-1} = S(-1), a (-1,0,1)-matrix with the same
  zero pattern as S and Thue-Morse ((−1)^{popcount}) sign structure in each nonzero
  entry; equivalently the 2^k × 2^k corner of S is the k-fold Kronecker product of
  [[1,0],[1,1]].
hypotheses: S infinite lower-triangular Pascal-mod-2 matrix, rows = down-sets M_d
holds-here: yes
status: proved
bearing: gives the Moebius-inversion weight of each down-set, the cancellation structure
  deciding which M_d △ M_{d'} survive in the S² Walsh sum (GOAL priority 1).
anchor: research/sources/sierpinski-thue-morse-callan.full.md
```

```claim
id: callan-selfsimilar
statement: S(x) S(y) = S(x+y) and S(x)^q = S(qx), where S(x)_{ij} = x^{popcount(i-j)}
  when i-j is free of j (binary subtraction, no borrows) and 0 otherwise; S(1) = S.
hypotheses: x,y indeterminates; i ≥ j ≥ 0
holds-here: yes
status: proved
bearing: the self-similarity/block-Kronecker decomposition behind imported result 4
  (distance enumerator O(n)) and result 5 (runs of M_d of length 2^{ν₂(d+1)}); the
  carry-free condition is the run-partition rule.
anchor: research/sources/sierpinski-thue-morse-callan.full.md
```

## What it does not settle

Does not enumerate which distinct `M_d △ M_{d'}` occur, nor their multiplicities —
that is the exact listing GOAL priority 1 wants and it remains open.
