# Bondy & Vince — "Cycles in a graph whose lengths differ by one or two"

Source: J. A. Bondy, A. Vince, *Journal of Graph Theory* 27(1) (1998) 11–15.
Open author copy:
[[bondy-vince-cycles-differ-1-2.full]] (`research/sources/bondy-vince-cycles-differ-1-2.full.md`).

## The question this answers

Erdős asked: in a simple graph where every vertex has degree at least three, must
there exist two cycles whose lengths differ by one or two? This is the *adjacent*
interval result that surrounds the Erdős–Gyárfás conjecture (which appears in the
same paper's introduction exactly as this run's problem.md states it: "If G is a
graph with minimum degree three, must G have a cycle of length 2^r for some integer r?").

## What it establishes

- **Theorem 1.** With the exception of K1 and K2, every simple graph having at most
  two vertices of degree less than three contains two cycles whose lengths differ
  by one or two. (So δ ≥ 3, and even a couple of degree-2 exceptions, force two
  cycles of lengths n and n±1 or n±2.)
- **Theorem 2.** Every nonbipartite 3-connected graph has two cycles whose lengths
  differ by one.
- Best-possible for the exceptions C3, P3, K2,3 (three vertices of degree < 3, no
  two cycles differing by 1 or 2); with twelve exceptions total, the theorem
  extends to three vertices of degree < 3.
- **Conjecture:** for every k, with finitely many exceptions, a graph with at most k
  vertices of degree < 3 has two cycles differing by 1 or 2. This is now proved for
  all k (Gao & Ma, "On a conjecture of Bondy and Vince", arXiv:1902.05701).

```claim
id: bondy-vince-theorem1
statement: With the exception of K1 and K2, every simple graph having at most two vertices of degree less than three contains two cycles whose lengths differ by one or two.
hypotheses: simple graph, ≤ 2 vertices of degree < 3
holds-here: true — a δ ≥ 3 graph certainly has ≤ 2 vertices of degree < 3
status: proved (source full text)
bearing: the adjacent interval result. It forces two close cycle lengths, not a power of two. Two lengths n, n+1 or n, n+2 do NOT in general contain a power of two, so this does not settle the conjecture. It is the obstruction problem.md names: interval results do not prescribe a sparse 2^k.
anchor: research/sources/bondy-vince-cycles-differ-1-2.full.md
```

## For this problem (the obstruction, made precise)

Bondy–Vince delivers cycles at lengths a and a±2 (even a and a+2). Two such lengths
need not straddle a power of two: powers of two are sparse (gap 2^k between
consecutive), so a pair a, a+1 or a, a+2 contains a power of two only if one of them
*is* that power. The result therefore confirms the run's central fact — that
interval/congruence cycle-length machinery cannot settle the conjecture at δ = 3; an
argument must produce a cycle at a *prescribed* sparse length. Confirms
`ghlu-ma-interval-results` and the problem.md obstruction from primary text.
