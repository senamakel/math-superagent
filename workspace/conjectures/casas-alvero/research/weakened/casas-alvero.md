# Weakened ladder — Casas–Alvero

```ladder
goal: Every monic polynomial f over a characteristic-0 field K of degree n, if f shares a root with each of its first n−1 derivatives, then f is a pure power (x−α)^n.
difficulties: unbounded-degree, five-plus-roots, mod-p-stall, char0-usage-unlocated, no-real-structure, scheme-infeasible
status: open
```

The difficulties, named precisely because off-lists must match on them:

- **unbounded-degree** — n is any composite; no settled family (p^k, 2p^k, 3p^k, 4p^k, 5p^k, 6p^k, 7p^k) covers them all, and 20 is the smallest open degree (Castryck–Laterveer–Ounaïes; Schaub–Spivakovsky; `smallest-open-degree`).
- **five-plus-roots** — a non-trivial CA polynomial has ≥5 distinct roots (Laterveer–Ounaïes Prop 5). It is the structural obstacle the ≤2/≤4-root collapses stop at; the shared-root wording "≥5 distinct roots of f" is the version that matters.
- **mod-p-stall** — reduction mod p, the device that settles the prime-power/primorial families, stalls exactly where the char-p degeneration is too weak to force collapse (n=p^r+1 boundary); and it is a lower-bound-only screen at the open degrees.
- **char0-usage-unlocated** — the obligation to *name* where an argument uses characteristic 0, every proof of CA must break in char p (CA is false there). Largely located by this run (Gauss–Lucas / convex-hull collapse has no F_p analogue; the per-color Hasse vacuity is only part of it — deg6-char7 is fully non-degenerate), but each new argument must locate its own break.
- **no-real-structure** — roots need not be real; the Rolle/interlacing order structure that settles the all-real-roots case is absent, so analytic convex-hull/Gauss–Lucas arguments lose their forcing.
- **scheme-infeasible** — the elimination/Gröbner system over the coefficient+root scheme blows up: direct-over-Q Gröbner tops out ~n=8, the minor criterion at n=6 (C≈1365, D≈2751, ~2.2e5 core-hours), the minors at n=20 untouchable (C≈1e20).

The ladder is weakest first. Settled rungs are quoted with the difficulties that were off; without the off-list each would read as a proof of more than it proved.

```rung
id: R-ca-deg4
statement: CA for n = 4 — every monic quartic over Q sharing a root with f′, f″, f‴ is a pure power.
off: unbounded-degree, five-plus-roots, mod-p-stall, char0-usage-unlocated, no-real-structure, scheme-infeasible
stance: settled
merge: n=4 is a prime power; bad primes {3,5,7} verified computationally (badprimes-n4-minor-criterion-verified: lcm_T J_T = 1575 = 3²·5²·7; rank-mod-p agrees). CA_4,0 settled by the ≥5-distinct-roots bound (a degree-4 f has ≤4 roots). Turning unbounded-degree back on is the known-families rung.
```

```rung
id: R-ca-two-roots
statement: CA for f with at most 2 distinct roots over C — if f = (x−α)^m (x−β)^{n−m}, α ≠ β, shares a root with each derivative, then f is a pure power.
off: five-plus-roots, mod-p-stall, char0-usage-unlocated, no-real-structure, scheme-infeasible
stance: settled
merge: Settled by ddj-not-two (Laterveer–Ounaïes Prop 1): the shared-root set {α_i} cannot have cardinality two. Note the char-free reading is FALSE over F_2 (deg4-char3-refuted: x^4+x = x(x+1)^3); the settled statement is the char-0 one. Turning four-plus-roots back on is the four-roots rung.
```

```rung
id: R-ca-four-roots
statement: CA for f with at most 4 distinct roots over C — a monic f of degree n with ≤4 distinct roots sharing a root with every derivative is a pure power.
off: five-plus-roots, mod-p-stall, char0-usage-unlocated, no-real-structure, scheme-infeasible
stance: settled
merge: at-least-five-distinct-roots (Laterveer–Ounaïes Prop 5): a non-trivial CA polynomial has ≥5 distinct roots, so ≤4 distinct roots cannot satisfy the hypothesis non-trivially. Turning the fifth root back on is the five-roots rung.
```

```rung
id: R-ca-real-roots
statement: CA for f ∈ R[x] that splits completely over R (all roots real), all n — the real-root case.
off: no-real-structure, scheme-infeasible, mod-p-stall
stance: settled
merge: y2014-real-rooted-ca-holds (Yakubovich; Abel–Gontcharoff/Rolle) and Polstra settle the all-real-roots case: the shared-root sequence is forced stationary, contradicting Rolle. Turning no-real-structure back on (admitting non-real roots) is where every other open rung lives.
```

