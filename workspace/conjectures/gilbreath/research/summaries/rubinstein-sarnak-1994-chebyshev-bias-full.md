# Rubinstein & Sarnak 1994, "Chebyshev's Bias" (Exp. Math. 3.3:173–197)

<!-- source: https://projecteuclid.org/euclid.em/1048515870 | full text at research/sources/rubinstein-sarnak-1994-chebyshev-bias-full.full.md -->

## What it establishes (anchored to the paper)

- **The object is logarithmic density.** The usual (natural) densities of the
  leadership sets P_{q;a1,…,ar} = {x : π(x;q,a1) > … > π(x;q,ar)} do **not**
  exist; the logarithmic density
  ρ(P) = lim_{X→∞}(1/log X)∫_{P∩[2,X]} dt/t is the right measure (§1, after
  Wintner 1941).
- **Theorem 1.1 (GRH).** E_{q;a1…ar}(x) = (log x/√x)(φ(q)π(x;q,aj) − π(x)) has a
  limiting distribution. So the race is probabilistically well-defined, but
  only with GRH.
- **Theorem 1.2 (GRH).** Tails are exponentially localized with a double-
  exponential lower bound: ρ(B_R) ≤ c₁exp(−c₂√R), ρ(B⁻_R) ≥ c₃exp(−exp c₄ R).
- **Theorem 1.3 / §4 (GRH + GSH).** Explicit computation:
  ρ(P_{4,3,1}) ≈ 0.9959, ρ(P_{3,2,1}) ≈ 0.9990, ρ(P_{5})≈0.9954,
  ρ(P_7)≈0.9782, ρ(P_11)≈0.9167, ρ(P_13)≈0.9443. Strong single-sided bias at
  small modulus.
- **Littlewood-type oscillation (unconditional, §1).** P_{4,1,3} and P_{4,3,1}
  both extend to infinity — π(x;4,3) − π(x;4,1) changes sign infinitely often
  (Littlewood 1914). **No one-sided "primes ≡ 3 mod 4 lead" inequality holds
  unconditionally.**
- **Theorem 1.4 (GRH+GSH).** symmetric (unbiased) iff r=2 with c(q;a1)=c(q;a2)
  or the r=3 congruence condition. **Theorem 1.5/1.6:** the bias dissolves as
  q→∞ (ρ(P)→1/r!); a central limit theorem holds.

## What this means for the ν_2 supply route (the honest consequence)

The mod-4 bias is **real but conditional and oscillating**. So a one-sided,
unconditional forcing of the consecutive-pair mod-4 switch rate
(bit_n = [p_{n+1} ≢ p_n mod 4]) is unavailable. Only the **logarithmic
density** of leadership exists, under GRH+GSH, and it is strictly between 0
and 1. Therefore the ν_2 supply can be a *fluctuation* statement at best
without conditioning on unproved L-function hypotheses — it is a two-point
statistic at Hardy–Littlewood / Lemke Oliver–Soundararajan level, never a
PNT-in-AP one-point cancellation. This **confirms** the adopted approach's
falsifier and the existing claim `los-2016-consecutive-pair-mod4-bias`.

```claim
id: rubinstein-sarnak-bias-oscillates-unconditional-false
statement: Under GRH+GSH the mod-4 prime race has explicit limiting distribution with logarithmic densities ρ(P_{4,3,1})≈0.9959; but the bias oscillates (Littlewood 1914), so no one-sided unconditional inequality "primes ≡ 3 mod 4 lead" holds, and leadership density is strictly between 0 and 1.
hypotheses: primes in residue classes mod 4 mod any q; GRH and (for explicit values) GSH/LI for Dirichlet L-zeros; oscillation unconditional.
holds-here: yes (primes; mod-4 two-point statistic underpinning Granville's ν_2)
status: proved (for what it asserts); the GRH+GSH values are asserted/conditional
bearing: caps Route B's supply side: ν_2 ≥ c·n can only be a fluctuation bound (Hardy–Littlewood / LOS level), never a one-sided density assertion.
anchor: research/sources/rubinstein-sarnak-1994-chebyshev-bias-full.full.md
answers: supply-one-sided-vs-fluctuation
contradicts: (any earlier claim that a one-sided mod-4 bias forces ν₂ — none on disk)
```
