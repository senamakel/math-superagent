# Workspace survey (cycle 1) — PE1006

Surveyed by the context curator before any work was attempted. What the
workspace holds and what it does not.

## The only substantive inputs

1. **Problem statement** — `/workspace/problem.md`, from
   https://projecteuler.net/minimal=1006. Oracle values: k=3 subwords
   001,010,100,101 → Ψ(3)=20302; Ψ(10) ≡ 10699667 (mod 101001001); target
   Ψ(10^18) mod 101001001. Template S_2=010, S_3=01001, S_4=01001010.
2. **Steering directives** — `/workspace/config/directives.jsonl` (2 lines).
   Dir. 1: pair-correlation, valid at k=F_n−1; C(j,jp)=A(jp−j) with
   A(d)=max(0,m−t)+max(0,m−(N−t)), N=F_n, m=#ones of standard word q_n,
   t=(dm) mod N; collapses to one lag-sum with geometric weights; remaining
   sum_d (ad mod N)·x^d evaluable by a Euclidean/Ostrowski recursion in
   O(log N). Dir. 2 (stronger, all k): mechanical-word model with rational
   slope a=F(n−1)/F(n); telescoped v(x)=floor(x+ka) − 10^(k−1)floor(x) +
   9·Σ_{j=1}^{k−1} 10^(k−1−j) floor(x+ja); Ψ(k) = second moment of the
   geometrically weighted floor sum; primitive is the universal Euclidean
   algorithm (Chtholly / AtCoder floor_sum generalisation) carrying
   (count, Σx^j, Σx^j·floor, Σx^j·floor^2) mod 101001001, x=10^−1 mod M,
   O(log) per evaluation.

## What is NOT here

- All ledgers empty (tasks, attempts, goals, claims, threads, approaches,
  board, weakened, blueprint, entailment, frontier, requests — 0 entries).
- `code/`, `code/lib/`, `code/out/` and every `research/` subfolder: template
  README/INDEX only. No brute.py, no solution.py, no captured output.
- `GOAL.md` and `derived/TASKS.md`: unwritten templates.
- Cognee: recall_memory and recall_scratch for PE1006 / Fibonacci subword /
  Ψ queries return nothing. (remember_memory attempt failed: memory server
  health check timed out — retry storing durable findings once it recovers.)
- Both directives claim verification *outside the container* (dir. 1:
  n=3..12 all lags; dir. 2: k=3,5,8,10,13,17,21,26,34,40,55, plus k=1..150
  gate and Ψ(10) check as next steps). **No in-container reproduction exists.**

## Status

Nothing established, nothing attempted, nothing failed in-container. The first
gate is a naive brute program reproducing Ψ(3)=20302 and
Ψ(10) ≡ 10699667 (mod 101001001); the second is reproducing the directive-2
route against that brute oracle before any full-size run. Modulus note:
gcd(10,101001001)=1, so 10 is invertible mod M (primality of M asserted in
dir. 2, unverified, and not needed for that invertibility).

Full context version: `/workspace/CONTEXT.md` (`Established` / `Asserted but
unverified` / `Gaps` sections).