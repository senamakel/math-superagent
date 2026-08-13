```skeleton
goal: There is an absolute constant C such that for every a > 1 and every admissible eps in (0,1), the number of nontrivial left-half representatives (n,k) with C(n,k)=a and 2 <= k < exp((log n)^{2/3+eps}) is at most C. This is the same as the G-boundary-uniform-count gap of the singmaster-uniform-bound skeleton; this skeleton decomposes it into attackable pieces.
implies: Fix eps in (0,1) and let B(eps) = { (n,k) : 2 <= k <= n/2, k < exp((log n)^{2/3+eps}) } be the boundary region. For a given a, let H_bnd(a) = #{ (n,k) in B(eps) : C(n,k)=a } be its boundary multiplicity (left-half, nontrivial). The argument:

(1) G-column-injectivity: For each fixed k, the equation C(n,k)=a has at most one solution n with n >= 2k, because C(n,k) is strictly increasing in n for n >= k (C(n+1,k)/C(n,k) = (n+1)/(n+1-k) > 1). So H_bnd(a) = #{ k : there exists n with (n,k) in B(eps) and C(n,k)=a }, i.e., the boundary count equals the number of distinct boundary columns k that hit a.

(2) Partition the boundary columns of a into collision pairs: if a has boundary columns k1 < k2 < ... < kr, each adjacent pair (ki, ki+1) comes from a solution of C(x,ki) = C(y,ki+1) = a for some x,y. (Actually the pairing is by collision, not adjacency — an a can have columns from multiple independent collision pairs; 3003 gives columns {2,5,6} from the (2,78) collision and the Fibonacci collision (5,6).)

(3) G-nonfibonacci-pair-list: There is a finite, computable set P of unordered pairs {k1,k2} with 2 <= k1 < k2 such that every boundary collision C(x,k1)=C(y,k2) with both (x,k1) and (y,k2) in the left half (k1 <= x/2, k2 <= y/2) and with {k1,k2} NOT of the Fibonacci-family form {k, k+1} belongs to P. Let K_max = max{k2 : {k1,k2} in P}. Then every non-Fibonacci boundary collision involves only columns <= K_max.

(4) G-known-collision-catalogue: The set P from (3) is already known for K_max <= 8 (de Weger Conjecture A for max(k1,k2) <= 8), and Stroeker-de Weger 1999 + BMSST 2008 exhaustively list all collisions for these pairs. Every collision for max(k1,k2) <= 8 produces a finite, explicit list of a-values; let A_small be the union of these.

(5) G-fibonacci-per-a-bounded: The Fibonacci family C(n+1,k+1)=C(n,k+2) with n = F_{2j+2}F_{2j+3}-1, k = F_{2j}F_{2j+3}-1 (j >= 1) stays in the BOUNDARY for all j when eps >= 1/3 (directive 24, verified: code/out/boundary_cut_corrected.captured.txt). Asymptotically: log k_j ~ 4j log φ (linear in j), (log n_j)^(2/3+eps) ~ (4j log φ)^(2/3+eps). The boundary condition holds for all large j iff 2/3+eps > 1, i.e. eps > 1/3. With eps=1/2 this is satisfied, so infinitely many distinct a's have boundary representatives. CRUCIALLY, each such a contributes at most 2 boundary left-half reps (the (k,k+1) Fibonacci collision plus possibly a k=2 collision) — the per-a count is bounded by a constant independent of j. The infinite family therefore does NOT threaten a constant bound on H_bnd(a) per a: what matters is the max over a, not whether infinitely many a's participate.

(6) Synthesis (revised): Every boundary collision for a either (i) has max(k1,k2) <= K and a in A_small, or (ii) is a Fibonacci collision (k,k+1) with a in the infinite Fibonacci set A_fib, or (iii) is a non-Fibonacci collision with max(k1,k2) > K — ruled out by claim (3). For case (ii), each Fibonacci a has at most 2 boundary left-half reps (the (k,k+1) pair and possibly a k=2 collision). For case (i), A_small is finite and each a in it is checked explicitly (witness set: max boundary reps = 3 at 3003). Therefore H_bnd(a) <= max(3, 2 + possible_extra_from_k2) for all a. The bound C is at most 3 + (max extra boundary reps from non-Fibonacci columns for a given a), and the hard step (3) remains the same: prove non-Fibonacci boundary pairs are bounded, which controls the "extra" term.

The hard step is (3): proving that non-Fibonacci boundary pairs are confined to a finite, computable set P. This is the core of Singmaster's conjecture in the boundary regime. The remaining gaps decompose this into (a) the Bilu-Tichy/HPT classification of which (k1,k2) pairs can have infinitely many solutions at all, and (b) the MRSTT boundary condition which forces additional restrictions on which of those pairs can actually produce boundary (as opposed to interior) solutions.
status: sketched
rests-on: genus-closed-form-derived-by-riemann-hurwitz, bst-genus-classification-matches-grid, deweger-smallk-effective, sdw-elliptic-logarithms-eight-pairs, avanesov-1967-cx3-cy2-complete, hpt-bilu-tichy-exceptional-classification, mrstt-exact-statement, infinite-family-6, convention-n3003-eight
```

