# Fibonacci-regular (Zeckendorf-regular) linear representation

```approach
idea: Treat the full state sequence s(k) = (Ψ(k), v_R(k), P1(k), N1(k)) — the state of the
  already-verified extension recurrence Ψ(k+1) = 100(Ψ(k)+v_R(k)²) + 20·P1(k) + N1(k) — as
  a Fibonacci-regular (Zeckendorf-regular) sequence: one with a finite linear representation
  over Zeckendorf numeration. Then Ψ(10^18) mod M is computed by writing 10^18 in Zeckendorf
  and multiplying the digit matrices, in O(log k) matrix products, with no step-by-step
  iteration in k.
mechanism: The Fibonacci word is the fixed point of the primitive Pisot substitution
  0→01, 1→0, so quantities built from its letters/factors and evaluated along the Fibonacci
  scale are computed by a finite transducer reading Zeckendorf digits (Du–Fici–Mousavi–Shallit,
  "Decision algorithms for Fibonacci-automatic words", already in FRONTIER). The run already
  has the step-1 recurrence; the missing piece is the jump-by-Fibonacci-length matrices,
  which is exactly a linear representation. This condition is strictly weaker than a
  constant-coefficient C-finite recurrence — which the run has already refuted for Ψ(k) — so
  the negative result does not apply: Zeckendorf-regular sequences need not satisfy any
  constant-order recurrence in k.
status: proposed
first-step: Build the Zeckendorf kernel of s(k) mod M (the subsequences s(F_i·n + c) induced
  by Zeckendorf digit-removal / digit-append maps) for k = 1..150, and compute its rank over
  Z/M. If the rank stabilizes at a finite value, solve the linear relations to extract the
  linear representation (digit matrices + row/column vectors) and evaluate it at the
  Zeckendorf representation of 10^18. First check it reproduces the oracle terms k=1..30.
```
