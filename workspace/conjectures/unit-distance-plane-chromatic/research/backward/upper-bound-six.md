# Upper bound: chi(G) <= 6

```skeleton
goal: prove chi(G) <= 6 for the unit-distance graph G on R^2
implies: U-six-colouring supplies a 6-colouring c: R^2 -> {1,...,6} whose same-colour pairs are all at distance > 1, with the minimum same-colour distance certified exactly. Then no two points at distance exactly 1 receive the same colour, so c is proper for G, giving chi(G) <= 6. Together with the standing lower bound chi(G) >= 4 (7-vertex graph, reproduced) this narrows the known gap to 4 <= chi(G) <= 6.
status: sketched
rests-on: none
```

```gap
id: U-six-colouring
lemma: there is an explicit 6-colouring of R^2 with the infimum of |x-y| over same-colour pairs strictly greater than 1, the margin stated as an exact algebraic number and certified.
status: open
next: tool_builder/symbolic_math: implement candidate 6-colour tilings (hexagonal and square/triangular recolourings, boundary rule included), compute the exact minimum same-colour distance symbolically for each, and report any with margin > 1.
```
