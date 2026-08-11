# Goal

Compute S(n) for the bit-deletion partisan game (Dr. One / Dr. Zero), the value
S(10^5) for Project Euler 882.

## Problem (from /workspace/problem.md)

Board starts with k copies of each k (k=1..n). Dr. One (Left) deletes a 1-bit
from a number's binary string; Dr. Zero (Right) deletes a 0-bit. Leading zeros
of the result are dropped; a string that becomes empty is the value 0; nobody
can move on 0. A player unable to move loses (normal play). Zero wins iff One
cannot move on One's turn. Only Zero may skip (pass the turn back to One,
counting one skip). S(n) = minimal total number of skips Zero needs to force a
win.

Worked examples (test oracle): S(2)=2, S(5)=17, S(10)=64. Given example game for
n=2 uses 2 skips.

## Governing theory (dyadic CGT Numbers, Simplicity Rule)

- Strictly partisan ⇒ Sprague–Grundy does not apply.
- Each single-number subgame is a canonical dyadic **Number**:
  g(0)=0; g(k) = { g(j) : j a 1-deletion of k  |  g(j) : j a 0-deletion of k }.
  All children j < k, so short. For every k≤10^5 the position is a genuine
  Number (max Left < min Right, asserted by solution.py, no violation).
- **Simplicity Rule** (Fenner–Rogers 2015, arXiv:1505.07416): g(k) = simplest
  dyadic rational strictly between max(Left) and min(Right).
- Board is a disjunctive sum of k copies of each k ⇒ G(n) = Σ_{k≤n} k·g(k).
- A Right skip adds −1; Zero (Right) wins iff G(n)−m ≤ 0 ⇒ **S(n) = ceil(G(n))**.

## Completion criteria (all met this run)

- [x] solution.py computes g(k) for k=1..100000, asserts every k is a Number
      (first violating k = none), reproduces the oracle
      S(1,2,3,4,5,10) = 1,2,8,9,17,64 — ALL MATCH.
- [x] Real-game minimax oracle (code/brute.py, code/fastbrute.py) reproduced
      S(1..5) = 1,2,8,9,17 on the true bit game (n=1..3 confirmed by an
      explicit independent move search); statement S(2)=2, S(5)=17 match.
- [x] Full-size value: G(10^5) = 517756101446417/32768,
      **S(10^5) = ceil(G(10^5)) = 15800662276**.
- [x] Independent verification: three fully separate code paths agree exactly
      on G(10^5) and S(10^5) — solution.py (forward sweep + toolkits
      simplest_dyadic), verify_dyadic.py (independent sweep), and
      indep_check.py (direct recursive surreal eval + from-scratch
      birthday-ordered simplest-dyadic). Exact integer ceiling check confirms
      the fraction's ceiling directly.
- [x] answer file /workspace/dyadic_answer.txt written:
      "S(100000)=ceil(G(100000))= 15800662276".

## Caveat

S(n)=ceil(G(n)) rests on the CGT rule that each single-number subgame is a
canonical dyadic Number and a Right skip is worth −1. Corroborated at every
value the real-game brute oracle can reach (n≤5) and all three statement
examples (n=2,5,10), but the true S(n) for n>10 (including 10^5) is not
reachable by that enumeration oracle.
