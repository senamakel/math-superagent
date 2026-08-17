# Morse–Hedlund theorem — MathWorld (encyclopedic tier)

<!-- source: https://mathworld.wolfram.com/Morse-HedlundTheorem.html | converted from HTML -->

Full text: `research/sources/mathworld-morse-hedlund-theorem.full.md`
(also present verbatim in `research/summaries/mathworld-morse-hedlund-theorem.md`).

## What it establishes

The **Morse–Hedlund theorem**, the primary source of the factor-complexity
statement PE1006 relies on:

- A right-infinite word is *ultimately periodic* iff its factor complexity
  satisfies `p_w(n) ≤ n` for some positive integer `n`.
- A bi-infinite word is *periodic* iff the same inequality holds for some `n`.
- Equivalently, every aperiodic right-infinite or bi-infinite word satisfies
  `p_w(n) ≥ n+1` for *every* `n ≥ 1`. This lower bound is sharp: the aperiodic
  binary words with `p_w(n) = n+1` for all `n` are exactly the **Sturmian
  sequences**.

## Why it matters here

- It is the cited authority behind the library's claim
  `governing-factor-complexity`: "A Sturmian word has exactly k+1 distinct
  factors of length k". That is exactly the problem statement's "for each
  positive integer k there are only k+1 different Fibonacci subwords of length
  k".
- It fixes the minimal-complexity framing: k+1 is the *smallest possible*
  complexity of an aperiodic word, and Sturmian words are precisely the words
  attaining it.

## Source

Morse, M. and Hedlund, G. A. "Symbolic Dynamics II. Sturmian Trajectories."
*Amer. J. Math.* **62**, 1-42, 1940. https://doi.org/10.2307/2371441.
(The 1940 paper itself is paywalled/jSTOR; this MathWorld entry is the
free encyclopedic statement held on disk.)

Status: encyclopedic/sourced statement. Not a proof of the theorem.
