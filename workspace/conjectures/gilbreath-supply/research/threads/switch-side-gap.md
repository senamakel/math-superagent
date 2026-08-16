# The switch-side gap: what every source converges on, and what it means for the fold

Digest synthesis across the reference library, on the arithmetic input the
switch-density reduction of SUPPLY would need.

```thread
id: switch-side-gap
question: Is there a provable arithmetic input on the prime gap-parity string h that is
  strictly weaker than positive mod-4 switch density and still forces wt(Φ_n h) ≥ c·n ?
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: abgs-p1-wide-open, lau-nonconstant-pattern-open, los-switch-preferred-mod4,
  maynard-positive-density-congruent-strings, shiu-string-theorem, abgs-mod4-nonuniform-measured
blocked-by: no single theorem closes it; every source confirms the switch (differing-pair)
  side is the one unknown.
next: (1) the only candidates priced for a weaker input are in REQUESTS.md
  (walsh-spectral-subset-b904) and GOAL.md priority 2 (bounded autocorrelation, variance/
  second-moment, Walsh coefficient, submask-XOR input); (2) the fold machinery (Bacher,
  Szechtman, Rampersad-Wiebe) is the lever, not the frequency.
```

## The convergence (all sources, same picture)

1. **The switch (differing-pair) side is open and L-function-inaccessible.**
   ABGS (2011 §1): the pair-frequency Problem 1.1 "is wide open, and cannot be
   treated using L-functions". Lau (2024): even a *single* non-constant pattern of
   length m (in particular mod-4 (1,3)/(3,1)) is not known to occur infinitely
   often. This is precisely the input the switch-density reduction needs.

2. **The equal (constant-pair) side is fully understood — and is the wrong
   direction.** Shiu (2000): arbitrarily long strings of consecutive primes ≡ a
   (mod q), for mod 4 giving arbitrarily long all-zero runs in h. Maynard (2016
   Thm 3.3): positive density of such strings, unconditionally for q=4. Freiberg:
   short-gap equal pairs. So every *equal-residue* statement is proved; none helps
   SUPPLY, because the reduction needs the differing side.

3. **The switch side is conjecturally the *preferred* side.** LOS (2016 Conj 1.2):
   for mod 4, differing pairs (a,−a) exceed equal (a,a) for ALL x ≥ 5, with
   difference ~ (x/4)(log x)^{-2} log(2πq/log x). ABGS's measured data agree
   (switch 57.5% over 10^3..10^6, ratio 1.353). So the heuristic points to switch
   density ≥ ~1/2 — but it is a conjecture, not a theorem.

4. **The single-residue race is already oscillatory/positive-density** (Rubinstein-
   Sarnak under GRH+GSH; Littlewood switches infinitely often), so the pair race is
   a strict generalisation and there is no easy averaging.

## What this means for the fold attack

None of the sources proves the switch-density input. Therefore the reduction of
SUPPLY to positive switch density is a dead end (as ORIGINAL.md says), and the
live question is whether `Φ` can force `wt(Φ_n h) ≥ c·n` from a *weaker* input the
sources do not rule out. The candidates (GOAL 2) are all statements about `h`
along the binary-submask coordinates Lucas makes Φ read — bounded autocorrelation,
a variance/second-moment bound, a Walsh-coefficient bound, or a submask-XOR input.
The fold machinery (Lucas submask, Bacher LU/recurrence-block structure,
Szechtman cancellations, Rampersad-Wiebe 2-regularity) is the natural lever for
those, and none of the five closed doors touches an averaged/weak-input theorem.
