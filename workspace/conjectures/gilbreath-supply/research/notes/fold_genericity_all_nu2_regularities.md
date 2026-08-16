# Fold-genericity of every measurable ν₂ regularity (incl. dip sparsity)

Consolidated by pattern_finder over the canonical
`code/out/nu2_primes_xor_40000.json` (guards ν₂(53)=18, ν₂(64)=27,
ν₂(4000)=1975, ν₂(40000)=20081 all reproduce). Full write-up:
`code/out/pattern_finder_deliverable_3_fold_genericity.md`.

```claim
id: fold-genericity-all-nu2-regularities-incl-dip-sparsity
statement: >
  Every measurable regularity of nu2(n) for the prime gap-parity fold is
  fold-generic, not prime-specific. (1) White-noise law: corr(S(n),S(n+1))
  = 0.0002, ACF1(dS) = -0.5009, var(S)/var(dS) = 0.5001 on n=2..40000.
  (2) Second-moment plateau E[S^2]/(n-2) flat ~1 (0.9996@40000; per-
  doubling-block max S^2/(n-2) in [5.4,14.55], no upward drift) -- the exact
  input from which density-1 SUPPLY follows by Chebyshev. (3) Finite
  exceptional set {n:nu2/n<c}: last members 105/763/5655/27624 at
  c=0.40/0.45/0.48/0.49, tail [30000,40000] empty for all c<=0.49.
  (4) NEW: dip sparsity itself is reproduced by matched iid strings at the
  measured prime switch density p~0.585 (dip-counts [2,3000) at c=0.45/0.48:
  primes 81/367 vs random 68-78/355-371; last-dip <=7000 at c=0.48: primes
  5655 vs random 5595-6989). So no measurable regularity of nu2 is
  prime-specific; the primes sit in the generic-balanced-good class.
hypotheses: canonical floored fold, nu2(n)=wt(Phi_n h), S=(n-2)-2nu2 exact,
  canonical prime-h JSON guard-checked; random controls at measured switch
  density p~0.585 via exact submask-zeta fold.
holds-here: yes (measured; all statements exact over n=2..40000 and random
  trials <= 8000).
status: measured-not-proved -- every regularity is a conjecture for all n;
  nothing here proves density-1 SUPPLY or any arithmetic input specific to
  the primes.
bearing: >
  Strengthens the honest negative frame: the fold Phi exhibits no output
  regularity specific to the primes, consistent with the GOAL single-hypothesis
  failing (SUPPLY equivalent to switch density), but a hunch not a proof. The
  open arithmetic barrier is unchanged and precisely named: prove
  E[S(n)^2]=O(n) for the specific prime string h (a submask-window
  second-moment / Walsh bound, strictly weaker than pointwise switch
  density), with the geometry side already proved
  (fold-distance-enumerator-On).
anchor: research/notes/fold_genericity_all_nu2_regularities.md
```

The sequence tools (find_linear_recurrence order<=10/8, analyze_sequence)
find **no** constant-coefficient linear recurrence, no low-degree polynomial,
and only trivial parity periodicity on ν₂, S, dS. The dyadic subsequence
ν₂(2^k)=2,2,12,13,27,66,136,243,502,1003,2010,4184,8338,16464 is an **OEIS
MISS** (uncatalogued). No closed form to look up; the structure must come from
the problem.
