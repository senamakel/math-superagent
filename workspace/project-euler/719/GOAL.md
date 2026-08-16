# Goal

Compute T(10^12) for Project Euler problem 719, verified.

**Definition.** A natural number n is an **S-number** iff n = r^2 for some
integer r >= 2, and the decimal digit string of n can be split into 2 or more
nonempty contiguous blocks ("2 or more numbers") whose values sum to r.
T(N) = sum of all S-numbers n <= N.

Symbols:
- r : candidate square root (r >= 2).
- n = r^2 : a perfect square.
- blocks : a partition of the decimal digits of n into k >= 2 contiguous
  nonempty blocks; each block read as an ordinary decimal integer (leading
  zeros allowed within a block, e.g. "00" -> 0, "01" -> 1).
- S = {n : n is an S-number}.
- T(N) = sum_{n in S, n <= N} n.

**Worked examples (test oracle, from problem statement):**
- 81 = 9^2, 9 = 8+1  -> S.
- 6724 = 82^2, 82 = 6+72+4 -> S.
- 8281 = 91^2, 91 = 8+2+81 = 82+8+1 -> S.
- 9801 = 99^2, 99 = 98+0+1 -> S.
- T(10^4) = 41333 (given, to reproduce).

**Structural key.** Since each S-number is r^2 for a root r <= 10^6 when
N = 10^12, T(N) = sum_{r=2}^{floor(sqrt N)} r^2 * [r is an S-root], turning a
10^12 candidate scan into a 10^6 root scan.

## Completion criteria (all must be met with evidence)

1. `/workspace/code/brute.py` (naive oracle) written, run, reproduces the four
   worked examples and T(10^4) = 41333, and gives T(10^6), T(10^12).
2. At least three genuinely different implementations of the split-and-sum
   search explored in parallel via spawn_candidates (recursive prune, digit-DP
   over carries, meet-in-the-middle over prefixes), each reproducing
   T(10^4)=41333 (and the examples) against its own brute force.
   DONE: code/candidates_dfs.py (forward DFS + overshoot pruning),
   code/candidates_digitdp.py (memoized (position,remaining-sum)),
   code/candidates_mitm.py (prefix/suffix sum sets + straddle block). All
   three reproduce T(10^4)=41333, T(10^6)=10804656, T(10^9)=6222187932; MITM
   has a full 10^12 run confirming T(10^12)=128088830547982 (count 406) and
   0 brute-force mismatches on every root in [2,5000]. The others were
   adopted; their own T(10^12) was confirmed by independent routes.
3. A method whose cost grows with sqrt(N), not N, established (root scan).
4. `/workspace/code/solution.py` — exact-integer implementation — agrees with
   brute.py on every case it can reach, reproduces all examples, and computes
   T(10^12).
5. Final answer 2-verified by an independent route (the brute oracle at the
   largest reachable N and/or an independent program), result recorded.
