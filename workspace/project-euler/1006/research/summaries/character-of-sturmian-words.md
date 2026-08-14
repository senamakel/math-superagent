# Character / cyclic complexity of Sturmian words

<!-- source: https://hal.science/hal-01829144v1/document | converted from PDF -->

**Digest replaced.** This is a research note introducing and studying *cyclic complexity*
`c_x(n)` = number of conjugacy classes of length-`n` factors of an infinite word `x`.

## What it establishes (relevant to PE1006)

- **Proposition 6**: A word `x` is Sturmian iff it has exactly `n+1` distinct factors of
  length `n` for every `n >= 0`. This is the classical Morse–Hedlund characterization,
  quoted as the definition of Sturmian word.
- The **Fibonacci word** `F = 010010100100101001...` is the fixed point of the
  substitution `0 -> 01, 1 -> 0`, and is the canonical example of a Sturmian word.
- Proposition 7: two Sturmian words have the same set of factors iff they have the same
  slope (so the factor set depends only on the slope, not on the intercept/finite truncation).

## Bearing on this problem

This source is the governing identification: `S_n` -> limit = infinite Fibonacci word, a
Sturmian word of slope `(3-sqrt5)/2`, hence exactly `k+1` distinct length-`k` factors.
That is the problem's stated FACT. The factor set of the infinite Fibonacci word equals the
set of all "Fibonacci subwords" (finite `S_n` factors) precisely because every length-`k`
factor of the infinite word first appears inside some finite `S_n`, and the finite `S_n`
factors are exactly those of the infinite word. Prop 7 (factors depend only on slope)
justifies treating the finite subwords as the Sturmian factor set.

Full text: `research/sources/character-of-sturmian-words.full.md`.
