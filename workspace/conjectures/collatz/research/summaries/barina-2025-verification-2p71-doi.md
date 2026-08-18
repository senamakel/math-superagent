> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/barina-2025-verification-2p71-doi.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://doi.org/10.1007/s11227-025-07337-0 | converted from HTML -->

## What is in it

- Improved verification limit for the convergence of the Collatz conjecture
  - Abstract
    - Similar content being viewed by others
    - [Convergence verification of the Collatz problem][8]
    - [Observations from Parallelising Three Maximum Common (Connected) Subgraph Algorithms][9]
    - [Computational Errors of the Extragradient Method for Equilibrium Problems][10]
    - Explore related subjects
  - 1 Introduction
  - 2 Related work
  - 3 Algorithms
    - 3.1 Baseline testing
    - 3.2 Sieve \(3^k\)
    - 3.3 Sieve \(2^k\)
    - 3.4 Solving congruence classes concurrently
  - 4 Distributed computing
  - 5 Evaluation
  - 6 Results
  - 7 Conclusion
  - Notes
  - References
  - Acknowledgements
- …


## What it claims

This article presents our project, which aims to verify the Collatz conjecture computationally. As a main point of the article, we introduce a new result that pushes the limit for which the conjecture is verified up to \(2^{71}\). We present our baseline algorithm and then several sub-algorithms that enhance acceleration. The total acceleration from the first algorithm we used on the CPU to our best algorithm on the GPU is \(1\,335\times\). We further distribute individual tasks to thousands of parallel workers running on several European supercomputers. Besides the convergence verification, our program also checks for path records during the convergence test. We found four new path records.

## Statements it makes

**Algorithm 1**

**Algorithm 2**

*[digest of a 41711 character source; every section, statement, and proof in full at `research/sources/barina-2025-verification-2p71-doi.full.md`]*
