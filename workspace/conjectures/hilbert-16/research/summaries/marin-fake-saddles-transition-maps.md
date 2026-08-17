# Marín 2026 — Fake saddles and their transition maps

Full text: [[marin-fake-saddles-transition-maps.full]]. EJQTDE 2026, No. 5, 1–10;
doi:10.14232/ejqtde.2026.1.5. Open access (UAB DDD repository PDF fetched).
Received 22 Sep 2025, appeared 19 Mar 2026. Communicated by Armengol Gasull.

URL: https://ddd.uab.cat/pub/artpub/2026/327411/p11901.pdf

## What the paper is

A *fake saddle* is a degenerate singular point of a planar vector field with zero
linear part, exactly two separatrices contained in a smooth invariant curve that
separates two hyperbolic sectors (also "impassable grain"). Inside a degenerate
flow box near such a singularity, the phase portrait is parallel fibers, all but
one free of singular points, and the singular fiber has a semi-stable equilibrium.
There is a well-defined transition (Poincaré) map Πω_α between two transverse
sections Σα, Σω to the singular fiber, on both sides of it.

This paper characterizes the *generic* (non-zero second-order jet) fake saddles and
gives the first term of a **uniform** (in parameters µ) asymptotic expansion of the
transition map, determining whether the singular fiber is attractive or repulsive
on each side. It extends [Coll–Gasull–Prohens 2025, "The effect of a singularity on
transition maps", DCDS-S 18:4021-4039] (their [2]) from the case a=0 to general a.

## The set-up and normal form

The second-order-jet-nonzero fake saddle reduces, after rectifying the singular
fiber to y=0 and rescaling, to a smooth family

  Xµ = (x² f1 + a(µ)xy + y² f2)∂x + (x g1 + y g2(y)) y ∂y         (1.1)

with f1(0,0;µ)=f2(0,0;µ)=1, and invariants

  a(µ),  b(µ) := g2(0;µ),  c(µ) := g1(0,0;µ),
  d(µ) := 4(1 − c(µ)) − (a(µ) − b(µ))² .

This is the same normal-form family as De Maesschalck–Rebollo-Perdomo–Torregrosa
2015 (JDE 258:588–620) "Cyclicity of a fake saddle inside the quadratic vector
fields", which connects DIRECTLY to the DRR program: a fake saddle is one of the
degenerate singularities appearing in quadratic DRR graphics (the D-families at
infinity).

## Theorem 1.1 — characterization of a generic fake saddle

If (a,b,c) ∉ {d=0} ∩ {a²−b²=4}, then the origin is a fake saddle iff either
d>0, or c=1 and a=b. In the first case, after blowing up the origin there is a
single singular point on the exceptional divisor, a hyperbolic saddle of
hyperbolicity ratio 1−c>0; in the second, a semi-hyperbolic saddle.

The hypothesis cannot be dropped (Example 3.1: X3=(x+y)²∂x+y³∂y, invariants
(2,0,0)∈{d=0}∩{a²−b²=4}, is NOT a fake saddle — a saddle-node appears whose weak
separatrix is not the strict transform and meets the exceptional divisor
transversely; whereas X4=(x+y)²∂x+y⁴∂y IS a fake saddle). This **contradicts a
claim of Coll–Gasull–Prohens [2]** which asserted a necessary condition
(h0,1−a1,1)²+4(h1,0−1)<0 or h1,0=1 and h0,1=a1,1; X4 with d=4 refutes it.

## Theorem 1.2 — uniform asymptotic expansion of the transition map

Under d = 4(1−c) − (a−b)² > 0, the transition map satisfies

  Πω_α(y; µ) = e^{γ±(µ)} y  +  F^{K}_{1+ε}({d>0})   on ±y ≥ 0,

where F^K_L(W) is Marín–Villadelprat's flat class (functions flat to order L in the
unfolding variables), and

  γ±(µ) = PV∫_{α}^{ω} g1(x,0;µ)/(x f1(x,0;µ)) dx  ±  π(2b(µ) − c(µ)(a(µ)+b(µ)))/√d(µ).

The remainder term is o(y) **uniformly in µ** — the uniformity is what lets the
result address cyclicity problems, not just stability. The sign of γ± determines
whether y=0 is attractive/repulsive on the side ±y>0. For a=b=0 the two γ values
coincide with the principal value.

The proof blows up the origin; the two charts give hyperbolic saddles with
λ+λ−=1, uses the Marín–Villadelprat Dulac-map asymptotic (Theorem 2.1) and flat-class
calculus; γ0 is evaluated by an arctan identity, F≡−π.

## Application (section 3, family (3.1)) — a certified zero-cyclicity result

The family (monodromic for β>1/4 per Gasull–Mañosa–Mañosas [4], JDE 182:169–190)

  Zµ:  ẋ = βx²y + αxy² − βy³ − x⁴,  ẏ = 4βxy² + αy³ + 2x⁵,  µ=(α,β)

is put in normal form (1.1) with c=1/3, d=(2/3)(4−1/β)>0 iff β>1/4. The Poincaré
return map is the composition of two transition maps, giving

  γ(µ) = γ+(µ)+γ−(µ) = 2πα/(β√3),   R(x;µ) = e^{2πα/(β√3)} x + flat remainder.

For β>1/4 the origin is a center of Z(0,β) (reversible via (x,y,t)↦(−x,y,−t)).
Because the flat remainder F^∞_{1+ε} is uniform in µ and vanishes at α=0, the run
concludes with the division lemma [Marín–Villadelprat 2022, Lemma 4.1]:

  **cyclicity of the origin in family (3.1) is zero at every µ0=(α0,β0) with β0>1/4.**

This last assertion "can not be deduced from the results in [4] because they are
not uniform with respect to parameters." This is the cleanest worked example in the
library of the exact argument shape THIS run's method policy prefers: a uniform
flat-remainder expansion + division-in-a-flat-class → a KERNEL-CHEcKABLE finite
statement (no limit cycle near the origin). It is a concrete template for the
`division in flat class`/`Bautin trick` step that the Lu H14_3 and RR center-graphic
arguments use.

## Bibliographic note / surrounding work

- [2] B. Coll, A. Gasull, R. Prohens, "The effect of a singularity on transition maps",
  DCDS-S 18(2025) no.12, 4021–4039, doi:10.3934/dcdss.2025125 — the predecessor this
  paper extends and corrects.
- [3] De Maesschalck, Rebollo-Perdomo, Torregrosa, "Cyclicity of a fake saddle inside
  the quadratic vector fields", JDE 258(2015) 588–620, doi:10.1016/j.jde.2014.09.024 —
  proves cyclicity ≤ 2 (configurations (2:0),(1:1)) for a fake saddle in quadratic
  fields; the DRR-relevant companion.
- [5],[7] Marín–Villadelprat asymptotic expansion of Dulac map, general setting
  (JDE 275 (2021) 684–732) and coefficient properties (JDE 404 (2024) 43–107).
- [6] Marín–Villadelprat, "The criticality of reversible quadratic centers at the outer
  boundary of its period annulus", JDE 332 (2022) 123–201 — sources the division lemma.
- [4] Gasull, Mañosa, Mañosas, "Monodromy and stability of a class of degenerate planar
  critical points", JDE 182 (2002) 169–190.

## Evidence class

proved (peer-reviewed article, full text held, mathematics checked by reading the
proofs; not independently machine-verified in this run). The uniform-expansion
statement (Thm 1.2) and the zero-cyclicity application are the load-bearing claims.
