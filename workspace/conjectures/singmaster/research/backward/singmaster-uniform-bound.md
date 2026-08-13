```skeleton
goal: N(a) is bounded by an absolute constant B, for every a > 1, under the both-mirrors-plus-trivial convention (N(3003)=8).
implies: Fix an admissible eps in (0,1) and let a_0(eps) be the effective MRSTT threshold. For a <= a_0, Lane-Clark gives N(a) <= 2*log2(a_0) + 2, an absolute constant (G-small-a-bounded). For a > a_0: write N(a) = 2*H(a) + 2 where H(a) = #{ (n,k) : C(n,k)=a, 2 <= k <= n/2 } counts nontrivial left-half representatives (half-triangle-convention-consistency). Split H(a) = H_int(a) + H_bnd(a) by whether k >= exp((log n)^{2/3+eps}) (interior) or k < exp((log n)^{2/3+eps}) (boundary). MRSTT gives H_int(a) <= 2 (G-interior-bounded), hence at most 4 interior occurrences counting mirrors. The boundary lemma gives H_bnd(a) <= C (G-boundary-uniform-count), hence at most 2C boundary occurrences counting mirrors. Therefore N(a) <= 4 + 2C + 2 = 2C + 6. Set B = max(2C + 6, 2*log2(a_0) + 2). Every term is an absolute constant, so B bounds N(a) for all a.
status: live
rests-on: mrstt-interior-theorem, mrstt-threshold-effective, lane-clark-normal-array-bound, half-triangle-convention-consistency
```

```gap
id: G-boundary-uniform-count
lemma: There is an absolute constant C such that for every a > 1 and every admissible eps in (0,1), the number of nontrivial left-half representatives (n,k) with C(n,k)=a and 2 <= k < exp((log n)^{2/3+eps}) is at most C. (Equivalently, counting both mirrors, at most 2C boundary occurrences.) The witness set forces C >= 3: 3003 has boundary representatives (78,2), (15,5), (14,6).
status: open
next: (structural target) reduce to de Weger's Conjecture A — a complete list of nontrivial collisions C(x,k1)=C(y,k2), k1<k2 — by showing every boundary representative outside the Fibonacci family has max(k1,k2) <= K for a computable K, so the boundary count becomes a finite per-pair sum; the K<=8 slice is already solved (deweger-smallk-effective covers (2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8)). (computation, today) tabulate, for the Fibonacci family j=1..6 and the witness set, each nontrivial occurrence's column k against the cut exp((log n)^{2/3+1/2}), producing the exact boundary-multiplicity table that pins the lower bound on C.
```

```gap
id: G-interior-bounded
lemma: For each admissible eps in (0,1) there is an effective threshold a_0(eps) such that for every a > a_0, at most 2 left-half representatives (n,k) of C(n,k)=a satisfy exp((log n)^{2/3+eps}) <= k <= n/2 (at most 4 in the full symmetric interior).
status: discharged
discharged-by: mrstt-interior-theorem (and mrstt-threshold-effective for the effectivity of a_0)
```

```gap
id: G-small-a-bounded
lemma: For a <= a_0(eps), N(a) <= 2*log2(a_0) + 2. The constant is structural — a_0 is a computable function of eps — but not numerically evaluated here, since the MRSTT threshold is astronomically large.
status: discharged
discharged-by: lane-clark-normal-array-bound (N(a) < 2*log2(a) + 2 for all a), mrstt-threshold-effective (a_0 effective)
```
