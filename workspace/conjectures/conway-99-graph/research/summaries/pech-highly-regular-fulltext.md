# Pech, "On highly regular strongly regular graphs" — full-text summary

**Source**: Christian Pech, *Algebraic Combinatorics* 4 (2021) no. 5, pp. 843-878,
doi 10.5802/alco.183. Open access. Full text:
`research/sources/pech-highly-regular-fulltext.full.md`.
(Companion capture `pech-highly-regular-alco.full.md` holds only front matter +
references; this is the complete primary text.)

## The theorem this run relies on — Theorem 5.7, PROVED here

**Statement.** Let Γ be the point graph of a partial quadrangle PQ(s,t,μ). Then Γ
is (2,5)-regular, i.e. it satisfies the 5-vertex condition.

**Proof (given in full).** For a PQ point graph Γ, #(Γ,T1)=(s−1)(s−2), and the
only graph type needing a check for the 5-vertex condition (all others contain
K4−e as an induced subgraph, which a PQ point graph cannot contain by Cameron's
characterization Thm 5.5) has count #(Γ,T2)=(s−1)(s−2)(s−3). Both counts are
constant, independent of the distinguished pair. So the 5-vertex condition holds
for EVERY partial quadrangle point graph.

**Direct consequence for the run's adopted approach (`pq-2-6-2-classification`).**
The 5-vertex condition is **INERT as a differentiator**: it holds uniformly for
rook(3)=PQ(2,1,2), BvLS=PQ(2,10,2), and any hypothetical srg(99,14,1,2)=PQ(2,6,2)
alike. It cannot separate 99 from the controls. This is analogous to the 4-vertex
condition (already known inert). The first hierarchy rung where a non-rank-3, non-GQ
PQ could differ from the rank-3 controls is the **6-vertex condition**:
- Prop 5.8: for a PQ point graph, the 6-vertex condition reduces to checking 8
  graph types (transversal of isomorphism classes of (2,6)-types whose Env is
  3-connected and whose underlying graph avoids K4−e).
- Prop 5.9: for a GQ point graph, it further reduces to 5 types (Reichard showed
  5 of the 8 are T-regular for every GQ), with explicit counts given.
Since 99 is a PROPER PQ (not a GQ: μ=2 ≠ t+1=7), the 6-vertex differentiator must
be tested against the 8 PQ types of Prop 5.8, not the 5 GQ types.

## Other content

- Unifies strong regularity, k-isoregularity, and the t-vertex condition via a
  category-theoretic composition/decomposition theory.
- GQ(q,q²) point graphs are (3,7)-regular (strengthening Reichard's 7-vertex);
  PQ(q−1,q²,q²−q) point graphs satisfy the 6-vertex condition (Cor 5.19).
- Thm 5.5 (Cameron): Γ is a PQ point graph iff μ>0 and Γ has no induced K4−e;
  a PQ is recovered from its point graph by taking maximal cliques as lines, with
  parameters (λ+1, k/(λ+1)−1, μ).
- Thm 5.10 (Cameron's inequality) with equality iff every triad has a constant
  number c of centers, c = 1+(μ−1)(μ−2)/(s(t−1)).
- Remark 5.6: proper partial quagles include triangle-free srgs (PQ(1,t,μ):
  pentagon, Petersen, Clebsch, Hoffman–Singleton, Gewirtz, Mesner, Higman–Sims)
  and PQ(q−1,q²,q²−q) / hemisystem constructions from GQ(q,q²). No construction
  gives s=2 proper PQs — the thin open rung that 99 occupies.

## Relevance

Gives the primary-source proof behind claim `bik-5vertex-holds-for-pq`
(upgrades it from asserted-by-survey to proved-by-source), and redirects the
live 5-vertex "differentiator" rung of the adopted approach upward to the
6-vertex condition. The 5-vertex condition is necessary but inert; the 6-vertex
condition on the 8 PQ types of Prop 5.8 is where a non-rank-3 99-graph has room
to fail where the rank-3 controls do not.
