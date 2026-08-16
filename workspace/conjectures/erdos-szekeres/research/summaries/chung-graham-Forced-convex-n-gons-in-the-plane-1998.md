# Chung & Graham 1998, "Forced convex n-gons in the plane", DCG 19(3):367–371

Source: https://fanchung.ucsd.edu/wp/forced.pdf (author's open-access PDF; published Decimate
Comput. Geom. 19 (1998) 367–371, DOI 10.1007/PL00009353, special issue in memory of Paul Erdős).
Full text: [[chung-graham-Forced-convex-n-gons-in-the-plane-1998.full]]

The first improvement to the Erdős–Szekeres upper bound in over 60 years, and the origin of the
"defective point / left-right-endpoint" graph method that Kleitman–Pachter and Tóth–Valtr
immediately refined. This closes the historical gap in the library between the 1935 binomial bound
and Tóth–Valtr.

## What it establishes

- **Theorem.** For $n \ge 4$, $g(n) \le \binom{2n-4}{n-2}$. That is, the "$+1$" is removed from the
  original ES upper bound $g(n) \le \binom{2n-4}{n-2}+1$. (Recall $\binom{2n-5}{n-3} = \frac12\binom{2n-4}{n-2}$.)
- Uses the ES cup/cap dichotomy (Lemma 1, sharp): $|X| > \binom{a+b-4}{a-2}$ forces an $a$-cap or a
  $b$-cup.
- Believes (with ES) the lower bound is the truth: $g(n)=2^{n-2}+1$, but admits little real evidence.

## The method (structural, worth holding)

1. Rotate/compress so every pair-line has slope in $(-0.1, 0.1)$, no pair horizontal/vertical.
2. Let $A = \{x \in X : x \text{ is the left-hand endpoint of some }(n-1)\text{-cap}\}$,
   $B = X \setminus A$.
3. Case analysis on $|A|$ vs $\binom{2n-5}{n-3} = \frac12\binom{2n-4}{n-2}$:
   - if $|A|$ too big, Lemma 1 gives an $(n-1)$-cup in $A$, whose last vertex is in $A$ hence a cap
     left-endpoint, forcing an $n$-cup or $n$-cap → convex $n$-gon.
   - if $|A|$ too small, same for $B$.
   - equality: every $b \in B$ is the right endpoint of an $(n-1)$-cup with left endpoint in $A$, and
     every $a \in A$ left endpoint of an $(n-1)$-cap with right endpoint in $B$.
4. Form a directed bipartite graph $G$ on $A\cup B$: edge $(u,v)$ if $u$=left end, $v$=right end of an
   $(n-1)$-cap (or reversed for cups). Every vertex has outdegree ≥ 1, so $G$ has a directed cycle
   $a_{i_1} b_{i_1} \cdots a_{i_r} b_{i_r}$.
5. **Geometry closes it:** each edge's "forbidden region" $Y(a,b)$ (below the polyline
   $L_+(a)+S(a,b)+R_-(b)$, where $L_\pm$ are slope-±0.1 downward half-lines) contains no point of $X$,
   else a convex $n$-gon. Adjacent edges force each new vertex to lie strictly above/below the
   previous edge line. Around the cycle, slopes of consecutive edge-lines strictly increase, yet all
   lie in $(-0.1,0.1)$ and the total turn is a full cycle < $\frac12\pi$ — contradiction.

## Why it matters for this run

It is the first "structural counting" beyond pure Ramsey cups-caps. The $A/B$ split and the directed
cycle with slope-monotonicity is a template: any exact bound must find *why forbidden local
configurations cannot close*, and here the closure fails on a geometric slope/cycle ground, not on a
pure count. It is the historical seed of the Kleitman–Pachter (bound
$\binom{2n-4}{n-2}+7-2n$) and Tóth–Valtr ($\binom{2n-5}{n-2}+2$) refinements, both citable from this
library.

```claim
id: cg98-first-improvement
statement: ES(n) -> g(n) <= C(2n-4, n-2) for n >= 4 (removes the +1 from the 1935 upper bound).
hypotheses: n >= 4
holds-here: yes
status: proved
bearing: the first structural-count improvement over the ES binomial bound; origin of the A/B
        left-right-endpoint graph-decomposition method. Superseded as a bound but the method is
        historically load-bearing for the run's exact-argument goal.
anchor: research/sources/chung-graham-Forced-convex-n-gons-in-the-plane-1998.full.md
```
