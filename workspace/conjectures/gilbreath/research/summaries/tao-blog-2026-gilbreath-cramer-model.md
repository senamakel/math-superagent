> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/tao-blog-2026-gilbreath-cramer-model.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/ | converted from HTML -->

## What is in it

- Gilbreath’s conjecture: a Cramér random model and a deterministic analysis
    - Share this:
    - Recent Comments
    - Top Posts
    - Archives
    - Categories
    - [image: RSS] [421] [The Polymath Blog][422]
  - 9 comments
    - Leave a comment [Cancel reply][456]
    - For commenters


## What it claims

[Zachary Chase][17], [Zach Hunter][18] and I have uploaded to the arXiv our preprint [Gilbreath’s conjecture: a Cramér random model and a deterministic analysis][19]. This paper is motivated by a [notorious conjecture of Gilbreath][20] (also proposed eighty years prior by Proth), which one can state as follows: if one starts with the sequence of primes and repeatedly takes absolute differences of consecutive terms, then the first term of each subsequent row is always [image: {1}]:

[image: \displaystyle  \begin{array}{ccccccccccc} 2 & & 3 & & 5 & & 7 & & 11 & & 13 \\ & 1 & & 2 & & 2 & & 4 & & 2 & \\ & & 1 & & 0 & & 2 & & 2 & \\ & & & 1 & & 2 & & 0 & & \\ & & & & 1 & & 2 & & & \\ & & & & & 1 & & & & \end{array}. ]

Coming from a PDE background, I like to think of this conjecture as a (discrete) nonlinear “wave equation” problem, where the primes are the “initial data”, the downward direction in the above pyramid is the arrow of “time”, and the “equation of motion” is that the value of the “scalar field” at any given point in “spacetime” is the absolute difference of the values of the…

## Statements it makes

**Theorem 1**Suppose the initial row entries [image: {a_n}] of a Gilbreath array are drawn independently from a uniform distribution on [image: {\{0,\dots,f(n)-1\}}] for some [image: {2 \leq f(n) \leq \frac{1}{10} \frac{\log\log n}{\log \log \log n}}]. Then almost surely, all but finitely many of the rows have a [image: {\{0,1\}}] -valued first entry.

*[digest of a 68139 character source; every section, statement, and proof in full at `research/sources/tao-blog-2026-gilbreath-cramer-model.full.md`]*
