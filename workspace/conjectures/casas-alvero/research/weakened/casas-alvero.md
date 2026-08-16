# Casas-Alvero: the ladder of weakened targets

Bottom first. `off` lists only difficulties declared in the header. Nothing here
is settled yet — `research/CLAIMS.md` is empty, so every rung is open for the
forward loop; the rungs that are literature-known (R5, R6) still need primary
sources before they can be banked.

```ladder
goal: Casas-Alvero (CA). K a field of characteristic 0, f ∈ K[x] monic of degree n ≥ 1; if gcd(f, f^(i)) ≠ 1 for every i = 1,…,n−1, then f = (x−a)^n for some a ∈ K̄.
difficulties: unbounded-degree, full-derivative-range, unrestricted-root-geometry, mod-p-stall, scheme-infeasible, components-unclassified
status: open
```

```rung
id: R-ca-deg4
statement: CA for n = 4: every monic quartic f over Q (hence over any char-0 field) that shares a root with each of f′, f″, f‴ is (x−a)^4. Settle by complete elimination over Q of the scheme S_4 = { f(r_i) = f^(i)(r_i) = 0 : i = 1,2,3 }, showing its only points have r_1 = r_2 = r_3.
off: unbounded-degree, unrestricted-root-geometry, mod-p-stall, scheme-infeasible, components-unclassified
stance: open
merge: turn unbounded-degree back on, one degree at a time (R2). First move: fix the weighted monomial order, then run the same elimination at n = 5, 6, 8, 9, 12, … and record, for each n, the machine, the order, the base ring, and the wall clock at termination or abandonment.
```

```rung
id: R-ca-elim-boundary
statement: CA for each feasible n in {5, 6, 8, 9, 12, 16, 18, …} by complete elimination of S_n over Q, with the feasibility boundary recorded as the result: the smallest n at which a weighted Gröbner basis of S_n fails to terminate within a stated wall clock, together with the intermediate degree reached when it was abandoned.
off: unbounded-degree, unrestricted-root-geometry, mod-p-stall, components-unclassified
stance: open
merge: scheme-infeasible turns on at the boundary; to get past it, replace computation by a uniform char-0 argument. First move: prove the structural lemma behind R3 — f^(n−1) is linear with root equal to the centroid (arithmetic mean of the roots counted with multiplicity), so the centroid is forced to be a root of f.
```

```rung
id: R-ca-two-roots
statement: CA for f with at most 2 distinct roots: if f = (x−α)^m (x−β)^(n−m) over C shares a root with every derivative i = 1,…,n−1, then α = β. Settled by a direct argument: f^(n−1) is linear with root (mα + (n−m)β)/n, which must lie in {α, β}, forcing α = β.
off: unrestricted-root-geometry, scheme-infeasible, components-unclassified
stance: open
merge: allow a third distinct root (R4). First move: run the same centroid argument with three roots — the centroid of the full multiset is forced to be a root of f — and enumerate (resultants or a SAT encoding over multiplicity triples (a,b,c)) which patterns can put the centroid on one of the roots while still sharing every derivative.
```

```rung
id: R-ca-k-roots
statement: CA for f with at most k distinct roots over C (k = 3, 4, …): every monic f with ≤ k distinct roots sharing a root with each derivative is a pure power. Equivalently: a hypothetical counterexample has at least k+1 distinct roots.
off: unrestricted-root-geometry, scheme-infeasible, components-unclassified
stance: open
merge: make the multiplicity bookkeeping uniform in k, or find the first k that admits a non-collapsed pattern. First move: for k = 3, 4, search exactly for a multiplicity pattern compatible with all n−1 gcd conditions; the first pattern that survives bounds the number of distinct roots of a minimal counterexample from below.
```

```rung
id: R-ca-real-roots
statement: CA for f with all roots real (all n): if f ∈ R[x] splits completely over R and shares a root with every derivative, then f is a pure power. This is the known real-rooted case; re-establish the theorem and its exact hypotheses from a primary source before banking it.
off: unrestricted-root-geometry, mod-p-stall, scheme-infeasible, components-unclassified
stance: open
merge: drop the real-root restriction and return to arbitrary complex roots. First move: take the ordering/Rolle argument that proves R5 and name the step that uses the total order of the real roots; run that step against the char-p counterexamples — the point where it breaks is exactly the char-0 content that must be preserved.
```

```rung
id: R-ca-known-families
statement: CA for every n of the form p^k, 2p^k, 3p^k, 4p^k (p prime): every monic f of such degree sharing a root with each derivative is a pure power. This is the literature's settled frontier; re-establish each family from primary sources with its exact hypotheses and reproduce the mod-p reduction.
off: mod-p-stall, scheme-infeasible
stance: open
merge: turn mod-p-stall on: n = 30 = 2·3·5 is the first degree not covered, where the mod-p degeneration no longer forces collapse. First move: write S_30 over Z and compute its fibres over F_2, F_3, F_5 to see which components survive reduction — that measures how much force the reduction still has at the first open degree.
```

```rung
id: R-ca-deg30
statement: CA for n = 30: every monic degree-30 f over Q sharing a root with each derivative i = 1,…,29 is a pure power. A settled proof is a new degree — a real result — and the first move past it is to make the argument run over a family.
off: unbounded-degree
stance: open
merge: turn unbounded-degree on: replace the single degree by a family. First move: identify what the n = 30 proof (or its obstruction) used about 30 = 2·3·5 and propagate it to n = 2·3·5·m or to all n with at least three distinct prime factors; that reaches the full conjecture and exhausts the ladder.
```
