> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/salez-seven-modular-equations.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/1406.6307v1 | converted from HTML -->

## What is in it

- The Erdős-Straus conjecture
New modular equations
and checking up to N = 10 17 N=10^{17}
        - Abstract
  - 1 Basic formulas
    - 1.1 Reduction
    - 1.2 Rosati’s formulas
        - Proposition 1
    - 1.3 Notations
  - 2 Generalization
    - 2.1 Definitions
    - 2.2 First application
        - Proposition 2
    - 2.3 Modular equations
        - Lemma 1
        - Proposition 3
    - 2.4 Application to the integers
        - Corollary 1
      - Comparison with previous results
      - "Complete" set of modular equations
    - 2.5 Examples
  - 3 Modular sieve
    - 3.1 Modular filters
    - 3.2 Shortened filters
  - 4 Checking of the conjecture
    - 4.1 Choice of the progressions
    - 4.2 Optimized sieve
- …


## What it claims

In 1999 Allan Swett [5] checked (in 150 hours) the Erdős-Straus conjecture up to N = 10 14 N=10^{14} with a sieve based on a single modular equation. After having proved the existence of a "complete" set of seven modular equations (including three new ones), this paper offers an optimized sieve based on these equations. A program written in C++ (and given elsewhere) allows then to make a checking whose running time, on a typical computer 1 1 1 AMD TurionII Dual-Core Mobile M250 ( 64 64 bits, 16 100 16\,100 MIPS)., range from few minutes for N = 10 14 N=10^{14} to about 16 hours for N = 10 17 N=10^{17}.

## Statements it makes

###### Proposition 1

###### Proposition 2

###### Lemma 1

###### Proposition 3

###### Corollary 1

Definition : A sieve is a sorted set of filters.

Definition : A filter 9 9 9 We use the terminology given by Swett. If an integer n ∈ ℕ 0 n\in\mathbb{N}_{0} is such that n % ​ m ∈ F n\%m\in F then n n verifies the conjecture and n n is ”trapped” by the filter. Otherwise n n ”pass through”. modulo m m is a set F F such that for any n ∈ ℕ 0 n\in\mathbb{N}_{0}

Definition: The shortened filter S m ∗ S^{*}_{m} is the set of all x ∈ S m x\in S_{m} such that

*[digest of a 47736 character source; every section, statement, and proof in full at `research/sources/salez-seven-modular-equations.full.md`]*
