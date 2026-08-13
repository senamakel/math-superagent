```skeleton
goal: There is an absolute constant C such that for every a > 1 and every admissible eps in (0,1), the number of nontrivial left-half representatives (n,k) with C(n,k)=a and 2 <= k < exp((log n)^{2/3+eps}) is at most C. This is the same as the G-boundary-uniform-count gap of the singmaster-uniform-bound skeleton; this skeleton decomposes it into attackable pieces.
implies: Fix eps in (0,1) and let B(eps) = { (n,k) : 2 <= k <= n/2, k < exp((log n)^{2/3+eps}) } be the boundary region. For a given a, let H_bnd(a) = #{ (n,k) in B(eps) : C(n,k)=a } be its boundary multiplicity (left-half, nontrivial). The argument:

(1) G-column-injectivity: For each fixed k, the equation C(n,k)=a has at most one solution n with n >= 2k, because C(n,k) is strictly increasing in n for n >= k (C(n+1,k)/C(n,k) = (n+1)/(n+1-k) > 1). So H_bnd(a) = #{ k : there exists n with (n,k) in B(eps) and C(n,k)=a }, i.e., the boundary count equals the number of distinct boundary columns k that hit a.

(2) Partition the boundary columns of a into collision pairs: if a has boundary columns k1 < k2 < ... < kr, each adjacent pair (ki, ki+1) comes from a solution of C(x,ki) = C(y,ki+1) = a for some x,y. (Actually the pairing is by collision, not adjacency — an a can have columns from multiple independent collision pairs; 3003 gives columns {2,5,6} from the (2,78) collision and the Fibonacci collision (5,6).)

(3) G-nonfibonacci-pair-list: There is a finite, computable set P of unordered pairs {k1,k2} with 2 <= k1 < k2 such that every boundary collision C(x,k1)=C(y,k2) with both (x,k1) and (y,k2) in the left half (k1 <= x/2, k2 <= y/2) and with {k1,k2} NOT of the Fibonacci-family form {k, k+1} belongs to P. Let K_max = max{k2 : {k1,k2} in P}. Then every non-Fibonacci boundary collision involves only columns <= K_max.

(4) G-known-collision-catalogue: The set P from (3) is already known for K_max <= 8 (de Weger Conjecture A for max(k1,k2) <= 8), and Stroeker-de Weger 1999 + BMSST 2008 exhaustively list all collisions for these pairs. Every collision for max(k1,k2) <= 8 produces a finite, explicit list of a-values; let A_small be the union of these.

(5) G-fibonacci-boundary-finite: The Fibonacci family C(n+1,k+1)=C(n,k+2) with n = F_{2j+2}F_{2j+3}-1, k = F_{2j}F_{2j+3}-1 (j >= 1) has the property that for any fixed eps > 0, only finitely many j satisfy the boundary condition k+1 < exp((log(n+1))^{2/3+eps}). Proof: k_j ~ φ^{4j}/5, n_j ~ φ^{4j}/5 with same exponential growth, so log k_j ∝ j while (log n_j)^{2/3+eps} ∝ j^{2/3+eps}. For j > J_0(eps), we have log k_j > (log n_j)^{2/3+eps}, placing the j-th member in the interior. The finite set j <= J_0(eps) produces a finite set A_fib of a-values.

(6) Synthesis: Every boundary collision for a either (i) has max(k1,k2) <= K_max and a in A_small, or (ii) is a Fibonacci collision with a in A_fib, or (iii) is a non-Fibonacci collision with max(k1,k2) > K_max — but this last case is ruled out by claim (3) since P exhausts all non-Fibonacci boundary pairs. Therefore the set of all a that can have any boundary collision is A_all = A_small ∪ A_fib, which is finite. By G-column-injectivity, each such a contributes at most |A_all| boundary columns, but actually each a has at most one representative per column and belongs to finitely many collision pairs, so its total boundary multiplicities across all a are finite. The maximum over a gives C.

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
lemma: For the Fibonacci/Singmaster infinite family C(n+1,k+1)=C(n,k+2) with n = F_{2j+2}F_{2j+3}-1, k = F_{2j}F_{2j+3}-1 (j >= 1), and for any fixed eps in (0,1), the boundary condition k+1 < exp((log(n+1))^{2/3+eps}) holds for only finitely many j. Explicitly, for eps = 1/2, determine the largest j with this property by direct computation.
status: open
next: (computation, today) Write a program that for j=1..100 computes n_j, k_j, evaluates the cut exp((log(n_j+1))^{2/3+1/2}), and reports which j satisfy k_j+1 < cut. Also compute the asymptotic crossing point: solve k_j ≈ exp((log n_j)^{2/3+eps}) asymptotically using the closed form k_j ~ φ^{4j+3}/5, log k_j ~ (4j+3)log φ - log 5, and log n_j ~ (4j+5)log φ - log 5, to find the theoretical J_0(eps). Capture.
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
lemma: The set A_all of all a > 1 that have at least one boundary collision (two distinct left-half representatives (n1,k1), (n2,k2) in B(eps) with C(n1,k1)=C(n2,k2)=a) is finite. Given G-fibonacci-boundary-finite (Fibonacci contributes finitely many a's) and G-nonfibonacci-pairs-are-bounded (all non-Fibonacci collisions involve columns <= K, and by G-known-small-collision-catalogue the solved range covers up to at least some K0, with the gap K0 < k <= K needing extension), the finiteness follows.
status: open
next: This gap is the synthesis: it is discharged once G-fibonacci-boundary-finite and G-nonfibonacci-pairs-are-bounded are both closed. The argument: every boundary collision involves a pair (k1,k2). Fibonacci pairs give finitely many a (G-fibonacci-boundary-finite). Non-Fibonacci pairs have max(k1,k2) <= K (G-nonfibonacci-pairs-are-bounded), so there are only finitely many such pairs (at most K choose 2). For each pair, BST 1999 gives finitely many a (ineffective, but for pairs <= K_solved the list is explicit). The union over finitely many finite sets is finite. Therefore A_all is finite.
```