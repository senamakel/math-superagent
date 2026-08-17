# OI Wiki (English) — Euclidean-like Algorithm (类欧几里德算法)

Source: https://en.oi-wiki.org/math/euclidean/ (English translation of the
Chinese OI Wiki article). Full text:
`research/sources/oi-wiki-euclidean-like-algorithm-en.full.md`.

## What it establishes

The Euclidean-like algorithm (introduced by 洪华敦 / Hong Huadun, 2016
winter-camp exchange) evaluates three mutually-recursive floor sums in
O(log n):

- f(a,b,c,n) = Σ_{i=0}^{n} ⌊(ai+b)/c⌋
- g(a,b,c,n) = Σ_{i=0}^{n} i·⌊(ai+b)/c⌋
- h(a,b,c,n) = Σ_{i=0}^{n} ⌊(ai+b)/c⌋²

**Reduction with a ≥ c or b ≥ c** (mod step): replace a ↦ a mod c, b ↦ b mod c
and add the closed-form contributions (polygonal terms in n, ⌊a/c⌋, ⌊b/c⌋).

**Reduction for 0 ≤ a,b < c** (flip step): with m = ⌊(an+b)/c⌋ and
t_j = ⌊(jc+c−b−1)/a⌋ — obtained by swapping the roles of condition and
contribution, i.e. counting j < ⌊(ai+b)/c⌋ as i > t_j — one gets

- f(a,b,c,n) = n·m − f(c, c−b−1, a, m−1)
- g(a,b,c,n) = ½[ m·n(n+1) − h(c,c−b−1,a,m−1) − f(c,c−b−1,a,m−1) ]
- h(a,b,c,n) = n·m(m+1) − 2g(c,c−b−1,a,m−1) − 2f(c,c−b−1,a,m−1) − f(a,b,c,n)

The three recurse together in O(log(max)) (the mutual recursion must be
computed simultaneously to avoid duplicate work). The page includes a complete
C++ implementation (`struct data { f, g, h }`, `calc(n,a,b,c)`) mod P — the
exact arithmetic shape a second-moment floor-sum evaluator needs.

## Relation to PE1006

- This is the classical (non-geometric) second-moment recursion: it computes
  Σ⌊·⌋² over i = 0..n in O(log), the same quantities as directive 2's
  v(x)² second moment *without* the decimal weight 10^{k-1-j}.
- PE1006's sum carries the extra geometric weight x^i with x = 10^{-1} mod M
  (directive 2's telescoped form has weights 10^{k-1-j} on ⌊x+ja⌋). The
  geometric-weight extension is supplied by the library's other universal-
  Euclidean sources: fhq's "sum f(x)aˣg(y)bʸ" monoid
  (`universal-euclidean-geometric-weight-fhq.full.md`), LOJ138 moment monoid
  (`loj138-universal-euclidean-floor-moments.full.md`), and OI Wiki (Chinese)
  universal Euclidean (`oi-wiki-universal-euclidean-floor-sum.full.md`).
- This English page is the backstop *derivation* of the f/g/h recursion in a
  language the run can read directly; the h-recursion's arithmetic (mod-step
  closure formulas) is what the solver's monoid combination must reproduce.

English-language treatment of a primitive previously held only in Chinese
sources; closes the "English treatment missing" note from the library status.