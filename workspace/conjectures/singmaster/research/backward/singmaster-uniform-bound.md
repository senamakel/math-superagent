```skeleton
goal: N(a) is bounded by an absolute constant B, for every a > 1, under the both-mirrors-plus-trivial convention (N(3003)=8).
implies: **This is a conditional reduction.** It assumes MRSTT interior theorem (asserted from primary, not re-derived here) and MRSTT threshold effectiveness (asserted from Remark 1.7, not re-derived). Given those, the argument is: Fix an admissible eps in (0,1) and let a_0(eps) be the effective MRSTT threshold. For a <= a_0, Lane-Clark gives N(a) <= 2*log2(a_0) + 2, an absolute constant (G-small-a-bounded). For a > a_0: write N(a) = 2*H(a) + 2 where H(a) = #{ (n,k) : C(n,k)=a, 2 <= k <= n/2 } counts nontrivial left-half representatives (half-triangle-convention-consistency). Split H(a) = H_int(a) + H_bnd(a) by whether k >= exp((log n)^{2/3+eps}) (interior) or k < exp((log n)^{2/3+eps}) (boundary). MRSTT gives H_int(a) <= 2 (G-interior-bounded), hence at most 4 interior occurrences counting mirrors. The boundary lemma gives H_bnd(a) <= C (G-boundary-uniform-count), hence at most 2C boundary occurrences counting mirrors. Therefore N(a) <= 4 + 2C + 2 = 2C + 6. Set B = max(2C + 6, 2*log2(a_0) + 2). Every term is an absolute constant, so B bounds N(a) for all a. **Without the MRSTT conditions, this is a reduction of Singmaster to the boundary-uniform-count problem — a genuine partial result, not the full conjecture.**
status: live
rests-on: mrstt-interior-theorem (asserted), mrstt-threshold-effective (asserted), lane-clark-normal-array-bound (checked), half-triangle-convention-consistency, boundary-finite-collisions (live — the G-boundary-uniform-count decomposition)
```

```gap
id: G-boundary-uniform-count
lemma: There is an absolute constant C such that for every a > 1 and every admissible eps in (0,1), the number of nontrivial left-half representatives (n,k) with C(n,k)=a and 2 <= k < exp((log n)^{2/3+eps}) is at most C. (Equivalently, counting both mirrors, at most 2C boundary occurrences.) The witness set forces C >= 3: 3003 has boundary representatives (78,2), (15,5), (14,6).
status: open — REDUCED to G-nonfibonacci-pairs-are-bounded in the boundary-finite-collisions skeleton. This gap is NOT independently attackable; it was the target of the decomposition in boundary-finite-collisions.md, whose steps (1),(4),(5) are now settled and whose only remaining open piece is G-nonfibonacci-pairs-are-bounded.
binding-case: The bound must hold for EVERY admissible eps in (0,1). Larger eps -> larger cut -> MORE boundary reps. So the binding case is eps -> 1, not eps = 1/2. The Fibonacci family stays boundary for all eps > 1/3 — most of the admissible interval — so it cannot be excluded from the boundary count by choosing a small eps; any C must cover it.
status-of-the-crux-computation: RESOLVED, do not re-run. The decisive question — does the per-a Fibonacci boundary count grow with j, refuting the decomposition — is ANSWERED NO. Exact per-column scans (code/out/extend_exact_N_family_i4.captured.txt, i5.captured.txt, verify_fibonacci_identity.captured.txt): a_j has N=6 = 2 mirrors + trivial pair for j=2..5, i.e. exactly the two construction reps as nontrivial left-half reps, no k=2 collision, no other column. Both reps are boundary for every eps>1/3 (proved structurally; verified j=1..12). So each a_j contributes at most 2 boundary left-half reps (3 at j=1=3003); the infinite family does NOT make C unbounded. The remaining work is ONLY G-nonfibonacci-pairs-are-bounded.
next: (do not re-run the Fibonacci scan — done.) Attack G-nonfibonacci-pairs-are-bounded in boundary-finite-collisions.md: the column-growth inequality linking k1,k2 for a shared boundary value a, forcing |k2-k1| small and reducing candidate collisions to a finite effective search.
```

```gap
id: G-interior-bounded
lemma: For each admissible eps in (0,1) there is an effective threshold a_0(eps) such that for every a > a_0, at most 2 left-half representatives (n,k) of C(n,k)=a satisfy exp((log n)^{2/3+eps}) <= k <= n/2 (at most 4 in the full symmetric interior).
status: catalogued
catalogued-from: mrstt-interior-theorem (asserted — read from MRSTT primary, Thm 1.3, not re-derived here), mrstt-threshold-effective (asserted — read from MRSTT Remark 1.7, not re-derived here)
```

```gap
id: G-small-a-bounded
lemma: For a <= a_0(eps), N(a) <= 2*log2(a_0) + 2. The constant is structural — a_0 is a computable function of eps — but not numerically evaluated here, since the MRSTT threshold is astronomically large.
status: catalogued
catalogued-from: lane-clark-normal-array-bound (checked — verified by this run, capture at code/out/verify_lane_clark_bound.captured.txt), mrstt-threshold-effective (asserted — read from MRSTT Remark 1.7, not re-derived here)
```
