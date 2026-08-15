# Fractional chromatic number: the LP over the independent-set polytope

**Subject.** The definition, LP-duality structure, and bounds of the **fractional
chromatic number** `chi_f(G)` — the mathematical backbone of the run's
`fractional-chromatic-lp-lower-bound` approach and of the never-yet-executed
calibration script `code/frac_chro_calib.py` (expects `chi_f(C5)=5/2`,
`chi_f(diamond)=3`, `chi_f(Moser)<=4`). This is the primary reference tier for
that thread; no such source was previously in the library.

## Sources

- **E. Scheinerman & D. Ullman, *Fractional Graph Theory: A Rational Approach
  to the Theory of Graphs*** (Wiley 1997; Dover reprint 2011; copyright reverted
  to the authors, who allow free download/print/copy with notice retained).
  Chapter 3 "Fractional Coloring".
  URL (author-hosted PDF): `http://www.ams.jhu.edu/~ers/fgt`
  Mirrored at `https://www.ams.jhu.edu/ers/wp-content/uploads/2015/12/fgt.pdf`
  (direct `download_document` blocked at this run's network boundary; content
  retrieved server-side via `read_sources`).
  Bibliography: MR2963519 (Dover 2011), ISBN 978-0-486-48593-5.
- **Szabó, *Estimating the fractional chromatic number of a graph*,
  Acta Univ. Sapientiae Informatica 13 (2021), DOI 10.2478/ausi-2021-0006** —
  the LP/duality formulation and a manageable LP relaxation that avoids
  enumerating all independent sets.
- **Pirot & Sereni, *Fractional Chromatic Number, Maximum Degree, and Girth*,
  SIAM J. Discrete Math. (2021), DOI 10.1137/20m1382283** — LP definitions and
  the `omega <= chi_f <= chi <= Delta+1` chain and perfect-graph equality.
- **Bonamy, Hylasová, Kaiser, Sereni, *Lower bound on the maximum denominator
  of fractional chromatic numbers*, Electr. J. Combin. (2025), DOI 10.37236/14524**
  — the `(p:q)`-colouring view and rationality of `chi_f`.

## What they establish (as retrieved, primary sources)

### Definition (primal LP over the independent-set polytope)
Let `I(G)` be the family of independent sets of `G`. `chi_f(G)` is the optimum
of

    min  sum_{I in I(G)} x_I
    s.t. sum_{I in I(G): v in I} x_I  >=  1   for every vertex v,
         x_I >= 0.

A *fractional colouring* of weight `w` is a feasible solution with total weight
`w`. A proper `k`-colouring is the special case `x_I = 1` on the `k`
monochromatic independent sets and `0` elsewhere.

### Dual LP and fractional clique number
The dual is the *fractional clique* problem

    max  sum_{v in V} w_v
    s.t. sum_{v in I} w_v <= 1   for every independent set I,
         w_v >= 0,

whose optimum is the **fractional clique number** `omega_f(G)`. **Strong LP
duality gives `chi_f(G) = omega_f(G)`**, and both are rational.

### Equivalent forms
- **(a:b)-colouring / b-fold colouring**: assign each vertex a `b`-subset of a
  palette of `a` colours so adjacent vertices get disjoint sets; `chi_f(G)` is
  the infimum (attained) of `a/b` over feasible `(a:b)`-colourings, equivalently
  `chi_f(G) = lim_b chi_b(G)/b` where `chi_b(G)` is the least `a` admitting an
  `a:b`-colouring.
- **Weight-ratio form**: `chi_f(G) = max_{w >= 0, w != 0} (sum_v w_v)/alpha_w(G)`,
  where `alpha_w(G)` is max weight of an independent set under weight `w`.
- Restricting to `{0,1}` weightings gives the **Hall ratio**
  `rho(G) = max_{H <= G} |V(H)|/alpha(H)`, with `rho(G) <= chi_f(G)`.

