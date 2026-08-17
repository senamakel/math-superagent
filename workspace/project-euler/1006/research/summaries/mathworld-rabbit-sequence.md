# MathWorld — *Rabbit Sequence*

Source: https://mathworld.wolfram.com/RabbitSequence.html
Summary only; no full text saved separately (short page).

## What this source establishes

Descriptive encyclopedic entry on the **rabbit sequence**, distinct from the
problem's word but trivially related:

- Rabbit sequence (0→1, 1→10 growth rule, or 1→10, 0→1 population model):
  1 0 1 1 0 1 0 1 1 0 …; the problem's Fibonacci word S = 0100101001001… is the
  same sequence with digits swapped (0↔1) and shifted by one —
  S(0)=0, S(1)=1, S(2)=0 whereas rabbit starts 1,0,1. (Also stated on the
  Wikipedia Fibonacci-word page: "differs from the Fibonacci word only trivially,
  by swapping 0s for 1s and shifting by one".)
- Binaries: the limiting sequence as a binary fraction 0.1011010110110…₂ is
  the **rabbit constant** (A005614).
- Terms as integers: 1, 2, 5, 22, 181, … (A005203) via
  a(n) = a(n−1)·2^{F(n−1)} + a(n−2).

## What it implies for PE1006

1. **Convention trap, third occurrence:** several sources (this one,
   Sivasankar–Rama, Wikipedia's slope-1/φ statement) describe the *rabbit*
   (complement) word. The problem's S is the *other* digit convention. Any
   factor-set, digit formula, or closed form taken from a rabbit-sequence
   source must be digit-complemented before comparing to the problem's factors.
2. MathWorld itself contributes nothing further to Ψ(k): no factor enumeration,
   no mechanical-word digit rule, no sums of squares.

## Claims anchored here

None directly (corroborates the convention warning in `governing-sturmian` and
`mechanical-word-digit-rule`).