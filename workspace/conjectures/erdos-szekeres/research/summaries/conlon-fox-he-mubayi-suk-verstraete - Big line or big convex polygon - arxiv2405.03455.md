# Big line or big convex polygon (Conlon–Fox–He–Mubayi–Suk–Verstraëte, arXiv:2405.03455, 2024)

Source: https://arxiv.org/pdf/2405.03455
Full text also: `research/sources/conlon-fox-he-mubayi-suk-verstraete - Big line or big convex polygon - arxiv2405.03455.HTML.full.md` (HTML conversion, theorems readable).

## What it establishes

Let $ES_\ell(n)$ be the minimum $N$ such that every $N$-point planar set contains either
$\ell$ collinear members or $n$ points in convex position. ($\ell=3$ is the exact ES problem:
a set in general position has no 3 collinear members.)

- **Theorem 1.1.** There is $C>0$ such that for all $\ell,n\ge3$,
  $$ ES_\ell(n) \le \ell^2 \cdot 2^{\,n + C\sqrt{n\log n}}. $$
  When $n$ is fixed and $\ell\to\infty$, their cups-caps theorem gives $ES_\ell(n)=O(\ell)$ (best possible up to constants).
- **Theorem 1.2 (lower bound).** For all $\ell,n\ge3$,
  $$ ES_\ell(n) \ge (3\ell-1)\cdot 2^{n-5} + 1. $$
  For $\ell=3$ this gives $ES_3(n)\ge 8\cdot 2^{n-5}+1 = 2^{n-2}+1$, agreeing with the classical ES lower bound.

## Why it matters for THIS run (the exact ES conjecture)

This is the second of two genuinely valuable threads, both **adjacent machinery**, not direct
tools for the exact constant $2^{n-2}+1$ — the same caveat as Suk / HMPT:

1. **New cups-caps theorem for arbitrary point sets (Theorem 2.1).**
   Let $f_\ell(m,n)$ be the least $N$ such that every $N$-point set contains either $\ell$
   collinear members, an $m$-cup, or an $n$-cap. Erdős–Szekeres proved
   $f_3(m,n)=\binom{m+n-4}{n-2}+1$ exactly. Conlon–Fox–He–Mubayi–Suk–Verstraëte prove, for $\ell\ge3$,
   $$ f_\ell(m,n) \le c\,(\min\{m-1,n-1\}+\ell)\binom{m+n-4}{n-2} $$
   with $c=10/\varepsilon$ from Beck's theorem (Lemma 2.2), via the Moshkovitz–Shapira down-set counting
   (`#down-sets in [m-2]×[n-2] = \binom{m+n-4}{n-2}`) plus a Beck-type line-counting lemma.
   Their **lower bound (Theorem 2.3)**:
   $$ f_\ell(m,n) > \tfrac{\ell-1}{2}\binom{m+n-4}{n-2} - \tfrac{\ell-3}{2}\binom{m+n-6}{n-3}, $$
   via an explicit recursive $X_{\ell,m,n}$ construction. The dependence on $\ell$ is $O(\ell)$,
   and the correct dependence on $\ell$ is left open.

2. **New positive-fraction cups-caps theorem for arbitrary point sets (Theorem 3.1).**
   For $N > c_1\ell\,2^{32k}$, there is a $k$-subset $X\subset P$ forming a $k$-cup or $k$-cap
   whose support regions $T_1,\dots,T_{k-1}$ each contain $\ge N/2^{32k}$ points of $P$; in
   particular every transversal (one point from each $T_i$) is in convex position. This directly
   parallels the run's established **positive-fraction ES theorem** (Bárány–Valtr) and the
   `es_construct` transversal-convexity finding. The engine is simplicial partitions (Matoušek/
   Chan; Lemma 3.2), the probabilistic method, and the ES cups-caps theorem used on a transversal.
   The Pach–Solymosi positive-fraction cups-caps theorem is the $\ell=3$ special case.

## Relevance / caveat

Both theorems are about the *relaxed* ES problem where up to $\ell$ collinear points are
allowed, and both upper bounds are of the suppressed-$2^{n+o(n)}$ asymptotic type rather than
the exact $2^{n-2}+1$. Recorded as **adjacent machinery and context**, NOT as a tool for the
exact conjecture (per GOAL.md drift guard). What is genuinely new here and worth the run's
attention: the Moshkovitz–Shapira down-set–binomial connection in the cups-caps upper-bound
proof (Theorem 2.1's proof), and the positive-fraction structural framework (Theorem 3.1) that
relates to the transversal-convexity direction.

Status: asserted-by-source (arXiv 2024, not journal-verified in this library). The $\ell=3$
case recovers the known $f_3$ exact value and the ES lower bound, which is a consistency check
only, not an independent verification.

```claim
id: cfhmsv-big-line-big-convex
statement: For ES_ℓ(n) = min N such that every N-point planar set contains ℓ collinear members or n in convex position: (Thm 1.1) ES_ℓ(n) ≤ ℓ^2 · 2^{n+C√(n log n)}; (Thm 1.2, lower bound) ES_ℓ(n) ≥ (3ℓ−1)·2^{n−5}+1, which for ℓ=3 recovers the classical 2^{n−2}+1 lower bound. New cups-caps theorem for arbitrary point sets (Thm 2.1): f_ℓ(m,n) ≤ c(min{m−1,n−1}+ℓ)·C(m+n−4,n−2), with c=10/ε from Beck's line lemma, via the Moshkovitz–Shapira down-set count (#down-sets in [m−2]×[n−2] = C(m+n−4,n−2)); lower bound (Thm 2.3): f_ℓ(m,n) > (ℓ−1)/2·C(m+n−4,n−2) − (ℓ−3)/2·C(m+n−6,n−3), via an explicit X_{ℓ,m,n} construction. New positive-fraction cups-caps (Thm 3.1): for N > c_1·ℓ·2^{32k} there is a k-cup or k-cap whose support regions each contain ≥ N/2^{32k} points of P, and every transversal (one point per region) is in convex position — engine: simplicial partitions (Matoušek/Chan) + probabilistic method + ES cups-caps; parallels Bárány–Valtr positive-fraction ES and the es_construct transversal-convexity finding.
hypotheses: ℓ,n,m,k ≥ 3; point sets with no ℓ collinear members; distinct x-coordinates (else rotate the plane, per the paper); C, c_1, ε absolute constants. ℓ=3 is exactly general position.
holds-here: adjacent machinery and context for the exact ES(n)=2^{n−2}+1 conjecture. Both upper bounds are suppressed 2^{n+o(n)} asymptotic type — the same caveat as Suk / HMPT; they do NOT bear on the exact constant. The Moshkovitz–Shapira down-set–binomial relation in Thm 2.1's proof and the positive-fraction structural framework (Thm 3.1) are the pieces worth the run's attention.
falsifies: a concrete f_ℓ(m,n) below the claimed lower bound, or an N-point set with no ℓ collinear and no m-cup/n-cap below the upper bound — not expected, theorems are proved in the source. The ℓ=3 recovery of the classical values is a consistency check, not an independent verification.
status: asserted-by-source (arXiv:2405.03455, 2024; not journal-verified in this library).
anchor: research/sources/conlon-fox-he-mubayi-suk-verstraete - Big line or big convex polygon - arxiv2405.03455.HTML.full.md
```
