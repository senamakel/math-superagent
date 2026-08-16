# Makhnev — "Graphs and automorphisms" (Bielefeld summer-school lecture notes)

<!-- source: https://www.math.uni-bielefeld.de/~baumeist/sommerschule/makhnev.pdf -->

## What this source is

A lecture note by A. A. Makhnev (Krasovskii Institute / Ural Federal University),
surveying automorphisms of strongly regular and distance-regular graphs. It is a
primary-ish source that reproduces, with attribution to `[3]` = Makhnev–Minakova
and `[4]` = Wilbrink 1984, the key automorphism results for the (99,14,1,2) graph.
This is the only library route to the content of **Wilbrink 1984** ("On the
(99,14,1,2) strongly regular graph", Papers dedicated to J. J. Seidel, Tech.
Report 84-WSK-03, TU/Eindhoven 1984, pp. 342–355), which is otherwise paywalled
and unobtainable.

## What it establishes (all for Γ = a putative srg(99,14,1,2))

**Seidel Problem / spectrum.** The existence of srg(99,14,1,2) was posed as
"Seidel Problem". If it exists: `[a]` (neighbourhood of any vertex) is the union
of 7 isolated edges (i.e. locally `7K₂` — confirms claim `c5`); spectrum is
`14^1, 3^54, −4^44` (confirms `integrality-five-members`); and the character of
the projection onto the 54-dim eigenspace is

```
χ2(g) = (4α0(g) + α1(g) − 18)/7
```

where `αi(g)` is the number of g-orbits of size i on vertices. This is the
workhorse identity behind every fixed-point dichotomy.

**Involutive automorphisms (Makhnev–Minakova 2004, `[3]`).** If t is an
involution, `Fix(t)` must be one of: (1) one-vertex graph; (2) triangle; (3)
three isolated triangles; (4) a vertex and two isolated triangles; (5) four
isolated vertices and a triangle; (6) an n-coclique, n = 3, 5, or 7; (7) a
3×3-grid. Only case (1) gives integer `χ2(t)`, via the identity above (worked
example given for case (5): `α1(t)=20`, `χ2(t)=(28+20−18)/7` = noninteger).

**Theorem 1 (Makhnev–Minakova `[3]`): fixed-point dichotomy for prime order p.**
For `g ∈ Aut(Γ)` of prime order p with `∆ = Fix(g)`:
1. `∆` is a one-vertex graph and `p = 2 or 7`;
2. `∆` is the empty graph and `p = 3 or 11`;
3. `∆` is a triangle and `p = 3`.

**Wilbrink's result (`[4]`, 1984).** The lecture states verbatim:

> H. Wilbrink [4] proved that Γ does not admit an automorphism of order 11. In
> particular, the order of the automorphism group of strongly regular graph with
> parameters (99, 14, 1, 2) divides 2 · 3³ · 7.

This is the library's on-record attribution of the **order-11 exclusion and the
`|G| | 2·3³·7` bound** to Wilbrink 1984 (the "divides 42 when an involution
exists" strengthening is Makhnev–Minakova).

**Corollary 1 (Makhnev–Minakova).** If G = Aut(Γ) contains an involution t,
then `|G|` is divisible by 7 and divides 42; `[O(G), t] = 1`; and in the case
`|G| = 42` the subgroup O(G) is nonabelian.

## Quotation vs interpretation

The statements in §3–§4 are quoted essentially verbatim from the lecture, whose
author is Makhnev himself reporting his own and Wilbrink's theorems, so this is
close to primary for these results. The numerical example in case (5) of the
involution classification is worked in the text. Nothing here has been
re-verified by this run's oracle (they are structural-for-any-putative-graph
statements, not oracle-decidable problems); they stand as `asserted-by-source`
but now with a traceable primary-source citation for the first time, which
promotes the "asserted, unverified" rows `aut-bounds-established` and
`automorphism-orders-consolidated` from "recalled, uncited" to "sourced".

## Where the full text lives

`research/sources/makhnev-symmetric-graphs-automorphisms-lecture.full.md`
(line 179 onward for the (99,14,1,2) content; reference `[4]` = Wilbrink at line 1515).
