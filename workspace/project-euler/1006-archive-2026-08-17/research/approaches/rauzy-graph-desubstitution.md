# Approach: Rauzy graph of the Fibonacci word and desubstitution transfer

```approach
idea: Treat the k+1 length-k factors as the vertices of the order-k Rauzy graph Gamma_k of the Fibonacci subshift (edges = length-(k+1) factors). For a Sturmian word Gamma_k is a single path carrying a single cycle, and its shape (cycle length, the two path-arm lengths) is governed by the continued fraction of the slope and by the unique bispecial factor. The Fibonacci substitution 0->01, 1->0 descends Gamma_{k+1} onto Gamma_k (desubstitution / derived sequence), so the weighted trace Psi(k) = sum over vertices of (decimal value)^2 satisfies a fixed-order linear recurrence over the Fibonacci index (k=F_m -> F_{m+1}), evaluable by matrix power in O(log k).
mechanism: Rauzy graphs and their "lollipop" (path + one cycle) structure for Sturmian words (Rauzy 1983, Arnoux-Rauzy); bispecial factors and return words; derived sequence / desubstitution by the Fibonacci morphism; a transfer matrix over the nearly-linear graph whose square-weights telescope; fast exponentiation over the Fibonacci index.
status: proposed
precedent: unchecked
first-step: From the existing factor lists (code/out/factors_k40.json) build Gamma_k for k=1..20 (vertices = length-k factors, edge u->v iff u[1..]=v[..k-1] and uv[k-1] is a length-(k+1) factor), then record for each k the unique cycle length and the two path-arm lengths; check they follow the Fibonacci/continued-fraction law (they should be the continued-fraction partial quotients of 1/phi^2). Then express sum_j value(w_j)^2 as a trace over this graph and find the substitution-induced recurrence relating k=F_{m+1} to k=F_m.
```

## Why the Rauzy graph is the right object

`Psi(k)` is a sum over the vertex set of `Gamma_k` of a vertex weight `value(w)^2`. For a
Sturmian word the order-k Rauzy graph is not an arbitrary digraph: it is a **path with exactly
one cycle** (a "lollipop"), because there is a unique right-special and a unique left-special
factor of each length. A weighted sum over vertices of such a graph is a sum along the two arms
plus a cyclic sum around the loop — each part telescopes or is a geometric series, so no
per-vertex enumeration is needed once the arm/cycle lengths are known.

The arm and cycle lengths are not new data: they are the standard "derived word" parameters,
determined by the continued fraction `[0;2,1,1,1,...]` of the slope. More importantly, the
Fibonacci morphism `0->01, 1->0` acts on Rauzy graphs: the length-`(F_{m+1})` structure is the
image of the length-`(F_m)` structure under a finite rewriting, which is exactly the kind of
relation that produces a linear recurrence in the Fibonacci index `m`. The vertex weights
`value(w)^2` transform under the morphism by a fixed linear rule (each `0` becomes `01` and each
`1` becomes `0`), so the weighted trace transforms by a fixed matrix. This is a *different
computational model* from the lex-order next-factor rule: it never orders the factors, it
exploits the subshift's return-word / desubstitution dynamics.

## What would kill it

If the order-k Rauzy graph of the Fibonacci word is *not* a single path with a single cycle at
some small k (which would contradict the Sturmian right/left-special uniqueness), or if the
morphism does not map `Gamma_k` to `Gamma_{k+1}` in a way that keeps the weight-rule finite, the
transfer must be replaced by a richer automaton. Both are checkable at k<=20 in minutes.

## Relation to the open threads

The open threads work with the *lexicographic* factor order (Perrin-Restivo). This approach
replaces the total order by the *Rauzy graph* (successor edges in the subshift), which has one
cycle instead of one linear chain, and drives the recurrence from the substitution rather than
from lex-consecutiveness.
