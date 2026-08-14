# Erdős's unit distance problem and rigidity — Pach, Raz, Solymosi (2025)

**Source:** doi.org/10.4230/lipics.socg.2026.83 (SoCG 2026, published 2025-07)
**Authors:** János Pach, Orit E. Raz, József Solymosi
**Full text:** NOT on disk — read via server-side read_sources over the DOI
landing (abstract + the paper's own theorem statements).

## What this establishes — the rigidity route to u(n)

This is the current (2025) statement of the rigidity programme the library
already holds secondhand from the PRS unit-distance-rigidity note. It updates
and sharpens three claims:

- **Raz–Solymosi Theorem 5 (ESTABLISHED).** Let G = ([n], E), α > 1/2, and
  suppose |E| = Ω(n^{1+α}). Let p ∈ (R²)ⁿ be a realization of G in which, for
  every vertex v, the neighbours of v are not embedded into a common line.
  Then, for n large enough, there exists a subgraph G′ ⊆ G with |V(G′)| ≥ 4
  such that (G′, p|_{V(G′)}) is a **rigid framework**.
- **Rigidity Conjecture (Conjecture 7, OPEN).** The same conclusion holds
  under the weaker hypothesis |E| ≳ n^{7/6} (equivalently |E| = Ω(n^{1+1/6})).
- **Conditional improvement of the unit-distance bound.** If Conjecture 7
  holds, then u(n) = O(n^{4/3} log^{1/12} n) — the first improvement over the
  classical Spencer–Szemerédi–Trotter O(n^{4/3}) bound, which has stood since
  1984 and has resisted Clarkson–Edelsbrunner–Guibas–Sharir–Welzl, Székely,
  and Pach–Tardos attacks (all yielding exactly n^{4/3}).
- **Theorem 6 (Structure Theorem).** For h(n) → ∞, a point set P of size n
  with u(P) ≥ n^{4/3}/h(n) decomposes into a large subset P′ and bipartite
  rigidity subgraphs — the near-extremal structure the run's ROOT already
  records.

## Why it matters here

The density constraint O(n^{4/3}) is the reason a minimal non-4-colourable
unit-distance graph must be *rigid* (problem.md's obstruction). This paper
gives the precise modern rigidity conjecture: any graph with more than
~n^{7/6} edges whose realization has no collinear neighbour sets contains a
rigid subframework on ≥ 4 vertices. For the run's size-lower-bound route
(G-crit: 5-critical ⇒ e ≥ 2n), the ℘-crossing point is where edge density n^{7/6}
meets chromatic forcing 2n — these are the two quantitative walls the search
operates between. The claim ledger's `prs-rigidity-conjecture` row should now
carry this 2025 statement and the established Raz–Solymosi α > 1/2 theorem.

```claim
id: prs-rigidity-conjecture-2025
statement: Rigidity conjectures for graphs with many edges and realizations with no collinear neighbour sets: (established, Raz-Solymosi Thm 5) if |E| = Omega(n^{1+alpha}) with alpha > 1/2 then a rigid subframework on >= 4 vertices exists; (open, Conjecture 7) the same for |E| ~>= n^{7/6}. If Conjecture 7 holds, u(n) = O(n^{4/3} log^{1/12} n).
hypotheses: realization p in R^2; for every vertex the neighbours are not collinear; n sufficiently large.
holds-here: yes - unit-distance realizations satisfy the non-collinearity hypothesis generically; the density threshold n^{7/6} is the wall the construction search must cross to force rigidity.
status: sourced (Pach-Raz-Solymosi SoCG 2026, DOI 10.4230/lipics.socg.2026.83; Theorem 5 established, Conjecture 7 open, conditional bound sourced); supersedes the earlier PRS rigidity claim in the unit-distance-rigidity note for the statement's modern form.
bearing: the rigidity walls for unit-distance graph density: n^{7/6} (rigid subframeworks) vs 2n (5-critical edges). Search operates between them.
anchor: research/sources/pach-raz-solymosi-rigidity-2025.md
```

## Note on download

Full text network-blocked (as for all publisher hosts in this run). Status:
**sourced via read_sources; full text not on disk**.