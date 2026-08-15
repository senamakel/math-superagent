# Switch-count conservation identity (G-supply reframing)

**Scholar, 2026.** A pure counting identity that reframes the G-supply open
problem. Established by counting — no computation is needed, but a numeric
confirmation script is provided (`code/out/check_switch_conservation.py`,
not executed this run).

## Statement

Let the primes be labeled by residue mod 4, and for primes ≤ x define

    N_switch(x)   = #{consecutive pairs p<q≤x : q ≢ p (mod 4)}   (= the mod-4
                     switch count = #\{gap ≡ 2 mod 4\} = the atomic bit count
                     feeding Granville's ν₂)
    N_nonswitch(x) = #{consecutive pairs p<q≤x : q ≡ p (mod 4)}  (equal-residue)

Then for every x:

    N_switch(x) + N_nonswitch(x) = π(x) − 1.

**Proof (counting, no hypotheses).** Every prime p ≤ x except the largest is
the first element of exactly one consecutive pair (p, next(p)). Split those
pairs by the residue of p: the pairs starting at a 1-mod-4 prime are the
disjoint union (1,1) and (1,3); those starting at a 3-mod-4 prime are (3,3)
and (3,1). Adding all four gives the total number of consecutive pairs,
π(x) − 1. ∎

## What it does to G-supply

The G-supply demand is a positive-density lower bound on the switch count,
`N_switch(x) ≥ c·π(x)` (equivalently `ν₂ ≥ c·n`). The identity rewrites that
as **exactly an upper-bound-below-1 on the non-switch count**:

    N_switch ≥ c·π(x)  ⟺  N_nonswitch ≤ (1−c)·π(x).

So a lower bound on the switch count (the direction ν₂ needs) is *the same
statement* as an upper bound strictly below density 1 on the non-switch
(equal-residue consecutive-pair) count.

**Why the held unconditional results give nothing:** Ruzsa 2001 / Shiu 2000
/Martin et al. 2024 [231] are all **lower** bounds on the non-switch side
(`N_nonswitch ≫ x loglog x / log² x` via Maier's method). That is the *wrong
direction* — it pushes non-switch density *up* toward π(x), i.e. it pushes the
switch count *down*, and does not upper-bound non-switch below 1. No held
unconditional source upper-bounds `N_nonswitch` below density 1, which is why
no unconditional positive-density switch (ν₂) lower bound exists. This is the
two-point crux (`research/notes/g-supply-two-point-crux-settled.md`) seen from
the other side.

This confirms the `abgs-s9-verbatim-verified` / `abgs-2011-s9-mod4-switch-limit-open`
picture: the whole content of G-supply is a below-density-1 **upper** bound on
the equal-residue consecutive-pair frequency, which at Hardy–Littlewood level
behaves like π(x)/4 + bias per residue (LOS-2016), i.e. ~ π(x)/2 total — far
below 1, consistent with switch density ≈ 1/2. It is not necessary to prove
bias-above-half; proving the non-switch pair frequency stays below density 1
is exactly the supply bound.

## Falsifier / what would settle it

A source upper-bounding the equal-residue consecutive-pair count
`N_nonswitch(x) ≤ (1−c)·π(x)` for some fixed c > 0, unconditionally, would
immediately give `ν₂ ≥ c·n` and (with the re-derived Lemma 5.4) a conditional
GC. No such source is held. A source upper-bounding non-matching pairs below
density 1 on HALF the class (e.g. only (1,1)) would not suffice — both
equal-residue pairs must be bounded together, and the switch count also
receives (1,3)+(3,1), so the bound must hold for the joint pair distribution.

## Numeric confirmation (available, not run this run)

`code/out/check_switch_conservation.py` verifies `N_switch + N_nonswitch =
π(x) − 1` and prints the switch density at x = 100..1e6 using `sympy.primerange`.
It was written but **not executed** in this run; it is for a worker with
execution to confirm the identity numerically. The identity itself stands on
the counting proof.

```claim
id: switch-conservation-identity
statement: For the primes ≤ x labelled by residue mod 4, the mod-4 switch count (consecutive pairs q≢p mod 4, feeding Granville's nu2) and the equal-residue pair count satisfy N_switch(x) + N_nonswitch(x) = pi(x) − 1 for every x. Hence a positive-density lower bound on the switch count (G-supply, nu2 ≥ c·n) is exactly equivalent to an upper bound strictly below density 1 on the equal-residue consecutive-pair count N_nonswitch ≤ (1−c)·pi(x).
hypotheses: primes only; stable classification by first-prime residue (counting proof, no analytic hypotheses).
holds-here: yes
status: proved  (pure counting; every prime ≤ x except the largest is the first element of exactly one consecutive pair)
bearing: reframes G-supply as a below-density-1 upper bound on equal-residue consecutive pairs, explaining why the held Ruzsa/Shiu lower bounds on the non-switch side (the classical obstruction) give nothing to nu2 — they push in the wrong direction. No unconditional below-density-1 upper bound on N_nonswitch exists in the library (consistent with abgs-2011-s9-mod4-switch-limit-open).
anchor: research/notes/switch-conservation-identity.md
answers: none (reframes the open request; does not close it)
contradicts: none
```
