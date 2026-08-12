# Approach: first-event dynamic programming

```approach
idea: Recursion by conditioning on the chronologically first event (earliest bump or finish)
mechanism: >
  The race is a sequence of elimination events. At any moment, each surviving boat
  has a finish time (L-p_j)/v_j and pairwise catch times 40(b-a)/(v_a-v_b).
  The first event to occur — minimum of all these times — eliminates one boat
  (bumper goes OUT on a bump; finisher is removed on a finish) and the remaining
  n-1 boats continue under the torpids rules with adjusted "next ahead" pointers.
  Conditioning on which boat triggers the first event and at what time yields an
  n-fold integral recurrence for p(n,L). The event-time minima are minima of
  inverse-exponential and Laplace-type random variables; their distributions and
  the conditional distributions of the survivors are tractable by the memoryless
  property and order-statistic theory. The key is that after one elimination, the
  remaining system is an (n-1)-boat torpids race with modified initial positions
  (the eliminated boat is transparent), so the recurrence closes.
status: proposed
first-step: >
  For n=3, write the explicit 6-fold integral (over v_1,v_2,v_3) partitioned by
  which of the 5 possible first events occurs (A bumps B, B bumps C, A finishes,
  B finishes, C finishes — A cannot bump C directly because B is in between and
  not yet eliminated). Verify that summing the sub-integrals reproduces p(3,160)=56/135.
  Then derive the general recurrence formula.
```