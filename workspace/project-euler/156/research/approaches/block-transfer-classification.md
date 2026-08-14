# Approach — block-transfer bijection giving s(d) in closed form

```approach
idea: Classify the solution set as a base-10 "block transfer": prove that for
k ≤ d−1 the map x ↦ k·10^10 + x is a bijection from the block-0 solutions to
the block-k solutions, so s(d) is a closed-form sum instead of an enumerated
total.
mechanism: The place-value identity gives, for 0 ≤ x < 10^m and k ≤ d−1,
  f_d(k·10^m + x) − f_d(x) = k·m·10^{m−1}
At m=10 this is exactly k·10^10, hence
  f_d(k·10^10 + x) = f_d(x) + k·10^10.
Therefore f_d(x)=x ⟺ f_d(k·10^10 + x) = k·10^10 + x: translation by k·10^10
carries block-0 solutions to block-k solutions.  Since every solution satisfies
n ≤ d·10^10 (Khovanova–Marton Prop 9.1), the full solution set is the disjoint
union over k=0..d−1 of the translates, giving
  s(d) = d·Σ_{x∈S_0(d)} x + (d(d−1)/2)·10^10·|S_0(d)|,
where S_0(d) = {x < 10^10 : f(x,d)=x} is the block-0 seed set.  This converts
the whole computation into (i) a proof of the residue identity, (ii) an
enumeration of the small seed set S_0(d) inside [0,10^10), and (iii) a
closed-form sum — no jump iterator over [0, d·10^10] at all.
status: adopted
first-step: the residue identity is now proven (derivation below); implement
`code/block_transfer.py` that (a) enumerates S_0(d) = solutions of f(n,d)=n
in [0,10^10) by the jump iterator, (b) assembles the full solution set as
∪_k (k·10^10 + S_0(d)) for k=0..d−1, (c) computes s(d) by the closed form,
and (d) verifies the bijection and s(d) against the 9 solution files
code/out/solutions-d*.txt already on disk.
```

## The residue identity — proven, not merely sampled

**Theorem (residue identity).** For 1 ≤ d ≤ 9, 1 ≤ k ≤ d−1, m ≥ 1, and every
0 ≤ x < 10^m:

    f_d(k·10^m + x) − f_d(x) = k·m·10^{m−1}.

**Proof.** Write f_d(N) = Σ_{j=0}^{N} c_d(j), c_d(j) = # of occurrences of digit
d in the decimal writing of j. For N = k·10^m + x with 0 ≤ x < 10^m:

    f_d(k·10^m + x) = f_d(k·10^m − 1) + Σ_{j=k·10^m}^{k·10^m+x} c_d(j).

Every j in [k·10^m, k·10^m + x] has decimal form (digits of k) followed by the
m digits of j − k·10^m (x padded to m digits). Since k ≤ d−1 ≤ 8, k is a single
digit ≠ d, so the high part contributes c_d(k) = 0 occurrences of d; the low
part runs through 0..x and, because d ≥ 1 means leading zeros are irrelevant,
contributes exactly f_d(x). Hence f_d(k·10^m + x) = f_d(k·10^m − 1) + f_d(x),
so the left side equals f_d(k·10^m − 1).

Now count d in 0..k·10^m − 1. Each such number has a high digit h ∈ {0,…,k−1}
(the coefficient of 10^m) and m low digits running 0..10^m−1. The high position
equals d only when d ≤ k−1, impossible since k ≤ d−1; it contributes 0. Each of
the m low positions, over the full cycle of 10^m values repeated once per high
digit h (k repetitions total), contains d exactly 10^{m−1} times per repetition,
so k·10^{m−1} times per position. Over m positions: k·m·10^{m−1}. ∎

**Corollary (block transfer, m = 10).** For 0 ≤ x < 10^10 and 1 ≤ k ≤ d−1:

    f_d(k·10^10 + x) = f_d(x) + k·10^10,
    hence  f_d(x) = x  ⟺  f_d(k·10^10 + x) = k·10^10 + x.

**Corollary (closed form).** With S_0(d) = {x < 10^10 : f_d(x) = x} and the
bound n ≤ d·10^10 (Khovanova–Marton Prop 9.1, on disk), the solution set of
f_d(n) = n is the disjoint union over k = 0..d−1 of k·10^10 + S_0(d), and

    s(d) = d·Σ_{x∈S_0(d)} x + (d(d−1)/2)·10^10·|S_0(d)|.

**Controlled break at k = d.** Here c_d(d) = 1, so the same computation gives

    f_d(d·10^10 + x) = f_d(x) + d·10^10 + x + 1 > d·10^10 + x,

i.e. no solution has n ≥ d·10^10. This is exactly the "controlled break" the
run already sampled in code/pattern_residue_exact.py.

## Verification against the run's own data

The classification is not a conjecture: it is visible in and checked against
the complete solution files code/out/solutions-d*.txt (661 solutions total,
produced by the independent jump iterator). Block structure confirmed:

| d | \|S_0(d)\| | blocks | total | s(d) |
| --- | --- | --- | --- | --- |
| 1 | 84 | 1 | 84 | 22786974071 |
| 2 | 7 | 2 | 14 | 73737982962 |
| 3 | 12 | 3 | 36 | 372647999625 |
| 4 | 12 | 4 | 48 | 741999999540 |
| 5 | 1 | 5 | 5 | 100000000000 |
| 6 | 12 | 6 | 72 | 2434703999430 |
| 7 | 7 | 7 | 49 | 1876917059570 |
| 8 | 43 | 8 | 344 | 15312327487352 |
| 9 | 1 | 9 | 9 | 360000000000 |

Closed-form check (hand-verified): for d=2, ΣS_0 = 1868991481, so
s(2) = 2·1868991481 + 1·10^10·7 = 73737982962 ✓. For d=7, ΣS_0 = 58131008510,
so s(7) = 7·58131008510 + 21·10^10·7 = 1876917059570 ✓. Grand total
Σ s(d) = 21295121502550, matching code/solution.py.

## Which parts are established, which are speculation

- **Established (proven above).** The residue identity and the block-transfer
  bijection; the closed form for s(d) given S_0(d); the break at k = d.
- **Sourced.** The bound n ≤ d·10^10 (Khovanova–Marton Prop 9.1, on disk).
- **Established by this run.** S_0(d) and s(d) for all nine digits (solution
  files on disk; s(d) matches the independent jump iterator).
- **Still open / the real remaining work.** Whether S_0(d) itself admits a
  further self-similar decomposition at scale 10^m for m < 10 (the seed sets
  show no obvious sub-block transfer, but the question is not closed), and
  whether the whole classification is already named in the literature (one
  research check was launched; see THREADS.md when it lands).
