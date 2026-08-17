# Sturmian sequence — MathWorld (encyclopedic tier)

<!-- source: https://mathworld.wolfram.com/SturmianSequence.html | converted from HTML -->

Full text: `research/sources/mathworld-sturmian-sequence.full.md`
(also present verbatim in `research/summaries/mathworld-sturmian-sequence.md`).

## What it establishes

- A **Sturmian sequence** is a right-infinite aperiodic binary sequence whose
  factor complexity is `p(n) = n+1` for every positive integer `n`. By the
  Morse–Hedlund theorem this is the smallest possible complexity of an
  aperiodic infinite word.
- It gives the canonical example by the substitution system `0 → 01`, `1 → 0`,
  yielding `0 → 01 → 010 → 01001 → 01001010 → ...`, the Sturmian sequence
  `01001010...`.

## Why it matters here

- The substitution `0 → 01, 1 → 0` is *exactly* the PE1006 construction:
  `S_0 = 0`, `S_1 = 01`, `S_n = S_{n-1} S_{n-2}`. Its limit `01001010...` is
  the infinite Fibonacci word, the source of the problem's "Fibonacci
  subwords". (Note the problem's `S_n` concatenation and this substitution
  generate the same infinite word.)
- Confirms the object under study is the characteristic Sturmian word, tying
  the whole mechanical-word / floor-sum construction to the encyclopedic
  definition.

## Source

Morse, M. and Hedlund, G. A. "Symbolic Dynamics II. Sturmian Trajectories."
*Amer. J. Math.* **62**, 1-42, 1940. https://doi.org/10.2307/2371441.

Status: encyclopedic/sourced statement.
