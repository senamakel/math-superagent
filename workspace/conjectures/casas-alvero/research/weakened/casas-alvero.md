# Weakened ladder — Casas–Alvero

```ladder
goal: Every monic polynomial f over a characteristic-0 field of degree n, if f shares a root with each of its first n−1 derivatives, then f is a pure power (x−α)^n.
difficulties: unbounded-degree, mod-p-stall, five-plus-roots, no-real-structure, scheme-infeasible, char0-usage-unlocated
status: open
```

```rung
id: R-ca-two-roots
statement: CA for f with at most 2 distinct roots over C — if f = (x−α)^m (x−β)^{n−m}, α ≠ β, shares a root with each derivative, then f is a pure power.
off: five-plus-roots, no-real-structure, scheme-infeasible, mod-p-stall
stance: settled
merge: Backed by Laterveer–Ounaïes / de Fernex–Ein–... (Prop 6): the shared-root set cannot have cardinality two. Turning four-plus-roots back on is what the four-roots rung does.
```

```rung
id: R-ca-four-roots
statement: CA for f with at most 4 distinct roots over C — a monic f of degree n with ≤4 distinct roots sharing a root with every derivative is a pure power.
off: five-plus-roots, no-real-structure, scheme-infeasible, mod-p-stall
stance: settled
merge: Rest on at-least-five-distinct-roots (Laterveer–Ounaïes Prop 5): a non-trivial CA polynomial has ≥5 distinct roots. The centroid (top Hasse derivative H_{n−1} = nx + a_1) collapses ≤4 roots onto the root set. Turning the fifth root back on is the five-roots rung.
```

```rung
id: R-ca-real-roots
statement: CA for f ∈ R[x] that splits completely over R (all roots real), all n — the real-root case.
off: no-real-structure, scheme-infeasible, mod-p-stall
stance: settled
merge: Polstra 2012 / Yakubovich 2014 settle the all-real-roots case. Turning no-real-structure back on (admitting non-real roots) is where every other rung lives.
```

```rung
id: R-ca-deg4
statement: CA for n = 4 — every monic quartic over Q sharing a root with f′, f″, f‴ is a pure power.
off: unbounded-degree, mod-p-stall, five-plus-roots, no-real-structure, scheme-infeasible
stance: settled
merge: n=4 is a prime power; bad primes {3,5,7} verified (badprimes-n4-minor-criterion-verified). Turning unbounded-degree back on is the known-families rung.
```

```rung
id: R-ca-known-families
statement: CA for every n of the form p^k, 2p^k, 3p^k (p≠2), 4p^k (p≠3,5,7), and 5p^k, 6p^k, 7p^k with their classified bad primes.
off: unbounded-degree, five-plus-roots, no-real-structure, scheme-infeasible
stance: settled
merge: The classified prime-power/primorial families; 5p-family bad-prime list (Chellali & Salinier; 5p-bad-primes-chellali). Turning unbounded-degree fully back on (all n, not just these families) is the whole conjecture.
```

```rung
id: R-ca-five-roots
statement: CA for f with at most 5 distinct roots over C — a monic f of degree n with ≤5 distinct roots sharing a root with each derivative is a pure power.
off: no-real-structure, scheme-infeasible, mod-p-stall
stance: open
merge: The frontier. A minimal counterexample needs ≥5 distinct roots (proved); ruling out exactly 5 is open. First move: write f = ∏_{j=1}^5 (x−α_j)^{m_j}, use the pinned centroid (H_{n−1} = nx + a_1 forces the weighted mean to be a root, from the centroid board post — promote it to a held claim first: the root-difference thread holds it only as an asserted post) plus the 4-in-nested-hull bound, and show no multiplicity pattern (m_1,…,m_5), Σm_j = n survives all n−1 derivative-sharing conditions. The char-0 step here is where any char-free argument would refute itself against the char-p witnesses already in the library.
```

```rung
id: R-ca-elim-boundary
statement: CA for each feasible n in {5, 6, 8, 9, 12} by complete elimination of S_n over Q, with the feasibility boundary named.
off: unbounded-degree, five-plus-roots, no-real-structure, mod-p-stall
stance: open
merge: Direct Gröbner/resultant verification over Q tops out ~n=8; n=12 needed scenario reduction + reduction-mod-p + char-p Gröbner (~3 weeks / 90 GB per scenario). name where the computation stops and why (computational-boundary thread).
```

```rung
id: R-ca-deg20
statement: CA for n = 20 — every monic degree-20 f over Q sharing a root with each derivative i = 1,…,19 is a pure power.
off: unbounded-degree, five-plus-roots, no-real-structure
stance: open
merge: 20 is the smallest open degree (Castryck–Laterveer–Ounaïes; Schaub–Spivakovsky). The minors-criterion bad-prime wall is at n=6 (scheme-infeasible); at n=20 the certified-bad list is a lower bound, the candidate-good primes are not proven good.
```
