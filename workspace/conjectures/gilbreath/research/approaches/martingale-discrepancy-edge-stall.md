```approach
idea: martingale-discrepancy-edge-stall (withdrawn — mechanism was false)
mechanism: |
  WITHDRAWN before grounding. The proposed mechanism claimed the boundary edge
  x_k is a martingale that XORs ONE fresh halved-gap parity bit per erosion
  step (x_{k+d} = x_{k+d-1} XOR fresh bit), and hence is i.i.d.-like with
  discrepancy/Azuma bounds. This is FALSE.

  The correct recurrence (verified by hand for a length-3 block h = h_1 h_2 h_3
  with edge h_3, using the proved rule90-interior-xor formula
  e_d = XOR_{j=0}^d [C(d,j) mod 2] h_{b_k-d+j}) is

      e_0 = h_3,
      e_1 = h_2 XOR h_3,
      e_2 = h_1 XOR h_3,

  i.e. e_{d+1} is NOT e_d XOR a single fresh bit. The edge couples to its LEFT
  neighbour (two-tap), and the "reveal one bit per step" filtration does not
  make x_k a martingale in any straightforward way. The i.i.d. law of large
  numbers that the proposal wanted to replace cannot be replaced by Doob/Azuma
  on this object, because the increments are not conditionally zero-mean under
  the natural filtration.

  The surviving, correct object — the anti-diagonal edge sequence e_d, its
  zero-runs and its partial sums — is already the subject of the renewal
  proposal (renewal-process-edge-flip-hitting-time, Route A) and the
  Walsh-Hadamard item. Do not resurrect this file.
precedent: |
  none — self-corrected by hand computation of the anti-diagonal formula before
  grounding. The correction is recorded so the false martingale claim is not
  re-proposed under a new name.
status: refuted
killed-by: |
  The "edge XORs one fresh bit per step" martingale claim is false: the edge
  sequence is e_d = XOR_{j=0}^d [C(d,j) mod 2] h_{b_k-d+j} (two-tap coupled
  recurrence), not a running XOR of independent fresh bits, so no Doob/Azuma
  martingale bound applies at the "one bit per step" filtration.
```
