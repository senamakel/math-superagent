# Fold: skip / pass mechanism

The Zero-skip as a zugzwang escape and a loopy self-loop resolved as a DP
fixpoint.

- [[pass_waiting]] — Larsson–Nowakowski–Santos 2015 arXiv:1505.01907: primary,
  rigorous theory of passes/waiting moves (the pass as zugzwang/tempo tool,
  order-embedding into normal-play when passes do no harm). Structural analogue
  of the problem's zero-skip; makes the earlier Wikipedia-level picture
  citable. Caveat: our skip costs budget, so S(n) still comes from the DP.
- [[zugzwang]] — One is forced to consume a 1-bit each turn; "passing, if
  allowed, would be best" is the classical description of the skip.
- [[loopy]] — the skip is a self-loop in the state graph making the DP a
  fixpoint; the game is a stopper (moves strictly decrease A or B), so no
  forced tie and a finite S(n) exists.

What this yields: justification that a finite minimal skip budget S(n) exists
and that the DP is a well-defined least fixpoint.
