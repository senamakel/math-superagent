# Summary — Strings of Congruent Primes in Short Intervals

Source: Tristan Freiberg, arXiv:1005.4703 (2011).
Full text: `research/sources/freiberg_strings_short_intervals.full.md`
Source URL: https://arxiv.org/pdf/1005.4703

## What this source establishes

Hybrid of Shiu's string method and Goldston–Pintz–Yıldırım small-gap method.
Main theorem: fix q ≥ 3, (q,a)=1, and ε > 0. There are infinitely many pairs of
consecutive primes p_r, p_{r+1} with p_r ≡ p_{r+1} ≡ a (mod q) and
**p_{r+1} − p_r < ε log p_r** — i.e. infinitely many *short* gaps where both
primes share the residue class a mod q.

For q=4, a=1,3: infinitely many short-gap equal-residue pairs. This strengthens
the equal side: not only do equal-residue consecutive pairs occur infinitely
often (Shiu), they occur with gaps < ε log p — i.e. they occur "in short
intervals", at the density scale of typical small gaps.

## Why it matters for SUPPLY

This is the strongest known bound on the *equal*-residue side of the mod-4 pair
distribution. SUPPLY's switch-density reduction needs the *differing*-residue
side (1,3)/(3,1) to have positive frequency; equal-residue results (Shiu,
Freiberg) are the opposite direction and don't help. But it does establish that
the equal-residue pairs are dense in the small-gap sense, which is the
counter-structure to anything that would say "equal pairs are so rare that
switch density is forced small by structural reasons." It bounds the wrong side,
confirming the reduction dead-end.

## Evidence class

Proved theorem (conditional on standard machinery used in the proof).

```claim
id: freiberg-short-equal-residue-pairs
statement: For q ≥ 3, (q,a)=1, ε>0, infinitely many consecutive-prime pairs p_r,p_{r+1}
  with both ≡ a (mod q) and gap < ε log p_r.
hypotheses: q ≥ 3, (q,a)=1.
holds-here: true for q=4, a=1,3 — the equal-residue side is known even in short intervals.
status: proved (Freiberg 2011).
bearing: the equal side of mod-4 pairs is well understood (infinitely many, in short
  intervals); the differing side needed for switch density is not. Reinforces that the
  reduction is a dead end and the fold is the right attack.
anchor: Freiberg 2011, Theorem 1.1.
```
