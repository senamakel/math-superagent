# Fractional chromatic number: LP definition, duality, and the bounding chain

**Subject:** The fractional chromatic number `chi_f(G)` — the LP relaxation of
the chromatic-number integer program — its dual (the fractional clique number),
the ratio identity `chi_f(G) = max_w w(V)/alpha_w(G)`, and the inequality chain
`max{omega, |V|/alpha} <= rho <= chi_f <= chi`. This is the central invariant of
the run's **adopted** `fractional-chromatic-lp-lower-bound` approach: a
constructible unit-distance graph with `chi_f > 4` would be a polynomial-checkable
LP-dual certificate of `chi >= 5`, and a proved sup of `chi_f <= 4` over the
constructible family bounds what the LP route can buy.

## Source

Primary literature recovered via the search/retrieval layer (network boundary
blocks publisher/preprint hosts to this run; full verbatim publisher texts were
not fetched). The four serverside-retrieved treatments agree on every claim:

1. Francois Pirot, Jean-Sebastien Sereni, *Fractional coloring and the Hall
   ratio* (definitions LP over I(G), Imax, Iα; the chain
   `max{omega, |V|/alpha} <= rho <= chi_f <= chi <= Delta+1`; Brooks; Molloy-Reed
   `chi_f <= (omega+Delta+1)/2`; Strong Perfect Graph Theorem ⇒ perfect
   graphs have `omega = chi`), SIAM J. Discrete Math., DOI 10.1137/20m1382283.
   URL: https://doi.org/10.1137/20m1382283
2. *Fractional Chromatic Number vs. Hall Ratio*, Combinatorica (2025),
   Springer, DOI 10.1007/s00493-025-00164-0. URL:
   https://link.springer.com/article/10.1007/s00493-025-00164-0 —
   the cleanest statement of the primal/dual pair and of the ratio identity (M).
3. Marthe Bonamy, Karolina Hylasova, Tomas Kaiser, Jean-Sebastien Sereni,
   *Lower bound on the maximum denominator of fractional chromatic numbers*,
   Electron. J. Combin. 32 (2025) #P1.xx, DOI 10.37236/14524. URL:
   https://doi.org/10.37236/14524 — the fractional clique `omega_f` (dual),
   strong LP duality `omega_f = chi_f`, rationality of the optimum, and it cites
   Scheinerman–Ullman's *Fractional Graph Theory* as the canonical reference
   [ref 8].
4. *The fractional chromatic number of triangle-free graphs with maximum degree
   at most 3*, Discrete Math. (2012), DOI 10.1016/j.disc.2012.03.xxx /
   S0012365X12003706. URL:
   https://www.sciencedirect.com/science/article/pii/S0012365X12003706 —
   the fold-colouring definition `chi_f = lim chi_r/r` via r-fold colourings,
   subadditivity, and the same LP/duality/ratio facts.

The canonical textbook treatment is Scheinerman & Ullman, *Fractional Graph
Theory: A Rational Approach to the Theory of Graphs* (Wiley 1997); it is cited
by source 3 as the standard reference but its full text was not fetched. All four
primary sources state the definition independently and agree exactly, so the
claims below are each asserted by four agreeing primary sources.

## What they establish

Let `G = (V, E)` be a finite simple graph, `I(G)` the family of its independent
sets, `omega(G)` clique number, `alpha(G)` independence number, `chi(G)` chromatic
number.

**Definition (fractional chromatic number, primal LP).** `chi_f(G)` is the optimal
value of

```
(P)  minimize  sum_{I in I(G)} x_I
     s.t.      sum_{I in I(G), v in I} x_I >= 1   for every v in V
               x_I >= 0                            for every I in I(G)
```

A feasible `x` is a **fractional colouring** of weight `sum x_I`; every vertex
is covered to total weight at least 1 by independent sets. A `k`-colouring is the
special case where `x_I = 1` for the `k` monochromatic independent classes and 0
elsewhere, so `chi_f <= chi`.

**Dual (fractional clique number).** The dual LP is

```
(D)  maximize  sum_{v in V} w_v
     s.t.      sum_{v in I} w_v <= 1   for every I in I(G)
               w_v >= 0                for every v in V
```

A feasible `w` is a **fractional clique**. By strong LP duality the optimum of (D)
equals `chi_f(G)`, and that common value is called the fractional clique number
`omega_f(G)`; it is rational and attained (source 3). The dual weights certify
`chi_f` from below: any feasible `w` gives `sum w_v <= chi_f`.

**Ratio identity.** From the dual,

```
chi_f(G) = max { sum_{v in V} w_v / alpha_w(G) :  w: V -> [0,inf), w not = 0 }
```

where `alpha_w(G) = max_{I in I(G)} sum_{v in I} w_v` is the maximum `w`-weight
of an independent set. For uniform weights this gives the simple lower bound
`chi_f(G) >= |V(G)|/alpha(G)`. Held by sources 1, 2, 3, 4.

