> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/alekseyev_diophantine_sigma_html.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2601.17832v1 | converted from HTML -->

## What is in it

- Computing bounded solutions to linear Diophantine equations with the sum of divisors
        - Abstract.
  - 1. Introduction
  - 2. Notation
  - 3. Method outline
    - 3.1. Shortcuts
        - Theorem 3.1 (OEIS [14]).
    - 3.2. Pruning with prime wheel
        - Theorem 3.2.
        - Proof.
        - Theorem 3.3.
        - Proof.
    - 3.3. Case of odd σ \sigma
    - 3.4. Case of gcd ⁡ ( a ′, c ′) > 1 \gcd(a^{\prime},c^{\prime})>1
  - 4. SageMath implementation
    - 4.1. RES framework
    - 4.2. Configurations reduction
    - 4.3. MapReduce parallelization
    - 4.4. Additional constraints
    - 4.5. Solutions above U U
    - 4.6. Availability
  - 5. Applications
    - 5.1. Numbers with a small abundance
- …


## What it claims

We propose an efficient computational method for finding all solutions n ≤ U n\leq U to the Diophantine equation a ​ σ ​ ( n) = b ​ n + c a\sigma(n)=bn+c, where integer coefficient a, b, c a,b,c and an upper bound U U are given. Our method is implemented in SageMath computer algebra system within the framework of recursively enumerated sets and natively benefits from MapReduce parallelization. We used it to discover new solutions to many published equations and close gaps in between the known large solutions, including but not limited to hyperperfect and f f -perfect numbers, as well as to significantly lift the existence bounds in open questions about quasiperfect and almost-perfect numbers.

## Statements it makes

###### Theorem 3.1 (OEIS [14]).

###### Theorem 3.2.

###### Theorem 3.3.

*[digest of a 44423 character source; every section, statement, and proof in full at `research/sources/alekseyev_diophantine_sigma_html.full.md`]*
