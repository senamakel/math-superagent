# Attack coupling-half: the conditionally-iid coupling optimization

```thread
id: coupling-half
question: Does the finite-dimensional conditionally-iid coupling optimization
  (Yu arXiv:2212.00658; Liu arXiv:2306.08824) certify H(A∨B) > H(A) at density
  1/2 — i.e. reach c = 1/2 — or does it exhibit an extremal μ that blocks 1/2?
status: dead
rests-on: yu-record-0-38234, liu-0-38271, sawin-above-barrier
blocked-by: none
next: |
  (1) Open research/sources/yu-dimension-free-bounds-2023.full.md, find Yu's
      finite-dimensional optimization as stated, and write it verbatim in a
      note — the objective, the constraint set, and the dimension of the
      auxiliary variable — before writing any code.
  (2) Implement it. Reproduce 0.38234 as a correctness check. If the
      implementation does not reproduce 0.38234, the implementation is wrong,
      and that is the finding to fix — not to route around.
  (3) Only then push the same optimization toward c = 1/2 and report which
      happens: it certifies H(A∨B) > H(A) at density 1/2, or it exhibits the
      extremal μ blocking it. Exhibiting the blocking μ is GOAL.md result
      class 3 — success, not failure.
```

## Why this direction

`research/backward/uc-via-entropy-coupling.md` reduces UC to one analytical gap
(`G-coupling-half`): if every coordinate density is `< 1/2`, there is a
conditionally-iid coupling (A,B) of (μ,μ) with `H(A∨B) > H(A)`. The iid
sub-instance is refuted (barrier `(3−√5)/2`); the conditionally-iid class is
the one whose finite-dimensional optimization already produced the current
record constants. This thread is the implementation of that gap: run Yu's
optimization to 0.38234 (correctness), then push the constant toward 1/2.

The deliverable is either the UC-entailing inequality at 1/2, or the extremal
μ where the class optimum stays below 1/2 — a proved barrier for this coupling
class (GOAL result class 3), and the realistic outcome.

## What would falsify it

A faithful implementation that reproduces 0.38234 but whose optimum saturates
at a constant strictly below 1/2 — with the extremal μ exhibited — shows this
coupling class cannot reach 1/2. That is a barrier for the class, not a
refutation of the direction; the gap `G-coupling-half` would then need a larger
coupling class. If the implementation cannot be made faithful (a stated step of
the paper cannot be turned into code), the task closes with that step named.
