# Goal

Compute S(n) for the bit-deletion partisan game (Dr. One / Dr. Zero) described
in problem.html, using two independent implementations:

- TASK A: `/workspace/brute.py` — naive minimax on the REAL game (multiset of
  numbers, whose turn, skip count budget). Print S(n) for n=1..8. For tiny
  n=1,2,3 verify with a fully explicit minimax search over the real-bit game.
- TASK B: the same DP on the reduced counting game (A,B) where A = total # of
  1-bits, B = total # of 0-bits; a One-move is (A-1,B), a Zero-move is
  (A,B-1), skip passes without change. Verify S(2)=2, S(5)=17, S(10)=64. Print
  S(n) for n=1..10 and the DP tables need_oneturn(A,B) / need_zeroturn(A,B)
  for A,B in 0..12.

Completion criteria:
- brute.py runs and prints S(1..8) for the real game.
- counting DP runs and reproduces S(2)=2, S(5)=17, S(10)=64.
- Real-game S(n) and counting-game S(n) agree wherever both run.
- Report the S(n) table for n=1..10, which examples matched, and the DP grid.
