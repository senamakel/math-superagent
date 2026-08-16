# Casas-Alvero: the ladder of weakened targets

Bottom first. `off` lists only difficulties declared in the header. A rung is
`settled` if the library already establishes it (status `asserted-by-source`,
`proved`, or `checked`); a `settled` rung is banked, and is not the goal. The
frontier — the weakest rung nobody has settled — is `R-ca-five-roots`.

The previous version of this ladder was stale in two ways: it claimed
`research/CLAIMS.md` was empty (it is not), and it marked as `open` rungs the
library already settles (n=4, and the ≤2/≤4-distinct-roots cases) while
targeting degree 30 as "smallest open" when the library's `smallest-open-degree`
is 20. This rewrite banks those settled rungs and moves the frontier to the
statement the library does *not* settle: 5 distinct roots.

```ladder
goal: Casas-Alvero (CA). K a field of characteristic 0, f ∈ K[x] monic of degree n ≥ 1; if gcd(f, f^(i)) ≠ 1 for every i = 1,…,n−1, then f = (x−a)^n for some a ∈ K̄.
difficulties: unbounded-degree, mod-p-stall, five-plus-roots, no-real-structure, scheme-infeasible, char0-usage-unlocated
status: open
```

```rung
id: R-ca-two-roots
statement: CA for f with at most 2 distinct roots over C: if f = (x−α)^m (x−β)^(n−m), α ≠ β, shares a root with each derivative i = 1,…,n−1, then α = β. Direct argument: f^(n−1) is linear with the single root (mα + (n−m)β)/n, which must lie in {α, β}, forcing α = β.
off: unbounded-degree, mod-p-stall, five-plus-roots, no-real-structure, scheme-infeasible, char0-usage-unlocated
stance: settled
settled-by: shared-root-set-not-2 (Laterveer–Ounaïes Prop 1; the 2-root centroid collapse is the direct proof given there)
merge: allow a third and fourth distinct root (R-ca-four-roots). The centroid argument survives, but with 3–4 roots the centroid-on-a-root condition alone no longer collapses them; that is exactly the step Laterveer–Ounaïes Prop 5 covers.
```

```rung
id: R-ca-four-roots
statement: CA for f with at most 4 distinct roots over C: a monic f of degree n with ≤4 distinct roots sharing a root with each derivative is a pure power. This is Laterveer–Ounaïes 2012 Prop 5 (restated as min-counter-structure: a non-trivial CA polynomial has ≥5 distinct roots, so CA holds for ≤4).
off: unbounded-degree, mod-p-stall, five-plus-roots, no-real-structure, scheme-infeasible, char0-usage-unlocated
stance: settled
settled-by: at-least-five-distinct-roots / min-counter-structure (Laterveer–Ounaïes 2012 Prop 5: a non-trivial CA polynomial has ≥5 distinct roots, so CA holds for ≤4 distinct roots)
merge: turn five-plus-roots back on (R-ca-five-roots). First move: extend the Laterveer–Ounaïes bookkeeping from 4 to 5 distinct roots — with 5 roots the multiplicity pattern (m_1,…,m_5), Σ m_j = n, must satisfy all n−1 derivative-sharing conditions, and the centroid is still forced to be a root but no longer collapses the set.
```

```rung
id: R-ca-real-roots
statement: CA for f ∈ R[x] that splits completely over R (all roots real), all n: if f shares a root with every derivative, then f is a pure power. Proved over C by Polstra 2012 (Vieta/multiplicity + Gauss–Lucas), with the equivalent convex-hull formulation: a CA counterexample over C must have a root that is not a vertex of its convex hull.
off: unbounded-degree, mod-p-stall, five-plus-roots, no-real-structure, scheme-infeasible, char0-usage-unlocated
stance: settled
settled-by: real-rooted-and-convex-hull (Polstra 2012, RHUMJ 13(1) Thm 3.1/Thm 4.3, via Vieta + Gauss–Lucas)
merge: drop the real/total-order structure (turn no-real-structure back on) and return to arbitrary complex roots. First move: name the step in the Polstra argument that uses the ordering of the real roots (Rolle / Gauss–Lucas on a totally-ordered set) — that step has no complex analogue and is the char-0-only content this rung enjoys for free.
```

