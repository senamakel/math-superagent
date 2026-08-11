# Goal

Compute S(n) for the bit-deletion partisan game (Dr. One / Dr. Zero) described
in problem.html, ultimately S(10^5).

Two earlier task paths (TASK A real-game brute, TASK B (A,B) counting DP) were
completed and recorded; the (A,B) counting surrogate was REFUTED (see MEMORY).

## Completed: dyadic CGT solution (this run)

The governing structural hypothesis (research/CONTEXT.md, code/dyadic.py):
each single number k is a canonical dyadic "Number" g(k) with
g(0)=0, g(k)=simplest dyadic strictly between max(1-deletion values) and
min(0-deletion values).  Board value G(n)=Σ_{k=1..n} k·g(k), S(n)=ceil(G(n)).

Results (all in /workspace/solution.py, answer in /workspace/dyadic_answer.txt):
- Every k in 1..100000 is a Number (max(Left) < min(Right); no violation).
- S_ceil(n)=ceil(G(n)) n=1..20 matches the real-game oracle for every value
  available: S(1,2,3,4,5,10) = 1,2,8,9,17,64 — ALL MATCH.
- **S(100000) = ceil(G(100000)) = 15800662276**
  (G(100000)=517756101446417/32768, floor 15800662275, remainder 19217).
- simplest_between toolkit validated against an independent birthday oracle
  (166 intervals, 0 mismatches); g(1..8) hand-checked values reproduced.
- Final answer cross-checked by an independent implementation (reproduces
  G(1..12)) and by exact integer arithmetic.

Completion criteria met: script runs to n=100000, prints S(100000), writes the
two-line answer file, and every available real-oracle value is reproduced.
