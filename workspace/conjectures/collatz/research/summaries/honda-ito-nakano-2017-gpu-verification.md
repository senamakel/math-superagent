> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/honda-ito-nakano-2017-gpu-verification.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://doi.org/10.15803/ijnc.7.1_69 | converted from HTML -->

## What is in it

      - Corresponding author
    - Register with J-STAGE for free!


## What it claims

The main contribution of this paper is to present an implementation that performs the exhaustive search to verify the Collatz conjecture using a GPU. Consider the following operation on an arbitrary positive number: if the number is even, divide it by two, and if the number is odd, triple it and add one. The Collatz conjecture asserts that, starting from any positive number m, repeated iteration of the operations eventually produces the value 1. We have implemented it on NVIDIA GeForce GTX TITAN X and evaluated the performance. The experimental results show that, our GPU implementation can verify 1.31×10 12 64-bit numbers per second. While the sequential CPU implementation on Intel Core i7-4790 can verify 5.25×10 9 64-bit numbers per second. Thus, our implementation on the GPU attains a speed-up factor of 249 over the sequential CPU implementation. Additionally, we accelerated the computation of counting the number of the above operations until a number reaches 1, called delay that is one of the mathematical interests for the Collatz conjecture by the GPU. Using a similar idea, we…

*[digest of a 5641 character source; every section, statement, and proof in full at `research/sources/honda-ito-nakano-2017-gpu-verification.full.md`]*
