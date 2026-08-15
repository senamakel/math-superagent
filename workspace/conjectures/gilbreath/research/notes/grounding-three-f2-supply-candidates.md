# Grounding round: three F₂-supply candidates, all refuted on the same structural fact

## Task
Take the three candidates targeting the single open step of Route B — the supply
bound ν₂(q_n) = wt(Φ_n h) ≥ c·w — to the literature and to the run's own checked
linear algebra.

## The load-bearing object
Φ_n is the F₂ Pascal/Rule-90 fold: rows k=2..n−2, cols j=2..n−1, entry
C(k−1, j−(n−k)) mod 2. h is the mod-4 switch bit over [2,n−1], w=wt(h). ν₂ =
wt(Φ_n h).

Run's checked claim `transfer-matrix-kernel-allones`: **rank Φ_n = n−3, nullity 1,
kernel = span(all-ones)** for every n=2..20 (exact F₂ Gaussian elimination +
Pascal-row-sum parity proof). Hand-verified here at n=5 (rank 2 = n−3, kernel
span(1,1,1)).

## The decisive consequence
Φ_n has n−3 rows and n−2 columns and rank n−3 — so it has **full row rank**.
Therefore **im(Φ_n) = F₂^{n−3}, the entire output space**. Three consequences,
killing all three candidates:

1. The image code C_n = im(Φ_n) has **d_min = 1** trivially. The Delsarte/
   MacWilliams/Krawtchouk minimum-distance machinery has nothing to certify: a
   full-space code has no minimum-distance constraint. Candidate 1's premise is
   false — ν₂ ≥ c·w is NOT a code minimum distance.
2. The kernel is a **single vector** (all-ones), not the "dyadic-periodic
   subspace" candidates 1–3 assume. There is no dyadic-characters/period-2^m
   structure to project h onto. The collapse direction is ONE codimension.
3. An F₂ uncertainty principle (Donoho–Stark etc.) bounds a product/sum of the
   function with its **Fourier transform**, never the image weight under a
   *surjective* linear fold; the all-ones h has wt(h)=n−2 maximal yet wt(Φ_n h)=0.
   Candidate 2's mechanism cannot fire.

## Candidate 3 fails a second, independent way
Even setting the linear algebra aside, the ergodic mechanism is wrong: **positive
entropy alone does NOT force disjointness from the odometer**. The 2-adic
odometer is zero-entropy, rigid, equicontinuous. The correct sufficient classes
are ZE^⊥ = K-automorphisms and Mild-mixing ⟂ Rigid (Furstenberg 1967;
Lemańczyk–Parreau–Thouvenot; Furstenberg–Weiss; Berk–Górska–de la Rue ETDS 2024).
So the honest hypothesis would be mild mixing / "odometer not a factor", a deep
number-theoretic claim about the prime bit — not the clean bit-string property
the candidate wants.

## What survives (the real content)
The empirically meaningful object — min_{h∈{primes}} ν₂/w ≈ 0.515–0.87 — is
**case (b) prime-specific** (per `g-supply-transfer-refuted` and
`g-supply-transfer-measured`). It is NOT recoverable from any universal
F₂/code/ergodic inequality; any supply lower bound must carry the two-point
mod-4 correlation content, whose unconditional form is named-open
(`abgs-2011-s9-mod4-switch-limit-open`). The refined target
min_{h∉ker} wt(Φ_n h)/wt(h) of candidate 1 is thinner than d_min but still
fails to be a uniform constant (the all-ones family shows relative expansion = 0
asymptotically).

## Verdicts
- `nu2-code-minimum-distance`: **refuted** (killed-by `transfer-matrix-kernel-allones`: image is full space, d_min=1).
- `f2-uncertainty-dyadic-spectral-mass`: **refuted** (kernel is one vector, not dyadic; uncertainty principle can't bound a surjective fold's image weight).
- `odometer-disjointness-subshift`: **refuted** (positive entropy ⟹ disjoint from odometer is false; the correct hypothesis is mild mixing / K, which is as deep as the two-point prime correlation).
- All three carry `precedent` = the real named mathematics (Delsarte LP,
  MacWilliams, Donoho–Stark, Furstenberg disjointness) with source URLs, and the
  explicit statement that none is applied to Gilbreath (consistent with
  `block-growth-literature-not-covered`).

## Sources consulted (URLs)
- On Delsarte's Linear Programming Bounds for Binary Codes, FOCS 2005, doi:10.1109/SFCS.2005.55
- New Solutions to Delsarte's Dual Linear Programs, IEEE-IT 2024, doi:10.1109/TIT.2024.3476974
- J. MacWilliams & N. J. A. Sloane, The Theory of Error-Correcting Codes (1977)
- Matusiak–Przebinda, The Donoho–Stark uncertainty principle for a finite abelian group, doi:S0195669804001453 / AMUC 73 (2004)
- Feng–Hollmann–Xiang, The shift bound for abelian codes and generalizations of the Donoho–Stark uncertainty principle, arXiv:1804.00367
- Furstenberg, Disjointness in ergodic theory, Math. Systems Theory 1 (1967)
- Berk–Górska–de la Rue, Joining properties of automorphisms disjoint with all ergodic systems, ETDS 2024, doi:10.1017/etds.2024.129
- Moreira, Disjointness for measurably distal group actions, ETDS 2022

These were used to confirm the named mechanisms exist and their precise
hypotheses; none was found applied to Gilbreath, confirming the open step is
unclaimed.
