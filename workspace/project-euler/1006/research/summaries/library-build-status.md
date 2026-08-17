# Library build status — PE1006 reference library

What the library holds, why each source is there, and where it lives. The Cognee
memory server was down for the whole of this cycle (every `remember_memory` and
every download's memory-vectorisation call failed with a server-health timeout),
so durable findings are recorded here on disk until memory recovers.

## The governing theory (established, sourced)

PE1006 is a problem about the distinct length-k factors (subwords) of the
Fibonacci word. The Fibonacci word is the canonical **characteristic Sturmian
word**; its factor complexity is exactly `k+1` for every length `k` (minimal
complexity, Morse–Hedlund). The `k+1` distinct factors are exactly the problem's
`k+1` Fibonacci subwords.

The magnitude of the result the run is chasing: `Psi(10^18) mod 101001001`,
i.e. the sum of squares of ~`10^18+1` distinct length-`10^18` subwords read as
decimal numbers, taken modulo `M = 101001001`. The governing reduction
(directives 1 & 2) turns this into a **geometrically weighted floor sum** over
`k+1` mechanical-word representatives, evaluated by the **universal Euclidean
algorithm** (monoid generalisation of AtCoder `floor_sum`, aka Chtholly's
algorithm) in `O(log)` — not by enumerating the billion-trillion factors.

## Sources on disk (research/sources/)

All were found via `exa_search` (verified URLs) then downloaded; each carries its
source URL. Full texts: `*.full.md`. Digests first: `research/summaries/*.md`.

1. **arXiv:2204.13977, Sivasankar & Rama — "Two-dimensional Fibonacci words:
   Tandem repeats and factor complexity"** (`fibonacci-word-2d-factor-complexity-ar5iv.full.md`,
   full text from ar5iv). **The position theorem.** Theorem 7: for
   `F(n) <= k < F(n+1)`, the k+1 distinct length-k factors `z_j^(k)` of the
   infinite Fibonacci word f are
   `z_j = f[j+1..j+k]` for `0<=j<=F(n)-1`, else `f[j+F(n+1)-k..+k]` for
   `F(n)<=j<=k`, listed in first-occurrence order. Theorem 8: factor complexity
   of the finite word `f_n` is piecewise `k+1`, `F(n-2)+2`, `F(n)+1-k`. This is
   the structural description the solver builds on.
2. **Wikipedia — Fibonacci word** (`wikipedia-fibonacci-word.full.md`). Canonical
   characterisation: Sturmian, complexity `C(n)=n+1`, lying on a line of slope
   `1/phi` / `phi-1`, digits `2+floor(n*phi)-floor((n+1)*phi)`.
3. **Perrin — Sturmian words, Lecture 2 (mechanical words)** 
   (`perrin-sturmian-words-lecture2-mechanical.full.md`). Defines the lower
   mechanical word `s_a,rho(n) = floor(a(n+1)+rho) - floor(a n + rho)` — the
   exact digit formula directive 2 uses — plus rotations, balance, and the
   interval/factor correspondence.
4. **Wikipedia — Sturmian word** (`wikipedia-sturmian-word.full.md`).
   Encyclopedic tier; factor complexity, mechanical words, balance equivalence.
5. **OEIS A003849** (`oeis-a003849-fibonacci-word.full.md`). The infinite
   Fibonacci word's sequence record; the canonical digit sequence reference.
6. **Berstel — Recent results in Sturmian words (DLT'95)**
   (`berstel-recent-results-sturmian-words-dlt95.full.md`). The standard survey;
   definitions, continued-fraction construction, standard words, Lyndon and
   Baldwin results.
7. **Berstel — Sturmian and Episturmian words, survey 2007**
   (`berstel-sturmian-episturmian-survey-2007.full.md`). 14 characterisations of
   central words; standard/episturmian structure.
8. **OI Wiki — Euclidean algorithm / universal Euclidean (万能欧几里得)**
   (`oi-wiki-universal-euclidean-floor-sum.full.md`). The magnitude-essential
   primitive reference: the monoid model, U/R operations, the merge-and-flip
   recursion `F(a,b,c,n,U,R) = R^... U F(c,..,a,..,R,U) R^...` in O(log), and
   the floor / i·floor / floor² component monoid `(x,y,sy,sxy,sy2)`.
9. **fhq_treap — 万能欧几里得 (universal Euclidean) study note**
   (`universal-euclidean-geometric-weight-fhq.full.md`). Explicitly covers the
   `sum f(x) a^x g(y) b^y` form — the geometric-weight floor sum directive 2
   requires — with a 6-component monoid
   `(cntu,cntr,sumi,sums,sqrs,prod)`, its combination rule, the merge/flip
   recursion, and an O(log) implementation. **This answers the open request**
   `citable-precise-statement-600d` / `citable-precise-statement-d2e7`.
10. **LOJ138 — universal Euclidean (floor moments)**
    (`loj138-universal-euclidean-floor-moments.full.md`). Covers
    `sum floor((px+r)/q)^k1 x^k2`, the moment-array Node monoid with
    combination via binomial expansion — the generalisation that includes both
    x^i and floor^i weights.
11. **AtCoder Library math doc** (`summaries/atcoder-math-floor_sum-doc.md`).
    Official `floor_sum` spec (O(log)).

## OEIS lookup result (finding)

`Psi(1..5) = 1, 101, 20302, 2042402, 204252402` returned **no OEIS match**. The
sequence of Psi values is not catalogued; no closed form will be looked up — the
structure must come from Sturmian/universal-Euclidean theory. (If these terms
are wrong the brute oracle will correct them; they are the stated-check basis
only.)

## The open request is answerable from the library

`requests` holds the gap "citable, precise statement of the generalised
floor_sum / universal Euclidean algorithm". Sources 8, 9, 10, 11 now supply it.
A claim block recorded against `citable-precise-statement-600d` should cite
sources 9 and 8.

## What could not be obtained

- maspypy's `floor_monoid_product.hpp` raw file: GitHub returned 503/429 twice.
  The same algorithm is fully covered by sources 8 and 9 (already on disk),
  so this is not a blocking gap.
- Berstel's original *Fibonacci words — a survey* (The Book of L) PDF is not
  freely hosted; the DLT'95 Sturmian survey (source 6) covers the needed ground.

## Next steps for the solver (not the librarian)

1. `code/brute.py`: naive Psi enumeration, must hit Psi(3)=20302 and
   Psi(10) mod M = 10699667.
2. Reproduce directive 2's mechanical-word/floor-sum construction vs brute on
   k=1..150, then Psi(10), then k=10^18.
3. Verify final answer by a second route (directive 1's autocorrelation form).
