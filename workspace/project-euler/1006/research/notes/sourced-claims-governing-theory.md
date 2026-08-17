# Sourced claims — PE1006 governing theory

Each claim below is backed by a source in `research/sources/` (full text, with its
URL in the first line). A claim's `anchor` names that source. Status `sourced`
means it is a standard theorem found in the library, not computed this run.

---

```claim
id: governing-sturmian
statement: The infinite Fibonacci word S = 0100101001001... (the S_n of the problem,
S_n = S_{n-1} S_{n-2}, S_0=0, S_1=01, in the limit) is a Sturmian word — specifically
the characteristic Sturmian word of slope 2 - phi = (3 - sqrt5)/2 = 1/phi^2, where
phi = (1+sqrt5)/2 is the golden ratio. Its digit at position n is
floor((n+2)r) - floor((n+1)r) with r = 2 - phi, i.e. a mechanical word of slope 2-phi.
hypotheses: S is the limit of the substitution 0 -> 01, 1 -> 0 applied to 0; slope 2-phi is irrational.
holds-here: yes — this is exactly the word whose length-k substrings the problem calls Fibonacci subwords.
bearing: It fixes the object under study as a Sturmian/mechanical word, opening the factor-complexity and mechanical-word theorems.
status: sourced
anchor: research/sources/wikipedia-fibonacci-word.full.md (URL https://en.wikipedia.org/wiki/Fibonacci_word); research/sources/perrin-restivo-note-sturmian-words.full.md (https://hal.science/hal-00828351/file/noteSturmianWords.pdf); research/sources/perrin-sturmian-words-lecture2-mechanical.full.md
```

```claim
id: governing-factor-complexity
statement: A Sturmian word has exactly k+1 distinct factors (contiguous substrings) of
length k for every k >= 1. This is the defining minimal-complexity property of Sturmian
words (Morse–Hedlund). Consequently the infinite Fibonacci word has exactly k+1 distinct
length-k substrings, which is precisely the "interestingly, for each positive integer k,
there are only k+1 different Fibonacci subwords of length k" assertion of the problem.
hypotheses: binary word, Sturmian (equivalently irrational mechanical, equivalently balanced and aperiodic).
holds-here: yes — the problem itself asserts the k+1 count, and the Sturmian theorem is the standard explanation.
bearing: Confirms the object set: the k+1 distinct subwords the solver must read as decimals and square-sum.
status: sourced
anchor: research/sources/perrin-restivo-note-sturmian-words.full.md (Theorem 1, Theorem 2 and Section 2: "Sturmian words have exactly n+1 factors of length n"); research/sources/perrin-sturmian-words-lecture2-mechanical.full.md (Morse–Hedlund 1940 equivalence theorem); research/sources/fibonacci-word-2d-factor-complexity-ar5iv.full.md (Proposition 4)
```

```claim
id: governing-mechanical-word-reps
statement: Every length-k factor of a Sturmian word of slope a is generated, over the k+1
different arc-midpoint intercepts x_m (m=0..k), by the mechanical-word digit rule
digit_j = floor((j+1)a + x) - floor(j a + x). The k+1 distinct factors are exactly the
decimal strings these k+1 representatives produce. (Directive-2 construction; equivalently
the factors are first-occurrence positions of the infinite word as in the Sivasankar–Rama
Theorem 7.)
hypotheses: a irrational slope (or rational approximation F(n-1)/F(n) with F(n) >> k, which reproduces the same factor set at exact-integer arithmetic).
holds-here: yes — this is the model the solver uses to avoid enumerating the 10^18+1 factors directly.
bearing: Reduces the object set to k+1 mechanical-word representatives with an arithmetic digit formula.
status: sourced (directive 2) + structural
anchor: research/sources/perrin-sturmian-words-lecture2-mechanical.full.md (interval/factor correspondence R^n(rho) in I_w); research/sources/fibonacci-word-2d-factor-complexity-ar5iv.full.md (Theorem 7 position theorem); config/directives.jsonl (directive 2)
```

```claim
id: governing-universal-euclidean
statement: The universal Euclidean algorithm (monoid generalisation of the AtCoder
floor_sum, "Chtholly's algorithm") evaluates sums of the form
sum_{i=0}^{n-1} x^i * floor((a*i+b)/c)  (and the (count, sum x^i, sum x^i floor,
sum x^i floor^2) tuple) in O(log) time, via the U/R merge-and-flip recursion
F(a,b,c,n,U,R) = R^q ... F(c, b mod c, a, n', R, U) ... U. It collapses to a geometric
series in x for the pure-power sub-sums.
hypotheses: c >= 1, a >= 0, b, n >= 0; x a unit in the ring (mod M, M = 101001001).
holds-here: yes — directive 2 requires exactly this to evaluate Psi(k) = second moment of a
geometrically weighted floor sum for k = 10^18 without enumerating k terms.
bearing: This is the O(log) primitive that makes Psi(10^18) mod M computable at all.
status: sourced
anchor: research/sources/oi-wiki-universal-euclidean-floor-sum.full.md (https://oi.wiki/math/number-theory/euclidean/); research/sources/universal-euclidean-geometric-weight-fhq.full.md (https://www.cnblogs.com/dixiao/p/15719155.html); research/sources/loj138-universal-euclidean-floor-moments.full.md; research/sources/atcoder-math-hpp-v151.full.md (floor_sum)
```

---

Notes on coverage:

- **Answers the open request `citable-statement-theorem-039a`** (Sturmian / factor
  complexity k+1): claims `governing-sturmian` and `governing-factor-complexity` carry
  the citable theorem + source (Perrin–Restivo Theorem 1; Morse–Hedlund via Perrin
  Lecture 2; Berstel DLT'95 survey).
- **Answers the open requests `citable-precise-statement-600d` and
  `citable-precise-statement-d2e7`** (universal Euclidean / geometric-weight floor_sum):
  claim `governing-universal-euclidean` cites OI Wiki, fhq study note, LOJ138, and
  AtCoder floor_sum.
- The OEIS corpus `research/sources/oeis-A003849-first-1652-subwords.full.md`
  (from https://oeis.org/A003849/a003849.txt) lists all length-1..10 factors
  (001, 010, 100, 101 are lines 6–9 of the length-3 block), matching the problem's
  length-3 subwords — an independent oracle for the factor set.
