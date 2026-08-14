# Shared context

This run solves Project Euler 233 (`/workspace/problem.md`). It is early: no
code, no solution.md exist yet; durable memory (Cognee) is empty; GOAL.md is the
template. Everything below is derived from the problem statement + standard
sum-of-two-squares theory. The run must confirm it with `code/brute.py` (small-N
oracle) before trusting it.

**Budget**: 10000 tokens; file currently ~1k.

## Established

**Reduction: f(N) = r₂(2N²).** The circle through the four square corners has
center (N/2,N/2) and radius N√2/2. Scaling its equation by 4:
(2x−N)² + (2y−N)² = 2N². Writing u=2x−N, v=2y−N gives an integer bijection
between lattice points (x,y) on the circle and solutions of u²+v²=2N² (both
sides even forces u,v same parity as N, so x,y stay integral). Hence
f(N) = r₂(2N²), the number of ordered signed representations of 2N² as a sum of
two squares. — *Proved by parity bijection; matches the stated f(10000)=36
(computed and checked, see Numbers).*

**Two-square theorem.** r₂(m) = 4·∏(e_p+1) over primes p≡1 (mod 4) if every
prime ≡3 (mod 4) divides m to even exponent, else 0. (Standard number-theory
result; the run should cite a source when it records it in CLAIMS.md.)

**Consequence.** For N = 2^a ·∏p_i^{e_i} (p_i≡1 mod4) ·∏q_j^{g_j} (q_j≡3 mod4),
2N² has exponents 2a+1 on 2, 2e_i on p_i, 2g_j on q_j. The q_j and the 2
contribute nothing to r₂; so
**f(N) = 4·∏_{p≡1 mod4, p|N} (2·e_p + 1)**.

**Target 420 ⇒ ∏(2e_p+1) = 105 = 3·5·7.** Multiplicative partitions of 105 into
odd parts ≥3 give exactly five exponent patterns for the ≡1-mod-4 primes of N
(listed as (2e+1) factors → exponents e):
- {105}: one prime, e=52
- {35,3}: e=17, e=1
- {21,5}: e=10, e=2
- {15,7}: e=7, e=3
- {7,5,3}: e=3, e=2, e=1

Two implications that structure the search:
1. Each valid N's ≡1-mod-4 primes match exactly one pattern — no double count.
2. Powers of 2 and powers of primes ≡3 mod 4 are **free**: any exponent, since
   their exponents are doubled (even) in 2N². So N = core·m where core is the
   {≡1-mod-4 primes}^e product for one of the five patterns, and m has only
   prime factors in {2}∪{primes≡3 mod4}, any exponents, with m ≤ 10^11/core.

**Method shape** (to be implemented, not exhaustive in the bound's sense): the
bound 10^11 is defeated by this factorization structure — enumerate the ~small
set of cores per pattern (distinct ≡1-mod-4 primes to prescribed exponents),
then for each count/sum the free part m by recursion over 2 and ≡3-mod-4 primes.
Sum of valid N = Σ_core c · (Σ of valid m ≤ limit/c). Reduce `code/brute.py`
oracle to small N; `code/solution.py` exact-integer at 10^11. Declare
complexity; must not enumerate up to 10^11 directly.

## Ruled out

(none yet — run has not attempted approaches)

## Numbers

- f(10000) = 36 per statement. Check of the formula: 10000=2⁴·5⁴, only p=5≡1
  mod4 with e=4 ⇒ f=4·(2·4+1)=36. ✓ (computed and checked; brute.py must give
  the same by direct counting).
- So far no brute.py small-N table exists; the run should produce one
  (e.g. f(N) for N≤~10^4 via direct circle-point count vs. the formula) as the
  oracle agreement range.

## Recalled

Cognee is empty (recall_memory returned no data). No earlier-run memory on this
problem or its shape to import. Mirror of a note: remember the reduction once
brute.py confirms it.

## Contradictions

None — the only stated example (f(10000)=36) is reproduced by the formula.

## Gaps

- brute.py not yet written; needs to reproduce f(10000)=36 by direct counting
  and to confirm the r₂ formula on a range of small N.
- A citable source for the two-square divisor formula (for CLAIMS.md) is still
  wanted; state a precise citation request if the run cannot supply one.
- The final sum at N≤10^11 is uncomputed by this run; the closing answer must
  be produced by `code/solution.py` and verified by an independent route
  (per-... independent program or brute at largest feasible N).
