# Erdős Problems collection #69 — "The Erdös–Gyárfás conjecture" (UCSD mathweb)

Source: https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/PowerOfTwoCycles.html
Full text: not separately downloaded (network fetch of the page failed); the
verbatim content below was captured via `read_sources` in the librarian run and
matches the page as served. This is the **graph-problem-collection (#69)** twin
of the forum/statement page erdosproblems.com/64 already held; it fixes the
classic bibliographic entries (see below).

## What it says

> "The Erdös–Gyárfás conjecture ($100 for proof, $50 for counterexample).
> Any graph with minimum degree 3 contains a simple cycle whose length is a
> power of 2."

- Royle and Markström showed through computer search that any counterexample
  contains more than 17 vertices, and moreover any **cubic** counterexample must
  contain more than 30 vertices [2].
- Known true for certain families:
  - Shauger 1998: graphs that avoid large induced stars and satisfy some degree
    constraints [1] (K_{1,m}-free with min degree ≥ m+1 or max degree ≥ 2m−1).
  - Daniel–Shauger 2001: planar claw-free graphs [3].
- Weaker "unavoidable cycle lengths":
  - Verstraëte 2005: set S of lengths with |S| = O(n^{0.99}) such that every
    graph of average degree ≥ 10 contains a cycle of length in S [5].
  - Sudakov–Verstraëte 2008: conjecture holds for every graph whose average
    degree is in the iterated logarithm of the number of vertices [4].

## Bibliography it fixes (exact bibliographic entries)

| # | Work |
| --- | --- |
| 1 | D. Daniel and S. Shauger, "A result on the Erdős–Gyárfás conjecture in planar graphs", Proc. 32nd Southeastern Int. Conf. Combinatorics, Graph Theory, and Computing (2001), 129–139. |
| 2 | K. Markström, "Extremal graphs for some problems on cycles in graphs", Congr. Numerantium 171 (2004), 179–192. |
| 3 | S. Shauger, "Results on the Erdős–Gyárfás conjecture in K_{1,m}-free graphs", Proc. 29th Southeastern Int. Conf. Combinatorics Graph Theory, and Computing 171 (1998), 61–65. |
| 4 | B. Sudakov and J. Verstraëte, "Cycle lengths in sparse graphs", Combinatorica 28 (2008), 357–372. |
| 5 | J. Verstraëte, "Unavoidable cycle lengths in graphs", Journal of Graph Theory 49 (2005), 151–167. |

Note the prize on this page is **$100 proof / $50 counterexample** (matching
West's older page, not erdosproblems.com/64's $1000). The bibliographic entries
cross-check the library's held summaries (Markström 2004, Sudakov–Verstraëte
Combinatorica 28, Verstraëte JGT 49). All five are already represented in the
library as summaries; this page adds their exact venue/year/page numbers.

```claim
id: ucsd-69-statement
statement: The Erdos-Gyarfas conjecture (every graph with minimum degree at least 3 has a simple cycle whose length is a power of 2) is open, with computer-search bound any counterexample has more than 17 vertices and any cubic counterexample more than 30; true for K_{1,m}-free (with degree constraints, Shauger 1998) and planar claw-free (Daniel-Shauger 2001) graphs.
hypotheses: none — this is the canonical statement-level reference, prize $100/$50
holds-here: yes (statement tier)
status: asserted (statement page; supersedes nothing, cross-checks West/Markstrom/Sudakov-Verstraete/Verstraete already held)
bearing: fixes the statement and the classic bibliography with exact venue/page numbers; no experimental content beyond what the library already holds
anchor: https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/PowerOfTwoCycles.html
```