### Bounds
`omega(G) <= chi_f(G) <= chi(G) <= Delta(G)+1`. Equality `chi_f = chi = omega`
for perfect graphs. `chi_f` is always rational.

## Values used by the calibration script

- **`chi_f(C5) = 5/2`.**

  Closed form for odd cycles: `chi_f(C_{2k+1}) = (2k+1)/k = 2 + 1/k`
  (`chi_f(C_n) = n/alpha(C_n)`, `alpha(C_{2k+1}) = k`). Consistent across all
  sources and with the script's expectation `5/2`.

- **Diamond (K4 minus an edge): `chi_f = 3`, matching `code/frac_chro_calib.py`.**
  Resolution: the diamond is chordal, hence perfect, and for perfect graphs
  `omega(G) <= chi_f(G) <= chi(G)` collapses: `omega = chi = 3` forces
  `chi_f = 3`. Some secondary sources read the diamond as `5/2`; those are
  wrong. (My earlier draft of this note flagged the discrepancy as unresolved
  and asked for a program — the perfect-graph argument in the parallel note
  `fractional-chromatic-number-lp-definition.md` settles it in closed form; an
  exact LP run is still a worthwhile independent check.)

- **Triangle-free does NOT imply `chi_f <= 2`.** This common claim is false:
  `C5` is triangle-free with `chi_f(C5)=5/2 > 2`. `chi_f <= 2` holds exactly for
  bipartite graphs. (One retrieved secondary source asserted the false claim;
  the `C5` counterexample refutes it. Recorded so the run does not rely on it.)

- **Moser spindle**: `chi_f(Moser) <= chi(Moser) = 4` (upper bound only, from
  the chain); the script's expectation `chi_f(Moser) <= 4` is consistent but the
  exact value is a computation.

## Bearing

For a unit-distance graph `G`, `chi_f(G) > 4` would be a certified LP lower
bound `chi(G) >= ceil(chi_f) > 4` (i.e. non-4-colourability) without a SAT
search — the goal of the `fractional-chromatic-lp-lower-bound` approach, which
scales where SAT cannot. The chain guarantees `chi_f` is a genuine relaxation of
`chi`, so a graph can only be certified non-4-colourable by `chi_f` if it truly
is; the importance of the `chi_f(plane)` analogue (Hadwiger–Nelson fractional
version, Scheinerman–Ullman §3.6) is that known bounds there are strictly
inside `[4,7]`, so `chi_f` is a *strictly weaker* certificate than the
orthodox SAT oracle — its value here is as a cheap negative filter and as a
second independent route.

## Claim
The fractional-chromatic theorem behind this thread (LP duality, `omega <= chi_f
= omega_f <= chi`, the weight-ratio identity, the chain, and the calibration
value `chi_f(C5)=5/2`, `chi_f(diamond)=3`) is recorded by the parallel source
note **`fractional-chromatic-number-lp-definition.md`** under claim id
`fractional-chromatic-lp-duality` (and `fractional-chromatic-chain`). This note
deliberately carries **no duplicate claim block** so the ledger stays
single-sourced: the canonical record is the other file. What this note adds is
the **primary textbook bibliographic record** — Scheinerman & Ullman,
*Fractional Graph Theory* (Wiley 1997 / Dover 2011), the canonical reference for
the subject that the other note cites but could not fetch, now recorded with its
author-hosted URL and MR number.

## What could not be obtained
The full verbatim text/PDF of Scheinerman–Ullman could not be held as a raw
file — direct `download_document` to the author-hosted PDF and to the
publisher/AMS hosts is blocked at the network boundary. The definitions,
dualities, bounds and the §3 table of contents were retrieved server-side via
`read_sources`. (The `chi_f(diamond)=3` value is settled by the perfect-graph
argument above, and the parallel note `fractional-chromatic-number-lp-definition.md`
records it; an exact LP run remains a worthwhile independent check, which the
scholar's `scholar_frac_chro_calib.py` and my `lib/frac_chro_verify.py` exist
to perform — neither had produced captured output at the time of writing.)
