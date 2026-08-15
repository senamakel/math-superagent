# Alon–Tarsi / Combinatorial Nullstellensatz coefficient certificate for non-4-colourability

```approach
idea: Certify non-4-colourability of a candidate unit-distance graph by a single
  exact integer — the Alon–Tarsi obstruction — instead of (or alongside) a SAT
  UNSAT proof. The Alon–Tarsi theorem (1992) says: if a graph G has an
  orientation D with maximum out-degree ≤ 3 and EE(D) ≠ EO(D), then G is not
  4-colourable.
mechanism: This changes the *certificate of the lower bound* from a solver
  verdict to an algebraic identity that is independent of the SAT encoding and
  its coordinates (the polynomial depends only on the edge set, so the
  certificate is an integer independent of the geometry). The search "does this
  graph have an unbalanced orientation of max out-degree ≤ 3" is a finite
  combinatorial question over orientations.
status: refuted
precedent:
  - Alon & Tarsi 1992, "Colorings and orientations of graphs", Combinatorica
    12(2):125–134, https://doi.org/10.1007/BF01204715 — the precise theorem
    (given verbatim below). THE DIRECTION IS THE OPPOSITE OF THE CANDIDATE'S.
  - Hefetz 2009, "On two generalizations of the Alon-Tarsi polynomial method",
    arXiv:0911.2099 — restates the same: EE(D)≠EO(D) with out-degree<k certifies
    AT(G)<=k, a CHOOSABILITY/UPPER bound, not a non-colorability certificate.
  - Alon & Tarsi 1992 primary statement (Princeton copy, chrom3.pdf;
    Theorem 1.1): "If D has max outdegree d and EE(D)≠EO(D), then for any
    assignment of a set S(v) of d+1 colors to each vertex v there is a legal
    vertex-coloring assigning each v a color from S(v)." So max-outdegree d with
    unbalanced parity ⇒ (d+1)-choosable ⇒ (d+1)-colourable.
  - Kozik–Podkanowicz 2023, arXiv:2303.02683; Brooks-via-AT note (2010): all
    confirm AT as an upper bound on choosability/chromatic number.
killed-by: alon-tarsi-is-upper-bound-not-noncolorability-certificate
```

## Literature verdict

**The named mathematics is correct — but the direction is exactly backwards.**
The Alon–Tarsi theorem (Combinatorica 12(2):125–134, 1992) states, verbatim:
> If G is a directed graph with maximum outdegree d, and if the number of
> Eulerian subgraphs of G with an even number of edges differs from the number
> with an odd number of edges, then for any assignment of a set S(v) of d+1
> colours for each vertex v there is a legal vertex-colouring of G assigning to
> each vertex v a colour from S(v).

An orientation with max out-degree ≤ 3 and EE(D) ≠ EO(D) therefore certifies
that G is **4-choosable, hence 4-colourable** — it proves G *is* 4-colourable,
not that it is not. This is confirmed by every secondary source found (Hefetz
arXiv:0911.2099: "AT(G) ≤ k iff there is an orientation with out-degree < k and
∉∑_H ω_D(H) = 0"; Kozik–Podkanowicz; the Brooks-via-AT note). The candidate's
"sufficient for non-4-colourability" claim inverts the theorem.

**This means the candidate's own calibration step would fail immediately:** it
proposes "K5 (not 4-colourable) must admit an unbalanced orientation of max
out-degree ≤ 3" — but the theorem guarantees such an orientation would *certify*
K5 as 4-colourable, which is absurd (chi(K5)=5). No such K5 orientation exists
with the balancing property, because K5 is not 4-choosable; and one cannot
"find" it, because it is the certificate of the *positive* statement. So the
proposal is refuted at the level of its own stated calibrations.

**What survives:** the *coefficient-extraction* half of the proposal (the
Combinatorial-Nullstellensatz identity linking EE−EO to the graph-polynomial
coefficient) is real and is exactly the Alon–Tarsi machinery. But as a
*certificate of non-4-colourability* it cannot work; at best the same coefficient
could be used as one more *positive* 4-colourability certificate, which the run
already has in SAT. It does not supply a lower-bound certificate.

**Honest limit of the finding:** the direction is settled beyond doubt from the
primary source (Alon & Tarsi 1992, retrieved verbatim) and multiple independent
re-statements; it is not a matter of absence of evidence. The file and note
`code/out/check_alon_tarsi_direction.md` spell out the calibration predictions
the candidate would have to satisfy (K4: has unbalanced orientation; K5: does
not) — which is itself the clean statement of why the inversion is fatal. Closed
as refuted on evidence, not on absence.
