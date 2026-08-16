# SUPPLY is equivalent to positive mod-4 switch density (the honest negative close)

Reduction of the goal to a single lemma. This is the **negative** branch: if it
discharges, the fold `Φ` adds nothing beyond switch density, SUPPLY is equivalent
to the named open problem (ABGS 2011 §9), and the problem closes honestly per
GOAL.md priority 3. Rival of `weak-input-fold.md`; at most one of the two can be
discharged.

```skeleton
goal: SUPPLY is equivalent to positive mod-4 switch density — that is, for every
  binary string h (the switch indicator), density of 1s equal to 0 implies
  wt(Φ_n h) = o(n). If true, the fold adds nothing beyond switch density and
  SUPPLY closes as equivalent to the L-function-inaccessible pair-frequency
  problem.
implies: One direction is the known reduction (problem.md, imported): positive
  mod-4 switch density — a positive fraction of consecutive prime pairs differing
  mod 4, i.e. positive density of 1s in h — implies ν₂(n) = wt(Φ_n h) ≥ c·n. The
  missing direction is exactly the contrapositive of gap G-eq-sparse-fold-is-sublinear:
  wt(Φ_n h) ≥ c·n for all large n forces positive density of 1s in h. Taking both
  directions together, SUPPLY ⟺ positive mod-4 switch density. The single gap is
  therefore a purely structural statement about the fold Φ on sparse inputs — no
  number theory — and the arithmetic content (that switch density itself is open,
  abgs-p1-wide-open) is imported, not re-derived.
status: broken
killed-by: the single gap is false. h = e_{2^m} (one switch at a power of two) has
  wt(h) = 1 = o(n), yet at n = 2^m+1 the windowed diagonal coordinates all equal 1
  (window [2^m−d, 2^m] contains the lone 1 at offset o=d, and d ⊆ d always), so
  wt(Φ_n h) = n − O(1). Sparse input therefore does NOT force sublinear fold
  weight: the equivalence SUPPLY ⇔ switch density is false for arbitrary binary
  strings, and even for boundary-realizable strings (r = 1…1,3…3 realizes this h).
  What survives is the restricted statement in supply-switch-equivalence.md,
  whose G-sup-implies-switch is stated for h arising from the primes, windowed —
  not for all h.
rests-on: lucas-submask-odd, abgs-p1-wide-open
```

```gap
id: G-eq-sparse-fold-is-sublinear
lemma: For every ε > 0 there is δ > 0 such that if wt(h) ≤ δ·n on the n-prefix
  for all large n (switch density 0), then wt(Φ_n h) ≤ ε·n for all sufficiently
  large n. The contrapositive is: a linear lower bound wt(Φ_n h) ≥ c·n forces
  positive switch density. This is a statement about the Pascal-mod-2 fold Φ
  alone, and its truth or falsity is decided by the fold's behaviour on sparse
  inputs.
status: refuted
refuted-by: h = e_{2^m} has wt(h)=1=o(n) but wt(Φ_n h)=n−O(1) at n=2^m+1, since the
  windowed coordinate T(n,d)=⊕_{o∈[0,d], o⊆d} h[n−1−d+o] equals h[2^m]=1 for every
  d∈[0,2^m] (the lone 1 sits at offset o=d and d⊆d). So the general
  sparse-⇒-sublinear transfer is false; the fold genuinely amplifies a single sparse
  switch to linear weight. The equivalence, if it holds at all, holds only for the
  specific prime string, which is supply-switch-equivalence.md's gap G-sup-implies-switch.
next: sat_solver + tool_builder: compute the curve max_{wt(h) ≤ k} wt(Φ_n h) for
  n = 8..64 via the submask-XOR characterisation (lucas-submask-odd: each image
  coordinate is the XOR of h over submasks, so the computation is a zeta-transform
  over the support). If this maximum is o(n) as k = δ·n with δ→0 uniformly, the
  lemma survives its first numerical attack and theorem_prover should next try the
  finite-fold statement symbolically (Lucas row structure: a support of size k
  has at most 2^k nonzero submasks, so wt(Φ_n h) ≤ min(n, 2^k) is the trivial
  ceiling — the lemma needs the sharper claim that sparse supports in fact fold to
  sublinear weight). If instead a sparse witness with wt(Φ_n h) ≥ ε·n surfaces at
  every reachable n, this gap is refuted and the witness discharges the rival gap
  G-weak-input-strictness in weak-input-fold.md. The two rivals share this one
  finite computation.
```
