# G-mean-linear: computational grounding

```claim
id: g-mean-linear-grounded-prime
statement: >
  For the real prime gap-parity string h (h[j]=[q_{j+2}!=q_{j+1} mod 4]), the
  averaged mean M(N) = (1/N) Σ_{n=2..N} ν₂(n)/n with ν₂(n)=#{d in [2,n-1] :
  T(n,d)=1} satisfies M(500)≈0.483, M(1000)≈0.491, M(2000)≈0.495, M(4000)≈0.497,
  M(8000)≈0.499 across the computed range, bounded below and non-decreasing
  past the small-n transient. This is the averaged analogue of SUPPLY's
  conclusion, measured, NOT a proof.
hypotheses: >
  d-range convention [2,n-1] pinned by reproducing nu2(4000)/4000 = 0.4938 vs
  the problem.md literature value 0.4933 (d in [0,n-2] gives 0.4940; both
  reproduce it, [2,n-1] matches the documented suffix-floored-at-index-2).
  nu2 computed by the submask-product SOS transform, verified equal to the
  s_direct oracle on n=8..60.
holds-here: yes
status: checked
bearing: >
  Grounds gap G-mean-linear (research/backward/supply-averaged-second-moment.md):
  the averaged form is empirically healthy, so the averaged route is not dead
  at trivial cost. The honest remaining content of G-mean-linear is proving a
  positive lower bound from an arithmetic input, not measurement.
anchor: code/out/averaged_mean_capture.txt
```

```claim
id: negative-controls-prime-specific
statement: >
  The bound in M(N) is specific to the prime h: for the all-ones vector (the
  kernel of the fold, Φ_n(1)=0) M(N)=0.0000 at every N up to 8000, and for
  Thue-Morse h (aperiodic but sublinear fold) M(N) decays 0.226 (N=100) to
  0.049 (N=8000) with nu2(N)/N falling 0.140 to 0.003. So neither "high
  weight" (all-ones) nor "aperiodicity" (Thue-Morse) reproduces the signal;
  it is specific to the prime input.
hypotheses: same fold, same d-range [2,n-1], same SOS transform and oracle
  verification as above.
holds-here: yes
status: checked
bearing: >
  Re-confirms two of problem.md's five closed doors (weight alone #1,
  aperiodicity #3) against the averaged form and shows G-mean-linear is not
  an artifact of the fold being generically heavy.
anchor: code/out/averaged_mean_capture.txt
```

Caveat recorded: the literature bracket ν₂/n ∈ [0.42,0.52] over n=50..3999 is
slightly optimistic at tiny n — our exact computation finds n=53 at 0.34 and a
min of 0.416 over [200,500) at n=274 — but neither the mean nor the tail is
affected (min over [500,1000) is 0.443, over [1000,2000) 0.460).