```rung
id: R-ca-deg4
statement: CA for n = 4: every monic quartic f over Q (hence over any char-0 field) sharing a root with each of f′, f″, f‴ is (x−a)^4. Settled because n=4 is elementary and 4 = 2² is of the form p^k; the char-p bad primes {3,5,7} of degree 4 are separately verified (badprimes-n4-minor-criterion-verified, deg4-char3/5/7-refuted).
off: unbounded-degree, mod-p-stall, five-plus-roots, scheme-infeasible, char0-usage-unlocated
stance: settled
settled-by: settled-classes (n=4 elementary; 4 = 2² = p^k via Graf-von-Bothmer 2007) with the degree-4 char-p bad primes {3,5,7} verified separately (badprimes-n4-minor-criterion-verified, deg4-char3/5/7-refuted)
merge: turn unbounded-degree back on one degree at a time (R-ca-elim-boundary). First move: run complete elimination of S_n over Q at n = 5, 6, 8, 9, 12, recording for each the weighted monomial order, base ring, machine, and wall clock at termination or abandonment.
```

```rung
id: R-ca-known-families
statement: CA for every n of the form p^k, 2p^k, 3p^k (p≠2), 4p^k (p≠3,5,7), and 5p^k, 6p^k, 7p^k with their classified bad primes (settled-classes). This is the literature's settled frontier, proved by reduction mod a good prime plus the GVB lift; degree 12 was additionally settled outright (Castryck et al 2012).
off: unbounded-degree, five-plus-roots, no-real-structure, scheme-infeasible, char0-usage-unlocated
stance: settled
settled-by: settled-classes (Graf-von-Bothmer 2007 for p^k, 2p^k; Draisma–de Jong for 3p^k (p≠2), 4p^k (p≠3,5,7); Castryck et al 2012 for 5p^k, 6p^k, 7p^k and degree 12)
merge: turn mod-p-stall back on: n = 20 = 4·5 is the first degree not covered (4p^k excludes p=5), where the mod-p degeneration no longer forces collapse. First move: write S_20 over Z and inspect its fibres over F_2, F_3, F_5 to measure how much reduction-force survives at the first open degree — that is the entry point of R-ca-deg20.
```

```rung
id: R-ca-five-roots
statement: CA for f with at most 5 distinct roots over C: if a monic f of degree n with ≤5 distinct roots shares a root with each derivative i = 1,…,n−1, then f is a pure power. Equivalently, no CA counterexample has exactly 5 distinct roots. This extends Laterveer–Ounaïes's ≤4 bound by one root and is the weakest statement not already in the library.
off: unbounded-degree, mod-p-stall, no-real-structure, scheme-infeasible, char0-usage-unlocated
stance: open
merge: turn no-real-structure (and ultimately unbounded root count) back on to reach unrestricted roots. First move: write f = ∏_{j=1}^5 (x−α_j)^{m_j}, Σ m_j = n, and eliminate the n−1 derivative-sharing conditions over the roots; the top Hasse derivative H_{n−1} = nx + a_1 forces the centroid (m_1α_1+…+m_5α_5)/n to be a root of f, and one shows no multiplicity pattern survives — or exhibits the first candidate pattern, which would bound a minimal counterexample from below at 6.
```

```rung
id: R-ca-elim-boundary
statement: CA for each feasible n in {5, 6, 8, 9, 12} by complete elimination of S_n over Q, with the feasibility boundary recorded as the result: the smallest n at which a weighted Gröbner basis of S_n fails to terminate within a stated wall clock, together with the intermediate degree reached when abandoned. The literature's reported boundary (≈8 over Q; 12 only via char-p scenario reduction) is reproduced and made this run's own.
off: unbounded-degree, mod-p-stall, five-plus-roots, no-real-structure, char0-usage-unlocated
stance: open
merge: scheme-infeasible turns on at the boundary; past it, replace computation by a uniform char-0 argument. First move: prove the centroid lemma (f^(n−1) is linear with root the arithmetic mean of the roots counted with multiplicity, so the centroid is forced to be a root of f) — the structural fact a uniform argument would rest on and the one R-ca-five-roots uses first.
```

```rung
id: R-ca-deg20
statement: CA for n = 20: every monic degree-20 f over Q sharing a root with each derivative i = 1,…,29 is a pure power. This is the smallest open degree (smallest-open-degree), a genuinely new degree if settled — a real result. It is the first composite degree where mod-p reduction stalls (20 = 4·5, and 4p^k excludes p=5).
off: unbounded-degree
stance: open
merge: turn unbounded-degree back on: replace the single degree by a family. First move: identify what the n=20 obstruction used about 20 = 4·5 and propagate it to n = 4·5·m or to all n with the same prime-factor structure; a uniform argument over the family reaches the full conjecture and exhausts the ladder.
```
