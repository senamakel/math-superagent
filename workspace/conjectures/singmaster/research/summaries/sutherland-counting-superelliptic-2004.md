> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/sutherland-counting-superelliptic-2004.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2004.10189v5 | converted from HTML -->

## What is in it

- Counting points on superelliptic curves in average polynomial time Thanks: The author was…
        - Abstract.
  - 1. Introduction
        - 1.
        - Remark 2.
        - 3.
  - 2. The Cartier operator
        - Definition 4.
        - Definition 5.
        - Lemma 6.
        - Proof.
        - Example 7.
        - 8.
        - Proof.
        - Remark 9.
  - 3. Linear recurrences
        - Remark 10.
  - 4. Translation tricks
        - Lemma 11.
        - Proof.
        - Remark 12.
        - Lemma 13.
        - Proof.
        - Remark 14.
        - Remark 15.
  - 5. Accumulating remainder trees and forests
        - 16 [22].
        - Corollary 17.
        - Proof.
  - 6. Algorithms
- …


## What it claims

We describe the practical implementation of an average polynomial-time algorithm for counting points on superelliptic curves defined over 𝐐 \mathbf{Q} that is substantially faster than previous approaches. Our algorithm takes as input a superelliptic curve y m = f ⁡ ( x) y^{m}=f(x) with m ≥ 2 m\geq 2 and f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] any squarefree polynomial of degree d ≥ 3 d\geq 3, along with a positive integer N N. It can compute #​ X ​ ( 𝐅 p) \#X(\mathbf{F}_{p}) for all p ≤ N p\leq N not dividing m ​ lc ⁡ ( f) ​ disc ​ ( f) m\operatorname{lc}(f)\operatorname{disc}(f) in time O ⁡ ( m ​ d 3 ​ N ​ log 3 ​ N ​ log ⁡ log ⁡ N) O(md^{3}N\log^{3}N\log\log N). It achieves this by computing the trace of the Cartier–Manin matrix of reductions of X X. We can also compute the Cartier–Manin matrix itself, which determines the p p -rank of the Jacobian of X X and the numerator of its zeta function modulo p p.

In memory of [Peter L. Montgomery][3].

## Statements it makes

###### Definition 4.

###### Definition 5.

###### Lemma 6.

###### Lemma 11.

###### Lemma 13.

###### Corollary 17.

*[digest of a 84523 character source; every section, statement, and proof in full at `research/sources/sutherland-counting-superelliptic-2004.full.md`]*
