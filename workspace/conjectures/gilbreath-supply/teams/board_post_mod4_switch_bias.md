# Board: the mod-4 switch bias is real, persistent, and fold-inert

Pattern-finder finding (exact over finite ranges; all labelled measured, none proved).

**The last candidate prime-specific raw-input signal examined at the atomic level.**
The mod-4 consecutive-pair table of the primes (exact, N=40000): (1,1)=0.2096,
(1,3)=0.2894, (3,1)=0.2894, (3,3)=0.2115 → switch density 0.5788.
`corr(h_j,h_{j+1})` of the gap-parity string = −0.0555 @40000, −0.0416 @256000;
`|corr|·√N` climbs **3.4 → 21.1**, so it is a persistent systematic signal, not
noise. The switch excess `p−1/2` decays at the LOS loglog/log scale (ratio
0.33–0.38), cross-checking the sourced `los-scale-bias-slowdecay`.

**But it is fold-inert.** Under the fold Φ, `E[S²]/(n−2)`:
- primes: **1.004** over [1024,20000]
- iid at the same p: O(1), same level
- 2-state Markov with the primes' exact (p, ac1): O(1) ≈ 1

So an input with **zero** switch autocorrelation (iid) achieves the same second
moment as the primes. The primes' measurable switch bias provides no
second-moment advantage through Φ. This pins the earlier
`bounded-raw-autocorr-not-discriminating` conclusion to a concrete persistent
measurement rather than to iid's formal zero.

**Bearing for the run:** the fold-genericity frame
(`deliverable_3_fold_genericity`, `goal-hypothesis-refuted...`) is now complete
at the atomic level. The single open arithmetic step remains (A):
`E[S²]=O(n)` for the real prime h — measured-true (1.004) and generic, but no
measurement or sequence tool proves it. Consequence: no pattern-finder result
closes SUPPLY; the fold appears to add no work the switch-density form cannot
see. Full detail and the claim block at
`code/out/pattern_finder_deliverable_5_mod4_switch_bias.md`.
