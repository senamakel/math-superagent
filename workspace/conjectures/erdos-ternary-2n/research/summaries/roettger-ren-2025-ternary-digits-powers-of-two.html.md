> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/roettger-ren-2025-ternary-digits-powers-of-two.html.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2511.03861v1 | converted from HTML -->

## What is in it

  - 1 Frequency of Ternary Digits of Powers of Two
        - Lemma 1.
        - Proof.
  - 2 Computational Evidence for Uniform Distribution
    - 2.1 Methodology
    - 2.2 Results for Aggregate Digit Frequencies
    - 2.3 Aggregate Digit String Frequencies
    - 2.4 Variance and Standard Deviation
    - 2.5 Non-aggregate digit tallies
  - 3 Uniform Distribution and Benford’s Law
        - Theorem 1 (Benford’s Law for ternary digits).
        - Proof.
        - Theorem 2 (Average count in leading digits).
        - Proof.
        - Theorem 3 (Uniform distribution of frequency in leading digits).
        - Proof.
        - Remark 1.
  - 4 A Special Case of Baker’s Theorem and its Implications
- …


## What it claims

The ternary digits of 2 n 2^{n} are a finite sequence of 0s, 1s, and 2s. It is a natural question to ask whether the frequency of any string of 0s, 1s, and 2s in this sequence approaches the same limit for all strings of the same length, as the exponent n n approaches infinity ( Uniform Distribution in the limit).

Currently the answer to this question is unknown. Even a much weaker conjecture by Erdös is still open. But we present computational results (up to n = 10 6 n=10^{6}) supporting uniform distribution in the limit.

In this context, we discuss implications of Benford’s Law and a special case of Baker’s Theorem.

Then we investigate the infinite sequence of ternary digits of log 3 ⁡ ( 2) \log_{3}(2). There are analogous questions about the distribution of strings of 0s, 1s, and 2s in that sequence. If there is uniform distribution in the limit, then log 3 ⁡ ( 2) \log_{3}(2) is called normal to base 3.

In the absence of definitive results, we can offer again computational evidence from the first 10 6 10^{6} ternary digits of log 3 ⁡ ( 2) \log_{3}(2), strongly supporting the…

## Statements it makes

###### Lemma 1.

###### Theorem 1 (Benford’s Law for ternary digits).

###### Theorem 2 (Average count in leading digits).

###### Theorem 3 (Uniform distribution of frequency in leading digits).

###### Theorem 4 (Baker 1975 – very special case).

###### Corollary 1 (Consequence of Baker’s Theorem).

Corollary 1 does not contradict part c) of Remark 1, but it narrows down the possibilities for the strings of digits after the leading digit of 2 n 2^{n}.

###### Definition 1.

*[digest of a 38904 character source; every section, statement, and proof in full at `research/sources/roettger-ren-2025-ternary-digits-powers-of-two.html.full.md`]*
