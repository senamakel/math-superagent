# Requests closed — Sturmian factor complexity and universal-Euclidean primitive

This run's four open requests are answerable from the library on disk. Each claim
below carries the `answers:` line required to close a request, and cites the exact
full-text source (with URL) that fixes the statement.

```claim
id: req-close-factor-complexity
statement: The infinite Fibonacci word is a Sturmian word; a Sturmian word has exactly
P(s,n)=n+1 distinct factors of length n for every n >= 0 (the defining minimal
complexity, Methode–Hedlund). Hence PE1006's "only k+1 different Fibonacci subwords of
length k" is the standard factor-complexity theorem, and the length-3 set is
{001,010,100,101} (Psi(3)=20302), exactly as the problem and Wikipedia both give.
hypotheses: binary aperiodic infinite word, Sturmian (equivalently irrational mechanical, balanced).
holds-here: true — the S_n limit is the infinite Fibonacci word whose length-k factors are the problem's subwords.
status: sourced
follows-from: governing-sturmian, governing-factor-complexity
bearing: Fixes the object set of the sum at exactly k+1 terms and confirms the statement example.
anchor: research/sources/lothaire-sturmian-words-C2.full.md (sec 2.1.1, def of complexity and Sturmian, P(s,n)=n+1); research/sources/wikipedia-fibonacci-word.full.md (complexity n+1, lists the 4 length-3 subwords); research/sources/perrin-restivo-note-sturmian-words.full.md (Theorem 1).
answers: citable-statement-theorem-039a
```

```claim
id: req-close-universal-euclidean
statement: The universal Euclidean algorithm (monoid generalisation of AtCoder floor_sum,
aka "Chtholly's algorithm" / 万能欧几里得) evaluates sums sum_{i=0}^{n-1} x^i *
floor((a*i+b)/c) — and the (count, sum x^i, sum x^i*floor, sum x^i*floor^2) tuple — in
O(log n), via the U/R merge-and-flip recursion; x = 10^-1 mod M is a unit so geometric
weights are well defined mod M = 101001001.
hypotheses: a,b,c,n in Z>=0, c>0; carried quantities linear in the floor argument; x a unit mod M.
holds-here: true — Psi(k) is the second moment of a 10^j-geometric floor sum over k+1 reps; linear closure holds.
status: sourced
bearing: This is the O(log) primitive that makes Psi(10^18) mod M computable without enumerating 10^18 terms.
anchor: research/sources/universal-euclidean-geometric-weight-fhq.full.md (https://www.cnblogs.com/dixiao/p/15719155.html, recursion + 6-component Po monoid); research/sources/oi-wiki-universal-euclidean-floor-sum.full.md (https://oi.wiki/math/number-theory/euclidean/, monoid proof + O(log n)); research/sources/loj138-universal-euclidean-floor-moments.full.md; research/sources/atcoder-library-math-floor_sum.
answers: citable-name-treatment-0c91, citable-precise-statement-600d, citable-precise-statement-d2e7
```

## Where the four requests now stand

- `citable-statement-theorem-039a` — closed by `req-close-factor-complexity` and
  `fibonacci-sturmian-complexity` above.
- `citable-name-treatment-0c91`, `citable-precise-statement-600d`,
  `citable-precise-statement-d2e7` — closed by `req-close-universal-euclidean` and
  `universal-euclidean-geometric-floor-sum`.

Both primitives are O(log), so the run's belief that Psi(10^18) collapses to an
O(log) second-moment floor sum is supported by the library; nothing on disk
falsifies the tuple-closure hypothesis. Next work is the run's own: brute oracle
and solution implementation (tool_builder), which will re-verify the claimed
construction against brute on k=1..150 before k=10^18.