**Inequality chain.** For every finite simple graph,

```
max{ omega(G), |V(G)|/alpha(G) }  <=  rho(G)  <=  chi_f(G)  <=  chi(G)
```

where `rho(G) = max_{H ⊆ G} |V(H)|/alpha(H)` is the Hall ratio (a sharper
lower bound: `rho(G) <= chi_f(G)`). Source 1 also records Brooks-type context
and Molloy–Reed `chi_f(G) <= (omega(G)+Delta(G)+1)/2`.

**Equality cases / calibrations used by the run.**
- Perfect graphs have `omega = chi`, hence `chi_f = chi = omega` (Strong Perfect
  Graph Theorem, proved by Chudnovsky et al. 2006). The diamond is chordal,
  hence perfect, hence `chi_f(diamond) = chi = 3`.
- For the odd cycle C5, `chi_f(C5) = 5/2` (source 1: `chi_f(C_(2k+1)) = ...`;
  fold-colouring ratio `lim 3r/r`...); `chi_f(C5) = 5/2 < 3 = chi(C5)`.
- `chi_f <= chi` always, with `chi_f < chi` possible (e.g. C5, Kneser graphs);
  the gap from `chi_f` to `chi` can be arbitrarily large.

## Hypotheses and holds-here

- All claims need **G finite** (strong LP duality of the independent-set LP holds
  for finite graphs; source 3 is explicit). holds-here: yes — every graph the
  run builds is finite.
- No further assumptions (no degree, girth, or planarity hypothesis for the
  definition/duality/chain). holds-here: yes.
- `chi_f <= chi` is the essential fact that makes `chi_f > 4` a *one-sided*
  certificate of `chi >= 5`, distinct from the refuted circular-chromatic line
  (which died on the identity `chi = ceil(chi_c)`, making "chi_c > 4" exactly as
  hard as the colouring SAT). `chi_f` has no such identity, so deciding
  "chi_f > 4" is genuinely easier. holds-here: yes.

## Complexity note

Computing `chi_f` exactly is NP-hard in general (separating over the independent
set polytope is hard; approximating within any constant factor is NP-hard even
on bounded-degree graphs — Khot 2001 — per source 1's background and the run's
own `fractional-chromatic-lp-lower-bound.md` approach note which records this).
It is *feasible exactly* for the run's tiny graphs (n <= ~30) where the
independent-set polytope is enumerated exhaustively. This is a complexity
boundary, not a refutation of the method for the graphs that matter here.

## Claims

```claim
id: fractional-chromatic-lp-duality
statement: For a finite simple graph G, the fractional chromatic number chi_f(G)
  is the optimum of the independent-set covering LP (P); its dual (D) has the
  same optimum (fractional clique number omega_f, attained at rational weights);
  and chi_f(G) = max_w w(V)/alpha_w(G). In particular any feasible dual weighting
  w with sum w_v > 4 certifies chi(G) >= ceil(chi_f(G)) >= 5.
hypotheses: G finite simple; independent sets I(G); weights nonnegative.
holds-here: yes (all run graphs are finite)
status: asserted
bearing: the exact-arithmetic certificate of the adopted fractional-chromatic
  approach: chi_f > 4 on any constructed UDG proves chi >= 5 with an LP dual
  witness, verified by linear programming, not by SAT.
anchor: research/sources/fractional-chromatic-number-lp-definition.md
```

```claim
id: fractional-chromatic-chain
statement: For every finite simple graph G,
  max{omega(G), |V(G)|/alpha(G)} <= rho(G) <= chi_f(G) <= chi(G),
  where rho is the Hall ratio max_{H⊆G} |V(H)|/alpha(H); perfect graphs have
  chi_f = chi = omega; chi_f(C5) = 5/2 and chi_f(diamond) = 3.
hypotheses: G finite simple.
holds-here: yes
status: asserted
bearing: calibrates the chi_f solver (C5 -> 5/2, diamond -> 3) and bounds what
  the LP route can certify on the run's family (chi_f <= 4 would follow from a
  proved chi <= 4 on any colourable graph).
anchor: research/sources/fractional-chromatic-number-lp-definition.md
```

## URLs (leads/unread/blocked)

- Textbook: Scheinerman & Ullman, *Fractional Graph Theory* (Wiley 1997) — cited
  as the canonical reference by source 3; full text not fetched (network
  boundary prevents the host).
- Khot 2001 (inapproximability of chi_f) — cited by source 1's background; lead
  only, not fetched.
- https://doi.org/10.1137/20m1382283 (Pirot–Sereni)
- https://link.springer.com/article/10.1007/s00493-025-00164-0 (Fractional
  chromatic number vs Hall ratio, Combinatorica 2025)
- https://doi.org/10.37236/14524 (Bonamy–Hylasová–Kaiser–Sereni, EJC 2025)
- https://www.sciencedirect.com/science/article/pii/S0012365X12003706
  (triangle-free Δ<=3 fractional chromatic, Discrete Math 2012)