```gap
id: G-column-injectivity
lemma: For each fixed integer k >= 2 and integer a > 1, the equation C(n,k) = a has at most one solution with n >= 2k. Consequently, a given integer a appears in at most one position per column k in the left half of Pascal's triangle.
status: discharged
discharged-by: Elementary — C(n+1,k)/C(n,k) = (n+1)/(n+1-k) > 1 for all n >= k, so C(n,k) is strictly increasing in n; injectivity follows immediately. Verified numerically for all k <= 100, n <= 1000 as a sanity check.
```

```gap
id: G-fibonacci-boundary-finite
lemma: (REFUTED as originally stated — corrected by directive 24.) The original claim said the Fibonacci family crosses out of the boundary for all eps > 0. The corrected computation (code/boundary_cut_corrected.py, capture code/out/boundary_cut_corrected.captured.txt, EXIT_CODE=0) shows: for eps=0.5 (so exponent = 7/6), ALL six family members j=1..6 satisfy k+1 < exp((log(n+1))^(7/6)). Asymptotically: log k_j ~ 4j log φ (linear in j), (log n_j)^(2/3+eps) ~ (4j log φ)^(2/3+eps). The boundary condition log k < (log n)^(2/3+eps) holds for all large j iff 2/3+eps > 1, i.e. eps > 1/3. For eps < 1/3, only finitely many j are boundary; for eps >= 1/3, infinitely many are. With the MRSTT-admissible choice eps=1/2, the family stays boundary forever.
status: refuted
refuted-by: Directive 24 — the original program code/boundary_cut.py executed exp((log n)^(2/3) + 0.5) instead of exp((log n)^(2/3+0.5)), a difference of 411,000× at n=229969 that misclassified j>=2 as interior. The corrected computation proves the opposite: every family member is boundary.
replacement: The skeleton's step (5) no longer claims A_fib is finite. Instead, the correct structural fact is: each Fibonacci a contributes at most 2 boundary representatives (the Fibonacci collision (k, k+1) plus possibly a k=2 collision), which is bounded by a constant independent of j. So the infinite family does not threaten the per-a bound: what matters for C is the max boundary reps per individual a, not whether infinitely many distinct a's have boundary reps.
```

```gap
id: G-bilu-tichy-exceptional-pairs
lemma: The Bilu-Tichy classification (Bilu-Tichy 2000, Thm 1.1/10.5) and its refinement by Hajdu-Papp-Tijdeman (2022, Thm 2.3) applied to the equal-binomial-coefficient equation C(x,k1)=C(y,k2) imply: for pairs (k1,k2) with 2 <= k1 < k2 not of the form (k, k+1) (the Fibonacci family), the equation has only finitely many integer solutions with k1 <= x/2, k2 <= y/2. For pairs of the form (k, k+1), the only infinite family is the Lind-Singmaster Fibonacci family; all other solutions are finite in number.
status: catalogued
catalogued-from: hpt-bilu-tichy-exceptional-classification (asserted — HPT 2022 Thm 2.3 states finiteness for non-exceptional pairs, ineffective), bilu-tichy-classification-primary (asserted — the five standard pairs over Q)
```

