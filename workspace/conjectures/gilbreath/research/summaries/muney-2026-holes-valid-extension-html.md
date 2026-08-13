> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/muney-2026-holes-valid-extension-html.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2606.23721v2 | converted from HTML -->

## What is in it

- Holes in Valid-Extension Sets of Finite Gilbreath Sequences
        - Abstract
  - 1 Introduction
    - 1.1 Note on a previously claimed interval characterization
    - 1.2 Notation guide
    - 1.3 Summary of main results
    - 1.4 Related work
  - 2 The exact extension criterion
        - Example 1.
        - Proposition 2 (Iterated absolute-value criterion).
        - Proof.
        - Corollary 3 (Candidate bound).
        - Proof.
  - 3 Parity
        - Lemma 4.
        - Proof.
        - Corollary 5.
        - Proof.
  - 4 Candidate set, holes, and defect
        - Definition 6.
        - Lemma 7.
        - Proof.
        - Definition 8.
  - 5 The signed-sum set
        - Example 9 (The signed sums need not fill the candidate interval).
- …


## What it claims

Given a finite sequence of integers, form its difference triangle by repeatedly taking absolute differences of consecutive entries. We call the sequence *Gilbreath*if the leftmost entry of every row below the top is 1 1. The Gilbreath conjecture, which remains open, asserts that every initial segment of the primes is a Gilbreath sequence.

This paper studies the local extension problem: given a Gilbreath sequence, which integers can be appended to it while preserving the Gilbreath property? We call the set of such admissible values the *valid-extension set*of the sequence. A previously proposed characterization in the literature predicts that this set always fills a natural parity interval around the last term. We show that this fails in general: the valid-extension set can have interior holes, with the smallest failure occurring at length 5 5 for the sequence ( 2, 3, 5, 9, 15) (2,3,5,9,15).

The paper develops a corrected extension set theory. We give an exact criterion for membership in the valid-extension set, an algorithm that computes it, and a sharp condition determining…

## Statements it makes

###### Proposition 2 (Iterated absolute-value criterion).

###### Corollary 3 (Candidate bound).

###### Lemma 4.

###### Corollary 5.

###### Definition 6.

###### Lemma 7.

###### Definition 8.

###### Theorem 11 (Classical completeness criterion).

###### Theorem 12 (Subset-sum reformulation).

###### Corollary 13.

Theorem 12 isolates the classical part of the problem. The signed-sum set forgets the order in which the absolute values are evaluated: it only remembers the multiset of fold sizes. By Brown’s criterion, the question S ± = C S S_{\pm}=C_{S} is answered by sorting the weights in W S W_{S} and checking whether each new sorted weight is at most one plus the sum of the preceding sorted weights.

###### Proposition 14 (Hierarchy of completeness conditions).

###### Theorem 15 (Endpoint validity).

###### Theorem 16 (Reflection symmetry).

###### Definition 17.

###### Proposition 18 (Reverse-tree characterization).

###### Theorem 20 (Interval-completeness criterion).

Claim. Let T ~ ⊆ { 0, 1, …, L } \widetilde{T}\subseteq\{0,1,\ldots,L\} and a ≥ 0 a\geq 0. Then Q a ​ ( T ~) = { 0, 1, …, a + L } Q_{a}(\widetilde{T})=\{0,1,\ldots,a+L\} if and only if T ~ = { 0, 1, …, L } \widetilde{T}=\{0,1,\ldots,L\} and a ≤ L a\leq L.

###### Corollary 22.

###### Corollary 23.

###### Theorem 24 (First hole).

###### Theorem 25 (Minimum extension width).

###### Lemma 26.

###### Lemma 27.

###### Lemma 28.

###### Theorem 29 (Extension width of the doubling sequence).

###### Conjecture 30 (Maximum width).

###### Definition 31.

###### Lemma 33.

###### Lemma 34 (Extremes and structure of D n D_{n}).

###### Theorem 35 (Exponentially many components).

###### Corollary 36.

*[digest of a 109614 character source; every section, statement, and proof in full at `research/sources/muney-2026-holes-valid-extension-html.full.md`]*
