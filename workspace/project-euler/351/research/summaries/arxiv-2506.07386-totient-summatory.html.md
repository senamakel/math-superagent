> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/arxiv-2506.07386-totient-summatory.html.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2506.07386v1 | converted from HTML -->

## What is in it

- Computation of the Totient Summatory Function
        - Abstract
  - 1 Introduction
    - 1.1 Conventions
    - 1.2 Overview of the paper
  - 2 Existing algorithms
    - 2.1 The Mertens-first algorithm
  - 3 The Mertens-first algorithm in less space
  - 4 Analysis of Algorithm 13
        - 1.
        - 2.
        - 3.
        - 4.
        - 5.
        - 6.
        - 7.
  - 5 Computational results
  - 6 Supporting lemmas
        - 8.
        - 9.
        - 10.
        - 11.
        - 12.
        - 13.
        - 14.
        - 15.
        - 16.
        - 17.
  - References


## What it claims

An algorithm is devised for computing Φ ⁡ ( n) = ϕ ⁡ ( 1) + ϕ ⁡ ( 2) + ⋯ + ϕ ⁡ ( n) \Phi(n)=\phi(1)+\phi(2)+\cdots+\phi(n) in time Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) and space Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}). The starting point is an existing algorithm based on the Dirichlet hyperbola method and the Mertens function. The algorithm is then used to compute Φ ⁡ ( 10 19) = 30396355092701331435065976498046398788 \Phi(10^{19})=30396355092701331435065976498046398788.

## Statements it makes

Algorithm 1 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 2) \widetilde{\Theta}(n^{1/2}) space [6].

Algorithm 1 has four phases:

Algorithm 1 takes Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time: phases 0–2 combined clearly take Θ ~ ​ ( a) \widetilde{\Theta}(a) time, and phase 3 takes time

Algorithm 1 takes Θ ~ ​ ( n) \widetilde{\Theta}(\sqrt{n}) space: we use three arrays of Θ ⁡ ( n) \Theta(\sqrt{n}) elements each to store the Möbius and Mertens values, the Möbius sieving consumes O ~ ​ ( a) \widetilde{O}(\sqrt{a}) space, and everything else fits in O ⁡ ( 1) O(1) space.

Algorithm 2 An extract from Algorithm 1

Algorithm 3 Algorithm 2, reordered

Algorithm 4 An extract from Algorithm 1

Algorithm 5 Algorithm 4, redone

Algorithm 6 Algorithm 4, redone again

Algorithm 7 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 2) \widetilde{\Theta}(n^{1/2}) space.

Algorithm 8 An extract from Algorithm 7

Algorithm 8 is therefore essentially equivalent to

Algorithm 9 Algorithm 8, redone

Algorithm 10 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 2) \widetilde{\Theta}(n^{1/2}) space.

Algorithm 11 An extract from Algorithm 10

Algorithm 12 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}) space.

Algorithm 13 Compute Φ ⁡ ( n) \Phi(n) in Θ ~ ​ ( n 2 / 3) \widetilde{\Theta}(n^{2/3}) time and Θ ~ ​ ( n 1 / 3) \widetilde{\Theta}(n^{1/3}) space.

Algorithm 14 An extract from Algorithm 13, with x = b x=b

Algorithm 15 An extract from Algorithm 13, with x = ⌊ n ⌋ ≢ 0 ( mod b) x={\left\lfloor\sqrt{n}\right\rfloor}\not\equiv 0\pmod{b}

Algorithm 13 computes Φ ⁡ ( n) \Phi(n) in Θ ⁡ ( n 1 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 2 / 3) \Theta\left(n^{1/3}\cdot(\ln(\ln(n)))^{2/3}\right) space and Θ ⁡ ( n 2 / 3 ⋅ ( ln ⁡ ( ln ⁡ ( n))) 1 / 3) \Theta\left(n^{2/3}\cdot(\ln(\ln(n)))^{1/3}\right) time.

*[digest of a 82040 character source; every section, statement, and proof in full at `research/sources/arxiv-2506.07386-totient-summatory.html.full.md`]*