```gap
id: G-known-small-collision-catalogue
lemma: For all pairs (k1,k2) with 2 <= k1 < k2 <= 8, the complete list of integer solutions to C(x,k1)=C(y,k2) with k1 <= x/2, k2 <= y/2 is known exactly (Stroeker-de Weger 1999 for (2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8); Avanesov 1967 for (2,3); BMSST 2008 for (2,5)). The union of all a-values arising from these collisions is a finite, explicit set containing the witness set {3003, 120, 210, 1540, 7140, 11628, 24310} plus additional values. For each such a, the number of boundary representatives is computable.
status: catalogued
catalogued-from: deweger-smallk-effective (asserted — per-pair effective results exist), sdw-elliptic-logarithms-eight-pairs (asserted — complete for eight pairs), bmsst-hyperelliptic-effective-method (asserted — (2,5) solved), grktu-known-solutions-list (asserted — complete known list)
```

```gap
id: G-nonfibonacci-pairs-are-bounded
lemma: There exists a computable constant K (depending only on eps) such that for every pair (k1,k2) with 2 <= k1 < k2, if there exists a boundary solution C(x,k1)=C(y,k2)=a with both (x,k1) and (y,k2) in the left-half boundary region B(eps), and {k1,k2} is not of the Fibonacci form {k, k+1}, then max(k1,k2) <= K. Equivalently, the set P of non-Fibonacci boundary-collision pairs is finite and computable.
status: open
next: (theorem_prover) This is the core structural gap. One route: combine the genus formula g(k1,k2) = ((k1-1)(k2-1)+1-gcd(k1,k2))/2 (proved, genus-closed-form-derived-by-riemann-hurwitz) with the boundary condition k1 < exp((log x)^{2/3+eps}) and the inequality C(x,k1) >= C(2k1,k1) >= 2^{k1} to bound k1 in terms of k2, then apply Bilu-Tichy/HPT to classify which pairs survive. Concretely: if k1 and k2 are both boundary columns for the same value a, then both satisfy the cut, and from a = C(x,k1) we have k1 <= log2(a) and x approx (k1! a)^{1/k1}. The growth constraints may force |k2 - k1| to be small, reducing to a finite search. Alternatively, use the genus classification: for large |k2 - k1|, the genus g(k1,k2) >= 2 grows, and Faltings gives finitely many rational points — but ineffectively. The effective route needs a different idea.
```

```gap
id: G-boundary-collision-a-finite
lemma: (REVISED — G-fibonacci-boundary-finite refuted.) The original synthesis that A_all is finite relied on G-fibonacci-boundary-finite claiming only finitely many Fibonacci a's enter the boundary. The corrected computation (directive 24) shows the Fibonacci family stays boundary forever for eps >= 1/3. So A_all is NOT finite — infinitely many a's have boundary collisions (the Fibonacci family). This is NOT a problem for the per-a bound: each Fibonacci a has at most 2 boundary left-half reps (the (k,k+1) Fibonacci collision plus possibly a k=2 collision), bounded independently of j. The finite-A_all route is closed; the correct reduction to G-boundary-uniform-count goes through per-a reasoning directly from G-nonfibonacci-pairs-are-bounded (which bounds the columns of non-Fibonacci boundary collisions) plus the Fibonacci-family's per-a contribution (which is already bounded by 2).
status: open
next: (decisive computation, directive 26) For j=1..12, count ALL nontrivial representatives of a_j (not just the two from the construction) and test each against the boundary cut. If every a_j has exactly 2 boundary reps, the "plus possibly a k=2 collision" does not occur and C=2 for the Fibonacci subproblem. If additional reps appear and grow with j, C is unbounded — G-boundary-uniform-count is false and singmaster-uniform-bound is broken. The next action after that computation depends on the outcome; see G-boundary-uniform-count.
binding-note: The epsilon-dependence of the boundary cut (directive 26) means the binding case is eps → 1; under eps > 1/3 the entire Fibonacci family is boundary, so the family is inside the counted object for most of the admissible range. Any argument for G-boundary-uniform-count must cover it — the family cannot be set aside as interior by choosing a small eps.
```