# Brouwer–Neumaier 1988, "A remark on partial linear spaces of girth 5 with an application to strongly regular graphs" (Combinatorica 8:57–61, 1988)

<!-- source: https://ir.cwi.nl/pub/1721/1721D.pdf -->
<!-- full text: research/sources/brouwer-neumaier-1988-combinatorica.full.md -->

**This is the primary structural source for the partial-linear-space
reformulation of the Conway problem.** (The file `research/sources/index.full.md`
is a duplicate Springer landing page of the same DOI 10.1007/BF02122552; the
real full text is this file.)

## What it establishes

**Theorem (lower bound).** A connected partial linear space with girth ≥ 5,
more than one line, and every point on Λ neighbours, contains
`k ≥ Λ(Λ+3)/2` points. (k = number of points, Λ = valency of the point graph.)

**Corollary (application to SRGs).** A strongly regular graph with μ=2 and
`k < λ(λ+3)/2` is a **partial quadrangle**, in particular it satisfies the
divisibility condition `(λ+1) | k`.

**Table (μ=2, v ≤ 2000, not nets).** — for (99,14,1,2) row:
```
v  k  λ  r  s  f   g   existence
99 14 1  3 −4 54  44  ?
```
adjacent to Gewirtz (56,10,0,2) and BvLS (243,22,1,2), both existing. The `?`
is Brouwer–Neumaier's own mark that (99,14,1,2) is **open** — the paper does
NOT rule it out.

## Why it does not give a 99 weapon

For (99,14,1,2): λ=1 ⇒ λ(λ+3)/2 = 2; k=14 ≥ 2, so the corollary's hypothesis
`k < 2` **fails** and nothing is forced. The whole μ=2/PLS forcing is in the
trivial first branch. (For the negative controls: rook(3) k=4≥2 and BvLS k=22≥2
also satisfy the bound, so the theorem is consistent with both existing
graphs.) See research/notes/brouwer-neumaier-mu2-structure.md and
research/notes/bagchi-mu2-dichotomy-resolution.md for the full branch
analysis, including why the strengthened Bagchi dichotomy also has no bite.

## Implication for this run
Confirms from the primary source: (i) the partial-linear-space / girth-5 basis
of problem.md's "231 lines of size 3, 7 through each point" reformulation;
(ii) (99,14,1,2) is genuinely open (the paper's table marks it `?`); (iii) any
99 nonexistence argument must go beyond this classical μ=2/PLS dichotomy — it
provably cannot lean on it.

```claim
id: brouwer-neumaier-1988-99-open-combinatorica
statement: Brouwer-Neumaier 1988 (Combinatorica 8:57-61) does NOT rule out
  srg(99,14,1,2); its μ=2 table lists (99,14,1) with spectrum 3^54,-4^44 and
  status '?'. The corollary (SRG with mu=2 and k<lambda(lambda+3)/2 is a
  partial quadrangle with (lambda+1)|k) does not apply: lambda=1 gives the
  bound 2 and k=14 >= 2.
hypotheses: none beyond reading the paper's own full text.
holds-here: yes.
status: sourced (primary full text in library; the bound arithmetic 1*4/2=2,
  k=14 is elementary and verified).
bearing: prevents spending effort on a theorem the paper does not state; resets
  (99,14,1,2) to genuinely open; supplies the PLS/girth-5 structural basis.
anchor: research/sources/brouwer-neumaier-1988-combinatorica.full.md
```

[[brouwer-neumaier-1988-combinatorica.full]]
