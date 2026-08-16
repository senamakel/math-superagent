# FINDINGS — uc-coupling scored search

**Status: the scorer now carries STEP 2 guards (ceiling clamp + degenerate-atom
floor + INVALID self-test). The high scores below are NOT believable and are
now rejected by the hardened scorer; only Yu's plateau at 0.3823435642
belongs.**

## Post-guard re-score (STEP 4, current truth)

After adding the ceiling clamp (T_HAT_MAX=0.3823455334 + slack 1e-6) and the
degenerate-atom floor (A_FLOOR/B_MINUS_A_FLOOR = 0.1), re-running every candidate
through the real harness `python3 score.py candidates/<id>.py`:

| id (family) | current | reading |
|---|---|---|
| c0000,c0001,c0002,c0005,c0006,c0007,c0009,c0016..c0023 | SCORE: 0.3823435642 | Yu witness block, believable |
| c0024..c0032 | INVALID (score > t_hat_max) | missing-inf artifact, rejected |
| c0033 | INVALID (degenerate-atom a=0.01 < floor) | small-a hole, rejected |
| c0003,c0008 | INVALID (no module-path params) | legacy in-module main() |
| c0004 | INVALID (no readable params) | diagnostic probe |
| c0010 | crash (malformed) | not a candidate |

STEP 1 verdict: the true inner-inf at t=0.38234, alpha=0.035 equals 1.00000889
(agreed by independent global search), but it is NOT certifiable by mpmath.iv
interval B&B in 10s (margin 8.9e-6, needs cell width ~4e-7 in 4 dims; B&B
stalls ~1100 splits in the 10s wall). That infeasibility is the blocker that
stops the scored search per the directive.

## Original finding (historical, pre-guard)

The scorer had a verification hole (missing inf over couplings). The high
scores below are NOT believable; they are an artifact of tuning a
non-minimizing coupling.

[original body follows]

## What was searched

Candidate = a two-atom symmetric coupling P_pq = (1−β)Q_{a1,a2} + β Q_{b1,b2},
parameters (alpha, a1, a2, b1, b2), β = (t−a)/(b−a), a=(a1+a2)/2, b=(b1+b2)/2.
The scorer computes g(P,α)/E h(p) over the t-grid and certifies the largest t
whose ratio ≥ 1. All scored candidates held b2=1, b1=a1=a2=a (Yu's certified
family shape), and swept alpha and a.

## The mathematical object (source-verified)

Yu eq (2): Γ(t) = sup_{P_ρ} inf_{P_p: Eh>0, Ep≤t} 𝔼_ρ[ inf_{P_pq ∈ C_s(P_p)} g(P_pq)/E h(p) ].

The certificate is Γ̂(t) = sup_α inf_{P_pq} g(P_pq,α)/E h(p). The **infimum over
the coupling space is part of the definition** — a certificate needs g(P,α)/Eh ≥ 1
to hold, in the worst case, over all admissible couplings, i.e. inf_P ≥ 1.

## The hole

The scorer evaluates g(P,α)/E h(p) for the **single coupling P fixed by the
candidate** (a1,a2,b1,b2), sweeping β with t. It never takes the inf over the
coupling space. For a single P:

    g(P,α)/E h(p)  ≥  inf_P g(P,α)/E h(p)   (upper bound, not lower)

so a candidate that is NOT the argmin coupling certifies an inflated ratio.
The certification direction is wrong: the scorer needs the argmin (smallest
ratio) to certify Γ̂(t) ≥ 1, but accepts whatever P the candidate supplies and
reports its ratio as if it were the certified density.

## Empirical demonstration (all inside Yu's two-atom class, b2=1, b1=a)

| id | alpha | a | b2 | certified t (scorer) |
|----|-------|---|----|-----------------------|
| c0009/c0016.. | 0.035..0.05 | 0.3300622 | 1.0 | 0.3823435642 |
| c0024 | 0.035 | 0.32 | 1.0 | 0.3823610000 |
| c0026 | 0.035 | 0.31 | 1.0 | 0.3824280000 |
| c0027 | 0.035 | 0.30 | 1.0 | 0.3825300000 |
| c0028 | 0.035 | 0.29 | 1.0 | 0.3826835000 |
| c0029 | 0.035 | 0.28 | 1.0 | 0.3828830000 |
| c0030 | 0.035 | 0.25 | 1.0 | 0.3838000000 |
| c0031 | 0.035 | 0.20 | 1.0 | 0.3859550000 |
| c0032 | 0.035 | 0.10 | 1.0 | 0.3937600000 |
| c0033 | 0.035 | 0.01 | 1.0 | 0.4219920000 |

The certified t climbs **monotonically as a → 0, past the proved ceiling
t̂_max ≈ 0.3823455 without any visible plateau.** That upward drift with no cap
is the missing-inf signature: as a moves away from Yu's argmin value (a≈0.33),
the single-coupling ratio g(P,α)/Eh rises without bound, and the scorer reports
it as a higher certified density. A true certificate (inf over P) is capped at
t̂_max by the proved non-increasing Γ̂.

## The BELIEVABLE result

Only the **Yu certified witness itself** (a = 0.3300622, b2 = 1, α ∈ [0.03,0.05])
is believable as a certified density: the scorer reproduces 0.3823435642 there,
consistently with Yu's published 0.38234 (Γ̂(0.38234) = 1.00000889) and with
Cambie's ceiling t̂_max = 0.3823455333667. That point is (near) the argmin
coupling, so its single-coupling ratio is (near) the true inf. The score is
grid-limited by the N=20000 t-scan: over (a, 0.5] step ≈ 8.5e-6, so the
certified t sits ~1 grid step below the true boundary.

## Binding constraint at the believable plateau

At the Yu witness, the binding constraint is the **t itself** (the
`Gamma_hat(t) >= 1` boundary / t structural ceiling): Γ̂(t) ≥ 1 holds up to
t̂_max ≈ 0.3823455 and fails beyond. This matches the proved monotonicity.

## On the exploited runs

Scores 0.3824 → 0.422 are **not believed**. They do not falsify the Γ̂
monotonicity proof; they expose that this scorer does not take the required
inf over couplings. 0.5 would be the same exploit continuing, not a proof of
Frankl.

## Would-be next step (if the scorer were fixed)

To make the certificate valid, score.py must take the inf over the coupling
space for each t (e.g. an SLSQP/exact minimization over (a1,a2,b1,b2) of
g(P,α)/Eh at fixed α,t), then certify t when that inf ≥ 1. That is the
`yu-gamma-hat-nonincreasing`/`yugamma_global_sup` optimization the run already
carries numerically. As written, the single-coupling scorer is a search that
will always "improve" by moving the coupling away from the argmin.
