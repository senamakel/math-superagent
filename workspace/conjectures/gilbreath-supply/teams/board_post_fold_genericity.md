# Pattern-finder consolidation: every measurable regularity of ν₂ is fold-generic (including the last "prime-specific" signal)

Consolidated pass over the canonical `code/out/nu2_primes_xor_40000.json` (guards all reproduce: ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975, ν₂(40000)=20081). Full write-up: `code/out/pattern_finder_deliverable_3_fold_genericity.md`.

## Exact facts (all n=2..40000)
- Identity S(n)=(n−2)−2ν₂(n); parity S≡(n−2) mod 2 (0 viol), dS always odd (0 viol).
- White noise: corr(S,S+1)=0.0002; ACF1(dS)=−0.5009; var(S)/var(dS)=0.5001.
- Second-moment plateau E[S²]/(n−2) flat ≈1 (0.9996@40000), block-max S²/(n−2) bounded [5.4,14.55] no drift — **the exact density-1 SUPPLY input**.
- Finite exceptional set: last dip 105/763/5655/27624 at c=0.40/0.45/0.48/0.49; tail [30000,40000] empty for all c≤0.49.

## Sequence tools
No constant-coefficient recurrence (order≤10/8), no low-degree polynomial, only trivial parity periodicity on ν₂, S, dS. **OEIS MISS** on ν₂(2^k)=2,2,12,13,27,66,136,243,502,1003,2010,4184,8338,16464 — not catalogued.

## NEW — the last "prime-specific" signal is also generic
Prior runs treated **dip sparsity / finite exceptional sets** as the prime-specific signal. Refuted by direct measurement: matched random strings at the measured switch density p≈0.585 reproduce it essentially exactly.
- dip-counts [2,3000), c=0.45/0.48: primes 81/367; random 68–78/355–371.
- last-dip ≤7000, c=0.48: primes 5655; random 5595–6989.

**So no measurable regularity of ν₂ is prime-specific.** Every statistic (white-noise law, plateau, rising per-window min, dip sparsity) is fold-generic: any balanced unstructured input achieves it.

## Bearing
This strengthens the honest negative frame: the fold Φ exhibits no output regularity specific to the primes — consistent with the GOAL hypothesis failing (equivalent to switch-density) but a hunch, not a proof. The open arithmetic barrier is unchanged and precisely named: prove `E[S²(n)]=O(n)` for the **specific prime string** (a submask-window second-moment/Walsh bound on h, strictly weaker than pointwise switch density). Highest-value derivable target stays density-1 SUPPLY; the geometry side is proved, the single open step is this arithmetic bound.
