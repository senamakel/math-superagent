> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/christoffel-words-collatz-2026.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2607.24844v1 | converted from HTML -->

## What is in it

- Christoffel Words as Extremal Structures in Collatz Dynamics
        - Abstract
  - 1 Introduction
  - 2 Parity sequences
  - 3 Rotations
        - Remark 3.1.
  - 4 Christoffel words
        - Definition 4.1.
  - 5 Local transformations
        - Proposition 5.1.
        - Proof.
        - Proposition 5.2.
        - Proof.
  - 6 Combinatorial structure
        - Lemma 6.1.
        - Proof.
        - Lemma 6.2.
        - Proof.
        - Theorem 6.3 (Position comparison).
        - Proof.
        - Theorem 6.4 (Connection by transpositions).
        - Proof.
  - 7 Main result
        - Proposition 7.1.
        - Proof.
        - Corollary 7.2.
        - Proof.
        - Theorem 7.3 (Main theorem).
- …


## What it claims

We study the combinatorial structure of parity sequences associated with the accelerated Collatz map with the goal of identifying extremal configurations and relating them to the existence of periodic orbits. To each finite sequence of an orbit, we associate a binary word whose ones encode the odd iterates, and we introduce a functional C ⁡ ( d) C(d) on such words which provides an explicit expression for the iterates and characterizes possible periodic cycles. We define a natural rotation action on binary words, compatible with the cyclic structure of periodic orbits, and consider the functional C min ​ ( d) C_{\min}(d) as a canonical representative of each rotation class. In this setting, we formulate and solve a discrete optimization problem on the set of binary words of fixed length and prescribed density.

We prove that Christoffel words are, up to rotation, the unique maximizers of C min ​ ( d) C_{\min}(d) on D N, r D_{N,r}, the set of binary words of length N N with exactly r r ones, thereby establishing a direct connection between the dynamics of the Collatz problem and the…

## Statements it makes

###### Definition 4.1.

###### Proposition 5.1.

###### Proposition 5.2.

Proposition 5.2 shows that moving a one to the right increases the value of C C. Consequently, configurations that minimize the functional tend to concentrate the ones in earlier positions. Moreover, it induces a partial order on the set of binary words compatible with the distribution of the ones, in the spirit of recent work on parity vectors [12].

###### Lemma 6.1.

###### Lemma 6.2.

###### Theorem 6.3 (Position comparison).

###### Theorem 6.4 (Connection by transpositions).

Theorem 6.4 shows that d N, r chr d^{\mathrm{chr}}_{N,r} can be reached from d c d^{c} by local transformations that progressively redistribute the ones in a more balanced way. This reveals the compatibility between the partial order induced by 10 → 01 10\to 01 transpositions and the structure of Christoffel words.

###### Proposition 7.1.

Proposition 7.1 shows that C C grows in a controlled manner as the length increases; the following corollary translates this into a monotonicity property of the quantity characterizing cycles.

###### Corollary 7.2.

Corollary 7.2 shows that as the length increases with the number of odd iterates fixed, the quantity associated with the possible existence of cycles decreases strictly. In particular, longer configurations are progressively less favourable for the existence of cycles.

###### Theorem 7.3 (Main theorem).

Theorem 7.3 shows that Christoffel words are not only combinatorially balanced, but also constitute the unique extremal configurations for the functional C min C_{\min}. This establishes a direct link between the dynamics of the Collatz problem and classical structures in combinatorics on words, showing that optimal configurations are governed by balanced distributions of the ones. To the best of our knowledge, this is the first result identifying Christoffel words as extremal configurations for a functional arising directly from Collatz dynamics.

###### Theorem 8.1.

Theorem 8.1 shows that the density of odd iterates in a periodic orbit is strongly constrained. The bound N ≤ 2 ​ r N\leq 2r is known in the literature [3]; what is new here is that…


*[further statements in the full text]*

*[digest of a 50470 character source; every section, statement, and proof in full at `research/sources/christoffel-words-collatz-2026.full.md`]*
