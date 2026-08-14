> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kulkov-dirichlet-convolution-fast-prefix-sums.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://codeforces.com/blog/entry/117635 | converted from HTML -->

## What is in it

- | User | Rating |
- | User | Contrib. |
    - [adamant's blog][88]
    - Dirichlet convolution
      - Hyperbola method
      - Choosing a better splitting point
      - Adding precomputation
      - Adding even more precomputation
    - Dirichlet inverse
    - Further reading
- Returns a list of tuples (L, R, t)
# such that n//k = t <=> t in [L, R]
def…
- Returns a list of tuples (L, R, t)
# such that n//k = t <=> t in [L, R]
def…


## What it claims

We need to compute a prefix sum of the [Dirichlet convolution][97] $$$(f * g)(n)$$$. In this article, we will consider some general methods, and show how to do so in $$$O(n^{2/3})$$$ if we can compute prefix sums of $$$F(n)$$$ and $$$G(n)$$$ in all possible values of $$$\lfloor n/k \rfloor$$$ in this complexity.

- **Part 1: Fast prefix sum computation**
- **[Part 2: Dirichlet series and prime counting][98]**

[e cnerwala][99] previously [mentioned][100] that it is possible, but did not go into much detail. There is also a [blog][101] by [Nisiyama_Suzune][102], which covers prefix sums of Dirichlet inverses in $$$O(n^{2/3})$$$.

---

## Statements it makes

**Claim**: Let $$$f(n)$$$ and $$$g(n)$$$ be such that $$$F\left(\lfloor n/k\rfloor\right)$$$ and $$$G\left(\lfloor n/k\rfloor\right)$$$ are known for all possible arguments. Then we can compute prefix sum $$$H(n)$$$ of $$$h(n) = (f * g)(n)$$$ in $$$O(\sqrt n)$$$. Moreover, we can find $$$H(\lfloor n/k \rfloor)$$$ for all possible arguments in $$$O(n^{2/3})$$$.

**Claim**: Let $$$f(n)$$$ be such that we can find values of $$$F\left(\left\lfloor n/k\right\rfloor\right)$$$ for all possible arguments in $$$O(n^{2/3})$$$. Then we can also find the prefix sums for all possible arguments of the Dirichlet inverse $$$f^{-1}(n)$$$ in $$$O(n^{2/3})$$$.

*[digest of a 52704 character source; every section, statement, and proof in full at `research/sources/kulkov-dirichlet-convolution-fast-prefix-sums.full.md`]*
