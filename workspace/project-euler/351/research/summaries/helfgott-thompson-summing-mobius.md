> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/helfgott-thompson-summing-mobius.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://doi.org/10.1007/s40993-022-00408-8 | converted from HTML -->

## What is in it

- Summing \(\mu (n)\): a faster elementary algorithm
  - Abstract
    - Similar content being viewed by others
    - [A note on the partial sum of Apostol's Möbius function][8]
    - [Monotone Nondecreasing Sequences of the Euler Totient Function][9]
    - [On the Missing Log Factor][10]
    - Explore related subjects
  - 1 Introduction
    - MainTheorem
    - 1.1 Our approach
    - 1.2 Alternatives
    - 1.3 Notation and algorithmic conventions
  - 2 Preparatory work: identities
  - 3 The case of a large non-free variable
    - Lemma 3.1
    - Proof
    - Proposition 3.2
    - Proof
  - 4 The case of a large free variable
    - 4.1 A first try
    - 4.2 Handling the difference between reality and an approximation
- …


## What it claims

We present a new elementary algorithm that takes \( \textrm{time} \ \ O_\epsilon \left( x^{\frac{3}{5}} (\log x)^{\frac{8}{5}+\epsilon } \right) \ \ \textrm{and} \ \textrm{space} \ \ O\left( x^{\frac{3}{10}} (\log x)^{\frac{13}{10}} \right) \) (measured bitwise) for computing \(M(x) = \sum _{n \le x} \mu (n),\) where \(\mu (n)\) is the Möbius function. This is the first improvement in the exponent of *x*for an elementary algorithm since 1985. We also show that it is possible to reduce space consumption to \(O(x^{1/5} (\log x)^{5/3})\) by the use of (Helfgott in: Math Comput 89:333–350, 2020), at the cost of letting time rise to the order of \(x^{3/5} (\log x)^2 \log \log x\).

## Statements it makes

### Lemma 3.1

### Proposition 3.2

Algorithm 23 computes *D*(*n*; *a*) recursively: it calls itself to compute \(D(n_0;a)\) and \(D(n_0;a/p_r)\), where \(n_0 = p_1 p_2 \cdots p_{r-1}\), and then returns \(D(n;a) = D(n_0;a) - D(n_0;a/p_r)\). The contribution of \(D(n_0;a)\) is that of divisors \(\ell |n\) with \(p_r\not \mid \ell \), whereas the contribution of \(D(n_0;a/p_r)\) corresponds to that of divisors \(\ell |n\) with \(p_r|\ell \).

### Lemma 4.1

### Lemma 4.2

### Lemma 4.3

### Lemma 4.4

### Lemma 4.5

### Lemma 4.6

*[digest of a 100197 character source; every section, statement, and proof in full at `research/sources/helfgott-thompson-summing-mobius.full.md`]*
