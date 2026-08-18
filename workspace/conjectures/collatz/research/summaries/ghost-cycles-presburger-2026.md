> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/ghost-cycles-presburger-2026.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2601.12772v1 | converted from HTML -->

## What is in it

- 2-Adic Obstructions to Presburger-Definable
Characterizations of Collatz Cycles
        - Abstract
  - 1 Introduction
    - 1.1 Motivation
  - 2 Background and Preliminaries
    - 2.1 Presburger Arithmetic and Semilinear Sets
        - Theorem 2.1 (Ginsburg–Spanier Characterization).
        - Definition 2.2 (Semilinear Sets).
        - Lemma 2.3 (Unbounded Fiber Period Obstruction).
        - Proof.
    - 2.2 The 2-adic Integers
  - 3 Parity Patterns and Cycle Equations
        - Definition 3.1 (Cycle-Admissible Pattern).
    - 3.1 Derivation of the Cycle Equation
        - Proposition 3.2.
        - Proof.
  - 4 Ghost Cycles in ℤ 2 \mathbb{Z}_{2}
        - Theorem 4.1 (Existence of Ghost Cycles).
- …


## What it claims

I investigate structural limitations of Presburger-arithmetic–based approaches to the Collatz problem. I show that the Collatz cycle equation admits a unique solution in the 2 2 -adic integers, which I term a *ghost cycle*. These ghost cycles are shown to be genuine periodic orbits of the 2 2 -adic Collatz map, satisfying all local parity constraints.

I prove unconditionally that the divisibility predicate 𝒟 y = { ( x, C) ∈ ℕ 2: ( 2 x − 3 y) ∣ C } \mathcal{D}_{y}=\{(x,C)\in\mathbb{N}^{2}:(2^{x}-3^{y})\mid C\}, which acts as the algebraic necessary condition for integrality, is not semilinear for any fixed number of odd steps y ≥ 1 y\geq 1. This result is established by demonstrating that the fibers of 𝒟 y \mathcal{D}_{y} exhibit unbounded periods, an obstruction to Presburger definability. Consequently, strategies relying solely on Presburger arithmetic or finite automata to define the integrality constraint cannot capture the distinction between ghost cycles and genuine integer cycles. I conclude with a heuristic argument suggesting that because ghost cycles satisfy the algebraic…

## Statements it makes

###### Theorem 2.1 (Ginsburg–Spanier Characterization).

###### Definition 2.2 (Semilinear Sets).

###### Lemma 2.3 (Unbounded Fiber Period Obstruction).

###### Definition 3.1 (Cycle-Admissible Pattern).

###### Proposition 3.2.

###### Theorem 4.1 (Existence of Ghost Cycles).

###### Definition 4.2 (Ghost Cycle).

###### Lemma 5.1.

###### Definition 6.1 ( 2 2 -adic Collatz map).

###### Lemma 6.3 (Forced valuations).

###### Theorem 6.5 (Ghost cycles satisfy iteration dynamics).

###### Corollary 6.6.

Theorem 6.5 establishes that every ghost cycle n 0 n_{0} satisfies T 2 ( ℓ) ​ ( n 0) = n 0 T_{2}^{(\ell)}(n_{0})=n_{0} for ℓ = x + y \ell=x+y, where the iteration follows the prescribed parity pattern with the correct number of halvings at each step. This confirms that ghost cycles are dynamically realized periodic points under repeated application of T 2 T_{2}. ∎

###### Definition 7.1 (General Divisibility Core).

###### Theorem 7.2 (Unconditional Non-Semilinearity).

###### Corollary 7.3.

*[digest of a 33723 character source; every section, statement, and proof in full at `research/sources/ghost-cycles-presburger-2026.full.md`]*
