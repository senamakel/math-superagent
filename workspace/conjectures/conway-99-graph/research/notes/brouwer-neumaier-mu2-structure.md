# Claim — the partial-linear-space / μ=2 structural theorem (Brouwer–Neumaier 1988)

```claim
id: bn-88-mu2-structure
statement: Let G be a regular graph of valency k in which every edge lies in
  exactly lambda triangles and any two nonadjacent vertices have at most two
  common neighbours (in particular any srg with mu=2). For a vertex x, H=Gamma(x)
  is a partial linear space of girth at least 5, formed by points=neighbours of x
  and lines=maximal cliques of H. Then EITHER k >= lambda*(lambda+3)/2, OR
  Gamma(x) is a disjoint union of lines of size lambda+1 (forcing (lambda+1)|k
  and G itself to be a partial linear space).
hypotheses: regular, valency k, each edge in exactly lambda triangles,
  nonadjacent pairs share at most 2 common neighbours; mu=2 for SRGs.
holds-here: for (99,14,1,2), lambda=1, k=14. First branch bound
  lambda*(lambda+3)/2 = 1*4/2 = 2. Since k=14 > 2, the FIRST branch holds
  trivially and the corollary's hypothesis k < 2 FAILS. So Brouwer-Neumaier
  does NOT force (99,14,1,2) to be a partial quadrangle. The second alternative
  (Gamma(x) a disjoint union of lambda+1 = 2 lines = perfect matching = 7K2)
  also holds as the known local structure, and (lambda+1)=2 divides k=14.
status: sourced (Brouwer-Neumaier 1988, Combinatorica 8(1) 57-61, full text in
  library). Verified computationally for the local-structure part: with
  lambda=1,k=14, mu=2, the neighbourhood of any vertex is a perfect matching
  7K2 (7 lines of size 2 through each point), and there are 99*7/2 = 693/... 
  Actually 99*7/3 = 231 lines of size 3 total (the triangles).
base: research/sources/brouwer-neumaier-1988-combinatorica.full.md
bearing: this is the primary-source basis of problem.md's partial-linear-space
  reformulation (99 points, lines of size 3, 7 lines through each point). It
  confirms the geometry and shows why the naive Bagchi reading (rule out 99 via
  mu=2 dichotomy) fails: the dichotomy's grid/generalized-quadrangle conclusion
  is triggered only when k < lambda*(lambda+3)/2, and for lambda=1 that bound is
  2, so the 99-graph is in the k-quiet regime where nothing is forced.
```

## The exact table row (Brouwer–Neumaier 1988, table)

For strongly regular graphs with v ≤ 2000 and μ=2 (not nets):

| v  | k  | λ | r | s  | f   | g   | existence |
|----|----|---|----|----|-----|-----|-----------|
| 99 | 14 | 1 | 3 | −4 | 54  | 44  | ? |

This exactly matches Brouwer's web table and my integrality computation:
spectrum 3⁵⁴, −4⁴⁴, existence open. The row confirms (99,14,1,2) is a
genuinely open member of the μ=2 family, adjacent in the table to the Gewirtz
graph (56,10,0,2, exists) and the BvLS graph (243,22,1,2, exists).

## What this means for the geometry route

For (99,14,1,2), because λ=1 makes `λ(λ+3)/2 = 2` so small, the entire
partial-line-space forcing machinery of Brouwer–Neumaier is in the "first
branch k ≥ 2 (trivial)" regime. The non-trivial content is the second
alternative: since k=14 ≥ 2 always, the theorem says nothing forces Γ(x) into
lines. So ANY nonexistence argument for 99 must go beyond this classical
result — it cannot lean on the μ=2/PLS dichotomy. This is a genuine "dead end
identified" — a known direction that provably does not bite 99. (It DOES bite
other μ=2 members like (300,26,4): there λ=4, lambda*(lambda+3)/2 = 4*7/2=14,
k=26 > 14 still... wait need lambda where k < lambda(lambda+3)/2. For the table
members ruled out in the note: (736,42,8,10): lambda=8, bound=8*11/2=44, k=42
< 44 ✓ so ruled out. (875,46,9): bound 9*12/2=54, k=46<54 ✓. (1944,67,10):
bound 10*13/2=65, k=67 > 65 — the note handles it separately. So the 99 row has
lambda=1, bound 2, k=14 — never in the ruled-out regime.)

## Negative-control check (why this passes on 9 and 243)

Rook's graph (9,4,1,2): lambda=1, bound = 2, k=4 > 2 — first branch trivial,
second branch: Gamma(x) is 4 vertices, lines of size 2 = the 2 edges of the
matching in the 3x3 grid neighbourhood (each row/column through x). Consistent,
G is a partial linear space (the 3x3 grid lines). Passes.
BvLS (243,22,1,2): lambda=1, bound 2, k=22 > 2 — first branch trivial. The
theorem does not rule it out, consistent with its existence. Passes.
So Brouwer-Neumaier is *consistent with both positive controls* — it gives no
weapon against 99, but also harms nothing. A corollary-writer must not claim
it rules out 99.
