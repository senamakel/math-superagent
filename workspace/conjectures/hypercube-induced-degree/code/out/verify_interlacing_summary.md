# Verification of the spectral-interlacing (Huang) lower-bound chain — small n

Backing program: `code/out/verify_interlacing_chain.py`
Output: `code/out/verify_interlacing_chain.captured.txt` (EXIT_CODE=0, runtime <1s).

## What was verified

Matrix `A_n` built by the exact recursion

```
A_1 = [[0,1],[1,0]]
A_n = block [[A_{n-1}, I_{2^{n-1}}], [I_{2^{n-1}}, -A_{n-1}]]
```

### (a) `A_n` properties, n = 1..8, exact integer arithmetic

- symmetric;
- entries in {0, ±1};
- zero diagonal;
- **A_n^2 = n·I** exactly (on integer matrices; diagonal all `n`, off-diagonal all `0`);
- support is exactly the edge set of `Q_n`: `A[u,v] ≠ 0` iff `u` and `v` differ in one bit.

All PASS for n = 1..8.

**Why A_n^2 = n I is true in general** (block multiplication, independent of the
numerical check): the recursion gives

```
A_n^2 = [[A_{n-1}^2 + I, A_{n-1} − A_{n-1}],
         [A_{n-1} − A_{n-1}, I + A_{n-1}^2]]
      = [[n I, 0], [0, n I]] = n I_{2^n}
```

by induction from `A_1^2 = I`. So for every n the spectrum of `A_n` is
{+√n, −√n}, each with multiplicity 2^{n-1} (A_n symmetric, zero diagonal, trace 0).
The multiplicity split was confirmed numerically for n = 1..8 (each eigen-double
appears exactly 2^{n-1} times).

### (b) Interlacing claim, n = 2..8

Take `S` = all even-weight vertices (2^{n-1} of them) plus one odd vertex
(vertex 1), so `|S| = 2^{n-1} + 1`. Let `B = A_n[S,S]`. Cauchy interlacing for a
k×k principal submatrix of an m×m symmetric matrix (`k = 2^{n-1}+1`) gives
`μ_1 ≥ λ_{m−k+1} = λ_{2^{n-1}} = √n`. Verified: λ_max(B) ≥ √n for every
n = 2..8, equality to ~1e-15 (machine precision).

Exact spot check n=2: `B = [[0,0,1],[0,0,1],[1,1,0]]` has charpoly
`λ(λ²−2)`, so λ_max = √2 = sqrt(2) exactly.

### (c) The pure even-weight independent set (|S| = 2^{n-1}), n = 2..8

λ_max(B) = 0 < √n for every n. (The even set is independent — all pairwise
Hamming distances are even — so its in-set adjacency submatrix is identically
zero; this is exactly the statement's example that `D = 0` at half-size.)

## What it does and does not prove

- **Established (numerically + the ∀n block proof above):** the recursion does
  give a symmetric {0,±1} matrix whose square is n I and whose support is Q_n,
  for at least n ≤ 8; and for the specific S = even-set + one odd vertex the
  interlacing inequality λ_max(B) ≥ √n holds.
- **Not established:** `f(n) ≥ √n for ALL n` (Huang's theorem / the claimed
  ground-level bound). This run only checked a handful of small n. The logic
  chain — for every admissible S, λ_max(B) ≥ √n, and Δ(Q_n[S]) ≥ λ_max(B) — is
  the standard Huang argument and is only numerically sampled here, not proved
  for all n. The full-spectrum ±√n and the interlacing theorem are the two
  pillars; both are classical and hold in general, but a complete proof for all
  n belongs to theorem_prover/lean_prover, not to this small-n check.

Exact values observed for the specific S (even-set + odd 1):

| n | |S| | λ_max(B) | √n |
|---|---|---|---|---|
| 2 | 3  | 1.41421356 | 1.41421356 |
| 3 | 5  | 1.73205081 | 1.73205081 |
| 4 | 9  | 2.00000000 | 2.00000000 |
| 5 | 17 | 2.23606798 | 2.23606798 |
| 6 | 33 | 2.44948974 | 2.44948974 |
| 7 | 65 | 2.64575131 | 2.64575131 |
| 8 | 129| 2.82842712 | 2.82842712 |
