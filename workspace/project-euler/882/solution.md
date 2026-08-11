# Solution — Project Euler 882 (Dr. One / Dr. Zero bit-deletion game)

## Problem
Board starts with k copies of each k (k=1..n). One deletes a 1-bit from a
number's binary string; Zero deletes a 0-bit (leading zeros dropped, empty→0;
0 has no moves). A player unable to move loses. Zero wins iff One cannot move
on One's turn. Only Zero may skip (pass the turn back to One, costing one skip).
S(n) = minimal total number of skips Zero needs to force a win. Given
S(2)=2, S(5)=17, S(10)=64. Find S(10^5).

## Governing theory: canonical dyadic Numbers and the Simplicity Rule
The game is **strictly partisan** — One and Zero delete disjoint bit types —
so Sprague–Grundy does not apply. But each single-number subgame is a
canonical **Number** in the sense of Conway's combinatorial game theory:

  g(0) = 0
  g(k) = { g(j) : j a 1-deletion of k  |  g(j) : j a 0-deletion of k }

Because every move strictly decreases the numeric value k (each option j < k),
the game is short, and being a Number means max(Left option values) <
min(Right option values). When that holds, the **Simplicity Rule** (Fenner &
Rogers 2015, arXiv:1505.07416) gives the exact value as the *simplest dyadic
rational strictly between* the two bounds: the dyadic of minimal birthday
(smallest denominator power of two) in the open interval (max L, min R).

For k=1..100000 this forward sweep never violates the Number property:
max(Left) < min(Right) for every k (verified by /workspace/solution.py;
first-violation = none). So g(k) is a well-defined dyadic for all k ≤ 10^5.

## Board value and the skip
The board is the **disjunctive sum** of k copies of each game k, so its value
is

  G(n) = Σ_{k=1..n} k · g(k).

A skip by Zero is a Right-move that passes the turn and is worth **−1**
(after each skip the position's value drops by exactly 1; the game is a
stopper, so the fixpoint is well-defined and finite). Zero wins from a position
of value G exactly when G − m ≤ 0, where m is the number of skips. Hence

  S(n) = ceil(G(n)) = minimal integer m with G(n) − m ≤ 0.

## Complexity
g(k) scans the ~17 bits of k, all children are < k, so the whole sweep is
O(N log N) with exact Fraction arithmetic — trivially fine for N = 10^5. No
enumeration of game states is involved; the bound is handled by structure.

## Result
    G(100000) = 517756101446417 / 32768  ≈ 1.58006622e10
    S(100000) = ceil(517756101446417 / 32768) = 15800662276

Check: 32768·15800662275 = 517756101427200 < G < 517756101459968 =
32768·15800662276, so the ceiling is 15800662276.

## How the method beats the alternatives
- The single-aggregate (A,B) counting surrogate is **refuted** (MEMORY.md):
  it collapses to max(0, A−B) and fails the real oracle after n=1. The real
  game value depends on the position/distribution of bits, which is exactly
  what the per-number dyadic CGT value captures.
- Plain enumeration of the real bit game is infeasible beyond n=5 (n=6 alone
  exceeds 1.5M states and times out); the stated bound 10^5 defeats it. The
  Simplicity Rule turns the whole game into a closed poly-size forward sweep.

## Verification (independent routes)
1. **Real-game minimax oracle** (/workspace/code/brute.py, /workspace/code/
   fastbrute.py) gives S(1..5) = 1,2,8,9,17 on the TRUE bit game; statement
   examples S(2)=2, S(5)=17 match; n=1..3 additionally verified by a fully
   explicit independent move search.
2. /workspace/solution.py reproduces ceil(G(n)) for n=1..20 = 1,2,8,9,17,23,
   44,45,56,64, which matches S(2)=2, S(5)=17, S(10)=64 (given) and every
   real-oracle value at n=1..5.
3. **Second independent code path** (/workspace/verify_dyadic.py, a separate
   implementation with its own deletion enumerators) returns the identical
   G(10^5) = 517756101446417/32768 and S = 15800662276.
4. Exact integer ceiling check (above) confirms the fraction's ceiling
   directly.

## Files
- /workspace/solution.py — the solution implementation (dyadic sweep, Number
  check, G and S at full size).
- /workspace/solve_dyadic.py, /workspace/verify_dyadic.py — two independent
  implementations that agree.
- /workspace/dyadic_answer.txt — two-line final result.
- /workspace/oracle_S.txt — real-game minimax S(n) table (n=1..5).
- /workspace/code/brute.py, /workspace/code/fastbrute.py — real-game oracles.
- /workspace/code/toolkits/simplest_dyadic.py — simplest-dyadic-between helper,
  validated against an independent birthday oracle.

**Answer: S(10^5) = 15800662276.**
