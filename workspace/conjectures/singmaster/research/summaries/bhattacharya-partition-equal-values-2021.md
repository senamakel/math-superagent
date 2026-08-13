# Tengely–Ulas 2021 — Equal values of partition functions via Diophantine equations

Source: Sz. Tengely, M. Ulas, Res. Number Theory 7:67 (2021), open access.
Full text read: `research/sources/bhattacharya-partition-equal-values-2021.full.md`
(the journal page lists Tengely–Ulas as authors; the file name carries an older
title). URL: https://doi.org/10.1007/s40993-021-00293-7

## What the paper establishes

For finite `A ⊂ N₊` with partition function `P_A(n)` (partitions of n with parts
in A), the equal-values Diophantine equation `P_A(x)=P_B(y)`:

- **Thm 2.1**: for `A={a₁,a₂}` coprime and any polynomial `f ∈ Z[x]` with
  positive leading coefficient, `P_A(x)=f(y)` has infinitely many solutions
  (`n = a₁a₂(f(m)−1)` works; uses Sertöz's formula `P_A(n)=⌊n/(a₁a₂)⌋ or +1`).
- **Thm 3.1**: `P₃(x)=P₄(y)` has infinitely many solutions, explicitly split
  into 54 cases over residue classes mod 6/12; several parameter families
  (quadratic→cubic reducibility), plus two isolated solutions (8,4) and
  (6533,439) from the elliptic curve `Y²=X³−108X+1728` (rank 2).
- **Thm 3.2**: `P₃(x)=P₅(y)` has only finitely many solutions — the complete
  16-point list {(1,1),…,(10093,388)}; proved with 360 quartic equations,
  Magma's IntegralQuarticPoints, elliptic reductions.
- **Thm 4.3/4.4/4.5**: for `A={1,2,a}`: `P_A(m)=P₄(n)` infinitely many iff
  `a ≢ 2 mod 4` (finitely many if `a ≡ 2 mod 4`); `y²=P_A(x)` has infinitely
  many solutions for every `a ≥ 3` (Pell parametrization; square a handled by
  polynomial-square families); `P_A(x)=P_B(y)` (a,b ≡ 0 mod 4, a/2 or b/2
  non-square) infinitely many via Pell.
- **Thm 5.1**: `y²=P₅(x)` has only the two solutions (1,1),(2027,77129).
  Conjecture 5.2: `y²=P_n(x)` has only (1,1) for n ≥ 6.
- **Thm 6.3**: for `A={1,2,a}, B={1,2,3,4,b}`, `b=4a`, `a ≡ 1,2,5,7,10,11
  mod 12`: `P_A(x)=P_B(y)` infinitely many.
- The finite-partition function case is quasi-polynomial (`P_A(L_A n+i) ∈ Q[n]`),
  so every such equation reduces to finitely many polynomial Diophantine
  equations with separable variables — the same separated-variable
  `f(x)=g(y)` structure as the binomial problem.

## Bearing for this run — does NOT help

- This is an **adjacent problem to a different object** (finite-set partition
  functions, not binomial coefficients). None of its theorems transfer to
  `C(x,k1)=C(y,k2)`: the partition function's quasi-polynomial/reducibility
  mechanism (a quadratic can equal a cubic only when a discriminant is a square,
  giving Pell families) has no analogue in the binomial collision curve, whose
  degrees in x and y are the *fixed* k1, k2.
- The paper is useful only as a **methodological comparison**: it shows a whole
  family of "equal values of counting functions" equations where *infinite
  families do occur* (unlike the binomial problem, where Jenkins/HPT/BST show
  the only infinite family is the quadratic/Fibonacci one). This contrast
  sharpens the run's structural claim: for the binomial problem, the
  exceptional (infinite) pairs are severely restricted by the Bilu–Tichy/HPT
  classification, whereas for partition functions they are generic.
- **Verdict: does not help the run's Singmaster goal.** Filed so nobody re-reads
  the 82 KB full text expecting a transferable theorem. No claim block; nothing
  in the run's ledger depended on it, and nothing should.

```claim
id: tengely-ulas-partition-equal-values-adjacent
statement: Tengely-Ulas 2021 (Res. Number Theory 7:67) solve several
  Diophantine equations P_A(x)=P_B(y) for finite-set partition functions: e.g.
  P_3=P_4 has infinitely many solutions (Thm 3.1), P_3=P_5 finitely many (Thm
  3.2, complete 16-list), y^2=P_A(x) infinitely many for all A={1,2,a} (Thm
  4.4), y^2=P_5(x) only (1,1),(2027,77129) (Thm 5.1). The mechanism is
  quasi-polynomiality of P_A plus discriminant-square (Pell) reducibility.
hypotheses: finite A,B; P_A the number of partitions with parts in A.
holds-here: no — different counting function (partitions, not binomials); the
  infinite-family mechanism does not transfer to C(x,k1)=C(y,k2).
status: asserted-by-source (full text read; statements quoted)
bearing: negative/methodological — a contrast case where equal-values equations
  are generically infinite, vs the binomial problem's severely restricted
  infinite families; no Singmaster content.
anchor: research/sources/bhattacharya-partition-equal-values-2021.full.md
```