```rung
id: R-ca-known-families
statement: CA for every n of the form p^k, 2p^k, 3p^k (p≠2), 4p^k (p≠3,5,7), and 5p^k, 6p^k, 7p^k with their classified bad primes.
off: unbounded-degree, five-plus-roots, mod-p-stall, char0-usage-unlocated, no-real-structure, scheme-infeasible
stance: settled
merge: The classified prime-power/primorial families (Graf-von-Bothmer et al.; Draisma–de Jong; Castryck et al.; Chellali–Salinier 5p bad primes {2,3,7,11,131,193,599,3541,8009}). Turning unbounded-degree fully back on — all n, not just these families — is the whole conjecture.
```

```rung
id: R-ca-deg6-five-roots
statement: CA for n = 6 with exactly 5 distinct roots, over C — a monic sextic f = (x−a)^2 (x−b)(x−c)(x−d)(x−e) sharing a root with each of f′, f″, f‴, f⁗, f⁗⁗ is a pure power.
off: unbounded-degree, no-real-structure, mod-p-stall, char0-usage-unlocated, scheme-infeasible
stance: open
merge: The smallest degree where the ≥5-distinct-roots difficulty genuinely bites (a 6th-degree f can have exactly 5 distinct roots; multiplicity 2 on one root, 1 on the other four, so no free multiplicity pattern). Attackable today: write f = (x−a)^2∏(x−r_j), pin the centroid — top Hasse derivative H_5(f) = 6x + a_1 is linear with root the centroid, and the root-difference identity (verified char-free) forces that centroid to be a shared root. A degree-6, 5-root system is small (≤7 variables) and exact elimination over Q is feasible; the char-0 collapse should force the two singles at the centroid to merge with the double root. 5 = 6−1 makes every derivative-index meaningful. Rests on the centroid condition, which as of this run lives only as a board post (asserted), not a held claim — promote it first. Turning unbounded-degree part-way up is the five-roots rung.
```

```rung
id: R-ca-five-roots
statement: CA for f with at most 5 distinct roots over C — a monic f of degree n with ≤5 distinct roots sharing a root with each derivative is a pure power.
off: no-real-structure, scheme-infeasible, mod-p-stall
stance: open
merge: The frontier of the whole problem: a minimal counterexample has ≥5 distinct roots (proved), and ruling out exactly 5, at any degree, is open. Chávez-Martínez settles the degree-20 4/5/6-root slices only in 302 of 627 cases (partial, unchecked). First move: write f = ∏_{j=1}^5 (x−α_j)^{m_j}, ‖m‖_1 = n, use the pinned centroid (forced root) plus the ≥4-in-nested-hull bound, and show no multiplicity pattern (m_1,…,m_5) with Σm_j=n survives all n−1 derivative-sharing conditions. The char-0 step is the Gauss–Lucas / convex-hull collapse (no F_p analogue — deg6-char7 shows a fully non-degenerate char-p failure, so the obstruction is not just Hasse vacuity).
```

```rung
id: R-ca-elim-boundary
statement: CA for each feasible n in {5, 6, 8, 9, 12} by complete elimination of S_n over Q, with the feasibility boundary named.
off: unbounded-degree, five-plus-roots, no-real-structure, mod-p-stall
stance: open
merge: Direct Gröbner/resultant verification over Q tops out ~n=8; n=12 needed scenario reduction + reduction-mod-p + char-p Gröbner (~3 weeks / 90 GB per scenario, 5 scenarios, degree12-settled). Name where the computation stops and why (computational-boundary thread). This rung deliberately keeps mod-p-stall ON — it records the honest boundary of the elimination method rather than resolving it.
```

```rung
id: R-ca-deg20
statement: CA for n = 20 — every monic degree-20 f over Q sharing a root with each derivative i = 1,…,19 is a pure power.
off: unbounded-degree, five-plus-roots, no-real-structure
stance: open
merge: 20 is the smallest open degree (Castryck–Laterveer–Ounaïes; Schaub–Spivakovsky; berger-smallest-open-degree-20-corroboration). The minors-criterion bad-prime wall is at n=6 (scheme-infeasible); at n=20 the certified-bad list is a LOWER bound (18 primes from p|C(20,i)−1) and the candidate-good primes are NOT proven good — goodness there demands a method that beats the C≈1e20 minor wall.
```

Ordering note: the rungs are listed with R-ca-deg6-five-roots newly introduced as the weakest open rung that actually engages the five-plus-roots difficulty — the natural next attack. R-ca-elim-boundary is open but only records the computational wall (it keeps mod-p-stall on), so the run's live ladder to the conjecture runs through R-ca-deg6-five-roots → R-ca-five-roots → R-ca-deg20.
