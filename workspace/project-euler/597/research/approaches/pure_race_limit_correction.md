# Approach: pure-race limit with explicit finite-L correction

```approach
idea: >
  Prove that p(n,L) = p(n,∞) + O(e^{-cL/n}) for some c>0, compute p(13,∞)
  exactly from the pure-race bump-forest theory, and bound the L=1800 remainder
  below 5×10^{-11}
mechanism: >
  The pure race (L=∞) removes the finish event: every boat rows until bumped or
  is the lead boat. The MC evidence shows p(n,1800) ≈ p(n,∞) for n=2..30,
  with differences ≤ 0.003 and decreasing with n. In the finite race, a boat
  finishes if its finish time is less than the time it would be bumped.
  The correction comes from boats that would have bumped in the pure race but
  finish first in the finite race. The probability of such a "pre-empted bump"
  decays exponentially in L/(n*v_typical).
  The pure-race parity p(n,∞) is a functional of the speed-ordering + magnitude
  alone — no finish line — and is exactly computable via the convex-minorant
  cluster decomposition (pure-race bump clusters = GCM segments, distribution
  known: Stirling numbers of the first kind). Within each cluster, the forest
  structure depends only on the relative speed ordering. The parity for the
  pure race may admit an exact formula in terms of record statistics.
status: refuted
killed-by: >
  The premise that p(n,∞) is "exactly computable via the convex-minorant cluster
  decomposition" is FALSE and is refuted by the run's own computation. The chain
  parity (# chain-pairs mod 2) is NOT a cluster-block functional of the speed
  vector: the convex-minorant cycle-parity model p(n,∞) = P(Σ_clusters C(size,2)
  even) gives 1/6 vs 0.389 at n=3 and 0.61627 (33545/54432) at n=13 against the
  true ~0.500 target (`code/cycle_parity.py`, `check_cycle_vs_pure.py`). The
  related pure-bump ordering-count model is also refuted (gives 1/3, 13/24,
  67/120 for n=3,4,5 vs true limits 7/18, 19/36). So there is NO known exact
  formula for p(13,∞) that this approach could evaluate — the object that "would
  then be the answer" does not have a closed form in any theory the run has
  found. Separately, the claimed uniform correction bound O(e^{-cL/n}) < 5e-11
  is unsupported: the measured corrections are far larger — p(3,1800)-p(3,∞)
  ≈ 0.0008, p(4,1800)-p(4,∞) ≈ -0.003 — so at n=4 the finite-L value differs
  from the infinite-L value at the ~3rd-4th decimal, and no source derives the
  exponential rate or a constant small enough for 5e-11 at L=1800. The approach
  needs BOTH an exact p(13,∞) (which no model provides) and a bound that is
  false at the measured magnitudes.
note: >
  The pure-race object IS classical and well-sourced: no-finish 1D ballistic
  aggregation == segments of the greatest convex minorant, cluster-size
  distribution == cycle-length composition of a uniform random permutation
  (Stirling first-kind), leaders = right-to-left record minima (Majumdar–Mallick–
  Sabhapandit; Goldie). That is a warm-up, exactly as CONTEXT.md records. What is
  NOT solved — and is the run's actual object — is the PARITY of the pure-race
  chain, and the run proved that parity is not a GCM-cluster functional. So the
  "exact p(13,∞)" half of this approach is dead on substance, not absence.
precedent: >
  - run refutations: code/cycle_parity.py, code/check_cycle_vs_pure.py,
    code/pure_bump_limit.py, code/purelimit_probe.py
  - pure-race = GCM / cycles of uniform random permutation:
    Majumdar, Mallick & Sabhapandit, Phys. Rev. E 79, 021109 (2009),
    arXiv:0811.0908, doi:10.1103/PhysRevE.79.021109
  - Goldie, "Records, permutations and greatest convex minorants", Math. Proc.
    Camb. Phil. Soc. (2022), doi:10.1017/S0305004122000031 (GCM/permutation bridge)
  - claim `cm-composition-distribution` (GCM face-lengths = cycle lengths,
    Stirling first-kind) — STEADFAST but does NOT give parity
  - claim `torpids-parity-not-gcm-functional` (equal GCM composition, different
    torpids parity — the structural reason chain-parity is not a cluster-block
    functional)
```
