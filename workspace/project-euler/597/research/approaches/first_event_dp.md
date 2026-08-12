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
status: refuted
killed-by: >
  The crux that closes the recurrence is the memoryless property, and it does not
  hold. Finish times (L-p_j)/v_j with v_j~Exp(1) are INVERSE-EXPONENTIAL with a
  NON-CONSTANT hazard (it grows then falls), so they are not exponentially
  distributed clocks and have no memoryless property: conditioning on the first
  event does not leave the survivors as an independent, identically-distributed
  (n-1)-boat torpids game. This is claim `finish-line-breaks-exponential-clock-machinery`
  in the library ledger, and it is independently confirmed by the general
  inverse-exponential distribution literature (Oguntunde & Adejumo 2014; see
  precedent). It is also measured directly: the run's own `research_recursion_test.py`
  tested precisely this first-event/argmin-style recursion and refuted it at every
  level — value-level exact p(3,160)=2/3 (truth 56/135), p(4,400)=5/6 (truth
  0.5108); per-vector n=2,L=160 counterexample [0.89157,0.33049] (oracle odd,
  recursion even); and the two crux claims it needs both fail — "left/right
  subranges decouple" fails 20177/300000 and "cross=|L||R|" holds only ~49%.
  Mechanism-level diagnosis: a bump can be PRE-EMPTED by a finish, so the bump
  order is not a compete-with-withdrawn-exponential draw and left/right subranges
  do not decouple.
note: >
  The n=3 partitioned-integration first-step is fine (it reproduces p(3,160)=56/135
  exactly — that is already the run's verified oracle), so the first event
  conditioning itself is a valid enumeration. The refutation is of the closure
  step, i.e. of any claim that the first-event recursion is polynomial in n.
  As an exact enumeration it is no cheaper than the arrangement: the number of
  distinct event sequences is the number of arrangement regions, which grows
  super-exponentially with n (n=4 -> 1202, n=5 -> ~13750), so even a correct
  first-event recursion cannot reach n=13.
precedent: >
  - claim `finish-line-breaks-exponential-clock-machinery`
    (research/torpids_parity_ballistic_aggregation_survey.md)
  - claim `torpids-bump-graph-forest` (research/torpids_parity_ballistic_aggregation_survey.md)
  - run refutation: code/research_recursion_test.py
  - Oguntunde & Adejumo 2014, "The Transmuted Inverse Exponential Distribution",
    https://doi.org/10.14419/ijasp.v3i1.3684  (inverse-exponential has non-constant,
    non-memoryless hazard)
  - inverse-exponential / general inverted-lifetime literature (PMID 35692408 /
    PMC9141993), all confirming non-constant (non-memoryless) hazard of inverted
    exponential lifetimes.
```
