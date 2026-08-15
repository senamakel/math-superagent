# Dirac 1957: on the number of edges in colour-critical graphs

**Subject:** The classical origin of the edge-count lower bound for k-critical
graphs — the first nontrivial result beyond the trivial min-degree bound, and
the root of the Gallai–Krivelevich–Kostochka–Yancey ladder the size-bound rung
rests on.

## Source
- G. A. Dirac, *A theorem of R. L. Brooks and a conjecture of Hadwiger*,
  Proc. London Math. Soc. (3) 7 (1957) 161–195. The edge-bound cited here is
  the classical "Dirac bound" on colour-critical graphs, recorded via the
  secondary statement in Kostochka–Stiebitz 2002 (J. Graph Theory 39, DOI
  10.1002/jgt.998) and the Kostochka–Yancey revision history. Retrieved via
  server-side retrieval; full text blocked at this run's network boundary.
- Source URL: https://doi.org/10.1002/jgt.998 (Kostochka–Stiebitz restatement)

## Exact statement

**Theorem (Dirac 1957).** Every k-colour-critical graph (k >= 4) on
`n >= k + 2` vertices has at least

    |E(G)| >= (1/2)( (k-1)n + k - 3 )

edges.

For `k = 5`: `|E| >= (1/2)(4n + 2) = 2n + 1` — average degree strictly above
`4` (this is the "average degree > 4" edge of a 5-critical graph; it comes from
`(1/2)(4n + 2)/n = 2 + 1/n` edges per vertex, degree `4 + 2/n`).

**Place in the ladder (identical hypotheses, improving estimate):**

| Bound | Edges per vertex | Source |
| --- | --- | --- |
| trivial (min degree) | (k-1)/2 | folklore |
| **Dirac 1957** | (1/2)(k-1) + (k-3)/(2n) | this paper |
| Gallai 1963 | (k-1)/2 + (k-3)/(2(k^2-3)) | Gallai |
| Krivelevich 1997 | (k-1)/2 + (k-3)/(2(k^2-2k-1)) | `krivelevich-1997-critical-edge-bound` |
| **Kostochka–Yancey 2014** | (k+1)(k-2)/(2(k-1)) | `kostochka-yancey-2014` |
| (k=5 value) | 2.25 n edges | — |

Dirac's is the first to beat the linear `(k-1)/2 n`; KY is the sharpest.

## Why it matters here
The size-bound rung's analytical route ("every unit-distance graph on at most N
vertices is 4-colourable") reduces to: a minimal 5-chromatic (5-critical)
unit-distance graph must have edge count above Dirac (and KY) lower bounds,
but the unit-distance density ceiling `u_2(n)=O(n^{4/3})` caps its edges — the
clash bounds N. Dirac's bound (`>= 2n+1` for k=5) is the weakest leg of that
clash and is where the run's refuted discharging computation ground away, but it
is the historically and structurally load-bearing first rung. The run's own
`critical-minimum-degree` claim (every 5-critical graph has min degree >= 4) is
the trivial rung that Dirac's theorem strengthens.

## Basis and status
- Statement as restated by Kostochka–Stiebitz (2002) and the KY survey; the
  original Dirac paper's full text is blocked at this run's network boundary.
  Recorded as asserted-by-source.

## Claim block
```claim
id: dirac-1957-critical-edge-bound
statement: Every k-colour-critical graph (k >= 4) on n >= k+2 vertices has
  at least (1/2)((k-1)n + k - 3) edges; for k=5 this is |E| >= 2n+1 (average
  degree > 4).
hypotheses: G finite simple k-colour-critical graph, k >= 4, n >= k+2.
holds-here: YES — a minimal 5-chromatic UDG is 5-critical, so the bound applies
  verbatim; it is the weakest leg of the size-bound clash and is subsumed by
  Kostochka–Yancey.
status: asserted-by-source (Dirac 1957, via Kostochka–Stiebitz 2002 secondary
  statement; not re-derived here).
bearing: the classical edge-count rung underlying the size-bound analysis; the
  run's `critical-minimum-degree` claim is its trivial min-degree rung.
anchor: research/sources/dirac-1957-critical-edge-bound.md
falsifies: a 5-critical unit-distance graph on n >= 7 vertices with 2n or fewer
  edges — impossible by the theorem for general graphs.
```
