# SUPPLY on a density-1 set, from a mean and a variance bound on the fold

GOAL.md priority 1 / problem.md result 3: the averaged form. This is a
*different theorem* from the two existing skeletons —
`supply-from-endpoint-parity.md` attacks the pointwise statement via a
character-sum bias (result 4), `supply-switch-equivalence.md` decides
equivalence to switch density (result 5). This one proves
`ν₂(n) ≥ c·n` only on a density-1 set, by Chebyshev over `n`: a linear lower
bound on the *mean* of `ν₂(n)/n` plus a *vanishing variance* forces the lower
tail to be empty asymptotically. Both arithmetic inputs are statements about
`h` read along binary-submask windows — exactly the "second-moment / variance
bound on `h`" candidate GOAL.md priority 2 names — and neither is the
pointwise character sum the other skeleton needs.

```skeleton
goal: Averaged SUPPLY: there is c > 0 and a density-1 set S with ν₂(n) ≥ c·n for every n ∈ S.
implies: G-mean-linear (mean of ν₂(n)/n ≥ c₀) + G-var-vanishing (variance → 0) + Chebyshev over n empties the lower tail: |{n ≤ N : ν₂(n) < (c₀/2)n}|/N ≤ 4σ²_N/c₀² → 0, so the density-1 set S = {n : ν₂(n) ≥ (c₀/2)n} works.
rests-on: G-dict-windowed-zeta (ν₂ = wt(Φ_n h) = #{d ∈ [2,n−1] : T(n,d)=1} ± 1), discharged in supply-from-endpoint-parity.md on problem.md facts 1–2; not yet carried by a CLAIMS.md id and to be re-grounded by the oracle.
status: sketched
```

```gap
id: G-mean-linear
lemma: >
  There is an absolute c₀ > 0 with (1/N)·Σ_{n≤N} ν₂(n)/n ≥ c₀ for all large
  N. Equivalently, over the triangular array {(n,d) : 2 ≤ d ≤ n−1, n ≤ N}, a
  positive fraction of the submask-XOR cells T(n,d) = s_d(n−1−d) equal 1.
  This is the averaged analogue of SUPPLY's conclusion and is strictly weaker
  than it: it allows ν₂(n) to be small for arbitrarily many individual n, as
  long as it is not small in the mean.
status: open
next: >
  DONE (tool_builder, code/averaged/mean_capture.py, code/out/averaged_mean_capture.txt):
  the gap has been grounded. M(N)=(1/N)Σν₂(n)/n for the prime h (d in
  [2,n-1], convention pinned by reproducing nu2(4000)/4000=0.4938 vs
  literature 0.4933) is M(100)=0.439, M(500)=0.483, M(1000)=0.491, M(2000)=0.495,
  M(4000)=0.497, M(8000)=0.499 — stable, no downward tail. Negative controls
  both FAIL as required: all-ones h → M=0 at every N (kernel), Thue-Morse h →
  M decaying 0.226→0.049 (sublinear). Signal is specific to the prime h.
  Discrepancy vs literature: the [0.42,0.52] bracket is optimistic at tiny n —
  n=53 gives 0.34, min in [200,500)=0.416 at n=274 — but the mean and tail
  past n=500 are firmly ≥0.44. Remaining before G-mean-linear is a *rung*:
  the empirical mean being ~0.49 is not a proof of a positive lower bound;
  the theorem needs an arithmetic input (bounded autocorrelation / second
  moment) as in G-var. G-mean-linear as a hypothesis survives its cheapest
  falsifier; it is not yet proved.
```

```gap
id: G-var-vanishing
lemma: >
  (1/N)·Σ_{n≤N} (ν₂(n)/n − μ_N)² → 0 as N → ∞, where μ_N is the empirical
  mean of ν₂(n)/n over n ≤ N. In words: the normalised fold weight ν₂(n)/n
  concentrates around its mean. Via the dictionary this is a second-moment /
  bounded-autocorrelation statement about the prime string h: expanding σ²_N
  in the s_d coordinates, it is controlled by
  Σ_{d,d'} Σ_{j,j'} E[(−1)^{s_d(j) ⊕ s_{d'}(j')}] over the windows, i.e. the
  autocorrelation of h along binary-submask windows decays. A Walsh/Fourier
  coefficient bound on h suffices to prove it.
status: open
next: >
  (a) tool_builder: compute σ²_N empirically up to the oracle ceiling with
  negative controls — random h gives σ²_N ≈ 1/n → 0 trivially (healthy),
  all-ones h gives σ²_N ≈ 0 but μ_N → 0 (vacuously concentrated at the wrong
  mean) — to confirm the prime h is in the healthy class. (b) lean_prover:
  formalise the Chebyshev glue (pure, no number theory) so the only unproved
  input is the variance bound itself. (c) symbolic_math/theorem_prover: bound
  the submask-window autocorrelation of h — this is the named "second-moment
  or Walsh bound on h" of GOAL.md priority 2. ADVERSARIAL CAVEAT: this gap is
  sufficient but possibly not minimal — if ν₂(n)/n fluctuates on positive
  density yet stays ≥ c for some c, averaged SUPPLY holds while σ²_N fails to
  vanish. A refutation of G-var therefore does NOT refute averaged SUPPLY; it
  only forces the lower-tail (minimal) form of this gap.
```

## Why this decomposition, and what it is not

The two existing skeletons and this one partition the three named realistic
targets (problem.md results 3, 4, 5) without overlap: the pointwise character
sum, the equivalence, and the averaged second moment. This one is the cheapest
to *refute* (G-mean-linear is one oracle run with two negative controls), which
is why GOAL.md lists it first: if the averaged route is dead, it dies before
the run spends anything on G-var.
