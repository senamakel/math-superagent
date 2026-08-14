# Screened: "Rigidity-Induced Scaling Laws in Unit Distance Graphs" — NOT admitted as a claim

**Source:** arxiv.org/abs/2601.18831 — Lucas Aloisio (2026-01), single-author
preprint. **Assessed, not admitted.**

## What the preprint claims

That dense unit-distance configurations must contain rigid bipartite Ks,t
(s,t ≥ 3) subgraphs; a "Flatness Lemma" claiming the configuration variety of
an embedded K3,3 in the plane has dimension ≤ 1 and K4,4 forces collinearity
or a 0-dimensional locus; and a headline claim that this **precludes the
n^{4/3} scaling**, i.e. u(n) = o(n^{4/3}) for non-degenerate configurations —
a result that would break a forty-year barrier the field's best programme (PRS
2026, Conjecture 7) only hopes to improve by log^{1/12} n.

## Why it was NOT filed as a claim

1. **The headline claim contradicts a load-bearing consensus.** The
   Spencer–Szemerédi–Trotter O(n^{4/3}) bound is widely believed near-tight;
   the entire rigidity programme reduces the possibility of improvement to a
   precise conjecture (PRS Conjecture 7), and even its truth only yields
   O(n^{4/3} log^{1/12} n), not o(n^{4/3}). A single 2026 preprint overturning
   this by a dimensional-collapse argument would require extraordinary
   corroboration.
2. **The Ks,t-collapse framing is consistent with an old, weaker fact, not a
   new bound.** K3,3 is not even a *unit-distance graph*: it contains K2,3,
   which is one of the two minimal forbidden graphs on ≤ 5 vertices
   (Globus–Parshall; three distinct points at unit distance from both of two
   fixed points is impossible — two unit circles intersect in at most two
   points). So a "collapse" of the K3,3 realization variety is unsurprising
   and says nothing about configurations that avoid Ks,t.
3. **The leap from "dense ⇒ contains collapsed Ks,t" to "o(n^{4/3})" is
   unproved in the excerpt**: the SST upper bound's whole mechanism is that
   such over-constrained substructures *limit* incidences; showing they cannot
   occur at all would need a degree-of-freedom/incidence argument the excerpt
   does not supply.
4. **Provenance and review status**: single-author preprint, days old in
   workspace time, no peer review visible from the landing page.

## Status for the run

Treat as **screened material, not evidence**. If the run's own exact-arithmetic
sweep ever finds a dense configuration with many near-Ks,t subgraphs, that
would be worth revisiting either way — but no claim block is filed, and
nothing in CONTEXT.md/CLAIMS.md should cite this note as establishing a bound.

```claim
id: screened-aloisio-o-n4-3-preprint
statement: A 2026 single-author preprint (arXiv 2601.18831) claims u(n) = o(n^{4/3}) via the impossibility of dense Ks,t subconfigurations; the claim is NOT admitted as evidence — it contradicts the field consensus that the 4/3-barrier is near-tight and its Ks,t premise is consistent with the known non-realizability of K2,3/K3,3.
hypotheses: n/a - this is a screening decision, not a theorem.
holds-here: n/a
status: screened - not admitted; listed so a later run does not rediscover it as a lead.
bearing: warns the run against citing or building on o(n^{4/3}) claims without extraordinary corroboration; keeps the PRS Conjecture 7 conditional improvement as the credible frontier.
anchor: research/sources/screened-aloisio-rigidity-preprint-2026.md
```

## Note on download

Full text network-blocked; assessment based on the server-side read_sources
pass over the abstract and its quoted lemma statements.