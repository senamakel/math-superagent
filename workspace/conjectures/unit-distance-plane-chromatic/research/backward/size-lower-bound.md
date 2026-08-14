# Lower bound on the size of a 5-chromatic unit-distance graph

```skeleton
goal: prove there is an N >= 1 such that every unit-distance graph on at most N vertices is 4-colourable, and certify the largest such N the run can establish
implies: suppose a unit-distance graph on at most N vertices with chi >= 5 exists and take a vertex-minimal one; G-crit makes it 5-critical, so it lies in the class G-exhaust sweeps. G-exhaust is complete over all 5-critical unit-distance graphs on at most N vertices and certifies none exists; contradiction. Hence every unit-distance graph on at most N vertices is 4-colourable. Uses the oracle pair G-oracle of lower-bound-five.md for exact edge certification and complete 4-colourability testing inside the sweep.
status: sketched
rests-on: none
```

```gap
id: G-crit
lemma: a vertex-minimal unit-distance graph of chromatic number >= 5 is 5-critical, and every k-critical graph has minimum degree >= k-1; so any minimal counterexample to 4-colourability on at most N vertices has minimum degree >= 4.
status: open
next: theorem_prover: formalise vertex-criticality and prove the standard bound delta >= k-1 for k-critical graphs, then restrict to unit-distance realisations.
```

```gap
id: G-exhaust
lemma: for a specified N there is a complete certification that no 5-critical unit-distance graph on at most N vertices exists; equivalently, the first-order sentence over the reals "there are n <= N points whose pairwise squared distances lie in {0,1} and whose induced graph is not 4-colourable" is false. Weaker honest fallback: the same sentence restricted to the class C_N of point sets the construction engine reaches, which yields the census deliverable rather than the full size theorem.
status: open
next: symbolic_math/sat_solver: encode the sentence for n = N over the reals and attempt a quantifier-elimination/CAD refutation starting at the smallest N above the literature's current verification bound; tool_builder: exhaust the Minkowski-sum/spindle closure of the seed set up to N vertices with the 4-colouring SAT test, recording the swept class explicitly.
```
