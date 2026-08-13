```skeleton
goal: N(a) is bounded by an absolute constant B, for every a > 1, under the both-mirrors-plus-trivial convention (N(3003)=8).
implies: **This is a conditional reduction.** It assumes MRSTT interior theorem (asserted from primary, not re-derived here) and MRSTT threshold effectiveness (asserted from Remark 1.7, not re-derived). Given those, the argument is: Fix an admissible eps in (0,1) and let a_0(eps) be the effective MRSTT threshold. For a <= a_0, Lane-Clark gives N(a) <= 2*log2(a_0) + 2, an absolute constant (G-small-a-bounded). For a > a_0: write N(a) = 2*H(a) + 2 where H(a) = #{ (n,k) : C(n,k)=a, 2 <= k <= n/2 } counts nontrivial left-half representatives (half-triangle-convention-consistency). Split H(a) = H_int(a) + H_bnd(a) by whether k >= exp((log n)^{2/3+eps}) (interior) or k < exp((log n)^{2/3+eps}) (boundary). MRSTT gives H_int(a) <= 2 (G-interior-bounded), hence at most 4 interior occurrences counting mirrors. The boundary lemma gives H_bnd(a) <= C (G-boundary-uniform-count), hence at most 2C boundary occurrences counting mirrors. Therefore N(a) <= 4 + 2C + 2 = 2C + 6. Set B = max(2C + 6, 2*log2(a_0) + 2). Every term is an absolute constant, so B bounds N(a) for all a. **Without the MRSTT conditions, this is a reduction of Singmaster to the boundary-uniform-count problem — a genuine partial result, not the full conjecture.**
status: live
rests-on: mrstt-interior-theorem (asserted), mrstt-threshold-effective (asserted), lane-clark-normal-array-bound (checked), half-triangle-convention-consistency
```

```gap
id: G-boundary-uniform-count
lemma: There is an absolute constant C such that for every a > 1 and every admissible eps in (0,1), the number of nontrivial left-half representatives (n,k) with C(n,k)=a and 2 <= k < exp((log n)^{2/3+eps}) is at most C. (Equivalently, counting both mirrors, at most 2C boundary occurrences.) The witness set forces C >= 3: 3003 has boundary representatives (78,2), (15,5), (14,6).
status: open
next: (computation, decisive) For the Fibonacci family a_j, j=1..12, count ALL nontrivial boundary representatives — not just the two named by the construction. The answer decides the gap: exactly 2 for every j → C >= 3 remains the live lower bound; the count grows with j → C is unbounded, G-boundary-uniform-count is FALSE, and singmaster-uniform-bound is broken. The computation is the one from directive 26. (structural target, if C stays bounded) reduce to de Weger's Conjecture A — a complete list of nontrivial collisions C(x,k1)=C(y,k2), k1<k2 — by showing every boundary representative outside the Fibonacci family has max(k1,k2) <= K for a computable K, so the boundary count becomes a finite per-pair sum; the K<=8 slice is already solved (deweger-smallk-effective covers (2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8)).
binding-case: The bound must hold for EVERY admissible eps in (0,1). Larger eps → larger cut → MORE boundary reps. So the binding case is eps → 1, not eps = 1/2. The run's general threshold result (directive 26): the Fibonacci family stays boundary for all eps > 1/3 — most of the admissible interval. So the family cannot be excluded from the boundary count by choosing a small eps; any C must cover it. The eps=1/2 used in the computation above is a conservative midpoint; if the per-a count grows at eps=1/2, the prognosis for larger eps is worse, and C is unbounded.
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
